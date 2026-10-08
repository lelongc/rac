package gkrmi;

import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

public class RMIServer {
    public static final int PORT = 1099;
    public static final String SERVICE_NAME = "RemoteService";

    public static void main(String[] args) {
        try {
            // Tự động tạo Registry tại cổng 1099 (hoặc dùng registry đang mở)
            try {
                LocateRegistry.createRegistry(PORT);
                System.out.println("RMI Registry duoc tao tai cong " + PORT);
            } catch (Exception e) {
                System.out.println("RMI Registry da ton tai tai cong " + PORT);
            }

            // Khởi tạo đối tượng Remote Service
            IRemoteService service = new RemoteServiceImpl();

            // Dang ky doi tuong vao Registry
            String rmiUrl = "rmi://localhost:" + PORT + "/" + SERVICE_NAME;
            Naming.rebind(rmiUrl, service);

            System.out.println("==================================================");
            System.out.println("  RMI SERVER DA KHOI DONG THANH CONG!");
            System.out.println("  Dich vu dang phuc vu tai: " + rmiUrl);
            System.out.println("==================================================");
        } catch (Exception e) {
            System.err.println("Loi Server: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
