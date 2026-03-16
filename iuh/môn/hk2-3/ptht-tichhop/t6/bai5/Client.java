package bai5;

import java.io.*;
import java.net.*;
import java.util.Scanner;

public class Client {
    private static final String HOST = "localhost";
    private static final int PORT = 6789;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in, "UTF-8");
        System.out.print("nhap chuoi can xu ly: ");
        String input = scanner.nextLine();

        try (Socket socket = new Socket(HOST, PORT)) {
            PrintWriter out = new PrintWriter(
                    new OutputStreamWriter(socket.getOutputStream(), "UTF-8"), true);
            BufferedReader in = new BufferedReader(
                    new InputStreamReader(socket.getInputStream(), "UTF-8"));

            out.println(input);

            String line;
            while ((line = in.readLine()) != null) {
                System.out.println(line);
            }

        } catch (ConnectException e) {
            System.out.println("khong the ket noi den server.");
        } catch (IOException e) {
            System.out.println("loi: " + e.getMessage());
        } finally {
            scanner.close();
        }
    }
}