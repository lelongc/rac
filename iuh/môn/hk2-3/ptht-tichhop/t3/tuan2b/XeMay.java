package tuan2b;

import java.io.*;

public class XeMay extends PhuongTien {
    private int dungTichXiLanh;

    public void nhapXeMay(BufferedReader br, PrintWriter pw) throws IOException {
        super.nhapThongTin(br, pw); 
        pw.print("Nhap dung tich xi lanh (cc): "); pw.flush();
        dungTichXiLanh = Integer.parseInt(br.readLine());
    }

    public double tinhThue() {
        return giaBan * 0.05; 
    }

    @Override
    public void hienThiThongTin(PrintWriter pw) {
        pw.println("\nTHONG TIN XE MAY");
        super.hienThiThongTin(pw);
        pw.println("Dung tich: " + dungTichXiLanh + "cc");
        pw.println("Thue phai nop: " + tinhThue());
    }
}