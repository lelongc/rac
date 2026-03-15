package tuan1;

import java.io.*;

public class ex1 {
    public static void main(String[] args) {
       
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out, true);

        try {
           
            pw.println("--- Bai 1 ---");
            pw.println("Hello, World!");

          
            pw.println("\n--- Bai 2 ---");
            pw.print("Nhap ten cua ban: "); pw.flush();
            String name = br.readLine();
            pw.println("Hi, I am " + name);

         
            pw.println("\n--- Bai 3 ---");
            pw.print("Nhap so A: "); pw.flush();
            double a = Double.parseDouble(br.readLine());
            pw.print("Nhap so B: "); pw.flush();
            double b = Double.parseDouble(br.readLine());
            pw.println("Tong A + B = " + (a + b));

          
            pw.println("\n--- Bai 4 ---");
            pw.print("Nhap mot so nguyen: "); pw.flush();
            int n = Integer.parseInt(br.readLine());
            if (n % 2 == 0) {
                pw.println(n + " la so chan");
            } else {
                pw.println(n + " la so le");
            }

            
            pw.println("\n--- Bai 5 ---");
            pw.print("Nhap mot thang (1-12): "); pw.flush();
            int month = Integer.parseInt(br.readLine());
            String result;
            switch (month) {
                case 1:  result = "January"; break;
                case 2:  result = "February"; break;
                case 3:  result = "March"; break;
                case 4:  result = "April"; break;
                case 5:  result = "May"; break;
                case 6:  result = "June"; break;
                case 7:  result = "July"; break;
                case 8:  result = "August"; break;
                case 9:  result = "September"; break;
                case 10: result = "October"; break;
                case 11: result = "November"; break;
                case 12: result = "December"; break;
                default: result = "Invalid month!"; break;
            }
            pw.println("English name: " + result);

        } catch (IOException e) {
            pw.println("Loi nhap xuat: " + e.getMessage());
        } catch (NumberFormatException e) {
            pw.println("Loi: Vui long nhap dung dinh dang so!");
        }
    }
}