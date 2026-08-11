import java.io.*;
import java.net.*;
import java.util.Random;

public class TCPServer {
    private static final int PORT = 9999;

    public static void main(String[] args) {
        System.out.println("=== TCP SERVER DOAN SO DANG KHOI DONG ===");
        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
            System.out.println("Server dang lang nghe ket noi tai cong " + PORT + "...");

            while (true) {
                Socket clientSocket = serverSocket.accept();
                System.out.println("Client moi ket noi tu: " + clientSocket.getRemoteSocketAddress());
                
                new Thread(new ClientHandler(clientSocket)).start();
            }
        } catch (IOException e) {
            System.err.println("Loi Server: " + e.getMessage());
        }
    }

    private static class ClientHandler implements Runnable {
        private final Socket socket;

        public ClientHandler(Socket socket) {
            this.socket = socket;
        }

        @Override
        public void run() {
            try (
                BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                PrintWriter writer = new PrintWriter(socket.getOutputStream(), true)
            ) {
                Random random = new Random();
                int secretNum = random.nextInt(100) + 1; // 1 <= n <= 100

                long startTime = System.currentTimeMillis();
                int attempts = 0;

                writer.println("Chao mung ban den voi tro choi Doan So (tu 1 den 100)! Hay nhap so ban doan:");

                String inputLine;
                while ((inputLine = reader.readLine()) != null) {
                    try {
                        int guess = Integer.parseInt(inputLine.trim());
                        attempts++;

                        if (guess < secretNum) {
                            writer.println("GOI Y: So ban doan NHO HON so bi mat. Hay doan lai:");
                        } else if (guess > secretNum) {
                            writer.println("GOI Y: So ban doan LON HON so bi mat. Hay doan lai:");
                        } else {
                            long endTime = System.currentTimeMillis();
                            double totalTimeSeconds = (endTime - startTime) / 1000.0;

                            String winMsg = String.format("CHINH XAC! So bi mat la %d. Thong ke: So lan doan = %d, Tong thoi gian = %.2f giay.",
                                    secretNum, attempts, totalTimeSeconds);
                            
                            writer.println("WIN:" + winMsg);

                            System.out.println(String.format("[THONG KE SERVER] Client %s da thang! So bi mat: %d, So lan doan: %d, Tong thoi gian: %.2fs",
                                    socket.getRemoteSocketAddress(), secretNum, attempts, totalTimeSeconds));
                            break;
                        }
                    } catch (NumberFormatException e) {
                        writer.println("LOI: Vui long nhap mot so nguyen hop le!");
                    }
                }
            } catch (IOException e) {
                System.out.println("Client ngat ket noi: " + socket.getRemoteSocketAddress());
            } finally {
                try {
                    socket.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
