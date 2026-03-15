import java.io.*;
import java.net.*;

public class CountCharClient {
      public static void main(String[] args) throws IOException {
            /*
            // Uncomment để tạo output.txt (không cần server đang chạy)
            try (java.io.PrintWriter pw = new java.io.PrintWriter(new java.io.FileWriter("output.txt"))) {
                pw.println("=== Demo countchar: Dem so ky tu ===");
                String[] inputs = {"Hello", "Java Programming", "TCP Socket", "Xin chao the gioi"};
                for (String s : inputs) {
                    pw.println("Nhap chuoi: " + s);
                    pw.println("Ket qua: So ky tu: " + s.length());
                }
            } catch (java.io.IOException ex) { ex.printStackTrace(); }
            System.exit(0);
            */

            Socket socket = new Socket("localhost", 8890);
            System.out.println("Kết nối đến server đếm ký tự");

            PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader reader = new BufferedReader(
                        new InputStreamReader(socket.getInputStream()));
            BufferedReader inputUser = new BufferedReader(new InputStreamReader(System.in));

            String userMessage;
            while (true) {
                  System.out.print("Nhập chuỗi (gõ 'exit' để thoát): ");
                  userMessage = inputUser.readLine();

                  if (userMessage.equalsIgnoreCase("exit")) {
                        writer.println("exit");
                        break;
                  }

                  writer.println(userMessage);
                  String response = reader.readLine();
                  System.out.println("Kết quả: " + response);
            }

            writer.close();
            reader.close();
            inputUser.close();
            socket.close();
            System.out.println("Ngắt kết nối!");
      }
}
