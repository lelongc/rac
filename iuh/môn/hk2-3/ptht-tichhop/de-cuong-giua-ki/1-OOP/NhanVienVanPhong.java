package oop;

import java.util.Scanner;

// Lớp con - kế thừa NhanVien
public class NhanVienVanPhong extends NhanVien {
    double luongCoBan;

    public void nhapThongTinVP() {
        super.nhapThongTin(); // gọi method lớp cha
        Scanner sc = new Scanner(System.in);
        System.out.print("Nhap luong co ban: ");
        luongCoBan = sc.nextDouble();
    }

    @Override
    public double tinhLuong() {
        return luongCoBan;
    }

    @Override
    public void hienThiThongTin() {
        super.hienThiThongTin(); // gọi method lớp cha
        System.out.print(" | Loai: Van phong");
    }
}
