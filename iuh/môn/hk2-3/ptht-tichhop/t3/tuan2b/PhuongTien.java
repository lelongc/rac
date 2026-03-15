package tuan2b;

import java.io.*;

public class PhuongTien {
    protected String hangSanXuat;
    protected int namSanXuat;
    protected double giaBan;

   
    public void nhapThongTin(BufferedReader br, PrintWriter pw) throws IOException {
        pw.print("Nhap hang san xuat: "); pw.flush();
        hangSanXuat = br.readLine();
        
        pw.print("Nhap nam san xuat: "); pw.flush();
        namSanXuat = Integer.parseInt(br.readLine());
        
        pw.print("Nhap gia ban: "); pw.flush();
        giaBan = Double.parseDouble(br.readLine());
    }

    public void hienThiThongTin(PrintWriter pw) {
        pw.println("Hang SX: " + hangSanXuat);
        pw.println("Nam SX: " + namSanXuat);
        pw.println("Gia ban: " + giaBan);
    }
}