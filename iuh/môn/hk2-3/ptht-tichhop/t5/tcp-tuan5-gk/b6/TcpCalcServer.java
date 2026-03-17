package b6;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
/*
 * Bai 6 TCP - Server
 * Lang nghe ket noi va tao 1 thread xu ly cho moi client.
 */
public class TcpCalcServer {
    public static void main(String[] args) {
        int port = 5000;
        try (ServerSocket server = new ServerSocket(port)) {
            System.out.println("TCP Calc Server running on port " + port);
            while (true) {
                Socket client = server.accept();
                new TcpClientHandler(client).start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}