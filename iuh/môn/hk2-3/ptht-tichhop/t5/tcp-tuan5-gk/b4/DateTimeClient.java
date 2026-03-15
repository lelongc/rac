package b4;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.util.Scanner;

public class DateTimeClient {
    public static void main(String[] args) {
        /*
        // Uncomment để tạo output.txt (không cần server đang chạy)
        try (java.io.PrintWriter pw = new java.io.PrintWriter(new java.io.FileWriter("output.txt"))) {
            pw.println("=== Demo b4: DateTime Client-Server ===");
            pw.println("[Server] MENU:\n1. Time\n2. Date\n3. Date & Time\nNhap 1/2/3 (hoac 0 de thoat)");
            pw.println("[Client] Chon: 1");
            pw.println("[Server] Time: " + java.time.LocalTime.now());
            pw.println("[Client] Chon: 2");
            pw.println("[Server] Date: " + java.time.LocalDate.now());
            pw.println("[Client] Chon: 3");
            pw.println("[Server] Date&Time: " + java.time.LocalDateTime.now());
            pw.println("[Client] Chon: 0");
            pw.println("[Server] Bye!");
        } catch (java.io.IOException ex) { ex.printStackTrace(); }
        System.exit(0);
        */

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