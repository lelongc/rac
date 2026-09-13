package com.example.faculty_crud.controller;

import com.example.faculty_crud.model.Faculty;
import com.example.faculty_crud.model.Student;
import com.example.faculty_crud.service.FacultyService;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;

@Controller
public class FacultyWebController {

    private final FacultyService facultyService;

    public FacultyWebController(FacultyService facultyService) {
        this.facultyService = facultyService;
    }

    // ===============================================
    // 1. GIAO DIỆN WEB CHO KHOA (FACULTY)
    // ===============================================

    // Trang chủ & Danh sách các khoa
    @GetMapping({"/", "/faculties"})
    public String listFaculties(Model model) {
        model.addAttribute("faculties", facultyService.getAllFaculties());
        return "faculty_list";
    }

    // Form thêm khoa mới
    @GetMapping("/faculties/new")
    public String showNewFacultyForm(Model model) {
        model.addAttribute("faculty", new Faculty());
        model.addAttribute("isEdit", false);
        return "faculty_form";
    }

    // Form sửa khoa
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

    // Lưu thông tin khoa (Cả Thêm mới và Sửa)
    @PostMapping("/faculties/save")
    public String saveFaculty(@ModelAttribute("faculty") Faculty faculty) {
        if (faculty.getId() == null) {
            facultyService.addFaculty(faculty);
        } else {
            facultyService.updateFaculty(faculty.getId(), faculty);
        }
        return "redirect:/faculties";
    }

    // Xóa khoa
    @GetMapping("/faculties/delete/{id}")
    public String deleteFaculty(@PathVariable("id") Long id) {
        facultyService.deleteFaculty(id);
        return "redirect:/faculties";
    }

    // ===============================================
    // 2. GIAO DIỆN WEB CHO SINH VIÊN TRONG KHOA
    // ===============================================

    // Xem danh sách sinh viên của một khoa
    @GetMapping("/faculties/{id}/students")
    public String viewFacultyStudents(@PathVariable("id") Long id, Model model) {
        Optional<Faculty> facultyOpt = facultyService.getFacultyById(id);
        if (facultyOpt.isPresent()) {
            model.addAttribute("faculty", facultyOpt.get());
            model.addAttribute("students", facultyOpt.get().getStudents());
            return "faculty_students";
        }
        return "redirect:/faculties";
    }

    // Form thêm sinh viên mới vào khoa
    @GetMapping("/faculties/{facultyId}/students/new")
    public String showNewStudentForm(@PathVariable("facultyId") Long facultyId, Model model) {
        Optional<Faculty> facultyOpt = facultyService.getFacultyById(facultyId);
        if (facultyOpt.isEmpty()) {
            return "redirect:/faculties";
        }
        model.addAttribute("faculty", facultyOpt.get());
        model.addAttribute("student", new Student());
        model.addAttribute("isEdit", false);
        return "student_form";
    }

    // Form sửa sinh viên trong khoa
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

    // Lưu thông tin sinh viên
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
