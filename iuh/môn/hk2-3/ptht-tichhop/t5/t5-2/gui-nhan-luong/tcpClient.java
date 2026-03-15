import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;

public class tcpClient {
    public static int port = 5678;

    public static void main(String[] args) throws IOException {
        /*
        // Uncomment để tạo output.txt (không cần server đang chạy)
        try (java.io.PrintWriter pw = new java.io.PrintWriter(new java.io.FileWriter("output.txt"))) {
            pw.println("=== Demo gui-nhan-luong: TCP Client (Echo byte) ===");
            pw.println("Client da duoc tao, ket noi localhost:" + port);
            for (int i = '0'; i <= '9'; i++) {
                pw.println("Gui: " + (char)i + "  =>  ket qua chuyen doi tu Server: " + (char)i);
            }
        } catch (java.io.IOException ex) { ex.printStackTrace(); }
        System.exit(0);
        */

        Socket client;

        try {
            client = new Socket("localhost", port);
            System.out.println("Client da duoc tao");

            OutputStream os = client.getOutputStream();
            InputStream is = client.getInputStream();

            for (int i = '0'; i <= '9'; i++) {
                os.write(i);

                int kq = is.read();
                System.out.println("ket qua chuyen doi tu Server: " + (char)kq);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}