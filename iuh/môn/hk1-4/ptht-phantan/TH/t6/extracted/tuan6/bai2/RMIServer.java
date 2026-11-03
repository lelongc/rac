package tuan6.bai2;

import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

/**
 * Bài 2: Cài đặt trên máy chủ RMIServer.
 */
public class RMIServer {
    public static final int PORT = 1099;

    public static void main(String[] args) {
        try {
            // Khởi tạo RMI Registry
            LocateRegistry.createRegistry(PORT);
            System.out.println("RMI Registry created on port " + PORT);

            Adder skeleton = new AdderImpl();
            // Đăng ký dịch vụ với tên "AdderService"
            Naming.rebind("rmi://localhost:" + PORT + "/AdderService", skeleton);

            System.out.println("RMIServer is ready for remote connections on port " + PORT);
        } catch (Exception e) {
            System.out.println("Server Error: " + e.getMessage());
        }
    }
}
