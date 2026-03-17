package b6;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
/*
 * Bai 6 TCP - ClientHandler
 * Nhan choice + n tu client, tinh toan va tra ket qua long.
 */
public class TcpClientHandler extends Thread {
    private final Socket socket;
    public TcpClientHandler(Socket socket) {
        this.socket = socket;
    }
    @Override
    public void run() {
        try (Socket s = socket;
             DataInputStream in = new DataInputStream(s.getInputStream());
             DataOutputStream out = new DataOutputStream(s.getOutputStream())) {
            while (true) {
                int choice;
                try {
                    choice = in.readInt();
                } catch (IOException e) {
                    break; 
                }
                if (choice == 0) { 
                    out.writeLong(0);
                    out.flush();
                    break;
                }
                int n = in.readInt();
                try {
                    long result = CalcService.calc(choice, n);
                    out.writeLong(result);
                } catch (IllegalArgumentException ex) {
                    out.writeLong(Long.MIN_VALUE);
                }
                out.flush();
            }
        } catch (IOException e) {
        }
    }
}