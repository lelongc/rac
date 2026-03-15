package b4;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.util.Scanner;

public class DateTimeClient {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.print("Nhap IP server: ");
            String host = sc.nextLine().trim();
            if (host.isEmpty()) host = "127.0.0.1";

            System.out.print("Nhap port: ");
            int port = Integer.parseInt(sc.nextLine().trim());

            try (Socket socket = new Socket(host, port);
                 DataInputStream in = new DataInputStream(socket.getInputStream());
                 DataOutputStream out = new DataOutputStream(socket.getOutputStream())) {

               
                System.out.println(in.readUTF());

                while (true) {
                    System.out.print("Chon: ");
                    int choice = Integer.parseInt(sc.nextLine().trim());

                    out.writeInt(choice);
                    out.flush();

                    String resp = in.readUTF();
                    System.out.println("Server: " + resp);

                    if (choice == 0) break;
                }

            } catch (IOException e) {
                System.out.println("Khong ket noi duoc server!");
                e.printStackTrace();
            }
        }
    }
}