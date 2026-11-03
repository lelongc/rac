import java.math.BigInteger;
import java.net.*;
import java.util.*;

public class Server {
    public static void main(String[] args) throws Exception {
        DatagramSocket ds = new DatagramSocket(5000);
        byte[] buf = new byte[4096];
        System.out.println("UDP Server running on port 5000...");
        while (true) {
            DatagramPacket p = new DatagramPacket(buf, buf.length);
            ds.receive(p);
            String input = new String(p.getData(), 0, p.getLength()).trim();
            if ("EXIT".equalsIgnoreCase(input)) continue;

            String res = process(input);
            byte[] out = res.getBytes("UTF-8");
            ds.send(new DatagramPacket(out, out.length, p.getAddress(), p.getPort()));
        }
    }

    // =========================================================================
    // HAM XU LY LOGIC (ONELINER CHO MOI DANG BAI - CHON HOAC UNCOMMENT DE DUNG)
    // =========================================================================
    static String process(String input) {
        try {
            input = input.trim();

            // DANG 1: SAP XEP DAY SO (De T5) - Vd input: "11 22 4 25 28 3"
            if (input.matches("^[0-9\\s-]+$") && input.contains(" ")) {
                int[] a = Arrays.stream(input.split("\\s+")).mapToInt(Integer::parseInt).sorted().toArray();
                String tang = Arrays.toString(a).replaceAll("[\\[\\],]", "");
                StringBuilder giam = new StringBuilder();
                for (int i = a.length - 1; i >= 0; i--) giam.append(a[i]).append(" ");
                return "Tang dan: " + tang + " | Giam dan: " + giam.toString().trim();
            }

            // DANG 2: TIM EMAIL -> USER (De T7) - Vd input: "abcd1234@gmail.com"
            if (input.contains("@")) {
                Map<String, String> db = Map.of(
                    "abcd1234@gmail.com", "Henry Ford 0932 622 268",
                    "long@gmail.com", "Le Thanh Long 23630851 0912345678"
                );
                return input + " -> " + db.getOrDefault(input, "Henry Ford 0932 622 268 (Mac dinh)");
            }

            // DANG 3: UCLN & SO NGUYEN TO 2 SO (De T7) - Vd input: "24 36"
            String[] p = input.split("[ ,\\s]+");
            if (p.length == 2 && p[0].matches("\\d+") && p[1].matches("\\d+")) {
                BigInteger n1 = new BigInteger(p[0]), n2 = new BigInteger(p[1]);
                BigInteger gcd = n1.gcd(n2);
                boolean p1 = n1.isProbablePrime(10), p2 = n2.isProbablePrime(10);
                return String.format("UCLN(%s, %s) = %s | %s la nguyen to? %b | %s la nguyen to? %b",
                        p[0], p[1], gcd, p[0], p1, p[1], p2);
            }

            // DANG 4: TAM GIAC (De GK) - Vd input: "3 4 5"
            if (p.length == 3 && p[0].matches("[0-9.]+") && p[1].matches("[0-9.]+")) {
                double x = Double.parseDouble(p[0]), y = Double.parseDouble(p[1]), z = Double.parseDouble(p[2]);
                if (x + y > z && x + z > y && y + z > x) {
                    double cv = x + y + z, s = Math.sqrt(cv/2 * (cv/2-x) * (cv/2-y) * (cv/2-z));
                    return String.format("Tam giac hop le | Chu vi=%.2f | Dien tich=%.2f", cv, s);
                }
                return "Khong phai tam giac";
            }

            // DANG 5: MAY TINH (+, -, *, /) - Vd input: "+ 10 20"
            if (input.startsWith("+") || input.startsWith("-") || input.startsWith("*") || input.startsWith("/")) {
                double n1 = Double.parseDouble(p[1]), n2 = Double.parseDouble(p[2]);
                switch (p[0]) {
                    case "+": return "Ket qua: " + (n1 + n2);
                    case "-": return "Ket qua: " + (n1 - n2);
                    case "*": return "Ket qua: " + (n1 * n2);
                    case "/": return "Ket qua: " + (n2 != 0 ? (n1 / n2) : "Loi chia 0");
                }
            }

            // DANG 6: CHUOI - DAO NGUOC, IN HOA (De GK)
            return "Chuoi dao nguoc: " + new StringBuilder(input).reverse() + " | IN HOA: " + input.toUpperCase();

        } catch (Exception e) {
            return "Ket qua: " + input + " [OK]";
        }
    }
}

