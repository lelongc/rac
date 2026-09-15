import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.util.List;
import java.util.concurrent.CopyOnWriteArrayList;

/**
 * ChatServer - ServerSocket nhận kết nối từ nhiều Client (Đa luồng).
 * Khi 1 Client gửi tin nhắn -> Server broadcast cho tất cả Client khác.
 * 
 * Môn: Phát triển hệ thống phân tán - IUH
 */
public class ChatServer {
    public static final int DEFAULT_PORT = 5000;
    private static final DateTimeFormatter TIME_FORMATTER = DateTimeFormatter.ofPattern("HH:mm:ss");

    // Danh sách các ClientHandler đang kết nối (thread-safe)
    private static final List<ClientHandler> clients = new CopyOnWriteArrayList<>();

    public static void main(String[] args) {
        int port = DEFAULT_PORT;

        // Ưu tiên đọc port từ tham số dòng lệnh hoặc biến môi trường PORT
        if (args.length > 0) {
            try {
                port = Integer.parseInt(args[0]);
            } catch (NumberFormatException e) {
                System.out.println("[CẢNH BÁO] Port không hợp lệ, sử dụng mặc định: " + DEFAULT_PORT);
            }
        } else {
            String envPort = System.getenv("PORT");
            if (envPort != null && !envPort.trim().isEmpty()) {
                try {
                    port = Integer.parseInt(envPort.trim());
                } catch (NumberFormatException ignored) {}
            }
        }

        System.out.println("=================================================");
        System.out.println("      SOCKET CHAT SERVER - HE PHAN TAN IUH      ");
        System.out.println("=================================================");
        System.out.println("[SERVER] Đang khởi động Server trên cổng: " + port + "...");

        try (ServerSocket serverSocket = new ServerSocket(port)) {
            System.out.println("[SERVER] Server đã sẵn sàng lắng nghe kết nối từ các Client!");

            while (true) {
                Socket clientSocket = serverSocket.accept();
                System.out.println("[SERVER] Phát hiện kết nối mới từ: " 
                        + clientSocket.getRemoteSocketAddress());

                ClientHandler handler = new ClientHandler(clientSocket);
                clients.add(handler);

                // Khởi chạy 1 luồng riêng biệt để phục vụ client này
                new Thread(handler).start();
                System.out.println("[SERVER] Số lượng Client hiện tại: " + clients.size());
            }
        } catch (IOException e) {
            System.err.println("[LỖI SERVER] " + e.getMessage());
        }
    }

    /**
     * Broadcast tin nhắn tới tất cả client khác (ngoại trừ người gửi)
     */
    public static void broadcast(String message, ClientHandler sender) {
        String timestamp = LocalTime.now().format(TIME_FORMATTER);
        String formattedMsg = "[" + timestamp + "] " + message;
        System.out.println("[LOG TIN NHẮN] " + formattedMsg);

        for (ClientHandler client : clients) {
            if (client != sender) {
                client.sendMessage(formattedMsg);
            }
        }
    }

    /**
     * Broadcast thông báo hệ thống tới toàn bộ client
     */
    public static void broadcastSystem(String message) {
        String timestamp = LocalTime.now().format(TIME_FORMATTER);
        String formattedMsg = "[" + timestamp + "] [HỆ THỐNG] " + message;
        System.out.println("[LOG HỆ THỐNG] " + formattedMsg);

        for (ClientHandler client : clients) {
            client.sendMessage(formattedMsg);
        }
    }

    /**
     * Xóa client khi ngắt kết nối
     */
    public static void removeClient(ClientHandler handler) {
        clients.remove(handler);
        System.out.println("[SERVER] Client ngắt kết nối. Số lượng Client còn lại: " + clients.size());
    }

    /**
     * Lớp ClientHandler quản lý từng kết nối Client trên 1 Thread riêng
     */
    static class ClientHandler implements Runnable {
        private final Socket socket;
        private BufferedReader reader;
        private PrintWriter writer;
        private String clientName = "Khách";

        public ClientHandler(Socket socket) {
            this.socket = socket;
        }

        public String getClientName() {
            return clientName;
        }

        @Override
        public void run() {
            try {
                reader = new BufferedReader(new InputStreamReader(socket.getInputStream(), "UTF-8"));
                writer = new PrintWriter(socket.getOutputStream(), true);

                // Gửi thông điệp chào mừng và yêu cầu nhập tên
                writer.println("XIN CHÀO! Vui lòng nhập tên hiển thị (Username) của bạn:");
                String nameInput = reader.readLine();

                if (nameInput != null && !nameInput.trim().isEmpty()) {
                    clientName = nameInput.trim();
                } else {
                    clientName = "User_" + socket.getPort();
                }

                writer.println("[HỆ THỐNG] Chào mừng " + clientName + " đã tham gia phòng chat!");
                writer.println("[HỆ THỐNG] Gõ tin nhắn và nhấn Enter để chat. Gõ 'exit' hoặc 'quit' để thoát.");

                // Thông báo cho tất cả client khác
                ChatServer.broadcastSystem(clientName + " đã tham gia phòng chat.");

                // Vòng lặp nhận tin nhắn từ client
                String clientMessage;
                while ((clientMessage = reader.readLine()) != null) {
                    clientMessage = clientMessage.trim();
                    if (clientMessage.equalsIgnoreCase("exit") || clientMessage.equalsIgnoreCase("quit")) {
                        break;
                    }

                    if (!clientMessage.isEmpty()) {
                        // Broadcast tin nhắn tới tất cả client khác
                        ChatServer.broadcast(clientName + ": " + clientMessage, this);
                    }
                }
            } catch (IOException e) {
                System.out.println("[SERVER] Mất kết nối đột ngột từ: " + clientName);
            } finally {
                closeConnection();
            }
        }

        public void sendMessage(String message) {
            if (writer != null) {
                writer.println(message);
            }
        }

        private void closeConnection() {
            try {
                ChatServer.removeClient(this);
                ChatServer.broadcastSystem(clientName + " đã rời phòng chat.");
                if (socket != null && !socket.isClosed()) {
                    socket.close();
                }
            } catch (IOException ignored) {}
        }
    }
}
