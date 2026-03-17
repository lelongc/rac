package b9;

import java.io.*;
import java.net.Socket;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) {

        /*
        // Uncomment để tạo output.txt (không cần server đang chạy)
        try (java.io.PrintWriter pw = new java.io.PrintWriter(new java.io.FileWriter("output.txt"))) {
            pw.println("=== Demo b9: Doc noi dung file tu server ===");
            pw.println("[Client] Nhap ten file: data.txt");
            pw.println("--- Noi dung file ---");
            pw.println("Dong 1: Xin chao! Day la noi dung file data.txt tren server.");
            pw.println("Dong 2: File nay duoc doc va gui toan bo den client khi co yeu cau.");
            pw.println("Dong 3: Server ho tro nhieu client ket noi cung luc (moi ket noi 1 thread).");
            pw.println("Dong 4: Client chi can nhap ten file, server se tim va gui noi dung.");
            pw.println("Dong 5: Het file data.txt.");
            pw.println("---------------------");
            pw.println("[Client] Nhap ten file: nofile.txt");
            pw.println("Server: ERROR: File khong ton tai: nofile.txt");
        } catch (java.io.IOException ex) { ex.printStackTrace(); }
        System.exit(0);
        */

        String host = "127.0.0.1";
        int    port = 5000;

        try (Scanner sc = new Scanner(System.in)) {
            System.out.print("Nhap IP server (Enter = 127.0.0.1): ");
            String h = sc.nextLine().trim();
            if (!h.isEmpty()) host = h;

            while (true) {
                System.out.print("Nhap ten file (exit de thoat): ");
                String fileName = sc.nextLine().trim();
                if (fileName.equalsIgnoreCase("exit")) break;

                // Mỗi lần đọc một file mở một kết nối mới (theo đề)
                try (Socket socket      = new Socket(host, port);
                     PrintWriter netOut = new PrintWriter(socket.getOutputStream(), true);
                     BufferedReader netIn = new BufferedReader(
                             new InputStreamReader(socket.getInputStream()))) {

                    netOut.println(fileName);

                    System.out.println("--- Noi dung file ---");
                    String line;
                    while ((line = netIn.readLine()) != null) {
                        if ("##END##".equals(line)) break;
                        System.out.println(line);
                    }
                    System.out.println("---------------------");

                } catch (IOException e) {
                    System.out.println("Loi ket noi: " + e.getMessage());
                }
            }
        }
    }
}
