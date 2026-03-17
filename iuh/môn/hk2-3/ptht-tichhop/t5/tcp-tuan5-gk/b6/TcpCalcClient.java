package b6;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.util.Scanner;
/*
 * Bai 6 TCP - Client
 * Nhap menu tinh toan, gui choice + n, nhan ket qua tu server.
 */
public class TcpCalcClient {
    public static void main(String[] args) {
        String host = "127.0.0.1";
        int port = 5000;
        try (Socket socket = new Socket(host, port);
             DataInputStream in = new DataInputStream(socket.getInputStream());
             DataOutputStream out = new DataOutputStream(socket.getOutputStream());
             Scanner sc = new Scanner(System.in)) {
            while (true) {
                System.out.println("\nChon phep tinh:");
                System.out.println("1) Tong 1+3+...+(2n+1)");
                System.out.println("2) Tong 1*2 + 2*3 + ... + n*(n+1)");
                System.out.println("3) 1-2+3-4+...+(2n+1)");
                System.out.println("0) Thoat");
                System.out.print("Choice: ");
                int choice = Integer.parseInt(sc.nextLine().trim());
                out.writeInt(choice);
                if (choice == 0) {
                    out.flush();
                    break;
                }
                System.out.print("Nhap n: ");
                int n = Integer.parseInt(sc.nextLine().trim());
                out.writeInt(n);
                out.flush();
                long result = in.readLong();
                if (result == Long.MIN_VALUE) {
                    System.out.println("Server: Tham so/choice khong hop le!");
                } else {
                    System.out.println("Ket qua = " + result);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}