package gk;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.Scanner;

public class Client {
    static final String HOST = "127.0.0.1";
    static final int PORT = 5000;

    public static void main(String[] args) throws Exception {
        try (Socket s = new Socket(HOST, PORT);
             BufferedReader in = new BufferedReader(new InputStreamReader(s.getInputStream()));
             PrintWriter out = new PrintWriter(s.getOutputStream(), true);
             Scanner sc = new Scanner(System.in)) {

            System.out.println(in.readLine());
            while (true) {
                System.out.print("> ");
                String data = sc.nextLine();
                out.println(data);
                System.out.println(in.readLine());
                if ("EXIT".equalsIgnoreCase(data.trim())) break;
            }
        }
    }
}
