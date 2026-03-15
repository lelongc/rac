package tuan2;

import java.io.*;

public class NhanVien {
    protected String maNV;
    protected String hoTen;

   
    public void nhapThongTin(BufferedReader br, PrintWriter pw) throws IOException {
        pw.print("Nhap ma nhan vien: "); pw.flush();
        maNV = br.readLine();
        pw.print("Nhap ho ten: "); pw.flush();
        hoTen = br.readLine();
    }

    public void hienThiThongTin(PrintWriter pw) {
        pw.println("Ma NV: " + maNV);
        pw.println("Ho ten: " + hoTen);
    }
}