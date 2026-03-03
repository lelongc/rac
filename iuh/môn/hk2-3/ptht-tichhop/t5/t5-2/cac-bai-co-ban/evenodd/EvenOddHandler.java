import java.io.*;
import java.net.*;

public class EvenOddHandler extends Thread {
      private Socket socket;
      private int clientId;

      public EvenOddHandler(Socket socket, int clientId) {
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
                              int num = Integer.parseInt(message);
                              String result = (num % 2 == 0) ? "Chẵn" : "Lẻ";
                              writer.println(num + " là số " + result);
                        } catch (NumberFormatException e) {
                              writer.println("Lỗi: Vui lòng nhập một số nguyên!");
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
