import java.net.*;
import java.io.*;

public class ProductUDPClient {
    public static void main(String[] args) {
        String serverAddress = "localhost";
        int port = 6124;
        String[] queries = { "Mouse", "Headphones", "XPS" };

        try (DatagramSocket socket = new DatagramSocket()) {
            InetAddress address = InetAddress.getByName(serverAddress);
            socket.setSoTimeout(2000); // 2 seconds timeout

            for (String query : queries) {
                System.out.println("UDP Querying for: " + query);
                byte[] sendBuffer = query.getBytes();
                DatagramPacket sendPacket = new DatagramPacket(sendBuffer, sendBuffer.length, address, port);
                socket.send(sendPacket);

                byte[] receiveBuffer = new byte[1024];
                DatagramPacket receivePacket = new DatagramPacket(receiveBuffer, receiveBuffer.length);

                try {
                    socket.receive(receivePacket);
                    String response = new String(receivePacket.getData(), 0, receivePacket.getLength());
                    System.out.println("UDP Server response: " + response);
                } catch (SocketTimeoutException e) {
                    System.err.println("UDP Request timed out for: " + query);
                }
            }
        } catch (IOException e) {
            System.err.println("UDP Client error: " + e.getMessage());
        }
    }
}
