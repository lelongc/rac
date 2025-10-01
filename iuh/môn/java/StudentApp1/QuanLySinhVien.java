package iuh.môn.java.StudentApp1;

import java.io.*;
import java.util.*;

public class QuanLySinhVien {
    private Student root; 
    
    public QuanLySinhVien() {
        this.root = null;
    }
    
    public Student getRoot() {
        return root;
    }
    
    // Them sinh vien moi
    public void themSinhVien(int id, String ten, double diem) {
        root = themSinhVienRecursive(root, id, ten, diem);
    }
    
    private Student themSinhVienRecursive(Student current, int id, String ten, double diem) {
        if (current == null) {
            System.out.println("Đã thêm sinh viên có ID: " + id);
            return new Student(id, ten, diem);
        }
        
        if (id < current.getStudentId()) {
            current.setPrev(themSinhVienRecursive(current.getPrev(), id, ten, diem));
        } else if (id > current.getStudentId()) {
            current.setNext(themSinhVienRecursive(current.getNext(), id, ten, diem));
        } else {
            System.out.println("Lỗi: ID đã tồn tại!");
            return current;
        }
        
        return current;
    }
    
    // Xoa sinh vien theo ID
    public void xoaSinhVien(int id) {
        root = xoaSinhVienRecursive(root, id);
    }
    
    private Student xoaSinhVienRecursive(Student current, int id) {
        if (current == null) {
            System.out.println("Không tìm thấy sinh viên có ID: " + id);
            return current;
        }
        
        if (id < current.getStudentId()) {
            current.setPrev(xoaSinhVienRecursive(current.getPrev(), id));
        } else if (id > current.getStudentId()) {
            current.setNext(xoaSinhVienRecursive(current.getNext(), id));
        } else {
            System.out.println("Đã xóa sinh viên có ID: " + id);
            
            // Xóa node có 0 hoặc 1 con
            if (current.getPrev() == null) {
                return current.getNext();
            } else if (current.getNext() == null) {
                return current.getPrev();
            }
            
            // Xóa node có 2 con (Tìm node nhỏ nhất bên cây con phải)
            Student temp = timMinNode(current.getNext());
            
            // Sao chép nội dung
            current.setStudentId(temp.getStudentId());
            current.setStudentName(temp.getStudentName());
            current.setStudentResult(temp.getStudentResult());
            
            // Xóa node successor đã sao chép
            current.setNext(xoaSinhVienRecursive(current.getNext(), temp.getStudentId()));
        }
        
        return current;
    }
    
    private Student timMinNode(Student node) {
        Student current = node;
        while (current.getPrev() != null) {
            current = current.getPrev();
        }
        return current;
    }
    
    // Hien thi danh sach sinh vien theo ID (In-Order)
    public void hienThiDanhSach() {
        System.out.println("\n=== DANH SÁCH SINH VIÊN (Theo ID) ===");
        if (root == null) {
            System.out.println("Danh sách trống!");
            return;
        }
        hienThiInOrder(root);
        System.out.println("=====================================");
    }
    
    private void hienThiInOrder(Student node) {
        if (node != null) {
            hienThiInOrder(node.getPrev());
            System.out.println(node);
            hienThiInOrder(node.getNext());
        }
    }
    
    // Helper: Thu thập tất cả sinh viên vào một danh sách List
    private void collectStudents(Student node, List<Student> list) {
        if (node == null) return;
        collectStudents(node.getPrev(), list);
        list.add(node);
        collectStudents(node.getNext(), list);
    }
    
    // Sap xep theo ten (hien thi)
    public void sapXepTheoTen() {
        System.out.println("\n=== DANH SÁCH SẮP XẾP THEO TÊN ===");
        if (root == null) {
            System.out.println("Danh sách trống!");
            return;
        }
        List<Student> list = new ArrayList<>();
        collectStudents(root, list);
        Collections.sort(list, (a, b) -> 
            a.getStudentName().toLowerCase().compareTo(b.getStudentName().toLowerCase())
        );
        for (Student s : list) {
            System.out.println(s);
        }
        System.out.println("===============================");
    }

    // Sap xep theo diem (cao den thap)
    public void sapXepTheoDiem() {
        System.out.println("\n=== DANH SÁCH SẮP XẾP THEO ĐIỂM (CAO ĐẾN THẤP) ===");
        if (root == null) {
            System.out.println("Danh sách trống!");
            return;
        }
        List<Student> list = new ArrayList<>();
        collectStudents(root, list);
        Collections.sort(list, (a, b) -> 
            Double.compare(b.getStudentResult(), a.getStudentResult())
        );
        for (Student s : list) {
            System.out.println(s);
        }
        System.out.println("================================================");
    }
    
    // --- Các chức năng IO File ---

    public void saveToFile(String filename) {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(filename))) {
            oos.writeObject(this.root);
            System.out.println("=> Đã lưu cây vào file '" + filename + "' thành công.");
        } catch (IOException e) {
            System.err.println("Lỗi khi lưu file: " + e.getMessage());
        }
    }

    public void loadFromFile(String filename) {
        File file = new File(filename);
        if (!file.exists()) {
            System.err.println("File '" + filename + "' không tồn tại!");
            return;
        }
        
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(file))) {
            this.root = (Student) ois.readObject();
            System.out.println("=> Đã đọc cây từ file '" + filename + "' thành công.");
        } catch (IOException e) {
            System.err.println("Lỗi khi đọc file: " + e.getMessage());
        } catch (ClassNotFoundException e) {
            System.err.println("Lỗi định dạng file: " + e.getMessage());
        }
    }
}