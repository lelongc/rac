import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;

/**
 * Chương trình máy chủ (Server Host - Chạy trên Máy A).
 * - Khởi tạo RMI Registry tại cổng 1099.
 * - Xuất đối tượng (Export) thành Remote Stub.
 * - Đăng ký dịch vụ với tên định danh "FactorialService".
 */
public class FactorialServer {
    public static final int PORT = 1099;
    public static final String SERVICE_NAME = "FactorialService";

    public static void main(String[] args) {
        try {
            // 1. Tạo đối tượng xử lý nghiệp vụ
            FactorialServiceImpl obj = new FactorialServiceImpl();

            // 2. Xuất đối tượng thành Remote Stub trên cổng ngẫu nhiên (port 0)
            FactorialService stub = (FactorialService) UnicastRemoteObject.exportObject(obj, 0);

            // 3. Khởi tạo máy chủ danh bạ RMI Registry tại cổng 1099
            Registry registry = LocateRegistry.createRegistry(PORT);

            // 4. Đăng ký dịch vụ vào Registry với tên "FactorialService"
            registry.rebind(SERVICE_NAME, stub);

            System.out.println("==================================================================");
            System.out.println("[SERVER] Factorial RMI Server đang chạy và lắng nghe tại cổng " + PORT + "...");
            System.out.println("[SERVER] Đã đăng ký dịch vụ: '" + SERVICE_NAME + "'");
            System.out.println("==================================================================");

        } catch (Exception e) {
            System.err.println("[-] Lỗi khởi động Factorial Server: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
