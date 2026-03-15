import java.io.*;
import java.net.*;
import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;

// ================================================================
//  Client.java  –  CHỈ CẦN 1 FILE NÀY CHO PHẦN CLIENT
//  Cách dùng: uncomment ĐÚNG 1 khối [CLIENT-...] bên dưới
//  Stream phải KHỚP với Handler.java đang dùng
// ================================================================
public class Client {

    static final String HOST = "127.0.0.1";  // ← đổi IP nếu khác máy
    static final int    PORT = 5000;          // ← phải trùng với Server.java


    public static void main(String[] args) throws IOException {


// ----------------------------------------------------------------
// [CLIENT-A] DataStream + gửi/nhận STRING  (khớp STREAM-A Handler)
//   Dùng khi: đề truyền String qua writeUTF/readUTF
//   Ví dụ: b1 (đọc số), b2/b3 (chat), uppercase/lowercase...
// ----------------------------------------------------------------
        try (Socket socket = new Socket(HOST, PORT);
             DataInputStream  in  = new DataInputStream(socket.getInputStream());
             DataOutputStream out = new DataOutputStream(socket.getOutputStream());
             BufferedReader   kb  = new BufferedReader(new InputStreamReader(System.in))) {

            System.out.println("Ket noi " + HOST + ":" + PORT + " thanh cong!");

            // Nhận chào mừng / menu từ server (bỏ comment nếu server gửi trước)
            // System.out.println(in.readUTF());

            while (true) {
                System.out.print("Nhap ('exit' de thoat): ");
                String input = kb.readLine();

                out.writeUTF(input);
                out.flush();

                String resp = in.readUTF();
                System.out.println("Server: " + resp);

                if ("exit".equalsIgnoreCase(input)) break;
            }
        }
// ----------------------------------------------------------------


// ----------------------------------------------------------------
// [CLIENT-B] DataStream + gửi INT (menu), nhận STRING
//   Dùng khi: đề có menu số nguyên (1/2/3/0)
//   Ví dụ: b4 (Time/Date/DateTime), b6 (tính toán)
// ----------------------------------------------------------------
//        try (Socket socket = new Socket(HOST, PORT);
//             DataInputStream  in  = new DataInputStream(socket.getInputStream());
//             DataOutputStream out = new DataOutputStream(socket.getOutputStream());
//             BufferedReader   kb  = new BufferedReader(new InputStreamReader(System.in))) {
//
//            System.out.println("Ket noi thanh cong!");
//
//            // Nhận menu từ server
//            System.out.println(in.readUTF());
//
//            while (true) {
//                System.out.print("Chon (0 de thoat): ");
//                int choice = Integer.parseInt(kb.readLine().trim());
//
//                out.writeInt(choice);
//                out.flush();
//
//                String resp = in.readUTF();
//                System.out.println("Server: " + resp);
//
//                if (choice == 0) break;
//            }
//        }
// ----------------------------------------------------------------


// ----------------------------------------------------------------
// [CLIENT-C] DataStream + gửi 2 INT (choice + n), nhận LONG
//   Dùng khi: đề tính toán dãy số, truyền 2 tham số int
//   Ví dụ: b6 TcpCalcClient
// ----------------------------------------------------------------
//        try (Socket socket = new Socket(HOST, PORT);
//             DataInputStream  in  = new DataInputStream(socket.getInputStream());
//             DataOutputStream out = new DataOutputStream(socket.getOutputStream());
//             BufferedReader   kb  = new BufferedReader(new InputStreamReader(System.in))) {
//
//            System.out.println("Ket noi thanh cong!");
//            while (true) {
//                System.out.println("\n1) Tong 1+3+...   2) Tong i*(i+1)   3) 1-2+3-...   0) Thoat");
//                System.out.print("Chon: ");
//                int choice = Integer.parseInt(kb.readLine().trim());
//
//                out.writeInt(choice);
//                if (choice == 0) { out.flush(); break; }
//
//                System.out.print("Nhap n: ");
//                int n = Integer.parseInt(kb.readLine().trim());
//                out.writeInt(n);
//                out.flush();
//
//                long result = in.readLong();
//                if (result == Long.MIN_VALUE) System.out.println("Loi tham so!");
//                else System.out.println("Ket qua = " + result);
//            }
//        }
// ----------------------------------------------------------------


// ----------------------------------------------------------------
// [CLIENT-D] BufferedReader / PrintWriter  (text theo dòng)
//   Dùng khi: khớp STREAM-B trong Handler
//   Ví dụ: uppercase, lowercase, countchar, sumnumbers, chat
// ----------------------------------------------------------------
//        try (Socket socket = new Socket(HOST, PORT);
//             BufferedReader  serverIn  = new BufferedReader(
//                     new InputStreamReader(socket.getInputStream()));
//             PrintWriter     serverOut = new PrintWriter(socket.getOutputStream(), true);
//             BufferedReader  kb        = new BufferedReader(
//                     new InputStreamReader(System.in))) {
//
//            System.out.println("Ket noi thanh cong!");
//
//            // Nhận chào mừng từ server (nếu có)
//            // System.out.println(serverIn.readLine());
//
//            while (true) {
//                System.out.print("Nhap ('exit' de thoat): ");
//                String input = kb.readLine();
//
//                serverOut.println(input);          // gửi
//                String resp = serverIn.readLine(); // nhận
//                System.out.println("Server: " + resp);
//
//                if ("exit".equalsIgnoreCase(input)) break;
//            }
//        }
// ----------------------------------------------------------------


// ----------------------------------------------------------------
// [CLIENT-E] UDP Client  (khớp SERVER-3 trong Server.java)
//   Dùng khi: đề yêu cầu UDP
// ----------------------------------------------------------------
//        try (DatagramSocket socket = new DatagramSocket();
//             BufferedReader  kb     = new BufferedReader(
//                     new InputStreamReader(System.in))) {
//
//            InetAddress serverAddr = InetAddress.getByName(HOST);
//            System.out.println("UDP Client -> " + HOST + ":" + PORT);
//
//            while (true) {
//                System.out.println("\n1. Time  2. Date  3. DateTime  0. Thoat");
//                System.out.print("Chon: ");
//                String choice = kb.readLine().trim();
//                if ("0".equals(choice)) break;
//
//                // Gửi String
//                byte[] data = choice.getBytes(StandardCharsets.UTF_8);
//                socket.send(new DatagramPacket(data, data.length, serverAddr, PORT));
//
//                // Nhận String
//                byte[] buf = new byte[1024];
//                DatagramPacket resp = new DatagramPacket(buf, buf.length);
//                socket.receive(resp);
//                System.out.println("Server: " + new String(
//                        resp.getData(), resp.getOffset(),
//                        resp.getLength(), StandardCharsets.UTF_8));
//            }
//        }
// ----------------------------------------------------------------


// ----------------------------------------------------------------
// [CLIENT-F] Chat 2 chiều REALTIME (thread nhận riêng)
//   Dùng khi: đề yêu cầu client có thể nhận bất kỳ lúc nào
//   Ví dụ: b2, b3 ChatClient
// ----------------------------------------------------------------
//        try (Socket socket = new Socket(HOST, PORT);
//             DataInputStream  in  = new DataInputStream(socket.getInputStream());
//             DataOutputStream out = new DataOutputStream(socket.getOutputStream());
//             BufferedReader   kb  = new BufferedReader(new InputStreamReader(System.in))) {
//
//            System.out.println("Ket noi thanh cong! ('/quit' de thoat)");
//
//            // Thread riêng chỉ để NHẬN từ server
//            new Thread(() -> {
//                try {
//                    while (true) System.out.println("\n[Server] " + in.readUTF());
//                } catch (IOException e) { System.out.println("[Mat ket noi]"); }
//            }).start();
//
//            // Main thread: GỬI
//            while (true) {
//                System.out.print("Ban: ");
//                String msg = kb.readLine();
//                out.writeUTF(msg); out.flush();
//                if ("/quit".equalsIgnoreCase(msg)) break;
//            }
//        }
// ----------------------------------------------------------------

    }
}
