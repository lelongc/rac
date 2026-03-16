import java.io.*;
import java.net.*;
import java.util.Scanner;

public class Client {
    private static final String HOST = "localhost";
    private static final int PORT = 6789;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Nhập số nguyên n để tính giai thừa: ");
        int n = scanner.nextInt();

        try (Socket socket = new Socket(HOST, PORT)) {
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader in = new BufferedReader(
                    new InputStreamReader(socket.getInputStream()));

            out.println(n);
            String response = in.readLine();
            System.out.println("Kết quả từ server: " + response);

        } catch (ConnectException e) {
            System.out.println("Không thể kết nối đến server. Hãy chắc chắn server đang chạy.");
        } catch (IOException e) {
            System.out.println("Lỗi: " + e.getMessage());
        } finally {
            scanner.close();
        }
    }
}
