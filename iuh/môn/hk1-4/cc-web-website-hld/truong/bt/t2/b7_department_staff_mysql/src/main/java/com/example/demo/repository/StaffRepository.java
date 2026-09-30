package com.example.demo.repository;

import com.example.demo.model.Staff;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface StaffRepository extends JpaRepository<Staff, Long> {

    // Tìm kiếm tất cả nhân viên theo ID phòng ban
    @Query("SELECT s FROM Staff s WHERE s.department.id = :departmentId")
    List<Staff> findByDepartmentId(@Param("departmentId") Long departmentId);

    // Tìm kiếm nhân viên theo tên (không phân biệt hoa thường)
    List<Staff> findByNameContainingIgnoreCase(String keyword);

    // Tìm kiếm nhân viên kết hợp cả phòng ban và tên
    @Query("SELECT s FROM Staff s WHERE s.department.id = :departmentId AND LOWER(s.name) LIKE LOWER(CONCAT('%', :keyword, '%'))")
    List<Staff> findByDepartmentIdAndNameContainingIgnoreCase(@Param("departmentId") Long departmentId, @Param("keyword") String keyword);
}
