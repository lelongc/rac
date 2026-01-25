package Bai1_ReverseString;

import java.io.*;
import java.net.Socket;
import java.util.Scanner;

/**
 * Client Class cho Bài 1: Đảo ngược chuỗi
 * Nhiệm vụ:
 * 1. Kết nối tới Server.
 * 2. Nhập chuỗi từ bàn phím.
 * 3. Gửi chuỗi lên Server.
 * 4. Nhận kết quả đã đảo ngược từ Server và in ra.
 */
public class Client {
    public static void main(String[] args) {
        // Địa chỉ IP của Server. "localhost" hoặc "127.0.0.1" là máy hiện tại.
        String serverHost = "localhost";
        // Cổng phải trùng với cổng mà Server đang mở
        int serverPort = 1234;

        try {
            // 1. Tạo Socket để kết nối tới Server
            System.out.println("Đang kết nối tới Server...");
            Socket socket = new Socket(serverHost, serverPort);
            System.out.println("Đã kết nối thành công!");

            // 2. Tạo luồng input/output để giao tiếp
            // Luồng để gửi dữ liệu đi (Output)
            PrintWriter pw = new PrintWriter(socket.getOutputStream(), true);
            // Luồng để nhận dữ liệu về (Input)
            BufferedReader br = new BufferedReader(new InputStreamReader(socket.getInputStream()));

            // Scanner để nhập dữ liệu từ bàn phím
            Scanner scanner = new Scanner(System.in);

            System.out.print("Nhập chuỗi cần đảo ngược: ");
            String inputString = scanner.nextLine();

            // 3. Gửi chuỗi lên Server
            pw.println(inputString);

            // 4. Nhận kết quả trả về từ Server
            String response = br.readLine();
            System.out.println("Kết quả từ Server: " + response);

            // 5. Đóng kết nối
            socket.close();
            scanner.close();

        } catch (IOException e) {
            System.out.println("Không thể kết nối tới Server. Hãy chắc chắn Server đang chạy.");
            e.printStackTrace();
        }
    }
}
