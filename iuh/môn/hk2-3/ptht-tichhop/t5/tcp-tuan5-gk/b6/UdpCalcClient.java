package b6;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.nio.ByteBuffer;
import java.util.Scanner;

public class UdpCalcClient {
    public static void main(String[] args) {
        String host = "127.0.0.1";
        int port = 6000;

        try (DatagramSocket socket = new DatagramSocket();
             Scanner sc = new Scanner(System.in)) {

            InetAddress server = InetAddress.getByName(host);

            while (true) {
                System.out.println("\nChon phep tinh:");
                System.out.println("1) Tong 1+3+...+(2n+1)");
                System.out.println("2) Tong 1*2 + 2*3 + ... + n*(n+1)");
                System.out.println("3) 1-2+3-4+...+(2n+1)");
                System.out.println("0) Thoat");
                System.out.print("Choice: ");
                int choice = Integer.parseInt(sc.nextLine().trim());

                if (choice == 0) break;

                System.out.print("Nhap n: ");
                int n = Integer.parseInt(sc.nextLine().trim());

                byte[] data = ByteBuffer.allocate(8).putInt(choice).putInt(n).array();
                DatagramPacket req = new DatagramPacket(data, data.length, server, port);
                socket.send(req);

                byte[] buf = new byte[8];
                DatagramPacket resp = new DatagramPacket(buf, buf.length);
                socket.receive(resp);

                long result = ByteBuffer.wrap(resp.getData(), 0, resp.getLength()).getLong();
                if (result == Long.MIN_VALUE) {
                    System.out.println("Server: Tham so/choice khong hop le!");
                } else {
                    System.out.println("Ket qua = " + result);
                }
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}