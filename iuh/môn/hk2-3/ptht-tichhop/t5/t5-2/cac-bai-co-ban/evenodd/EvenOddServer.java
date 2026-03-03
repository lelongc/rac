import java.io.*;
import java.net.*;

public class EvenOddServer {
      public static void main(String[] args) throws IOException {
            ServerSocket serverSocket = new ServerSocket(8891);
            System.out.println("Server kiểm tra chẵn lẻ - Lắng nghe trên port 8891...");

            int clientCount = 0;
            while (true) {
                  Socket socket = serverSocket.accept();
                  clientCount++;
                  System.out.println("Client #" + clientCount + " kết nối!");
                  
                  EvenOddHandler handler = new EvenOddHandler(socket, clientCount);
                  handler.start();
            }
      }
}
