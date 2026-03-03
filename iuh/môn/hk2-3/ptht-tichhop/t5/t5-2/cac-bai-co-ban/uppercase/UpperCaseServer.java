import java.io.*;
import java.net.*;

public class UpperCaseServer {
      public static void main(String[] args) throws IOException {
            ServerSocket serverSocket = new ServerSocket(8888);
            System.out.println("Server chuyển sang chữ hoa - Lắng nghe trên port 8888...");

            int clientCount = 0;
            while (true) {
                  Socket socket = serverSocket.accept();
                  clientCount++;
                  System.out.println("Client #" + clientCount + " kết nối!");
                  
                  UpperCaseHandler handler = new UpperCaseHandler(socket, clientCount);
                  handler.start();
            }
      }
}
