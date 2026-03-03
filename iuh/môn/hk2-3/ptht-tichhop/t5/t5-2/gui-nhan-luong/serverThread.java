import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;

public class serverThread extends Thread {
    private Socket client;

    public serverThread(Socket client) {
        this.client = client;
    }

    @Override
    public void run() {
        try {
            // In thông tin client
            System.out.println("===== Client kết nối =====");
            System.out.println("IP Address: " + client.getInetAddress().getHostAddress());
            System.out.println("Port: " + client.getPort());
            System.out.println("Local Port: " + client.getLocalPort());
            System.out.println("Connect Time: " + new java.util.Date());
            System.out.println("========================");
            
            InputStream is = client.getInputStream();
            OutputStream os = client.getOutputStream();

            int ch = 0;
            
            while (true) {
                ch = is.read();
                if (ch == -1) break; 
                
                System.out.println("client goi : " + (char)ch);
                
                
                os.write((char)ch);
            }
            
            System.out.println("Client từ " + client.getInetAddress().getHostAddress() + " đã ngắt kết nối!");
            client.close();
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}