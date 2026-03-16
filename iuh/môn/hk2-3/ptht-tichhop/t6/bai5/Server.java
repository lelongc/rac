package bai5;


import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {
    private static final int PORT = 6789;

    public static void main(String[] args) {
        System.out.println("Server TCP lang nghe tai cong " + PORT + "...");
        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
            while (true) {
                Socket clientSocket = serverSocket.accept();
                System.out.println("ket noi tu: " + clientSocket.getInetAddress());

                
                new ClientHandler(clientSocket).start();
            }
        } catch (IOException e) {
            System.out.println("loi server: " + e.getMessage());
        }
    }
}