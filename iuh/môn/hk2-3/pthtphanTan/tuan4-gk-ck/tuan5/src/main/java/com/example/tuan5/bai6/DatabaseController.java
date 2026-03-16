package com.example.tuan5.bai6;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import jakarta.annotation.PostConstruct;
import java.util.Arrays;

@Controller
@RequestMapping("/bai6")
public class DatabaseController {

    @Autowired
    private ProductRepository repository;

    @PostConstruct
    public void init() {
        try {
            if (repository.count() == 0) {
                repository.saveAll(Arrays.asList(
                    new Product("iPhone 15 Pro Max 256GB", 32990000),
                    new Product("Samsung Galaxy S24 Ultra", 29500000),
                    new Product("MacBook Air M3 2024", 27900000),
                    new Product("Sony WH-1000XM5", 8500000)
                ));
            }
        } catch (Exception e) {
            System.err.println("Database init error: " + e.getMessage());
        }
    }

    @GetMapping
    public String index(Model model) {
        try {
            model.addAttribute("products", repository.findAll());
            return "bai6";
        } catch (Exception e) {
            e.printStackTrace();
            model.addAttribute("error", "Lỗi kết nối database: " + e.getMessage());
            return "index";
        }
    }

    @PostMapping("/add")
    public String addProduct(@RequestParam String name, @RequestParam double price) {
        repository.save(new Product(name, price));
        return "redirect:/bai6";
    }

    @GetMapping("/delete/{id}")
    public String deleteProduct(@PathVariable Long id) {
        repository.deleteById(id);
        return "redirect:/bai6";
    }
}
