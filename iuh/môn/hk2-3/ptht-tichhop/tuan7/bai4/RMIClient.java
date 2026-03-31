package bai4;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class RMIClient {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);
            ContactService service = (ContactService) registry.lookup("ContactService");

            while (true) {
                System.out.println("\n===== QUAN LY DANH BA =====");
                System.out.println("1. Them / Cap nhat lien he");
                System.out.println("2. Tim lien he");
                System.out.println("3. Xoa lien he");
                System.out.println("0. Thoat");
                System.out.print("Chon: ");

                int choice = Integer.parseInt(sc.nextLine().trim());

                switch (choice) {
                    case 1:
                        System.out.print("Nhap ten: ");
                        String nameAdd = sc.nextLine().trim();
                        System.out.print("Nhap so dien thoai: ");
                        String phone = sc.nextLine().trim();
                        service.addContact(nameAdd, phone);
                        System.out.println("Da luu lien he.");
                        break;

                    case 2:
                        System.out.print("Nhap ten can tim: ");
                        String nameFind = sc.nextLine().trim();
                        String result = service.findContact(nameFind);
                        if (result != null) {
                            System.out.println("So dien thoai: " + result);
                        } else {
                            System.out.println("Khong tim thay lien he.");
                        }
                        break;

                    case 3:
                        System.out.print("Nhap ten can xoa: ");
                        String nameDelete = sc.nextLine().trim();
                        boolean deleted = service.deleteContact(nameDelete);
                        System.out.println(deleted ? "Xoa thanh cong." : "Khong tim thay de xoa.");
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