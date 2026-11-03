package tuan6.bai2;

import java.rmi.Naming;

/**
 * Bài 2: RMIClient xác định địa chỉ IP và Port của RMIServer dựa theo tham số truyền vào (args).
 * Cú pháp chạy: java tuan6.bai2.RMIClient <server_ip> <port>
 */
public class RMIClient {
    public static void main(String[] args) {
        String serverIp = "localhost";
        int serverPort = 1099;

        // Đọc tham số IP và Port từ args
        if (args.length >= 2) {
            serverIp = args[0];
            try {
                serverPort = Integer.parseInt(args[1]);
            } catch (NumberFormatException e) {
                System.err.println("Cổng không hợp lệ, dùng cổng mặc định: 1099");
            }
        } else if (args.length == 1) {
            serverIp = args[0];
        } else {
            System.out.println("Không có tham số dòng lệnh. Mặc định kết nối: " + serverIp + ":" + serverPort);
            System.out.println("Cú pháp truyền tham số: java tuan6.bai2.RMIClient <IP_Server> <Port>");
        }

        try {
            String rmiUrl = "rmi://" + serverIp + ":" + serverPort + "/AdderService";
            System.out.println("Đang kết nối tới RMIServer tại: " + rmiUrl);

            Adder stub = (Adder) Naming.lookup(rmiUrl);
            int a = 15;
            int b = 25;
            int result = stub.add(a, b);

            System.out.println("Kết quả tính toán từ Server (" + serverIp + "): " + a + " + " + b + " = " + result);
        } catch (Exception e) {
            System.err.println("Lỗi gọi RMI từ xa: " + e.getMessage());
        }
    }
}
