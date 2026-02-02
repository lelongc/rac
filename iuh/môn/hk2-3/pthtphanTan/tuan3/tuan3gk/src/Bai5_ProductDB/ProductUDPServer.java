package Bai5_ProductDB;

import java.net.*;

public class ProductUDPServer {
    public static void main(String[] args) throws Exception {
        try (DatagramSocket s = new DatagramSocket(6124)) {
            System.out.println("UDP Server: 6124");
            byte[] buf = new byte[1024];
            while (true) {
                DatagramPacket p = new DatagramPacket(buf, buf.length);
                s.receive(p);
                String q = new String(p.getData(), 0, p.getLength()).trim();
                Product prod = DatabaseUtils.find(q);
                String res = (prod != null ? prod.toString() : "Not found: " + q);
                byte[] send = res.getBytes();
                s.send(new DatagramPacket(send, send.length, p.getAddress(), p.getPort()));
            }
        }
    }
}
