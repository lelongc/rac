import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;

// FILE 3: CLIENT
// - Kết nối tới server
// - Gửi từng ký tự (byte) → nhận lại kết quả
public class tcpClient {
    public static int PORT = 5678;

    public static void main(String[] args) {
        try {
            // === KẾT NỐI ===
            Socket client = new Socket("localhost", PORT);
            System.out.println("Da ket noi toi server!");

            // === XỬ LÝ (Stream kiểu int/byte) ===
            OutputStream os = client.getOutputStream(); // gửi tới server
            InputStream is = client.getInputStream();   // nhận từ server

            // Gửi các ký tự 'a' đến 'e'
            for (int i = 'a'; i <= 'e'; i++) {
                os.write(i); // gửi 1 byte

                int ketQua = is.read(); // nhận 1 byte từ server
                System.out.println("Gui: " + (char) i + "  |  Nhan lai: " + (char) ketQua);
            }

            // === ĐÓNG KẾT NỐI ===
            client.close();
            System.out.println("Da ngat ket noi!");
        } catch (Exception e) {
            System.out.println("Loi client: " + e);
        }
    }
}
