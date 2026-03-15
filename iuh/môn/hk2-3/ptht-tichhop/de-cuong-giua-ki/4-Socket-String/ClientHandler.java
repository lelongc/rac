import java.io.*;
import java.net.*;

// FILE 2: THREAD XỬ LÝ (th_processing)
// - Nhận 1 Socket client
// - Đọc String theo từng dòng (BufferedReader) → xử lý → gửi lại (PrintWriter)
// Chuỗi stream: InputStream → InputStreamReader → BufferedReader
public class ClientHandler extends Thread {
    private Socket client;
    private int clientId;

    public ClientHandler(Socket client, int clientId) {
        this.client = client;
        this.clientId = clientId;
    }

    @Override
    public void run() {
        try {
            // === THÔNG TIN CLIENT (InetAddress) ===
            System.out.println("===== Client #" + clientId + " =====");
            System.out.println("IP   : " + client.getInetAddress().getHostAddress());
            System.out.println("Port : " + client.getPort());
            System.out.println("========================");

            // === XỬ LÝ (Stream kiểu String) ===
            // InputStream (byte) → InputStreamReader (byte→char) → BufferedReader (buffer + dòng)
            BufferedReader reader = new BufferedReader(
                    new InputStreamReader(client.getInputStream()));

            // PrintWriter: true = auto flush (tự gửi ngay khi println)
            PrintWriter writer = new PrintWriter(client.getOutputStream(), true);

            String message;
            // readLine() trả null khi client ngắt kết nối
            while ((message = reader.readLine()) != null) {
                System.out.println("Client #" + clientId + " gui: " + message);

                // Xử lý: chuyển thành chữ hoa rồi gửi lại
                String phanHoi = "Server phan hoi: " + message.toUpperCase();
                writer.println(phanHoi);
            }

            System.out.println("Client #" + clientId + " ngat ket noi!");

            // === ĐÓNG KẾT NỐI ===
            reader.close();
            writer.close();
            client.close();
        } catch (Exception e) {
            System.out.println("Loi client #" + clientId + ": " + e);
        }
    }
}
