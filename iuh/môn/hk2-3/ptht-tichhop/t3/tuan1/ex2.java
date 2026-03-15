package tuan1;

import java.util.Scanner;

public class ex2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Nhap ten cua ban: ");
        String name = sc.nextLine(); 
        System.out.println("Hi, I am " + name);
    }
}