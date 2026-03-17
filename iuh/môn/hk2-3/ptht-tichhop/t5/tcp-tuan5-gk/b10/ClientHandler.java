package b10;
import java.io.*;
import java.net.Socket;
/*
 * Bai 10 - ClientHandler
 * Doc tin nhan den khi gap "HET", ghi vao clientX.txt
 * (uu tien package source b10 thay vi bin).
 */
public class ClientHandler extends Thread {
    private final Socket socket;
    private final int    clientId;
    public ClientHandler(Socket socket, int clientId) {
        this.socket   = socket;
        this.clientId = clientId;
    }
    @Override
    public void run() {
        try {
            File projectDir = new File(System.getProperty("user.dir"));
            File sourceDir  = new File(projectDir, "src\\b10");
            if (!sourceDir.exists()) sourceDir = new File(projectDir, "b10");
            if (!sourceDir.exists()) sourceDir.mkdirs();
            File outFile = new File(sourceDir, "client" + clientId + ".txt");
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
                        + " tin nhan vao " + outFile.getAbsolutePath());
                netOut.println("Da luu " + count + " tin nhan vao file " + outFile.getName());
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try { socket.close(); } catch (IOException e) {}
        }
    }
}
