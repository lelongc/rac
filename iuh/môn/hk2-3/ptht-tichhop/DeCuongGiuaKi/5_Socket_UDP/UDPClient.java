package Socket_UDP;

import java.io.*;
import java.net.*;

public class UDPClient {
    public static String HOST = "localhost";
    public static int PORT = 9999;

    public static void main(String[] args) {
        if (args.length >= 2) {
            HOST = args[0];
            PORT = Integer.parseInt(args[1]);
        } else if (args.length == 1) {
            HOST = args[0];
        }

        try (DatagramSocket socket = new DatagramSocket();
             BufferedReader userInput = new BufferedReader(new InputStreamReader(System.in))) {
            
            InetAddress serverIp = InetAddress.getByName(HOST);

            System.out.println("UDP Client started!");
            while (true) {
                System.out.print("UDP Client > ");
                String message = userInput.readLine();
                if (message == null || message.equalsIgnoreCase("exit")) break;

                // Gui di
                byte[] sendData = message.getBytes();
                DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, serverIp, PORT);
                socket.send(sendPacket);

                // Nhan ve
                byte[] receiveData = new byte[1024];
                DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
                socket.receive(receivePacket);

                String response = new String(receivePacket.getData(), 0, receivePacket.getLength());
                System.out.println("UDP Server > " + response);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
