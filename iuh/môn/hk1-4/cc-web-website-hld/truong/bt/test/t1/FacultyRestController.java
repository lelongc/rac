package com.example.demo;




import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import model.Student;

import java.util.List;

@RestController
@RequestMapping("/api/faculties")
public class FacultyRestController {

    private final FacultyService facultyService;

    public FacultyRestController(FacultyService facultyService) {
        this.facultyService = facultyService;
    }

    // GET /api/faculties/1/students
    @GetMapping("/{facultyId}/students")
    public ResponseEntity<List<Student>> getStudentsByFacultyId(@PathVariable Long facultyId) {
        return facultyService.getStudentsByFacultyId(facultyId)
            .map(ResponseEntity::ok)
            .orElseGet(() -> ResponseEntity.notFound().build());
    }

    // GET /api/faculties/by-name/Engineering/students
    @GetMapping("/by-name/{name}/students")
    public ResponseEntity<List<Student>> getStudentsByFacultyName(@PathVariable String name) {
        return facultyService.getStudentsByFacultyName(name)
            .map(ResponseEntity::ok)
            .orElseGet(() -> ResponseEntity.notFound().build());
    }
}