import java.io.*;
import java.net.*;

public class Server {
    private static final int PORT = 6789;

    public static void main(String[] args) {
        System.out.println("Server TCP (Giai thừa) đang lắng nghe tại cổng " + PORT + "...");
        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
            while (true) {
                Socket clientSocket = serverSocket.accept();
                System.out.println("Kết nối từ: " + clientSocket.getInetAddress());

                BufferedReader in = new BufferedReader(
                        new InputStreamReader(clientSocket.getInputStream()));
                PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);

                String line = in.readLine();
                try {
                    int n = Integer.parseInt(line.trim());
                    if (n < 0) {
                        out.println("Lỗi: Không tính giai thừa của số âm.");
                    } else {
                        long result = factorial(n);
                        out.println("Giai thừa của " + n + " = " + result);
                    }
                } catch (NumberFormatException e) {
                    out.println("Lỗi: Giá trị không hợp lệ.");
                }

                clientSocket.close();
            }
        } catch (IOException e) {
            System.out.println("Lỗi server: " + e.getMessage());
        }
    }

    private static long factorial(int n) {
        if (n == 0 || n == 1) return 1;
        long result = 1;
        for (int i = 2; i <= n; i++) {
            result *= i;
        }
        return result;
    }
}
