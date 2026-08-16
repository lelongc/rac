package firstoop;

import java.util.ArrayList;
import java.util.List;

public class PersonManagement {
    private List<Person> personList;

    public PersonManagement() {
        this.personList = new ArrayList<>();
    }

    public void addPerson(Person p) {
        personList.add(p);
    }

    public void displayAll() {
        System.out.println("=== DANH SACH THANH VIEN ===");
        for (Person p : personList) {
            System.out.println(p);
        }
    }

    public List<Person> getPersonList() {
        return personList;
    }
}
