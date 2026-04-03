import java.io.*;
import java.net.Socket;
import java.util.*;

public class ThreadProcessSimple extends Thread {
    private final Socket socket;
    private final int clientId;

    public ThreadProcessSimple(Socket socket, int clientId) {
        this.socket = socket;
        this.clientId = clientId;
    }

    @Override
    public void run() {
        try (BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
             PrintWriter out = new PrintWriter(socket.getOutputStream(), true)) {
            out.println("Connected. Send data or EXIT.");
            String line;
            while ((line = in.readLine()) != null) {
                if ("EXIT".equalsIgnoreCase(line.trim())) {
                    out.println("Bye");
                    break;
                }
                out.println(processData(line));
            }
        } catch (Exception e) {
            System.out.println("Client #" + clientId + " error: " + e.getMessage());
        }
    }

    // ====================================================================
    // KHI THI: XOA HET CAC BAI KHONG CAN, GIU LAI BAI DANG LAM
    // ====================================================================
    public static String processData(String data) {
        try {
            String[] a = data.trim().split("[ ,\\s]+");
            
            // ========== BAI 1: Tam giac - Input: "a b c" (vd: 3 4 5) ==========
            if (a.length != 3) return "Nhap: a b c";
            double x = Double.parseDouble(a[0]), y = Double.parseDouble(a[1]), z = Double.parseDouble(a[2]);
            if (!(x > 0 && y > 0 && z > 0 && x + y > z && x + z > y && y + z > x)) return "Khong phai tam giac";
            double p = x + y + z;
            double s = Math.sqrt((p / 2) * (p / 2 - x) * (p / 2 - y) * (p / 2 - z));
            return String.format("Tam giac hop le | Chu vi=%.2f | Dien tich=%.2f", p, s);

            // ========== BAI 2: So phuc - Input: "op a b c d" (ADD/SUB/MUL/DIV a+bi c+di) ==========
            // if (a.length != 5) return "Nhap: op a b c d";
            // String op = a[0].toUpperCase();
            // double ar = Double.parseDouble(a[1]), ai = Double.parseDouble(a[2]);
            // double br = Double.parseDouble(a[3]), bi = Double.parseDouble(a[4]);
            // double rr = 0, ri = 0;
            // if (op.equals("ADD")) { rr = ar + br; ri = ai + bi; }
            // else if (op.equals("SUB")) { rr = ar - br; ri = ai - bi; }
            // else if (op.equals("MUL")) { rr = ar * br - ai * bi; ri = ar * bi + ai * br; }
            // else if (op.equals("DIV")) {
            //     double den = br * br + bi * bi;
            //     if (den == 0) return "Loi chia 0";
            //     rr = (ar * br + ai * bi) / den; ri = (ai * br - ar * bi) / den;
            // } else return "op chi ADD|SUB|MUL|DIV";
            // return String.format("%.4f%+.4fi", rr, ri);

            // ========== BAI 3: Fibonacci - Input: "n" (vd: 10) ==========
            // int n = Integer.parseInt(data.trim());
            // if (n < 0) return "n phai >= 0";
            // if (n == 0) return "0";
            // if (n == 1) return "1";
            // long fib_a = 0, fib_b = 1;
            // for (int i = 2; i <= n; i++) { long c = fib_a + fib_b; fib_a = fib_b; fib_b = c; }
            // return String.valueOf(fib_b);
            // // Muon in day: StringBuilder seq = new StringBuilder(); seq.append(fib_a);
            // // if (n >= 1) seq.append(", ").append(fib_b);
            // // for (...) { ... seq.append(", ").append(c); ... }
            // // return seq.toString();

            // ========== BAI 4: Quy doi tien te - Input: "amount from to" (100 USD VND) ==========
            // if (a.length != 3) return "Nhap: amount from to";
            // double amount = Double.parseDouble(a[0]);
            // String from = a[1].toUpperCase(), to = a[2].toUpperCase();
            // Map<String, Double> rate = new HashMap<>();
            // rate.put("VND", 1.0); rate.put("USD", 25000.0); rate.put("EUR", 27000.0); rate.put("JPY", 170.0);
            // if (!rate.containsKey(from) || !rate.containsKey(to)) return "Chi ho tro: VND USD EUR JPY";
            // double vnd = amount * rate.get(from);
            // return String.format("%.4f %s", vnd / rate.get(to), to);

            // ========== BAI 5: Nguyen to - Input: "n" ==========
            // long n = Long.parseLong(data.trim());
            // if (n < 2) return "Khong phai so nguyen to";
            // for (long i = 2; i * i <= n; i++) if (n % i == 0) return "Khong phai so nguyen to";
            // return "La so nguyen to";

            // ========== BAI 6: Sap xep tang dan - Input: "5,2,9,1" or "5 2 9 1" ==========
            // List<Double> list = new ArrayList<>();
            // for (String s : a) if (!s.isBlank()) list.add(Double.parseDouble(s.trim()));
            // Collections.sort(list);
            // return list.toString();

            // ========== BAI 7: Sap xep giam dan - Input: "5,2,9,1" ==========
            // List<Double> list = new ArrayList<>();
            // for (String s : a) if (!s.isBlank()) list.add(Double.parseDouble(s.trim()));
            // list.sort((x, y) -> Double.compare(y, x));
            // return list.toString();

            // ========== BAI 8: Thong ke tu - Input: "phat trien he thong phat trien" ==========
            // String[] w = data.toLowerCase().trim().split("\\s+");
            // Map<String, Integer> map = new LinkedHashMap<>();
            // for (String x : w) if (!x.isBlank()) map.put(x, map.getOrDefault(x, 0) + 1);
            // return map.toString();

            // ========== BAI 9: Sap xep chuoi - Input: "zebra,apple,cat" ==========
            // String[] arr = data.split(",");
            // List<String> list = new ArrayList<>();
            // for (String s : arr) list.add(s.trim());
            // Collections.sort(list);
            // return list.toString();

            // ========== BAI 10: Dao chuoi ==========
            // return new StringBuilder(data).reverse().toString();

            // ========== BAI 11: Ngat chuoi - Input: "a-b-c-d|-" ==========
            // String[] p = data.split("\\|", 2);
            // if (p.length != 2) return "Nhap: text|delimiter";
            // return Arrays.toString(p[0].split(java.util.regex.Pattern.quote(p[1])));

            // ========== BAI 12: UCLN BCNN - Input: "a b" (24 36) ==========
            // if (a.length != 2) return "Nhap: a b";
            // long x = Math.abs(Long.parseLong(a[0])), y = Math.abs(Long.parseLong(a[1]));
            // if (x == 0 && y == 0) return "UCLN=0, BCNN=0";
            // long g = gcd(x, y);
            // long l = (x == 0 || y == 0) ? 0 : (x / g) * y;
            // return "UCLN=" + g + ", BCNN=" + l;

            // ========== BAI 13: PT bac 1 - Input: "a b" => ax+b=0 ==========
            // if (a.length != 2) return "Nhap: a b";
            // double A = Double.parseDouble(a[0]), B = Double.parseDouble(a[1]);
            // if (A == 0 && B == 0) return "Vo so nghiem";
            // if (A == 0) return "Vo nghiem";
            // return String.format("x=%.6f", -B / A);

            // ========== BAI 14: PT bac 2 - Input: "a b c" => ax^2+bx+c=0 ==========
            // if (a.length != 3) return "Nhap: a b c";
            // double A = Double.parseDouble(a[0]), B = Double.parseDouble(a[1]), C = Double.parseDouble(a[2]);
            // if (A == 0) { // PT bac 1
            //     if (B == 0 && C == 0) return "Vo so nghiem";
            //     if (B == 0) return "Vo nghiem";
            //     return String.format("x=%.6f", -C / B);
            // }
            // double delta = B * B - 4 * A * C;
            // if (delta < 0) return "Vo nghiem thuc";
            // if (delta == 0) return String.format("x1=x2=%.6f", -B / (2 * A));
            // double x1 = (-B + Math.sqrt(delta)) / (2 * A);
            // double x2 = (-B - Math.sqrt(delta)) / (2 * A);
            // return String.format("x1=%.6f, x2=%.6f", x1, x2);

            // ========== BAI 15: Tong 1..n - Input: "n" ==========
            // long n = Long.parseLong(data.trim());
            // if (n < 0) return "n phai >= 0";
            // return String.valueOf(n * (n + 1) / 2);

            // ========== BAI 16: Dem nguyen am phu am - Input: "mot chuoi" ==========
            // int vowel = 0, consonant = 0;
            // String s = data.toLowerCase();
            // for (char c : s.toCharArray()) {
            //     if (c >= 'a' && c <= 'z') {
            //         if ("aeiou".indexOf(c) >= 0) vowel++; else consonant++;
            //     }
            // }
            // return "NguyenAm=" + vowel + ", PhuAm=" + consonant;

            // ========== BAI 17: Chuan hoa chuoi - Input: "  phat  trien HE thong  " ==========
            // String[] w = data.trim().toLowerCase().split("\\s+");
            // StringBuilder sb = new StringBuilder();
            // for (String word : w) if (!word.isBlank()) {
            //     sb.append(Character.toUpperCase(word.charAt(0))).append(word.substring(1)).append(' ');
            // }
            // return sb.toString().trim();

            // ========== BAI 18: Palindrome - Input: "racecar" ==========
            // String s = data.replaceAll("\\s+", "").toLowerCase();
            // String r = new StringBuilder(s).reverse().toString();
            // return s.equals(r) ? "Palindrome" : "Khong palindrome";

            // ========== BAI 19: Giai thua - Input: "n" ==========
            // int n = Integer.parseInt(data.trim());
            // if (n < 0) return "n phai >= 0";
            // long f = 1;
            // for (int i = 2; i <= n; i++) f *= i;
            // return String.valueOf(f);

            // ========== BAI 20: Tong chu so - Input: "12345" ==========
            // String s = data.trim();
            // int sum = 0;
            // for (char c : s.toCharArray()) {
            //     if (Character.isDigit(c)) sum += c - '0';
            //     else if (c != '-') return "Chi nhap so nguyen";
            // }
            // return String.valueOf(sum);

            // ========== BAI 21: Tong danh sach so - Input: "1,2,3,4,5" ==========
            // List<Double> list = new ArrayList<>();
            // for (String s : a) if (!s.isBlank()) list.add(Double.parseDouble(s.trim()));
            // double sum = 0;
            // for (double num : list) sum += num;
            // return String.format("Tong=%.4f", sum);

            // ========== BAI 22: Min Max - Input: "5,2,9,1" ==========
            // List<Double> list = new ArrayList<>();
            // for (String s : a) if (!s.isBlank()) list.add(Double.parseDouble(s.trim()));
            // if (list.isEmpty()) return "Danh sach rong";
            // double min = list.get(0), max = list.get(0);
            // for (double num : list) { if (num < min) min = num; if (num > max) max = num; }
            // return String.format("Min=%.4f, Max=%.4f", min, max);

            // ========== BAI 23: Chan le - Input: "n" ==========
            // long n = Long.parseLong(data.trim());
            // return (n % 2 == 0) ? "So chan" : "So le";

            // ========== BAI 24: In hoa ==========
            // return data.toUpperCase();

            // ========== BAI 25: In thuong ==========
            // return data.toLowerCase();

            // ========== BAI 26: Dem ky tu - Input: "abc de" ==========
            // int all = data.length();
            // int noSpace = data.replace(" ", "").length();
            // return "TongKyTu=" + all + ", KhongTinhSpace=" + noSpace;

            // ========== BAI 27: Dien tich HCN - Input: "width height" or "3,4" ==========
            // if (a.length != 2) return "Nhap: width height";
            // double w = Double.parseDouble(a[0]), h = Double.parseDouble(a[1]);
            // return String.format("Dien tich HCN=%.4f", w * h);

            // ========== BAI 28: Dien tich hinh tron - Input: "r" (vd: 3) ==========
            // double r = Double.parseDouble(data.trim());
            // if (r < 0) return "Ban kinh phai >= 0";
            // return String.format("Dien tich hinh tron=%.4f", Math.PI * r * r);

            // ========== BAI 29: Dien tich hinh thang - Input: "a b h" (vd: 3 4 5) ==========
            // if (a.length != 3) return "Nhap: a b h";
            // double A = Double.parseDouble(a[0]), B = Double.parseDouble(a[1]), H = Double.parseDouble(a[2]);
            // if (H < 0) return "Chieu cao phai >= 0";
            // return String.format("Dien tich hinh thang=%.4f", (A + B) * H / 2.0);

            // ========== BAI 30: Chu vi hinh vuong - Input: "side" (vd: 4) ==========
            // double side = Double.parseDouble(data.trim());
            // return String.format("Chu vi hinh vuong=%.4f", 4 * side);

            // ========== BAI 31: Chu vi HCN - Input: "width height" (vd: 3 4) ==========
            // if (a.length != 2) return "Nhap: width height";
            // double w = Double.parseDouble(a[0]), h = Double.parseDouble(a[1]);
            // return String.format("Chu vi HCN=%.4f", 2 * (w + h));

        } catch (Exception e) {
            return "Loi: " + e.getMessage();
        }
    }

    // Helper: UCLN (chi can cho bai 12)
    static long gcd(long a, long b) {
        while (b != 0) { long t = a % b; a = b; b = t; }
        return Math.abs(a);
    }
}
