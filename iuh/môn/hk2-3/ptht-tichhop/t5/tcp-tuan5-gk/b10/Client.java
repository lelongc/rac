package b10;
import java.io.*;
import java.net.Socket;
import java.util.Scanner;
/*
 * Bai 10 - Client
 * Gui nhieu dong tin nhan den server, ket thuc bang "HET".
 */
public class Client {
    public static void main(String[] args) {
        String host = "127.0.0.1";
        int    port = 5000;
        try (Socket socket      = new Socket(host, port);
             BufferedReader in  = new BufferedReader(
                     new InputStreamReader(socket.getInputStream()));
             PrintWriter    out = new PrintWriter(socket.getOutputStream(), true);
             Scanner sc          = new Scanner(System.in)) {
            System.out.println("Server: " + in.readLine());
            while (true) {
                System.out.print("Tin nhan (HET de ket thuc): ");
                String msg = sc.nextLine();
                out.println(msg);
                if ("HET".equalsIgnoreCase(msg)) {
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