package com.example.productservice.service;

import com.example.productservice.exception.ProductNotFoundException;
import com.example.productservice.model.Product;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

@Service
public class ProductService {
    private List<Product> products = new ArrayList<>();

    public ProductService() {
        products.add(new Product(1, "Laptop", 1200.0, "Electronics"));
        products.add(new Product(2, "Book", 15.0, "Education"));
        products.add(new Product(3, "Phone", 800.0, "Electronics"));
    }

    public List<Product> getAll() {
        return products;
    }

    public Product getById(int id) {
        return products.stream()
                .filter(p -> p.getId() == id)
                .findFirst()
                .orElseThrow(() -> new ProductNotFoundException("Product ID " + id + " not found"));
    }

    public Product add(Product p) {
        products.add(p);
        return p;
    }

    public Product update(int id, Product updated) {
        Product existing = getById(id);
        existing.setName(updated.getName());
        existing.setPrice(updated.getPrice());
        existing.setCategory(updated.getCategory());
        return existing;
    }

    public String delete(int id) {
        Product p = getById(id);
        products.remove(p);
        return "Deleted product: " + p.getName();
    }

    public List<Product> findByCategory(String category) {
        return products.stream()
                .filter(p -> p.getCategory().equalsIgnoreCase(category))
                .toList();
    }
}
