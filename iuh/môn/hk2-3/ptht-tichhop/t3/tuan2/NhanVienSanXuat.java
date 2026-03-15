package tuan2;

import java.io.*;

public class NhanVienSanXuat extends NhanVien {
    private int soSanPham;
    private double donGia;

    public void nhapSanXuat(BufferedReader br, PrintWriter pw) throws IOException {
        super.nhapThongTin(br, pw);
        pw.print("Nhap so san pham: "); pw.flush();
        soSanPham = Integer.parseInt(br.readLine());
        pw.print("Nhap don gia: "); pw.flush();
        donGia = Double.parseDouble(br.readLine());
    }

    public double tinhLuong() {
        return soSanPham * donGia;
    }

    public void hienThiSanXuat(PrintWriter pw) {
        super.hienThiThongTin(pw);
        pw.println("Luong San Xuat: " + tinhLuong());
    }
}