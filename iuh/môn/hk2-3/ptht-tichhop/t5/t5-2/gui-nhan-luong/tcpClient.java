import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;

public class tcpClient {
    public static int port = 5678;

    public static void main(String[] args) throws IOException {
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