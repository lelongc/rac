package com.example.demojpa;

import com.example.demojpa.entity.Student;
import com.example.demojpa.repository.StudentRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class DemojpaApplication {

    public static void main(String[] args) {
        SpringApplication.run(DemojpaApplication.class, args);
    }

    /**
     * Tự động khởi tạo dữ liệu mẫu vào MySQL khi ứng dụng chạy lần đầu
     */
    @Bean
    public CommandLineRunner initData(StudentRepository studentRepo) {
        return args -> {
            if (studentRepo.count() == 0) {
                System.out.println(">>> Nap du lieu sinh vien mau vao MySQL Server...");
                studentRepo.save(new Student("Nguyen Van An", "an.nguyen@iuh.edu.vn", "0901234567"));
                studentRepo.save(new Student("Tran Thi Binh", "binh.tran@iuh.edu.vn", "0912345678"));
                studentRepo.save(new Student("Le Hoang Cuong", "cuong.le@iuh.edu.vn", "0923456789"));
                studentRepo.save(new Student("Pham Thi Dung", "dung.pham@iuh.edu.vn", "0934567890"));
                studentRepo.save(new Student("Doan Minh Em", "em.doan@iuh.edu.vn", "0945678901"));
                System.out.println(">>> Khoi tao thanh cong 5 sinh vien vao MySQL!");
            }
        };
    }
}
