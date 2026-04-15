package ck;

import java.rmi.Naming;
import java.util.Scanner;

/**
 * Lop khach ket noi toi Server va goi phuong thuc
 */
public class RMIClient {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            // 1. Tim kiem dich vu tu xa qua Naming.lookup
            IService service = (IService) Naming.lookup("rmi://localhost:6789/SeptemberRMI");

            System.out.println("--- RMI Client da ket noi den Server ---");
            System.out.println("Nhap du lieu de gui den Server (hoac nhap 'exit' de thoat):");

            while (true) {
                System.out.print("> ");
                String input = sc.nextLine();
                if ("exit".equalsIgnoreCase(input.trim())) break;

                // 2. Goi phuong thuc tu xa va lay ket qua
                String result = service.xuLyDuLieu(input);

                System.out.println("Ket qua tu Server: " + result);
            }
        } catch (Exception e) {
            System.err.println("Client exception: " + e.toString());
            e.printStackTrace();
        }
    }
}
