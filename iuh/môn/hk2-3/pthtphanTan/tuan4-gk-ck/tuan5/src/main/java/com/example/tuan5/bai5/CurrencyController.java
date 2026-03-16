package com.example.tuan5.bai5;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class CurrencyController {

    private static final double RATE = 25000.0;

    @GetMapping("/bai5")
    public String index() {
        return "bai5";
    }

    @PostMapping("/bai5/convert")
    public String convert(@RequestParam double amount, @RequestParam String direction, Model model) {
        double result;
        String from, to;
        
        if (direction.equals("usd2vnd")) {
            result = amount * RATE;
            from = amount + " USD";
            to = String.format("%,.0f VND", result);
        } else {
            result = amount / RATE;
            from = String.format("%,.0f VND", amount);
            to = String.format("%.2f USD", result);
        }
        
        model.addAttribute("amount", amount);
        model.addAttribute("from", from);
        model.addAttribute("to", to);
        return "bai5";
    }
}
