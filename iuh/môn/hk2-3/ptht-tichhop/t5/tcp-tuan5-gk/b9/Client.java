package b9;
import java.io.*;
import java.net.Socket;
import java.util.Scanner;
/*
 * Bai 9 - Client
 * Gui ten file can doc va hien thi noi dung server tra ve.
 */
public class Client {
    public static void main(String[] args) {
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