package gkudp;

import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.nio.charset.StandardCharsets;

public class Server {
    static final int PORT = 5000;

    public static void main(String[] args) throws Exception {
        try (DatagramSocket ds = new DatagramSocket(PORT)) {
            System.out.println("UDP Server listening on port " + PORT);
            byte[] buf = new byte[8192];
            while (true) {
                DatagramPacket req = new DatagramPacket(buf, buf.length);
                ds.receive(req);
                String msg = new String(req.getData(), 0, req.getLength(), StandardCharsets.UTF_8);
                if ("HELLO".equalsIgnoreCase(msg.trim())) {
                    byte[] hi = "Connected. Send data or EXIT.".getBytes(StandardCharsets.UTF_8);
                    ds.send(new DatagramPacket(hi, hi.length, req.getAddress(), req.getPort()));
                    continue;
                }
                if ("EXIT".equalsIgnoreCase(msg.trim())) {
                    byte[] bye = "Bye".getBytes(StandardCharsets.UTF_8);
                    ds.send(new DatagramPacket(bye, bye.length, req.getAddress(), req.getPort()));
                    continue;
                }
                String resp = ThreadProcess.processData(msg);
                byte[] out = resp.getBytes(StandardCharsets.UTF_8);
                DatagramPacket reply = new DatagramPacket(out, out.length, req.getAddress(), req.getPort());
                ds.send(reply);
            }
        }
    }
}
