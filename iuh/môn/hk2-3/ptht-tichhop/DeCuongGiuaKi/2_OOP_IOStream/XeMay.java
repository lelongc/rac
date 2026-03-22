package OOP_IOStream;

import java.io.*;

public class XeMay extends PhuongTien {
    private int dungTichXiLanh;

    public void nhapXeMay(BufferedReader br, PrintWriter pw) throws IOException {
        super.nhapThongTin(br, pw);
        pw.print("Nhap dung tich xi lanh (cc): "); pw.flush();
        dungTichXiLanh = Integer.parseInt(br.readLine());
    }

    public double tinhThue() {
        if (dungTichXiLanh > 200) return giaBan * 0.2;
        else if (dungTichXiLanh >= 100) return giaBan * 0.1;
        else return giaBan * 0.05;
    }

    public void hienThiXeMay(PrintWriter pw) {
        super.hienThiThongTin(pw);
        pw.println("Dung tich xi lanh: " + dungTichXiLanh + "cc | Thue phai dong: " + tinhThue());
    }
}
