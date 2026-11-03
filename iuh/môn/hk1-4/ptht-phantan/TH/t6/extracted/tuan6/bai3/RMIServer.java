package tuan6.bai3;

import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

public class RMIServer {
    public static final int PORT = 1099;

    public static void main(String[] args) {
        try {
            // Tự động tạo RMI Registry tại cổng 1099
            LocateRegistry.createRegistry(PORT);
            System.out.println("RMI Registry created on port " + PORT);

            // Đăng ký dịch vụ Calculator
            Calculator skeleton = new CalculatorImpl();
            Naming.rebind("rmi://localhost:" + PORT + "/CalculatorService", skeleton);

            System.out.println("=== Calculator RMIServer đã sẵn sàng phục vụ ===");
            System.out.println("Các dịch vụ cung cấp: Cộng (+), Trừ (-), Nhân (*), Chia (/)");
        } catch (Exception e) {
            System.out.println("Server Error: " + e.getMessage());
        }
    }
}
