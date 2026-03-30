package bai1;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class RMIServer {
    public static void main(String[] args) {
        try {
            HelloService service = new HelloServiceImpl();

           
            Registry registry = LocateRegistry.createRegistry(1099);

            
            registry.rebind("HelloService", service);

            System.out.println("RMI Server dang chay...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}