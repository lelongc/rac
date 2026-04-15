package ck;

import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

/**
 * Lop khoi chay RMI Server
 */

public class RMIServer {
    public static void main(String[] args) {
        try {
            // 1. Tao doi tuong thuc thi
            IService service = new ServiceImpl();

            // 2. Khoi tao Registry tren cong 6789
            LocateRegistry.createRegistry(6789);

            // 3. Dang ky service vao Registry voi ten "SeptemberRMI"
            Naming.rebind("rmi://localhost:6789/SeptemberRMI", service);

            System.out.println(">>>>> INFO: RMI Server is running on port 6789...");
            System.out.println("Service name: SeptemberRMI");
        } catch (Exception e) {
            System.err.println("Server exception: " + e.toString());
            e.printStackTrace();
        }
    }
}
