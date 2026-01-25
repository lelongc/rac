package test;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        PersonManager manager = new PersonManager();
        
        while (true) {
            System.out.println("\n====== MANAGEMENT SYSTEM ======");
            System.out.println("1. Add new Student");
            System.out.println("2. Add new Teacher");
            System.out.println("3. Show all list");
            System.out.println("0. Exit");
            System.out.print("Choose option: ");
            
            int choice = sc.nextInt();
            sc.nextLine(); 

            switch (choice) {
                case 1:
                    System.out.println("--- Enter Student Info ---");
                    Student s = new Student();
                    s.input(sc); 
                    manager.addPerson(s);
                    break;
                case 2:
                    System.out.println("--- Enter Teacher Info ---");
                    Teacher t = new Teacher();
                    t.input(sc);
                    manager.addPerson(t);
                    break;
                case 3:
                    manager.displayAll();
                    break;
                case 0:
                    System.out.println("Exiting program...");
                    sc.close();
                    return; 
                default:
                    System.out.println("Invalid option! Please choose again.");
            }
        }
    }
}