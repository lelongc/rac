package com.example.demo.controller;

import com.example.demo.model.Item;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.concurrent.CopyOnWriteArrayList;
import java.util.concurrent.atomic.AtomicLong;
import java.util.stream.Collectors;

@RestController
@RequestMapping({"/api/items", "/api/products", "/api/students", "/items", "/products", "/students"})
public class ItemController {

    private final List<Item> items = new CopyOnWriteArrayList<>();
    private final AtomicLong idGenerator = new AtomicLong(1);

    public ItemController() {
        // Sample seed data to ensure instant response when testing
        items.add(new Item(idGenerator.getAndIncrement(), "Laptop Dell XPS 15", "DELL-XPS", 25000000.0, "Electronics", 10, "High performance laptop"));
        items.add(new Item(idGenerator.getAndIncrement(), "Mouse Logitech MX Master 3", "LOGI-MX3", 1850000.0, "Accessories", 25, "Wireless ergonomics mouse"));
        items.add(new Item(idGenerator.getAndIncrement(), "Keyboard Keychron K2", "KEY-K2", 2100000.0, "Accessories", 15, "Mechanical wireless keyboard"));
    }

    // 1. GET ALL: Lấy tất cả danh sách
    @GetMapping
    public List<Item> getAll() {
        return items;
    }

    // 2. GET BY ID: Lấy chi tiết theo ID
    @GetMapping("/{id}")
    public ResponseEntity<Item> getById(@PathVariable Long id) {
        return items.stream()
                .filter(item -> item.getId() != null && item.getId().equals(id))
                .findFirst()
                .map(ResponseEntity::ok)
                .orElseGet(() -> ResponseEntity.status(HttpStatus.NOT_FOUND).build());
    }

    // 3. POST: Thêm đối tượng mới
    @PostMapping
    public ResponseEntity<Item> create(@RequestBody Item newItem) {
        if (newItem.getId() == null || newItem.getId() <= 0) {
            long maxId = items.stream()
                    .mapToLong(i -> i.getId() != null ? i.getId() : 0)
                    .max()
                    .orElse(0);
            long nextId = Math.max(maxId + 1, idGenerator.getAndIncrement());
            newItem.setId(nextId);
        } else {
            if (newItem.getId() >= idGenerator.get()) {
                idGenerator.set(newItem.getId() + 1);
            }
        }
        items.add(newItem);
        return ResponseEntity.status(HttpStatus.CREATED).body(newItem);
    }

    // 4. PUT: Cập nhật thông tin đối tượng theo ID
    @PutMapping("/{id}")
    public ResponseEntity<Item> update(@PathVariable Long id, @RequestBody Item updatedData) {
        for (int i = 0; i < items.size(); i++) {
            Item current = items.get(i);
            if (current.getId() != null && current.getId().equals(id)) {
                if (updatedData.getName() != null) current.setName(updatedData.getName());
                if (updatedData.getPrice() != null) current.setPrice(updatedData.getPrice());
                if (updatedData.getCode() != null) current.setCode(updatedData.getCode());
                if (updatedData.getCategory() != null) current.setCategory(updatedData.getCategory());
                if (updatedData.getQuantity() != null) current.setQuantity(updatedData.getQuantity());
                if (updatedData.getDescription() != null) current.setDescription(updatedData.getDescription());
                return ResponseEntity.ok(current);
            }
        }
        return ResponseEntity.status(HttpStatus.NOT_FOUND).build();
    }

    // 5. DELETE: Xóa theo ID
    @DeleteMapping("/{id}")
    public ResponseEntity<String> delete(@PathVariable Long id) {
        boolean removed = items.removeIf(item -> item.getId() != null && item.getId().equals(id));
        if (removed) {
            return ResponseEntity.ok("Deleted item with ID: " + id);
        } else {
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body("Item not found with ID: " + id);
        }
    }

    // 6. SEARCH: Tìm kiếm theo từ khóa (name hoặc code hoặc category)
    @GetMapping("/search")
    public List<Item> search(@RequestParam(name = "keyword", defaultValue = "") String keyword) {
        String kw = keyword.trim().toLowerCase();
        if (kw.isEmpty()) {
            return items;
        }
        return items.stream()
                .filter(i -> (i.getName() != null && i.getName().toLowerCase().contains(kw))
                        || (i.getCode() != null && i.getCode().toLowerCase().contains(kw))
                        || (i.getCategory() != null && i.getCategory().toLowerCase().contains(kw)))
                .collect(Collectors.toList());
    }

    // 7. FILTER: Lọc theo khoảng giá hoặc số lượng
    @GetMapping("/filter")
    public List<Item> filter(
            @RequestParam(name = "minPrice", required = false) Double minPrice,
            @RequestParam(name = "maxPrice", required = false) Double maxPrice) {
        return items.stream()
                .filter(i -> {
                    if (minPrice != null && (i.getPrice() == null || i.getPrice() < minPrice)) {
                        return false;
                    }
                    if (maxPrice != null && (i.getPrice() == null || i.getPrice() > maxPrice)) {
                        return false;
                    }
                    return true;
                })
                .collect(Collectors.toList());
    }
}
