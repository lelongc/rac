// ============================================================
// MODULE 5 – TCP SERVER (DataInputStream / DataOutputStream)
// Dùng khi: truyền int, long, String qua DataStream
// Ghép với: M5c_Client, M2 (handler là thread), M1 (xử lý object)
// PORT MẶC ĐỊNH: 5000
// ============================================================
import java.io.*;
import java.net.*;

// ════════════════════════════════════════════════════════════
//  FILE 1/3 – SERVER  (chạy TRƯỚC)
// ════════════════════════════════════════════════════════════
class M5a_Server {
    static final int PORT = 5000;       // TODO: đổi port nếu cần

    public static void main(String[] args) throws IOException {
        try (ServerSocket ss = new ServerSocket(PORT)) {
            System.out.println("Server lang nghe port " + PORT + " ...");
            while (true) {
                Socket client = ss.accept();
                new M5b_Handler(client).start();   // mỗi client 1 thread
            }
        }
    }
}

// ════════════════════════════════════════════════════════════
//  FILE 2/3 – HANDLER  (1 thread = 1 client)
// ════════════════════════════════════════════════════════════
class M5b_Handler extends Thread {
    private final Socket socket;

    public M5b_Handler(Socket socket) { this.socket = socket; }

    @Override
    public void run() {
        System.out.println("Client ket noi: " + socket.getInetAddress() + ":" + socket.getPort());
        try (Socket s = socket;
             DataInputStream  in  = new DataInputStream(s.getInputStream());
             DataOutputStream out = new DataOutputStream(s.getOutputStream())) {

            // TODO: gửi menu / chào mừng trước (tuỳ đề)
            // out.writeUTF("Chao ban! Go exit de thoat.");
            // out.flush();

            while (true) {
                // ── Nhận từ client ──────────────────────────
                // Nhận String:
                String msg = in.readUTF();
                // Nhận int:    int choice = in.readInt();
                // Nhận long:   long val = in.readLong();

                if ("exit".equalsIgnoreCase(msg)) {
                    out.writeUTF("Bye!");
                    out.flush();
                    break;
                }

                // ── Xử lý ───────────────────────────────────
                String result = xuLy(msg);   // TODO: thay bằng logic đề bài

                // ── Gửi kết quả ─────────────────────────────
                out.writeUTF(result);
                // out.writeInt(n);          // gửi int
                // out.writeLong(v);         // gửi long
                out.flush();
            }
        } catch (IOException e) { /* client ngắt đột ngột – bỏ qua */ }
        System.out.println("Client ngat: " + socket.getPort());
    }

    // ── HÀM XỬ LÝ – SỬA Ở ĐÂY ─────────────────────────────
    private String xuLy(String input) {
        // TODO: thay logic theo đề bài
        // Ví dụ các biến thể hay gặp:
        return input.toUpperCase();               // đề: chuyển hoa
        // return input.toLowerCase();             // đề: chuyển thường
        // return String.valueOf(input.length());  // đề: đếm ký tự
        // return docSo(input.charAt(0));          // đề: đọc số 0-9
    }

    // Ví dụ: đọc số 0-9 tiếng Việt (b1)
    /*
    private String docSo(char c) {
        switch (c) {
            case '0': return "khong"; case '1': return "mot";
            case '2': return "hai";   case '3': return "ba";
            case '4': return "bon";   case '5': return "nam";
            case '6': return "sau";   case '7': return "bay";
            case '8': return "tam";   case '9': return "chin";
            default:  return "Khong phai so";
        }
    }
    */

    // Ví dụ: xử lý menu int (b4 DateTime)
    /*
    private String xuLyMenu(int choice) {
        switch (choice) {
            case 1: return "Time: "      + java.time.LocalTime.now();
            case 2: return "Date: "      + java.time.LocalDate.now();
            case 3: return "DateTime: "  + java.time.LocalDateTime.now();
            default: return "Lua chon khong hop le";
        }
    }
    */
}

// ════════════════════════════════════════════════════════════
//  FILE 3/3 – CLIENT  (chạy SAU khi server đã chạy)
// ════════════════════════════════════════════════════════════
class M5c_Client {
    static final String HOST = "127.0.0.1";   // TODO: đổi IP nếu thi khác máy
    static final int    PORT = 5000;

    public static void main(String[] args) throws IOException {
        try (Socket socket = new Socket(HOST, PORT);
             DataInputStream  in  = new DataInputStream(socket.getInputStream());
             DataOutputStream out = new DataOutputStream(socket.getOutputStream());
             java.util.Scanner sc = new java.util.Scanner(System.in)) {

            System.out.println("Da ket noi server " + HOST + ":" + PORT);

            // Nhận chào mừng (nếu server gửi trước)
            // System.out.println(in.readUTF());

            while (true) {
                System.out.print("Nhap (exit de thoat): ");
                String input = sc.nextLine();

                // Gửi String:
                out.writeUTF(input);
                // out.writeInt(Integer.parseInt(input));  // gửi int
                out.flush();

                // Nhận kết quả
                String resp = in.readUTF();
                // long resp = in.readLong();   // nhận long
                System.out.println("Server: " + resp);

                if ("exit".equalsIgnoreCase(input)) break;
            }
        }
    }
}

/*
 GHÉP VỚI MODULE KHÁC:
 ┌─────────────────────────────────────────────────────────┐
 │  Đề: TCP + OOP (truyền object dạng String CSV)         │
 │  Client: out.writeUTF(id + "," + name + "," + luong)   │
 │  Handler: String[] p = msg.split(",");  tạo object      │
 │  → Ghép M1_OOP vào phần xuLy() của Handler             │
 ├─────────────────────────────────────────────────────────┤
 │  Đề: TCP + Thread đồng bộ (Handler ghi vào SharedKho)  │
 │  → Thêm SharedResource (M3) làm static field Server    │
 │  → Handler gọi resource.produce() hoặc consume()       │
 └─────────────────────────────────────────────────────────┘

 THỨ TỰ CHẠY: Server → Client (cùng máy: localhost, khác máy: IP thật)
*/
