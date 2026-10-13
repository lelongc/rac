package com.example.productservice;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;
import java.util.concurrent.CopyOnWriteArrayList;

@RestController
@RequestMapping({"/api/products", "/products"})
public class ProductController {

    private final List<Product> products = new CopyOnWriteArrayList<>();

    public ProductController() {
        products.add(new Product(1L, "Laptop Dell XPS 15", 25000000.0));
        products.add(new Product(2L, "Mouse Logitech MX Master", 1850000.0));
        products.add(new Product(3L, "Keyboard Keychron K2", 2100000.0));
    }

    @GetMapping
    public List<Product> getAllProducts() {
        return products;
    }

    @PostMapping
    public Product addProduct(@RequestBody Product newProduct) {
        if (newProduct.getId() == null) {
            long maxId = products.stream()
                    .mapToLong(p -> p.getId() != null ? p.getId() : 0)
                    .max()
                    .orElse(0);
            newProduct.setId(maxId + 1);
        }
        products.add(newProduct);
        return newProduct;
    }

    @DeleteMapping("/{id}")
    public String deleteProduct(@PathVariable Long id) {
        boolean removed = products.removeIf(p -> p.getId() != null && p.getId().equals(id));
        if (removed) {
            return "Deleted product with ID: " + id;
        } else {
            return "Product not found with ID: " + id;
        }
    }
}
