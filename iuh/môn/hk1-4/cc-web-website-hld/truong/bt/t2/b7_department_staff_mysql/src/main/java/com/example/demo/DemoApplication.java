package com.example.demo;

import com.example.demo.model.Department;
import com.example.demo.model.Staff;
import com.example.demo.repository.DepartmentRepository;
import com.example.demo.repository.StaffRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class DemoApplication {

    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }

    /**
     * Tự động khởi tạo dữ liệu mẫu vào MySQL khi chạy lần đầu
     * Nếu bảng departments chưa có dữ liệu, Hibernate sẽ nạp sẵn các phòng ban và nhân viên mẫu.
     */
    @Bean
    public CommandLineRunner initData(DepartmentRepository deptRepo, StaffRepository staffRepo) {
        return args -> {
            if (deptRepo.count() == 0) {
                System.out.println(">>> Khoi tao du lieu mau vao Database MySQL...");

                Department deptIt = deptRepo.save(new Department("Engineering (Ky thuat)"));
                Department deptHr = deptRepo.save(new Department("Human Resources (Nhan su)"));
                Department deptMkt = deptRepo.save(new Department("Marketing & Truyen thong"));
                Department deptFin = deptRepo.save(new Department("Finance (Tai chinh)"));

                staffRepo.save(new Staff("Nguyen Van An", "an.nguyen@example.com", deptIt));
                staffRepo.save(new Staff("Tran Thi Binh", "binh.tran@example.com", deptIt));
                staffRepo.save(new Staff("Le Hoang Cuong", "cuong.le@example.com", deptHr));
                staffRepo.save(new Staff("Pham Thi Dung", "dung.pham@example.com", deptMkt));
                staffRepo.save(new Staff("Doan Minh Em", "em.doan@example.com", deptFin));

                System.out.println(">>> Khoi tao thanh cong 4 phong ban va 5 nhan vien mau vao MySQL!");
            }
        };
    }
}
