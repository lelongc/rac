package api;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

public class ProductService {
    private static final List<Product> products = new ArrayList<>();

    static {
        products.add(new Product("SP01", "Laptop Dell XPS 15", 35000000, 5, "Laptop"));
        products.add(new Product("SP02", "iPhone 15 Pro Max", 30000000, 10, "Dien thoai"));
        products.add(new Product("SP03", "Tai nghe Sony WH-1000XM5", 8500000, 12, "Phu kien"));
        products.add(new Product("SP04", "Ban phim Keychron K2", 2100000, 8, "Phu kien"));
    }

    // 1. GET: Lấy tất cả hoặc theo ID
    public static synchronized String getAllAsJson() {
        StringBuilder sb = new StringBuilder("[");
        for (int i = 0; i < products.size(); i++) {
            sb.append(products.get(i).toJson());
            if (i < products.size() - 1) sb.append(",");
        }
        sb.append("]");
        return sb.toString();
    }

    public static synchronized String getByIdAsJson(String id) {
        Optional<Product> p = products.stream().filter(prod -> prod.getId().equalsIgnoreCase(id)).findFirst();
        if (p.isPresent()) {
            return p.get().toJson();
        }
        return "{\"status\":\"error\",\"message\":\"Khong tim thay san pham\"}";
    }

    // 2. POST: Thêm mới sản phẩm
    public static synchronized String addProduct(String id, String name, double price, int quantity, String category) {
        boolean exists = products.stream().anyMatch(p -> p.getId().equalsIgnoreCase(id));
        if (exists) {
            return "{\"status\":\"error\",\"message\":\"Ma san pham da ton tai\"}";
        }
        Product p = new Product(id, name, price, quantity, category);
        products.add(p);
        return "{\"status\":\"success\",\"message\":\"Them san pham thanh cong\",\"data\":" + p.toJson() + "}";
    }

    // 3. PUT: Cập nhật sản phẩm
    public static synchronized String updateProduct(String id, String name, double price, int quantity, String category) {
        for (Product p : products) {
            if (p.getId().equalsIgnoreCase(id)) {
                if (name != null && !name.isEmpty()) p.setName(name);
                if (price > 0) p.setPrice(price);
                if (quantity >= 0) p.setQuantity(quantity);
                if (category != null && !category.isEmpty()) p.setCategory(category);
                return "{\"status\":\"success\",\"message\":\"Cap nhat san pham thanh cong\",\"data\":" + p.toJson() + "}";
            }
        }
        return "{\"status\":\"error\",\"message\":\"Khong tim thay san pham de cap nhat\"}";
    }

    // 4. DELETE: Xóa sản phẩm
    public static synchronized String deleteProduct(String id) {
        boolean removed = products.removeIf(p -> p.getId().equalsIgnoreCase(id));
        if (removed) {
            return "{\"status\":\"success\",\"message\":\"Xoa san pham thanh cong ID=" + id + "\"}";
        }
        return "{\"status\":\"error\",\"message\":\"Khong tim thay san pham de xoa\"}";
    }
}
