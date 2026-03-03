import java.net.ServerSocket;
import java.net.Socket;

public class tcpServer extends Thread {
    public static int port = 5678; 
    public static void main(String[] args) {
        try {
            ServerSocket server = new ServerSocket(port);
            System.out.println("Server đã được tạo (port: " + port + ")");
            System.out.println("Đang chờ kết nối từ client...\n");
            
            int clientCount = 0;
            while (true) {
                Socket client = server.accept();
                clientCount++;
                System.out.println(">>> Client #" + clientCount + " kết nối!");

                serverThread th = new serverThread(client);
                th.start();
            }
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}