package b3;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.util.Scanner;

public class ChatClient {
    public static void main(String[] args) {
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