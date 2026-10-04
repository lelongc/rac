package com.example.demojpa.service;

import com.example.demojpa.entity.Student;
import com.example.demojpa.repository.StudentRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Optional;

@Service
public class StudentService {

    // Tiêm (Inject) cái kho StudentRepository vào Service qua Constructor
    private final StudentRepository studentRepository;

    public StudentService(StudentRepository studentRepository) {
        this.studentRepository = studentRepository;
    }

    // Lấy toàn bộ danh sách sinh viên từ CSDL
    public List<Student> getAllStudents() {
        return studentRepository.findAll();
    }

    // Lấy chi tiết 1 sinh viên theo ID
    public Optional<Student> getStudentById(Long id) {
        return studentRepository.findById(id);
    }

    // Thêm mới hoặc lưu sinh viên
    @Transactional
    public Student saveStudent(Student student) {
        return studentRepository.save(student);
    }

    // Cập nhật sinh viên
    @Transactional
    public Optional<Student> updateStudent(Long id, Student studentData) {
        return studentRepository.findById(id).map(existing -> {
            existing.setName(studentData.getName());
            existing.setEmail(studentData.getEmail());
            existing.setPhone(studentData.getPhone());
            return studentRepository.save(existing);
        });
    }

    // Xóa sinh viên
    @Transactional
    public boolean deleteStudent(Long id) {
        if (studentRepository.existsById(id)) {
            studentRepository.deleteById(id);
            return true;
        }
        return false;
    }

    // Tìm kiếm theo tên
    public List<Student> searchStudents(String keyword) {
        if (keyword != null && !keyword.trim().isEmpty()) {
            return studentRepository.findByNameContainingIgnoreCase(keyword.trim());
        }
        return studentRepository.findAll();
    }
}
