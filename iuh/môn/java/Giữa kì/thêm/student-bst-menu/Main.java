import java.util.InputMismatchException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);
        StudentBST dsSV = new StudentBST();
        
        // Them du lieu mau
        dsSV.themSV(103, "Nguyen Van An", 8.5);
        dsSV.themSV(101, "Tran Thi Binh", 6.0);
        dsSV.themSV(105, "Le Van Chien", 9.2);
        dsSV.themSV(102, "Pham Thi Dung", 4.5);
        dsSV.themSV(104, "Hoang Van Em", 7.8);
        dsSV.themSV(106, "Vu Thi Phuong", 5.5);
        
        System.out.println("\n╔════════════════════════════════════════════════════╗");
        System.out.println("║    CHUONG TRINH QUAN LY SINH VIEN BST             ║");
        System.out.println("╚════════════════════════════════════════════════════╝");
        
        while (true) {
            
            System.out.println("\n╔════════════════════════════════════════════════════╗");
            System.out.println("║               MENU CHUC NANG                      ║");
            System.out.println("╠════════════════════════════════════════════════════╣");
            System.out.println("║ 1. Them sinh vien moi                             ║");
            System.out.println("║ 2. Xoa sinh vien theo ID                          ║");
            System.out.println("║ 3. Hien thi danh sach sinh vien                   ║");
            System.out.println("║ 4. Xuat thong tin tong hop                        ║");
            System.out.println("║ 5. Thong ke phan loai diem                        ║");
            System.out.println("║ 0. Thoat chuong trinh                             ║");
            System.out.println("╚════════════════════════════════════════════════════╝");
            System.out.print(">> Vui long chon chuc nang: ");
            
            int choice = -1;
            try {
                choice = scanner.nextInt();
            } catch (InputMismatchException e) {
                System.out.println("✗ Loi: Vui long chi nhap so!");
                scanner.next();
                continue;
            }
            
            switch (choice) {
                case 1:
                    // Them sinh vien moi
                    System.out.println("\n--- Them sinh vien moi ---");
                    System.out.print("Nhap ID: ");
                    int id = -1;
                    try {
                        id = scanner.nextInt();
                    } catch (InputMismatchException e) {
                        System.out.println("✗ Loi: ID phai la so nguyen!");
                        scanner.next();
                        break;
                    }
                    scanner.nextLine();
                    
                    System.out.print("Nhap ten: ");
                    String ten = scanner.nextLine();
                    
                    System.out.print("Nhap diem (0-10): ");
                    double diem = -1;
                    try {
                        diem = scanner.nextDouble();
                        if (diem < 0 || diem > 10) {
                            System.out.println("✗ Loi: Diem phai tu 0 den 10!");
                            break;
                        }
                    } catch (InputMismatchException e) {
                        System.out.println("✗ Loi: Diem phai la so!");
                        scanner.next();
                        break;
                    }
                    
                    dsSV.themSV(id, ten, diem);
                    break;
                    
                case 2:
                    // Xoa sinh vien
                    System.out.print("\nNhap ID sinh vien can xoa: ");
                    int xoaId = -1;
                    try {
                        xoaId = scanner.nextInt();
                    } catch (InputMismatchException e) {
                        System.out.println("✗ Loi: ID phai la so nguyen!");
                        scanner.next();
                        break;
                    }
                    dsSV.xoaSV(xoaId);
                    break;
                    
                case 3:
                    // Hien thi danh sach
                    dsSV.hienThi();
                    break;
                    
                case 4:
                    // Xuat thong tin tong hop
                    dsSV.xuatThongTin();
                    break;
                    
                case 5:
                    // Thong ke phan loai
                    dsSV.thongKeDiem();
                    break;
                    
                case 0:
                    // Thoat chuong trinh
                    System.out.println("\n╔════════════════════════════════════════════════════╗");
                    System.out.println("║     Cam on da su dung chuong trinh!               ║");
                    System.out.println("╚════════════════════════════════════════════════════╝");
                    scanner.close();
                    System.exit(0);
                    break;
                    
                default:
                    System.out.println("✗ Lua chon khong hop le, vui long chon lai tu 0 den 5.");
            }
        }
    }
}
