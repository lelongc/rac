package test;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        
        System.out.println("NHAP THONG TIN SINH VIEN");
        Student sv = new Student();
        sv.input(sc);

        
        System.out.println("\nNHAP THONG TIN GIAO VIEN");
        Teacher gv = new Teacher();
        gv.input(sc);

        
        System.out.println("\nKET QUA QUAN LY");
        sv.display();
        gv.display();

        sc.close();
    }
}