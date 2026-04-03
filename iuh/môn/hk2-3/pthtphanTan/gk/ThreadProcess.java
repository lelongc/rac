import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.*;

public class ThreadProcess extends Thread {
    private final Socket socket;
    private final int clientId;

    public ThreadProcess(Socket socket, int clientId) {
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

    // ==========================================================
    // CHON 1 BAI DUY NHAT: COMMENT / UNCOMMENT 1 DONG DUOI DAY
    // -------- NHOM SO --------
    // 1,2,3,4,5,6,7,12,13,14,15,19,20,21,22,23,27,28,29,30,31
    // -------- NHOM CHUOI --------
    // 8,9,10,11,16,17,18,24,25,26
    // ==========================================================
    public static String processData(String data) {
        // ===== NHOM SO =====
        // return triangleMetrics(data);
        // return complexArithmetic(data);                 // + - * /
        // return fibonacciValue(data);
        // return currencyConvert(data);
        // return primeCheck(data);
        // return sortNumbersAsc(data);
        // return sortNumbersDesc(data);
        // return wordFrequency(data);
        // return sortStringsAsc(data);
        // return reverseText(data);
        // return splitTextByDelimiter(data);
        // return gcdLcm(data);
        // return solveLinearEquation(data);
        // return solveQuadraticEquation(data);
        // return sumOneToN(data);
        // return factorialValue(data);
        // return sumDigits(data);
        // return sumNumberList(data);
        // return minMaxNumberList(data);
        // return evenOddCheck(data);
        // ===== THEM CAC BAI HINH HOC =====
        // return areaRectangle(data);      // Input: "width height" or "width,height"
        // return areaCircle(data);         // Input: "radius"
        // return areaTrapezoid(data);      // Input: "a b h"
        // return perimeterSquare(data);   // Input: "side"
        // return perimeterRectangle(data);// Input: "width height"

        // ===== NHOM CHUOI =====
        // return wordFrequency(data);
        // return sortStringsAsc(data);
        return reverseText(data);                 // mac dinh
        // return splitTextByDelimiter(data);
        // return countVowelsConsonants(data);
        // return normalizeText(data);
        // return palindromeCheck(data);
        // return toUpperCaseText(data);
        // return toLowerCaseText(data);
        // return countCharacters(data);
    }

    // ===== BAI 1: Tam giac =====
    // Input: "a b c"  (vd: 3 4 5)
    static String triangleMetrics(String data) {
        try {
            String[] a = data.trim().split("\\s+");
            if (a.length != 3) return "Nhap: a b c";
            double x = Double.parseDouble(a[0]);
            double y = Double.parseDouble(a[1]);
            double z = Double.parseDouble(a[2]);
            if (!(x > 0 && y > 0 && z > 0 && x + y > z && x + z > y && y + z > x)) return "Khong phai tam giac";
            double p = x + y + z;
            double s = Math.sqrt((p / 2) * (p / 2 - x) * (p / 2 - y) * (p / 2 - z));
            return String.format("Tam giac hop le | Chu vi=%.2f | Dien tich=%.2f", p, s);
        } catch (Exception e) {
            return "Nhap sai dinh dang so";
        }
    }

    // ===== BAI 2: So phuc (+ - * /) =====
    // Input: "op a b c d"  (op=ADD|SUB|MUL|DIV ; z1=a+bi, z2=c+di)
    static String complexArithmetic(String data) {
        try {
            String[] a = data.trim().split("\\s+");
            if (a.length != 5) return "Nhap: op a b c d";
            String op = a[0].toUpperCase();
            double ar = Double.parseDouble(a[1]), ai = Double.parseDouble(a[2]);
            double br = Double.parseDouble(a[3]), bi = Double.parseDouble(a[4]);
            double rr, ri;
            switch (op) {
                case "ADD": rr = ar + br; ri = ai + bi; break;
                case "SUB": rr = ar - br; ri = ai - bi; break;
                case "MUL": rr = ar * br - ai * bi; ri = ar * bi + ai * br; break;
                case "DIV":
                    double den = br * br + bi * bi;
                    if (den == 0) return "Loi chia 0";
                    rr = (ar * br + ai * bi) / den;
                    ri = (ai * br - ar * bi) / den;
                    break;
                default: return "op chi ADD|SUB|MUL|DIV";
            }
            return String.format("%.4f%+.4fi", rr, ri);
        } catch (Exception e) {
            return "Nhap sai dinh dang so";
        }
    }

    // ===== BAI 3: Fibonacci =====
    // Input: "n"  (vd: 10)
    static String fibonacciValue(String data) {
        try {
            int n = Integer.parseInt(data.trim());
            if (n < 0) return "n phai >= 0";
            if (n == 0) return "0";
            if (n == 1) return "1";
            
            // ===== UNCOMMENT DONG DUOI DE IN RA DAY SO FIBONACCI TU 0 DEN N =====
            // StringBuilder sequence = new StringBuilder();
            // long a = 0, b = 1;
            // sequence.append(a);
            // if (n >= 1) sequence.append(", ").append(b);
            // for (int i = 2; i <= n; i++) {
            //     long c = a + b;
            //     sequence.append(", ").append(c);
            //     a = b;
            //     b = c;
            // }
            // return "Day Fibonacci: " + sequence.toString();
            // ===================================================================
            
            long a = 0, b = 1;
            for (int i = 2; i <= n; i++) {
                long c = a + b;
                a = b;
                b = c;
            }
            return String.valueOf(b);
        } catch (Exception e) {
            return "Nhap sai dinh dang so";
        }
    }

    // ===== BAI 4: Quy doi tien te =====
    // Input: "amount from to"  (vd: 100 USD VND)
    static String currencyConvert(String data) {
        try {
            String[] a = data.trim().split("\\s+");
            if (a.length != 3) return "Nhap: amount from to";
            double amount = Double.parseDouble(a[0]);
            String from = a[1].toUpperCase(), to = a[2].toUpperCase();
            Map<String, Double> rate = new HashMap<>();
            rate.put("VND", 1.0);
            rate.put("USD", 25000.0);
            rate.put("EUR", 27000.0);
            rate.put("JPY", 170.0);
            if (!rate.containsKey(from) || !rate.containsKey(to)) return "Chi ho tro: VND USD EUR JPY";
            double vnd = amount * rate.get(from);
            return String.format("%.4f %s", vnd / rate.get(to), to);
        } catch (Exception e) {
            return "Nhap sai dinh dang";
        }
    }

    // ===== BAI 5: Nguyen to =====
    // Input: "n"
    static String primeCheck(String data) {
        try {
            long n = Long.parseLong(data.trim());
            if (n < 2) return "Khong phai so nguyen to";
            for (long i = 2; i * i <= n; i++) if (n % i == 0) return "Khong phai so nguyen to";
            return "La so nguyen to";
        } catch (Exception e) {
            return "Nhap sai dinh dang so";
        }
    }

    // ===== BAI 6: Sap xep tang dan (so) =====
    // Input: "5,2,9,1"
    static String sortNumbersAsc(String data) {
        List<Double> list = parseNumberList(data);
        if (list == null) return "Nhap sai dinh dang! Nhap cac so cach nhau boi dau phay hoac khoang trang.";
        list.sort(Double::compareTo);
        return list.toString();
    }

    // ===== BAI 7: Sap xep giam dan (so) =====
    static String sortNumbersDesc(String data) {
        List<Double> list = parseNumberList(data);
        if (list == null) return "Nhap sai dinh dang! Nhap cac so cach nhau boi dau phay hoac khoang trang.";
        list.sort((x, y) -> Double.compare(y, x));
        return list.toString();
    }

    // ===== BAI 8: Thong ke so lan xuat hien cua tu =====
    // Input: "phat trien he thong tich hop phat trien"
    static String wordFrequency(String data) {
        String[] w = data.toLowerCase().trim().split("\\s+");
        Map<String, Integer> map = new LinkedHashMap<>();
        for (String x : w) {
            if (x.isBlank()) continue;
            map.put(x, map.getOrDefault(x, 0) + 1);
        }
        return map.toString();
    }

    // ===== BAI 9: Sap xep chuoi =====
    // Input: "zebra,apple,cat"
    static String sortStringsAsc(String data) {
        String[] a = data.split(",");
        List<String> list = new ArrayList<>();
        for (String s : a) list.add(s.trim());
        Collections.sort(list);
        return list.toString();
    }

    // ===== BAI 10: Dao chuoi =====
    static String reverseText(String data) {
        return new StringBuilder(data).reverse().toString();
    }

    // ===== BAI 11: Ngat chuoi =====
    // Input: "a-b-c-d|-"
    static String splitTextByDelimiter(String data) {
        String[] p = data.split("\\|", 2);
        if (p.length != 2) return "Nhap: text|delimiter";
        return Arrays.toString(p[0].split(java.util.regex.Pattern.quote(p[1])));
    }

    // ===== BAI 12: UCLN + BCNN =====
    // Input: "a b"  (vd: 24 36)
    static String gcdLcm(String data) {
        try {
            String[] a = data.trim().split("\\s+");
            if (a.length != 2) return "Nhap: a b";
            long x = Math.abs(Long.parseLong(a[0]));
            long y = Math.abs(Long.parseLong(a[1]));
            if (x == 0 && y == 0) return "UCLN=0, BCNN=0";
            long g = gcd(x, y);
            long l = (x == 0 || y == 0) ? 0 : (x / g) * y;
            return "UCLN=" + g + ", BCNN=" + l;
        } catch (Exception e) {
            return "Nhap sai dinh dang so";
        }
    }

    // ===== BAI 13: Giai PT bac 1 =====
    // Input: "a b"  => ax + b = 0
    static String solveLinearEquation(String data) {
        try {
            String[] a = data.trim().split("\\s+");
            if (a.length != 2) return "Nhap: a b";
            double A = Double.parseDouble(a[0]);
            double B = Double.parseDouble(a[1]);
            if (A == 0 && B == 0) return "Vo so nghiem";
            if (A == 0) return "Vo nghiem";
            return String.format("x=%.6f", -B / A);
        } catch (Exception e) {
            return "Nhap sai dinh dang so";
        }
    }

    // ===== BAI 14: Giai PT bac 2 =====
    // Input: "a b c" => ax^2 + bx + c = 0
    static String solveQuadraticEquation(String data) {
        try {
            String[] a = data.trim().split("\\s+");
            if (a.length != 3) return "Nhap: a b c";
            double A = Double.parseDouble(a[0]);
            double B = Double.parseDouble(a[1]);
            double C = Double.parseDouble(a[2]);
            if (A == 0) return solveLinearEquation(B + " " + C);
            double d = B * B - 4 * A * C;
            if (d < 0) return "Vo nghiem thuc";
            if (d == 0) return String.format("x1=x2=%.6f", -B / (2 * A));
            double x1 = (-B + Math.sqrt(d)) / (2 * A);
            double x2 = (-B - Math.sqrt(d)) / (2 * A);
            return String.format("x1=%.6f, x2=%.6f", x1, x2);
        } catch (Exception e) {
            return "Nhap sai dinh dang so";
        }
    }

    // ===== BAI 15: Tong day so 1..n =====
    // Input: "n"
    static String sumOneToN(String data) {
        try {
            long n = Long.parseLong(data.trim());
            if (n < 0) return "n phai >= 0";
            return String.valueOf(n * (n + 1) / 2);
        } catch (Exception e) {
            return "Nhap sai dinh dang so";
        }
    }

    // ===== BAI 16: Dem nguyen am phu am =====
    // Input: "mot chuoi bat ky"
    static String countVowelsConsonants(String data) {
        int vowel = 0, consonant = 0;
        String s = data.toLowerCase();
        for (char c : s.toCharArray()) {
            if (c >= 'a' && c <= 'z') {
                if ("aeiou".indexOf(c) >= 0) vowel++;
                else consonant++;
            }
        }
        return "NguyenAm=" + vowel + ", PhuAm=" + consonant;
    }

    // ===== BAI 17: Chuan hoa chuoi =====
    // Input: "   phat   trien  he THONG   "
    static String normalizeText(String data) {
        String[] w = data.trim().toLowerCase().split("\\s+");
        StringBuilder sb = new StringBuilder();
        for (String x : w) {
            if (x.isBlank()) continue;
            sb.append(Character.toUpperCase(x.charAt(0))).append(x.substring(1)).append(' ');
        }
        return sb.toString().trim();
    }

    // ===== BAI 18: Kiem tra doi xung =====
    // Input: "racecar"
    static String palindromeCheck(String data) {
        String s = data.replaceAll("\\s+", "").toLowerCase();
        String r = new StringBuilder(s).reverse().toString();
        return s.equals(r) ? "Palindrome" : "Khong palindrome";
    }

    // ===== BAI 19: Giai thua =====
    // Input: "n"
    static String factorialValue(String data) {
        try {
            int n = Integer.parseInt(data.trim());
            if (n < 0) return "n phai >= 0";
            long f = 1;
            for (int i = 2; i <= n; i++) f *= i;
            return String.valueOf(f);
        } catch (Exception e) {
            return "Nhap sai dinh dang so";
        }
    }

    // ===== BAI 20: Tong chu so =====
    // Input: "12345"
    static String sumDigits(String data) {
        String s = data.trim();
        int sum = 0;
        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) sum += c - '0';
            else if (c != '-') return "Chi nhap so nguyen";
        }
        return String.valueOf(sum);
    }

    // ===== BAI 21: Tong danh sach so =====
    // Input: "1,2,3,4,5"
    static String sumNumberList(String data) {
        List<Double> list = parseNumberList(data);
        if (list == null || list.isEmpty()) return "Nhap sai dinh dang! Nhap cac so cach nhau boi dau phay hoac khoang trang.";
        double sum = 0;
        for (double x : list) sum += x;
        return String.format("Tong=%.4f", sum);
    }

    // ===== BAI 22: Tim Max/Min =====
    // Input: "5,2,9,1"
    static String minMaxNumberList(String data) {
        List<Double> list = parseNumberList(data);
        if (list == null || list.isEmpty()) return "Nhap sai dinh dang! Nhap cac so cach nhau boi dau phay hoac khoang trang.";
        double min = list.get(0), max = list.get(0);
        for (double x : list) {
            if (x < min) min = x;
            if (x > max) max = x;
        }
        return String.format("Min=%.4f, Max=%.4f", min, max);
    }

    // ===== BAI 23: Kiem tra chan/le =====
    // Input: "n"
    static String evenOddCheck(String data) {
        try {
            long n = Long.parseLong(data.trim());
            return (n % 2 == 0) ? "So chan" : "So le";
        } catch (Exception e) {
            return "Nhap sai dinh dang so";
        }
    }

    // ===== BAI 24: In hoa =====
    static String toUpperCaseText(String data) {
        return data.toUpperCase();
    }

    // ===== BAI 25: In thuong =====
    static String toLowerCaseText(String data) {
        return data.toLowerCase();
    }

    // ===== BAI 26: Dem ky tu =====
    // Input: "abc de"
    static String countCharacters(String data) {
        int all = data.length();
        int noSpace = data.replace(" ", "").length();
        return "TongKyTu=" + all + ", KhongTinhSpace=" + noSpace;
    }

    // ===== BAI 27: Dien tich HCN =====
    // Input: "width height" or "width,height" (vd: "3 4" or "3,4")
    static String areaRectangle(String data) {
        String[] a = data.trim().split("[ ,]+");
        if (a.length != 2) return "Nhap: width height";
        try {
            double w = Double.parseDouble(a[0]);
            double h = Double.parseDouble(a[1]);
            return String.format("Dien tich HCN=%.4f", w * h);
        } catch (Exception e) {
            return "Nhap sai dinh dang so";
        }
    }

    // ===== BAI 28: Dien tich hinh tron =====
    // Input: "r"  (vd: 3)
    static String areaCircle(String data) {
        try {
            double r = Double.parseDouble(data.trim());
            if (r < 0) return "Ban kinh phai >= 0";
            return String.format("Dien tich hinh tron=%.4f", Math.PI * r * r);
        } catch (Exception e) { return "Nhap sai dinh dang so"; }
    }

    // ===== BAI 29: Dien tich hinh thang =====
    // Input: "a b h"  (vd: 3 4 5)
    static String areaTrapezoid(String data) {
        String[] a = data.trim().split("[ ,]+");
        if (a.length != 3) return "Nhap: a b h";
        try {
            double A = Double.parseDouble(a[0]);
            double B = Double.parseDouble(a[1]);
            double H = Double.parseDouble(a[2]);
            if (H < 0) return "Chieu cao phai >= 0";
            return String.format("Dien tich hinh thang=%.4f", (A + B) * H / 2.0);
        } catch (Exception e) { return "Nhap sai dinh dang so"; }
    }

    // ===== BAI 30: Chu vi hinh vuong =====
    // Input: "side"  (vd: 4)
    static String perimeterSquare(String data) {
        try {
            double a = Double.parseDouble(data.trim());
            return String.format("Chu vi hinh vuong=%.4f", 4 * a);
        } catch (Exception e) { return "Nhap sai dinh dang so"; }
    }

    // ===== BAI 31: Chu vi hinh chu nhat =====
    // Input: "width height" (vd: 3 4)
    static String perimeterRectangle(String data) {
        String[] a = data.trim().split("[ ,]+");
        if (a.length != 2) return "Nhap: width height";
        try {
            double w = Double.parseDouble(a[0]);
            double h = Double.parseDouble(a[1]);
            return String.format("Chu vi HCN=%.4f", 2 * (w + h));
        } catch (Exception e) { return "Nhap sai dinh dang so"; }
    }

    static long gcd(long a, long b) {
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        return Math.abs(a);
    }

    static List<Double> parseNumberList(String data) {
        String[] a = data.trim().split("[ ,]+");
        List<Double> list = new ArrayList<>();
        try {
            for (String s : a) {
                if (s.isBlank()) continue;
                list.add(Double.parseDouble(s.trim()));
            }
        } catch (Exception e) {
            return null;
        }
        return list;
    }
}

