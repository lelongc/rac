package com.example.basic_web.controller;

import com.example.basic_web.model.Product;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.Arrays;
import java.util.List;

@Controller
public class ProductController {

    @GetMapping("/")
    public String index() {
        return "redirect:/products";
    }

    @GetMapping("/products")
    public String getProducts(Model model) {
        List<Product> productList = Arrays.asList(
                new Product(1L, "Laptop Dell XPS 15", 999.99),
                new Product(2L, "Smartphone iPhone 15", 699.99),
                new Product(3L, "Wireless Headphones Sony", 149.99),
                new Product(4L, "Mechanical Keyboard RGB", 89.50)
        );

        model.addAttribute("products", productList);
        return "product_list";
    }

    @GetMapping("/dashboard")
    public String getDashboard() {
        return "dashboard";
    }

    @GetMapping("/table-demo")
    public String getTableDemo() {
        return "abc";
    }
}
