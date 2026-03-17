package b10;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.concurrent.atomic.AtomicInteger;

// Server lưu tin nhắn mỗi client vào file riêng: client1.txt, client2.txt, ...
public class Server {
    static final int PORT = 5000;
    // Đếm số client để đặt tên file (thread-safe)
    static AtomicInteger clientCount = new AtomicInteger(0);

    public static void main(String[] args) {
        try (ServerSocket ss = new ServerSocket(PORT)) {
            System.out.println("Message Server dang chay port " + PORT + " ...");
            while (true) {
                Socket client = ss.accept();
                int id = clientCount.incrementAndGet();
                System.out.println("Client #" + id + " ket noi: "
                        + client.getInetAddress().getHostAddress());
                new ClientHandler(client, id).start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
