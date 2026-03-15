package tuan2b;

import java.io.*;

public class Main {
    public static void main(String[] args) {
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        
        PrintWriter pw = new PrintWriter(System.out, true);

        try {
          
            pw.println("NHAP DU LIEU XE MAY:");
            XeMay xm = new XeMay();
            xm.nhapXeMay(br, pw);

          
            pw.println("\nNHAP DU LIEU O TO:");
            Oto ot = new Oto();
            ot.nhapOto(br, pw);

         
            pw.println("\nKET QUA QUAN LY");
            xm.hienThiThongTin(pw);
            pw.println(" ");
            ot.hienThiThongTin(pw);

        } catch (IOException e) {
            pw.println("Loi vao ra du lieu: " + e.getMessage());
        } catch (NumberFormatException e) {
            pw.println("Loi sai dinh dang so!");
        } finally {
           
            pw.flush();
        }
    }
}