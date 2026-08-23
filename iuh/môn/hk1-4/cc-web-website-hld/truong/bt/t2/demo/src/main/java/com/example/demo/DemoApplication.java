package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class DemoApplication {

	public static void main(String[] args) {
		SpringApplication.run(DemoApplication.class, args);
		System.out.println("=================================================");
		System.out.println("  SPRING BOOT DEMO APPLICATION DANG CHAY!       ");
		System.out.println("  Mo trinh duyet truy cap:                       ");
		System.out.println("  👉 http://localhost:8080/                      ");
		System.out.println("  👉 http://localhost:8080/api/hello             ");
		System.out.println("=================================================");
	}

}
