package tuan1;

import java.util.Scanner;

public class ex4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Nhap vao mot so: ");
        int n = sc.nextInt();
        
        if (n % 2 == 0) {
            System.out.println(n + " la so chan.");
        } else {
            System.out.println(n + " la so le.");
        }
    }
}