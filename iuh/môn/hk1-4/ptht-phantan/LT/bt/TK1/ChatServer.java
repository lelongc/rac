import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.util.List;
import java.util.concurrent.CopyOnWriteArrayList;

public class ChatServer {
    public static final int DEFAULT_PORT = 5000;
    public static final String DEFAULT_ROOM = "general";
    public static final String LOG_FILE = "chatroom.log";
    public static final DateTimeFormatter TIME_FORMAT = DateTimeFormatter.ofPattern("HH:mm:ss");

    private static final List<ClientHandler> clients = new CopyOnWriteArrayList<>();

    public static void main(String[] args) {
        int port = DEFAULT_PORT;
        if (args.length > 0) {
            try {
                port = Integer.parseInt(args[0]);
            } catch (NumberFormatException ignored) {}
        } else {
            String envPort = System.getenv("SERVER_PORT");
            if (envPort == null || envPort.trim().isEmpty()) {
                envPort = System.getenv("PORT");
            }
            if (envPort != null && !envPort.trim().isEmpty()) {
                try {
                    port = Integer.parseInt(envPort.trim());
                } catch (NumberFormatException ignored) {}
            }
        }

        System.out.println("==================================================");
        System.out.println("  MULTI-ROOM CHAT SERVER - DE 2 THUONG KY 1       ");
        System.out.println("==================================================");
        System.out.println("[SERVER] Dang lang nghe tai cong: " + port);
        System.out.println("[SERVER] Phong mac dinh: " + DEFAULT_ROOM);
        System.out.println("[SERVER] File log: " + LOG_FILE);

        try (ServerSocket serverSocket = new ServerSocket()) {
            serverSocket.setReuseAddress(true);
            serverSocket.bind(new java.net.InetSocketAddress(port));
            while (true) {
                Socket clientSocket = serverSocket.accept();
                ClientHandler handler = new ClientHandler(clientSocket);
                clients.add(handler);
                new Thread(handler).start();
            }
        } catch (IOException e) {
            System.err.println("[SERVER ERROR] " + e.getMessage());
        }
    }

    public static synchronized void logChat(String room, String nickname, String message) {
        String time = LocalTime.now().format(TIME_FORMAT);
        String logLine = String.format("[%s][%s][%s]: %s", room, nickname, time, message);
        System.out.println(logLine);

        try (FileWriter fw = new FileWriter(LOG_FILE, true);
             BufferedWriter bw = new BufferedWriter(fw);
             PrintWriter pw = new PrintWriter(bw)) {
            pw.println(logLine);
        } catch (IOException e) {
            System.err.println("[LOG ERROR] Khong the ghi log: " + e.getMessage());
        }
    }

    public static void broadcastRoom(String room, String senderNick, String message, ClientHandler sender) {
        String time = LocalTime.now().format(TIME_FORMAT);
        String formatted = String.format("[%s][%s][%s]: %s", room, senderNick, time, message);

        logChat(room, senderNick, message);

        for (ClientHandler client : clients) {
            if (client.getRoom().equalsIgnoreCase(room) && client != sender) {
                client.sendMessage(formatted);
            }
        }
    }

    public static void broadcastRoomSystem(String room, String message) {
        String time = LocalTime.now().format(TIME_FORMAT);
        String formatted = String.format("[%s][HE THONG][%s]: %s", room, time, message);
        System.out.println(formatted);

        for (ClientHandler client : clients) {
            if (client.getRoom().equalsIgnoreCase(room)) {
                client.sendMessage(formatted);
            }
        }
    }

    public static void removeClient(ClientHandler client) {
        clients.remove(client);
        System.out.println("[SERVER] Client '" + client.getNickname() + "' da thoat. So luong con lai: " + clients.size());
    }

    static class ClientHandler implements Runnable {
        private final Socket socket;
        private BufferedReader in;
        private PrintWriter out;
        private String nickname = "Anonymous";
        private String room = DEFAULT_ROOM;

        public ClientHandler(Socket socket) {
            this.socket = socket;
        }

        public String getNickname() {
            return nickname;
        }

        public String getRoom() {
            return room;
        }

        public void setRoom(String room) {
            this.room = room;
        }

        public void sendMessage(String msg) {
            if (out != null) {
                out.println(msg);
            }
        }

        @Override
        public void run() {
            try {
                in = new BufferedReader(new InputStreamReader(socket.getInputStream(), "UTF-8"));
                out = new PrintWriter(socket.getOutputStream(), true);

                String nickInput = in.readLine();
                if (nickInput != null && !nickInput.trim().isEmpty()) {
                    nickname = nickInput.trim();
                }

                String roomInput = in.readLine();
                if (roomInput != null && !roomInput.trim().isEmpty()) {
                    room = roomInput.trim();
                } else {
                    room = DEFAULT_ROOM;
                }

                System.out.println("[SERVER] Client ket noi: " + nickname + " vao phong [" + room + "]");
                out.println("[HE THONG] Chao mung " + nickname + " den voi phong [" + room + "]!");
                out.println("[HE THONG] Dung lenh '/join <ten_phong>' de chuyen phong. Go 'exit' de thoat.");

                broadcastRoomSystem(room, nickname + " da gia nhap phong.");

                String line;
                while ((line = in.readLine()) != null) {
                    line = line.trim();
                    if (line.equalsIgnoreCase("exit") || line.equalsIgnoreCase("quit") || line.equalsIgnoreCase("/quit")) {
                        break;
                    }

                    if (line.startsWith("/join ")) {
                        String newRoom = line.substring(6).trim();
                        if (!newRoom.isEmpty() && !newRoom.equalsIgnoreCase(room)) {
                            String oldRoom = room;
                            broadcastRoomSystem(oldRoom, nickname + " da roi phong.");
                            room = newRoom;
                            out.println("[HE THONG] Ban da chuyen sang phong [" + room + "].");
                            broadcastRoomSystem(room, nickname + " da gia nhap phong.");
                        } else if (newRoom.equalsIgnoreCase(room)) {
                            out.println("[HE THONG] Ban da o trong phong [" + room + "] roi.");
                        }
                        continue;
                    }

                    if (!line.isEmpty()) {
                        broadcastRoom(room, nickname, line, this);
                    }
                }
            } catch (IOException e) {
                System.out.println("[SERVER] Mat ket noi voi: " + nickname);
            } finally {
                cleanup();
            }
        }

        private void cleanup() {
            removeClient(this);
            broadcastRoomSystem(room, nickname + " da roi phong chat.");
            try {
                if (in != null) in.close();
                if (out != null) out.close();
                if (socket != null && !socket.isClosed()) socket.close();
            } catch (IOException ignored) {}
        }
    }
}
