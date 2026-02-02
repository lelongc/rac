package Bai4_WordCount;
import java.io.*; import java.net.*; import java.util.*; import java.util.stream.*;

public class Server {
    public static void main(String[] a) throws Exception {
        try (ServerSocket srv = new ServerSocket(4000)) {
            System.out.println("Server 4000");
            while (true) {
                try (Socket s = srv.accept();
                     BufferedReader r = new BufferedReader(new InputStreamReader(s.getInputStream()));
                     PrintWriter w = new PrintWriter(s.getOutputStream(), true)) {
                    String l = r.readLine();
                    if (l != null) {
                        try {
                            String res = Arrays.stream(l.trim().split("[\\s,.]+")) // Tach bang khoang trang, phay, cham
                                .filter(s1 -> !s1.isEmpty())
                                .map(String::toLowerCase)
                                .collect(Collectors.groupingBy(k -> k, Collectors.counting()))
                                .toString();
                            w.println(res);
                        } catch (Exception e) { w.println("Err: " + e); }
                    }
                }
            }
        }
    }
}
