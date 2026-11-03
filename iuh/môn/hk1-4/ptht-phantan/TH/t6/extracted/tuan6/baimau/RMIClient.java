package tuan6.baimau;

import java.rmi.Naming;

public class RMIClient {
    public static void main(String[] args) {
        try {
            Adder stub = (Adder) Naming.lookup("rmi://localhost:1099/Adder");
            int a = 2;
            int b = 2;
            int result = stub.add(a, b);
            System.out.println(a + "+" + b + "=" + result);
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}
