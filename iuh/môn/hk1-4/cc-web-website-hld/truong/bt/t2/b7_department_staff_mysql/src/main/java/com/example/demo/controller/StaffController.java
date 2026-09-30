package com.example.demo.controller;

import com.example.demo.model.Staff;
import com.example.demo.service.OrganizationService;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/staffs")
@CrossOrigin(origins = "*")
public class StaffController {

    private final OrganizationService service;

    public StaffController(OrganizationService service) {
        this.service = service;
    }

    // Lấy danh sách nhân viên (có hỗ trợ tìm kiếm theo từ khóa và lọc theo phòng ban)
    @GetMapping
    public List<Staff> getStaffs(
            @RequestParam(required = false) String keyword,
            @RequestParam(required = false) Long departmentId) {
        if ((keyword != null && !keyword.trim().isEmpty()) || (departmentId != null && departmentId > 0)) {
            return service.searchStaff(keyword, departmentId);
        }
        return service.getAllStaff();
    }

    // Lấy thông tin 1 nhân viên theo ID
    @GetMapping("/{id}")
    public ResponseEntity<Staff> getStaffById(@PathVariable Long id) {
        return service.getStaffById(id)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    // THÊM MỚI NHÂN VIÊN (CREATE)
    @PostMapping
    public ResponseEntity<Staff> createStaff(@RequestBody Staff staff) {
        return service.createStaff(staff)
                .map(created -> ResponseEntity.status(HttpStatus.CREATED).body(created))
                .orElse(ResponseEntity.badRequest().build());
    }

    // CẬP NHẬT NHÂN VIÊN (UPDATE)
    @PutMapping("/{id}")
    public ResponseEntity<Staff> updateStaff(@PathVariable Long id, @RequestBody Staff staff) {
        return service.updateStaff(id, staff)
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    // XÓA NHÂN VIÊN (DELETE)
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteStaff(@PathVariable Long id) {
        if (service.deleteStaff(id)) {
            return ResponseEntity.noContent().build();
        }
        return ResponseEntity.notFound().build();
    }
}
