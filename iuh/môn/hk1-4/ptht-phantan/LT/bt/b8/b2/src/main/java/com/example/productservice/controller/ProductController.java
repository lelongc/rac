package com.example.productservice.controller;

import com.example.productservice.model.Product;
import com.example.productservice.service.ProductService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/products")
public class ProductController {

    private final ProductService service;

    public ProductController(ProductService service) {
        this.service = service;
    }

    @GetMapping
    public List<Product> getAll() {
        return service.getAll();
    }

    @GetMapping("/{id}")
    public Product getById(@PathVariable int id) {
        return service.getById(id);
    }

    @GetMapping("/category/{category}")
    public List<Product> findByCategory(@PathVariable String category) {
        return service.findByCategory(category);
    }

    @PostMapping
    public Product add(@RequestBody Product p) {
        return service.add(p);
    }

    @PutMapping("/{id}")
    public Product update(@PathVariable int id, @RequestBody Product p) {
        return service.update(id, p);
    }

    @DeleteMapping("/{id}")
    public String delete(@PathVariable int id) {
        return service.delete(id);
    }
}
