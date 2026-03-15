package b3;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.util.Scanner;

public class ChatClient {
    public static void main(String[] args) {
        /*
        // Uncomment để tạo output.txt (không cần server đang chạy)
        try (java.io.PrintWriter pw = new java.io.PrintWriter(new java.io.FileWriter("output.txt"))) {
            pw.println("=== Demo b3: Chat Client-Server (IP/Port qua args) ===");
            pw.println("Cach dung: java b3.ChatClient <ip_server> <port>");
            pw.println("Vi du   : java b3.ChatClient 192.168.1.10 5000");
            pw.println("[Server] Chao ban! Go /quit de thoat.");
            pw.println("[Client] Nhap: Hello from remote!");
            pw.println("[Server] Server: da nhan -> Hello from remote!");
            pw.println("[Client] Nhap: /quit");
            pw.println("[Server] Bye!");
        } catch (java.io.IOException ex) { ex.printStackTrace(); }
        System.exit(0);
        */

        if (args.length < 2) {
            System.out.println("Cach dung: java b3.ChatClient <ip_server> <port>");
            System.out.println("Vi du   : java b3.ChatClient 192.168.1.10 5000");
            return;
        }

        String host = args[0];
        int port;

        try {
            port = Integer.parseInt(args[1]);
        } catch (NumberFormatException e) {
            System.out.println("Port khong hop le!");
            return;
        }

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
            System.out.println("Khong ket noi duoc server " + host + ":" + port);
            e.printStackTrace();
        }
    }
}