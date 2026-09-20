package com.example.gk.service;

import com.example.gk.model.Faculty;
import com.example.gk.model.Student;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;
import java.util.concurrent.CopyOnWriteArrayList;
import java.util.concurrent.atomic.AtomicLong;

@Service
public class FacultyService {

    // Danh sách lưu trữ trong bộ nhớ RAM
    private final List<Faculty> faculties = new CopyOnWriteArrayList<>();
    private final AtomicLong facultyIdGenerator = new AtomicLong(3);
    private final AtomicLong studentIdGenerator = new AtomicLong(301);

    public FacultyService() {
        // Khởi tạo sẵn 3 Khoa mẫu
        List<Student> itStudents = new ArrayList<>(List.of(
            new Student(101L, "Nguyễn Văn An", "an@iuh.edu.vn"),
            new Student(102L, "Trần Thị Bình", "binh@iuh.edu.vn")
        ));

        List<Student> mechaStudents = new ArrayList<>(List.of(
            new Student(201L, "Lê Hoàng Long", "long@iuh.edu.vn"),
            new Student(202L, "Phạm Quốc Dũng", "dung@iuh.edu.vn")
        ));

        List<Student> bizStudents = new ArrayList<>(List.of(
            new Student(301L, "Đỗ Minh Khang", "khang@iuh.edu.vn")
        ));

        faculties.add(new Faculty(1L, "Công Nghệ Thông Tin", itStudents));
        faculties.add(new Faculty(2L, "Kỹ Thuật Cơ Khí", mechaStudents));
        faculties.add(new Faculty(3L, "Quản Trị Kinh Doanh", bizStudents));
    }

    // ==========================================
    // 1. NGHIỆP VỤ KHOA (FACULTY)
    // ==========================================

    // Lấy toàn bộ danh sách khoa
    public List<Faculty> getAllFaculties() {
        return faculties;
    }

    // Lấy thông tin 1 khoa theo ID
    public Optional<Faculty> getFacultyById(Long id) {
        return faculties.stream()
                .filter(f -> f.getId().equals(id))
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

    // ==========================================
    // 2. NGHIỆP VỤ SINH VIÊN (STUDENT)
    // ==========================================

    // Lấy danh sách sinh viên của 1 khoa (hoặc tìm kiếm theo từ khóa nếu có)
    public Optional<List<Student>> getStudentsByFacultyId(Long facultyId) {
        return getFacultyById(facultyId).map(Faculty::getStudents);
    }

    // [TÌM KIẾM] Tìm sinh viên theo từ khóa (tên hoặc email) trong khoa
    public List<Student> searchStudents(Long facultyId, String keyword) {
        Optional<List<Student>> studentsOpt = getStudentsByFacultyId(facultyId);
        if (studentsOpt.isEmpty()) return List.of();
        if (keyword == null || keyword.trim().isEmpty()) {
            return studentsOpt.get();
        }
        String lower = keyword.trim().toLowerCase();
        return studentsOpt.get().stream()
                .filter(s -> (s.getName() != null && s.getName().toLowerCase().contains(lower)) ||
                             (s.getEmail() != null && s.getEmail().toLowerCase().contains(lower)))
                .toList();
    }

    // Lấy thông tin 1 sinh viên trong khoa
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

    // [SỬA] Cập nhật sinh viên trong khoa
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

    // [SỬA TRỰC TIẾP] Cập nhật sinh viên theo ID (không cần ID khoa)
    public Optional<Student> updateStudent(Long studentId, Student updatedStudent) {
        for (Faculty f : faculties) {
            for (Student s : f.getStudents()) {
                if (s.getId().equals(studentId)) {
                    if (updatedStudent.getName() != null && !updatedStudent.getName().isBlank()) {
                        s.setName(updatedStudent.getName());
                    }
                    if (updatedStudent.getEmail() != null && !updatedStudent.getEmail().isBlank()) {
                        s.setEmail(updatedStudent.getEmail());
                    }
                    return Optional.of(s);
                }
            }
        }
        return Optional.empty();
    }

    // [XÓA TRỰC TIẾP] Xóa sinh viên theo ID (không cần ID khoa)
    public boolean deleteStudent(Long studentId) {
        for (Faculty f : faculties) {
            if (f.getStudents().removeIf(s -> s.getId().equals(studentId))) {
                return true;
            }
        }
        return false;
    }
}
