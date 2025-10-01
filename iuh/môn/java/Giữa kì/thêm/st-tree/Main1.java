import java.util.Scanner;

public class Main1 {
    private static StudentBST dsSV = new StudentBST();
    private static Scanner scanner = new Scanner(System.in);
    
    public static void main(String[] args) {
        System.out.println("=== CHUONG TRINH QUAN LY SINH VIEN ===");
        System.out.println("Su dung cay BST de quan ly danh sach sinh vien\n");
        
        // Them mot so du lieu mau
        themDuLieuMau();
        
        int luaChon;
        do {
            hienThiMenu();
            luaChon = nhapLuaChon();
            xuLyLuaChon(luaChon);
        } while (luaChon != 0);
        
        System.out.println("Cam on ban da su dung chuong trinh!");
        scanner.close();
    }
    
    private static void hienThiMenu() {
        System.out.println("\n=== MENU CHINH ===");
        System.out.println("1. Them sinh vien");
        System.out.println("2. Xoa sinh vien");
        System.out.println("3. Hien thi danh sach sinh vien");
        System.out.println("4. Xuat thong tin tong ket");
        System.out.println("5. Thong ke phan loai diem");
        System.out.println("6. Tim kiem sinh vien theo ID");
        System.out.println("7. Them du lieu mau");
        System.out.println("0. Thoat chuong trinh");
        System.out.print("Nhap lua chon cua ban: ");
    }
    
    private static int nhapLuaChon() {
        try {
            return Integer.parseInt(scanner.nextLine());
        } catch (NumberFormatException e) {
            return -1;
        }
    }
    
    private static void xuLyLuaChon(int luaChon) {
        switch (luaChon) {
            case 1:
                themSinhVien();
                break;
            case 2:
                xoaSinhVien();
                break;
            case 3:
                dsSV.hienThi();
                break;
            case 4:
                dsSV.xuatThongTin();
                break;
            case 5:
                dsSV.thongKeDiem();
                break;
            case 6:
                timKiemSinhVien();
                break;
            case 7:
                themDuLieuMau();
                break;
            case 0:
                System.out.println("Dang thoat chuong trinh...");
                break;
            default:
                System.out.println("Lua chon khong hop le! Vui long chon lai.");
        }
    }
    
    private static void themSinhVien() {
        System.out.println("\n--- THEM SINH VIEN ---");
        try {
            System.out.print("Nhap ID sinh vien: ");
            int id = Integer.parseInt(scanner.nextLine());
            
            System.out.print("Nhap ten sinh vien: ");
            String ten = scanner.nextLine();
            
            System.out.print("Nhap diem sinh vien (0-10): ");
            double diem = Double.parseDouble(scanner.nextLine());
            
            if (diem < 0 || diem > 10) {
                System.out.println("Diem phai trong khoang 0-10!");
                return;
            }
            
            dsSV.themSV(id, ten, diem);
            
        } catch (NumberFormatException e) {
            System.out.println("Du lieu nhap khong hop le!");
        }
    }
    
    private static void xoaSinhVien() {
        System.out.println("\n--- XOA SINH VIEN ---");
        try {
            System.out.print("Nhap ID sinh vien can xoa: ");
            int id = Integer.parseInt(scanner.nextLine());
            dsSV.xoaSV(id);
        } catch (NumberFormatException e) {
            System.out.println("ID khong hop le!");
        }
    }
    
    private static void timKiemSinhVien() {
        System.out.println("\n--- TIM KIEM SINH VIEN ---");
        try {
            System.out.print("Nhap ID sinh vien can tim: ");
            int id = Integer.parseInt(scanner.nextLine());
            dsSV.timKiem(id);
        } catch (NumberFormatException e) {
            System.out.println("ID khong hop le!");
        }
    }
    
    private static void themDuLieuMau() {
        System.out.println("\n--- THEM DU LIEU MAU ---");
        dsSV.themSV(103, "Nguyen Van A", 8.5);
        dsSV.themSV(101, "Tran Thi B", 6.0);
        dsSV.themSV(105, "Le Van C", 9.2);
        dsSV.themSV(102, "Pham Thi D", 4.5);
        dsSV.themSV(104, "Hoang Van E", 7.8);
        dsSV.themSV(106, "Vu Thi F", 5.5);
        dsSV.themSV(107, "Dao Van G", 9.8);
        dsSV.themSV(108, "Bui Thi H", 3.2);
        System.out.println("Da them du lieu mau vao he thong!");
    }
}
