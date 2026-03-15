package b4;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;

public class ClientHandler extends Thread {
    private final Socket socket;

    public ClientHandler(Socket socket) {
        this.socket = socket;
    }

    private String handle(int choice) {
        switch (choice) {
            case 1: 
                return "Time: " + LocalTime.now();
            case 2: 
                return "Date: " + LocalDate.now();
            case 3: 
                return "Date&Time: " + LocalDateTime.now();
            default:
                return "Lua chon khong hop le!";
        }
    }

    @Override
    public void run() {
        try (Socket s = socket;
             DataInputStream in = new DataInputStream(s.getInputStream());
             DataOutputStream out = new DataOutputStream(s.getOutputStream())) {

            
            out.writeUTF("MENU:\n1. Time\n2. Date\n3. Date & Time\nNhap 1/2/3 (hoac 0 de thoat)");
            out.flush();

            while (true) {
                int choice = in.readInt(); 
                if (choice == 0) {
                    out.writeUTF("Bye!");
                    out.flush();
                    break;
                }

                String resp = handle(choice);
                out.writeUTF(resp);
                out.flush();
            }

        } catch (IOException e) {
           
        }
    }
}