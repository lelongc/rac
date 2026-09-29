package com.example.student.controller;

import com.example.student.model.Student;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import java.util.concurrent.CopyOnWriteArrayList;
import java.util.concurrent.atomic.AtomicLong;

@RestController
@RequestMapping({"/students", "/api/students"})
public class StudentController {

    private final List<Student> students = new CopyOnWriteArrayList<>();
    private final AtomicLong idGenerator = new AtomicLong(1);

    public StudentController() {
        students.add(new Student(idGenerator.getAndIncrement(), "Nguyen Van An", 20));
        students.add(new Student(idGenerator.getAndIncrement(), "Tran Thi Binh", 21));
        students.add(new Student(idGenerator.getAndIncrement(), "Le Van Cuong", 22));
    }

    @GetMapping
    public List<Student> getAllStudents() {
        return students;
    }

    @GetMapping("/{id}")
    public Student getStudentById(@PathVariable Long id) {
        return students.stream()
                .filter(student -> student.getId().equals(id))
                .findFirst()
                .orElse(null);
    }

    @PostMapping
    public Student addStudent(@RequestBody Student student) {
        if (student.getId() == null) {
            student.setId(idGenerator.getAndIncrement());
        } else if (student.getId() >= idGenerator.get()) {
            idGenerator.set(student.getId() + 1);
        }
        students.add(student);
        return student;
    }
}
