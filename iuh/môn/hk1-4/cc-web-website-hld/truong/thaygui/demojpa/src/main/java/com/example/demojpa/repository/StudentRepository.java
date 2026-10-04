package com.example.demojpa.repository;

import com.example.demojpa.entity.Student;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

/**
 * Interface Repository (Thầy ví von là "CÁI KHO" chứa Student)
 * Kế thừa JpaRepository để có sẵn các hàm:
 * - findAll(): Lấy tất cả sinh viên
 * - findById(id): Tìm theo mã sinh viên
 * - save(entity): Thêm mới hoặc cập nhật
 * - deleteById(id): Xóa sinh viên
 */
@Repository
public interface StudentRepository extends JpaRepository<Student, Long> {

    // Tìm kiếm sinh viên theo tên (không phân biệt chữ hoa, chữ thường)
    List<Student> findByNameContainingIgnoreCase(String name);
}
