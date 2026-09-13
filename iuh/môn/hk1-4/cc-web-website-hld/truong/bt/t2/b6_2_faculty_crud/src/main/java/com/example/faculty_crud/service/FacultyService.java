package com.example.faculty_crud.service;

import com.example.faculty_crud.model.Faculty;
import com.example.faculty_crud.model.Student;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.concurrent.CopyOnWriteArrayList;
import java.util.concurrent.atomic.AtomicLong;

@Service
public class FacultyService {

    private final List<Faculty> faculties = new CopyOnWriteArrayList<>();
    private final AtomicLong facultyIdGenerator = new AtomicLong(3);
    private final AtomicLong studentIdGenerator = new AtomicLong(301);

    public FacultyService() {
        // Dữ liệu mẫu ban đầu (khớp bài giảng của Thầy: 3 khoa)
        List<Student> itStudents = new ArrayList<>(List.of(
            new Student(101L, "Alice Johnson", "alice@cs.edu"),
            new Student(102L, "Bob Smith", "bob@cs.edu")
        ));

        List<Student> bizStudents = new ArrayList<>(List.of(
            new Student(201L, "Clara Davis", "clara@business.edu"),
            new Student(202L, "Emma Wilson", "emma@business.edu")
        ));

        List<Student> engStudents = new ArrayList<>(List.of(
            new Student(301L, "Daniel Lee", "daniel@eng.edu")
        ));

        faculties.add(new Faculty(1L, "Computer Science", itStudents));
        faculties.add(new Faculty(2L, "Business Administration", bizStudents));
        faculties.add(new Faculty(3L, "Engineering", engStudents));
    }

    // ==========================================
    // 1. CÁC PHƯƠNG THỨC CRUD CHO KHOA (FACULTY)
    // ==========================================

    // Lấy toàn bộ danh sách khoa
    public List<Faculty> getAllFaculties() {
        return faculties;
    }

    // Lấy thông tin khoa theo ID
    public Optional<Faculty> getFacultyById(Long id) {
        return faculties.stream()
                .filter(f -> f.getId().equals(id))
                .findFirst();
    }

    // Tìm kiếm khoa theo tên
    public Optional<Faculty> getFacultyByName(String name) {
        return faculties.stream()
                .filter(f -> f.getName().equalsIgnoreCase(name))
                .findFirst();
    }

    // [THÊM] Thêm khoa mới
    public Faculty addFaculty(Faculty faculty) {
        if (faculty.getId() == null) {
            faculty.setId(facultyIdGenerator.incrementAndGet());
        }
        if (faculty.getStudents() == null) {
            faculty.setStudents(new ArrayList<>());
        }
        faculties.add(faculty);
        return faculty;
    }

    // [SỬA] Cập nhật thông tin khoa
    public Optional<Faculty> updateFaculty(Long id, Faculty updatedFaculty) {
        return getFacultyById(id).map(existingFaculty -> {
            if (updatedFaculty.getName() != null && !updatedFaculty.getName().isBlank()) {
                existingFaculty.setName(updatedFaculty.getName());
            }
            return existingFaculty;
        });
    }

    // [XÓA] Xóa khoa theo ID
    public boolean deleteFaculty(Long id) {
        return faculties.removeIf(f -> f.getId().equals(id));
    }

    // ===============================================
    // 2. CÁC PHƯƠNG THỨC CRUD CHO SINH VIÊN (STUDENT)
    // ===============================================

    // Lấy danh sách sinh viên theo facultyId
    public Optional<List<Student>> getStudentsByFacultyId(Long facultyId) {
        return getFacultyById(facultyId).map(Faculty::getStudents);
    }

    // Lấy thông tin 1 sinh viên cụ thể trong khoa
    public Optional<Student> getStudentById(Long facultyId, Long studentId) {
        return getFacultyById(facultyId).flatMap(faculty ->
                faculty.getStudents().stream()
                        .filter(s -> s.getId().equals(studentId))
                        .findFirst()
        );
    }

    // [THÊM] Thêm sinh viên mới vào khoa
    public Optional<Student> addStudentToFaculty(Long facultyId, Student student) {
        return getFacultyById(facultyId).map(faculty -> {
            if (student.getId() == null) {
                student.setId(studentIdGenerator.incrementAndGet());
            }
            faculty.getStudents().add(student);
            return student;
        });
    }

    // [SỬA] Cập nhật thông tin sinh viên
    public Optional<Student> updateStudent(Long facultyId, Long studentId, Student updatedStudent) {
        return getStudentById(facultyId, studentId).map(existingStudent -> {
            if (updatedStudent.getName() != null && !updatedStudent.getName().isBlank()) {
                existingStudent.setName(updatedStudent.getName());
            }
            if (updatedStudent.getEmail() != null && !updatedStudent.getEmail().isBlank()) {
                existingStudent.setEmail(updatedStudent.getEmail());
            }
            return existingStudent;
        });
    }

    // [XÓA] Xóa sinh viên khỏi khoa
    public boolean deleteStudentFromFaculty(Long facultyId, Long studentId) {
        Optional<Faculty> facultyOpt = getFacultyById(facultyId);
        if (facultyOpt.isPresent()) {
            return facultyOpt.get().getStudents().removeIf(s -> s.getId().equals(studentId));
        }
        return false;
    }
}
