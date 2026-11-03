package lab7.bai2;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class RMIClient {
    public static void main(String[] args) {
        try {
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);
            
            MathService mathService = (MathService) registry.lookup("MathService");
            
            Scanner scanner = new Scanner(System.in);
            System.out.print("Nhập số A: ");
            int a = scanner.nextInt();
            System.out.print("Nhập số B: ");
            int b = scanner.nextInt();
            
            int gcd = mathService.findGCD(a, b);
            System.out.println("=> Ước số chung lớn nhất của " + a + " và " + b + " là: " + gcd);
            
            String primeCheck = mathService.checkPrime(a, b);
            System.out.println("=> " + primeCheck);
            
        } catch (Exception e) {
            System.out.println("Lỗi kết nối RMI. Hãy chắc chắn RMIServer đã chạy.");
            e.printStackTrace();
        }
    }
}
