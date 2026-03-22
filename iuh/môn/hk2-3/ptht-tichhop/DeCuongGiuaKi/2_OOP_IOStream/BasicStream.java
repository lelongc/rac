package OOP_IOStream;

import java.io.*;

public class BasicStream {
    public static void main(String[] args) {
        System.out.println("===== CHON BAI TAP TUAN 3 STREAM (BO COMMENT DE CHAY) =====");

        // =========================================================================
        // DANG 1 (Ex1): Doc InputStream tung byte (char) cho den khi gap 'q'
        // =========================================================================
        /*
        System.out.println("-> Nhap cac ki tu roi an Enter (go 'q' de ket thuc):");
        InputStream is = System.in;
        while (true) {
            try {
                int ch = is.read();
                if (ch == -1 || (char)ch == 'q') {
                    while(is.available() > 0) is.read(); // xoa bo dem
                    break;
                }
                if (ch != '\r' && ch != '\n') {
                    System.out.println("Ban vua nhap: " + (char) ch);
                }
            } catch (IOException ie) {
                System.out.println("Error: " + ie);
            }
        }
        */

        // =========================================================================
        // DANG 2 (Ex2): Doc InputStream bang byte[] va is.available()
        // =========================================================================
        /*
        System.out.println("-> Nhap mot chuoi (go dau '.' de bo qua cho trong, Ctrl+C de ngat):");
        InputStream is2 = System.in;
        while (true) {
            try {
                int num = is2.available();
                if (num > 0) {
                    byte[] b = new byte[num];
                    int result = is2.read(b);
                    if (result == -1) break;
                    String s = new String(b);
                    System.out.print(s); // in ra chuoi vua nhap
                } else {
                    // System.out.print("."); // (Giau di vi in luyen thuyen)
                    Thread.sleep(100); 
                }
            } catch (Exception ie) {
                System.out.println("Error: " + ie);
            }
        }
        */

        // =========================================================================
        // DANG 3 (Ex3): Su dung BufferedReader de doc tung dong (readLine)
        // =========================================================================
        /*
        System.out.println("-> Nhap tung dong văn ban (go 'exit' de ket thuc):");
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(isr);
        while (true) {
            try {
                String line = br.readLine();
                if (line != null && line.equalsIgnoreCase("exit")) break;
                if (line != null) {
                    System.out.println("Da nhan dong: " + line);
                }
            } catch (IOException ie) {
                System.out.println("Error: " + ie);
            }
        }
        */

        // =========================================================================
        // DANG 4 (Ex4): Su dung PrintWriter de ghi ra chong System.out
        // =========================================================================
        /*
        System.out.println("-> Xuat PrintWriter:");
        OutputStream os = System.out;
        PrintWriter pw = new PrintWriter(os, true); 
        pw.write("this is a string (Su dung pw.write) \r\n");
        pw.println("this is a line (Su dung pw.println)");
        pw.write("Bye!Bye!\n");
        // pw.flush() da co true trong constructor Auto-flush
        */
    }
}
