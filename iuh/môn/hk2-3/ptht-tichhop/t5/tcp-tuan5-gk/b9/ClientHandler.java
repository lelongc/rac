package b9;
import java.io.*;
import java.net.Socket;
/*
 * Bai 9 - ClientHandler
 * Nhan ten file tu client, doc file trong thu muc package b9,
 * gui tung dong noi dung va ket thuc bang ##END##.
 */
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
            File dir  = new File(getClass().getResource("").toURI());
            File file = new File(dir, fileName);
            if (!file.exists() || !file.isFile()) {
                netOut.println("ERROR: File khong ton tai: " + file.getAbsolutePath());
                return;
            }
            try (BufferedReader fileIn = new BufferedReader(new FileReader(file))) {
                String line;
                while ((line = fileIn.readLine()) != null) {
                    netOut.println(line);
                }
            }
            netOut.println("##END##");
            System.out.println("Da gui xong file: " + file.getAbsolutePath());
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try { socket.close(); } catch (IOException e) {}
        }
    }
}