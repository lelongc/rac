import java.io.*;
import java.net.*;

// ╔══════════════════════════════════════════════════════════════╗
// ║  SERVER.java  –  mang vào thi, uncomment đúng phần là xong ║
// ║  Chạy TRƯỚC Client                                          ║
// ╚══════════════════════════════════════════════════════════════╝
public class Server {

    static final int PORT = 5000; // TODO: đổi port nếu cần

    public static void main(String[] args) throws IOException {

        // ════════════════════════════════════════════════════════
        // ▶▶ TCP SERVER (dùng cho hầu hết bài)  ◀◀
        //    Uncomment 1 trong 2 khối bên dưới tuỳ đề
        // ════════════════════════════════════════════════════════

        try (ServerSocket ss = new ServerSocket(PORT)) {
            System.out.println("TCP Server lang nghe port " + PORT + " ...");
            int count = 0;
            while (true) {
                Socket client = ss.accept();
                count++;
                System.out.println("Client #" + count + " ket noi: "
                        + client.getInetAddress().getHostAddress()
                        + ":" + client.getPort());
                new Handler(client, count).start();  // mỗi client 1 thread
            }
        }

        // ════════════════════════════════════════════════════════
        // ▶▶ UDP SERVER (uncomment cả khối này, comment TCP trên) ◀◀
        // ════════════════════════════════════════════════════════
        /*
        try (DatagramSocket socket = new DatagramSocket(PORT)) {
            System.out.println("UDP Server lang nghe port " + PORT);
            byte[] buf = new byte[1024];
            while (true) {
                DatagramPacket req = new DatagramPacket(buf, buf.length);
                socket.receive(req);

                // ── Nhận String từ client ──
                String msg = new String(req.getData(), req.getOffset(),
                                        req.getLength(), java.nio.charset.StandardCharsets.UTF_8);

                // ── Nhận 2 int (choice + n) từ client ──
                // java.nio.ByteBuffer bb = java.nio.ByteBuffer.wrap(req.getData(), 0, req.getLength());
                // int choice = bb.getInt();
                // int n      = bb.getInt();

                System.out.println("Client " + req.getAddress().getHostAddress()
                                   + ":" + req.getPort() + " gui: " + msg);

                // ── Xử lý ──
                String resp = Handler.xuLyUDP(msg);
                // long result = Handler.tinhToanUDP(choice, n);

                // ── Gửi String về client ──
                byte[] out = resp.getBytes(java.nio.charset.StandardCharsets.UTF_8);
                socket.send(new DatagramPacket(out, out.length, req.getAddress(), req.getPort()));

                // ── Gửi long về client ──
                // byte[] out = java.nio.ByteBuffer.allocate(8).putLong(result).array();
                // socket.send(new DatagramPacket(out, out.length, req.getAddress(), req.getPort()));
            }
        }
        */
    }
}
