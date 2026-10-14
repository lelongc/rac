package com.example.demojpa.entity;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import jakarta.persistence.*;
import java.util.HashSet;
import java.util.Objects;
import java.util.Set;

@Entity
@Table(name = "subjects")
public class Subject {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, length = 100)
    private String name; // Tên môn học (Lập trình Java, Kiến trúc phần mềm...)

    @Column(length = 20, unique = true)
    private String code; // Mã môn học (CS101, SE202...)

    private int credits; // Số tín chỉ

    // ======================================================================
    // QUAN HỆ NHIỀU - NHIỀU VỚI STUDENT:
    // mappedBy = "subjects": Student là bên chủ sở hữu bảng trung gian,
    // Subject là bên nghịch đảo (Inverse side)
    // ======================================================================
    @ManyToMany(mappedBy = "subjects", fetch = FetchType.LAZY)
    @JsonIgnoreProperties("subjects") // Chống lặp vô tận JSON
    private Set<Student> students = new HashSet<>();

    public Subject() {
    }

    public Subject(String name, String code, int credits) {
        this.name = name;
        this.code = code;
        this.credits = credits;
    }

    public void addStudent(Student student) {
        this.students.add(student);
        student.getSubjects().add(this);
    }

    public void removeStudent(Student student) {
        this.students.remove(student);
        student.getSubjects().remove(this);
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

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public int getCredits() {
        return credits;
    }

    public void setCredits(int credits) {
        this.credits = credits;
    }

    public Set<Student> getStudents() {
        return students;
    }

    public void setStudents(Set<Student> students) {
        this.students = students;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Subject subject = (Subject) o;
        return Objects.equals(id, subject.id);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id);
    }
}
