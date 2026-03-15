package tuan2;

import java.io.*;

public class Main {
    public static void main(String[] args) {
                     
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        
        PrintWriter pw = new PrintWriter(System.out, true);

        try {
            pw.println("NHAP NHAN VIEN VAN PHONG");
            NhanVienVanPhong nvvp = new NhanVienVanPhong();
            nvvp.nhapVanPhong(br, pw);

            pw.println("\nNHAP NHAN VIEN SAN XUAT");
            NhanVienSanXuat nvsx = new NhanVienSanXuat();
            nvsx.nhapSanXuat(br, pw);

            pw.println("\nKET QUA QUAN LY ");
            nvvp.hienThiVanPhong(pw);
            pw.println(" ");
            nvsx.hienThiSanXuat(pw);

        } catch (IOException e) {
            pw.println("Loi doc du lieu: " + e.getMessage());
        } catch (NumberFormatException e) {
            pw.println("Loi dinh dang so: Vui long nhap dung con so!");
        } finally {
            
            pw.close();
        }
    }
}