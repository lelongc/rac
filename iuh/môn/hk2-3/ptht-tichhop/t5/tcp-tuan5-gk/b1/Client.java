package b1;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) {
        String host = "127.0.0.1";
        int port = 5000;

        /*
        // Uncomment để tạo output.txt (không cần server đang chạy)
        try (java.io.PrintWriter pw = new java.io.PrintWriter(new java.io.FileWriter("output.txt"))) {
            pw.println("=== Demo b1: Gui ky tu so, nhan ten tieng Viet ===");
            String[] digits = {"0","1","2","3","4","5","6","7","8","9"};
            String[] names  = {"không","một","hai","ba","bốn","năm","sáu","bảy","tám","chín"};
            for (int i = 0; i < digits.length; i++) {
                pw.println("Nhap: " + digits[i] + "  =>  Server tra ve: " + names[i]);
            }
            pw.println("Nhap: exit  =>  Server tra ve: Bye");
        } catch (java.io.IOException ex) { ex.printStackTrace(); }
        System.exit(0);
        */

        try (Socket socket = new Socket(host, port);
             DataInputStream in = new DataInputStream(socket.getInputStream());
             DataOutputStream out = new DataOutputStream(socket.getOutputStream());
             Scanner sc = new Scanner(System.in)) {

            System.out.println("Da ket noi server. Nhap 1 ky tu (0-9) hoac 'exit' de thoat:");

            while (true) {
                System.out.print("Nhap: ");
                String s = sc.nextLine();

      
                String send = s.equalsIgnoreCase("exit") ? "exit"
                        : (s.isEmpty() ? "" : String.valueOf(s.charAt(0)));

                out.writeUTF(send);
                out.flush();

                String resp = in.readUTF();
                System.out.println("Server tra ve: " + resp);

                if ("exit".equalsIgnoreCase(send)) break;
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}