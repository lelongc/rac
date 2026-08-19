package api;

import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpServer;

import java.io.*;
import java.net.InetSocketAddress;
import java.net.URLDecoder;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.atomic.AtomicInteger;

/**
 * Server chay tai cong 8084 cho bai 4 (App quang cao san pham ket noi Virtual RESTful API)
 */
public class ServerB4 {

    private static final int PORT = 8084;
    private static final Map<Integer, LocalProduct> db = new ConcurrentHashMap<>();
    private static final AtomicInteger idCounter = new AtomicInteger(100);

    // Lop san pham local
    public static class LocalProduct {
        public int id;
        public String title;
        public double price;
        public String description;
        public String category;
        public String image;

        public LocalProduct(int id, String title, double price, String description, String category, String image) {
            this.id = id;
            this.title = title;
            this.price = price;
            this.description = description;
            this.category = category;
            this.image = image;
        }

        public String toJson() {
            return String.format(
                "{\"id\":%d,\"title\":\"%s\",\"price\":%.2f,\"description\":\"%s\",\"category\":\"%s\",\"image\":\"%s\"}",
                id, escape(title), price, escape(description), escape(category), escape(image)
            );
        }

        private String escape(String s) {
            if (s == null) return "";
            return s.replace("\\", "\\\\").replace("\"", "\\\"").replace("\n", " ");
        }
    }

    // Khoi tao du lieu mau co anh thuc te
    static {
        db.put(1, new LocalProduct(1, "Laptop Gaming ASUS ROG Zephyrus G14", 32990000, "Man hinh 14 inch QHD 165Hz, Ryzen 9, RTX 4060, sieu mong nhe.", "Electronics", "https://images.unsplash.com/photo-1603302576837-37561b2e2302?w=500&q=80"));
        db.put(2, new LocalProduct(2, "Apple iPhone 15 Pro Max 256GB Titan", 29490000, "Chip A17 Pro khung vien Titan sang trong, camera 5x zoom quang hoc.", "Electronics", "https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=500&q=80"));
        db.put(3, new LocalProduct(3, "Tai nghe chong on Sony WH-1000XM5", 6890000, "Cong nghe chong on dinh cao, thoi luong pin 30 gio lien tuc.", "Accessories", "https://images.unsplash.com/photo-1546435770-a3e426bf472b?w=500&q=80"));
        db.put(4, new LocalProduct(4, "Dong ho thoi trang Nam Seiko Automatic", 5200000, "Mat kinh Sapphire, bo may co Nhat Ban ben bi, chong nuoc 100m.", "Jewelry", "https://images.unsplash.com/photo-1524805444758-089113d48a6d?w=500&q=80"));
        db.put(5, new LocalProduct(5, "Ao khoac Bomber Nam Classic Jacket", 850000, "Chat lieu vai du 2 lop chong nuoc nhe, phong cach tre trung.", "Fashion", "https://images.unsplash.com/photo-1551028719-00167b16eac5?w=500&q=80"));
        db.put(6, new LocalProduct(6, "Giay Sneaker The Thao Nike Air Max", 3190000, "Dem khi Air Max em ai, thiet ke thoi thuong danh cho gioi tre.", "Fashion", "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500&q=80"));
    }

    public static void main(String[] args) throws IOException {
        HttpServer server = HttpServer.create(new InetSocketAddress(PORT), 0);

        // 1. Static Web Content Handler
        server.createContext("/", new StaticHandler());

        // 2. Local RESTful API Handler
        server.createContext("/api/products", new LocalApiHandler());

        server.setExecutor(null);
        server.start();

        System.out.println("=================================================");
        System.out.println("  SERVER B4 (APP QUANG CAO SAN PHAM VIRTUAL API)  ");
        System.out.println("  Mo trinh duyet truy cap:                       ");
        System.out.println("  👉 http://localhost:" + PORT + "/index.html     ");
        System.out.println("  Endpoint Local API:                            ");
        System.out.println("  👉 http://localhost:" + PORT + "/api/products  ");
        System.out.println("=================================================");
    }

    // Static Handler tra ve file HTML/CSS/JS tu thu muc WebContent
    static class StaticHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            String path = exchange.getRequestURI().getPath();
            if (path.equals("/") || path.isEmpty()) {
                path = "/index.html";
            }

            File file = new File("WebContent" + path);
            if (!file.exists() || file.isDirectory()) {
                file = new File("b4_product_ads/WebContent" + path);
            }

            if (file.exists() && !file.isDirectory()) {
                String contentType = "text/html; charset=UTF-8";
                if (path.endsWith(".css")) contentType = "text/css; charset=UTF-8";
                else if (path.endsWith(".js")) contentType = "application/javascript; charset=UTF-8";
                else if (path.endsWith(".json")) contentType = "application/json; charset=UTF-8";
                else if (path.endsWith(".png")) contentType = "image/png";
                else if (path.endsWith(".jpg") || path.endsWith(".jpeg")) contentType = "image/jpeg";

                byte[] bytes = Files.readAllBytes(file.toPath());
                exchange.getResponseHeaders().set("Content-Type", contentType);
                exchange.getResponseHeaders().set("Access-Control-Allow-Origin", "*");
                exchange.sendResponseHeaders(200, bytes.length);
                try (OutputStream os = exchange.getResponseBody()) {
                    os.write(bytes);
                }
            } else {
                String notFound = "<h1>404 Not Found</h1><p>Khong tim thay file: " + path + "</p>";
                byte[] bytes = notFound.getBytes(StandardCharsets.UTF_8);
                exchange.getResponseHeaders().set("Content-Type", "text/html; charset=UTF-8");
                exchange.sendResponseHeaders(404, bytes.length);
                try (OutputStream os = exchange.getResponseBody()) {
                    os.write(bytes);
                }
            }
        }
    }

    // Local API Handler tra ve RESTful API
    static class LocalApiHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            String method = exchange.getRequestMethod().toUpperCase();

            // Set CORS headers
            exchange.getResponseHeaders().set("Access-Control-Allow-Origin", "*");
            exchange.getResponseHeaders().set("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS");
            exchange.getResponseHeaders().set("Access-Control-Allow-Headers", "Content-Type, Authorization");
            exchange.getResponseHeaders().set("Content-Type", "application/json; charset=UTF-8");

            if ("OPTIONS".equals(method)) {
                exchange.sendResponseHeaders(204, -1);
                return;
            }

            String query = exchange.getRequestURI().getQuery();
            Map<String, String> queryParams = parseParams(query);

            String responseJson = "{}";
            int statusCode = 200;

            if ("GET".equals(method)) {
                if (queryParams.containsKey("id")) {
                    try {
                        int id = Integer.parseInt(queryParams.get("id"));
                        LocalProduct p = db.get(id);
                        if (p != null) {
                            responseJson = p.toJson();
                        } else {
                            statusCode = 404;
                            responseJson = "{\"status\":\"error\",\"message\":\"Khong tim thay san pham ID=" + id + "\"}";
                        }
                    } catch (Exception e) {
                        statusCode = 400;
                        responseJson = "{\"status\":\"error\",\"message\":\"ID khong hop le\"}";
                    }
                } else {
                    StringBuilder sb = new StringBuilder("[");
                    int i = 0;
                    for (LocalProduct p : db.values()) {
                        if (i > 0) sb.append(",");
                        sb.append(p.toJson());
                        i++;
                    }
                    sb.append("]");
                    responseJson = sb.toString();
                }
            } else if ("POST".equals(method)) {
                String body = readBody(exchange.getRequestBody());
                Map<String, String> postParams = parseParams(body);
                if (postParams.isEmpty()) postParams = queryParams;

                String title = postParams.getOrDefault("title", "San pham moi");
                double price = parseDouble(postParams.get("price"), 100000);
                String desc = postParams.getOrDefault("description", "Mo ta san pham");
                String cat = postParams.getOrDefault("category", "General");
                String img = postParams.getOrDefault("image", "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500&q=80");

                int newId = idCounter.incrementAndGet();
                LocalProduct np = new LocalProduct(newId, title, price, desc, cat, img);
                db.put(newId, np);

                statusCode = 201;
                responseJson = String.format("{\"status\":\"success\",\"message\":\"Them san pham thanh cong\",\"product\":%s}", np.toJson());
            } else if ("PUT".equals(method)) {
                String body = readBody(exchange.getRequestBody());
                Map<String, String> putParams = parseParams(body);
                putParams.putAll(queryParams);

                int id = parseInt(putParams.get("id"), -1);
                if (id != -1 && db.containsKey(id)) {
                    LocalProduct p = db.get(id);
                    if (putParams.containsKey("title")) p.title = putParams.get("title");
                    if (putParams.containsKey("price")) p.price = parseDouble(putParams.get("price"), p.price);
                    if (putParams.containsKey("description")) p.description = putParams.get("description");
                    if (putParams.containsKey("category")) p.category = putParams.get("category");
                    if (putParams.containsKey("image")) p.image = putParams.get("image");

                    responseJson = String.format("{\"status\":\"success\",\"message\":\"Cap nhat san pham ID=%d thanh cong\",\"product\":%s}", id, p.toJson());
                } else {
                    statusCode = 404;
                    responseJson = "{\"status\":\"error\",\"message\":\"Khong tim thay san pham can cap nhat\"}";
                }
            } else if ("DELETE".equals(method)) {
                int id = parseInt(queryParams.get("id"), -1);
                if (id != -1 && db.containsKey(id)) {
                    db.remove(id);
                    responseJson = String.format("{\"status\":\"success\",\"message\":\"Xoa san pham ID=%d thanh cong\"}", id);
                } else {
                    statusCode = 404;
                    responseJson = "{\"status\":\"error\",\"message\":\"Khong tim thay san pham can xoa\"}";
                }
            }

            byte[] bytes = responseJson.getBytes(StandardCharsets.UTF_8);
            exchange.sendResponseHeaders(statusCode, bytes.length);
            try (OutputStream os = exchange.getResponseBody()) {
                os.write(bytes);
            }
        }

        private Map<String, String> parseParams(String data) {
            Map<String, String> map = new HashMap<>();
            if (data == null || data.trim().isEmpty()) return map;
            String[] pairs = data.split("&");
            for (String pair : pairs) {
                String[] kv = pair.split("=", 2);
                if (kv.length == 2) {
                    try {
                        String k = URLDecoder.decode(kv[0], StandardCharsets.UTF_8.name());
                        String v = URLDecoder.decode(kv[1], StandardCharsets.UTF_8.name());
                        map.put(k, v);
                    } catch (Exception ignored) {}
                }
            }
            return map;
        }

        private String readBody(InputStream is) throws IOException {
            BufferedReader reader = new BufferedReader(new InputStreamReader(is, StandardCharsets.UTF_8));
            StringBuilder sb = new StringBuilder();
            String line;
            while ((line = reader.readLine()) != null) {
                sb.append(line);
            }
            return sb.toString();
        }

        private int parseInt(String s, int def) {
            try { return Integer.parseInt(s); } catch (Exception e) { return def; }
        }

        private double parseDouble(String s, double def) {
            try { return Double.parseDouble(s); } catch (Exception e) { return def; }
        }
    }
}
