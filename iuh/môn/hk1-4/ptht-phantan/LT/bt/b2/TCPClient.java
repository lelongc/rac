import java.io.*;
import java.net.*;
import java.util.Scanner;

public class TCPClient {
    private static final String SERVER_HOST = "localhost";
    private static final int SERVER_PORT = 9999;

    public static void main(String[] args) {
        System.out.println("=== TCP CLIENT DOAN SO ===");
        try (
            Socket socket = new Socket(SERVER_HOST, SERVER_PORT);
            BufferedReader serverReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter serverWriter = new PrintWriter(socket.getOutputStream(), true);
            Scanner scanner = new Scanner(System.in)
        ) {
            System.out.println("Da ket noi thanh cong toi Server (" + SERVER_HOST + ":" + SERVER_PORT + ")");
            
            String welcomeMsg = serverReader.readLine();
            System.out.println("Server: " + welcomeMsg);

            while (true) {
                System.out.print("Nhap so doan cua ban: ");
                String userGuess = scanner.nextLine();

                if (userGuess.equalsIgnoreCase("exit") || userGuess.equalsIgnoreCase("quit")) {
                    System.out.println("Ban da thoat tro choi.");
                    break;
                }

                serverWriter.println(userGuess);

                String response = serverReader.readLine();
                if (response == null) {
                    System.out.println("Ket noi toi Server bi ngat.");
                    break;
                }

                if (response.startsWith("WIN:")) {
                    System.out.println("\n[THANG CUOC] " + response.substring(4));
                    System.out.println("Tro choi ket thuc. Cam on ban da choi!");
                    break;
                } else {
                    System.out.println("Server: " + response);
                }
            }
        } catch (IOException e) {
            System.err.println("Khong the ket noi toi Server: " + e.getMessage());
        }
    }
}
