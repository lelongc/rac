import java.io.*;
import java.net.*;
import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;

// ================================================================
//  Handler.java  –  XỬ LÝ 1 CLIENT (Thread)
//  Cách dùng:
//    1. Uncomment ĐÚNG 1 khối [STREAM-...] để chọn loại stream
//    2. Uncomment ĐÚNG 1 khối [XU-LY-...] trong hàm xuLy()
//    3. Thêm OOP class phía dưới nếu đề yêu cầu kế thừa
// ================================================================
public class Handler extends Thread {

    private Socket socket;
    private int    clientId;

    public Handler(Socket socket, int clientId) {
        this.socket   = socket;
        this.clientId = clientId;
    }

    // ============================================================
    //  run() – chọn 1 trong 3 loại stream, uncomment khối đó
    // ============================================================
    @Override
    public void run() {

        System.out.println("=== Client #" + clientId + " ===");
        System.out.println("IP   : " + socket.getInetAddress().getHostAddress());
        System.out.println("Port : " + socket.getPort());
        System.out.println("Time : " + new java.util.Date());


// ----------------------------------------------------------------
// [STREAM-A] DataInputStream / DataOutputStream
//   Dùng khi: truyền String (writeUTF/readUTF) hoặc int/long
//   Phổ biến nhất trong bài thi tcp-tuan5-gk
// ----------------------------------------------------------------
        try (Socket s = socket;
             DataInputStream  in  = new DataInputStream(s.getInputStream());
             DataOutputStream out = new DataOutputStream(s.getOutputStream())) {

            // Gửi chào trước (bỏ comment nếu đề yêu cầu)
            // out.writeUTF("Chao ban! Nhap 'exit' de thoat."); out.flush();

            // Gửi menu (bỏ comment nếu đề có menu)
            // out.writeUTF("MENU:\n1. ...\n2. ...\nNhap 0 de thoat"); out.flush();

            while (true) {

                // --- Nhận dữ liệu từ client ---

                // Nhận String:
                String msg = in.readUTF();
                if ("exit".equalsIgnoreCase(msg)) { out.writeUTF("Bye!"); out.flush(); break; }
                String result = xuLy(msg);
                out.writeUTF(result);
                out.flush();

                // Nhận int (menu choice):
//                int choice = in.readInt();
//                if (choice == 0) { out.writeUTF("Bye!"); out.flush(); break; }
//                String result = xuLyMenu(choice);
//                out.writeUTF(result);
//                out.flush();

                // Nhận 2 int (choice + n):
//                int choice = in.readInt();
//                if (choice == 0) { out.writeLong(0); out.flush(); break; }
//                int n = in.readInt();
//                try { out.writeLong(tinhToan(choice, n)); }
//                catch (IllegalArgumentException e) { out.writeLong(Long.MIN_VALUE); }
//                out.flush();
            }

        } catch (IOException e) { /* client ngat dot ngot */ }
// ----------------------------------------------------------------


// ----------------------------------------------------------------
// [STREAM-B] BufferedReader / PrintWriter  (text theo dòng)
//   Dùng khi: truyền chuỗi văn bản, chat, uppercase/lowercase...
//   Phổ biến trong bài t5-2
// ----------------------------------------------------------------
//        try (BufferedReader reader = new BufferedReader(
//                 new InputStreamReader(socket.getInputStream()));
//             PrintWriter writer = new PrintWriter(socket.getOutputStream(), true)) {
//
//            // Gửi chào (tuỳ đề)
//            // writer.println("Chao ban! Go 'exit' de thoat.");
//
//            String msg;
//            while ((msg = reader.readLine()) != null) {
//                if (msg.equalsIgnoreCase("exit")) { writer.println("Bye!"); break; }
//                System.out.println("Client #" + clientId + " gui: " + msg);
//                writer.println(xuLy(msg));   // auto-flush vì PrintWriter(true)
//            }
//
//        } catch (IOException e) { /* bỏ qua */ }
//        finally { try { socket.close(); } catch (IOException e) {} }
// ----------------------------------------------------------------


// ----------------------------------------------------------------
// [STREAM-C] InputStream / OutputStream  (byte thô)
//   Dùng khi: đề truyền từng byte, ký tự ASCII
//   Ví dụ: t5/t5-2/gui-nhan-luong/serverThread.java
// ----------------------------------------------------------------
//        try (InputStream is = socket.getInputStream();
//             OutputStream os = socket.getOutputStream()) {
//            int ch;
//            while ((ch = is.read()) != -1) {
//                // TODO: xử lý byte ch, gửi về
//                os.write(ch);   // ví dụ: echo lại
//            }
//        } catch (IOException e) { /* bỏ qua */ }
//        finally { try { socket.close(); } catch (IOException e) {} }
// ----------------------------------------------------------------

        System.out.println("Client #" + clientId + " ngat.");
    }


    // ============================================================
    //  xuLy() – UNCOMMENT ĐÚNG 1 VARIANT theo đề bài
    // ============================================================
    private String xuLy(String input) {

// [XU-LY-1] Chuyển CHỮ HOA
        return input.toUpperCase();

// [XU-LY-2] Chuyển chữ thường
//        return input.toLowerCase();

// [XU-LY-3] Đếm số ký tự
//        return "So ky tu: " + input.length();

// [XU-LY-4] Kiểm tra CHẴN / LẺ  (input là số nguyên dạng String)
//        try {
//            int n = Integer.parseInt(input.trim());
//            return n + " la so " + (n % 2 == 0 ? "Chan" : "Le");
//        } catch (NumberFormatException e) {
//            return "Loi: vui long nhap so nguyen";
//        }

// [XU-LY-5] Tính TỔNG các số cách nhau bởi dấu cách  ("1 2 3 4")
//        try {
//            String[] parts = input.trim().split("\\s+");
//            int sum = 0;
//            for (String p : parts) sum += Integer.parseInt(p);
//            return "Tong: " + sum;
//        } catch (NumberFormatException e) {
//            return "Loi: nhap cac so cach nhau bang dau cach";
//        }

// [XU-LY-6] Đọc số 0-9 tiếng Việt  (input là 1 ký tự)
//        if (input.isEmpty()) return "Rong";
//        switch (input.charAt(0)) {
//            case '0': return "khong"; case '1': return "mot";
//            case '2': return "hai";   case '3': return "ba";
//            case '4': return "bon";   case '5': return "nam";
//            case '6': return "sau";   case '7': return "bay";
//            case '8': return "tam";   case '9': return "chin";
//            default:  return "Khong phai so nguyen (0-9)";
//        }

// [XU-LY-7] Echo lại (chat cơ bản)
//        return "Server nhan: " + input;

// [XU-LY-8] Tính tổng xuôi-ngược xen kẽ: 1-2+3-4+...  (input = "n")
//        try {
//            int n = Integer.parseInt(input.trim());
//            // Công thức: kết quả = n+1  (nếu tính đến 2n+1)
//            long result = (long) n + 1;
//            return "Ket qua: " + result;
//        } catch (NumberFormatException e) { return "Loi: nhap so nguyen"; }

    }


    // ============================================================
    //  xuLyMenu() – dùng khi đề có MENU INT (STREAM-A, nhận int)
    // ============================================================
//    private String xuLyMenu(int choice) {
//        switch (choice) {
//
// [MENU-1] Time / Date / DateTime
//            case 1: return "Time: "     + java.time.LocalTime.now();
//            case 2: return "Date: "     + java.time.LocalDate.now();
//            case 3: return "DateTime: " + java.time.LocalDateTime.now();
//
// [MENU-2] Tính toán (thêm tham số n ở phần nhận int bên trên)
//            // case 1: return "Tong 1+3+...+(2n+1) = " + ...;
//            // case 2: return "Tong i*(i+1) = " + ...;
//
//            default: return "Lua chon khong hop le";
//        }
//    }


    // ============================================================
    //  tinhToan() – dùng khi đề có TÍNH TOÁN DÃY SỐ (2 int)
    // ============================================================
//    private long tinhToan(int choice, int n) {
//        if (n < 0) throw new IllegalArgumentException("n >= 0");
//        switch (choice) {
//            case 1: { // Tong 1+3+5+...+(2n+1) = (n+1)^2
//                long k = (long) n + 1; return k * k;
//            }
//            case 2: { // Tong i*(i+1), i=1..n
//                long nn = n;
//                return nn*(nn+1)*(2*nn+1)/6 + nn*(nn+1)/2;
//            }
//            case 3: { // 1-2+3-4+...+(2n+1) = n+1
//                return (long) n + 1;
//            }
//            default: throw new IllegalArgumentException("choice 1/2/3");
//        }
//    }


    // ============================================================
    //  xuLyUDP() – static, gọi từ Server.java khi dùng [SERVER-3]
    // ============================================================
//    public static String xuLyUDP(String req) {
//        switch (req.trim()) {
//            case "1": return "Time: "     + java.time.LocalTime.now();
//            case "2": return "Date: "     + java.time.LocalDate.now();
//            case "3": return "DateTime: " + java.time.LocalDateTime.now();
//            default:  return "Nhap 1/2/3";
//        }
//    }


    // ============================================================
    //  OOP – uncomment + chỉnh khi đề kết hợp kế thừa
    // ============================================================

    // --- Lớp cha ---
//    static class Entity {
//        String id, name;
//        public Entity() {}
//        public Entity(String id, String name) { this.id=id; this.name=name; }
//        public double tinhToan() { return 0; }
//        @Override public String toString() { return id + " | " + name; }
//
//        // Parse từ "id,name,field1,field2" gửi qua socket
//        public static Entity fromCSV(String csv) {
//            String[] p = csv.split(",");
//            // TODO: gán fields
//            return new Entity(p[0].trim(), p[1].trim());
//        }
//    }

    // --- Lớp con ---
//    static class ConA extends Entity {
//        int    soLuong;
//        double donGia;
//        public ConA() { super(); }
//        @Override public double tinhToan() { return soLuong * donGia; }
//
//        public static ConA fromCSV(String csv) {
//            String[] p = csv.split(",");
//            ConA c = new ConA();
//            c.id      = p[0].trim();
//            c.name    = p[1].trim();
//            c.soLuong = Integer.parseInt(p[2].trim());
//            c.donGia  = Double.parseDouble(p[3].trim());
//            return c;
//        }
//
//        @Override public String toString() {
//            return super.toString() + " | Luong: " + tinhToan();
//        }
//    }


    // ============================================================
    //  THREAD ĐỒNG BỘ – uncomment khi đề yêu cầu Kho / Producer-Consumer
    // ============================================================

//    // --- Shared Resource (đặt làm static field của Server) ---
//    // static SharedKho kho = new SharedKho(10);
//
//    static class SharedKho {
//        private int suc, ton = 0;
//        public SharedKho(int suc) { this.suc = suc; }
//
//        public synchronized void nhap(int x, String who) throws InterruptedException {
//            while (ton + x > suc) { System.out.println(who + " cho (day)..."); wait(); }
//            ton += x;
//            System.out.println(who + " nhap " + x + " | ton: " + ton);
//            notifyAll();
//        }
//
//        public synchronized void xuat(int x, String who) throws InterruptedException {
//            while (ton < x) { System.out.println(who + " cho (thieu)..."); wait(); }
//            ton -= x;
//            System.out.println(who + " xuat " + x + " | ton: " + ton);
//            notifyAll();
//        }
//    }

}
