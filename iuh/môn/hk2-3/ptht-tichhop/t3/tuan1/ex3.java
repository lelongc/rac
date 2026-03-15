package tuan1;

import java.io.*;

public class ex3 {
    public static void main(String[] args) throws IOException {
        // InputStream (byte) → InputStreamReader (byte→char) → BufferedReader (buffer + dòng)
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out, true);

        try {
            pw.print("Nhap so A: "); pw.flush();
            int a = Integer.parseInt(br.readLine());

            pw.print("Nhap so B: "); pw.flush();
            int b = Integer.parseInt(br.readLine());

            pw.println("Tong cua A + B la: " + (a + b));
        } catch (NumberFormatException e) {
            pw.println("Vui long nhap so nguyen hop le!");
        }
    }
}
