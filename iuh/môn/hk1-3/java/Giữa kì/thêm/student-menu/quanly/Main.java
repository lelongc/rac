package quanly;

import java.util.Optional;
import java.util.Scanner;

public class Main {
    private static Scanner scanner = new Scanner(System.in);
    private static QuanLyHocSinh manager = new QuanLyHocSinh();

    public static void main(String[] args) {
        int choice;
        do {
            System.out.println("\n--- MENU QUAN LY HOC SINH ---");
            System.out.println("1. Them hoc sinh");
            System.out.println("2. Xoa hoc sinh theo ma");
            System.out.println("3. Tim hoc sinh theo ma");
            System.out.println("4. Sap xep theo ten");
            System.out.println("5. Sap xep theo diem (giam dan)");
            System.out.println("6. Hien thi danh sach");
            System.out.println("7. Luu danh sach vao file");
            System.out.println("8. Doc danh sach tu file");
            System.out.println("0. Thoat");
            System.out.print(">> Chon chuc nang: ");

            try {
                choice = Integer.parseInt(scanner.nextLine());
                
                switch (choice) {
                    case 1:
                        System.out.print("Nhap Ma HS: "); String maHS = scanner.nextLine();
                        System.out.print("Nhap Ten HS: "); String tenHS = scanner.nextLine();
                        System.out.print("Nhap Diem : "); double diem = Double.parseDouble(scanner.nextLine());
                        
                        // ==========================================================
                        // ===== THAY ĐỔI: KIỂM TRA ĐIỂM NGAY TẠI NƠI NHẬP LIỆU =====
                        // ==========================================================
                        if (diem < 0 || diem > 10) {
                            System.out.println("Loi: Diem phai nam trong khoang tu 0 den 10.");
                            System.out.println("=> Thao tac them da bi huy. Quay ve menu chinh.");
                        } else {
                            // Chỉ thêm sinh viên nếu điểm hợp lệ
                            manager.themHS(maHS, tenHS, diem);
                            System.out.println("=> Da them hoc sinh thanh cong.");
                        }
                        break;
                    case 2:
                        System.out.print("Nhap Ma HS can xoa: "); String maXoa = scanner.nextLine();
                        if (manager.xoaHS(maXoa)) System.out.println("=> Da xoa.");
                        else System.out.println("=> Khong tim thay HS.");
                        break;
                    case 3:
                        System.out.print("Nhap Ma HS can tim: "); String maTim = scanner.nextLine();
                        Optional<HocSinh> hsOpt = manager.timHSTheoMa(maTim);
                        if (hsOpt.isPresent()) {
                            System.out.println("=> Tim thay:");
                            System.out.println(hsOpt.get());
                        } else {
                            System.out.println("=> Khong tim thay HS.");
                        }
                        break;
                    case 4:
                        manager.sapXepTheoTen();
                        System.out.println("=> Da sap xep theo ten.");
                        manager.hienThiDanhSach();
                        break;
                    case 5:
                        manager.sapXepTheoDiem();
                        System.out.println("=> Da sap xep theo diem.");
                        manager.hienThiDanhSach();
                        break;
                    case 6:
                        manager.hienThiDanhSach();
                        break;
                    case 7:
                        if (manager.luuFile()) System.out.println("=> Da luu file thanh cong.");
                        else System.out.println("=> Luu file that bai.");
                        break;
                    case 8:
                        if (manager.docFile()) {
                            System.out.println("=> Da doc file thanh cong.");
                            manager.hienThiDanhSach();
                        } else {
                            System.out.println("=> Doc file that bai.");
                        }
                        break;
                    case 0:
                        System.out.println("Da thoat chuong trinh.");
                        break;
                    default:
                        System.out.println("Chuc nang khong hop le.");
                }
            } catch (NumberFormatException e) {
                System.out.println("Vui long nhap mot so.");
                choice = -1; 
            }
        } while (choice != 0);
        
        scanner.close();
    }
}