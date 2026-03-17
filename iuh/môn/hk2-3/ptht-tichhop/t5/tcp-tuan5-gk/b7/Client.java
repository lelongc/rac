package b7;

import java.io.*;
import java.net.Socket;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) {

        /*
        // Uncomment để tạo output.txt (không cần server đang chạy)
        try (java.io.PrintWriter pw = new java.io.PrintWriter(new java.io.FileWriter("output.txt"))) {
            pw.println("=== Demo b7: TCP File Transfer ===");
            pw.println("[Client] Nhap dia chi server: 127.0.0.1");
            pw.println("[Client] Nhap port: 5000");
            pw.println("[Client] Nhap duong dan file can truyen: C:/test/hello.txt");
            pw.println("[Client] Nhap duong dan luu tren server: C:/received");
            pw.println("[Client] Dang truyen file hello.txt (13 bytes)...");
            pw.println("[Server] OK: Da luu C:\\received\\hello.txt");
        } catch (java.io.IOException ex) { ex.printStackTrace(); }
        System.exit(0);
        */

        try (Scanner sc = new Scanner(System.in)) {
            System.out.print("Nhap dia chi server (Enter = 127.0.0.1): ");
            String host = sc.nextLine().trim();
            if (host.isEmpty()) host = "127.0.0.1";

            System.out.print("Nhap port: ");
            int port = Integer.parseInt(sc.nextLine().trim());

            System.out.print("Nhap duong dan file can truyen: ");
            String filePath = sc.nextLine().trim();

            System.out.print("Nhap duong dan luu tren server: ");
            String savePath = sc.nextLine().trim();

            File file = new File(filePath);
            if (!file.exists() || !file.isFile()) {
                System.out.println("File khong ton tai: " + filePath);
                return;
            }

            try (Socket socket         = new Socket(host, port);
                 DataOutputStream out  = new DataOutputStream(socket.getOutputStream());
                 DataInputStream  in   = new DataInputStream(socket.getInputStream());
                 FileInputStream  fis  = new FileInputStream(file)) {

                // Gửi thông tin file
                out.writeUTF(file.getName());
                out.writeUTF(savePath);
                out.writeLong(file.length());

                // Gửi dữ liệu file
                System.out.println("Dang truyen file " + file.getName()
                        + " (" + file.length() + " bytes)...");
                byte[] buf = new byte[4096];
                int n;
                while ((n = fis.read(buf)) != -1) {
                    out.write(buf, 0, n);
                }
                out.flush();

                // Nhận kết quả
                String resp = in.readUTF();
                System.out.println("Server: " + resp);

            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
