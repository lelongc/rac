import java.net.*;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) throws Exception {
        try (DatagramSocket ds = new DatagramSocket();
             Scanner sc = new Scanner(System.in)) {

            InetAddress ip = InetAddress.getByName("localhost");
            byte[] buf = new byte[4096];
            System.out.println("=== KET NOI UDP SERVER (5000) SAN SANG ===");

            while (true) {
                System.out.print("> Nhap du lieu: ");
                String line = sc.nextLine();
                if ("EXIT".equalsIgnoreCase(line.trim())) break;

                byte[] out = line.getBytes("UTF-8");
                ds.send(new DatagramPacket(out, out.length, ip, 5000));

                DatagramPacket p = new DatagramPacket(buf, buf.length);
                ds.receive(p);
                System.out.println("< Server tra ve: " + new String(p.getData(), 0, p.getLength(), "UTF-8"));
            }
        }
    }
}

