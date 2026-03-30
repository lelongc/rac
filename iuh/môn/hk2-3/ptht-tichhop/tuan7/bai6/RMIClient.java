package bai6;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class RMIClient {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);
            BankService service = (BankService) registry.lookup("BankService");

            while (true) {
                System.out.println("\n===== NGAN HANG RMI =====");
                System.out.println("1. Xem so du");
                System.out.println("2. Gui tien");
                System.out.println("3. Rut tien");
                System.out.println("0. Thoat");
                System.out.print("Chon: ");

                int choice = Integer.parseInt(sc.nextLine().trim());

                switch (choice) {
                    case 1:
                        System.out.println("So du hien tai: " + service.getBalance());
                        break;

                    case 2:
                        System.out.print("Nhap so tien muon gui: ");
                        double depositAmount = Double.parseDouble(sc.nextLine().trim());
                        service.deposit(depositAmount);
                        System.out.println("Gui tien thanh cong. So du moi: " + service.getBalance());
                        break;

                    case 3:
                        System.out.print("Nhap so tien muon rut: ");
                        double withdrawAmount = Double.parseDouble(sc.nextLine().trim());
                        boolean ok = service.withdraw(withdrawAmount);
                        if (ok) {
                            System.out.println("Rut tien thanh cong. So du moi: " + service.getBalance());
                        } else {
                            System.out.println("Rut tien that bai (so tien khong hop le hoac khong du so du).");
                        }
                        break;

                    case 0:
                        System.out.println("Tam biet!");
                        return;

                    default:
                        System.out.println("Lua chon khong hop le.");
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}