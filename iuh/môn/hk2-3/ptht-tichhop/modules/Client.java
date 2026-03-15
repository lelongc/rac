import java.io.*;
import java.net.*;
import java.util.Scanner;

// ╔══════════════════════════════════════════════════════════════╗
// ║  Client.java  –  mang vào thi, uncomment đúng phần là xong ║
// ║  Chạy SAU Server                                            ║
// ╚══════════════════════════════════════════════════════════════╝
public class Client {

    static final String HOST = "localhost"; // TODO: đổi nếu kết nối máy khác
    static final int    PORT = 5000;        // TODO: đồng bộ với Server.java

    // ════════════════════════════════════════════════════════════
    // ▶▶ CHỌN 1 CLIENT – comment phần còn lại                  ◀◀
    //
    //   A – DataInputStream/DataOutputStream + nhập chuỗi (text)
    //   B – DataInputStream/DataOutputStream + menu int
    //   C – DataInputStream/DataOutputStream + 2 số (choice + n)
    //   D – BufferedReader/PrintWriter        + nhập chuỗi (text)
    //   E – UDP + menu / chuỗi
    //   F – Chat 2 chiều realtime (TCP, 2 thread)
    // ════════════════════════════════════════════════════════════

    public static void main(String[] args) throws IOException {

        // ┌──────────────────────────────────────────────────────┐
        // │  CLIENT A – DataStream, gửi/nhận String (readUTF)   │
        // │  Dùng với Handler CÁCH A + xuLyString()             │
        // └──────────────────────────────────────────────────────┘
        try (Socket s         = new Socket(HOST, PORT);
             DataOutputStream out = new DataOutputStream(s.getOutputStream());
             DataInputStream  in  = new DataInputStream(s.getInputStream());
             Scanner sc = new Scanner(System.in)) {

            // Nhận lời chào nếu server gửi trước
            // System.out.println("Server: " + in.readUTF());

            while (true) {
                System.out.print("Nhap chuoi (exit de thoat): ");
                String msg = sc.nextLine();
                out.writeUTF(msg); out.flush();

                String resp = in.readUTF();
                System.out.println("Server: " + resp);
                if (msg.equalsIgnoreCase("exit")) break;
            }
        }

        // ┌──────────────────────────────────────────────────────┐
        // │  CLIENT B – DataStream, menu int → nhận String      │
        // │  Dùng với Handler CÁCH A + xuLyMenu(int choice)     │
        // └──────────────────────────────────────────────────────┘
        /*
        try (Socket s         = new Socket(HOST, PORT);
             DataOutputStream out = new DataOutputStream(s.getOutputStream());
             DataInputStream  in  = new DataInputStream(s.getInputStream());
             Scanner sc = new Scanner(System.in)) {

            // Menu nếu server gửi trước
            // System.out.println("Server: " + in.readUTF());

            while (true) {
                System.out.print("Chon (1.Time 2.Date 3.DateTime 0.Thoat): ");
                int choice = sc.nextInt();
                out.writeInt(choice); out.flush();

                String resp = in.readUTF();
                System.out.println("Server: " + resp);
                if (choice == 0) break;
            }
        }
        */

        // ┌──────────────────────────────────────────────────────┐
        // │  CLIENT C – DataStream, gửi 2 int (choice + n),     │
        // │             nhận long (kết quả dãy số)              │
        // │  Dùng với Handler CÁCH A + tinhDaySo(choice, n)     │
        // └──────────────────────────────────────────────────────┘
        /*
        try (Socket s         = new Socket(HOST, PORT);
             DataOutputStream out = new DataOutputStream(s.getOutputStream());
             DataInputStream  in  = new DataInputStream(s.getInputStream());
             Scanner sc = new Scanner(System.in)) {

            while (true) {
                System.out.print("Chon cong thuc (1/2/3, 0=thoat): ");
                int choice = sc.nextInt();
                if (choice == 0) { out.writeInt(0); out.flush(); break; }
                System.out.print("Nhap n: ");
                int n = sc.nextInt();
                out.writeInt(choice); out.flush();
                out.writeInt(n);      out.flush();

                long result = in.readLong();
                System.out.println("Ket qua: " + result);
            }
        }
        */

        // ┌──────────────────────────────────────────────────────┐
        // │  CLIENT D – BufferedReader / PrintWriter (text)     │
        // │  Dùng với Handler CÁCH B                            │
        // └──────────────────────────────────────────────────────┘
        /*
        try (BufferedReader reader = new BufferedReader(
                 new InputStreamReader(
                     new Socket(HOST, PORT).getInputStream()));
             PrintWriter writer = new PrintWriter(
                 new Socket(HOST, PORT).getOutputStream(), true);
             Scanner sc = new Scanner(System.in)) {

            // Cách chuẩn: 1 socket, 2 stream
            Socket sock = new Socket(HOST, PORT);
            BufferedReader r = new BufferedReader(new InputStreamReader(sock.getInputStream()));
            PrintWriter    w = new PrintWriter(sock.getOutputStream(), true);

            // Nhận chào nếu cần
            // System.out.println("Server: " + r.readLine());

            String msg;
            while (true) {
                System.out.print("Nhap: ");
                msg = sc.nextLine();
                w.println(msg);
                System.out.println("Server: " + r.readLine());
                if (msg.equalsIgnoreCase("exit")) break;
            }
            sock.close();
        }
        */

        // ┌──────────────────────────────────────────────────────┐
        // │  CLIENT E – UDP                                      │
        // │  Dùng với UDP Server trong Server.java              │
        // └──────────────────────────────────────────────────────┘
        /*
        try (DatagramSocket socket = new DatagramSocket();
             Scanner sc = new Scanner(System.in)) {

            InetAddress addr = InetAddress.getByName(HOST);
            byte[] buf;

            while (true) {
                System.out.print("Nhap (1/2/3, 0=thoat): ");
                String input = sc.nextLine();
                if ("0".equals(input)) break;

                // ── Gửi String ──
                buf = input.getBytes(java.nio.charset.StandardCharsets.UTF_8);
                socket.send(new DatagramPacket(buf, buf.length, addr, PORT));

                // ── Nhận String ──
                byte[] resp = new byte[1024];
                DatagramPacket pkt = new DatagramPacket(resp, resp.length);
                socket.receive(pkt);
                System.out.println("Server: " + new String(pkt.getData(), 0,
                        pkt.getLength(), java.nio.charset.StandardCharsets.UTF_8));

                // ── Gửi 2 int (choice + n) ──
                // java.nio.ByteBuffer bb = java.nio.ByteBuffer.allocate(8);
                // bb.putInt(Integer.parseInt(input)); // choice
                // System.out.print("n = "); bb.putInt(sc.nextInt()); sc.nextLine();
                // buf = bb.array();
                // socket.send(new DatagramPacket(buf, buf.length, addr, PORT));

                // ── Nhận long ──
                // byte[] resp = new byte[8];
                // DatagramPacket pkt = new DatagramPacket(resp, resp.length);
                // socket.receive(pkt);
                // long result = java.nio.ByteBuffer.wrap(pkt.getData()).getLong();
                // System.out.println("Ket qua: " + result);
            }
        }
        */

        // ┌──────────────────────────────────────────────────────┐
        // │  CLIENT F – Chat 2 chiều realtime (TCP)             │
        // │  1 thread đọc server, main thread gửi              │
        // └──────────────────────────────────────────────────────┘
        /*
        Socket sock2 = new Socket(HOST, PORT);
        BufferedReader chatIn  = new BufferedReader(new InputStreamReader(sock2.getInputStream()));
        PrintWriter    chatOut = new PrintWriter(sock2.getOutputStream(), true);
        Scanner        sc2     = new Scanner(System.in);

        // Thread nhận liên tục từ server
        new Thread(() -> {
            try {
                String line;
                while ((line = chatIn.readLine()) != null)
                    System.out.println("Server: " + line);
            } catch (IOException e) { System.out.println("Server ngat ket noi."); }
        }).start();

        // Main thread gửi
        while (true) {
            String msg2 = sc2.nextLine();
            chatOut.println(msg2);
            if (msg2.equalsIgnoreCase("exit")) break;
        }
        sock2.close();
        */
    }
}
