package bai6;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class RMIServer {
    public static void main(String[] args) {
        try {
            double initialBalance = 1000.0; // so du ban dau
            BankService service = new BankServiceImpl(initialBalance);

            Registry registry = LocateRegistry.createRegistry(1099);
            registry.rebind("BankService", service);

            System.out.println("RMI Server dang chay... So du ban dau: " + initialBalance);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}