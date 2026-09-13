package com.example.demo;


import org.springframework.stereotype.Service;

import model.Faculty;
import model.Student;

import java.util.List;
import java.util.Optional;

@Service
public class FacultyService {

    // In-memory collection storing faculties with their student collections
    private final List<Faculty> faculties = List.of(
        new Faculty(
            1L,
            "Computer Science",
            List.of(
                new Student(101L, "Alice Johnson", "alice@cs.edu"),
                new Student(102L, "Bob Smith", "bob@cs.edu")
            )
        ),
        new Faculty(
            2L,
            "Business Administration",
            List.of(
                new Student(201L, "Clara Davis", "clara@business.edu"),
                new Student(202L, "Emma Wilson", "emma@business.edu")
            )
        ),
        new Faculty(
            3L,
            "Engineering",
            List.of(
                new Student(301L, "Daniel Lee", "daniel@eng.edu")
            )
        )
    );

    public Optional<List<Student>> getStudentsByFacultyId(Long facultyId) {
        return faculties.stream()
            .filter(faculty -> faculty.getId().equals(facultyId))
            .map(Faculty::getStudents)
            .findFirst();
    }

    public Optional<List<Student>> getStudentsByFacultyName(String facultyName) {
        return faculties.stream()
            .filter(faculty -> faculty.getName().equalsIgnoreCase(facultyName))
            .map(Faculty::getStudents)
            .findFirst();
    }
}