import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;

// FILE 2: THREAD XỬ LÝ (th_processing)
// - Nhận 1 Socket client
// - Đọc từng byte từ client → xử lý → gửi lại
public class serverThread extends Thread {
    private Socket client;
    private int clientId;

    public serverThread(Socket client, int clientId) {
        this.client = client;
        this.clientId = clientId;
    }

    @Override
    public void run() {
        try {
            // === THÔNG TIN CLIENT (InetAddress) ===
            System.out.println("===== Client #" + clientId + " =====");
            System.out.println("IP   : " + client.getInetAddress().getHostAddress());
            System.out.println("Port : " + client.getPort());
            System.out.println("Local Port: " + client.getLocalPort());
            System.out.println("Thoi gian : " + new java.util.Date());
            System.out.println("========================");

            // === XỬ LÝ (Stream kiểu int/byte) ===
            InputStream is = client.getInputStream();   // nhận byte từ client
            OutputStream os = client.getOutputStream(); // gửi byte về client

            int ch; // đọc từng byte (int)
            while (true) {
                ch = is.read();     // đọc 1 byte; trả -1 khi client ngắt
                if (ch == -1) break;

                System.out.println("Client #" + clientId + " gui: " + (char) ch);

                // Xử lý: chuyển chữ thường → chữ hoa rồi gửi lại
                os.write(Character.toUpperCase((char) ch));
            }

            System.out.println("Client #" + clientId + " ngat ket noi!");

            // === ĐÓNG KẾT NỐI ===
            client.close();
        } catch (Exception e) {
            System.out.println("Loi client #" + clientId + ": " + e);
        }
    }
}
