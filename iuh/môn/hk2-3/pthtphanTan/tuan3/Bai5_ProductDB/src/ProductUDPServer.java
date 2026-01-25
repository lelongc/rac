import java.net.*;
import java.io.*;

public class ProductUDPServer {
    public static void main(String[] args) {
        int port = 6124;
        try (DatagramSocket socket = new DatagramSocket(port)) {
            System.out.println("UDP Product Server is running on port " + port);
            byte[] receiveBuffer = new byte[1024];

            while (true) {
                DatagramPacket receivePacket = new DatagramPacket(receiveBuffer, receiveBuffer.length);
                socket.receive(receivePacket);

                String query = new String(receivePacket.getData(), 0, receivePacket.getLength()).trim();
                System.out.println("UDP Received request for: " + query);

                String response;
                Product product = DatabaseUtils.findProductByName(query);
                if (product != null) {
                    response = product.toString();
                } else {
                    response = "Product not found: " + query;
                }

                byte[] sendBuffer = response.getBytes();
                DatagramPacket sendPacket = new DatagramPacket(
                        sendBuffer, sendBuffer.length,
                        receivePacket.getAddress(), receivePacket.getPort());
                socket.send(sendPacket);
            }
        } catch (IOException e) {
            System.err.println("UDP Server error: " + e.getMessage());
        }
    }
}
