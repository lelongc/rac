package b2;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class ChatServer {
    public static void main(String[] args) {
        int port = 5000;

        try (ServerSocket server = new ServerSocket(port)) {
            System.out.println("Server running on port " + port);

            while (true) {
                Socket client = server.accept();
                new ClientHandler(client).start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}