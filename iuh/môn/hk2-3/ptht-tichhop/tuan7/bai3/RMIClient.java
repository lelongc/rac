package bai3;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class RMIClient {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);
            PrimeService service = (PrimeService) registry.lookup("PrimeService");

            System.out.print("Nhap n: ");
            int n = sc.nextInt();

            boolean result = service.isPrime(n);
            System.out.println(result ? (n + " la so nguyen to")
                                      : (n + " khong phai so nguyen to"));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}