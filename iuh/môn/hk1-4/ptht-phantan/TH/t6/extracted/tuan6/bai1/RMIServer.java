package tuan6.bai1;

import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

/**
 * Bài 1: Cải tiến RMIServer sử dụng LocateRegistry.createRegistry(PORT)
 * Giúp tạo và khởi động RMI Registry trực tiếp trong mã nguồn Java,
 * không cần mở cmd chạy lệnh "start rmiregistry 1099" thủ công.
 */
public class RMIServer {
    public static final int PORT = 1099;

    public static void main(String[] args) {
        try {
            // Yêu cầu bài 1: Khởi tạo Registry trực tiếp bằng câu lệnh createRegistry
            LocateRegistry.createRegistry(PORT);
            System.out.println("RMI Registry created on port " + PORT);

            // Tạo đối tượng từ xa và đăng ký với Registry
            Adder skeleton = new AdderImpl();
            Naming.rebind("rmi://localhost:" + PORT + "/Adder", skeleton);

            System.out.println("Server has started");
            System.out.println("Adder bound");
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
