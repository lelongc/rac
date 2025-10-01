public class Main {
    public static void main(String[] args) {
        StudentBST dsSV = new StudentBST();
        
        System.out.println("=== TEST CHUONG TRINH QUAN LY SINH VIEN ===\n");
        
        // a) Them sinh vien
        System.out.println("--- THEM SINH VIEN ---");
        dsSV.themSV(103, "Nguyen Van A", 8.5);
        dsSV.themSV(101, "Tran Thi B", 6.0);
        dsSV.themSV(105, "Le Van C", 9.2);
        dsSV.themSV(102, "Pham Thi D", 4.5);
        dsSV.themSV(104, "Hoang Van E", 7.8);
        dsSV.themSV(106, "Vu Thi F", 5.5);
        
        // Hien thi danh sach
        dsSV.hienThi();
        
        // c) Xuat thong tin
        dsSV.xuatThongTin();
        
        // d) Thong ke phan loai
        dsSV.thongKeDiem();
        
        // b) Xoa sinh vien
        System.out.println("\n--- XOA SINH VIEN ---");
        dsSV.xoaSV(102);
        dsSV.hienThi();
        
        // Xuat lai thong tin sau khi xoa
        dsSV.xuatThongTin();
        dsSV.thongKeDiem();
    }
}
