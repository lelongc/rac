package com.example.demojpa.entity;

import com.fasterxml.jackson.annotation.JsonBackReference;
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import jakarta.persistence.*;
import java.util.HashSet;
import java.util.Objects;
import java.util.Set;

@Entity
@Table(name = "students")
public class Student {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, length = 100)
    private String name;

    @Column(nullable = false, unique = true, length = 100)
    private String email;

    private int age;

    // ======================================================================
    // 1. QUAN HỆ NHIỀU - 1 VỚI KHOA (Faculty):
    // Sinh viên giữ khóa ngoại faculty_id
    // ======================================================================
    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "faculty_id")
    @JsonBackReference
    private Faculty faculty;

    // ======================================================================
    // 2. QUAN HỆ NHIỀU - NHIỀU VỚI MÔN HỌC (Subject):
    // - 1 Sinh viên có Nhiều Môn học, 1 Môn học có Nhiều Sinh viên học.
    // - Student là bên chủ sở hữu định nghĩa @JoinTable.
    // - Bảng trung gian sinh ra trong MySQL là: "student_subject"
    // ======================================================================
    @ManyToMany(fetch = FetchType.LAZY)
    @JoinTable(
        name = "student_subject",
        joinColumns = @JoinColumn(name = "student_id"),
        inverseJoinColumns = @JoinColumn(name = "subject_id")
    )
    @JsonIgnoreProperties("students") // Chặn vòng lặp vô tận JSON
    private Set<Subject> subjects = new HashSet<>();

    public Student() {
    }

    public Student(String name, String email, int age) {
        this.name = name;
        this.email = email;
        this.age = age;
    }

    // Tiện ích đồng bộ quan hệ 2 chiều
    public void addSubject(Subject subject) {
        this.subjects.add(subject);
        subject.getStudents().add(this);
    }

    public void removeSubject(Subject subject) {
        this.subjects.remove(subject);
        subject.getStudents().remove(this);
    }

    // Getters and Setters
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

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public Faculty getFaculty() {
        return faculty;
    }

    public void setFaculty(Faculty faculty) {
        this.faculty = faculty;
    }

    public Set<Subject> getSubjects() {
        return subjects;
    }

    public void setSubjects(Set<Subject> subjects) {
        this.subjects = subjects;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Student student = (Student) o;
        return Objects.equals(id, student.id);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id);
    }
}