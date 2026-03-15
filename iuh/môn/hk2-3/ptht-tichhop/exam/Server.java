import java.io.*;
import java.net.*;

// ================================================================
//  SERVER.java  –  CHỈ CẦN 1 FILE NÀY CHO PHẦN SERVER
//  Cách dùng: uncomment ĐÚNG 1 khối [SERVER-...] bên dưới
//  Nhớ uncomment Handler.java tương ứng
// ================================================================
public class Server {

    static final int PORT = 5000;   // ← đổi port nếu đề yêu cầu


    public static void main(String[] args) throws IOException {

// ----------------------------------------------------------------
// [SERVER-1] TCP NHIỀU CLIENT + THREAD  ← dùng cho hầu hết bài thi
//   Mỗi client được phục vụ bởi 1 thread Handler riêng
//   Ghép với: Handler.java (bất kỳ variant)
// ----------------------------------------------------------------
        try (ServerSocket ss = new ServerSocket(PORT)) {
            System.out.println("Server chay port " + PORT + " ...");
            int count = 0;
            while (true) {
                Socket client = ss.accept();
                count++;
                System.out.println("Client #" + count + " ket noi: "
                        + client.getInetAddress().getHostAddress()
                        + ":" + client.getPort());
                new Handler(client, count).start();
            }
        }
// ----------------------------------------------------------------


// ----------------------------------------------------------------
// [SERVER-2] TCP 1 CLIENT DUY NHẤT (không thread)
//   Dùng khi đề nói "server phục vụ 1 client"
// ----------------------------------------------------------------
//        try (ServerSocket ss = new ServerSocket(PORT)) {
//            System.out.println("Server chay port " + PORT + " ...");
//            Socket client = ss.accept();
//            System.out.println("Client ket noi: "
//                    + client.getInetAddress().getHostAddress());
//            new Handler(client, 1).run();   // gọi run() trực tiếp, không start()
//        }
// ----------------------------------------------------------------


// ----------------------------------------------------------------
// [SERVER-3] UDP (không cần accept, không cần thread)
//   Dùng khi đề yêu cầu UDP
//   Ghép với: phần [HANDLER-UDP] trong Handler.java
// ----------------------------------------------------------------
//        try (DatagramSocket socket = new DatagramSocket(PORT)) {
//            System.out.println("UDP Server port " + PORT + " ...");
//            byte[] buf = new byte[1024];
//            while (true) {
//                DatagramPacket req = new DatagramPacket(buf, buf.length);
//                socket.receive(req);
//                // Gọi hàm xử lý từ Handler
//                String msg = new String(req.getData(), req.getOffset(),
//                        req.getLength(), java.nio.charset.StandardCharsets.UTF_8);
//                String result = Handler.xuLyUDP(msg);   // static method
//                byte[] out = result.getBytes(java.nio.charset.StandardCharsets.UTF_8);
//                socket.send(new DatagramPacket(out, out.length,
//                        req.getAddress(), req.getPort()));
//            }
//        }
// ----------------------------------------------------------------

    }
}
