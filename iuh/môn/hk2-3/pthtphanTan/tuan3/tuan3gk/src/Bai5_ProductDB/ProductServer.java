package Bai5_ProductDB;

import java.io.*;
import java.net.*;

public class ProductServer {
    public static void main(String[] args) throws Exception {
        try (ServerSocket srv = new ServerSocket(6123)) {
            System.out.println("TCP Server: 6123");
            while (true) {
                try (Socket s = srv.accept();
                        BufferedReader r = new BufferedReader(new InputStreamReader(s.getInputStream()));
                        PrintWriter w = new PrintWriter(s.getOutputStream(), true)) {
                    String q = r.readLine();
                    if (q != null) {
                        Product p = DatabaseUtils.find(q);
                        w.println(p != null ? p.toString() : "Not found: " + q);
                    }
                }
            }
        }
    }
}
