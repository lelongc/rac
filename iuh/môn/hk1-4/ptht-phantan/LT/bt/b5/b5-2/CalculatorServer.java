import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;

/**
 * Chương trình máy chủ (Server Host - Bài 2).
 * - Khởi tạo RMI Registry tại cổng 1099.
 * - Xuất (export) đối tượng CalculatorImpl thành Remote Stub qua port ngẫu nhiên (port 0).
 * - Đăng ký (rebind) dịch vụ vào Registry với tên định danh "CalcService".
 */
public class CalculatorServer {
    public static final int PORT = 1099;
    public static final String SERVICE_NAME = "CalcService";

    public static void main(String[] args) {
        try {
            // 1. Tạo đối tượng xử lý nghiệp vụ
            CalculatorImpl obj = new CalculatorImpl();

            // 2. Xuất đối tượng (Export) thành Remote Stub lắng nghe trên cổng ngẫu nhiên (port 0)
            Calculator stub = (Calculator) UnicastRemoteObject.exportObject(obj, 0);

            // 3. Khởi tạo RMI Registry tại cổng 1099
            Registry registry = LocateRegistry.createRegistry(PORT);

            // 4. Đăng ký dịch vụ với tên định danh "CalcService"
            registry.rebind(SERVICE_NAME, stub);

            System.out.println("==================================================================");
            System.out.println("[SERVER] Calculator RMI Server đã sẵn sàng phục vụ tại cổng " + PORT + "...");
            System.out.println("[SERVER] Dịch vụ đã đăng ký: '" + SERVICE_NAME + "'");
            System.out.println("==================================================================");
        } catch (Exception e) {
            System.err.println("[-] Lỗi khởi động Calculator Server: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
