package com.example.demo.controller;

import com.example.demo.model.Student;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.ArrayList;
import java.util.List;

@Controller
public class WebController {

    @GetMapping("/")
    public String index(Model model) {
        // 1. Thong tin tong quan de tai
        model.addAttribute("projectTitle", "BÀI TẬP LỚN: XÂY DỰNG BLOG WEBSITE");
        model.addAttribute("university", "ĐẠI HỌC CÔNG NGHIỆP TP. HỒ CHÍ MINH (IUH)");
        model.addAttribute("subject", "Công nghệ web và website hướng dữ liệu");
        model.addAttribute("description", "Nền tảng diễn đàn trực tuyến chia sẻ bài viết - Xây dựng trên nền tảng Spring Boot & Thymeleaf");

        // 2. Danh sach 3 sinh vien thuc hien
        List<Student> students = new ArrayList<>();
        students.add(new Student("Hoàng Đại Dương", "24743991", "D"));
        students.add(new Student("Nguyễn Trung Dũng", "24000905", "D"));
        students.add(new Student("Lê Thành Long", "23630851", "L"));
        model.addAttribute("students", students);

        // 3. Danh sach cong nghe
        List<String> techStack = List.of(
            "☕ Java 21",
            "🌱 Spring Boot 3.5.x",
            "🗄️ Spring Data JPA (Hibernate)",
            "🐬 MySQL 8.0",
            "🔒 Spring Security 6 & JWT",
            "☁️ Cloudinary API",
            "🍃 Thymeleaf Template Engine",
            "🅱️ Bootstrap 5 CSS Framework",
            "⚡ MapStruct & Lombok"
        );
        model.addAttribute("techStack", techStack);

        return "index"; // Render template index.html trong src/main/resources/templates/
    }
}
