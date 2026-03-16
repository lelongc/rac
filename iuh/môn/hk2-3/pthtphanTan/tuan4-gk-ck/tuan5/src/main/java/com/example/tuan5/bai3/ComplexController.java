package com.example.tuan5.bai3;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class ComplexController {

    @GetMapping("/bai3")
    public String index() {
        return "bai3";
    }

    @PostMapping("/bai3/calculate")
    public String calculate(
            @RequestParam double r1, @RequestParam double i1,
            @RequestParam double r2, @RequestParam double i2,
            @RequestParam String op,
            Model model) {
        
        double resR = 0, resI = 0;
        String opText = "";
        
        switch (op) {
            case "add":
                resR = r1 + r2; resI = i1 + i2; opText = "+";
                break;
            case "sub":
                resR = r1 - r2; resI = i1 - i2; opText = "-";
                break;
            case "mul":
                resR = r1 * r2 - i1 * i2;
                resI = r1 * i2 + r2 * i1;
                opText = "*";
                break;
            case "div":
                double den = r2 * r2 + i2 * i2;
                if (den == 0) {
                    model.addAttribute("error", "Không thể chia cho 0");
                    return "bai3";
                }
                resR = (r1 * r2 + i1 * i2) / den;
                resI = (i1 * r2 - r1 * i2) / den;
                opText = "/";
                break;
        }
        
        model.addAttribute("result", String.format("%.2f + %.2fi", resR, resI));
        model.addAttribute("calculation", String.format("(%.1f + %.1fi) %s (%.1f + %.1fi)", r1, i1, opText, r2, i2));
        return "bai3";
    }
}
