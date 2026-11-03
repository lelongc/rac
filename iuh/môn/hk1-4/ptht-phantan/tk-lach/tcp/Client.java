import java.io.*;
import java.net.*;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) throws Exception {
        try (Socket s = new Socket("localhost", 5000);
             BufferedReader in = new BufferedReader(new InputStreamReader(s.getInputStream()));
             PrintWriter out = new PrintWriter(s.getOutputStream(), true);
             Scanner sc = new Scanner(System.in)) {

            System.out.println("=== KET NOI TCP SERVER (5000) THANH CONG ===");
            while (true) {
                System.out.print("> Nhap du lieu: ");
                String line = sc.nextLine();
                if ("EXIT".equalsIgnoreCase(line.trim())) {
                    out.println("EXIT");
                    break;
                }
                out.println(line);
                System.out.println("< Server tra ve: " + in.readLine());
            }
        }
    }
}

