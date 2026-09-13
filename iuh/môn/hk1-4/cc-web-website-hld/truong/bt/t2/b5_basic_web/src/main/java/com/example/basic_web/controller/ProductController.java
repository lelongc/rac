package com.example.basic_web.controller;

import com.example.basic_web.model.Product;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.Arrays;
import java.util.List;

@Controller
public class ProductController {

    // 1. Danh sách sản phẩm: Hỗ trợ mọi biến thể URL thường gặp để chống lỗi 404
    @GetMapping({"/", "/products", "/product", "/product-list", "/product_list", "/home", "/index"})
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

    // 2. Giao diện Admin Dashboard
    @GetMapping({"/dashboard", "/admin", "/admin/dashboard"})
    public String getDashboard() {
        return "dashboard";
    }

    // 3. Demo bảng tương tác
    @GetMapping({"/table-demo", "/table", "/abc"})
    public String getTableDemo() {
        return "abc";
    }
}
