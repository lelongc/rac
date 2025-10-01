public class Student {
    int Student_ID;
    String Student_name;
    double Student_Result;
    Student Prev;
    Student Next;
    Student Left;
    Student Right;
    
    public Student(int ID, String name, double result) {
        this.Student_ID = ID;
        this.Student_name = name;
        this.Student_Result = result;
        this.Prev = null;
        this.Next = null;
        this.Left = null;
        this.Right = null;
    }
    
    @Override
    public String toString() {
        return String.format("ID: %d | Ten: %-20s | Diem: %.2f", 
            Student_ID, Student_name, Student_Result);
    }
}
