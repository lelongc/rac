package api;

import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpExchange;

import java.io.*;
import java.net.InetSocketAddress;
import java.net.URI;
import java.nio.file.Files;
import java.util.HashMap;
import java.util.Map;

public class ServerB3 {
    private static final int PORT = 8083;

    public static void main(String[] args) throws IOException {
        HttpServer server = HttpServer.create(new InetSocketAddress(PORT), 0);

        // RESTful API Endpoint xử lý cả 4 phương thức HTTP: GET, POST, PUT, DELETE
        server.createContext("/api/products", new HttpHandler() {
            @Override
            public void handle(HttpExchange exchange) throws IOException {
                // Thiết lập Header CORS đầy đủ cho Postman & Fetch Call
                exchange.getResponseHeaders().add("Access-Control-Allow-Origin", "*");
                exchange.getResponseHeaders().add("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS");
                exchange.getResponseHeaders().add("Access-Control-Allow-Headers", "Content-Type, Authorization");
                exchange.getResponseHeaders().add("Content-Type", "application/json; charset=UTF-8");

                String method = exchange.getRequestMethod();

                if ("OPTIONS".equalsIgnoreCase(method)) {
                    exchange.sendResponseHeaders(204, -1);
                    return;
                }

                URI requestURI = exchange.getRequestURI();
                Map<String, String> queryParams = parseQuery(requestURI.getQuery());

                // Đọc dữ liệu Body (dành cho POST / PUT)
                String bodyText = readRequestBody(exchange.getRequestBody());
                Map<String, String> bodyParams = parseQuery(bodyText);

                String id = queryParams.getOrDefault("id", bodyParams.get("id"));
                String responseJson;

                switch (method.toUpperCase()) {
                    case "GET":
                        if (id != null && !id.isEmpty()) {
                            responseJson = ProductService.getByIdAsJson(id);
                        } else {
                            responseJson = ProductService.getAllAsJson();
                        }
                        break;

                    case "POST":
                        String pName = bodyParams.getOrDefault("name", queryParams.get("name"));
                        double pPrice = parseDouble(bodyParams.getOrDefault("price", queryParams.get("price")));
                        int pQty = parseInt(bodyParams.getOrDefault("quantity", queryParams.get("quantity")));
                        String pCat = bodyParams.getOrDefault("category", queryParams.get("category"));

                        responseJson = ProductService.addProduct(id, pName, pPrice, pQty, pCat);
                        break;

                    case "PUT":
                        String uName = bodyParams.getOrDefault("name", queryParams.get("name"));
                        double uPrice = parseDouble(bodyParams.getOrDefault("price", queryParams.get("price")));
                        int uQty = parseInt(bodyParams.getOrDefault("quantity", queryParams.get("quantity")));
                        String uCat = bodyParams.getOrDefault("category", queryParams.get("category"));

                        responseJson = ProductService.updateProduct(id, uName, uPrice, uQty, uCat);
                        break;

                    case "DELETE":
                        responseJson = ProductService.deleteProduct(id);
                        break;

                    default:
                        responseJson = "{\"status\":\"error\",\"message\":\"Method not supported\"}";
                        break;
                }

                byte[] bytes = responseJson.getBytes("UTF-8");
                exchange.sendResponseHeaders(200, bytes.length);
                OutputStream os = exchange.getResponseBody();
                os.write(bytes);
                os.close();
            }
        });

        // Serves WebContent files (HTML, CSS, JS)
        server.createContext("/", new HttpHandler() {
            @Override
            public void handle(HttpExchange exchange) throws IOException {
                String path = exchange.getRequestURI().getPath();
                if (path.equals("/")) path = "/index.html";

                File file = new File("WebContent" + path);
                if (!file.exists()) file = new File("b3_rest_crud/WebContent" + path);

                if (file.exists() && !file.isDirectory()) {
                    String mime = "text/html";
                    if (path.endsWith(".css")) mime = "text/css";
                    else if (path.endsWith(".js")) mime = "application/javascript";

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
        });

        server.setExecutor(null);
        System.out.println("=== RESTFUL API SERVER (GET, POST, PUT, DELETE) DA KHỞI ĐỘNG ===");
        System.out.println("Giao dien test tren Trinh duyet: http://localhost:" + PORT + "/index.html");
        System.out.println("REST API Endpoint cho Postman: http://localhost:" + PORT + "/api/products");
        server.start();
    }

    private static String readRequestBody(InputStream is) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(is, "UTF-8"));
        StringBuilder sb = new StringBuilder();
        String line;
        while ((line = br.readLine()) != null) {
            sb.append(line);
        }
        return sb.toString();
    }

    private static Map<String, String> parseQuery(String query) {
        Map<String, String> result = new HashMap<>();
        if (query == null || query.isEmpty()) return result;
        for (String param : query.split("&")) {
            String[] pair = param.split("=");
            if (pair.length > 1) {
                try {
                    result.put(pair[0], java.net.URLDecoder.decode(pair[1], "UTF-8"));
                } catch (Exception e) {
                    result.put(pair[0], pair[1]);
                }
            } else if (pair.length == 1) {
                result.put(pair[0], "");
            }
        }
        return result;
    }

    private static double parseDouble(String str) {
        if (str == null || str.isEmpty()) return 0;
        try { return Double.parseDouble(str); } catch (Exception e) { return 0; }
    }

    private static int parseInt(String str) {
        if (str == null || str.isEmpty()) return 0;
        try { return Integer.parseInt(str); } catch (Exception e) { return 0; }
    }
}
