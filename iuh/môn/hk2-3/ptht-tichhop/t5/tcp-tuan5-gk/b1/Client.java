package b1;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) {
        String host = "127.0.0.1";
        int port = 5000;

        try (Socket socket = new Socket(host, port);
             DataInputStream in = new DataInputStream(socket.getInputStream());
             DataOutputStream out = new DataOutputStream(socket.getOutputStream());
             Scanner sc = new Scanner(System.in)) {

            System.out.println("Da ket noi server. Nhap 1 ky tu (0-9) hoac 'exit' de thoat:");

            while (true) {
                System.out.print("Nhap: ");
                String s = sc.nextLine();

      
                String send = s.equalsIgnoreCase("exit") ? "exit"
                        : (s.isEmpty() ? "" : String.valueOf(s.charAt(0)));

                out.writeUTF(send);
                out.flush();

                String resp = in.readUTF();
                System.out.println("Server tra ve: " + resp);

                if ("exit".equalsIgnoreCase(send)) break;
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}