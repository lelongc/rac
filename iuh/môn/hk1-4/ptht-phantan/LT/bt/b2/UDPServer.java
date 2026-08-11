import java.io.IOException;
import java.net.*;
import java.util.*;

public class UDPServer {
    private static final int PORT = 8888;
    private static final int BUFFER_SIZE = 1024;

    private static class GameSession {
        int secretNum;
        int attempts;
        long startTime;

        public GameSession() {
            this.secretNum = new Random().nextInt(100) + 1; // 1 <= n <= 100
            this.attempts = 0;
            this.startTime = System.currentTimeMillis();
        }
    }

    public static void main(String[] args) {
        System.out.println("=== UDP SERVER DOAN SO DANG KHOI DONG ===");
        Map<String, GameSession> sessions = new HashMap<>();

        try (DatagramSocket socket = new DatagramSocket(PORT)) {
            System.out.println("Server UDP dang lang nghe tai cong " + PORT + "...");
            byte[] receiveData = new byte[BUFFER_SIZE];

            while (true) {
                DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
                socket.receive(receivePacket);

                InetAddress clientAddress = receivePacket.getAddress();
                int clientPort = receivePacket.getPort();
                String clientKey = clientAddress.getHostAddress() + ":" + clientPort;

                String message = new String(receivePacket.getData(), 0, receivePacket.getLength()).trim();
                System.out.println("Nhan tu [" + clientKey + "]: " + message);

                GameSession session = sessions.get(clientKey);
                if (session == null || message.equalsIgnoreCase("NEW")) {
                    session = new GameSession();
                    sessions.put(clientKey, session);
                    sendResponse(socket, clientAddress, clientPort, 
                            "Chao mung ban den voi tro choi Doan So UDP (1-100)! Hay gui so ban doan:");
                    continue;
                }

                try {
                    int guess = Integer.parseInt(message);
                    session.attempts++;

                    if (guess < session.secretNum) {
                        sendResponse(socket, clientAddress, clientPort, 
                                "GOI Y: So ban doan NHO HON so bi mat.");
                    } else if (guess > session.secretNum) {
                        sendResponse(socket, clientAddress, clientPort, 
                                "GOI Y: So ban doan LON HON so bi mat.");
                    } else {
                        long endTime = System.currentTimeMillis();
                        double totalTime = (endTime - session.startTime) / 1000.0;

                        String winMsg = String.format("WIN:CHINH XAC! So bi mat la %d. Thong ke: So lan doan = %d, Tong thoi gian = %.2f giay.",
                                session.secretNum, session.attempts, totalTime);
                        sendResponse(socket, clientAddress, clientPort, winMsg);

                        System.out.println(String.format("[THONG KE SERVER] Client UDP %s thang! So bi mat: %d, Lan doan: %d, Thoi gian: %.2fs",
                                clientKey, session.secretNum, session.attempts, totalTime));

                        sessions.remove(clientKey);
                    }
                } catch (NumberFormatException e) {
                    sendResponse(socket, clientAddress, clientPort, "LOI: Vui long nhap so nguyen hop le!");
                }
            }
        } catch (IOException e) {
            System.err.println("Loi Server UDP: " + e.getMessage());
        }
    }

    private static void sendResponse(DatagramSocket socket, InetAddress address, int port, String response) throws IOException {
        byte[] sendData = response.getBytes();
        DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, address, port);
        socket.send(sendPacket);
    }
}
