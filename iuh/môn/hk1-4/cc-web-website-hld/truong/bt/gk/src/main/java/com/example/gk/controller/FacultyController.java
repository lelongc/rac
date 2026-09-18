package com.example.gk.controller;

import com.example.gk.model.Faculty;
import com.example.gk.model.Student;
import com.example.gk.service.FacultyService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;

@Controller
public class FacultyController {

    private final FacultyService facultyService;

    public FacultyController(FacultyService facultyService) {
        this.facultyService = facultyService;
    }

    // ==========================================
    // 1. CÁC HÀM XỬ LÝ GIAO DIỆN KHOA (FACULTY)
    // ==========================================

    // Hiển thị danh sách tất cả các khoa
    @GetMapping({"/", "/faculties"})
    public String listFaculties(Model model) {
        model.addAttribute("faculties", facultyService.getAllFaculties());
        return "faculty_list"; // Tìm file templates/faculty_list.html
    }

    // Mở trang form thêm khoa mới
    @GetMapping("/faculties/new")
    public String showNewFacultyForm(Model model) {
        model.addAttribute("faculty", new Faculty());
        model.addAttribute("isEdit", false);
        return "faculty_form"; // Tìm file templates/faculty_form.html
    }

    // Mở trang form chỉnh sửa thông tin khoa
    @GetMapping("/faculties/edit/{id}")
    public String showEditFacultyForm(@PathVariable("id") Long id, Model model) {
        Optional<Faculty> facultyOpt = facultyService.getFacultyById(id);
        if (facultyOpt.isPresent()) {
            model.addAttribute("faculty", facultyOpt.get());
            model.addAttribute("isEdit", true);
            return "faculty_form";
        }
        return "redirect:/faculties";
    }

    // Nhận dữ liệu submit từ Form để lưu khoa (Cả Thêm mới và Sửa)
    @PostMapping("/faculties/save")
    public String saveFaculty(@ModelAttribute("faculty") Faculty faculty) {
        if (faculty.getId() == null) {
            facultyService.addFaculty(faculty);
        } else {
            facultyService.updateFaculty(faculty.getId(), faculty);
        }
        return "redirect:/faculties";
    }

    // Xóa một khoa theo ID
    @GetMapping("/faculties/delete/{id}")
    public String deleteFaculty(@PathVariable("id") Long id) {
        facultyService.deleteFaculty(id);
        return "redirect:/faculties";
    }

    // ==========================================
    // 2. CÁC HÀM XỬ LÝ GIAO DIỆN SINH VIÊN (STUDENT)
    // ==========================================

    // Xem danh sách sinh viên của 1 khoa
    @GetMapping("/faculties/{id}/students")
    public String viewFacultyStudents(@PathVariable("id") Long id, Model model) {
        Optional<Faculty> facultyOpt = facultyService.getFacultyById(id);
        if (facultyOpt.isPresent()) {
            model.addAttribute("faculty", facultyOpt.get());
            model.addAttribute("students", facultyOpt.get().getStudents());
            return "faculty_students"; // Tìm file templates/faculty_students.html
        }
        return "redirect:/faculties";
    }

    // Mở trang form thêm sinh viên mới vào khoa
    @GetMapping("/faculties/{facultyId}/students/new")
    public String showNewStudentForm(@PathVariable("facultyId") Long facultyId, Model model) {
        Optional<Faculty> facultyOpt = facultyService.getFacultyById(facultyId);
        if (facultyOpt.isEmpty()) {
            return "redirect:/faculties";
        }
        model.addAttribute("faculty", facultyOpt.get());
        model.addAttribute("student", new Student());
        model.addAttribute("isEdit", false);
        return "student_form"; // Tìm file templates/student_form.html
    }

    // Mở trang form chỉnh sửa sinh viên
    @GetMapping("/faculties/{facultyId}/students/edit/{studentId}")
    public String showEditStudentForm(@PathVariable("facultyId") Long facultyId,
                                      @PathVariable("studentId") Long studentId,
                                      Model model) {
        Optional<Faculty> facultyOpt = facultyService.getFacultyById(facultyId);
        Optional<Student> studentOpt = facultyService.getStudentById(facultyId, studentId);
        if (facultyOpt.isPresent() && studentOpt.isPresent()) {
            model.addAttribute("faculty", facultyOpt.get());
            model.addAttribute("student", studentOpt.get());
            model.addAttribute("isEdit", true);
            return "student_form";
        }
        return "redirect:/faculties/" + facultyId + "/students";
    }

    // Nhận dữ liệu submit từ Form để lưu sinh viên
    @PostMapping("/faculties/{facultyId}/students/save")
    public String saveStudent(@PathVariable("facultyId") Long facultyId,
                              @ModelAttribute("student") Student student) {
        if (student.getId() == null) {
            facultyService.addStudentToFaculty(facultyId, student);
        } else {
            facultyService.updateStudent(facultyId, student.getId(), student);
        }
        return "redirect:/faculties/" + facultyId + "/students";
    }

    // Xóa sinh viên khỏi khoa
    @GetMapping("/faculties/{facultyId}/students/delete/{studentId}")
    public String deleteStudent(@PathVariable("facultyId") Long facultyId,
                                @PathVariable("studentId") Long studentId) {
        facultyService.deleteStudentFromFaculty(facultyId, studentId);
        return "redirect:/faculties/" + facultyId + "/students";
    }
}
