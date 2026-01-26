package Bai2_SortNumbers;

import java.io.*;
import java.net.*;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) throws IOException {
        try (Socket socket = new Socket("localhost", 2001);
                Scanner sc = new Scanner(System.in);
                PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
                BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()))) {
            System.out.print("Input (e.g., 5,1,9): ");
            out.println(sc.nextLine());
            System.out.println("Sorted: " + in.readLine());
        }
    }
}
