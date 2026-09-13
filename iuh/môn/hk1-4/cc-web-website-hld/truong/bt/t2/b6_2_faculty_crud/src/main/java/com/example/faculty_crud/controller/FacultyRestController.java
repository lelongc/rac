package com.example.faculty_crud.controller;

import com.example.faculty_crud.model.Faculty;
import com.example.faculty_crud.model.Student;
import com.example.faculty_crud.service.FacultyService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/faculties")
public class FacultyRestController {

    private final FacultyService facultyService;

    public FacultyRestController(FacultyService facultyService) {
        this.facultyService = facultyService;
    }

    // ===============================================
    // 1. CÁC API CRUD CHO KHOA (FACULTY)
    // ===============================================

    // [GET] /api/faculties - Lấy toàn bộ danh sách các khoa
    @GetMapping
    public ResponseEntity<List<Faculty>> getAllFaculties() {
        return ResponseEntity.ok(facultyService.getAllFaculties());
    }

    // [GET] /api/faculties/{id} - Lấy chi tiết một khoa theo ID
    @GetMapping("/{id}")
    public ResponseEntity<Faculty> getFacultyById(@PathVariable("id") Long id) {
        return facultyService.getFacultyById(id)
                .map(ResponseEntity::ok)
                .orElseGet(() -> ResponseEntity.notFound().build());
    }

    // [GET] /api/faculties/by-name/{name} - Tìm khoa theo tên
    @GetMapping("/by-name/{name}")
    public ResponseEntity<Faculty> getFacultyByName(@PathVariable("name") String name) {
        return facultyService.getFacultyByName(name)
                .map(ResponseEntity::ok)
                .orElseGet(() -> ResponseEntity.notFound().build());
    }

    // [POST] /api/faculties - [THÊM] Tạo mới một khoa
    @PostMapping
    public ResponseEntity<Faculty> createFaculty(@RequestBody Faculty faculty) {
        Faculty created = facultyService.addFaculty(faculty);
        return ResponseEntity.status(HttpStatus.CREATED).body(created);
    }

    // [PUT] /api/faculties/{id} - [SỬA] Cập nhật thông tin khoa
    @PutMapping("/{id}")
    public ResponseEntity<Faculty> updateFaculty(@PathVariable("id") Long id, @RequestBody Faculty updatedFaculty) {
        return facultyService.updateFaculty(id, updatedFaculty)
                .map(ResponseEntity::ok)
                .orElseGet(() -> ResponseEntity.notFound().build());
    }

    // [DELETE] /api/faculties/{id} - [XÓA] Xóa một khoa theo ID
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteFaculty(@PathVariable("id") Long id) {
        boolean deleted = facultyService.deleteFaculty(id);
        if (deleted) {
            return ResponseEntity.noContent().build();
        }
        return ResponseEntity.notFound().build();
    }

    // ===============================================
    // 2. CÁC API CRUD CHO SINH VIÊN TRONG KHOA
    // ===============================================

    // [GET] /api/faculties/{facultyId}/students - Lấy danh sách sinh viên của khoa
    @GetMapping("/{facultyId}/students")
    public ResponseEntity<List<Student>> getStudentsByFacultyId(@PathVariable("facultyId") Long facultyId) {
        return facultyService.getStudentsByFacultyId(facultyId)
                .map(ResponseEntity::ok)
                .orElseGet(() -> ResponseEntity.notFound().build());
    }

    // [GET] /api/faculties/{facultyId}/students/{studentId} - Lấy chi tiết 1 sinh viên
    @GetMapping("/{facultyId}/students/{studentId}")
    public ResponseEntity<Student> getStudentById(@PathVariable("facultyId") Long facultyId,
                                                  @PathVariable("studentId") Long studentId) {
        return facultyService.getStudentById(facultyId, studentId)
                .map(ResponseEntity::ok)
                .orElseGet(() -> ResponseEntity.notFound().build());
    }

    // [POST] /api/faculties/{facultyId}/students - [THÊM] Thêm sinh viên vào khoa
    @PostMapping("/{facultyId}/students")
    public ResponseEntity<Student> addStudentToFaculty(@PathVariable("facultyId") Long facultyId,
                                                       @RequestBody Student student) {
        return facultyService.addStudentToFaculty(facultyId, student)
                .map(createdStudent -> ResponseEntity.status(HttpStatus.CREATED).body(createdStudent))
                .orElseGet(() -> ResponseEntity.notFound().build());
    }

    // [PUT] /api/faculties/{facultyId}/students/{studentId} - [SỬA] Cập nhật sinh viên
    @PutMapping("/{facultyId}/students/{studentId}")
    public ResponseEntity<Student> updateStudent(@PathVariable("facultyId") Long facultyId,
                                                 @PathVariable("studentId") Long studentId,
                                                 @RequestBody Student updatedStudent) {
        return facultyService.updateStudent(facultyId, studentId, updatedStudent)
                .map(ResponseEntity::ok)
                .orElseGet(() -> ResponseEntity.notFound().build());
    }

    // [DELETE] /api/faculties/{facultyId}/students/{studentId} - [XÓA] Xóa sinh viên
    @DeleteMapping("/{facultyId}/students/{studentId}")
    public ResponseEntity<Void> deleteStudent(@PathVariable("facultyId") Long facultyId,
                                              @PathVariable("studentId") Long studentId) {
        boolean deleted = facultyService.deleteStudentFromFaculty(facultyId, studentId);
        if (deleted) {
            return ResponseEntity.noContent().build();
        }
        return ResponseEntity.notFound().build();
    }
}
