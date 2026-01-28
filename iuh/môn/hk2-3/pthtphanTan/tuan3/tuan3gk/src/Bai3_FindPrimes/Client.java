package Bai3_FindPrimes;

import java.io.*;
import java.net.*;
import java.util.Scanner;

public class Client {
    public static void main(String[] a) throws Exception {
        try (Socket s = new Socket("localhost", 3000);
                Scanner sc = new Scanner(System.in);
                PrintWriter w = new PrintWriter(s.getOutputStream(), true);
                BufferedReader r = new BufferedReader(new InputStreamReader(s.getInputStream()))) {
            System.out.print("Input: ");
            w.println(sc.nextLine());
            System.out.println("Primes: " + r.readLine());
        }
    }
}
