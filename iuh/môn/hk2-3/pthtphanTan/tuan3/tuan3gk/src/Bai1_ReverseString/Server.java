package Bai1_ReverseString;

import java.io.*;
import java.net.*;

public class Server {
    public static void main(String[] args) throws IOException {
        try (ServerSocket server = new ServerSocket(1234)) {
            System.out.println("Server running on 1234");
            while (true) {
                try (Socket socket = server.accept();
                        BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                        PrintWriter out = new PrintWriter(socket.getOutputStream(), true)) {
                    String line = in.readLine();
                    if (line != null)
                        out.println(new StringBuilder(line).reverse());
                }
            }
        }
    }
}
