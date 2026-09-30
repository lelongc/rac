package com.example.demo.controller;

import com.example.demo.model.Department;
import com.example.demo.service.OrganizationService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/departments")
@CrossOrigin(origins = "*")
public class DepartmentController {

    private final OrganizationService service;

    public DepartmentController(OrganizationService service) {
        this.service = service;
    }

    // Lấy tất cả các phòng ban (dùng để đổ dữ liệu vào Combobox)
    @GetMapping
    public List<Department> getAllDepartments() {
        return service.getAllDepartments();
    }

    // Lấy chi tiết 1 phòng ban kèm danh sách nhân viên
    @GetMapping("/{id}/staffs")
    public ResponseEntity<Department> getDepartmentStaffs(@PathVariable Long id) {
        return service.getDepartmentWithStaffs(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }
}
