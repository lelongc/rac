package test;


import java.util.ArrayList;
import java.util.Scanner;

public class PersonManager {
   
    private ArrayList<Person> list = new ArrayList<>();

   
    public void addPerson(Person p) {
        list.add(p);
        System.out.println("Added successfully!");
    }

  
    public void displayAll() {
        if (list.isEmpty()) {
            System.out.println("List is empty!");
            return;
        }

        System.out.println("\n--- LIST OF PERSONS ---");
        for (Person p : list) {
           
            if (p instanceof IPerson) {
                ((IPerson) p).display(); 
            }
        }
    }
}