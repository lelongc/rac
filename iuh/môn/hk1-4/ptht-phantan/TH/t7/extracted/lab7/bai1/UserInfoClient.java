package lab7.bai1;

import java.io.*;
import java.net.*;
import java.util.Scanner;

public class UserInfoClient {
    public static void main(String[] args) {
        try (Socket socket = new Socket("localhost", 12345);
             PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
             BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
             Scanner scanner = new Scanner(System.in)) {

            System.out.print("Nhập email cần tìm (VD: abcd1234@gmail.com): ");
            String email = scanner.nextLine();

            out.println(email);

            String response = in.readLine();
            System.out.println("Kết quả từ Server: " + response);

        } catch (IOException e) {
            System.out.println("Lỗi kết nối tới Server. Hãy chắc chắn Server đang chạy.");
            e.printStackTrace();
        }
    }
}
