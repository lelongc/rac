import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

/**
 * ChatClient - Kết nối tới ChatServer qua Socket.
 * Hỗ trợ 2 luồng: 1 luồng đọc tin nhắn từ Server và 1 luồng gửi tin từ bàn phím.
 * 
 * Môn: Phát triển hệ thống phân tán - IUH
 */
public class ChatClient {
    public static final String DEFAULT_HOST = "localhost";
    public static final int DEFAULT_PORT = 5000;

    public static void main(String[] args) {
        String host = DEFAULT_HOST;
        int port = DEFAULT_PORT;
        String defaultUsername = null;

        // Ưu tiên đọc từ biến môi trường nếu có
        String envHost = System.getenv("SERVER_HOST");
        if (envHost != null && !envHost.trim().isEmpty()) {
            host = envHost.trim();
        }

        String envPort = System.getenv("SERVER_PORT");
        if (envPort != null && !envPort.trim().isEmpty()) {
            try {
                port = Integer.parseInt(envPort.trim());
            } catch (NumberFormatException ignored) {}
        }

        String envUser = System.getenv("CHAT_USER");
        if (envUser != null && !envUser.trim().isEmpty()) {
            defaultUsername = envUser.trim();
        }

        // Tham số dòng lệnh: java ChatClient [host] [port] [username]
        if (args.length > 0 && !args[0].trim().isEmpty()) {
            host = args[0].trim();
        }
        if (args.length > 1) {
            try {
                port = Integer.parseInt(args[1].trim());
            } catch (NumberFormatException ignored) {}
        }
        if (args.length > 2) {
            defaultUsername = args[2].trim();
        }

        System.out.println("=================================================");
        System.out.println("      SOCKET CHAT CLIENT - HE PHAN TAN IUH      ");
        System.out.println("=================================================");
        System.out.println("[CLIENT] Đang kết nối tới Server: " + host + ":" + port + "...");

        try {
            Socket socket = new Socket(host, port);
            System.out.println("[CLIENT] Kết nối Server thành công!\n");

            BufferedReader serverReader = new BufferedReader(new InputStreamReader(socket.getInputStream(), "UTF-8"));
            PrintWriter serverWriter = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader consoleReader = new BufferedReader(new InputStreamReader(System.in, "UTF-8"));

            // Luồng phụ: Liên tục nhận tin nhắn từ Server và in ra màn hình
            Thread readThread = new Thread(() -> {
                try {
                    String serverMessage;
                    while ((serverMessage = serverReader.readLine()) != null) {
                        System.out.println(serverMessage);
                    }
                } catch (IOException e) {
                    System.out.println("[CLIENT] Đã ngắt kết nối với Server.");
                } finally {
                    try {
                        socket.close();
                    } catch (IOException ignored) {}
                    System.exit(0);
                }
            });
            readThread.setDaemon(true);
            readThread.start();

            // Nếu có sẵn username truyền qua biến môi trường hoặc tham số
            if (defaultUsername != null && !defaultUsername.isEmpty()) {
                // Chờ đọc câu chào hỏi đầu tiên nếu có rồi gửi tên
                serverWriter.println(defaultUsername);
            }

            // Luồng chính: Đọc dữ liệu từ Console của người dùng và gửi lên Server
            String userInput;
            while ((userInput = consoleReader.readLine()) != null) {
                serverWriter.println(userInput);
                if (userInput.trim().equalsIgnoreCase("exit") || userInput.trim().equalsIgnoreCase("quit")) {
                    System.out.println("[CLIENT] Đang thoát ứng dụng chat...");
                    break;
                }
            }

            socket.close();
        } catch (IOException e) {
            System.err.println("[LỖI KẾT NỐI] Không thể kết nối tới Server " + host + ":" + port);
            System.err.println("Chi tiết: " + e.getMessage());
            System.err.println("Hãy chắc chắn rằng ChatServer đã được bật!");
        }
    }
}
