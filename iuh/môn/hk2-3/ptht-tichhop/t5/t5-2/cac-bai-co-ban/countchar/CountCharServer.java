import java.io.*;
import java.net.*;

public class CountCharServer {
      public static void main(String[] args) throws IOException {
            ServerSocket serverSocket = new ServerSocket(8890);
            System.out.println("Server đếm số ký tự - Lắng nghe trên port 8890...");

            int clientCount = 0;
            while (true) {
                  Socket socket = serverSocket.accept();
                  clientCount++;
                  System.out.println("Client #" + clientCount + " kết nối!");
                  
                  CountCharHandler handler = new CountCharHandler(socket, clientCount);
                  handler.start();
            }
      }
}
