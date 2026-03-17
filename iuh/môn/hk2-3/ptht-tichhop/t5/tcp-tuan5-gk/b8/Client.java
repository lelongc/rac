package b8;
import java.io.*;
import java.net.Socket;
import java.util.Scanner;
/*
 * Bai 8 - Client
 * Nguoi dung nhap dang 100+200, client doi sang "+ 100 200" de gui.
 */
public class Client {
    public static void main(String[] args) {
        String host = "127.0.0.1";
        int    port = 5000;
        try (Socket socket      = new Socket(host, port);
             BufferedReader in  = new BufferedReader(
                     new InputStreamReader(socket.getInputStream()));
             PrintWriter    out = new PrintWriter(socket.getOutputStream(), true);
             Scanner sc         = new Scanner(System.in)) {
            System.out.println("Ket noi server " + host + ":" + port + " thanh cong.");
            System.out.println("Nhap phep tinh (vi du: 100+200) hoac 'exit' de thoat.");
            while (true) {
                System.out.print("Nhap: ");
                String input = sc.nextLine().trim();
                if (input.equalsIgnoreCase("exit")) {
                    out.println("exit");
                    System.out.println("Server: " + in.readLine());
                    break;
                }
                String msg = parseExpr(input);
                if (msg == null) {
                    System.out.println("Dinh dang sai! Vd: 100+200 | 50-8 | 6*7 | 10/4");
                    continue;
                }
                out.println(msg);   
                String resp = in.readLine();
                System.out.println("Ket qua: " + resp);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private static String parseExpr(String s) {
        char[] ops = {'+', '-', '*', '/'};
        for (char op : ops) {
            int idx = (op == '-') ? s.indexOf('-', 1) : s.indexOf(op);
            if (idx > 0) {
                String a = s.substring(0, idx).trim();
                String b = s.substring(idx + 1).trim();
                if (!a.isEmpty() && !b.isEmpty())
                    return op + " " + a + " " + b;
            }
        }
        return null;
    }
}