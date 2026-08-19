package bt2_products;

import java.io.IOException;
import java.io.PrintWriter;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/api/products")
public class ProductServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        // Thiết lập header trả về kiểu dữ liệu JSON
        response.setContentType("application/json; charset=UTF-8");
        response.setHeader("Access-Control-Allow-Origin", "*");

        PrintWriter out = response.getWriter();

        // Mảng đối tượng sản phẩm dưới dạng mảng JSON
        String productsJson = "[\n" +
            "  { \"id\": \"SP01\", \"name\": \"Laptop Dell XPS 15\", \"price\": 35000000, \"quantity\": 5, \"category\": \"Laptop\" },\n" +
            "  { \"id\": \"SP02\", \"name\": \"Điện thoại iPhone 15 Pro\", \"price\": 28000000, \"quantity\": 10, \"category\": \"Điện thoại\" },\n" +
            "  { \"id\": \"SP03\", \"name\": \"Tai nghe Sony WH-1000XM5\", \"price\": 8500000, \"quantity\": 12, \"category\": \"Phụ kiện\" },\n" +
            "  { \"id\": \"SP04\", \"name\": \"Bàn phím cơ Keychron K2\", \"price\": 2100000, \"quantity\": 8, \"category\": \"Phụ kiện\" },\n" +
            "  { \"id\": \"SP05\", \"name\": \"Màn hình LG UltraGear 27 inch\", \"price\": 7900000, \"quantity\": 4, \"category\": \"Màn hình\" }\n" +
            "]";

        out.print(productsJson);
    }
}
