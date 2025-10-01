package StudentApp1;

import java.io.Serializable;

public class Student implements Serializable {
    private int studentId;
    private String studentName;
    private double studentResult;
    private Student prev;
    private Student next;

    public Student(int id, String name, double result) {
        this.studentId = id;
        this.studentName = name;
        this.studentResult = result;
        this.prev = null;
        this.next = null;
    }

    public int getStudentId() {
        return studentId;
    }

    public void setStudentId(int studentId) {
        this.studentId = studentId;
    }

    public String getStudentName() {
        return studentName;
    }

    public void setStudentName(String studentName) {
        this.studentName = studentName;
    }

    public double getStudentResult() {
        return studentResult;
    }

    public void setStudentResult(double studentResult) {
        this.studentResult = studentResult;
    }

    public Student getPrev() {
        return prev;
    }

    public void setPrev(Student prev) {
        this.prev = prev;
    }

    public Student getNext() {
        return next;
    }

    public void setNext(Student next) {
        this.next = next;
    }

    @Override
    public String toString() {
        return "ID: " + studentId + ", Name: " + studentName + ", Score: " + studentResult;
    }
}