package com.example.demojpa.controller;

import com.example.demojpa.entity.Student;
import com.example.demojpa.service.StudentService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

@Controller
@RequestMapping("/students")
public class StudentViewController {

    private final StudentService studentService;

    public StudentViewController(StudentService studentService) {
        this.studentService = studentService;
    }

    // Hiển thị danh sách sinh viên qua Thymeleaf Template (hỗ trợ tìm kiếm theo từ khóa)
    @GetMapping
    public String viewStudents(@RequestParam(required = false) String keyword, Model model) {
        model.addAttribute("students", studentService.searchStudents(keyword));
        model.addAttribute("keyword", keyword != null ? keyword : "");
        model.addAttribute("newStudent", new Student());
        return "students";
    }

    // Thêm mới sinh viên qua Form Thymeleaf
    @PostMapping("/add")
    public String addStudent(@ModelAttribute("newStudent") Student student) {
        studentService.saveStudent(student);
        return "redirect:/students";
    }

    // Cập nhật sinh viên qua Form Thymeleaf
    @PostMapping("/update/{id}")
    public String updateStudent(@PathVariable Long id, @ModelAttribute Student student) {
        studentService.updateStudent(id, student);
        return "redirect:/students";
    }

    // Xóa sinh viên qua Thymeleaf Link/Form
    @GetMapping("/delete/{id}")
    public String deleteStudent(@PathVariable Long id) {
        studentService.deleteStudent(id);
        return "redirect:/students";
    }
}
