package ck;

import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

public class RMIServer {
    public static void main(String[] args) {
        try {
            IService service = new ServiceImpl();
            LocateRegistry.createRegistry(6789);
            Naming.rebind("rmi://localhost:6789/SeptemberRMI", service);
            System.out.println(">>>>> RMI Server is running on port 6789...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
