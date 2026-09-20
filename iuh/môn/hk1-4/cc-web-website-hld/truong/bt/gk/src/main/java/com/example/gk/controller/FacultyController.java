package com.example.gk.controller;

import com.example.gk.model.Faculty;
import com.example.gk.model.Student;
import com.example.gk.service.FacultyService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

/**
 * CONTROLLER REST API (WEB SERVICE)
 * 1 Controller duy nhất phục vụ ứng dụng SPA (Single Page Application).
 * Trả về dữ liệu thô dạng JSON cho Frontend gọi.
 */
@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "*")
public class FacultyController {

    private final FacultyService facultyService;

    public FacultyController(FacultyService facultyService) {
        this.facultyService = facultyService;
    }

    // =========================================================
    // BƯỚC 1: LẤY DANH SÁCH TẤT CẢ KHOA (ĐỔ VÀO COMBOBOX)
    // GET /api/faculties
    // =========================================================
    @GetMapping("/faculties")
    public List<Faculty> getAllFaculties() {
        return facultyService.getAllFaculties();
    }

    @GetMapping("/faculties/{id}")
    public ResponseEntity<Faculty> getFacultyById(@PathVariable Long id) {
        return facultyService.getFacultyById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    // =========================================================
    // BƯỚC 2: LẤY DANH SÁCH SINH VIÊN THEO KHOA (ĐỔ TABLE & TÌM KIẾM)
    // GET /api/faculties/{facultyId}/students?keyword=...
    // =========================================================
    @GetMapping("/faculties/{facultyId}/students")
    public ResponseEntity<List<Student>> getStudents(
            @PathVariable Long facultyId,
            @RequestParam(name = "keyword", required = false) String keyword) {
        if (keyword != null && !keyword.trim().isEmpty()) {
            return ResponseEntity.ok(facultyService.searchStudents(facultyId, keyword));
        }
        return facultyService.getStudentsByFacultyId(facultyId)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    // =========================================================
    // BƯỚC 3: THÊM SINH VIÊN VÀO KHOA (POST)
    // POST /api/faculties/{facultyId}/students
    // =========================================================
    @PostMapping("/faculties/{facultyId}/students")
    public ResponseEntity<Student> addStudent(
            @PathVariable Long facultyId,
            @RequestBody Student student) {
        Optional<Student> created = facultyService.addStudentToFaculty(facultyId, student);
        return created.map(s -> ResponseEntity.status(HttpStatus.CREATED).body(s))
                      .orElse(ResponseEntity.notFound().build());
    }

    // =========================================================
    // BƯỚC 3: SỬA SINH VIÊN TRONG KHOA (PUT)
    // PUT /api/faculties/{facultyId}/students/{studentId}
    // =========================================================
    @PutMapping("/faculties/{facultyId}/students/{studentId}")
    public ResponseEntity<Student> updateStudent(
            @PathVariable Long facultyId,
            @PathVariable Long studentId,
            @RequestBody Student student) {
        Optional<Student> updated = facultyService.updateStudent(facultyId, studentId, student);
        return updated.map(ResponseEntity::ok)
                      .orElse(ResponseEntity.notFound().build());
    }

    // Hỗ trợ endpoint rút gọn: PUT /api/students/{studentId}
    @PutMapping("/students/{studentId}")
    public ResponseEntity<Student> updateStudentDirect(
            @PathVariable Long studentId,
            @RequestBody Student student) {
        Optional<Student> updated = facultyService.updateStudent(studentId, student);
        return updated.map(ResponseEntity::ok)
                      .orElse(ResponseEntity.notFound().build());
    }

    // =========================================================
    // BƯỚC 3: XÓA SINH VIÊN KHỎI KHOA (DELETE)
    // DELETE /api/faculties/{facultyId}/students/{studentId}
    // =========================================================
    @DeleteMapping("/faculties/{facultyId}/students/{studentId}")
    public ResponseEntity<Void> deleteStudent(
            @PathVariable Long facultyId,
            @PathVariable Long studentId) {
        boolean deleted = facultyService.deleteStudentFromFaculty(facultyId, studentId);
        if (deleted) {
            return ResponseEntity.noContent().build();
        }
        return ResponseEntity.notFound().build();
    }

    // Hỗ trợ endpoint rút gọn: DELETE /api/students/{studentId}
    @DeleteMapping("/students/{studentId}")
    public ResponseEntity<Void> deleteStudentDirect(@PathVariable Long studentId) {
        boolean deleted = facultyService.deleteStudent(studentId);
        if (deleted) {
            return ResponseEntity.noContent().build();
        }
        return ResponseEntity.notFound().build();
    }
}
