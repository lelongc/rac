package test;

import java.util.Scanner;

public class Teacher extends Person implements IPerson {
    private double luong;

    @Override
    public void input(Scanner sc) {
        System.out.print("Nhap Ma GV: ");
        id = sc.nextLine();
        System.out.print("Nhap Ten GV: ");
        name = sc.nextLine();
        System.out.print("Nhap Tuoi: ");
        age = sc.nextInt();
        System.out.print("Nhap Luong: ");
        luong = sc.nextDouble();
        sc.nextLine(); 
    }

    @Override
    public void display() {
        System.out.println("[Giao Vien] Ma: " + id + " | Ten: " + name + 
                           " | Tuoi: " + age + " | Luong: " + luong);
    }
}