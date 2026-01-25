package Bai2_SortNumbers;

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Server Class cho Bài 2: Sắp xếp số
 * Nhiệm vụ:
 * 1. Nhận chuỗi các số từ Client (ví dụ: "5,1,9,3").
 * 2. Tách chuỗi thành các số nguyên.
 * 3. Sắp xếp tăng dần.
 * 4. Gửi kết quả về Client.
 */
public class Server {
    public static void main(String[] args) {
        int port = 2000; // Chọn cổng khác bài 1 để tránh xung đột nếu chạy cùng lúc

        try {
            ServerSocket serverSocket = new ServerSocket(port);
            System.out.println("Server Bai 2 đang chạy tại cổng " + port + "...");

            while (true) {
                Socket socket = serverSocket.accept();
                System.out.println("Client Bai 2 đã kết nối.");

                BufferedReader br = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                PrintWriter pw = new PrintWriter(socket.getOutputStream(), true);

                String inputLine = br.readLine();
                if (inputLine != null) {
                    System.out.println("Nhận dữ liệu: " + inputLine);

                    try {
                        // Xử lý logic
                        String result = sortNumbers(inputLine);
                        System.out.println("Kết quả: " + result);
                        pw.println(result);
                    } catch (NumberFormatException e) {
                        pw.println("Lỗi: Dữ liệu nhập không hợp lệ. Hãy nhập các số cách nhau bởi dấu phẩy.");
                    }
                }

                socket.close();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // Hàm tách và sắp xếp số
    private static String sortNumbers(String input) {
        String[] parts = input.split(",");
        List<Integer> numbers = new ArrayList<>();
        
        for (String part : parts) {
            numbers.add(Integer.parseInt(part.trim()));
        }

        Collections.sort(numbers);

        // Chuyển lại thành chuỗi
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < numbers.size(); i++) {
            sb.append(numbers.get(i));
            if (i < numbers.size() - 1) {
                sb.append(", ");
            }
        }
        return sb.toString();
    }
}
