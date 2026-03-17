package b7;
import java.io.*;
import java.net.Socket;
/*
 * Bai 7 TCP - ClientHandler
 * Nhan ten file, duong dan luu, kich thuoc va du lieu file.
 * Sau khi luu xong se gui thong bao OK ve client.
 */
public class ClientHandler extends Thread {
    private final Socket socket;
    public ClientHandler(Socket socket) {
        this.socket = socket;
    }
    @Override
    public void run() {
        try (DataInputStream  in  = new DataInputStream(socket.getInputStream());
             DataOutputStream out = new DataOutputStream(socket.getOutputStream())) {
            String fileName = in.readUTF();   
            String savePath = in.readUTF();   
            long   fileSize = in.readLong();  
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