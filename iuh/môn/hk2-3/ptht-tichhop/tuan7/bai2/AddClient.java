package bai2;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class AddClient {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);
            AddService service = (AddService) registry.lookup("AddService");

            System.out.print("Nhap a: ");
            int a = sc.nextInt();
            System.out.print("Nhap b: ");
            int b = sc.nextInt();

            int sum = service.add(a, b);
            System.out.println("Tong a + b = " + sum);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}