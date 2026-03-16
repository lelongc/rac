import java.io.*;
import java.net.*;

public class Server {
    private static final int PORT = 6789;

    public static void main(String[] args) {
        System.out.println("Server TCP (Xử lý chuỗi) đang lắng nghe tại cổng " + PORT + "...");
        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
            while (true) {
                Socket clientSocket = serverSocket.accept();
                System.out.println("Kết nối từ: " + clientSocket.getInetAddress());

                BufferedReader in = new BufferedReader(
                        new InputStreamReader(clientSocket.getInputStream(), "UTF-8"));
                PrintWriter out = new PrintWriter(
                        new OutputStreamWriter(clientSocket.getOutputStream(), "UTF-8"), true);

                String received = in.readLine();
                if (received != null) {
                    String upperCase = received.toUpperCase();
                    int charCount = received.length();
                    out.println("Chuỗi viết hoa: " + upperCase);
                    out.println("Số ký tự: " + charCount);
                }

                clientSocket.close();
            }
        } catch (IOException e) {
            System.out.println("Lỗi server: " + e.getMessage());
        }
    }
}
