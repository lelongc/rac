package com.example.studentservice;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping({"/students"})
public class StudentController {
    private List<Student> students = new ArrayList<>();

    public StudentController() {
        students.add(new Student(1, "An Nguyen", "an@example.com"));
        students.add(new Student(2, "Binh Tran", "binh@example.com"));
    }

    @GetMapping
    public List<Student> getAllStudents() {
        return students;
    }

    @GetMapping("/{id}")
    public Student getStudentById(@PathVariable int id) {
        return students.stream()
                .filter(s -> s.getId() == id)
                .findFirst()
                .orElse(null);
    }

    @PostMapping
    public Student addStudent(@RequestBody Student newStudent) {
        students.add(newStudent);
        return newStudent;
    }

    @DeleteMapping("/{id}")
    public String deleteStudent(@PathVariable int id) {
        students.removeIf(s -> s.getId() == id);
        return "Deleted student with ID: " + id;
    }
}
