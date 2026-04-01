import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.Socket;
import java.nio.charset.StandardCharsets;
import java.util.Scanner;

public class Client {
    static final String HOST = "127.0.0.1";
    static final int PORT = 5000;

    public static void main(String[] args) throws Exception {
        // ================= TCP CLIENT (MAC DINH) =================
        try (Socket s = new Socket(HOST, PORT);
             BufferedReader in = new BufferedReader(new InputStreamReader(s.getInputStream()));
             PrintWriter out = new PrintWriter(s.getOutputStream(), true);
             Scanner sc = new Scanner(System.in)) {

            System.out.println(in.readLine());
            while (true) {
                // NHAP DATA THEO BAI DANG UNCOMMENT O ThreadProcess.processData()\r\n                // NHOM SO: 3 4 5 | ADD 1 2 3 4 | 10 | 97 | 5,2,9,1 | 100 USD VND\r\n                // NHOM CHUOI: phat trien he thong | zebra,apple,cat | a-b-c|- | hello
                System.out.print("> ");
                String data = sc.nextLine();
                out.println(data);
                System.out.println(in.readLine());
                if ("EXIT".equalsIgnoreCase(data.trim())) break;
            }
        }

        // ================= UDP CLIENT =================
        /*
        try (DatagramSocket ds = new DatagramSocket();
             Scanner sc = new Scanner(System.in)) {
            InetAddress ip = InetAddress.getByName(HOST);
            byte[] buf = new byte[8192];
            while (true) {
                // NHAP DATA THEO BAI DANG UNCOMMENT O ThreadProcess.processData()\r\n                // NHOM SO: 3 4 5 | ADD 1 2 3 4 | 10 | 97 | 5,2,9,1 | 100 USD VND\r\n                // NHOM CHUOI: phat trien he thong | zebra,apple,cat | a-b-c|- | hello
                System.out.print("> ");
                String data = sc.nextLine();
                byte[] out = data.getBytes(StandardCharsets.UTF_8);
                ds.send(new DatagramPacket(out, out.length, ip, PORT));
                DatagramPacket resp = new DatagramPacket(buf, buf.length);
                ds.receive(resp);
                System.out.println(new String(resp.getData(), 0, resp.getLength(), StandardCharsets.UTF_8));
                if ("EXIT".equalsIgnoreCase(data.trim())) break;
            }
        }
        */
    }
}

