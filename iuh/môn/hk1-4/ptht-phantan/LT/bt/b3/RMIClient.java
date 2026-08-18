import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class RMIClient {
    public static final String SERVER_HOST = "localhost";
    public static final int RMI_PORT = 1099;
    public static final String SERVICE_NAME = "GameService";

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String host = (args.length > 0) ? args[0] : SERVER_HOST;

        try {
            System.out.println("=================================================");
            System.out.println("          KET NOI TRO CHOI DOAN SO (RMI)         ");
            System.out.println("=================================================");
            System.out.println("[*] Dang ket noi den RMI Server tai: " + host + ":" + RMI_PORT + "...");

            // Lay Registry tu Server
            Registry registry = LocateRegistry.getRegistry(host, RMI_PORT);
            
            // Tra cuu (Lookup) dich vu tu xa
            GameService gameService = (GameService) registry.lookup(SERVICE_NAME);

            System.out.println("[+] Ket noi thanh cong den Game Server!");
            System.out.println("-------------------------------------------------");

            // Nhap ten nguoi choi
            String playerName = "";
            while (playerName.trim().isEmpty()) {
                System.out.print("Nhap ten/nickname cua ban: ");
                playerName = scanner.nextLine().trim();
            }

            // Tham gia phong choi
            String welcomeMsg = gameService.joinRoom(playerName);
            System.out.println("\n" + welcomeMsg + "\n");

            // Vong lap choi game
            boolean playing = true;
            while (playing) {
                System.out.print("[" + playerName + "] Nhap so (1-100) hoac lenh (bxh / diem / thoat): ");
                String input = scanner.nextLine().trim();

                if (input.isEmpty()) {
                    continue;
                }

                if (input.equalsIgnoreCase("thoat") || input.equalsIgnoreCase("exit") || input.equalsIgnoreCase("q")) {
                    gameService.leaveRoom(playerName);
                    System.out.println("[*] Ban da roi khoi phong choi. Tam biet!");
                    playing = false;
                } else if (input.equalsIgnoreCase("bxh") || input.equalsIgnoreCase("leaderboard")) {
                    String leaderboard = gameService.getLeaderboard();
                    System.out.println("\n" + leaderboard + "\n");
                } else if (input.equalsIgnoreCase("diem") || input.equalsIgnoreCase("score")) {
                    int score = gameService.getScore(playerName);
                    System.out.println("\n[DIEM SO] Diem hien tai cua " + playerName + ": " + score + " diem.\n");
                } else {
                    // Xu ly doan so
                    try {
                        int guess = Integer.parseInt(input);
                        String result = gameService.makeGuess(playerName, guess);
                        System.out.println("\n" + result + "\n");
                    } catch (NumberFormatException e) {
                        System.out.println("[!] Vui long nhap mot so nguyen tu 1 den 100 hoac cac lenh: 'bxh', 'diem', 'thoat'!\n");
                    }
                }
            }

        } catch (Exception e) {
            System.err.println("[-] Loi ket noi hoac thuc thi RMI: " + e.getMessage());
            System.err.println("[!] Hay chac chan rang RMIServer da duoc khoi dong truoc!");
        } finally {
            scanner.close();
        }
    }
}
