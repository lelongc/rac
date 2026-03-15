// ============================================================
// MODULE 9 – KẾT HỢP: OOP + TCP + Thread
// Đây là template GHÉP hoàn chỉnh cho đề bài ép nhiều chủ đề
// Ví dụ: "Viết hệ thống TCP: client gửi NhanVien,
//         server tính lương và trả về, nhiều client cùng lúc"
// ============================================================
import java.io.*;
import java.net.*;

// ══════════════════════════════════════════════════════════
//  PHẦN 1 – OOP (copy từ M1, rút gọn)
// ══════════════════════════════════════════════════════════
class NV {                             // TODO: đổi thành class nghiệp vụ thực tế
    String maNV, hoTen;
    int    soSP;
    double donGia;

    // Parse từ chuỗi CSV gửi qua socket: "ma,ten,soSP,donGia"
    public static NV fromCSV(String csv) {
        String[] p = csv.split(",");
        NV nv = new NV();
        nv.maNV   = p[0].trim();
        nv.hoTen  = p[1].trim();
        nv.soSP   = Integer.parseInt(p[2].trim());
        nv.donGia = Double.parseDouble(p[3].trim());
        return nv;
    }

    // Tuần tự hóa sang CSV để gửi qua socket
    public String toCSV() {
        return maNV + "," + hoTen + "," + soSP + "," + donGia;
    }

    public double tinhLuong() { return soSP * donGia; }  // TODO: công thức

    @Override public String toString() {
        return "[" + maNV + "] " + hoTen + " | Luong: " + tinhLuong();
    }
}

// ══════════════════════════════════════════════════════════
//  PHẦN 2 – SERVER
// ══════════════════════════════════════════════════════════
class M9_Server {
    static final int PORT = 5000;

    public static void main(String[] args) throws IOException {
        try (ServerSocket ss = new ServerSocket(PORT)) {
            System.out.println("Server khoi dong port " + PORT);
            int count = 0;
            while (true) {
                Socket client = ss.accept();
                count++;
                System.out.println("Client #" + count + ": "
                        + client.getInetAddress().getHostAddress() + ":" + client.getPort());
                new M9_Handler(client, count).start();
            }
        }
    }
}

// ══════════════════════════════════════════════════════════
//  PHẦN 3 – HANDLER (Thread)
// ══════════════════════════════════════════════════════════
class M9_Handler extends Thread {
    private Socket socket;
    private int    id;

    public M9_Handler(Socket socket, int id) {
        this.socket = socket;
        this.id     = id;
    }

    @Override
    public void run() {
        // Chọn 1 trong 2 cách stream theo đề:

        // ── CÁCH A: DataInputStream/DataOutputStream (int/String) ──
        try (Socket s = socket;
             DataInputStream  in  = new DataInputStream(s.getInputStream());
             DataOutputStream out = new DataOutputStream(s.getOutputStream())) {

            while (true) {
                String csv;
                try { csv = in.readUTF(); } catch (IOException e) { break; }

                if ("exit".equalsIgnoreCase(csv)) {
                    out.writeUTF("Bye!"); out.flush(); break;
                }

                // Parse OOP object từ CSV
                NV nv = NV.fromCSV(csv);

                // Xử lý và gửi kết quả
                String result = nv.toString();
                System.out.println("Client #" + id + ": " + result);
                out.writeUTF(result);
                out.flush();
            }

        } catch (IOException e) { /* bỏ qua */ }

        // ── CÁCH B: BufferedReader/PrintWriter (text theo dòng) ──
        // try (BufferedReader reader = new BufferedReader(
        //          new InputStreamReader(socket.getInputStream()));
        //      PrintWriter writer = new PrintWriter(socket.getOutputStream(), true)) {
        //     String line;
        //     while ((line = reader.readLine()) != null && !line.equals("exit")) {
        //         NV nv = NV.fromCSV(line);
        //         writer.println(nv.toString());
        //     }
        // } catch (IOException e) {}
    }
}

// ══════════════════════════════════════════════════════════
//  PHẦN 4 – CLIENT
// ══════════════════════════════════════════════════════════
class M9_Client {
    static final String HOST = "127.0.0.1";
    static final int    PORT = 5000;

    public static void main(String[] args) throws IOException {
        try (Socket socket = new Socket(HOST, PORT);
             DataInputStream  in  = new DataInputStream(socket.getInputStream());
             DataOutputStream out = new DataOutputStream(socket.getOutputStream());
             java.util.Scanner sc = new java.util.Scanner(System.in)) {

            System.out.println("Ket noi thanh cong!");

            while (true) {
                System.out.println("\nNhap NhanVien (ma,ten,soSP,donGia) hoac 'exit':");
                String input = sc.nextLine().trim();

                out.writeUTF(input);
                out.flush();

                String resp = in.readUTF();
                System.out.println("Server tra ve: " + resp);

                if ("exit".equalsIgnoreCase(input)) break;
            }
        }
    }
}

/*
 ┌──────────────────────────────────────────────────────────┐
 │  CÁCH GHÉP MODULE THEO ĐỀ BÀI                           │
 ├──────────────────────────────────────────────────────────┤
 │  OOP thuần (không mạng)        → M1                     │
 │  Thread thuần (không mạng)     → M2 hoặc M3             │
 │  Stream I/O console            → M4                     │
 │  TCP + int/String (DataStream) → M5                     │
 │  TCP + text (BufferedReader)   → M6                     │
 │  UDP                           → M7                     │
 │  Hiển thị IP/hostname          → M8                     │
 │  OOP + TCP + Thread (ghép)     → M9 (file này)          │
 ├──────────────────────────────────────────────────────────┤
 │  BẢNG CHỌN STREAM THEO DỮ LIỆU TRUYỀN:                 │
 │  int/long/byte số nhị phân → DataInputStream/Output     │
 │  String/văn bản/dòng       → BufferedReader/PrintWriter  │
 │  Byte thô (ký tự ASCII)    → InputStream/OutputStream   │
 │  UDP bất kỳ                → ByteBuffer / UTF-8 bytes   │
 └──────────────────────────────────────────────────────────┘

 THỨ TỰ CHẠY KHI THI:
   1. Mở Eclipse, tạo project mới
   2. Tạo package (hoặc default)
   3. Copy từng class cần thiết vào các file riêng
   4. Sửa TODO theo đề bài
   5. Run Server trước → Run Client sau
*/
