package gkrmi;

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.*;

public class RemoteServiceImpl extends UnicastRemoteObject implements IRemoteService {
    private static final long serialVersionUID = 1L;

    // Dữ liệu mẫu người dùng: Email -> "Họ tên SĐT" (Phục vụ Câu 2 đề thi giữa kỳ)
    private final Map<String, String> userDatabase = new HashMap<>();

    // Danh sách mẫu SinhVien (Phục vụ Lab 1 & Lab 3)
    private final List<SinhVien> sinhVienList = new ArrayList<>();

    public RemoteServiceImpl() throws RemoteException {
        super();
        // Khởi tạo dữ liệu người dùng mẫu
        userDatabase.put("abcd1234@gmail.com", "HenryFord 825 893 5382");
        userDatabase.put("nguyenvana@gmail.com", "Nguyen Van A 0912345678");
        userDatabase.put("tranthib@gmail.com", "Tran Thi B 0987654321");
        userDatabase.put("lethanhlong@gmail.com", "Le Thanh Long 0909123456");

        // Khởi tạo danh sách sinh viên mẫu
        sinhVienList.add(new SinhVien("SV01", "Nguyen Van An", 8.8));
        sinhVienList.add(new SinhVien("SV02", "Tran Thi Binh", 7.2));
        sinhVienList.add(new SinhVien("SV03", "Le Thanh Long", 9.0));
    }

    // =========================================================================
    // NHÓM 1: TOÁN HỌC & MÁY TÍNH
    // =========================================================================
    @Override
    public int add(int a, int b) throws RemoteException {
        return a + b;
    }

    @Override
    public int sub(int a, int b) throws RemoteException {
        return a - b;
    }

    @Override
    public int mul(int a, int b) throws RemoteException {
        return a * b;
    }

    @Override
    public double div(int a, int b) throws RemoteException {
        if (b == 0) {
            throw new ArithmeticException("Lỗi: Không thể chia cho 0!");
        }
        return (double) a / b;
    }

    @Override
    public boolean isPrime(long n) throws RemoteException {
        if (n < 2) return false;
        for (long i = 2; i * i <= n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }

    @Override
    public long giaiThua(int n) throws RemoteException {
        if (n < 0) return -1;
        long f = 1;
        for (int i = 2; i <= n; i++) f *= i;
        return f;
    }

    @Override
    public long fibonacci(int n) throws RemoteException {
        if (n <= 0) return 0;
        if (n == 1) return 1;
        long a = 0, b = 1;
        for (int i = 2; i <= n; i++) {
            long c = a + b;
            a = b;
            b = c;
        }
        return b;
    }

    @Override
    public String dayFibonacci(int n) throws RemoteException {
        if (n < 0) return "n phai >= 0";
        if (n == 0) return "0";
        StringBuilder sb = new StringBuilder("0, 1");
        long a = 0, b = 1;
        for (int i = 2; i <= n; i++) {
            long c = a + b;
            sb.append(", ").append(c);
            a = b;
            b = c;
        }
        return sb.toString();
    }

    @Override
    public long gcd(long a, long b) throws RemoteException {
        a = Math.abs(a);
        b = Math.abs(b);
        while (b != 0) {
            long t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    @Override
    public long lcm(long a, long b) throws RemoteException {
        if (a == 0 || b == 0) return 0;
        return Math.abs(a * b) / gcd(a, b);
    }

    @Override
    public String giaiPTBac1(double a, double b) throws RemoteException {
        if (a == 0 && b == 0) return "Vo so nghiem";
        if (a == 0) return "Vo nghiem";
        return String.format("x = %.4f", -b / a);
    }

    @Override
    public String giaiPTBac2(double a, double b, double c) throws RemoteException {
        if (a == 0) return giaiPTBac1(b, c);
        double delta = b * b - 4 * a * c;
        if (delta < 0) return "Vo nghiem thuc";
        if (delta == 0) return String.format("Nghiem kep x1 = x2 = %.4f", -b / (2 * a));
        double x1 = (-b + Math.sqrt(delta)) / (2 * a);
        double x2 = (-b - Math.sqrt(delta)) / (2 * a);
        return String.format("x1 = %.4f, x2 = %.4f", x1, x2);
    }

    @Override
    public String tinhTamGiac(double a, double b, double c) throws RemoteException {
        if (a <= 0 || b <= 0 || c <= 0 || a + b <= c || a + c <= b || b + c <= a) {
            return "Khong phai 3 canh cua tam giac";
        }
        double cv = a + b + c;
        double p = cv / 2;
        double dt = Math.sqrt(p * (p - a) * (p - b) * (p - c));
        return String.format("Chu vi = %.2f, Dien tich = %.2f", cv, dt);
    }

    // =========================================================================
    // NHÓM 2: XỬ LÝ CHUỖI
    // =========================================================================

    // ĐỀ THI GIỮA KỲ: "3432" -> "3432: ba bốn ba hai"
    @Override
    public String doiSoThanhChu(String numberStr) throws RemoteException {
        if (numberStr == null || numberStr.isBlank()) return "Chuoi rong";
        String[] words = {"không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"};
        StringBuilder sb = new StringBuilder();
        for (char ch : numberStr.trim().toCharArray()) {
            if (ch >= '0' && ch <= '9') {
                sb.append(words[ch - '0']).append(" ");
            } else {
                return "Chuoi chua ky tu khong phai chu so!";
            }
        }
        return numberStr.trim() + ": " + sb.toString().trim();
    }

    @Override
    public String daoChuoi(String str) throws RemoteException {
        return new StringBuilder(str).reverse().toString();
    }

    @Override
    public String inHoa(String str) throws RemoteException {
        return str.toUpperCase();
    }

    @Override
    public String inThuong(String str) throws RemoteException {
        return str.toLowerCase();
    }

    @Override
    public String chuanHoaChuoi(String str) throws RemoteException {
        String[] words = str.trim().toLowerCase().split("\\s+");
        StringBuilder sb = new StringBuilder();
        for (String w : words) {
            if (!w.isBlank()) {
                sb.append(Character.toUpperCase(w.charAt(0))).append(w.substring(1)).append(" ");
            }
        }
        return sb.toString().trim();
    }

    @Override
    public String demKyTu(String str) throws RemoteException {
        int all = str.length();
        int vowels = 0, consonants = 0, digits = 0, spaces = 0;
        String s = str.toLowerCase();
        for (char c : s.toCharArray()) {
            if (Character.isDigit(c)) digits++;
            else if (Character.isWhitespace(c)) spaces++;
            else if (c >= 'a' && c <= 'z') {
                if ("aeiou".indexOf(c) >= 0) vowels++;
                else consonants++;
            }
        }
        return String.format("Tong=%d, NguyenAm=%d, PhuAm=%d, ChuSo=%d, KhoangTrang=%d",
                all, vowels, consonants, digits, spaces);
    }

    @Override
    public String thongKeTu(String str) throws RemoteException {
        String[] words = str.trim().toLowerCase().split("\\s+");
        Map<String, Integer> freq = new LinkedHashMap<>();
        for (String w : words) {
            if (!w.isBlank()) freq.put(w, freq.getOrDefault(w, 0) + 1);
        }
        return freq.toString();
    }

    @Override
    public boolean isPalindrome(String str) throws RemoteException {
        String clean = str.replaceAll("\\s+", "").toLowerCase();
        return clean.equals(new StringBuilder(clean).reverse().toString());
    }

    // =========================================================================
    // NHÓM 3: DÃY SỐ / MẢNG (LAB 5)
    // =========================================================================
    @Override
    public String sapXepDaySo(String inputNumbers) throws RemoteException {
        try {
            String[] tokens = inputNumbers.trim().split("[ ,\\s]+");
            List<Double> list = new ArrayList<>();
            for (String t : tokens) {
                if (!t.isBlank()) list.add(Double.parseDouble(t));
            }
            if (list.isEmpty()) return "Loi: Danh sach so rong";

            // Chuỗi nhận được
            String original = inputNumbers.trim();

            // Sắp xếp tăng dần
            List<Double> asc = new ArrayList<>(list);
            Collections.sort(asc);

            // Sắp xếp giảm dần
            List<Double> desc = new ArrayList<>(list);
            desc.sort(Collections.reverseOrder());

            return "Chuoi nhan duoc: " + original +
                    "\nChuoi sap giam dan: " + formatList(desc) +
                    "\nChuoi sap tang dan: " + formatList(asc);
        } catch (NumberFormatException e) {
            return "Loi: Du lieu co chua ky tu khong phai so hop le";
        }
    }

    @Override
    public String timMaxMinTong(String inputNumbers) throws RemoteException {
        try {
            String[] tokens = inputNumbers.trim().split("[ ,\\s]+");
            List<Double> list = new ArrayList<>();
            double sum = 0;
            for (String t : tokens) {
                if (!t.isBlank()) {
                    double val = Double.parseDouble(t);
                    list.add(val);
                    sum += val;
                }
            }
            if (list.isEmpty()) return "Danh sach rong";
            double min = Collections.min(list);
            double max = Collections.max(list);
            double avg = sum / list.size();
            return String.format("Min=%.2f, Max=%.2f, Tong=%.2f, TBC=%.2f", min, max, sum, avg);
        } catch (Exception e) {
            return "Loi: " + e.getMessage();
        }
    }

    private String formatList(List<Double> list) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < list.size(); i++) {
            double v = list.get(i);
            if (v == (long) v) sb.append((long) v);
            else sb.append(v);
            if (i < list.size() - 1) sb.append(" ");
        }
        return sb.toString();
    }

    // =========================================================================
    // NHÓM 4: ĐỐI TƯỢNG & TÌM KIẾM (CÂU 2 ĐỀ THI GIỮA KỲ & LAB 1, 3)
    // =========================================================================
    @Override
    public String timNguoiDungTheoEmail(String email) throws RemoteException {
        if (email == null) return "Email khong hop le";
        String key = email.trim().toLowerCase();
        if (userDatabase.containsKey(key)) {
            return email.trim() + " và " + userDatabase.get(key);
        }
        return email.trim() + " -> Khong tim thay nguoi dung trong he thong";
    }

    @Override
    public SinhVien timSinhVienTheoMa(String maSV) throws RemoteException {
        for (SinhVien sv : sinhVienList) {
            if (sv.getMaSV().equalsIgnoreCase(maSV.trim())) {
                return sv;
            }
        }
        return null;
    }

    @Override
    public boolean themSinhVien(SinhVien sv) throws RemoteException {
        if (sv == null) return false;
        sinhVienList.add(sv);
        return true;
    }

    @Override
    public List<SinhVien> getDanhSachSinhVien() throws RemoteException {
        return new ArrayList<>(sinhVienList);
    }
}
