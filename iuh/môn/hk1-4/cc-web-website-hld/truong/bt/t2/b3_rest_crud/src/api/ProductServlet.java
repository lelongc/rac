package api;

// Servlet đại diện chuẩn RESTful API cho 4 phương thức HTTP GET, POST, PUT, DELETE
public class ProductServlet {
    // 1. GET (Read)
    public String doGet(String id) {
        if (id == null || id.isEmpty()) {
            return ProductService.getAllAsJson();
        }
        return ProductService.getByIdAsJson(id);
    }

    // 2. POST (Create)
    public String doPost(String id, String name, double price, int quantity, String category) {
        return ProductService.addProduct(id, name, price, quantity, category);
    }

    // 3. PUT (Update)
    public String doPut(String id, String name, double price, int quantity, String category) {
        return ProductService.updateProduct(id, name, price, quantity, category);
    }

    // 4. DELETE (Delete)
    public String doDelete(String id) {
        return ProductService.deleteProduct(id);
    }
}
