// ============================================================
// MODULE 8 – INETADDRESS + THÔNG TIN KẾT NỐI
// Dùng khi: đề yêu cầu hiển thị IP, hostname, thông tin client
// Ghép với: M5/M6 (trong phần Handler), M7 (UDP)
// ============================================================
import java.net.*;

public class M8_InetAddress {
    public static void main(String[] args) throws Exception {

        // ── Lấy thông tin máy cục bộ ────────────────────────
        InetAddress local = InetAddress.getLocalHost();
        System.out.println("Hostname : " + local.getHostName());
        System.out.println("IP local : " + local.getHostAddress());

        // ── Resolve từ tên miền / IP ────────────────────────
        InetAddress addr = InetAddress.getByName("localhost");
        System.out.println("localhost -> " + addr.getHostAddress());   // 127.0.0.1

        // InetAddress remote = InetAddress.getByName("192.168.1.10");

        // ── Trong ServerHandler: lấy thông tin từ Socket ────
        // (dán vào đầu run() của ClientHandler)
        /*
        Socket s = ...;
        System.out.println("=== Client ket noi ===");
        System.out.println("IP     : " + s.getInetAddress().getHostAddress());
        System.out.println("Port   : " + s.getPort());
        System.out.println("L.Port : " + s.getLocalPort());  // port server dùng
        System.out.println("Time   : " + new java.util.Date());
        System.out.println("======================");
        */

        // ── Kiểm tra reachable ──────────────────────────────
        // boolean ok = InetAddress.getByName("8.8.8.8").isReachable(3000);
        // System.out.println("Google DNS reachable: " + ok);
    }
}

/*
 HAY DÙNG TRONG THI:
   socket.getInetAddress().getHostAddress()  →  IP của client kết nối
   socket.getPort()                          →  port phía client
   socket.getLocalPort()                     →  port server đang dùng

 Xem thêm: t5/t5-2/gui-nhan-luong/serverThread.java
*/
