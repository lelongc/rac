package gk;

import java.net.ServerSocket;
import java.net.Socket;

public class Server {
    static final int PORT = 5000;

    public static void main(String[] args) throws Exception {
        try (ServerSocket ss = new ServerSocket(PORT)) {
            System.out.println("TCP Server listening on port " + PORT);
            int clientId = 0;
            while (true) {
                Socket s = ss.accept();
                clientId++;
                new ThreadProcess(s, clientId).start();
            }
        }
    }
}
