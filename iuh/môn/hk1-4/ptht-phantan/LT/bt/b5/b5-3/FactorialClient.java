import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

/**
 * Chương trình máy khách (Client App - Chạy trên Máy B).
 * - Kết nối RMI Registry của Máy Server A qua IP và Cổng.
 * - Tra cứu (lookup) dịch vụ từ xa "FactorialService".
 * - Gọi hàm tính giai thừa từ xa và in kết quả.
 */
public class FactorialClient {
    public static final String DEFAULT_SERVER_IP = "localhost";
    public static final int PORT = 1099;
    public static final String SERVICE_NAME = "FactorialService";

    public static void main(String[] args) {
        // Cho phép nhập địa chỉ IP Server từ dòng lệnh: java FactorialClient [IP]
        String serverHost = (args.length > 0) ? args[0] : DEFAULT_SERVER_IP;

        try {
            System.out.println("[CLIENT] Đang kết nối tới Server RMI tại " + serverHost + ":" + PORT + "...");

            // 1. Kết nối tới RMI Registry của Máy Server A
            Registry registry = LocateRegistry.getRegistry(serverHost, PORT);

            // 2. Tra cứu dịch vụ từ xa qua tên
            FactorialService stub = (FactorialService) registry.lookup(SERVICE_NAME);

            System.out.println("[CLIENT] Kết nối thành công! Bắt đầu gọi hàm tính giai thừa từ xa:");
            System.out.println("------------------------------------------------------------------");

            // 3. Thực hiện các lời gọi hàm từ xa qua Stub
            int[] testNumbers = {5, 7, 10, 12, 15};
            for (int n : testNumbers) {
                long result = stub.factorial(n);
                System.out.printf(">>> Giai thừa của %2d (%2d!) từ Server = %15d%n", n, n, result);
            }

            System.out.println("------------------------------------------------------------------");
            System.out.println("[CLIENT] Hoàn thành tất cả lời gọi hàm từ xa!");

        } catch (Exception e) {
            System.err.println("[-] Lỗi kết nối hoặc gọi RMI Client: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
