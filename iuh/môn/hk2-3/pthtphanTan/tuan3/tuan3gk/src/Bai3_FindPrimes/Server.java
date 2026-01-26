package Bai3_FindPrimes;

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;

/**
 * Server Class cho Bài 3: Tìm số nguyên tố
 * Nhiệm vụ:
 * 1. Nhận danh sách số.
 * 2. Lọc ra các số nguyên tố.
 * 3. Trả về danh sách các số nguyên tố.
 */
public class Server {
    public static void main(String[] args) {
        int port = 3000;

        try {
            ServerSocket serverSocket = new ServerSocket(port);
            System.out.println("Server Bai 3 đang chạy tại cổng " + port + "...");

            while (true) {
                Socket socket = serverSocket.accept();
                System.out.println("Client Bai 3 đã kết nối.");

                BufferedReader br = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                PrintWriter pw = new PrintWriter(socket.getOutputStream(), true);

                String inputLine = br.readLine();
                if (inputLine != null) {
                    System.out.println("Nhận dữ liệu: " + inputLine);
                    String result = filterPrimes(inputLine);
                    System.out.println("Kết quả (số nguyên tố): " + result);
                    pw.println(result);
                }
                socket.close();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static String filterPrimes(String input) {
        String[] parts = input.split(",");
        List<Integer> primes = new ArrayList<>();

        for (String part : parts) {
            try {
                int num = Integer.parseInt(part.trim());
                if (isPrime(num)) {
                    primes.add(num);
                }
            } catch (NumberFormatException e) {
                // Ignore non-numbers
            }
        }

        if (primes.isEmpty())
            return "Không có số nguyên tố nào.";

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < primes.size(); i++) {
            sb.append(primes.get(i));
            if (i < primes.size() - 1) {
                sb.append(", ");
            }
        }
        return sb.toString();
    }

    private static boolean isPrime(int n) {
        if (n <= 1)
            return false;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0)
                return false;
        }
        return true;
    }
}
