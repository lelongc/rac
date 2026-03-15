import java.io.*;
import java.net.*;

public class TCPClient {
      public static void main(String[] args) throws IOException {
            /*
            // Uncomment để tạo output.txt (không cần server đang chạy)
            try (java.io.PrintWriter pw = new java.io.PrintWriter(new java.io.FileWriter("output.txt"))) {
                pw.println("=== Demo gui-nhan: TCP Client-Server (Echo) ===");
                pw.println("Ket noi den server localhost:8888");
                pw.println("Gui: Hello Server");
                pw.println("Nhan tu server: Echo: Hello Server");
            } catch (java.io.IOException ex) { ex.printStackTrace(); }
            System.exit(0);
            */

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
