package tuan1;

import java.util.Scanner;

public class ex3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        try {
            System.out.print("Nhap so A: ");
            int a = sc.nextInt();
            System.out.print("Nhap so B: ");
            int b = sc.nextInt();
            
            int tong = a + b;
            System.out.println("Tong cua A + B la: " + tong);
        } catch (Exception e) {
            System.out.println("Vui long nhap so nguyen hop le!");
        }
    }
}
