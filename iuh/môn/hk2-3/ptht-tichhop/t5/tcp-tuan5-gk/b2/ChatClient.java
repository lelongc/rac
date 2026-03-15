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