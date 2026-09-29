import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.nio.charset.StandardCharsets;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.List;
import java.util.Scanner;

public class AuctionClient {
    public static final String DEFAULT_HOST = "localhost";
    public static final int DEFAULT_RMI_PORT = 1099;
    public static final String SERVICE_NAME = "AuctionService";

    public static void main(String[] args) {
        String host = DEFAULT_HOST;
        int rmiPort = DEFAULT_RMI_PORT;
        String username = null;

        String envHost = System.getenv("SERVER_HOST");
        if (envHost != null && !envHost.trim().isEmpty()) {
            host = envHost.trim();
        }

        String envRmiHost = System.getenv("RMI_HOST");
        if (envRmiHost != null && !envRmiHost.trim().isEmpty()) {
            host = envRmiHost.trim();
        }

        String envRmiPort = System.getenv("RMI_PORT");
        if (envRmiPort != null && !envRmiPort.trim().isEmpty()) {
            try {
                rmiPort = Integer.parseInt(envRmiPort.trim());
            } catch (NumberFormatException ignored) {}
        }

        String envUser = System.getenv("AUCTION_USER");
        if (envUser != null && !envUser.trim().isEmpty()) {
            username = envUser.trim();
        }

        if (args.length > 0 && !args[0].trim().isEmpty()) {
            host = args[0].trim();
        }
        if (args.length > 1 && !args[1].trim().isEmpty()) {
            try {
                rmiPort = Integer.parseInt(args[1].trim());
            } catch (NumberFormatException ignored) {}
        }
        if (args.length > 2 && !args[2].trim().isEmpty()) {
            username = args[2].trim();
        }

        Scanner scanner = new Scanner(System.in, StandardCharsets.UTF_8);

        if (username == null || username.trim().isEmpty()) {
            System.out.println("==================================================");
            System.out.println("       HE THONG DAU GIA PHAN TAN - CLIENT         ");
            System.out.println("==================================================");
            System.out.print("Nhap ten nguoi tham gia (Username): ");
            username = scanner.nextLine().trim();
            if (username.isEmpty()) {
                username = "User_" + System.currentTimeMillis() % 1000;
            }
        }

        System.out.println("[CLIENT] Dang ket noi RMI toi " + host + ":" + rmiPort + "...");

        try {
            Registry registry = LocateRegistry.getRegistry(host, rmiPort);
            AuctionService service = (AuctionService) registry.lookup(SERVICE_NAME);
            service.registerUser(username);

            int socketPort = service.getSocketPort();
            System.out.println("[CLIENT] Dang mo Socket TCP toi " + host + ":" + socketPort + " de nhan tin tuc truc tiep...");

            Socket socket = new Socket(host, socketPort);
            PrintWriter socketWriter = new PrintWriter(socket.getOutputStream(), true, StandardCharsets.UTF_8);

            Thread socketReaderThread = new Thread(() -> {
                try (BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream(), StandardCharsets.UTF_8))) {
                    String msg;
                    while ((msg = reader.readLine()) != null) {
                        System.out.println("\n>>> " + msg);
                        System.out.print("> ");
                    }
                } catch (Exception ignored) {
                } finally {
                    System.out.println("\n[CLIENT] Kenh Socket TCP da dong.");
                }
            });
            socketReaderThread.setDaemon(true);
            socketReaderThread.start();

            System.out.println("[CLIENT] Ket noi RMI va Socket TCP thanh cong! Chuc mung " + username + "!");

            boolean running = true;
            while (running) {
                System.out.println("\n--------------------------------------------------");
                System.out.println("MENU CHUC NANG DAU GIA:");
                System.out.println("1. Xem danh sach san pham & phien dau gia (RMI)");
                System.out.println("2. Dat gia san pham (RMI -> Phat song Socket TCP)");
                System.out.println("3. Xem danh sach nguoi tham gia (RMI)");
                System.out.println("4. Xem chi tiet 1 san pham (RMI)");
                System.out.println("0. Thoat");
                System.out.println("--------------------------------------------------");
                System.out.print("Chon thao tac (0-4): ");

                String choice = scanner.nextLine().trim();
                switch (choice) {
                    case "1":
                        List<AuctionItem> items = service.getItems();
                        System.out.println("\n=== DANH SACH SAN PHAM DANG DAU GIA ===");
                        for (AuctionItem item : items) {
                            System.out.println("  " + item.toString());
                        }
                        break;

                    case "2":
                        System.out.print("Nhap Ma san pham muon dat gia (vd: SP01): ");
                        String bidItemId = scanner.nextLine().trim().toUpperCase();
                        AuctionItem targetItem = service.getItem(bidItemId);
                        if (targetItem == null) {
                            System.out.println("[-] San pham khong ton tai!");
                            break;
                        }
                        System.out.println("San pham: " + targetItem.getName() + " | Gia hien tai: " + String.format("%,.0f VND", targetItem.getCurrentPrice()));
                        System.out.print("Nhap muc gia dat moi (phai lon hon gia hien tai): ");
                        String priceInput = scanner.nextLine().trim();
                        try {
                            double newPrice = Double.parseDouble(priceInput);
                            boolean ok = service.placeBid(bidItemId, username, newPrice);
                            if (ok) {
                                System.out.println("[+] DAT GIA THANH CONG! He thong da cap nhat gia moi.");
                            } else {
                                System.out.println("[-] DAT GIA THAT BAI! Muc gia cua ban phai lon hon gia hien tai.");
                            }
                        } catch (NumberFormatException e) {
                            System.out.println("[-] Muc gia nhap vao khong dung dinh dang so!");
                        }
                        break;

                    case "3":
                        List<String> users = service.getParticipants();
                        System.out.println("\n=== DANH SACH NGUOI DANG THAM GIA ===");
                        for (String u : users) {
                            System.out.println("  - " + u);
                        }
                        break;

                    case "4":
                        System.out.print("Nhap Ma san pham can xem: ");
                        String detailId = scanner.nextLine().trim().toUpperCase();
                        AuctionItem detail = service.getItem(detailId);
                        if (detail != null) {
                            System.out.println("\n" + detail.toString());
                        } else {
                            System.out.println("[-] Khong tim thay san pham!");
                        }
                        break;

                    case "0":
                    case "exit":
                    case "quit":
                        System.out.println("[CLIENT] Dang thoat khoi he thong...");
                        socketWriter.println("exit");
                        running = false;
                        break;

                    default:
                        System.out.println("[-] Lua chon khong hop le, vui long chon lai!");
                        break;
                }
            }

            socket.close();
        } catch (Exception e) {
            System.err.println("[CLIENT ERROR] Khong the ket noi toi Server: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
