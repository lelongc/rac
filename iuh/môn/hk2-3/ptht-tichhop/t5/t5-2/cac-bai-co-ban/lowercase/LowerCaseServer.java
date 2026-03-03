import java.io.*;
import java.net.*;

public class LowerCaseServer {
      public static void main(String[] args) throws IOException {
            ServerSocket serverSocket = new ServerSocket(8889);
            System.out.println("Server chuyển sang chữ thường - Lắng nghe trên port 8889...");

            int clientCount = 0;
            while (true) {
                  Socket socket = serverSocket.accept();
                  clientCount++;
                  System.out.println("Client #" + clientCount + " kết nối!");
                  
                  LowerCaseHandler handler = new LowerCaseHandler(socket, clientCount);
                  handler.start();
            }
      }
}
