package webserver;

import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpExchange;

import java.io.*;
import java.net.InetSocketAddress;
import java.net.URI;
import java.nio.file.Files;
import java.util.HashMap;
import java.util.Map;

public class WebServer {
    private static final int PORT = 8080;

    public static void main(String[] args) throws IOException {
        HttpServer server = HttpServer.create(new InetSocketAddress(PORT), 0);

        // 1. Route RESTful API Quy doi tien te (Package bt1_currency)
        server.createContext("/api/convert", new ConvertHandler());

        // 2. Route RESTful API Danh sach san pham (Package bt2_products)
        server.createContext("/api/products", new ProductsHandler());

        // 3. Static File Server cho WebContent (HTML, CSS, JS)
        server.createContext("/", new StaticFileHandler());

        server.setExecutor(null);
        System.out.println("=== WEB SERVER DA KHỞI ĐỘNG DỰ ÁN T2 ===");
        System.out.println("Truy cap trang chu: http://localhost:" + PORT + "/index.html");
        System.out.println("Bai 1 (Quy doi tien te): http://localhost:" + PORT + "/b1_currency.html");
        System.out.println("Bai 2 (Danh sach san pham): http://localhost:" + PORT + "/b2_products.html");
        System.out.println("REST API Products: http://localhost:" + PORT + "/api/products");
        System.out.println("REST API Convert: http://localhost:" + PORT + "/api/convert?amount=100&from=USD&to=VND");
        server.start();
    }

    // Handler 1: RESTful API quy đổi tiền tệ
    static class ConvertHandler implements HttpHandler {
        private static final Map<String, Double> RATES = new HashMap<>();
        static {
            RATES.put("USD", 1.0);
            RATES.put("VND", 25450.0);
            RATES.put("EUR", 0.92);
            RATES.put("JPY", 155.2);
            RATES.put("GBP", 0.79);
        }

        @Override
        public void handle(HttpExchange exchange) throws IOException {
            exchange.getResponseHeaders().add("Access-Control-Allow-Origin", "*");
            exchange.getResponseHeaders().add("Content-Type", "application/json; charset=UTF-8");

            URI requestURI = exchange.getRequestURI();
            String query = requestURI.getQuery();
            Map<String, String> params = parseQuery(query);

            String amountStr = params.get("amount");
            String from = params.get("from");
            String to = params.get("to");

            String jsonResponse;
            int statusCode = 200;

            if (amountStr != null && from != null && to != null && RATES.containsKey(from) && RATES.containsKey(to)) {
                try {
                    double amount = Double.parseDouble(amountStr);
                    double result = (amount / RATES.get(from)) * RATES.get(to);
                    jsonResponse = String.format(
                        "{\"status\":\"success\",\"amount\":%.2f,\"from\":\"%s\",\"to\":\"%s\",\"result\":%.2f}",
                        amount, from, to, result
                    );
                } catch (NumberFormatException e) {
                    statusCode = 400;
                    jsonResponse = "{\"status\":\"error\",\"message\":\"So tien khong hop le\"}";
                }
            } else {
                statusCode = 400;
                jsonResponse = "{\"status\":\"error\",\"message\":\"Thieu tham so request\"}";
            }

            byte[] responseBytes = jsonResponse.getBytes("UTF-8");
            exchange.sendResponseHeaders(statusCode, responseBytes.length);
            OutputStream os = exchange.getResponseBody();
            os.write(responseBytes);
            os.close();
        }
    }

    // Handler 2: RESTful API danh sách sản phẩm
    static class ProductsHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            exchange.getResponseHeaders().add("Access-Control-Allow-Origin", "*");
            exchange.getResponseHeaders().add("Content-Type", "application/json; charset=UTF-8");

            String jsonResponse = "[\n" +
                "  { \"id\": \"SP01\", \"name\": \"Laptop Dell XPS 15\", \"price\": 35000000, \"quantity\": 5, \"category\": \"Laptop\" },\n" +
                "  { \"id\": \"SP02\", \"name\": \"Điện thoại iPhone 15 Pro\", \"price\": 28000000, \"quantity\": 10, \"category\": \"Điện thoại\" },\n" +
                "  { \"id\": \"SP03\", \"name\": \"Tai nghe Sony WH-1000XM5\", \"price\": 8500000, \"quantity\": 12, \"category\": \"Phụ kiện\" },\n" +
                "  { \"id\": \"SP04\", \"name\": \"Bàn phím cơ Keychron K2\", \"price\": 2100000, \"quantity\": 8, \"category\": \"Phụ kiện\" },\n" +
                "  { \"id\": \"SP05\", \"name\": \"Màn hình LG UltraGear 27 inch\", \"price\": 7900000, \"quantity\": 4, \"category\": \"Màn hình\" }\n" +
                "]";

            byte[] responseBytes = jsonResponse.getBytes("UTF-8");
            exchange.sendResponseHeaders(200, responseBytes.length);
            OutputStream os = exchange.getResponseBody();
            os.write(responseBytes);
            os.close();
        }
    }

    // Handler 3: Phục vụ các file WebContent
    static class StaticFileHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            String path = exchange.getRequestURI().getPath();
            if (path.equals("/")) {
                path = "/index.html";
            }

            File file = new File("WebContent" + path);
            if (!file.exists()) {
                file = new File("t2/WebContent" + path);
            }

            if (file.exists() && !file.isDirectory()) {
                String mime = "text/html";
                if (path.endsWith(".css")) mime = "text/css";
                else if (path.endsWith(".js")) mime = "application/javascript";
                else if (path.endsWith(".json")) mime = "application/json";

                exchange.getResponseHeaders().set("Content-Type", mime + "; charset=UTF-8");
                byte[] bytes = Files.readAllBytes(file.toPath());
                exchange.sendResponseHeaders(200, bytes.length);
                OutputStream os = exchange.getResponseBody();
                os.write(bytes);
                os.close();
            } else {
                String notFound = "<h1>404 Not Found</h1>";
                exchange.sendResponseHeaders(404, notFound.length());
                OutputStream os = exchange.getResponseBody();
                os.write(notFound.getBytes());
                os.close();
            }
        }
    }

    private static Map<String, String> parseQuery(String query) {
        Map<String, String> result = new HashMap<>();
        if (query == null || query.isEmpty()) return result;
        for (String param : query.split("&")) {
            String[] pair = param.split("=");
            if (pair.length > 1) {
                result.put(pair[0], pair[1]);
            } else if (pair.length == 1) {
                result.put(pair[0], "");
            }
        }
        return result;
    }
}
