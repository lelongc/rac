import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;

public class ChatClient {
    public static final String DEFAULT_HOST = "localhost";
    public static final int DEFAULT_PORT = 5000;
    public static final String DEFAULT_ROOM = "general";
    public static final DateTimeFormatter TIME_FORMAT = DateTimeFormatter.ofPattern("HH:mm:ss");

    private static String currentRoom = DEFAULT_ROOM;
    private static String nickname = "23630851_1";

    public static void main(String[] args) {
        String host = DEFAULT_HOST;
        int port = DEFAULT_PORT;
        String room = null;
        String nick = null;

        if (args.length > 0 && !args[0].trim().isEmpty()) {
            host = args[0].trim();
        } else {
            String envHost = System.getenv("SERVER_HOST");
            if (envHost != null && !envHost.trim().isEmpty()) {
                host = envHost.trim();
            }
        }

        if (args.length > 1 && !args[1].trim().isEmpty()) {
            try {
                port = Integer.parseInt(args[1].trim());
            } catch (NumberFormatException ignored) {}
        } else {
            String envPort = System.getenv("SERVER_PORT");
            if (envPort != null && !envPort.trim().isEmpty()) {
                try {
                    port = Integer.parseInt(envPort.trim());
                } catch (NumberFormatException ignored) {}
            }
        }

        Scanner scanner = new Scanner(System.in, "UTF-8");

        System.out.println("==================================================");
        System.out.println("   MULTI-ROOM CHAT CLIENT - DE 2 THUONG KY 1      ");
        System.out.println("==================================================");

        if (args.length > 2 && !args[2].trim().isEmpty()) {
            nick = args[2].trim();
        }

        if (args.length > 3 && !args[3].trim().isEmpty()) {
            room = args[3].trim();
        }

        if (nick == null || nick.trim().isEmpty()) {
            System.out.print("Nhap Nickname (Ma SV_1, Ma SV_2, ... vd: 23630851_1): ");
            nick = scanner.nextLine().trim();
            while (nick.isEmpty()) {
                System.out.print("Vui long nhap Nickname (khong duoc de trong): ");
                nick = scanner.nextLine().trim();
            }
        }
        nickname = nick;

        if (room == null || room.trim().isEmpty()) {
            System.out.print("Nhap phong chat (Nhan Enter de vao phong mac dinh 'general'): ");
            room = scanner.nextLine().trim();
            if (room.isEmpty()) {
                room = DEFAULT_ROOM;
            }
        }
        currentRoom = room;

        System.out.println("\n[CLIENT] Dang ket noi toi Server tai " + host + ":" + port + "...");

        try (Socket socket = new Socket(host, port);
             BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream(), "UTF-8"));
             PrintWriter out = new PrintWriter(socket.getOutputStream(), true)) {

            System.out.println("[CLIENT] Ket noi thanh cong!\n");

            out.println(nickname);
            out.println(currentRoom);

            Thread receiver = new Thread(() -> {
                try {
                    String msg;
                    while ((msg = in.readLine()) != null) {
                        System.out.println(msg);
                    }
                } catch (IOException e) {
                    System.out.println("[HE THONG] Da ngat ket noi voi Server.");
                }
            });
            receiver.setDaemon(true);
            receiver.start();

            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                if (line == null) break;
                line = line.trim();
                if (line.isEmpty()) continue;

                out.println(line);

                if (line.equalsIgnoreCase("exit") || line.equalsIgnoreCase("quit") || line.equalsIgnoreCase("/quit")) {
                    System.out.println("[HE THONG] Da thoat khoi phong chat.");
                    try { Thread.sleep(150); } catch (InterruptedException ignored) {}
                    break;
                }

                if (line.startsWith("/join ")) {
                    String newRoom = line.substring(6).trim();
                    if (!newRoom.isEmpty()) {
                        currentRoom = newRoom;
                    }
                } else {
                    String time = LocalTime.now().format(TIME_FORMAT);
                    System.out.println(String.format("[%s][%s][%s]: %s", currentRoom, nickname, time, line));
                }
            }
        } catch (IOException e) {
            System.err.println("[CLIENT ERROR] Khong the ket noi toi Server (" + host + ":" + port + "): " + e.getMessage());
        }
    }
}
