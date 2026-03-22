package OOP_IOStream;

import java.io.*;

public class Main {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out, true);

        try {
            pw.println("NHAP THONG TIN NHAN VIEN VAN PHONG:");
            NhanVienVanPhong nvvp = new NhanVienVanPhong();
            nvvp.nhapVanPhong(br, pw);

            pw.println("\n--- KET QUA ---");
            nvvp.hienThiVanPhong(pw);

        } catch (IOException e) {
            pw.println("Loi xu ly file: " + e.getMessage());
        } catch (NumberFormatException e) {
            pw.println("Loi: Vui long nhap dung dinh dang so!");
        } 
    }
}
