package test;

import java.util.Scanner;

public class Student extends Person implements IPerson {
    private double gpa;

    @Override
    public void input(Scanner sc) {
        System.out.print("Nhap Ma SV: ");
        id = sc.nextLine();
        System.out.print("Nhap Ten SV: ");
        name = sc.nextLine();
        System.out.print("Nhap Tuoi: ");
        age = sc.nextInt();
        System.out.print("Nhap Diem GPA: ");
        gpa = sc.nextDouble();
        sc.nextLine();
    }

    @Override
    public void display() {
        System.out.println("[Sinh Vien] Ma: " + id + " | Ten: " + name + 
                           " | Tuoi: " + age + " | GPA: " + gpa);
    }
}