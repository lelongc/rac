// ============================================================
// MODULE 6 – TCP SERVER (BufferedReader / PrintWriter – text dòng)
// Dùng khi: truyền chuỗi văn bản, nhiều client, chat
// Ghép với: M2 (thread), M4 (stream), M3 (đồng bộ nếu cần)
// PORT MẶC ĐỊNH: 8888
// ============================================================
import java.io.*;
import java.net.*;

// ════════════════════════════════════════════════════════════
//  FILE 1/3 – SERVER  (chạy TRƯỚC)
// ════════════════════════════════════════════════════════════
class M6a_Server {
    static final int PORT = 8888;       // TODO: đổi port nếu cần

    public static void main(String[] args) throws IOException {
        try (ServerSocket ss = new ServerSocket(PORT)) {
            System.out.println("Server lang nghe port " + PORT + " ...");
            int count = 0;
            while (true) {
                Socket client = ss.accept();
                count++;
                System.out.println("Client #" + count + " ket noi!");
                new M6b_Handler(client, count).start();
            }
        }
    }
}

// ════════════════════════════════════════════════════════════
//  FILE 2/3 – HANDLER  (1 thread = 1 client)
// ════════════════════════════════════════════════════════════
class M6b_Handler extends Thread {
    private Socket socket;
    private int    clientId;

    public M6b_Handler(Socket socket, int clientId) {
        this.socket   = socket;
        this.clientId = clientId;
    }

    @Override
    public void run() {
        try (BufferedReader reader = new BufferedReader(
                 new InputStreamReader(socket.getInputStream()));
             PrintWriter writer = new PrintWriter(socket.getOutputStream(), true)) {

            // Gửi chào (tuỳ đề)
            writer.println("Chao client #" + clientId + "! Go 'exit' de thoat.");

            String message;
            while ((message = reader.readLine()) != null) {
                if (message.equalsIgnoreCase("exit")) {
                    writer.println("Bye!");
                    break;
                }

                System.out.println("Client #" + clientId + " gui: " + message);

                // ── Xử lý – SỬA Ở ĐÂY ─────────────────────
                String result = xuLy(message);

                writer.println(result);     // gửi về client (tự flush vì true)
            }

        } catch (IOException e) { /* bỏ qua */ }
        finally {
            try { socket.close(); } catch (IOException e) {}
        }
        System.out.println("Client #" + clientId + " ngat ket noi.");
    }

    // ── HÀM XỬ LÝ – SỬA Ở ĐÂY ─────────────────────────────
    private String xuLy(String msg) {
        // TODO: đổi theo đề bài
        return "Echo: " + msg;

        // --- Ví dụ các biến thể ---
        // return msg.toUpperCase();                     // chuyển hoa
        // return msg.toLowerCase();                     // chuyển thường
        // return "So ky tu: " + msg.length();           // đếm ký tự
        // try {                                         // tổng các số
        //     String[] parts = msg.split("\\s+");
        //     int sum = 0;
        //     for (String p : parts) sum += Integer.parseInt(p);
        //     return "Tong: " + sum;
        // } catch (NumberFormatException e) {
        //     return "Loi: nhap so cach nhau bang dau cach";
        // }
        // try {                                         // chẵn lẻ
        //     int n = Integer.parseInt(msg.trim());
        //     return n + " la so " + (n % 2 == 0 ? "Chan" : "Le");
        // } catch (NumberFormatException e) {
        //     return "Loi: vui long nhap so nguyen";
        // }
    }
}

// ════════════════════════════════════════════════════════════
//  FILE 3/3 – CLIENT  (chạy SAU khi server đã chạy)
// ════════════════════════════════════════════════════════════
class M6c_Client {
    static final String HOST = "localhost"; // TODO: đổi IP nếu khác máy
    static final int    PORT = 8888;

    public static void main(String[] args) throws IOException {
        try (Socket socket = new Socket(HOST, PORT);
             BufferedReader serverIn = new BufferedReader(
                 new InputStreamReader(socket.getInputStream()));
             PrintWriter serverOut = new PrintWriter(socket.getOutputStream(), true);
             BufferedReader userIn  = new BufferedReader(
                 new InputStreamReader(System.in))) {

            System.out.println("Da ket noi server " + HOST + ":" + PORT);
            // Nhận chào mừng (nếu có)
            System.out.println(serverIn.readLine());

            String input;
            while (true) {
                System.out.print("Nhap: ");
                input = userIn.readLine();
                if (input == null) break;

                serverOut.println(input);           // gửi tới server

                String resp = serverIn.readLine();  // nhận từ server
                System.out.println("Server: " + resp);

                if ("exit".equalsIgnoreCase(input)) break;
            }
        }
    }
}

/*
 GHÉP VỚI MODULE KHÁC:
 ┌─────────────────────────────────────────────────────────┐
 │  Đề: Chat 2 chiều realtime (client nhận bất kỳ lúc)   │
 │  → Client tạo thêm 1 thread chỉ để đọc từ server:      │
 │    new Thread(() -> {                                   │
 │        try { while(true) println(serverIn.readLine());  │
 │        } catch(IOException e){}                         │
 │    }).start();                                          │
 ├─────────────────────────────────────────────────────────┤
 │  Đề: Ghi log tất cả tin nhắn vào file                  │
 │  → Thêm FileWriter fw = new FileWriter("log.txt",true) │
 │    trong Handler, fw.write(message + "\n");             │
 └─────────────────────────────────────────────────────────┘

 KHÁC BIỆT VỚI M5:
 M5 (DataStream) → truyền int/long/String nhị phân, dùng writeInt/readInt
 M6 (Text)       → truyền dòng văn bản, dùng println/readLine, dễ debug hơn
*/
