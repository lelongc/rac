import java.net.ServerSocket;
import java.net.Socket;

// FILE 1: SERVER
// - Tạo ServerSocket lắng nghe
// - Mỗi client kết nối → tạo 1 Thread mới (serverThread) để xử lý
public class tcpServer {
    public static int PORT = 5678;

    public static void main(String[] args) {
        try {
            // === KẾT NỐI ===
            ServerSocket server = new ServerSocket(PORT);
            System.out.println("Server da tao (port: " + PORT + ")");
            System.out.println("Dang cho ket noi tu client...\n");

            int clientCount = 0;
            while (true) {
                Socket client = server.accept(); // chờ client kết nối
                clientCount++;
                System.out.println(">>> Client #" + clientCount + " ket noi!");

                // Tạo thread riêng để xử lý client này
                serverThread th = new serverThread(client, clientCount);
                th.start();
            }
            // ServerSocket không close vì chạy vô tận
        } catch (Exception e) {
            System.out.println("Loi server: " + e);
        }
    }
}
