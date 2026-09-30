package com.example.demo.service;

import com.example.demo.model.Department;
import com.example.demo.model.Staff;
import com.example.demo.repository.DepartmentRepository;
import com.example.demo.repository.StaffRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Optional;

@Service
public class OrganizationService {

    private final DepartmentRepository departmentRepository;
    private final StaffRepository staffRepository;

    public OrganizationService(DepartmentRepository departmentRepository, StaffRepository staffRepository) {
        this.departmentRepository = departmentRepository;
        this.staffRepository = staffRepository;
    }


    public List<Department> getAllDepartments() {
        return departmentRepository.findAll();
    }

    public Optional<Department> getDepartmentById(Long departmentId) {
        return departmentRepository.findById(departmentId);
    }

    @Transactional(readOnly = true)
    public Optional<Department> getDepartmentWithStaffs(Long departmentId) {
        return departmentRepository.findById(departmentId);
    }

    public List<Staff> getAllStaff() {
        return staffRepository.findAll();
    }

    public Optional<Staff> getStaffById(Long staffId) {
        return staffRepository.findById(staffId);
    }

    public List<Staff> getStaffByDepartment(Long departmentId) {
        return staffRepository.findByDepartmentId(departmentId);
    }
    public List<Staff> searchStaff(String keyword, Long departmentId) {
        boolean hasKeyword = keyword != null && !keyword.trim().isEmpty();
        boolean hasDept = departmentId != null && departmentId > 0;

        if (hasKeyword && hasDept) {
            return staffRepository.findByDepartmentIdAndNameContainingIgnoreCase(departmentId, keyword.trim());
        } else if (hasKeyword) {
            return staffRepository.findByNameContainingIgnoreCase(keyword.trim());
        } else if (hasDept) {
            return staffRepository.findByDepartmentId(departmentId);
        } else {
            return staffRepository.findAll();
        }
    }

    @Transactional
    public Optional<Staff> createStaff(Staff staff) {
        Long deptId = staff.getDepartmentId();
        if (deptId == null && staff.getDepartment() != null) {
            deptId = staff.getDepartment().getId();
        }

        if (deptId == null) {
            return Optional.empty();
        }

        Optional<Department> deptOpt = departmentRepository.findById(deptId);
        if (deptOpt.isEmpty()) {
            return Optional.empty(); // Phong ban khong ton tai
        }

        staff.setDepartment(deptOpt.get());
        Staff saved = staffRepository.save(staff);
        return Optional.of(saved);
    }

    // CẬP NHẬT NHÂN VIÊN (UPDATE)
    @Transactional
    public Optional<Staff> updateStaff(Long id, Staff updatedStaff) {
        Optional<Staff> existingOpt = staffRepository.findById(id);
        if (existingOpt.isEmpty()) {
            return Optional.empty(); // Nhan vien khong ton tai
        }

        Long deptId = updatedStaff.getDepartmentId();
        if (deptId == null && updatedStaff.getDepartment() != null) {
            deptId = updatedStaff.getDepartment().getId();
        }

        if (deptId == null) {
            return Optional.empty();
        }

        Optional<Department> targetDeptOpt = departmentRepository.findById(deptId);
        if (targetDeptOpt.isEmpty()) {
            return Optional.empty(); // Phong ban moi khong ton tai
        }

        Staff existing = existingOpt.get();
        existing.setName(updatedStaff.getName());
        existing.setEmail(updatedStaff.getEmail());
        existing.setDepartment(targetDeptOpt.get());

        Staff saved = staffRepository.save(existing);
        return Optional.of(saved);
    }

    // XÓA NHÂN VIÊN (DELETE)
    @Transactional
    public boolean deleteStaff(Long staffId) {
        if (staffRepository.existsById(staffId)) {
            staffRepository.deleteById(staffId);
            return true;
        }
        return false;
    }
}
