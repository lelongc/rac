package test;

import java.util.Scanner;

public class Student extends Person implements IPerson {
    public Student(String id, String name, int age) {
		super(id, name, age);
		// TODO Auto-generated constructor stub
	}
    

	public Student() {
		// TODO Auto-generated constructor stub
	}


	private double gpa;

    @Override
    public void input(Scanner sc) {
        System.out.print("Enter student's ID: ");
        setId(sc.nextLine());
        System.out.print("Enter student's name: ");
        setName(sc.nextLine());
        System.out.print("Enter student's age: ");
        setAge(sc.nextInt());
        System.out.print("Enter student's GPA: ");
        gpa = sc.nextDouble();
        sc.nextLine();
    }

    @Override
    public void display() {
        System.out.println("[student] ID: " + getId() + " | Name: " + getName() + 
                           " | Age: " + getAge() + " | GPA: " + gpa);
    }
}