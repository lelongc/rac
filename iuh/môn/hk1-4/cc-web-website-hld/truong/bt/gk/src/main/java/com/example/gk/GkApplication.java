package com.example.gk;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class GkApplication {

    public static void main(String[] args) {
        SpringApplication.run(GkApplication.class, args);
        System.out.println("=================================================");
        System.out.println(">> UNG DUNG THI GIUA KY: WEB SERVICE (REST API) + SPA DANG CHAY!");
        System.out.println(">> TRUY CAP GIAO DIEN SPA: http://localhost:8084/");
        System.out.println(">> WEB SERVICE API KHOA: http://localhost:8084/api/faculties");
        System.out.println("=================================================");
    }
}
