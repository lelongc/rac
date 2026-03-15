package tuan2;

import java.util.Scanner;

public class NhanVienVanPhong extends NhanVien {
    double luongCoBan;

    public void nhapThongTinVP() {
        super.nhapThongTin(); 
        Scanner sc = new Scanner(System.in);
        System.out.print("nhap luong can ban : ");
        luongCoBan = sc.nextDouble();
    }

    public double tinhLuong() {
        return luongCoBan;
    }
}