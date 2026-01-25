package Bai3_FindPrimes;

import java.io.*;
import java.net.Socket;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) {
        String serverHost = "localhost";
        int serverPort = 3000;

        try {
            Socket socket = new Socket(serverHost, serverPort);
            System.out.println("Đã kết nối tới Server tìm số nguyên tố.");

            PrintWriter pw = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader br = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            Scanner scanner = new Scanner(System.in);

            System.out.print("Nhập các số (vd: 12, 5, 7, 20): ");
            String inputLine = scanner.nextLine();

            pw.println(inputLine);

            String response = br.readLine();
            System.out.println("Các số nguyên tố là: " + response);

            socket.close();
            scanner.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
