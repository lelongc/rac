package tuan1;

import java.io.*;

public class ex4 {
    public static void main(String[] args) throws IOException {
        // InputStream (byte) → InputStreamReader (byte→char) → BufferedReader (buffer + dòng)
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out, true);

        pw.print("Nhap vao mot so: "); pw.flush();
        int n = Integer.parseInt(br.readLine());

        if (n % 2 == 0) {
            pw.println(n + " la so chan.");
        } else {
            pw.println(n + " la so le.");
        }
    }
}