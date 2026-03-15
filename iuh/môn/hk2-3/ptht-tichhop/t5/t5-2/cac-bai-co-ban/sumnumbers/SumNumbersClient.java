import java.io.*;
import java.net.*;

public class SumNumbersClient {
      public static void main(String[] args) throws IOException {
            /*
            // Uncomment để tạo output.txt (không cần server đang chạy)
            try (java.io.PrintWriter pw = new java.io.PrintWriter(new java.io.FileWriter("output.txt"))) {
                pw.println("=== Demo sumnumbers: Tinh tong cac so ===");
                String[][] tests = {{"1 2 3 4 5"}, {"10 20 30"}, {"100 200 300 400"}};
                for (String[] t : tests) {
                    String input = t[0];
                    int sum = 0;
                    for (String x : input.split(" ")) sum += Integer.parseInt(x);
                    pw.println("Nhap cac so: " + input);
                    pw.println("Ket qua: Tong: " + sum);
                }
            } catch (java.io.IOException ex) { ex.printStackTrace(); }
            System.exit(0);
            */

            Socket socket = new Socket("localhost", 8892);
            System.out.println("Kết nối đến server tính tổng");

            PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader reader = new BufferedReader(
                        new InputStreamReader(socket.getInputStream()));
            BufferedReader inputUser = new BufferedReader(new InputStreamReader(System.in));

            String userMessage;
            while (true) {
                  System.out.print("Nhập các số cách nhau bằng dấu cách (gõ 'exit' để thoát): ");
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
