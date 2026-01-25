package Bai1_ReverseString;

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

/**
 * Server Class cho Bài 1: Đảo ngược chuỗi
 * Nhiệm vụ:
 * 1. Lắng nghe kết nối từ Client.
 * 2. Nhận chuỗi từ Client.
 * 3. Đảo ngược chuỗi.
 * 4. Gửi chuỗi đã đảo ngược về lại Client.
 */
public class Server {
    public static void main(String[] args) {
        // Cổng (Port) mà Server sẽ lắng nghe.
        // Các số hiệu cổng dưới 1024 thường dành cho hệ thống (System ports reserved).
        // Nên chọn cổng lớn hơn 1024.
        int port = 1234;

        try {
            // 1. Tạo ServerSocket và lắng nghe tại cổng đã định
            ServerSocket serverSocket = new ServerSocket(port);
            System.out.println("Server đang chạy tại cổng " + port + "...");
            System.out.println("Đang chờ kết nối từ Client...");

            while (true) {
                // 2. Chấp nhận kết nối từ Client
                // Phương thức accept() sẽ block (dừng) chương trình cho đến khi có Client kết nối
                Socket socket = serverSocket.accept();
                System.out.println("Client đã kết nối: " + socket.getInetAddress());

                // 3. Tạo luồng input/output để giao tiếp với Client
                // InputStreamReader: Đọc byte và chuyển thành ký tự
                // BufferedReader: Đọc văn bản hiệu quả
                // PrintWriter: Gửi văn bản đi dễ dàng
                InputStream is = socket.getInputStream();
                BufferedReader br = new BufferedReader(new InputStreamReader(is));

                OutputStream os = socket.getOutputStream();
                PrintWriter pw = new PrintWriter(os, true); // true để auto-flush dữ liệu đi ngay

                // 4. Nhận dữ liệu từ Client
                String inputLine = br.readLine();
                if (inputLine != null) {
                    System.out.println("Nhận từ Client: " + inputLine);

                    // 5. Xử lý logic: Đảo ngược chuỗi
                    // Sử dụng StringBuilder để đảo ngược dễ dàng
                    String reversedString = new StringBuilder(inputLine).reverse().toString();
                    System.out.println("Chuỗi sau khi đảo: " + reversedString);

                    // 6. Gửi kết quả về Client
                    pw.println(reversedString);
                }

                // 7. Đóng kết nối với Client hiện tại (để chờ Client mới trong vòng lặp)
                // Trong thực tế có thể dùng Thread để xử lý đa luồng (nhiều client cùng lúc)
                socket.close();
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
