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

public class ServerB1 {
    private static final int PORT = 8081;

    public static void main(String[] args) throws IOException {
        HttpServer server = HttpServer.create(new InetSocketAddress(PORT), 0);

        // API Context
        server.createContext("/api/convert", new HttpHandler() {
            @Override
            public void handle(HttpExchange exchange) throws IOException {
                exchange.getResponseHeaders().add("Access-Control-Allow-Origin", "*");
                exchange.getResponseHeaders().add("Content-Type", "application/json; charset=UTF-8");

                URI requestURI = exchange.getRequestURI();
                Map<String, String> params = parseQuery(requestURI.getQuery());

                String jsonResponse = CurrencyServlet.processRequest(
                    params.get("amount"), params.get("from"), params.get("to")
                );

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
                if (!file.exists()) file = new File("b1_currency/WebContent" + path);

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
        System.out.println("=== DỰ ÁN BÀI 1 (QUY ĐỔI TIỀN TỆ) ĐÃ CHẠY ===");
        System.out.println("Truy cap: http://localhost:" + PORT + "/index.html");
        server.start();
    }

    private static Map<String, String> parseQuery(String query) {
        Map<String, String> result = new HashMap<>();
        if (query == null || query.isEmpty()) return result;
        for (String param : query.split("&")) {
            String[] pair = param.split("=");
            if (pair.length > 1) result.put(pair[0], pair[1]);
        }
        return result;
    }
}
