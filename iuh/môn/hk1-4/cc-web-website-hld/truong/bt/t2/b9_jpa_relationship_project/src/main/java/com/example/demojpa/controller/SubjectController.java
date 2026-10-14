package com.example.demojpa.controller;

import com.example.demojpa.entity.Subject;
import com.example.demojpa.service.SubjectService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/subjects")
public class SubjectController {

    private final SubjectService subjectService;

    public SubjectController(SubjectService subjectService) {
        this.subjectService = subjectService;
    }

    @GetMapping
    public List<Subject> getAll() {
        return subjectService.getAllSubjects();
    }

    @GetMapping("/{id}")
    public ResponseEntity<Subject> getById(@PathVariable Long id) {
        return ResponseEntity.ok(subjectService.getSubjectById(id));
    }

    @PostMapping
    public ResponseEntity<Subject> create(@RequestBody Subject subject) {
        return new ResponseEntity<>(subjectService.createSubject(subject), HttpStatus.CREATED);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> delete(@PathVariable Long id) {
        subjectService.deleteSubject(id);
        return ResponseEntity.noContent().build();
    }

    // ======================================================================
    // API ĐĂNG KÝ MÔN HỌC (QUAN HỆ NHIỀU - NHIỀU):
    // POST /api/subjects/1/students/2 (Đăng ký sinh viên 2 vào môn học 1)
    // ======================================================================
    @PostMapping("/{subjectId}/students/{studentId}")
    public ResponseEntity<Subject> enrollStudent(
            @PathVariable Long subjectId,
            @PathVariable Long studentId) {
        return ResponseEntity.ok(subjectService.enrollStudent(subjectId, studentId));
    }

    // API HỦY ĐĂNG KÝ MÔN HỌC:
    @DeleteMapping("/{subjectId}/students/{studentId}")
    public ResponseEntity<Subject> removeStudent(
            @PathVariable Long subjectId,
            @PathVariable Long studentId) {
        return ResponseEntity.ok(subjectService.removeStudentFromSubject(subjectId, studentId));
    }
}
