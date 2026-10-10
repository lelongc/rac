package gkchat;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.Scanner;

public class ChatClient {
    public static final String HOST = "127.0.0.1";
    public static final int PORT = 10008;

    public static void main(String[] args) {
        System.out.println("Dang ket noi toi Chat Server (" + HOST + ":" + PORT + ")...");

        try (Socket socket = new Socket(HOST, PORT)) {
            System.out.println("Ket noi thanh cong!\n");

            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            Scanner scanner = new Scanner(System.in);

            // Luong 1: Lang nghe tin nhan tu Server gui ve
            Thread receiver = new Thread(() -> {
                try {
                    String serverMsg;
                    while ((serverMsg = in.readLine()) != null) {
                        System.out.println(serverMsg);
                    }
                } catch (IOException e) {
                    System.out.println("Da ngat ket noi voi Server.");
                }
            });
            receiver.setDaemon(true);
            receiver.start();

            // Luong 2 (chinh): Doc tu ban phim va gui len Server
            while (true) {
                String input = scanner.nextLine();
                out.println(input);
                if (input.equalsIgnoreCase("exit") || input.equalsIgnoreCase("bye")) {
                    break;
                }
            }

            scanner.close();
            System.out.println("Da roi khoi phong chat.");
        } catch (IOException e) {
            System.err.println("Loi ket noi: " + e.getMessage());
        }
    }
}
