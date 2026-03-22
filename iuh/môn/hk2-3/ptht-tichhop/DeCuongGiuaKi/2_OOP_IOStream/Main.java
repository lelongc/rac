package OOP_IOStream;

import java.io.*;

public class Main {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out, true);

        System.out.println("=== CHON BAI TAP TUAN 2 OOP (BO COMMENT DE CHAY) ===");

        // =========================================================================
        // DANG 1: QUAN LY NHAN VIEN (NV Van Phong & NV San Xuat)
        // =========================================================================
        /*
        try {
            pw.println("--> NHAP THONG TIN NV VAN PHONG:");
            NhanVienVanPhong nvvp = new NhanVienVanPhong();
            nvvp.nhapVanPhong(br, pw);

            pw.println("\n--> NHAP THONG TIN NV SAN XUAT:");
            NhanVienSanXuat nvsx = new NhanVienSanXuat();
            nvsx.nhapSanXuat(br, pw);

            pw.println("\n--- KET QUA ---");
            nvvp.hienThiVanPhong(pw);
            nvsx.hienThiSanXuat(pw);
        } catch (Exception e) {}
        */

        // =========================================================================
        // DANG 2: QUAN LY PHUONG TIEN (Oto & Xe May)
        // =========================================================================
        /*
        try {
            pw.println("--> NHAP THONG TIN OTO:");
            Oto oto = new Oto();
            oto.nhapOto(br, pw);

            pw.println("\n--> NHAP THONG TIN XE MAY:");
            XeMay xm = new XeMay();
            xm.nhapXeMay(br, pw);
            
            pw.println("\n--- KET QUA OTO ---");
            oto.hienThiOto(pw);

            pw.println("\n--- KET QUA XE MAY ---");
            xm.hienThiXeMay(pw);
        } catch (Exception e) {}
        */

        // =========================================================================
        // DANG 3: QUAN LY DONG VAT (Cho & Meo)
        // =========================================================================
        /*
        DongVat cho = new Cho("Corgi", 2);
        DongVat meo = new Meo("Mimi", 1);
        
        System.out.println("--- THONG TIN CHO ---");
        cho.inThongTin(); cho.an(); cho.taoAmThanh(); ((Cho)cho).chay();
        
        System.out.println("\n--- THONG TIN MEO ---");
        meo.inThongTin(); meo.an(); meo.taoAmThanh(); ((Meo)meo).leoTuong();
        */
    }
}
