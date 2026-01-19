package test;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        
        System.out.println("NHAP THONG TIN SINH VIEN");
        SinhVien sv = new SinhVien();
        sv.nhap(sc);

        
        System.out.println("\nNHAP THONG TIN GIAO VIEN");
        GiaoVien gv = new GiaoVien();
        gv.nhap(sc);

        
        System.out.println("\nKET QUA QUAN LY");
        sv.hienThi();
        gv.hienThi();

        sc.close();
    }
}