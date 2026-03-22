package Socket_TCP_Thread;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {
    public static final int PORT = 8888;

    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
            System.out.println("Server dang chay tren port " + PORT + "...");
            int clientCount = 0;

            while (true) {
                Socket clientSocket = serverSocket.accept();
                clientCount++;
                System.out.println(">>> Client #" + clientCount + " da ket noi!");

                // Nemo socket cho WorkerThread xu ly
                WorkerThread worker = new WorkerThread(clientSocket, clientCount);
                worker.start();
            }
        } catch (IOException e) {
            System.err.println("Loi khoi tao Server: " + e.getMessage());
        }

        // =========================================================================================
        // [BLOCK UDP SERVER] - NẾU THI YÊU CẦU UDP, COMMENT TOÀN BỘ KHỐI TCP TRÊN VÀ UNCOMMENT KHỐI NÀY
        // Chú ý: UDP không có khái niệm Connection nên không dùng WorkerThread. 
        // Logic xử lý chuỗi (đảo ngược, tính toán v.v) bạn bỏ thẳng vào trong vòng lặp dưới đây.
        // =========================================================================================
        /*
        try (java.net.DatagramSocket udpSocket = new java.net.DatagramSocket(PORT)) {
            System.out.println("UDP Server dang lang nghe tren port " + PORT + "...");
            byte[] receiveData = new byte[1024];

            while (true) {
                java.net.DatagramPacket receivePacket = new java.net.DatagramPacket(receiveData, receiveData.length);
                udpSocket.receive(receivePacket);
                
                String inputLine = new String(receivePacket.getData(), 0, receivePacket.getLength()).trim();
                java.net.InetAddress clientIp = receivePacket.getAddress();
                int clientPort = receivePacket.getPort();
                System.out.println("Nhan tu UDP Client [" + clientIp + ":" + clientPort + "]: " + inputLine);

                // --- Gắn logic xử lý chuỗi tại đây (Co the mo WorkerThread de copy logic bo qua day) ---
                String result = new StringBuilder(inputLine).reverse().toString(); // Demo Dạng đảo ngược chuỗi
                
                byte[] sendData = result.getBytes();
                java.net.DatagramPacket sendPacket = new java.net.DatagramPacket(sendData, sendData.length, clientIp, clientPort);
                udpSocket.send(sendPacket);
            }
        } catch (IOException e) {
            System.err.println("Loi UDP Server: " + e.getMessage());
        }
        */
    }
}
