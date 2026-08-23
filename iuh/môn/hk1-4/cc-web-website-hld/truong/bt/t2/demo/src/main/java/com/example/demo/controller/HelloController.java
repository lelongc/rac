package com.example.demo.controller;

import org.springframework.web.bind.annotation.*;

import java.util.*;

@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "*")
public class HelloController {

    // 1. GET API don gian
    @GetMapping("/hello")
    public Map<String, Object> sayHello(@RequestParam(value = "name", defaultValue = "Sinh vien IUH") String name) {
        Map<String, Object> res = new HashMap<>();
        res.put("status", "success");
        res.put("message", "Xin chao " + name + " den voi Spring Boot RESTful API!");
        res.put("timestamp", new Date());
        return res;
    }

    // 2. GET API tra ve danh sach san pham mau
    @GetMapping("/products")
    public List<Map<String, Object>> getProducts() {
        List<Map<String, Object>> list = new ArrayList<>();

        Map<String, Object> p1 = new HashMap<>();
        p1.put("id", 1);
        p1.put("name", "Laptop Gaming ASUS ROG");
        p1.put("price", 28000000);
        p1.put("image", "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=500");
        list.add(p1);

        Map<String, Object> p2 = new HashMap<>();
        p2.put("id", 2);
        p2.put("name", "Apple iPhone 15 Pro Max");
        p2.put("price", 29500000);
        p2.put("image", "https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=500");
        list.add(p2);

        return list;
    }
}
