package api;

import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpExchange;

import java.io.*;
import java.net.InetSocketAddress;
import java.nio.file.Files;

public class ServerB2 {
    private static final int PORT = 8082;

    public static void main(String[] args) throws IOException {
        HttpServer server = HttpServer.create(new InetSocketAddress(PORT), 0);

        // API Context
        server.createContext("/api/products", new HttpHandler() {
            @Override
            public void handle(HttpExchange exchange) throws IOException {
                exchange.getResponseHeaders().add("Access-Control-Allow-Origin", "*");
                exchange.getResponseHeaders().add("Content-Type", "application/json; charset=UTF-8");

                String jsonResponse = ProductServlet.getProductsJson();
                byte[] bytes = jsonResponse.getBytes("UTF-8");
                exchange.sendResponseHeaders(200, bytes.length);
                OutputStream os = exchange.getResponseBody();
                os.write(bytes);
                os.close();
            }
        });

        // Static Files Context
        server.createContext("/", new HttpHandler() {
            @Override
            public void handle(HttpExchange exchange) throws IOException {
                String path = exchange.getRequestURI().getPath();
                if (path.equals("/")) path = "/index.html";

                File file = new File("WebContent" + path);
                if (!file.exists()) file = new File("b2_products/WebContent" + path);

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
        System.out.println("=== DỰ ÁN BÀI 2 (DANH SÁCH SẢN PHẨM) ĐÃ CHẠY ===");
        System.out.println("Truy cap: http://localhost:" + PORT + "/index.html");
        server.start();
    }
}
