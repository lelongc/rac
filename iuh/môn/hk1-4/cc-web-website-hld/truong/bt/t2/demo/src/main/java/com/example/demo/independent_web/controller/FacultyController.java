package com.example.demo.independent_web.controller;

import com.example.demo.independent_web.model.Faculty;
import com.example.demo.independent_web.model.Student;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

@Controller
@RequestMapping("/faculties")
public class FacultyController {

    private List<Faculty> facultyList = new ArrayList<>();

    public FacultyController() {
        // Khoa Công nghệ Thông tin (Computer Science)
        List<Student> csStudents = Arrays.asList(
            new Student(1L, "Nguyễn Văn An", "an.nguyen@example.com"),
            new Student(2L, "Trần Thị Bình", "binh.tran@example.com"),
            new Student(3L, "Lê Hoàng Long", "long.le@example.com")
        );

        // Khoa Cơ khí - Kỹ thuật (Engineering)
        List<Student> engStudents = Arrays.asList(
            new Student(4L, "Phạm Quốc Dũng", "dung.pham@example.com"),
            new Student(5L, "Đỗ Minh Khang", "khang.do@example.com")
        );

        facultyList.add(new Faculty(1L, "Khoa Công Nghệ Thông Tin", csStudents));
        facultyList.add(new Faculty(2L, "Khoa Kỹ Thuật Cơ Khí", engStudents));
    }

    @GetMapping
    public String listFaculties(Model model) {
        model.addAttribute("faculties", facultyList);
        return "faculty_list";
    }

    @GetMapping("/{id}/students")
    public String viewFacultyStudents(@PathVariable("id") Long id, Model model) {
        Faculty selectedFaculty = null;

        for (Faculty faculty : facultyList) {
            if (faculty.getId().equals(id)) {
                selectedFaculty = faculty;
                break;
            }
        }

        if (selectedFaculty != null) {
            model.addAttribute("faculty", selectedFaculty);
            model.addAttribute("students", selectedFaculty.getStudents());
        } else {
            return "redirect:/faculties";
        }
        
        return "faculty_students";
    }
}
