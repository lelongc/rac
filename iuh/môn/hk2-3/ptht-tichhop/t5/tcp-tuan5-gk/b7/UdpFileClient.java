package b7;
import java.io.*;
import java.net.*;
import java.util.Scanner;
/*
 * Bai 7 UDP - Client
 * Cat file thanh chunk, gui theo thu tu va doi ACK tu server.
 */
public class UdpFileClient {
    static final int CHUNK_SIZE = 60000;
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.print("Nhap dia chi server (Enter = 127.0.0.1): ");
            String host = sc.nextLine().trim();
            if (host.isEmpty()) host = "127.0.0.1";
            System.out.print("Nhap port UDP server: ");
            int port = Integer.parseInt(sc.nextLine().trim());
            System.out.print("Nhap duong dan file can truyen: ");
            String filePath = sc.nextLine().trim();
            System.out.print("Nhap duong dan luu tren server: ");
            String savePath = sc.nextLine().trim();
            File file = new File(filePath);
            if (!file.exists() || !file.isFile()) {
                System.out.println("File khong ton tai!");
                return;
            }
            byte[] fileBytes;
            try (FileInputStream fis = new FileInputStream(file)) {
                fileBytes = fis.readAllBytes();
            }
            int totalChunks = (int) Math.ceil((double) fileBytes.length / CHUNK_SIZE);
            if (totalChunks == 0) totalChunks = 1; 
            InetAddress addr = InetAddress.getByName(host);
            try (DatagramSocket socket = new DatagramSocket()) {
                socket.setSoTimeout(5000); 
                String header = "HEADER|" + file.getName() + "|" + savePath + "|" + totalChunks;
                sendStr(socket, header, addr, port);
                String ack = recvStr(socket, 1024);
                if (!"READY".equals(ack)) {
                    System.out.println("Server khong san sang: " + ack); return;
                }
                System.out.println("Server READY. Bat dau truyen " + totalChunks + " chunk...");
                for (int seq = 0; seq < totalChunks; seq++) {
                    int offset  = seq * CHUNK_SIZE;
                    int dataLen = Math.min(CHUNK_SIZE, fileBytes.length - offset);
                    if (dataLen <= 0) dataLen = 0;
                    byte[] pktData = new byte[4 + dataLen];
                    pktData[0] = (byte) (seq >> 24);
                    pktData[1] = (byte) (seq >> 16);
                    pktData[2] = (byte) (seq >> 8);
                    pktData[3] = (byte)  seq;
                    if (dataLen > 0)
                        System.arraycopy(fileBytes, offset, pktData, 4, dataLen);
                    socket.send(new DatagramPacket(pktData, pktData.length, addr, port));
                    System.out.println("Truyen chunk " + seq + " (" + dataLen + " bytes)...");
                    String resp = recvStr(socket, 32);
                    System.out.println("Server: " + resp);
                }
                sendStr(socket, "END", addr, port);
                String result = recvStr(socket, 512);
                System.out.println("Server: " + result);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private static void sendStr(DatagramSocket s, String msg,
                                InetAddress addr, int port) throws IOException {
        byte[] data = msg.getBytes("UTF-8");
        s.send(new DatagramPacket(data, data.length, addr, port));
    }
    private static String recvStr(DatagramSocket s, int bufSize) throws IOException {
        byte[] buf = new byte[bufSize];
        DatagramPacket pkt = new DatagramPacket(buf, buf.length);
        s.receive(pkt);
        return new String(pkt.getData(), 0, pkt.getLength(), "UTF-8");
    }
}