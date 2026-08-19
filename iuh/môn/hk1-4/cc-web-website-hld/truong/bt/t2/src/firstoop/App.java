package firstoop;

public class App {
    public static void main(String[] args) {
        System.out.println("=== CHUONG TRINH QUAN LY THANH VIEN (FIRST OOP) ===");

        PersonManagement pm = new PersonManagement();

        Student s1 = new Student("P01", "Nguyen Van A", 20, "SV001", 3.6);
        Student s2 = new Student("P02", "Tran Thi B", 21, "SV002", 3.8);
        Student s3 = new Student("P03", "Le Van C", 19, "SV003", 3.2);

        Teacher t1 = new Teacher("P04", "Pham Van D", 45, "Cong nghe thong tin", 18000000);
        Teacher t2 = new Teacher("P05", "Hoang Thi E", 38, "Khoa hoc may tinh", 16500000);

        pm.addPerson(s1);
        pm.addPerson(s2);
        pm.addPerson(s3);
        pm.addPerson(t1);
        pm.addPerson(t2);

        pm.displayAll();

        pm.displayStudentsOnly();
        pm.displayTeachersOnly();

        pm.countStats();
    }
}
