package Bai5_ProductDB;

import java.io.*;
import java.net.*;
import java.util.Scanner;

public class ProductClient {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        while (true) {
            System.out.print("TCP Search (type 'exit' to quit): ");
            String q = sc.nextLine();
            if (q.equals("exit"))
                break;
            try (Socket s = new Socket("localhost", 6123);
                    PrintWriter w = new PrintWriter(s.getOutputStream(), true);
                    BufferedReader r = new BufferedReader(new InputStreamReader(s.getInputStream()))) {
                w.println(q);
                System.out.println("Result: " + r.readLine());
            } catch (Exception e) {
                System.out.println("Err: " + e);
            }
        }
    }
}
