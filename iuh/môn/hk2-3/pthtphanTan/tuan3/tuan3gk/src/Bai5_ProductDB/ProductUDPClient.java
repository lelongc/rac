package Bai5_ProductDB;

import java.net.*;
import java.util.Scanner;

public class ProductUDPClient {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        try (DatagramSocket s = new DatagramSocket()) {
            s.setSoTimeout(1000);
            while (true) {
                System.out.print("UDP Search (type 'exit' to quit): ");
                String q = sc.nextLine();
                if (q.equals("exit"))
                    break;
                byte[] b = q.getBytes();
                s.send(new DatagramPacket(b, b.length, InetAddress.getByName("localhost"), 6124));
                byte[] buf = new byte[1024];
                DatagramPacket p = new DatagramPacket(buf, buf.length);
                try {
                    s.receive(p);
                    System.out.println("Result: " + new String(p.getData(), 0, p.getLength()));
                } catch (Exception e) {
                    System.out.println("Timeout or Err");
                }
            }
        }
    }
}
