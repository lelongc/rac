package com.example.gk.controller;

import com.example.gk.model.Faculty;
import com.example.gk.model.Student;
import com.example.gk.service.FacultyService;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;
import java.util.List;
import java.util.Optional;

@RestController
@CrossOrigin(origins = "*")
public class FacultyController {

    private final FacultyService facultyService;

    public FacultyController(FacultyService facultyService) {
        this.facultyService = facultyService;
    }

    // Khi người dùng mở trên trình duyệt các đường dẫn như /faculties, /faculty... -> Tự động chuyển về trang giao diện chính (/)
    @GetMapping(value = {"/faculties", "/faculty", "/students", "/student"}, produces = MediaType.TEXT_HTML_VALUE)
    public void redirectToHome(HttpServletResponse response) throws IOException {
        response.sendRedirect("/");
    }

    // 1. Lấy danh sách tất cả khoa (hỗ trợ cả /api/faculties và /faculties)
    @GetMapping(value = {"/api/faculties", "/faculties"}, produces = MediaType.APPLICATION_JSON_VALUE)
    public List<Faculty> getAllFaculties() {
        return facultyService.getAllFaculties();
    }

    @GetMapping(value = {"/api/faculties/{id}", "/faculties/{id}"}, produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<Faculty> getFacultyById(@PathVariable("id") Long id) {
        return facultyService.getFacultyById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    // 2. Lấy danh sách sinh viên theo khoa (hỗ trợ tìm kiếm theo từ khóa)
    @GetMapping(value = {"/api/faculties/{facultyId}/students", "/faculties/{facultyId}/students"}, produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<List<Student>> getStudents(
            @PathVariable("facultyId") Long facultyId,
            @RequestParam(name = "keyword", required = false) String keyword) {
        if (keyword != null && !keyword.trim().isEmpty()) {
            return ResponseEntity.ok(facultyService.searchStudents(facultyId, keyword));
        }
        return facultyService.getStudentsByFacultyId(facultyId)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    // 3. Thêm sinh viên vào khoa
    @PostMapping(value = {"/api/faculties/{facultyId}/students", "/faculties/{facultyId}/students"})
    public ResponseEntity<Student> addStudent(
            @PathVariable("facultyId") Long facultyId,
            @RequestBody Student student) {
        Optional<Student> created = facultyService.addStudentToFaculty(facultyId, student);
        return created.map(s -> ResponseEntity.status(HttpStatus.CREATED).body(s))
                      .orElse(ResponseEntity.notFound().build());
    }

    // 4. Sửa thông tin sinh viên
    @PutMapping(value = {"/api/faculties/{facultyId}/students/{studentId}", "/faculties/{facultyId}/students/{studentId}"})
    public ResponseEntity<Student> updateStudent(
            @PathVariable("facultyId") Long facultyId,
            @PathVariable("studentId") Long studentId,
            @RequestBody Student student) {
        Optional<Student> updated = facultyService.updateStudent(facultyId, studentId, student);
        return updated.map(ResponseEntity::ok)
                      .orElse(ResponseEntity.notFound().build());
    }

    @PutMapping(value = {"/api/students/{studentId}", "/students/{studentId}"})
    public ResponseEntity<Student> updateStudentDirect(
            @PathVariable("studentId") Long studentId,
            @RequestBody Student student) {
        Optional<Student> updated = facultyService.updateStudent(studentId, student);
        return updated.map(ResponseEntity::ok)
                      .orElse(ResponseEntity.notFound().build());
    }

    // 5. Xóa sinh viên
    @DeleteMapping(value = {"/api/faculties/{facultyId}/students/{studentId}", "/faculties/{facultyId}/students/{studentId}"})
    public ResponseEntity<Void> deleteStudent(
            @PathVariable("facultyId") Long facultyId,
            @PathVariable("studentId") Long studentId) {
        boolean deleted = facultyService.deleteStudentFromFaculty(facultyId, studentId);
        if (deleted) {
            return ResponseEntity.noContent().build();
        }
        return ResponseEntity.notFound().build();
    }

    @DeleteMapping(value = {"/api/students/{studentId}", "/students/{studentId}"})
    public ResponseEntity<Void> deleteStudentDirect(@PathVariable("studentId") Long studentId) {
        boolean deleted = facultyService.deleteStudent(studentId);
        if (deleted) {
            return ResponseEntity.noContent().build();
        }
        return ResponseEntity.notFound().build();
    }
}
