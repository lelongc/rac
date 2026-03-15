package b6;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.nio.ByteBuffer;

public class UdpCalcServer {
    public static void main(String[] args) {
        int port = 6000;

        try (DatagramSocket socket = new DatagramSocket(port)) {
            System.out.println("UDP Calc Server running on port " + port);

            byte[] buf = new byte[8]; 

            while (true) {
                DatagramPacket req = new DatagramPacket(buf, buf.length);
                socket.receive(req);

                ByteBuffer bb = ByteBuffer.wrap(req.getData(), 0, req.getLength());
                int choice = bb.getInt();
                int n = bb.getInt();

                long result;
                try {
                    result = CalcService.calc(choice, n);
                } catch (IllegalArgumentException ex) {
                    result = Long.MIN_VALUE;
                }

                byte[] out = ByteBuffer.allocate(8).putLong(result).array();
                DatagramPacket resp = new DatagramPacket(out, out.length, req.getAddress(), req.getPort());
                socket.send(resp);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}