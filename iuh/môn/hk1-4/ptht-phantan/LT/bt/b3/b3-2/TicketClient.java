import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.charset.StandardCharsets;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class TicketClient {
    public static final String SERVER_HOST = "localhost";
    public static final int RMI_PORT = 1099;
    public static final String SERVICE_NAME = "TicketService";

    private static ServerSocket invoiceServerSocket;
    private static int clientListeningPort;
    private static volatile boolean running = true;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String serverHost = (args.length > 0) ? args[0] : SERVER_HOST;

        try {
            // 1. Khoi tao ServerSocket tren mot cong ngau nhien de nhan hoa don tu Server qua TCP
            invoiceServerSocket = new ServerSocket(0);
            clientListeningPort = invoiceServerSocket.getLocalPort();

            // 2. Chay luong (Thread) nen de lang nghe hoa don tu Server
            Thread invoiceReceiverThread = new Thread(new Runnable() {
                @Override
                public void run() {
                    listenForInvoices();
                }
            });
            invoiceReceiverThread.setDaemon(true);
            invoiceReceiverThread.start();

            System.out.println("====================================================================");
            System.out.println("            HE THONG DAT VE XE TRUC TUYEN (CLIENT RMI)              ");
            System.out.println("====================================================================");
            System.out.println("[*] Dang ket noi toi Server RMI: " + serverHost + ":" + RMI_PORT + "...");
            System.out.println("[+] Client da san sang nhan hoa don qua TCP cong: " + clientListeningPort);

            // 3. Tra cuu RMI Service
            Registry registry = LocateRegistry.getRegistry(serverHost, RMI_PORT);
            TicketService ticketService = (TicketService) registry.lookup(SERVICE_NAME);

            System.out.println("[+] Ket noi thanh cong den he thong dat ve!");
            System.out.println("--------------------------------------------------------------------");

            // 4. Vong lap menu chinh
            while (running) {
                printMenu();
                System.out.print("Chon chuc nang (1-4): ");
                String choice = scanner.nextLine().trim();

                switch (choice) {
                    case "1":
                        System.out.println("\n" + ticketService.getTripList() + "\n");
                        break;

                    case "2":
                        handleBooking(scanner, ticketService);
                        break;

                    case "3":
                        System.out.print("Nhap ma chuyen xe can tra cuu (vd: CX01): ");
                        String tripId = scanner.nextLine().trim();
                        System.out.println("\n" + ticketService.checkTrip(tripId) + "\n");
                        break;

                    case "4":
                        System.out.println("[*] Cam on ban da su dung dich vu dat ve xe. Tam biet!");
                        running = false;
                        break;

                    default:
                        System.out.println("[!] Lua chon khong hop le. Vui long chon tu 1 den 4.\n");
                        break;
                }
            }

        } catch (Exception e) {
            System.err.println("[-] Loi ket noi hoac thuc thi: " + e.getMessage());
            System.err.println("[!] Hay chac chan TicketServer da duoc bat truoc khi chay Client.");
        } finally {
            try {
                if (invoiceServerSocket != null && !invoiceServerSocket.isClosed()) {
                    invoiceServerSocket.close();
                }
            } catch (Exception ignored) {}
            scanner.close();
        }
    }

    private static void printMenu() {
        System.out.println("================== MENU CHUC NANG ==================");
        System.out.println("  1. Xem danh sach chuyen xe & so ghe con trong");
        System.out.println("  2. Dat ve xe truc tuyen (Nhan hoa don qua TCP)");
        System.out.println("  3. Tra cuu chi tiet chuyen xe theo ma");
        System.out.println("  4. Thoat chuong trinh");
        System.out.println("====================================================");
    }

    private static void handleBooking(Scanner scanner, TicketService ticketService) {
        try {
            System.out.println("\n--- THUC HIEN DAT VE ---");
            System.out.print("Nhap ma chuyen xe (vd: CX01, CX02...): ");
            String tripId = scanner.nextLine().trim();

            System.out.print("Nhap ho va ten khach hang: ");
            String customerName = scanner.nextLine().trim();

            System.out.print("Nhap so dien thoai: ");
            String phone = scanner.nextLine().trim();

            System.out.print("Nhap so luong ve can dat: ");
            int seatCount;
            try {
                seatCount = Integer.parseInt(scanner.nextLine().trim());
            } catch (NumberFormatException e) {
                System.out.println("[-] So luong ve phai la so nguyen!\n");
                return;
            }

            // Goi RMI method bookTicket, truyen thong tin host va cong TCP cua Client
            System.out.println("[*] Dang gui yeu cau dat ve den Server...");
            String response = ticketService.bookTicket(tripId, customerName, phone, seatCount, "127.0.0.1", clientListeningPort);
            System.out.println("\n" + response + "\n");

            // Nghi 500ms de hoa don TCP in xong truoc khi hien lai menu
            Thread.sleep(500);

        } catch (Exception e) {
            System.err.println("[-] Loi khi dat ve: " + e.getMessage());
        }
    }

    /**
     * Luong lang nghe va nhan hoa don dien tu duoc Server gui qua Socket TCP
     */
    private static void listenForInvoices() {
        while (running && !invoiceServerSocket.isClosed()) {
            try {
                Socket socket = invoiceServerSocket.accept();
                BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream(), StandardCharsets.UTF_8));
                
                StringBuilder sb = new StringBuilder();
                String line;
                while ((line = reader.readLine()) != null) {
                    sb.append(line).append("\n");
                }
                
                // In hoa don nhan duoc tu Server ra man hinh
                System.out.println(sb.toString());
                socket.close();
            } catch (Exception e) {
                if (!running) break;
            }
        }
    }
}
