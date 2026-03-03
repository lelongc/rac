import java.io.*;
import java.net.*;

public class SumNumbersHandler extends Thread {
      private Socket socket;
      private int clientId;

      public SumNumbersHandler(Socket socket, int clientId) {
            this.socket = socket;
            this.clientId = clientId;
      }

      @Override
      public void run() {
            try {
                  BufferedReader reader = new BufferedReader(
                        new InputStreamReader(socket.getInputStream()));
                  PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);

                  String message;
                  while ((message = reader.readLine()) != null && !message.equals("exit")) {
                        System.out.println("Client #" + clientId + " gửi: " + message);
                        try {
                              String[] numbers = message.split(" ");
                              int sum = 0;
                              for (String num : numbers) {
                                    sum += Integer.parseInt(num);
                              }
                              writer.println("Tổng: " + sum);
                        } catch (NumberFormatException e) {
                              writer.println("Lỗi: Vui lòng nhập các số cách nhau bằng dấu cách!");
                        }
                  }

                  System.out.println("Client #" + clientId + " ngắt kết nối!");
                  reader.close();
                  writer.close();
                  socket.close();
            } catch (IOException e) {
                  System.out.println("Lỗi với client #" + clientId);
            }
      }
}
