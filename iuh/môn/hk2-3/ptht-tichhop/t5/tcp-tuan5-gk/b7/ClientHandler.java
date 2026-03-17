package b7;

import java.io.*;
import java.net.Socket;

// Giao thức TCP file transfer:
// 1. Client gửi tên file     (writeUTF)
// 2. Client gửi đường dẫn lưu trên server (writeUTF)
// 3. Client gửi kích thước file (writeLong)
// 4. Client gửi toàn bộ bytes của file
// 5. Server trả về "OK: ..." hoặc "ERROR: ..."
public class ClientHandler extends Thread {
    private final Socket socket;

    public ClientHandler(Socket socket) {
        this.socket = socket;
    }

    @Override
    public void run() {
        try (DataInputStream  in  = new DataInputStream(socket.getInputStream());
             DataOutputStream out = new DataOutputStream(socket.getOutputStream())) {

            String fileName = in.readUTF();   // tên file, vd: "test.txt"
            String savePath = in.readUTF();   // thư mục lưu, vd: "C:/received"
            long   fileSize = in.readLong();  // kích thước bytes

            // Tạo thư mục nếu chưa có
            File dir = new File(savePath);
            if (!dir.exists()) dir.mkdirs();

            File dest = new File(dir, fileName);
            try (FileOutputStream fos = new FileOutputStream(dest)) {
                byte[] buf = new byte[4096];
                long remaining = fileSize;
                while (remaining > 0) {
                    int toRead = (int) Math.min(buf.length, remaining);
                    int n = in.read(buf, 0, toRead);
                    if (n < 0) break;
                    fos.write(buf, 0, n);
                    remaining -= n;
                }
            }

            System.out.println("Da luu file: " + dest.getAbsolutePath()
                    + " (" + fileSize + " bytes)");
            out.writeUTF("OK: Da luu " + dest.getAbsolutePath());
            out.flush();

        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try { socket.close(); } catch (IOException e) {}
        }
    }
}
