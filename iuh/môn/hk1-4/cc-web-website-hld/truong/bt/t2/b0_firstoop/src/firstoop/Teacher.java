package firstoop;

public class Teacher extends Person {
    private String department;
    private double salary;

    public Teacher() { super(); }

    public Teacher(String id, String name, int age, String department, double salary) {
        super(id, name, age);
        this.department = department;
        this.salary = salary;
    }

    public String getDepartment() { return department; }
    public void setDepartment(String department) { this.department = department; }

    public double getSalary() { return salary; }
    public void setSalary(double salary) { this.salary = salary; }

    @Override
    public String toString() {
        return "Teacher [" + super.toString() + ", department=" + department + ", salary=" + salary + "]";
    }
}
