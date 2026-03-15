package b6;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.util.Scanner;

public class TcpCalcClient {
    public static void main(String[] args) {
        String host = "127.0.0.1";
        int port = 5000;

        /*
        // Uncomment để tạo output.txt (không cần server đang chạy)
        try (java.io.PrintWriter pw = new java.io.PrintWriter(new java.io.FileWriter("output.txt"))) {
            pw.println("=== Demo b6: TCP Calc Client ===");
            // Phep 1: Tong 1+3+5+...+(2n+1), n=4 => (n+1)^2 = 25
            int n1 = 4;
            long r1 = (long)(n1 + 1) * (n1 + 1);
            pw.println("Chon: 1 (Tong 1+3+...+(2n+1)), n=" + n1 + "  =>  Ket qua = " + r1);
            // Phep 2: Tong i*(i+1) i=1..n, n=4 => 2+6+12+20 = 40
            int n2 = 4; long sum2 = 0;
            for (int k = 1; k <= n2; k++) sum2 += (long)k * (k + 1);
            pw.println("Chon: 2 (Tong 1*2+2*3+...+n*(n+1)), n=" + n2 + "  =>  Ket qua = " + sum2);
            // Phep 3: 1-2+3-4+...+(2n+1) = n+1, n=4 => 5
            int n3 = 4;
            long r3 = (long)(n3 + 1);
            pw.println("Chon: 3 (1-2+3-4+...+(2n+1)), n=" + n3 + "  =>  Ket qua = " + r3);
        } catch (java.io.IOException ex) { ex.printStackTrace(); }
        System.exit(0);
        */

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