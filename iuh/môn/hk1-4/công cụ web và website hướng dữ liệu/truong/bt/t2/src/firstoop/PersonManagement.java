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
        System.out.println("=== DANH SACH TAT CA THANH VIEN ===");
        for (Person p : personList) {
            System.out.println(p);
        }
    }

    public void displayStudentsOnly() {
        System.out.println("\n=== DANH SACH SINH VIEN (DUNG INSTANCEOF) ===");
        for (Person p : personList) {
            if (p instanceof Student) {
                Student s = (Student) p;
                System.out.println("[Student] ID: " + s.getStudentId() + " - Ten: " + s.getName() + " - GPA: " + s.getGpa());
            }
        }
    }

    public void displayTeachersOnly() {
        System.out.println("\n=== DANH SACH GIANG VIEN (DUNG INSTANCEOF) ===");
        for (Person p : personList) {
            if (p instanceof Teacher) {
                Teacher t = (Teacher) p;
                System.out.println("[Teacher] Khoa: " + t.getDepartment() + " - Ten: " + t.getName() + " - Luong: " + t.getSalary());
            }
        }
    }

    public void countStats() {
        int studentCount = 0;
        int teacherCount = 0;

        for (Person p : personList) {
            if (p instanceof Student) {
                studentCount++;
            } else if (p instanceof Teacher) {
                teacherCount++;
            }
        }

        System.out.println("\n=== THONG KE SO LUONG (DUNG INSTANCEOF) ===");
        System.out.println("So luong Sinh vien: " + studentCount);
        System.out.println("So luong Giang vien: " + teacherCount);
    }

    public List<Person> getPersonList() {
        return personList;
    }
}
