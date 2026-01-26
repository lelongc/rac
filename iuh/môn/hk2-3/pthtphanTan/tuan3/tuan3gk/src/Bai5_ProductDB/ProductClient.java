package Bai5_ProductDB;

import java.io.*;
import java.net.*;

public class ProductClient {
    public static void main(String[] args) {
        String serverAddress = "localhost";
        int port = 6123;
        String[] queries = { "Laptop", "iPhone", "Samsung", "Nike" }; // Nike should fail

        for (String query : queries) {
            try (Socket socket = new Socket(serverAddress, port);
                    PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);
                    BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream()))) {

                System.out.println("Querying for: " + query);
                writer.println(query);

                String response = reader.readLine();
                System.out.println("Server response: " + response);

            } catch (IOException e) {
                System.err.println("Client error: " + e.getMessage());
            }
        }
    }
}
