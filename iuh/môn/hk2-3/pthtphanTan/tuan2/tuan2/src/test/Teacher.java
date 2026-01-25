package test;

import java.util.Scanner;

public class Teacher extends Person implements IPerson {
    public Teacher(String id, String name, int age) {
		super(id, name, age);
		// TODO Auto-generated constructor stub
	}

	public Teacher() {
		// TODO Auto-generated constructor stub
	}

	private double salary;

    @Override
    public void input(Scanner sc) {
        System.out.print("Enter teacher's ID: ");
        setId(sc.nextLine());
        System.out.print("Enter teacher's name: ");
        setName(sc.nextLine());
        System.out.print("Enter teacher's age: ");
        setAge(sc.nextInt());
        System.out.print("Enter teacher's salary: ");
        salary = sc.nextDouble();
        sc.nextLine(); 
    }

    @Override
    public void display() {
        System.out.println("[Teacher] ID: " + getId() + " | Name: " + getName() + 
                           " | Age: " + getAge() + " | Salary: " + salary);
    }
}