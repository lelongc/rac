package com.example.faculty_crud;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class FacultyCrudApplication {

    public static void main(String[] args) {
        SpringApplication.run(FacultyCrudApplication.class, args);
        System.out.println("=================================================");
        System.out.println(">> b6_2_faculty_crud DANG CHAY TAI CONG 8083!");
        System.out.println(">> Web UI:      http://localhost:8083/faculties");
        System.out.println(">> REST API:    http://localhost:8083/api/faculties");
        System.out.println("=================================================");
    }
}
