import java.io.*;
import java.net.*;

public class TCPClient {
      public static void main(String[] args) throws IOException {
            Socket socket = new Socket("localhost", 8888);
            System.out.println("Kết nối đến server");

            PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader reader = new BufferedReader(
                        new InputStreamReader(socket.getInputStream()));

            writer.println("Hello Server");

            String response = reader.readLine();
            System.out.println("Nhận từ server: " + response);

            writer.close();
            reader.close();
            socket.close();
      }
}
