package api;

// RESTful API Servlet cho Bài 2 Danh sách sản phẩm
public class ProductServlet {
    public static String getProductsJson() {
        return "[\n" +
            "  { \"id\": \"SP01\", \"name\": \"Laptop Dell XPS 15\", \"price\": 35000000, \"quantity\": 5, \"category\": \"Laptop\" },\n" +
            "  { \"id\": \"SP02\", \"name\": \"Điện thoại iPhone 15 Pro\", \"price\": 28000000, \"quantity\": 10, \"category\": \"Điện thoại\" },\n" +
            "  { \"id\": \"SP03\", \"name\": \"Tai nghe Sony WH-1000XM5\", \"price\": 8500000, \"quantity\": 12, \"category\": \"Phụ kiện\" },\n" +
            "  { \"id\": \"SP04\", \"name\": \"Bàn phím cơ Keychron K2\", \"price\": 2100000, \"quantity\": 8, \"category\": \"Phụ kiện\" },\n" +
            "  { \"id\": \"SP05\", \"name\": \"Màn hình LG UltraGear 27 inch\", \"price\": 7900000, \"quantity\": 4, \"category\": \"Màn hình\" }\n" +
            "]";
    }
}
