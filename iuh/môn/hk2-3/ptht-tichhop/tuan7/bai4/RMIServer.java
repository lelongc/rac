package bai4;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class RMIServer {
    public static void main(String[] args) {
        try {
            ContactService service = new ContactServiceImpl();
            Registry registry = LocateRegistry.createRegistry(1099);
            registry.rebind("ContactService", service);
            System.out.println("RMI Server dang chay...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}