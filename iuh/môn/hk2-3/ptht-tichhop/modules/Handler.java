import java.io.*;
import java.net.*;

// ╔══════════════════════════════════════════════════════════════╗
// ║  Handler.java  –  1 thread xử lý 1 client                  ║
// ║  Chứa TẤT CẢ logic xử lý – uncomment đúng phần là xong     ║
// ╚══════════════════════════════════════════════════════════════╝
public class Handler extends Thread {

    private Socket socket;
    private int    clientId;

    public Handler(Socket socket, int clientId) {
        this.socket   = socket;
        this.clientId = clientId;
    }

    // ════════════════════════════════════════════════════════════
    // ▶▶ CHỌN 1 TRONG 2 CÁCH STREAM – comment cái kia lại ◀◀
    //
    //   CÁCH A – DataInputStream/DataOutputStream
    //     → Dùng khi đề truyền: int, long, String nhị phân
    //     → writeUTF / readUTF / writeInt / readInt / writeLong
    //
    //   CÁCH B – BufferedReader / PrintWriter
    //     → Dùng khi đề truyền: chuỗi văn bản, chat, text theo dòng
    //     → println / readLine
    // ════════════════════════════════════════════════════════════

    @Override
    public void run() {

        // ┌──────────────────────────────────────────────────────┐
        // │  CÁCH A – DataInputStream / DataOutputStream        │
        // └──────────────────────────────────────────────────────┘
        try (Socket s = socket;
             DataInputStream  in  = new DataInputStream(s.getInputStream());
             DataOutputStream out = new DataOutputStream(s.getOutputStream())) {

            // ── Gửi chào / menu trước (bỏ comment nếu đề yêu cầu) ──
            // out.writeUTF("Chao ban! Go exit de thoat."); out.flush();
            // out.writeUTF("MENU:\n1. Time\n2. Date\n3. Date&Time\n0. Thoat"); out.flush();

            while (true) {

                // ── NHẬN từ client – chọn 1 dòng phù hợp ──────────
                String msg    = in.readUTF();          // nhận String
                // int    choice = in.readInt();        // nhận int (menu)
                // long   val    = in.readLong();       // nhận long

                // ── Kiểm tra thoát ───────────────────────────────
                if ("exit".equalsIgnoreCase(msg)) {
                    out.writeUTF("Bye!"); out.flush(); break;
                }
                // if (choice == 0) { out.writeLong(0); out.flush(); break; } // thoát khi int

                // ── XỬ LÝ – uncomment hàm phù hợp ──────────────
                String result = xuLyString(msg);
                // int    result = xuLyInt(choice);
                // long   result = xuLyMenu(choice, Integer.parseInt(msg));

                // ── GỬI kết quả về client – chọn 1 dòng phù hợp ──
                out.writeUTF(result);   out.flush();   // gửi String
                // out.writeInt(result);  out.flush();  // gửi int
                // out.writeLong(result); out.flush();  // gửi long
            }

        } catch (IOException e) { /* client ngắt đột ngột – bỏ qua */ }

        // ┌──────────────────────────────────────────────────────┐
        // │  CÁCH B – BufferedReader / PrintWriter (text dòng)  │
        // │  Comment toàn bộ CÁCH A, uncomment khối này         │
        // └──────────────────────────────────────────────────────┘
        /*
        try (BufferedReader reader = new BufferedReader(
                 new InputStreamReader(socket.getInputStream()));
             PrintWriter writer = new PrintWriter(socket.getOutputStream(), true)) {

            // Gửi chào (bỏ comment nếu cần)
            // writer.println("Chao client #" + clientId + "! Go 'exit' de thoat.");

            String msg;
            while ((msg = reader.readLine()) != null) {
                if (msg.equalsIgnoreCase("exit")) { writer.println("Bye!"); break; }

                System.out.println("Client #" + clientId + " gui: " + msg);

                String result = xuLyString(msg);   // TODO: đổi hàm xử lý
                writer.println(result);            // tự flush vì PrintWriter(true)
            }
        } catch (IOException e) {}
        finally { try { socket.close(); } catch (IOException e) {} }
        */

        System.out.println("Client #" + clientId + " ngat ket noi.");
    }

    // ════════════════════════════════════════════════════════════
    //  CÁC HÀM XỬ LÝ – uncomment hàm nào cần, gọi trong run()
    // ════════════════════════════════════════════════════════════

    // ── Xử lý String → String ───────────────────────────────────
    private String xuLyString(String msg) {

        return msg.toUpperCase();                       // ĐỀ: chuyển hoa
        // return msg.toLowerCase();                    // ĐỀ: chuyển thường
        // return "So ky tu: " + msg.length();          // ĐỀ: đếm ký tự
        // return msg.toUpperCase() + " (" + msg.length() + " ky tu)"; // kết hợp

        // ĐỀ: đảo ngược chuỗi
        // return new StringBuilder(msg).reverse().toString();

        // ĐỀ: tổng các số cách nhau bằng dấu cách ("1 2 3 4")
        /*
        try {
            int sum = 0;
            for (String p : msg.trim().split("\\s+")) sum += Integer.parseInt(p);
            return "Tong: " + sum;
        } catch (NumberFormatException e) { return "Loi: nhap so nguyen cach nhau dau cach"; }
        */

        // ĐỀ: kiểm tra chẵn lẻ (client gửi String chứa số)
        /*
        try {
            int n = Integer.parseInt(msg.trim());
            return n + " la so " + (n % 2 == 0 ? "Chan" : "Le");
        } catch (NumberFormatException e) { return "Loi: khong phai so nguyen"; }
        */
    }

    // ── Xử lý int → String (menu chọn 1/2/3) ───────────────────
    /*
    private String xuLyMenu(int choice) {
        switch (choice) {
            // ĐỀ: trả về thời gian
            case 1: return "Time: "     + java.time.LocalTime.now();
            case 2: return "Date: "     + java.time.LocalDate.now();
            case 3: return "DateTime: " + java.time.LocalDateTime.now();

            // ĐỀ: tính toán dãy số (choice + n gửi cùng lúc)
            // case 1: return "TODO: cong thuc 1";
            // case 2: return "TODO: cong thuc 2";
            // case 3: return "TODO: cong thuc 3";

            default: return "Lua chon khong hop le";
        }
    }
    */

    // ── Xử lý int choice + int n → long (b6: dãy số) ───────────
    /*
    private long tinhDaySo(int choice, int n) {
        switch (choice) {
            case 1: { // 1+3+5+...+(2n+1) = (n+1)^2
                long k = n + 1; return k * k;
            }
            case 2: { // 1*2 + 2*3 + ... + n*(n+1)
                long s = 0; for (int i = 1; i <= n; i++) s += (long)i*(i+1); return s;
            }
            case 3: { // 1-2+3-4+...+(2n+1) = n+1
                return n + 1;
            }
            default: return Long.MIN_VALUE; // báo lỗi
        }
    }
    */

    // ── Xử lý 1 ký tự số → tên tiếng Việt (b1) ─────────────────
    /*
    private String docSo(char c) {
        switch (c) {
            case '0': return "khong"; case '1': return "mot";
            case '2': return "hai";   case '3': return "ba";
            case '4': return "bon";   case '5': return "nam";
            case '6': return "sau";   case '7': return "bay";
            case '8': return "tam";   case '9': return "chin";
            default:  return "Khong phai so nguyen";
        }
    }
    */

    // ── Hàm tĩnh dùng cho UDP Server (gọi từ Server.java) ───────
    public static String xuLyUDP(String msg) {
        switch (msg.trim()) {
            case "1": return "Time: "     + java.time.LocalTime.now();
            case "2": return "Date: "     + java.time.LocalDate.now();
            case "3": return "DateTime: " + java.time.LocalDateTime.now();
            default:  return "Nhap 1/2/3";
        }
    }

    /*
    public static long tinhToanUDP(int choice, int n) {
        // TODO: dán logic tinhDaySo vào đây nếu cần UDP + tính toán
        return 0;
    }
    */

    // ════════════════════════════════════════════════════════════
    //  OOP (kế thừa) – dán class cha/con vào đây nếu đề ép OOP
    // ════════════════════════════════════════════════════════════
    /*
    // Lớp cha
    static class NhanVien {
        String maNV, hoTen;
        public double tinhLuong() { return 0; }
        // parse từ CSV gửi qua socket: "maNV,hoTen,..."
        public static NhanVien fromCSV(String csv) {
            // TODO: tạo subclass phù hợp từ csv.split(",")
            return null;
        }
        @Override public String toString() {
            return maNV + " | " + hoTen + " | Luong: " + tinhLuong();
        }
    }
    // Lớp con
    static class NVSanXuat extends NhanVien {
        int soSP; double donGia;
        @Override public double tinhLuong() { return soSP * donGia; }
    }
    static class NVVanPhong extends NhanVien {
        double luongCB, phuCap;
        @Override public double tinhLuong() { return luongCB + phuCap; }
    }
    */

    // ════════════════════════════════════════════════════════════
    //  SYNCHRONIZED / PRODUCER-CONSUMER – dán vào nếu đề ép
    // ════════════════════════════════════════════════════════════
    /*
    static class SharedKho {
        private int max, cur = 0;
        SharedKho(int max) { this.max = max; }

        public synchronized void nhap(int amt, String who) throws InterruptedException {
            while (cur + amt > max) { System.out.println(who + " cho day..."); wait(); }
            cur += amt;
            System.out.println(who + " nhap " + amt + " | ton: " + cur);
            notifyAll();
        }
        public synchronized void xuat(int amt, String who) throws InterruptedException {
            while (cur < amt) { System.out.println(who + " cho thieu..."); wait(); }
            cur -= amt;
            System.out.println(who + " xuat " + amt + " | ton: " + cur);
            notifyAll();
        }
    }
    */
}
