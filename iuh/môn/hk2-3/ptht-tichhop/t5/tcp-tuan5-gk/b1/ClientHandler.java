package b1;


import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;

public class ClientHandler extends Thread {
    private final Socket socket;

    public ClientHandler(Socket socket) {
        this.socket = socket;
    }

    private String docSo(char c) {
        switch (c) {
            case '0': return "không";
            case '1': return "một";
            case '2': return "hai";
            case '3': return "ba";
            case '4': return "bốn";
            case '5': return "năm";
            case '6': return "sáu";
            case '7': return "bảy";
            case '8': return "tám";
            case '9': return "chín";
            default:  return "Không phải số nguyên";
        }
    }

    @Override
    public void run() {
        System.out.println("Client ket noi: " + socket.getInetAddress() + ":" + socket.getPort());

        try (Socket s = socket;
             DataInputStream in = new DataInputStream(s.getInputStream());
             DataOutputStream out = new DataOutputStream(s.getOutputStream())) {

            while (true) {
                String msg;
                try {
                    msg = in.readUTF(); 
                } catch (IOException e) {
                    
                    break;
                }

                if ("exit".equalsIgnoreCase(msg)) {
                    out.writeUTF("Bye");
                    out.flush();
                    break;
                }

                char c = msg.isEmpty() ? '\0' : msg.charAt(0);
                String kq = docSo(c);

                out.writeUTF(kq);
                out.flush();
            }

        } catch (IOException e) {
            e.printStackTrace();
        }

        System.out.println("Client ngat: " + socket.getInetAddress() + ":" + socket.getPort());
    }
}