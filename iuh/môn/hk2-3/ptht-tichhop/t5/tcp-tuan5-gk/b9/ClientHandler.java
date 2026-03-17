package b9;

import java.io.*;
import java.net.Socket;

// Giao thức:
// 1. Client gửi tên file (readLine)
// 2. Server tìm file trong thư mục làm việc
//    - Nếu không tìm thấy: gửi "ERROR: File khong ton tai: <ten>\n" rồi đóng
//    - Nếu thấy: gửi từng dòng nội dung, kết thúc bằng "##END##"
public class ClientHandler extends Thread {
    private final Socket socket;

    public ClientHandler(Socket socket) {
        this.socket = socket;
    }

    @Override
    public void run() {
        try (BufferedReader netIn  = new BufferedReader(
                 new InputStreamReader(socket.getInputStream()));
             PrintWriter    netOut = new PrintWriter(socket.getOutputStream(), true)) {

            String fileName = netIn.readLine();
            if (fileName == null || fileName.trim().isEmpty()) return;
            fileName = fileName.trim();

            System.out.println("Client yeu cau file: " + fileName);

            // File đặt cùng thư mục chạy server (user.dir trong Eclipse = thư mục project)
            File file = new File(fileName);
            if (!file.exists() || !file.isFile()) {
                netOut.println("ERROR: File khong ton tai: " + fileName);
                return;
            }

            // Gửi nội dung từng dòng
            try (BufferedReader fileIn = new BufferedReader(new FileReader(file))) {
                String line;
                while ((line = fileIn.readLine()) != null) {
                    netOut.println(line);
                }
            }
            // Cờ kết thúc
            netOut.println("##END##");
            System.out.println("Da gui xong file: " + fileName);

        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try { socket.close(); } catch (IOException e) {}
        }
    }
}
