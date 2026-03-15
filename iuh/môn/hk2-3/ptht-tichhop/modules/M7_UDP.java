// ============================================================
// MODULE 7 – UDP SERVER + CLIENT (DatagramSocket)
// Dùng khi: đề yêu cầu UDP (connectionless), truyền String/byte
// Ghép với: M5 (cùng service logic, khác transport)
// PORT MẶC ĐỊNH: 5000 (UDP)
// ============================================================
import java.io.*;
import java.net.*;
import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;

// ════════════════════════════════════════════════════════════
//  FILE 1/2 – UDP SERVER
// ════════════════════════════════════════════════════════════
class M7a_UDPServer {
    static final int PORT = 5000;

    public static void main(String[] args) throws IOException {
        try (DatagramSocket socket = new DatagramSocket(PORT)) {
            System.out.println("UDP Server lang nghe port " + PORT);
            byte[] buf = new byte[1024];

            while (true) {
                // ── Nhận gói tin ────────────────────────────
                DatagramPacket req = new DatagramPacket(buf, buf.length);
                socket.receive(req);               // chặn chờ

                // ── Lấy nội dung ────────────────────────────
                // Cách A: nhận String UTF-8
                String msg = new String(req.getData(), req.getOffset(),
                                        req.getLength(), StandardCharsets.UTF_8);

                // Cách B: nhận 2 int (int choice + int n = 8 byte)
                // ByteBuffer bb = ByteBuffer.wrap(req.getData(), 0, req.getLength());
                // int choice = bb.getInt();
                // int n      = bb.getInt();

                System.out.println("Client " + req.getAddress() + ":" + req.getPort()
                                   + " gui: " + msg);

                // ── Xử lý ───────────────────────────────────
                String respText = xuLy(msg);       // TODO: đổi logic

                // ── Gửi phản hồi ────────────────────────────
                // Cách A: gửi String UTF-8
                byte[] out = respText.getBytes(StandardCharsets.UTF_8);
                DatagramPacket resp = new DatagramPacket(
                        out, out.length, req.getAddress(), req.getPort());
                socket.send(resp);

                // Cách B: gửi long (8 byte)
                // byte[] out = ByteBuffer.allocate(8).putLong(result).array();
                // socket.send(new DatagramPacket(out, out.length,
                //             req.getAddress(), req.getPort()));
            }
        }
    }

    private static String xuLy(String req) {
        // TODO: đổi theo đề bài
        switch (req.trim()) {
            case "1": return "Time: "     + java.time.LocalTime.now();
            case "2": return "Date: "     + java.time.LocalDate.now();
            case "3": return "DateTime: " + java.time.LocalDateTime.now();
            default:  return "Nhap 1/2/3";
        }
    }
}

// ════════════════════════════════════════════════════════════
//  FILE 2/2 – UDP CLIENT
// ════════════════════════════════════════════════════════════
class M7b_UDPClient {
    static final String HOST = "127.0.0.1"; // TODO: IP server
    static final int    PORT = 5000;

    public static void main(String[] args) throws IOException {
        try (DatagramSocket socket = new DatagramSocket();
             java.util.Scanner sc = new java.util.Scanner(System.in)) {

            InetAddress serverAddr = InetAddress.getByName(HOST);
            System.out.println("UDP Client san sang -> " + HOST + ":" + PORT);

            while (true) {
                // ── Menu / nhập liệu ─────────────────────────
                System.out.println("\n1. Time  2. Date  3. DateTime  0. Thoat");
                System.out.print("Chon: ");
                String choice = sc.nextLine().trim();
                if ("0".equals(choice)) break;

                // ── Gửi gói tin ─────────────────────────────
                // Cách A: gửi String
                byte[] data = choice.getBytes(StandardCharsets.UTF_8);
                socket.send(new DatagramPacket(data, data.length, serverAddr, PORT));

                // Cách B: gửi 2 int (choice + n)
                // int n = Integer.parseInt(sc.nextLine().trim());
                // byte[] data = ByteBuffer.allocate(8).putInt(Integer.parseInt(choice)).putInt(n).array();
                // socket.send(new DatagramPacket(data, data.length, serverAddr, PORT));

                // ── Nhận phản hồi ────────────────────────────
                // Cách A: nhận String
                byte[] buf = new byte[1024];
                DatagramPacket resp = new DatagramPacket(buf, buf.length);
                socket.receive(resp);
                String text = new String(resp.getData(), resp.getOffset(),
                                         resp.getLength(), StandardCharsets.UTF_8);
                System.out.println("Server: " + text);

                // Cách B: nhận long
                // DatagramPacket resp = new DatagramPacket(new byte[8], 8);
                // socket.receive(resp);
                // long result = ByteBuffer.wrap(resp.getData(), 0, resp.getLength()).getLong();
                // System.out.println("Ket qua: " + result);
            }
        }
    }
}

/*
 SO SÁNH TCP vs UDP:
 ┌────────────┬──────────────────────────┬──────────────────────────┐
 │            │ TCP (M5/M6)              │ UDP (M7)                 │
 ├────────────┼──────────────────────────┼──────────────────────────┤
 │ Class      │ ServerSocket / Socket    │ DatagramSocket           │
 │ Kết nối    │ accept() → persistent    │ receive() → stateless    │
 │ Gửi        │ out.writeUTF / println   │ socket.send(packet)      │
 │ Nhận       │ in.readUTF / readLine    │ socket.receive(packet)   │
 │ Thread     │ new Handler(socket).start│ Thường xử lý tuần tự    │
 │ Độ tin cậy │ Có (TCP guarantee)       │ Không đảm bảo            │
 └────────────┴──────────────────────────┴──────────────────────────┘
*/
