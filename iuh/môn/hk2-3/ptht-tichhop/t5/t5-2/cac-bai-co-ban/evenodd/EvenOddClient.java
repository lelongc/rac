import java.io.*;
import java.net.*;

public class EvenOddClient {
      public static void main(String[] args) throws IOException {
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
