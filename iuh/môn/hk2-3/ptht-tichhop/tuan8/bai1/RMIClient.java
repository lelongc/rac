package bai1;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class RMIClient {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);
            CalcService service = (CalcService) registry.lookup("CalcService");

            System.out.println("Nhap bieu thuc (go 'exit' de thoat).");

            while (true) {
                System.out.print("Bieu thuc> ");
                String expr = sc.nextLine().trim();

                if (expr.equalsIgnoreCase("exit")) {
                    System.out.println("Thoat chuong trinh.");
                    break;
                }

                if (expr.isEmpty()) {
                    System.out.println("ERROR: bieu thuc rong");
                    continue;
                }

                String result = service.evaluate(expr);
                System.out.println("Ket qua: " + result);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}