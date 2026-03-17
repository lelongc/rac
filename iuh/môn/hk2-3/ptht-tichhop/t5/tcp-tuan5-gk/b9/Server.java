package b9;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

// Server lưu trữ các file (vd: data.txt) trong thư mục chạy.
// Nhiều client có thể đọc nội dung file cùng lúc.
public class Server {
    static final int PORT = 5000;

    public static void main(String[] args) {
        try (ServerSocket ss = new ServerSocket(PORT)) {
            System.out.println("File Server dang chay port " + PORT + " ...");
            System.out.println("Thu muc phuc vu: " + System.getProperty("user.dir"));
            while (true) {
                Socket client = ss.accept();
                System.out.println("Client ket noi: " + client.getInetAddress().getHostAddress());
                new ClientHandler(client).start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
