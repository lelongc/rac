package gkudp;

import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.nio.charset.StandardCharsets;
import java.util.Scanner;

public class Client {
    static final String HOST = "127.0.0.1";
    static final int PORT = 5000;

    public static void main(String[] args) throws Exception {
        try (DatagramSocket ds = new DatagramSocket();
             Scanner sc = new Scanner(System.in)) {

            InetAddress ip = InetAddress.getByName(HOST);
            byte[] buf = new byte[8192];
            byte[] hello = "HELLO".getBytes(StandardCharsets.UTF_8);
            ds.send(new DatagramPacket(hello, hello.length, ip, PORT));

            DatagramPacket welcome = new DatagramPacket(buf, buf.length);
            ds.receive(welcome);
            System.out.println(new String(welcome.getData(), 0, welcome.getLength(), StandardCharsets.UTF_8));

            while (true) {
                System.out.print("> ");
                String data = sc.nextLine();
                byte[] out = data.getBytes(StandardCharsets.UTF_8);
                ds.send(new DatagramPacket(out, out.length, ip, PORT));

                DatagramPacket resp = new DatagramPacket(buf, buf.length);
                ds.receive(resp);
                System.out.println(new String(resp.getData(), 0, resp.getLength(), StandardCharsets.UTF_8));

                if ("EXIT".equalsIgnoreCase(data.trim())) break;
            }
        }
    }
}
