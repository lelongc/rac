package Bai2_SortNumbers;

import java.io.*;
import java.net.*;
import java.util.*;
import java.util.stream.Collectors;

public class Server {
    public static void main(String[] args) throws IOException {
        try (ServerSocket server = new ServerSocket(2001)) {
            System.out.println("Server running on 2001");
            while (true) {
                try (Socket socket = server.accept();
                        BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                        PrintWriter out = new PrintWriter(socket.getOutputStream(), true)) {
                    String line = in.readLine();
                    if (line != null) {
                        try {
                            // Split by comma OR space
                            String res = Arrays.stream(line.split("[ ,]+"))
                                    .map(String::trim)
                                    .filter(s -> !s.isEmpty())
                                    .map(Integer::parseInt)
                                    .sorted()
                                    .map(String::valueOf)
                                    .collect(Collectors.joining(", "));
                            out.println(res);
                        } catch (Exception e) {
                            out.println("Error: " + e.toString()); // Use toString for more info
                        }
                    }
                }
            }
        }
    }
}
