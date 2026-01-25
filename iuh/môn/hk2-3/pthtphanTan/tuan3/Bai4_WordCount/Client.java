package Bai4_WordCount;

import java.io.*;
import java.net.Socket;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) {
        String serverHost = "localhost";
        int serverPort = 4000;

        try {
            Socket socket = new Socket(serverHost, serverPort);
            System.out.println("Đã kết nối tới Server đếm từ.");

            PrintWriter pw = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader br = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            Scanner scanner = new Scanner(System.in);

            System.out.print("Nhập chuỗi văn bản: ");
            String inputLine = scanner.nextLine();

            pw.println(inputLine);

            String response = br.readLine();
            System.out.println("Tần suất xuất hiện của các từ: " + response);

            socket.close();
            scanner.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
