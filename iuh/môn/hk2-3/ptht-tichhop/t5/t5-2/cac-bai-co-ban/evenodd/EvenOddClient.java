import java.io.*;
import java.net.*;

public class EvenOddClient {
      public static void main(String[] args) throws IOException {
            /*
            // Uncomment để tạo output.txt (không cần server đang chạy)
            try (java.io.PrintWriter pw = new java.io.PrintWriter(new java.io.FileWriter("output.txt"))) {
                pw.println("=== Demo evenodd: Kiem tra chan le ===");
                int[] nums = {4, 7, 0, 13, 100};
                for (int n : nums) {
                    pw.println("Nhap so: " + n);
                    pw.println("Ket qua: " + n + " la so " + (n % 2 == 0 ? "Chẵn" : "Lẻ"));
                }
            } catch (java.io.IOException ex) { ex.printStackTrace(); }
            System.exit(0);
            */

            Socket socket = new Socket("localhost", 8891);
            System.out.println("Kết nối đến server kiểm tra chẵn lẻ");

            PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader reader = new BufferedReader(
                        new InputStreamReader(socket.getInputStream()));
            BufferedReader inputUser = new BufferedReader(new InputStreamReader(System.in));

            String userMessage;
            while (true) {
                  System.out.print("Nhập số (gõ 'exit' để thoát): ");
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
