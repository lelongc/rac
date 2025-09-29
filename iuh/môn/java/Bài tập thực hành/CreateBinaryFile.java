
import java.io.*;
import java.util.LinkedList;

public class CreateBinaryFile {
    public static void main(String[] args) {
        LinkedList<Student> students = new LinkedList<>();
        
        // Tạo dữ liệu mẫu
        Student s1 = new Student("SV001", "Nguyen Van A");
        s1.setStudent_result(8.5);
        students.add(s1);
        
        Student s2 = new Student("SV002", "Tran Thi B");
        s2.setStudent_result(7.2);
        students.add(s2);
        
        Student s3 = new Student("SV003", "Le Van C");
        s3.setStudent_result(6.0);
        students.add(s3);
        
        Student s4 = new Student("SV004", "Pham Thi D");
        s4.setStudent_result(4.5);
        students.add(s4);
        
        Student s5 = new Student("SV005", "Hoang Van E");
        s5.setStudent_result(9.0);
        students.add(s5);
        
        // Lưu ra file binary
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream("students.dat"))) {
            oos.writeObject(students);
            System.out.println("Đã tạo file binary students.dat thành công!");
            System.out.println("Số lượng sinh viên: " + students.size());
            
            // Hiển thị dữ liệu đã tạo
            System.out.println("\n=== DỮ LIỆU ĐÃ TẠO ===");
            System.out.printf("%-10s %-20s %-10s %-10s\n", "ID", "Name", "Result", "Rank");
            System.out.println("-".repeat(60));
            for (Student s : students) {
                System.out.println(s);
            }
            
        } catch (IOException e) {
            System.out.println("Lỗi tạo file: " + e.getMessage());
        }
    }
}