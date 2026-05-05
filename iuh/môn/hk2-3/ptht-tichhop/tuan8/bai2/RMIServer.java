package bai2;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class RMIServer {
    public static void main(String[] args) {
        try {
            IdentityService service = new IdentityServiceImpl();
            Registry registry = LocateRegistry.createRegistry(1099);
            registry.rebind("IdentityService", service);
            System.out.println("RMI Server dang chay...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}