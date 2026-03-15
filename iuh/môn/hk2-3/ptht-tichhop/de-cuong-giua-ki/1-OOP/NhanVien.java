package oop;

import java.util.Scanner;

// Lớp cha - abstract (không thể tạo trực tiếp)
public abstract class NhanVien {
    String maNV;
    String hoTen;

    public void nhapThongTin() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Nhap ma NV: ");
        maNV = sc.nextLine();
        System.out.print("Nhap ho ten: ");
        hoTen = sc.nextLine();
    }

    public void hienThiThongTin() {
        System.out.print("Ma NV: " + maNV + " | Ho ten: " + hoTen);
    }

    // Abstract: bắt buộc lớp con phải override
    public abstract double tinhLuong();
}
