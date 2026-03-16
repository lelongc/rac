package com.example.tuan5.bai4;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import java.util.ArrayList;
import java.util.List;

@Controller
public class FibonacciController {

    @GetMapping("/bai4")
    public String index() {
        return "bai4";
    }

    @PostMapping("/bai4/calculate")
    public String calculate(@RequestParam int n, Model model) {
        if (n < 0) {
            model.addAttribute("error", "Vui lòng nhập số dương");
            return "bai4";
        }
        
        List<Long> sequence = new ArrayList<>();
        if (n >= 1) sequence.add(0L);
        if (n >= 2) sequence.add(1L);
        
        for (int i = 2; i < n; i++) {
            sequence.add(sequence.get(i - 1) + sequence.get(i - 2));
        }
        
        model.addAttribute("n", n);
        model.addAttribute("sequence", sequence);
        return "bai4";
    }
}
