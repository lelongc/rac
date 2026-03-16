package com.example.tuan5.bai2;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class TriangleController {

    @GetMapping("/bai2")
    public String index() {
        return "bai2";
    }

    @PostMapping("/bai2/calculate")
    public String calculate(@RequestParam double base, @RequestParam double height, Model model) {
        if (base <= 0 || height <= 0) {
            model.addAttribute("error", "Cạnh đáy và chiều cao phải lớn hơn 0");
            return "bai2";
        }
        
        double area = 0.5 * base * height;
        model.addAttribute("base", base);
        model.addAttribute("height", height);
        model.addAttribute("area", area);
        return "bai2";
    }
}
