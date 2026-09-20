package com.example.gk.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

/**
 * WEB CONTROLLER - BÀI THI GIỮA KỲ (IUH)
 * Môn: Xây dựng website hướng dịch vụ
 * 
 * Chỉ cần duy nhất 1 route trả về giao diện Single Page (SPA).
 * Toàn bộ tương tác dữ liệu (Combobox, Table, Thêm, Sửa, Xóa, Tìm kiếm)
 * đều được thực hiện qua Web Service REST API bằng JavaScript.
 */
@Controller
public class FacultyController {

    @GetMapping({"/", "/index", "/spa"})
    public String index() {
        return "index"; // Trả về templates/index.html
    }
}
