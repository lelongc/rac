package com.example.gk;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class GkApplication {

    public static void main(String[] args) {
        SpringApplication.run(GkApplication.class, args);
        System.out.println("=================================================");
        System.out.println(">> UNG DUNG THI GIUA KY (MVC THYMELEAF) DANG CHAY!");
        System.out.println(">> TRUY CAP TAI CONG: http://localhost:8084/faculties");
        System.out.println("=================================================");
    }
}
