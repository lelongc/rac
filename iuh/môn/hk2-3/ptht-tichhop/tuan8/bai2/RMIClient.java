package bai2;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class RMIClient {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);
            IdentityService service = (IdentityService) registry.lookup("IdentityService");

            System.out.print("Nhap so CMND/CCCD: ");
            String id = sc.nextLine();

            String result = service.lookup(id);
            System.out.println(result);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}