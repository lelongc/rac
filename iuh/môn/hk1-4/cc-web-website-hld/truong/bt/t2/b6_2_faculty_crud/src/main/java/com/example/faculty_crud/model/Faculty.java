package com.example.faculty_crud.model;

import java.util.ArrayList;
import java.util.List;

public class Faculty {
    private Long id;
    private String name;
    private List<Student> students = new ArrayList<>();

    public Faculty() {
    }

    public Faculty(Long id, String name) {
        this.id = id;
        this.name = name;
        this.students = new ArrayList<>();
    }

    public Faculty(Long id, String name, List<Student> students) {
        this.id = id;
        this.name = name;
        this.students = students != null ? new ArrayList<>(students) : new ArrayList<>();
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Student> getStudents() {
        return students;
    }

    public void setStudents(List<Student> students) {
        this.students = students != null ? new ArrayList<>(students) : new ArrayList<>();
    }

    @Override
    public String toString() {
        return "Faculty{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", studentCount=" + (students != null ? students.size() : 0) +
                '}';
    }
}
