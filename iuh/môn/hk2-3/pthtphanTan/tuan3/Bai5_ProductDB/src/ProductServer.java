import java.io.*;
import java.net.*;

public class ProductServer {
    public static void main(String[] args) {
        int port = 6123;
        try (ServerSocket serverSocket = new ServerSocket(port)) {
            System.out.println("TCP Product Server is running on port " + port);
            while (true) {
                try (Socket socket = serverSocket.accept();
                        BufferedReader reader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                        PrintWriter writer = new PrintWriter(socket.getOutputStream(), true)) {

                    String productName = reader.readLine();
                    System.out.println("Received request for product: " + productName);

                    if (productName != null && !productName.isEmpty()) {
                        Product product = DatabaseUtils.findProductByName(productName);
                        if (product != null) {
                            writer.println(product.toString());
                        } else {
                            writer.println("Product not found: " + productName);
                        }
                    }
                } catch (IOException e) {
                    System.err.println("Error handling client: " + e.getMessage());
                }
            }
        } catch (IOException e) {
            System.err.println("Server error: " + e.getMessage());
        }
    }
}
