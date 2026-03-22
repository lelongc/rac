package OOP_IOStream;

import java.io.*;

public class BasicStream {
    public static void main(String[] args) {
        // Tương đương Lab 2 Week 3
        System.out.println("===== TEST IN STREAM 1 (Doc Char tung byte tung byte) =====");
        System.out.println("Nhap cac ki tu roi an Enter (go 'q' de ket thuc phan nay):");
        InputStream is = System.in;
        while (true) {
            try {
                int ch = is.read();
                if (ch == -1 || (char)ch == 'q') {
                    // Xoa bo dem neu co Enter thua
                    while(is.available() > 0) is.read();
                    break;
                }
                if (ch != '\r' && ch != '\n') {
                    System.out.println("Ban vua nhap: " + (char) ch);
                }
            } catch (IOException ie) {
                System.out.println("Error: " + ie);
            }
        }

        System.out.println("\n===== TEST READ LINE (BufferedReader) =====");
        System.out.println("Nhap tin nhan (go 'exit' de ket thuc):");
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(isr);
        while (true) {
            try {
                String line = br.readLine();
                if (line != null && line.equalsIgnoreCase("exit")) break;
                if (line != null && !line.trim().isEmpty()) {
                    System.out.println("Line nhan duoc: " + line);
                }
            } catch (IOException ie) {
                System.out.println("Error: " + ie);
            }
        }

        System.out.println("\n===== TEST OUT STREAM (PrintWriter) =====");
        OutputStream os = System.out;
        PrintWriter pw = new PrintWriter(os, true); // true de auto-flush
        pw.write("this is a string (Su dung pw.write) \r\n");
        pw.println("this is a line (Su dung pw.println)");
        pw.write("Bye!Bye!\n");
        pw.flush();
    }
}
