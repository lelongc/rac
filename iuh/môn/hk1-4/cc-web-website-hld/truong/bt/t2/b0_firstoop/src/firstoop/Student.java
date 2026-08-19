package firstoop;

public class Student extends Person {
    private String studentId;
    private double gpa;

    public Student() { super(); }

    public Student(String id, String name, int age, String studentId, double gpa) {
        super(id, name, age);
        this.studentId = studentId;
        this.gpa = gpa;
    }

    public String getStudentId() { return studentId; }
    public void setStudentId(String studentId) { this.studentId = studentId; }

    public double getGpa() { return gpa; }
    public void setGpa(double gpa) { this.gpa = gpa; }

    @Override
    public String toString() {
        return "Student [" + super.toString() + ", studentId=" + studentId + ", gpa=" + gpa + "]";
    }
}
