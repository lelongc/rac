package gkchat;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Vector;

public class ChatServer {
    public static final int PORT = 10008;
    private static final Vector<ClientHandler> clients = new Vector<>();
    private static int clientCount = 0;

    public static void main(String[] args) {
        System.out.println("=== TCP CHAT SERVER (MULTI-CLIENT BROADCAST) ===");
        System.out.println("Dang lang nghe ket noi tai cong " + PORT + "...");

        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
            while (true) {
                Socket socket = serverSocket.accept();
                clientCount++;
                String clientName = "Client_" + clientCount;
                System.out.println(clientName + " da ket noi tu: " + socket.getInetAddress());

                ClientHandler handler = new ClientHandler(socket, clientName);
                clients.add(handler);
                handler.start();
            }
        } catch (IOException e) {
            System.err.println("Loi Server: " + e.getMessage());
        }
    }

    public static void broadcast(String message, ClientHandler sender) {
        for (ClientHandler client : clients) {
            if (client != sender) {
                client.sendMessage(message);
            }
        }
    }

    public static void removeClient(ClientHandler client) {
        clients.remove(client);
        System.out.println(client.getClientName() + " da roi phong chat. So luong con lai: " + clients.size());
        broadcast("[" + client.getClientName() + "] da roi phong chat.", null);
    }

    static class ClientHandler extends Thread {
        private final Socket socket;
        private final String clientName;
        private BufferedReader in;
        private PrintWriter out;

        public ClientHandler(Socket socket, String clientName) {
            this.socket = socket;
            this.clientName = clientName;
        }

        public String getClientName() {
            return clientName;
        }

        public void sendMessage(String msg) {
            if (out != null) {
                out.println(msg);
            }
        }

        @Override
        public void run() {
            try {
                in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                out = new PrintWriter(socket.getOutputStream(), true);

                out.println("=== Chao mung " + clientName + " den voi phong chat ===");
                out.println("Go tin nhan va Enter de tro chuyen. Go 'bye' hoac 'exit' de thoat.");
                broadcast("[" + clientName + "] da tham gia phong chat!", this);

                String line;
                while ((line = in.readLine()) != null) {
                    line = line.trim();
                    if (line.equalsIgnoreCase("exit") || line.equalsIgnoreCase("bye")) {
                        break;
                    }
                    System.out.println("[" + clientName + "]: " + line);
                    broadcast(clientName + ": " + line, this);
                }
            } catch (IOException e) {
                System.out.println(clientName + " mat ket noi.");
            } finally {
                removeClient(this);
                try {
                    if (in != null) in.close();
                    if (out != null) out.close();
                    if (socket != null) socket.close();
                } catch (IOException ignored) {}
            }
        }
    }
}
