package com.example.demo.controller;

import org.springframework.web.bind.annotation.*;
import java.util.*;

@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "*")
public class HelloController {

    @GetMapping("/hello")
    public Map<String, Object> sayHello(@RequestParam(value = "name", defaultValue = "Sinh viên IUH") String name) {
        Map<String, Object> res = new HashMap<>();
        res.put("status", "success");
        res.put("message", "Xin chào " + name + " đến với Spring Boot RESTful API!");
        res.put("timestamp", new Date());
        return res;
    }
}
