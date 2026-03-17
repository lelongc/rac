package b10;

import java.io.*;
import java.net.Socket;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) {

        /*
        // Uncomment để tạo output.txt (không cần server đang chạy)
        try (java.io.PrintWriter pw = new java.io.PrintWriter(new java.io.FileWriter("output.txt"))) {
            pw.println("=== Demo b10: Luu tin nhan vao file ===");
            pw.println("[Server] Xin chao client #1! Nhap tin nhan, go 'HET' de ket thuc.");
            pw.println("[Client] Tin nhan thu nhat");
            pw.println("[Client] Tin nhan thu hai");
            pw.println("[Client] Xin chao server!");
            pw.println("[Client] HET");
            pw.println("[Server] Da luu 3 tin nhan vao file client1.txt");
        } catch (java.io.IOException ex) { ex.printStackTrace(); }
        System.exit(0);
        */

        String host = "127.0.0.1";
        int    port = 5000;

        try (Socket socket      = new Socket(host, port);
             BufferedReader in  = new BufferedReader(
                     new InputStreamReader(socket.getInputStream()));
             PrintWriter    out = new PrintWriter(socket.getOutputStream(), true);
             Scanner sc          = new Scanner(System.in)) {

            // Nhận lời chào từ server
            System.out.println("Server: " + in.readLine());

            while (true) {
                System.out.print("Tin nhan (HET de ket thuc): ");
                String msg = sc.nextLine();
                out.println(msg);

                if ("HET".equalsIgnoreCase(msg)) {
                    // Chờ thông báo lưu thành công từ server
                    String resp = in.readLine();
                    System.out.println("Server: " + resp);
                    break;
                }
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
