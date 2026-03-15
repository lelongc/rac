package b5;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.nio.charset.StandardCharsets;

public class DateTimeUDPServer {
    public static void main(String[] args) {
        int port = 5000;

        try (DatagramSocket socket = new DatagramSocket(port)) {
            System.out.println("UDP Server running on port " + port);

            byte[] buf = new byte[1024];

            while (true) {
                DatagramPacket req = new DatagramPacket(buf, buf.length);
                socket.receive(req);

                String msg = new String(
                        req.getData(), req.getOffset(), req.getLength(),
                        StandardCharsets.UTF_8
                );

                String respText = DateTimeService.handle(msg);

                byte[] out = respText.getBytes(StandardCharsets.UTF_8);
                DatagramPacket resp = new DatagramPacket(out, out.length, req.getAddress(), req.getPort());
                socket.send(resp);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}