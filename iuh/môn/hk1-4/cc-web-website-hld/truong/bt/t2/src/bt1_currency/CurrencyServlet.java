package bt1_currency;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.Map;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/api/convert")
public class CurrencyServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;

    // Bảng tỷ giá quy đổi gốc (USD = 1.0)
    private static final Map<String, Double> RATES = new HashMap<>();
    static {
        RATES.put("USD", 1.0);
        RATES.put("VND", 25450.0);
        RATES.put("EUR", 0.92);
        RATES.put("JPY", 155.2);
        RATES.put("GBP", 0.79);
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        // Cấu hình Header trả về kiểu dữ liệu JSON
        response.setContentType("application/json; charset=UTF-8");
        response.setHeader("Access-Control-Allow-Origin", "*");

        PrintWriter out = response.getWriter();

        try {
            String amountParam = request.getParameter("amount");
            String from = request.getParameter("from");
            String to = request.getParameter("to");

            if (amountParam == null || from == null || to == null ||
                !RATES.containsKey(from) || !RATES.containsKey(to)) {
                response.setStatus(HttpServletResponse.SC_BAD_REQUEST);
                out.print("{\"status\":\"error\",\"message\":\"Tham so khong hop le\"}");
                return;
            }

            double amount = Double.parseDouble(amountParam);
            double rateFrom = RATES.get(from);
            double rateTo = RATES.get(to);
            double result = (amount / rateFrom) * rateTo;

            // Tạo chuỗi JSON trả về cho Client
            String jsonResponse = String.format(
                "{\"status\":\"success\",\"amount\":%.2f,\"from\":\"%s\",\"to\":\"%s\",\"result\":%.2f}",
                amount, from, to, result
            );

            out.print(jsonResponse);
        } catch (Exception e) {
            response.setStatus(HttpServletResponse.SC_INTERNAL_SERVER_ERROR);
            out.print("{\"status\":\"error\",\"message\":\"Loi xu ly Server\"}");
        }
    }
}
