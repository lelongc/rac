package codetuan3.StudentManagement;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;

public class StudentManagement {

    private LinkedList<Student> studentList;

    @SuppressWarnings("unchecked")
    public StudentManagement() {
        this.setStudentList(new LinkedList());
    }

    public List<Student> getStudentList() {
        return studentList;
    }

    public void setStudentList(LinkedList<Student> studentList) {
        this.studentList = studentList;
    }

    public void addStudent(Student student) {
        this.studentList.add(student);
    }

    public void displayStudents() {
        System.out.println("--- DANH SÁCH SINH VIÊN ---");
        if (studentList.isEmpty()) {
            System.out.println("Danh sách trống.");
        } else {

            for (Student student : studentList) {

                System.out.println(student);
            }
        }
        System.out.println("--------------------------");
    }

    public void sortByName() {

        this.studentList.sort(Comparator.comparing(Student::getName));
        System.out.println("Đã sắp xếp danh sách theo tên.");
    }

    public void sortBySe() {

        this.studentList.sort(Comparator.comparing(Student::getResult).reversed());
        System.out.println("Đã sắp xếp danh sách theo result từ cao xuống thấp.");
    }

    public void removeStudent(int id) {

        boolean isRemoved = this.studentList.removeIf(student -> student.getId() == id);

        if (isRemoved) {
            System.out.println("Đã xóa sinh viên có ID: " + id);
        } else {
            System.out.println("Không tìm thấy sinh viên có ID: " + id);
        }
    }

}