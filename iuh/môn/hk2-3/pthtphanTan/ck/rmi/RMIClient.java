package ck;

import java.rmi.Naming;
import java.util.Scanner;

public class RMIClient {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            IService service = (IService) Naming.lookup("rmi://localhost:6789/SeptemberRMI");

            System.out.println("--- RMI Client connected ---");
            System.out.println("Nhap du lieu (hoac 'exit' de thoat):");

            while (true) {
                System.out.print("> ");
                if (!sc.hasNextLine()) break;
                String input = sc.nextLine();
                if ("exit".equalsIgnoreCase(input.trim())) break;

                System.out.println("Result: " + service.xuLyDuLieu(input));
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
