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
 * REST CONTROLLER - WEB SERVICE BACKEND (TRẢ VỀ JSON)
 * Đóng vai trò là Web Service mà thầy sẽ cung cấp cho sinh viên trong phòng thi.
 * Giúp sinh viên chạy và luyện tập gọi API ngay tại nhà.
 * 
 * Môn: Xây dựng website hướng dịch vụ (IUH)
 */
@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "*") // Cho phép gọi API từ mọi nguồn, tránh lỗi CORS
public class FacultyRestController {

    private final FacultyService facultyService;

    public FacultyRestController(FacultyService facultyService) {
        this.facultyService = facultyService;
    }

    // =========================================================================
    // BƯỚC 1: API LẤY DANH SÁCH TẤT CẢ KHOA (ĐỂ ĐỔ VÀO COMBOBOX)
    // =========================================================================
    // GET /api/faculties
    @GetMapping("/faculties")
    public List<Faculty> getAllFaculties() {
        return facultyService.getAllFaculties();
    }

    // GET /api/faculties/{id}
    @GetMapping("/faculties/{id}")
    public ResponseEntity<Faculty> getFacultyById(@PathVariable("id") Long id) {
        return facultyService.getFacultyById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    // =========================================================================
    // BƯỚC 2 & BƯỚC 3: API LẤY DANH SÁCH & TÌM KIẾM SINH VIÊN THEO KHOA
    // =========================================================================
    // GET /api/faculties/{facultyId}/students?keyword=...
    @GetMapping("/faculties/{facultyId}/students")
    public ResponseEntity<List<Student>> getStudentsByFacultyId(
            @PathVariable("facultyId") Long facultyId,
            @RequestParam(name = "keyword", required = false) String keyword) {
        
        if (keyword != null && !keyword.trim().isEmpty()) {
            return ResponseEntity.ok(facultyService.searchStudents(facultyId, keyword));
        }
        return facultyService.getStudentsByFacultyId(facultyId)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    // =========================================================================
    // BƯỚC 3: BỘ CRUD SINH VIÊN (THÊM, SỬA, XÓA QUA WEB SERVICE)
    // =========================================================================

    // 1. THÊM SINH VIÊN MỚI VÀO KHOA
    // POST /api/faculties/{facultyId}/students
    // Request Body (JSON): {"name": "Nguyễn Văn X", "email": "x@iuh.edu.vn"}
    @PostMapping("/faculties/{facultyId}/students")
    public ResponseEntity<Student> addStudent(@PathVariable("facultyId") Long facultyId,
                                              @RequestBody Student student) {
        Optional<Student> created = facultyService.addStudentToFaculty(facultyId, student);
        return created.map(s -> ResponseEntity.status(HttpStatus.CREATED).body(s))
                      .orElse(ResponseEntity.notFound().build());
    }

    // 2. SỬA THÔNG TIN SINH VIÊN TRONG KHOA
    // PUT /api/faculties/{facultyId}/students/{studentId}
    // Request Body (JSON): {"name": "Tên Mới", "email": "emailmoi@iuh.edu.vn"}
    @PutMapping("/faculties/{facultyId}/students/{studentId}")
    public ResponseEntity<Student> updateStudent(@PathVariable("facultyId") Long facultyId,
                                                 @PathVariable("studentId") Long studentId,
                                                 @RequestBody Student updatedStudent) {
        Optional<Student> updated = facultyService.updateStudent(facultyId, studentId, updatedStudent);
        return updated.map(ResponseEntity::ok)
                      .orElse(ResponseEntity.notFound().build());
    }

    // 3. XÓA SINH VIÊN KHỎI KHOA
    // DELETE /api/faculties/{facultyId}/students/{studentId}
    @DeleteMapping("/faculties/{facultyId}/students/{studentId}")
    public ResponseEntity<Void> deleteStudent(@PathVariable("facultyId") Long facultyId,
                                              @PathVariable("studentId") Long studentId) {
        boolean deleted = facultyService.deleteStudentFromFaculty(facultyId, studentId);
        if (deleted) {
            return ResponseEntity.noContent().build(); // 204 No Content
        } else {
            return ResponseEntity.notFound().build();  // 404 Not Found
        }
    }
}
