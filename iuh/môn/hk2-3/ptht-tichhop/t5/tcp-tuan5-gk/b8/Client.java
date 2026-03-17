package b8;

import java.io.*;
import java.net.Socket;
import java.util.Scanner;

// Client nhập phép tính dạng thông thường: "100+200", "5*3", "10/2", "8-3"
// Client tự parse → gửi sang server dạng "OP op1 op2\n"
// Server tính và trả về kết quả
public class Client {
    public static void main(String[] args) {

        /*
        // Uncomment để tạo output.txt (không cần server đang chạy)
        try (java.io.PrintWriter pw = new java.io.PrintWriter(new java.io.FileWriter("output.txt"))) {
            pw.println("=== Demo b8: Calculator Client-Server ===");
            pw.println("[Client] Nhap: 100+200   => [Server] 300");
            pw.println("[Client] Nhap: 50-8      => [Server] 42");
            pw.println("[Client] Nhap: 6*7       => [Server] 42");
            pw.println("[Client] Nhap: 10/4      => [Server] 2.50");
            pw.println("[Client] Nhap: 5/0       => [Server] Loi: Chia cho 0");
            pw.println("[Client] Nhap: exit      => [Server] Bye!");
        } catch (java.io.IOException ex) { ex.printStackTrace(); }
        System.exit(0);
        */

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

                // Parse "a OP b" từ cách nhập thông thường
                String msg = parseExpr(input);
                if (msg == null) {
                    System.out.println("Dinh dang sai! Vd: 100+200 | 50-8 | 6*7 | 10/4");
                    continue;
                }

                out.println(msg);   // gửi "OP op1 op2"
                String resp = in.readLine();
                System.out.println("Ket qua: " + resp);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // Chuyển "100+200" → "+ 100 200"
    private static String parseExpr(String s) {
        // Tìm operator: +, -, *, /  (bỏ qua dấu '-' ở đầu nếu là số âm)
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
