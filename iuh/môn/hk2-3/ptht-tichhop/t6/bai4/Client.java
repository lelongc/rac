package bai4;

import java.io.*;
import java.net.*;
import java.util.Scanner;

public class Client {
    private static final String HOST = "localhost";
    private static final int PORT = 6789;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        try {
            System.out.print("nhap so nguyen n de tinh giai thua: ");
            int n = scanner.nextInt();

            try (Socket socket = new Socket(HOST, PORT)) {
                PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
                BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));

                out.println(n);
                String response = in.readLine();
                System.out.println("ket qua tu server: " + response);

            } catch (ConnectException e) {
                System.out.println("khong the ket noi server.");
            } catch (IOException e) {
                System.out.println("loi: " + e.getMessage());
            }
        } finally {
            scanner.close();
        }
    }
}