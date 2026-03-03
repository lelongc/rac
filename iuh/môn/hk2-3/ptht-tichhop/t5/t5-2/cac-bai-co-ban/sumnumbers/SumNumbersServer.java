import java.io.*;
import java.net.*;

public class SumNumbersServer {
      public static void main(String[] args) throws IOException {
            ServerSocket serverSocket = new ServerSocket(8892);
            System.out.println("Server tính tổng các số - Lắng nghe trên port 8892...");

            int clientCount = 0;
            while (true) {
                  Socket socket = serverSocket.accept();
                  clientCount++;
                  System.out.println("Client #" + clientCount + " kết nối!");
                  
                  SumNumbersHandler handler = new SumNumbersHandler(socket, clientCount);
                  handler.start();
            }
      }
}
