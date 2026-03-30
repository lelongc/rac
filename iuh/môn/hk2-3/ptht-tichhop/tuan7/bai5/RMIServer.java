package bai5;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class RMIServer {
    public static void main(String[] args) {
        try {
            ChatService service = new ChatServiceImpl();
            Registry registry = LocateRegistry.createRegistry(1099);
            registry.rebind("ChatService", service);
            System.out.println("RMI Server dang chay...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}