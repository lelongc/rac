package tuan6.baimau;

import java.rmi.Naming;
import java.rmi.registry.LocateRegistry; 
public class RMIServer {
    public static void main(String[] args) {
        try {
        	LocateRegistry.createRegistry(1099);
            Adder skeleton = new AdderImpl();
            Naming.rebind("rmi://localhost:1099/Adder", skeleton);
            System.out.println("Server has started");
            System.out.println("Adder bound");
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
