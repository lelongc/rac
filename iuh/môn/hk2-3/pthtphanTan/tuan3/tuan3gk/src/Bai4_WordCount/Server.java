package Bai4_WordCount;

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.HashMap;
import java.util.Map;

/**
 * Server Class cho Bài 4: Đếm số lần xuất hiện của từ
 * Nhiệm vụ:
 * 1. Nhận một chuỗi văn bản từ Client.
 * 2. Tách từ và đếm tần suất xuất hiện.
 * 3. Gửi kết quả (Map) dạng chuỗi về Client.
 */
public class Server {
    public static void main(String[] args) {
        int port = 4000;

        try {
            ServerSocket serverSocket = new ServerSocket(port);
            System.out.println("Server Bai 4 đang chạy tại cổng " + port + "...");

            while (true) {
                Socket socket = serverSocket.accept();
                System.out.println("Client Bai 4 đã kết nối.");

                BufferedReader br = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                PrintWriter pw = new PrintWriter(socket.getOutputStream(), true);

                String inputLine = br.readLine();
                if (inputLine != null) {
                    System.out.println("Nhận dữ liệu: " + inputLine);
                    String result = countWordFrequency(inputLine);
                    System.out.println("Kết quả: " + result);
                    pw.println(result);
                }
                socket.close();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static String countWordFrequency(String input) {
        // Tách từ theo khoảng trắng
        String[] words = input.trim().split("\\s+");
        Map<String, Integer> wordCount = new HashMap<>();

        for (String word : words) {
            // Chuyển về chữ thường để đếm không phân biệt hoa thường
            String w = word.toLowerCase();
            wordCount.put(w, wordCount.getOrDefault(w, 0) + 1);
        }

        // Chuyển Map thành String để gửi đi
        StringBuilder sb = new StringBuilder();
        for (Map.Entry<String, Integer> entry : wordCount.entrySet()) {
            sb.append(entry.getKey()).append(":").append(entry.getValue()).append("; ");
        }
        return sb.toString();
    }
}
