package oop;

import java.util.Scanner;

// Lớp con - kế thừa NhanVien
public class NhanVienSanXuat extends NhanVien {
    int soSanPham;
    double donGia;

    public void nhapThongTinSX() {
        super.nhapThongTin(); // gọi method lớp cha
        Scanner sc = new Scanner(System.in);
        System.out.print("So san pham: ");
        soSanPham = sc.nextInt();
        System.out.print("Don gia: ");
        donGia = sc.nextDouble();
    }

    @Override
    public double tinhLuong() {
        return soSanPham * donGia;
    }

    @Override
    public void hienThiThongTin() {
        super.hienThiThongTin(); // gọi method lớp cha
        System.out.print(" | Loai: San xuat");
    }
}
