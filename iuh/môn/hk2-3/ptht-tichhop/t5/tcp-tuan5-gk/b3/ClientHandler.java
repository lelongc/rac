package b3;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;

public class ClientHandler extends Thread {
    private final Socket socket;

    public ClientHandler(Socket socket) {
        this.socket = socket;
    }

    @Override
    public void run() {
        System.out.println("Client connected: " + socket.getInetAddress() + ":" + socket.getPort());

        try (Socket s = socket;
             DataInputStream in = new DataInputStream(s.getInputStream());
             DataOutputStream out = new DataOutputStream(s.getOutputStream())) {

            out.writeUTF("Chao ban! Go /quit de thoat.");
            out.flush();

            while (true) {
                String msg = in.readUTF();
                if ("/quit".equalsIgnoreCase(msg)) {
                    out.writeUTF("Bye!");
                    out.flush();
                    break;
                }

                System.out.println("From client " + s.getPort() + ": " + msg);

                out.writeUTF("Server: da nhan -> " + msg);
                out.flush();
            }

        } catch (IOException e) {
           
        }

        System.out.println("Client disconnected: " + socket.getPort());
    }
}