package OOP_IOStream;

import java.io.*;

public class Oto extends PhuongTien {
    private int soChoNgoi;

    public void nhapOto(BufferedReader br, PrintWriter pw) throws IOException {
        super.nhapThongTin(br, pw);
        pw.print("Nhap so cho ngoi: "); pw.flush();
        soChoNgoi = Integer.parseInt(br.readLine());
    }

    public double tinhThue() {
        if (soChoNgoi >= 7) return giaBan * 0.3;
        else if (soChoNgoi >= 5) return giaBan * 0.5;
        else return giaBan * 0.7; // Thue tieu thu dac biet tham khao
    }

    public void hienThiOto(PrintWriter pw) {
        super.hienThiThongTin(pw);
        pw.println("So cho ngoi: " + soChoNgoi + " | Thue phai dong: " + tinhThue());
    }
}
