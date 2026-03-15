package tuan2;

           
 
import java.io.*;

public class NhanVienVanPhong extends NhanVien {
    private double luongCoBan;

    public void nhapVanPhong(BufferedReader br, PrintWriter pw) throws IOException {
        super.nhapThongTin(br, pw);
        pw.print("Nhap luong co ban: "); pw.flush();
        luongCoBan = Double.parseDouble(br.readLine());
    }

    public double tinhLuong() {
        return luongCoBan;
    }

    public void hienThiVanPhong(PrintWriter pw) {
        super.hienThiThongTin(pw);
        pw.println("Luong: " + tinhLuong());
    }
}