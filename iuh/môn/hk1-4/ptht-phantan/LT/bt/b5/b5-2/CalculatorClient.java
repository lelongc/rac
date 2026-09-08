import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

/**
 * Chương trình máy khách (Client App - Bài 2).
 * - Kết nối RMI Registry của Server.
 * - Tra cứu (lookup) Stub đại diện cho "CalcService".
 * - Gọi các hàm từ xa (add, subtract, multiply).
 */
public class CalculatorClient {
    public static final String DEFAULT_HOST = "localhost";
    public static final int PORT = 1099;
    public static final String SERVICE_NAME = "CalcService";

    public static void main(String[] args) {
        String host = (args.length > 0) ? args[0] : DEFAULT_HOST;

        try {
            System.out.println("[CLIENT] Đang kết nối tới RMI Registry tại " + host + ":" + PORT + "...");

            // 1. Kết nối tới RMI Registry của Server
            Registry registry = LocateRegistry.getRegistry(host, PORT);

            // 2. Tra cứu (Lookup) dịch vụ qua tên "CalcService" để nhận về Stub đại diện
            Calculator stub = (Calculator) registry.lookup(SERVICE_NAME);

            System.out.println("========== KẾT QUẢ GỌI HÀM TỪ XA (RPC / RMI) ==========");

            // 3. Gọi hàm từ xa: Stub tự động đóng gói qua Socket TCP tới Server và nhận kết quả
            int sum = stub.add(10, 20);
            System.out.println("Kết quả add(10, 20)       = " + sum);

            int diff = stub.subtract(50, 15);
            System.out.println("Kết quả subtract(50, 15)  = " + diff);

            int product = stub.multiply(6, 8);
            System.out.println("Kết quả multiply(6, 8)    = " + product);

            System.out.println("=======================================================");

        } catch (Exception e) {
            System.err.println("[-] Lỗi kết nối hoặc gọi RMI Client: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
