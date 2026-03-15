package b5;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.nio.charset.StandardCharsets;
import java.util.Scanner;

public class DateTimeUDPClient {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in);
             DatagramSocket socket = new DatagramSocket()) {

            System.out.print("Nhap IP server: ");
            String host = sc.nextLine().trim();
            if (host.isEmpty()) host = "127.0.0.1";

            System.out.print("Nhap port: ");
            int port = Integer.parseInt(sc.nextLine().trim());

            InetAddress serverAddr = InetAddress.getByName(host);

            while (true) {
                System.out.println("\n1. Time\n2. Date\n3. Date & Time\n0. Thoat");
                System.out.print("Chon: ");
                String choice = sc.nextLine().trim();

                if ("0".equals(choice)) break;

                byte[] data = choice.getBytes(StandardCharsets.UTF_8);
                DatagramPacket req = new DatagramPacket(data, data.length, serverAddr, port);
                socket.send(req);

                byte[] buf = new byte[1024];
                DatagramPacket resp = new DatagramPacket(buf, buf.length);
                socket.receive(resp);

                String text = new String(resp.getData(), resp.getOffset(), resp.getLength(), StandardCharsets.UTF_8);
                System.out.println("Server: " + text);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}