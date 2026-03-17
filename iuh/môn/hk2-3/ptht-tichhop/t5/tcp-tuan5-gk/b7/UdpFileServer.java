package b7;
import java.io.*;
import java.net.*;
/*
 * Bai 7 UDP - Server
 * Nhan header, nhan tung chunk co so thu tu, ACK tung chunk,
 * ghep lai va ghi ra file dich.
 */
public class UdpFileServer {
    static final int PORT    = 5001;
    static final int MAXDATA = 60000; 
    public static void main(String[] args) throws IOException {
        try (DatagramSocket socket = new DatagramSocket(PORT)) {
            System.out.println("UDP File Server dang chay port " + PORT + " ...");
            byte[] buf = new byte[MAXDATA + 4];
            while (true) {
                DatagramPacket pkt = new DatagramPacket(buf, buf.length);
                socket.receive(pkt);
                String header = new String(pkt.getData(), 0, pkt.getLength(), "UTF-8");
                System.out.println("Header: " + header);
                if (!header.startsWith("HEADER|")) continue;
                String[] parts   = header.split("\\|", 4);
                String fileName  = parts[1];
                String savePath  = parts[2];
                int    totalChunks = Integer.parseInt(parts[3].trim());
                InetAddress clientAddr = pkt.getAddress();
                int         clientPort = pkt.getPort();
                send(socket, "READY", clientAddr, clientPort);
                File dir = new File(savePath);
                if (!dir.exists()) dir.mkdirs();
                File dest = new File(dir, fileName);
                byte[][] chunks = new byte[totalChunks][];
                int[] sizes = new int[totalChunks];
                for (int i = 0; i < totalChunks; i++) {
                    pkt = new DatagramPacket(buf, buf.length);
                    socket.receive(pkt);
                    int seq = ((buf[0] & 0xFF) << 24) | ((buf[1] & 0xFF) << 16)
                            | ((buf[2] & 0xFF) << 8)  |  (buf[3] & 0xFF);
                    int dataLen = pkt.getLength() - 4;
                    chunks[seq] = new byte[dataLen];
                    System.arraycopy(buf, 4, chunks[seq], 0, dataLen);
                    sizes[seq] = dataLen;
                    send(socket, "ACK:" + seq, clientAddr, clientPort);
                }
                pkt = new DatagramPacket(buf, buf.length);
                socket.receive(pkt);
                try (FileOutputStream fos = new FileOutputStream(dest)) {
                    for (int i = 0; i < totalChunks; i++) {
                        fos.write(chunks[i], 0, sizes[i]);
                    }
                }
                System.out.println("Da luu: " + dest.getAbsolutePath());
                send(socket, "OK: Da luu " + dest.getAbsolutePath(), clientAddr, clientPort);
            }
        }
    }
    private static void send(DatagramSocket s, String msg,
                             InetAddress addr, int port) throws IOException {
        byte[] data = msg.getBytes("UTF-8");
        s.send(new DatagramPacket(data, data.length, addr, port));
    }
}