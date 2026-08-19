package api;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.Map;

// RESTful API Servlet cho Bài 1 Quy đổi tiền tệ
public class CurrencyServlet {
    private static final Map<String, Double> RATES = new HashMap<>();
    static {
        RATES.put("USD", 1.0);
        RATES.put("VND", 25450.0);
        RATES.put("EUR", 0.92);
        RATES.put("JPY", 155.2);
        RATES.put("GBP", 0.79);
    }

    public static String processRequest(String amountStr, String from, String to) {
        if (amountStr == null || from == null || to == null || !RATES.containsKey(from) || !RATES.containsKey(to)) {
            return "{\"status\":\"error\",\"message\":\"Tham so khong hop le\"}";
        }
        try {
            double amount = Double.parseDouble(amountStr);
            double result = (amount / RATES.get(from)) * RATES.get(to);
            return String.format(
                "{\"status\":\"success\",\"amount\":%.2f,\"from\":\"%s\",\"to\":\"%s\",\"result\":%.2f}",
                amount, from, to, result
            );
        } catch (NumberFormatException e) {
            return "{\"status\":\"error\",\"message\":\"So tien khong hop le\"}";
        }
    }
}
