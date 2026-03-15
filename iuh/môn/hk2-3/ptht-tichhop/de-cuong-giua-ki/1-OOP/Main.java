package oop;

public class Main {
    public static void main(String[] args) {
        // Tạo nhân viên văn phòng
        NhanVienVanPhong nv1 = new NhanVienVanPhong();
        System.out.println("=== Nhap nhan vien van phong ===");
        nv1.nhapThongTinVP();

        // Tạo nhân viên sản xuất
        NhanVienSanXuat nv2 = new NhanVienSanXuat();
        System.out.println("\n=== Nhap nhan vien san xuat ===");
        nv2.nhapThongTinSX();

        // Hiển thị kết quả
        System.out.println("\n=== Danh sach nhan vien ===");
        nv1.hienThiThongTin();
        System.out.println(" | Luong: " + nv1.tinhLuong());

        nv2.hienThiThongTin();
        System.out.println(" | Luong: " + nv2.tinhLuong());
    }
}
