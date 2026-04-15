package ck;

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.*;

public class ServiceImpl extends UnicastRemoteObject implements IService {
    private static final long serialVersionUID = 1L;

    public ServiceImpl() throws RemoteException {
        super();
    }

    @Override
    public String xuLyDuLieu(String data) throws RemoteException {
        try {
            // ==========================================================
            // CHON 1 BAI DUY NHAT: COMMENT / UNCOMMENT 1 DONG DUOI DAY
            // ==========================================================
            
            // return triangleMetrics(data);      // Bai 1
             return complexArithmetic(data);    // Bai 2
            // return fibonacciValue(data);       // Bai 3
            // return currencyConvert(data);      // Bai 4
            // return primeCheck(data);           // Bai 5
            // return sortNumbersAsc(data);       // Bai 6
            // return sortNumbersDesc(data);      // Bai 7
            // return wordFrequency(data);        // Bai 8
            // return sortStringsAsc(data);       // Bai 9
            // return reverseText(data);             // Bai 10 (Mac dinh)
            // return splitTextByDelimiter(data); // Bai 11
            // return gcdLcm(data);               // Bai 12
            // return solveLinearEquation(data);  // Bai 13
            // return solveQuadraticEquation(data);// Bai 14
            // return sumOneToN(data);            // Bai 15
            // return countVowelsConsonants(data); // Bai 16
            // return normalizeText(data);        // Bai 17
            // return palindromeCheck(data);      // Bai 18
            // return factorialValue(data);       // Bai 19
            // return sumDigits(data);            // Bai 20
            // return sumNumberList(data);        // Bai 21
            // return minMaxNumberList(data);     // Bai 22
            // return evenOddCheck(data);         // Bai 23
            // return toUpperCaseText(data);      // Bai 24
            // return toLowerCaseText(data);      // Bai 25
            // return countCharacters(data);      // Bai 26
            // return areaRectangle(data);        // Bai 27
            // return areaCircle(data);           // Bai 28
            // return areaTrapezoid(data);        // Bai 29
            // return perimeterSquare(data);      // Bai 30
            // return perimeterRectangle(data);   // Bai 31
        } catch (Exception e) {
            return "Loi xử lý: " + e.getMessage();
        }
    }

    // ========== BAI 1: Tam giac - Input: "a b c" (vd: 3 4 5) ==========
    private String triangleMetrics(String data) {
        try {
            String[] a = data.trim().split("[ ,\\s]+");
            if (a.length != 3) return "Nhap: a b c";
            double x = Double.parseDouble(a[0]), y = Double.parseDouble(a[1]), z = Double.parseDouble(a[2]);
            if (!(x > 0 && y > 0 && z > 0 && x + y > z && x + z > y && y + z > x)) return "Khong phai tam giac";
            double p = x + y + z, s = Math.sqrt((p / 2) * (p / 2 - x) * (p / 2 - y) * (p / 2 - z));
            return String.format("Tam giac hop le | Chu vi=%.2f | Dien tich=%.2f", p, s);
        } catch (Exception e) { return "Loi: " + e.getMessage(); }
    }

    // ========== BAI 2: So phuc - Input: "op a b c d" (op=ADD|SUB|MUL|DIV ; z1=a+bi, z2=c+di) ==========
    private String complexArithmetic(String data) {
        try {
            String[] a = data.trim().split("[ ,\\s]+");
            if (a.length != 5) return "Nhap: op a b c d";
            String op = a[0].toUpperCase();
            double ar = Double.parseDouble(a[1]), ai = Double.parseDouble(a[2]), br = Double.parseDouble(a[3]), bi = Double.parseDouble(a[4]);
            double rr, ri;
            switch (op) {
                case "ADD": rr = ar + br; ri = ai + bi; break;
                case "SUB": rr = ar - br; ri = ai - bi; break;
                case "MUL": rr = ar * br - ai * bi; ri = ar * bi + ai * br; break;
                case "DIV":
                    double den = br * br + bi * bi; if (den == 0) return "Loi chia 0";
                    rr = (ar * br + ai * bi) / den; ri = (ai * br - ar * bi) / den; break;
                default: return "op chi ADD|SUB|MUL|DIV";
            }
            return String.format("%.4f%+.4fi", rr, ri);
        } catch (Exception e) { return "Loi: " + e.getMessage(); }
    }

    // ========== BAI 3: Fibonacci - Input: "n" (vd: 10) ==========
    private String fibonacciValue(String data) {
        try {
            int n = Integer.parseInt(data.trim());
            if (n < 0) return "n >= 0";
            if (n == 0) return "0"; 
            StringBuilder seq = new StringBuilder("0");
            if (n >= 1) { seq.append(", 1"); long a = 0, b = 1; for (int i = 2; i <= n; i++) { long c = a + b; seq.append(", ").append(c); a = b; b = c; } }
            return "Day Fibonacci: " + seq.toString();
        } catch (Exception e) { return "Loi: " + e.getMessage(); }
    }

    // ========== BAI 4: Quy doi tien te - Input: "amount from to" (vd: 100 USD VND) ==========
    private String currencyConvert(String data) {
        try {
            String[] a = data.trim().split("[ ,\\s]+");
            double amount = Double.parseDouble(a[0]);
            String from = a[1].toUpperCase(), to = a[2].toUpperCase();
            Map<String, Double> r = new HashMap<>(); r.put("VND", 1.0); r.put("USD", 25000.0); r.put("EUR", 27000.0); r.put("JPY", 170.0);
            if (!r.containsKey(from) || !r.containsKey(to)) return "Support: VND USD EUR JPY";
            return String.format("%.4f %s", (amount * r.get(from)) / r.get(to), to);
        } catch (Exception e) { return "Loi: " + e.getMessage(); }
    }

    // ========== BAI 5: Nguyen to - Input: "n" ==========
    private String primeCheck(String data) {
        try {
            long n = Long.parseLong(data.trim());
            if (n < 2) return "Khong phai SNT";
            for (long i = 2; i * i <= n; i++) if (n % i == 0) return "Khong phai SNT";
            return "La SNT";
        } catch (Exception e) { return "Loi"; }
    }

    // ========== BAI 6: Sap xep tang dan (So) - Input: "5,2,9,1" or "5 2 9" ==========
    private String sortNumbersAsc(String data) {
        List<Double> l = parseNumberList(data); if (l == null) return "Loi";
        Collections.sort(l); return l.toString();
    }

    // ========== BAI 7: Sap xep giam dan (So) - Input: "5,2,9,1" ==========
    private String sortNumbersDesc(String data) {
        List<Double> l = parseNumberList(data); if (l == null) return "Loi";
        l.sort(Collections.reverseOrder()); return l.toString();
    }

    // ========== BAI 8: Thong ke tu - Input: "phat trien he thong phat trien" ==========
    private String wordFrequency(String data) {
        String[] w = data.toLowerCase().trim().split("\\s+");
        Map<String, Integer> map = new LinkedHashMap<>();
        for (String x : w) if (!x.isBlank()) map.put(x, map.getOrDefault(x, 0) + 1);
        return map.toString();
    }

    // ========== BAI 9: Sap xep chuoi - Input: "zebra,apple,cat" ==========
    private String sortStringsAsc(String data) {
        String[] a = data.split(","); List<String> l = new ArrayList<>();
        for (String s : a) l.add(s.trim()); Collections.sort(l); return l.toString();
    }

    // ========== BAI 10: Dao chuoi - Input: "abcde" ==========
    private String reverseText(String data) { return new StringBuilder(data).reverse().toString(); }

    // ========== BAI 11: Ngat chuoi - Input: "text|delimiter" (vd: "a-b-c|-") ==========
    private String splitTextByDelimiter(String data) {
        String[] p = data.split("\\|", 2); if (p.length != 2) return "Nhap: text|delimiter";
        return Arrays.toString(p[0].split(java.util.regex.Pattern.quote(p[1])));
    }

    // ========== BAI 12: UCLN BCNN - Input: "a b" (vd: 24 36) ==========
    private String gcdLcm(String data) {
        try {
            String[] a = data.trim().split("[ ,\\s]+");
            long x = Math.abs(Long.parseLong(a[0])), y = Math.abs(Long.parseLong(a[1]));
            long g = gcd(x, y); return "UCLN=" + g + ", BCNN=" + ((x == 0 || y == 0) ? 0 : (x / g) * y);
        } catch (Exception e) { return "Loi"; }
    }

    // ========== BAI 13: PT bac 1 - Input: "a b" (vd: 2 4 => 2x+4=0) ==========
    private String solveLinearEquation(String data) {
        try {
            String[] a = data.trim().split("[ ,\\s]+");
            double A = Double.parseDouble(a[0]), B = Double.parseDouble(a[1]);
            if (A == 0) return (B == 0) ? "Vo so nghiem" : "Vo nghiem";
            return "x=" + (-B / A);
        } catch (Exception e) { return "Loi"; }
    }

    // ========== BAI 14: PT bac 2 - Input: "a b c" (vd: 1 2 1 => x^2+2x+1=0) ==========
    private String solveQuadraticEquation(String data) {
        try {
            String[] a = data.trim().split("[ ,\\s]+");
            double A = Double.parseDouble(a[0]), B = Double.parseDouble(a[1]), C = Double.parseDouble(a[2]);
            if (A == 0) return solveLinearEquation(B + " " + C);
            double d = B * B - 4 * A * C;
            if (d < 0) return "Vo nghiem thuc";
            if (d == 0) return "x=" + (-B / (2 * A));
            return "x1=" + ((-B + Math.sqrt(d)) / (2 * A)) + ", x2=" + ((-B - Math.sqrt(d)) / (2 * A));
        } catch (Exception e) { return "Loi"; }
    }

    // ========== BAI 15: Tong 1..n - Input: "n" ==========
    private String sumOneToN(String data) {
        try { long n = Long.parseLong(data.trim()); return String.valueOf(n * (n + 1) / 2); } catch (Exception e) { return "Loi"; }
    }

    // ========== BAI 16: Dem nguyen am phu am - Input: "mot chuoi" ==========
    private String countVowelsConsonants(String data) {
        int v = 0, c = 0; String s = data.toLowerCase();
        for (char ch : s.toCharArray()) if (ch >= 'a' && ch <= 'z') { if ("aeiou".indexOf(ch) >= 0) v++; else c++; }
        return "Vowels=" + v + ", Consonants=" + c;
    }

    // ========== BAI 17: Chuan hoa chuoi - Input: "  phat  TRIEN he thong  " ==========
    private String normalizeText(String data) {
        String[] w = data.trim().toLowerCase().split("\\s+"); StringBuilder sb = new StringBuilder();
        for (String x : w) if (!x.isBlank()) sb.append(Character.toUpperCase(x.charAt(0))).append(x.substring(1)).append(" ");
        return sb.toString().trim();
    }

    // ========== BAI 18: Palindrome - Input: "racecar" ==========
    private String palindromeCheck(String data) {
        String s = data.replaceAll("\\s+", "").toLowerCase();
        return s.equals(new StringBuilder(s).reverse().toString()) ? "Palindrome" : "No";
    }

    // ========== BAI 19: Giai thua - Input: "n" ==========
    private String factorialValue(String data) {
        try { int n = Integer.parseInt(data.trim()); long f = 1; for (int i = 2; i <= n; i++) f *= i; return String.valueOf(f); } catch (Exception e) { return "Loi"; }
    }

    // ========== BAI 20: Tong chu so - Input: "12345" ==========
    private String sumDigits(String data) {
        int s = 0; for (char c : data.trim().toCharArray()) if (Character.isDigit(c)) s += c - '0';
        return String.valueOf(s);
    }

    // ========== BAI 21: Tong danh sach so - Input: "1,2,3,4,5" ==========
    private String sumNumberList(String data) {
        List<Double> l = parseNumberList(data); if (l == null) return "Loi";
        double s = 0; for (double x : l) s += x; return "Tong=" + s;
    }

    // ========== BAI 22: Tim Max/Min - Input: "5,2,9,1" ==========
    private String minMaxNumberList(String data) {
        List<Double> l = parseNumberList(data); if (l == null || l.isEmpty()) return "Loi";
        double min = Collections.min(l), max = Collections.max(l);
        return "Min=" + min + ", Max=" + max;
    }

    // ========== BAI 23: Chan le - Input: "n" ==========
    private String evenOddCheck(String data) {
        try { return (Long.parseLong(data.trim()) % 2 == 0) ? "Chan" : "Le"; } catch (Exception e) { return "Loi"; }
    }

    // ========== BAI 24: In hoa - Input: "abc" ==========
    private String toUpperCaseText(String data) { return data.toUpperCase(); }

    // ========== BAI 25: In thuong - Input: "ABC" ==========
    private String toLowerCaseText(String data) { return data.toLowerCase(); }

    // ========== BAI 26: Dem ky tu - Input: "abc de" ==========
    private String countCharacters(String data) { return "Tong=" + data.length(); }

    // ========== BAI 27: Dien tich HCN - Input: "width height" (vd: 3 4) ==========
    private String areaRectangle(String data) {
        try { String[] a = data.trim().split("[ ,\\s]+"); double w = Double.parseDouble(a[0]), h = Double.parseDouble(a[1]); return "Area=" + (w * h); } catch (Exception e) { return "Loi"; }
    }

    // ========== BAI 28: Dien tich hinh tron - Input: "r" (vd: 3) ==========
    private String areaCircle(String data) {
        try { double r = Double.parseDouble(data.trim()); return "Area=" + (Math.PI * r * r); } catch (Exception e) { return "Loi"; }
    }

    // ========== BAI 29: Dien tich hinh thang - Input: "a b h" (vd: 3 4 5) ==========
    private String areaTrapezoid(String data) {
        try { String[] a = data.trim().split("[ ,\\s]+"); double A = Double.parseDouble(a[0]), B = Double.parseDouble(a[1]), H = Double.parseDouble(a[2]); return "Area=" + ((A + B) * H / 2.0); } catch (Exception e) { return "Loi"; }
    }

    // ========== BAI 30: Chu vi hinh vuong - Input: "side" ==========
    private String perimeterSquare(String data) { try { return "Perimeter=" + (4 * Double.parseDouble(data.trim())); } catch (Exception e) { return "Loi"; } }

    // ========== BAI 31: Chu vi HCN - Input: "width height" ==========
    private String perimeterRectangle(String data) {
        try { String[] a = data.trim().split("[ ,\\s]+"); double w = Double.parseDouble(a[0]), h = Double.parseDouble(a[1]); return "Perimeter=" + (2 * (w + h)); } catch (Exception e) { return "Loi"; }
    }

    private static long gcd(long a, long b) { while (b != 0) { long t = a % b; a = b; b = t; } return Math.abs(a); }
    private static List<Double> parseNumberList(String data) {
        try { String[] a = data.trim().split("[ ,\\s]+"); List<Double> l = new ArrayList<>();
        for (String s : a) if (!s.isBlank()) l.add(Double.parseDouble(s.trim())); return l; } catch (Exception e) { return null; }
    }
}
