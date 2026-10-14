package com.example.demojpa.service;

import com.example.demojpa.entity.Student;
import com.example.demojpa.entity.Subject;
import com.example.demojpa.repository.StudentRepository;
import com.example.demojpa.repository.SubjectRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
public class SubjectService {

    private final SubjectRepository subjectRepository;
    private final StudentRepository studentRepository;

    public SubjectService(SubjectRepository subjectRepository, StudentRepository studentRepository) {
        this.subjectRepository = subjectRepository;
        this.studentRepository = studentRepository;
    }

    public List<Subject> getAllSubjects() {
        return subjectRepository.findAll();
    }

    public Subject getSubjectById(Long id) {
        return subjectRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("Subject not found with ID: " + id));
    }

    public Subject createSubject(Subject subject) {
        return subjectRepository.save(subject);
    }

    public void deleteSubject(Long id) {
        Subject subject = getSubjectById(id);
        for (Student student : subject.getStudents()) {
            student.getSubjects().remove(subject);
        }
        subjectRepository.delete(subject);
    }

    // ======================================================================
    // NGHIỆP VỤ ĐĂNG KÝ MÔN HỌC (QUAN HỆ NHIỀU - NHIỀU):
    // 1 Sinh viên đăng ký 1 Môn học -> lưu vào bảng trung gian student_subject
    // ======================================================================
    @Transactional
    public Subject enrollStudent(Long subjectId, Long studentId) {
        Subject subject = getSubjectById(subjectId);
        Student student = studentRepository.findById(studentId)
                .orElseThrow(() -> new RuntimeException("Student not found with ID: " + studentId));

        student.addSubject(subject);
        studentRepository.save(student);

        return subject;
    }

    @Transactional
    public Subject removeStudentFromSubject(Long subjectId, Long studentId) {
        Subject subject = getSubjectById(subjectId);
        Student student = studentRepository.findById(studentId)
                .orElseThrow(() -> new RuntimeException("Student not found with ID: " + studentId));

        student.removeSubject(subject);
        studentRepository.save(student);

        return subject;
    }
}
