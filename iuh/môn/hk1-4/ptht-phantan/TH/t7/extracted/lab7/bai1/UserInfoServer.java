package lab7.bai1;

import java.io.*;
import java.net.*;
import java.util.*;

public class UserInfoServer {
    private static final Map<String, String> userData = new HashMap<>();

    static {
        userData.put("abcd1234@gmail.com", "Henry Ford 0932 622 268");
        userData.put("sinhvien@iuh.edu.vn", "Long Le 0909 123 456");
    }

    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(12345)) {
            System.out.println("User Info Server (TCP) đang chạy ở port 12345...");
            while (true) {
                Socket socket = serverSocket.accept();
                new Thread(() -> handleClient(socket)).start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void handleClient(Socket socket) {
        try (
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true)
        ) {
            String email = in.readLine();
            if (email != null) {
                System.out.println("Đã nhận yêu cầu tìm kiếm email: " + email);
                String info = userData.get(email.trim());
                
                if (info != null) {
                    out.println(email + " và " + info);
                } else {
                    out.println(email + " (Không tìm thấy thông tin trên Server)");
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
