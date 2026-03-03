import java.io.*;
import java.net.*;

public class CountCharHandler extends Thread {
      private Socket socket;
      private int clientId;

      public CountCharHandler(Socket socket, int clientId) {
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
                        int count = message.length();
                        writer.println("Số ký tự: " + count);
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
