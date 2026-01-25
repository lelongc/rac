package Bai2_SortNumbers;

import java.io.*;
import java.net.Socket;
import java.util.Scanner;

/**
 * Client Class cho Bài 2: Sắp xếp số
 */
public class Client {
    public static void main(String[] args) {
        String serverHost = "localhost";
        int serverPort = 2000;

        try {
            Socket socket = new Socket(serverHost, serverPort);
            System.out.println("Đã kết nối tới Server sắp xếp số.");

            PrintWriter pw = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader br = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            Scanner scanner = new Scanner(System.in);

            System.out.print("Nhập các số tự nhiên, cách nhau bằng dấu phẩy (vd: 5,1,9): ");
            String inputNumbers = scanner.nextLine();

            pw.println(inputNumbers);

            String response = br.readLine();
            System.out.println("Kết quả sau sắp xếp: " + response);

            socket.close();
            scanner.close();

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
