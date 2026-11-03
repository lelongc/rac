package lab7.bai2;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class RMIServer {
    public static void main(String[] args) {
        try {
            MathService mathService = new MathServiceImpl();
            
            Registry registry = LocateRegistry.createRegistry(1099);
            
            registry.rebind("MathService", mathService);
            System.out.println("RMI Server đang chạy ở port 1099...");
            
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
