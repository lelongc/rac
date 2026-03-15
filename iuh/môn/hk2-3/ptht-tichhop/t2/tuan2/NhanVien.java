package tuan2;

import java.util.Scanner;

public class NhanVien {
    String maNV;
    String hoTen;

    
    public void nhapThongTin() {
        Scanner sc = new Scanner(System.in);
        System.out.print("nhap ma nv: ");
        maNV = sc.nextLine();
        System.out.print("nhap ho ten: ");
        hoTen = sc.nextLine();
    }

   
    public void hienThiThongTin() {
        System.out.print("ma nv : " + maNV + " | ho ten : " + hoTen);
    }
}