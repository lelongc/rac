package tuan1;

import java.io.*;

public class ex2 {
    public static void main(String[] args) throws IOException {
        // InputStream (byte) → InputStreamReader (byte→char) → BufferedReader (buffer + dòng)
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out, true);

        pw.print("Nhap ten cua ban: "); pw.flush();
        String name = br.readLine();
        pw.println("Hi, I am " + name);
    }
}