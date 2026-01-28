package Bai3_FindPrimes;

import java.io.*;
import java.net.*;
import java.util.*;
import java.util.stream.*;

public class Server {
    public static void main(String[] a) throws Exception {
        try (ServerSocket srv = new ServerSocket(3000)) {
            System.out.println("Server 3000");
            while (true) {
                try (Socket s = srv.accept();
                        BufferedReader r = new BufferedReader(new InputStreamReader(s.getInputStream()));
                        PrintWriter w = new PrintWriter(s.getOutputStream(), true)) {
                    String l = r.readLine();
                    if (l != null) {
                        try {
                            String res = Arrays.stream(l.split("[,\\s]+"))
                                    .map(String::trim).filter(x -> !x.isEmpty())
                                    .map(Integer::parseInt)
                                    .filter(n -> n > 1 && java.util.stream.IntStream.rangeClosed(2, (int) Math.sqrt(n))
                                            .noneMatch(i -> n % i == 0))
                                    .map(String::valueOf)
                                    .collect(Collectors.joining(", "));
                            w.println(res.isEmpty() ? "No primes" : res);
                        } catch (Exception e) {
                            w.println("Err: " + e);
                        }
                    }
                }
            }
        }
    }
}
