package Socket_TCP_Thread;

import java.io.*;
import java.net.Socket;

public class Client {
    public static String HOST = "localhost";
    public static int PORT = 8888;

    public static void main(String[] args) {
        // Dạng truyền tham số qua CLI (như Bài 3 Tuần 5)
        if (args.length >= 2) {
            HOST = args[0];
            PORT = Integer.parseInt(args[1]);
        } else if (args.length == 1) {
            HOST = args[0]; // Mặc định chỉ truyền IP
        }

        try (Socket socket = new Socket(HOST, PORT);
             BufferedReader userInput = new BufferedReader(new InputStreamReader(System.in));
             BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
             PrintWriter out = new PrintWriter(socket.getOutputStream(), true)) {

            System.out.println("Da ket noi den Server " + HOST + ":" + PORT);
            System.out.println("Nhap van ban de gui den Server (go 'exit' de thoat):");

            String message;
            
            // =========================================================================================
            // DẠNG CHUẨN: GỬI XONG CHỜ NHẬN RỒI MỚI GỬI TIẾP (Dong bo)
            // =========================================================================================
            while (true) {
                System.out.print("Client > ");
                message = userInput.readLine();

                if (message == null || message.equalsIgnoreCase("exit")) {
                    break;
                }

                out.println(message); 
                
                String response = in.readLine(); 
                System.out.println("Server > " + response);
            }

            // =========================================================================================
            // DẠNG BÀI 2 TUẦN 5: CHAT HAI CHIỀU (BẤT ĐỒNG BỘ) - Gởi/Nhận liên tục không chờ nhau
            // NẾU THI BÀI CHAT: Mở khối này và Comment cái while(true) chuẩn ở trên lại!
            // =========================================================================================
            /*
            Thread receiveThread = new Thread(() -> {
                try {
                    String response;
                    while ((response = in.readLine()) != null) {
                        System.out.println("\nServer > " + response);
                        System.out.print("Client > "); // In lai prompt neu can
                    }
                } catch (IOException e) {
                    System.out.println("Da ngat ket noi nhan tin.");
                }
            });
            receiveThread.start();
            
            while (true) {
                System.out.print("Client > ");
                message = userInput.readLine();
                if (message == null || message.equalsIgnoreCase("exit")) break;
                out.println(message); 
            }
            */

        } catch (IOException e) {
            System.err.println("Loi ket noi den Server TCP: " + e.getMessage());
        }

        // =========================================================================================
        // [BLOCK UDP CLIENT] - NẾU THI YÊU CẦU UDP, COMMENT TOÀN BỘ KHỐI TCP TRÊN VÀ UNCOMMENT KHỐI NÀY
        // =========================================================================================
        /*
        try (java.net.DatagramSocket udpSocket = new java.net.DatagramSocket();
             BufferedReader userInput = new BufferedReader(new InputStreamReader(System.in))) {
            
            java.net.InetAddress serverIp = java.net.InetAddress.getByName(HOST);
            System.out.println("Da bat UDP Client, san sang gui den " + HOST + ":" + PORT);

            while (true) {
                System.out.print("UDP Client > ");
                String message = userInput.readLine();
                if (message == null || message.equalsIgnoreCase("exit")) break;

                // Gui di
                byte[] sendData = message.getBytes();
                java.net.DatagramPacket sendPacket = new java.net.DatagramPacket(sendData, sendData.length, serverIp, PORT);
                udpSocket.send(sendPacket);

                // Nhan ve
                byte[] receiveData = new byte[1024];
                java.net.DatagramPacket receivePacket = new java.net.DatagramPacket(receiveData, receiveData.length);
                udpSocket.receive(receivePacket);

                String response = new String(receivePacket.getData(), 0, receivePacket.getLength());
                System.out.println("UDP Server > " + response);
            }
        } catch (Exception e) {
            System.err.println("Loi UDP Client: " + e.getMessage());
        }
        */
    }
}
