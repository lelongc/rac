package tuan2;

import java.util.Scanner;

public class NhanVienSanXuat extends NhanVien {
    int soSanPham;
    double donGia;

    public void nhapThongTinSX() {
        super.nhapThongTin(); 
        Scanner sc = new Scanner(System.in);
        System.out.print("so san pham : ");
        soSanPham = sc.nextInt();
        System.out.print("don gia : ");
        donGia = sc.nextDouble();
    }

    public double tinhLuong() {
        return soSanPham * donGia;
    }
}