package b8;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
/*
 * Bai 8 - Server
 * Nhan bieu thuc dang "OP so1 so2" va tra ve ket qua.
 */
public class Server {
    static final int PORT = 5000;
    public static void main(String[] args) {
        try (ServerSocket ss = new ServerSocket(PORT)) {
            System.out.println("Calc Server dang chay port " + PORT + " ...");
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