import java.io.*;
import java.net.*;

// FILE 3: CLIENT
// - Kết nối tới server
// - Đọc input từ bàn phím → gửi → nhận phản hồi
// - Gõ 'exit' để thoát
public class TCPClient {
    public static int PORT = 8888;

    public static void main(String[] args) {
        try {
            // === KẾT NỐI ===
            Socket client = new Socket("localhost", PORT);
            System.out.println("Da ket noi toi server!");

            // === XỬ LÝ (Stream kiểu String) ===
            // InputStream (byte) → InputStreamReader (byte→char) → BufferedReader (buffer + dòng)
            BufferedReader reader = new BufferedReader(
                    new InputStreamReader(client.getInputStream()));

            PrintWriter writer = new PrintWriter(client.getOutputStream(), true);

            // Đọc input từ bàn phím
            BufferedReader keyboard = new BufferedReader(new InputStreamReader(System.in));

            String userInput;
            while (true) {
                System.out.print("Nhap tin nhan (exit de thoat): ");
                userInput = keyboard.readLine();

                if (userInput.equalsIgnoreCase("exit")) break;

                // Gửi tin nhắn tới server
                writer.println(userInput);

                // Nhận phản hồi từ server
                String response = reader.readLine();
                System.out.println("Nhan tu server: " + response);
            }

            // === ĐÓNG KẾT NỐI ===
            reader.close();
            writer.close();
            keyboard.close();
            client.close();
            System.out.println("Da ngat ket noi!");
        } catch (Exception e) {
            System.out.println("Loi client: " + e);
        }
    }
}
