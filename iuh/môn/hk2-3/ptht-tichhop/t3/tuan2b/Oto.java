/**
 * 
 */
package tuan2b;

import java.io.*;

public class Oto extends PhuongTien {
    private int soChoNgoi;

    public void nhapOto(BufferedReader br, PrintWriter pw) throws IOException {
        super.nhapThongTin(br, pw);
        pw.print("Nhap so cho ngoi: "); pw.flush();
        soChoNgoi = Integer.parseInt(br.readLine());
    }

    public double tinhThue() {
        return giaBan * 0.1; 
    }

    @Override
    public void hienThiThongTin(PrintWriter pw) {
        pw.println("\nTHONG TIN O TO");
        super.hienThiThongTin(pw);
        pw.println("So cho ngoi: " + soChoNgoi);
        pw.println("Thue phai nop: " + tinhThue());
    }
}