package com.example.tuan5.bai6;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import jakarta.annotation.PostConstruct;
import java.util.Arrays;

@Controller
public class DatabaseController {

    @Autowired
    private ProductRepository repository;

    @PostConstruct
    public void init() {
        if (repository.count() == 0) {
            repository.saveAll(Arrays.asList(
                new Product("iPhone 15 Pro Max 256GB", 32990000),
                new Product("Samsung Galaxy S24 Ultra", 29500000),
                new Product("MacBook Air M3 2024", 27900000),
                new Product("Sony WH-1000XM5", 8500000),
                new Product("iPad Pro M2 11-inch", 21000000),
                new Product("Apple Watch Series 9", 10500000)
            ));
        }
    }

    @GetMapping("/bai6")
    public String index(Model model) {
        try {
            model.addAttribute("products", repository.findAll());
            return "bai6";
        } catch (Exception e) {
            e.printStackTrace();
            model.addAttribute("error", e.getMessage());
            return "index"; // Tra ve trang chu neu loi
        }
    }
}
