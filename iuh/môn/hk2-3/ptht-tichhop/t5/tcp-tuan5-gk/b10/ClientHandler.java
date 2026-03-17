package b10;

import java.io.*;
import java.net.Socket;

// Giao thức:
// 1. Client gửi từng dòng tin nhắn (readLine)
// 2. Client gửi "HET" để kết thúc
// 3. Server lưu tất cả tin nhắn vào file "client<id>.txt"
// 4. Server gửi thông báo lưu thành công
public class ClientHandler extends Thread {
    private final Socket socket;
    private final int    clientId;

    public ClientHandler(Socket socket, int clientId) {
        this.socket   = socket;
        this.clientId = clientId;
    }

    @Override
    public void run() {
        String outFile = "client" + clientId + ".txt";

        try (BufferedReader netIn  = new BufferedReader(
                 new InputStreamReader(socket.getInputStream()));
             PrintWriter    netOut = new PrintWriter(socket.getOutputStream(), true);
             PrintWriter    fileOut = new PrintWriter(new FileWriter(outFile))) {

            netOut.println("Xin chao client #" + clientId
                    + "! Nhap tin nhan, go 'HET' de ket thuc.");

            String msg;
            int count = 0;
            while ((msg = netIn.readLine()) != null) {
                if ("HET".equalsIgnoreCase(msg)) break;
                fileOut.println(msg);
                fileOut.flush();
                count++;
                System.out.println("Client #" + clientId + " gui: " + msg);
            }

            System.out.println("Client #" + clientId + " da luu " + count
                    + " tin nhan vao " + outFile);
            netOut.println("Da luu " + count + " tin nhan vao file " + outFile);

        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try { socket.close(); } catch (IOException e) {}
        }
    }
}
