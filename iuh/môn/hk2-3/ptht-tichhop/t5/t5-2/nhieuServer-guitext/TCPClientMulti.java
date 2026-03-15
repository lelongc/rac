
import java.io.*;
import java.net.*;

public class TCPClientMulti {
      public static void main(String[] args) throws IOException {
            /*
            // Uncomment để tạo output.txt (không cần server đang chạy)
            try (java.io.PrintWriter pw = new java.io.PrintWriter(new java.io.FileWriter("output.txt"))) {
                pw.println("=== Demo nhieuServer-guitext: TCP Multi-Client (Echo) ===");
                String[] msgs = {"Xin chao!", "Day la tin nhan thu 2", "Ket thuc phien"};
                for (String m : msgs) {
                    pw.println("Nhap tin nhan: " + m);
                    pw.println("Nhan tu server: Echo tu server: " + m);
                }
            } catch (java.io.IOException ex) { ex.printStackTrace(); }
            System.exit(0);
            */

            Socket socket = new Socket("localhost", 8888);
            System.out.println("Kết nối đến server");

            PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader reader = new BufferedReader(
                        new InputStreamReader(socket.getInputStream()));
            BufferedReader inputUser = new BufferedReader(new InputStreamReader(System.in));

            String userMessage;
            while (true) {
                  System.out.print("Nhập tin nhắn (gõ 'exit' để thoát): ");
                  userMessage = inputUser.readLine();

                  if (userMessage.equalsIgnoreCase("exit")) {
                        break;
                  }

                  writer.println(userMessage);
                  String response = reader.readLine();
                  System.out.println("Nhận từ server: " + response);
            }

            writer.close();
            reader.close();
            inputUser.close();
            socket.close();
            System.out.println("Ngắt kết nối!");
      }
}
