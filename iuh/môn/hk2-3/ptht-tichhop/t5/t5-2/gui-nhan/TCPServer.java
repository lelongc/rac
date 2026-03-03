import java.io.*;
import java.net.*;

public class TCPServer {
      public static void main(String[] args) throws IOException {
            ServerSocket serverSocket = new ServerSocket(8888);
            System.out.println("Server đang lắng nghe trên port 8888...");

            Socket socket = serverSocket.accept();
            System.out.println("Client kết nối!");

            BufferedReader reader = new BufferedReader(
                        new InputStreamReader(socket.getInputStream()));
            PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);

            String message = reader.readLine();
            System.out.println("Nhận từ client: " + message);

            writer.println("Echo: " + message);

            reader.close();
            writer.close();
            socket.close();
            serverSocket.close();
      }
}
