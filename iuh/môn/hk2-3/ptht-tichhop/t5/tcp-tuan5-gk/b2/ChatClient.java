package b2;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.util.Scanner;

public class ChatClient {
    public static void main(String[] args) {
        String host = "127.0.0.1";
        int port = 5000;

        /*
        // Uncomment để tạo output.txt (không cần server đang chạy)
        try (java.io.PrintWriter pw = new java.io.PrintWriter(new java.io.FileWriter("output.txt"))) {
            pw.println("=== Demo b2: Chat Client-Server ===");
            pw.println("[Server] Chao ban! Go /quit de thoat.");
            pw.println("[Client] Nhap: Xin chao Server!");
            pw.println("[Server] Server: da nhan -> Xin chao Server!");
            pw.println("[Client] Nhap: Hom nay the nao?");
            pw.println("[Server] Server: da nhan -> Hom nay the nao?");
            pw.println("[Client] Nhap: /quit");
            pw.println("[Server] Bye!");
        } catch (java.io.IOException ex) { ex.printStackTrace(); }
        System.exit(0);
        */

        try (Socket socket = new Socket(host, port);
             DataInputStream in = new DataInputStream(socket.getInputStream());
             DataOutputStream out = new DataOutputStream(socket.getOutputStream());
             Scanner sc = new Scanner(System.in)) {

            
            new Thread(() -> {
                try {
                    while (true) {
                        System.out.println("\n" + in.readUTF());
                        System.out.print("Nhap: ");
                    }
                } catch (IOException e) {
                    System.out.println("\n[Mat ket noi server]");
                }
            }).start();

            
            while (true) {
                System.out.print("Nhap: ");
                String msg = sc.nextLine();

                out.writeUTF(msg);
                out.flush();

                if ("/quit".equalsIgnoreCase(msg)) break;
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}