package gkrmi;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.*;

public class RemoteServiceImpl extends UnicastRemoteObject implements IRemoteService {
    private static final long serialVersionUID = 1L;

    public RemoteServiceImpl() throws RemoteException {
        super();
    }

    // =========================================================================
    // ⚠️ QUY TẮC PHÒNG THI ĐỂ BÀI NỘP KHÔNG BỊ THỪA:
    // 1. Chỉ uncomment ĐÚNG 1 BÀI tương ứng với IRemoteService và RMIClient.
    // 2. VỀ FILE SinhVien.java:
    //    CHỈ DUY NHẤT [BÀI 37: ĐỐI TƯỢNG SINH VIÊN] MỚI CẦN FILE SinhVien.java.
    //    NẾU ĐỀ RA BẤT KỲ BÀI NÀO KHÁC (BÀI 1 ĐẾN BÀI 36):
    //    -> HÃY XÓA THẲNG TAY FILE SinhVien.java ĐI, DỰ ÁN VẪN BIÊN DỊCH VÀ CHẠY 100%!
    // =========================================================================

    // ========== BAI 1: May tinh 4 phep tinh (+, -, *, /) - [TUAN 6 BAI 3 - MAC DINH BAT] [KHONG CAN SinhVien.java] ==========
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
        if (b == 0) throw new ArithmeticException("Khong the chia cho 0!");
        return (double) a / b;
    }

    // ========== BAI 2: Tam giac (Chu vi, dien tich Heron) - Input: a, b, c - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String tinhTamGiac(double a, double b, double c) throws RemoteException {
    //     if (!(a > 0 && b > 0 && c > 0 && a + b > c && a + c > b && b + c > a)) {
    //         return "Khong phai tam giac hop le!";
    //     }
    //     double p = a + b + c;
    //     double s = Math.sqrt((p / 2) * (p / 2 - a) * (p / 2 - b) * (p / 2 - c));
    //     return String.format("Tam giac hop le | Chu vi=%.2f | Dien tich=%.2f", p, s);
    // }

    // ========== BAI 3: So phuc (ADD/SUB/MUL/DIV) - Input: op, ar, ai, br, bi - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String soPhuc(String op, double ar, double ai, double br, double bi) throws RemoteException {
    //     String operation = (op == null) ? "" : op.trim().toUpperCase();
    //     double rr = 0, ri = 0;
    //     if (operation.equals("ADD")) { rr = ar + br; ri = ai + bi; }
    //     else if (operation.equals("SUB")) { rr = ar - br; ri = ai - bi; }
    //     else if (operation.equals("MUL")) { rr = ar * br - ai * bi; ri = ar * bi + ai * br; }
    //     else if (operation.equals("DIV")) {
    //         double den = br * br + bi * bi;
    //         if (den == 0) return "Loi chia 0";
    //         rr = (ar * br + ai * bi) / den; ri = (ai * br - ar * bi) / den;
    //     } else return "Toan tu chi chap nhan ADD|SUB|MUL|DIV";
    //     return String.format("%.4f%+.4fi", rr, ri);
    // }

    // ========== BAI 4: So Fibonacci / In day Fibonacci - Input: n - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String fibonacci(int n) throws RemoteException {
    //     if (n < 0) return "n phai >= 0";
    //     if (n == 0) return "0";
    //     if (n == 1) return "0, 1 (F1 = 1)";
    //     long fibA = 0, fibB = 1;
    //     StringBuilder sb = new StringBuilder("0, 1");
    //     for (int i = 2; i <= n; i++) {
    //         long c = fibA + fibB;
    //         sb.append(", ").append(c);
    //         fibA = fibB;
    //         fibB = c;
    //     }
    //     return "F(" + n + ") = " + fibB + " | Day: " + sb.toString();
    // }

    // ========== BAI 5: Quy doi tien te - Input: amount, from, to (USD, EUR, JPY, VND) - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String quyDoiTienTe(double amount, String from, String to) throws RemoteException {
    //     Map<String, Double> rates = new HashMap<>();
    //     rates.put("VND", 1.0); rates.put("USD", 25000.0); rates.put("EUR", 27000.0); rates.put("JPY", 170.0);
    //     String f = (from == null) ? "" : from.trim().toUpperCase();
    //     String t = (to == null) ? "" : to.trim().toUpperCase();
    //     if (!rates.containsKey(f) || !rates.containsKey(t)) return "Chi ho tro tien te: VND, USD, EUR, JPY";
    //     double inVnd = amount * rates.get(f);
    //     double res = inVnd / rates.get(t);
    //     return String.format("%.2f %s = %.4f %s", amount, f, res, t);
    // }

    // ========== BAI 6: Kiem tra so nguyen to - Input: n - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public boolean isPrime(long n) throws RemoteException {
    //     if (n < 2) return false;
    //     for (long i = 2; i * i <= n; i++) if (n % i == 0) return false;
    //     return true;
    // }

    // ========== BAI 7: Sap xep tang dan danh sach so - Input: "5,2,9,1" - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String sapXepTangDan(String inputNumbers) throws RemoteException {
    //     if (inputNumbers == null || inputNumbers.trim().isEmpty()) return "Danh sach rong";
    //     String[] tokens = inputNumbers.trim().split("[ ,\\s]+");
    //     List<Double> list = new ArrayList<>();
    //     for (String s : tokens) if (!s.trim().isEmpty()) list.add(Double.parseDouble(s.trim()));
    //     Collections.sort(list);
    //     return "Tang dan: " + list.toString();
    // }

    // ========== BAI 8: Sap xep giam dan danh sach so - Input: "5,2,9,1" - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String sapXepGiamDan(String inputNumbers) throws RemoteException {
    //     if (inputNumbers == null || inputNumbers.trim().isEmpty()) return "Danh sach rong";
    //     String[] tokens = inputNumbers.trim().split("[ ,\\s]+");
    //     List<Double> list = new ArrayList<>();
    //     for (String s : tokens) if (!s.trim().isEmpty()) list.add(Double.parseDouble(s.trim()));
    //     list.sort(Collections.reverseOrder());
    //     return "Giam dan: " + list.toString();
    // }

    // ========== BAI 9: Thong ke so lan xuat hien cua tu - Input: str - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String thongKeTu(String str) throws RemoteException {
    //     if (str == null || str.trim().isEmpty()) return "Chuoi rong";
    //     String[] words = str.toLowerCase().trim().split("\\s+");
    //     Map<String, Integer> map = new LinkedHashMap<>();
    //     for (String w : words) if (!w.trim().isEmpty()) map.put(w, map.getOrDefault(w, 0) + 1);
    //     return map.toString();
    // }

    // ========== BAI 10: Sap xep chuoi theo chu cai - Input: "zebra,apple,cat" - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String sapXepChuoiTheoChuCai(String str) throws RemoteException {
    //     if (str == null || str.trim().isEmpty()) return "Chuoi rong";
    //     String[] words = str.split("[ ,\\s]+");
    //     List<String> list = new ArrayList<>();
    //     for (String w : words) if (!w.trim().isEmpty()) list.add(w.trim());
    //     Collections.sort(list);
    //     return list.toString();
    // }

    // ========== BAI 11: Dao nguoc chuoi - Input: str - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String daoChuoi(String str) throws RemoteException {
    //     if (str == null) return "";
    //     return new StringBuilder(str).reverse().toString();
    // }

    // ========== BAI 12: Ngat chuoi theo ky tu phan cach - Input: text, delimiter - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String ngatChuoi(String text, String delimiter) throws RemoteException {
    //     if (text == null) return "Chuoi rong";
    //     if (delimiter == null || delimiter.isEmpty()) delimiter = " ";
    //     String[] parts = text.split(java.util.regex.Pattern.quote(delimiter));
    //     return Arrays.toString(parts);
    // }

    // ========== BAI 13: UCLN va BCNN - Input: a, b - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String uclnVaBcnn(long a, long b) throws RemoteException {
    //     long x = Math.abs(a), y = Math.abs(b);
    //     long g = gcd(x, y);
    //     long l = (x == 0 || y == 0) ? 0 : (x / g) * y;
    //     return "UCLN=" + g + ", BCNN=" + l;
    // }

    // ========== BAI 14: Giai phuong trinh bac 1 (ax + b = 0) - Input: a, b - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String giaiPTBac1(double a, double b) throws RemoteException {
    //     if (a == 0 && b == 0) return "Vo so nghiem";
    //     if (a == 0) return "Vo nghiem";
    //     return String.format("Nghiem x = %.4f", -b / a);
    // }

    // ========== BAI 15: Giai phuong trinh bac 2 (ax^2 + bx + c = 0) - Input: a, b, c - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String giaiPTBac2(double a, double b, double c) throws RemoteException {
    //     if (a == 0) {
    //         if (b == 0 && c == 0) return "Vo so nghiem";
    //         if (b == 0) return "Vo nghiem";
    //         return String.format("Nghiem x = %.4f", -c / b);
    //     }
    //     double delta = b * b - 4 * a * c;
    //     if (delta < 0) return "Phuong trinh vo nghiem thuc";
    //     if (delta == 0) return String.format("Nghiem kep x1 = x2 = %.4f", -b / (2 * a));
    //     double x1 = (-b + Math.sqrt(delta)) / (2 * a);
    //     double x2 = (-b - Math.sqrt(delta)) / (2 * a);
    //     return String.format("x1 = %.4f, x2 = %.4f", x1, x2);
    // }

    // ========== BAI 16: Tinh tong 1..n - Input: n - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public long tong1DenN(long n) throws RemoteException {
    //     if (n < 0) return 0;
    //     return n * (n + 1) / 2;
    // }

    // ========== BAI 17: Dem nguyen am va phu am - Input: str - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String demNguyenAmPhuAm(String str) throws RemoteException {
    //     if (str == null) return "Chuoi rong";
    //     int v = 0, c = 0;
    //     String s = str.toLowerCase();
    //     for (char ch : s.toCharArray()) {
    //         if (ch >= 'a' && ch <= 'z') {
    //             if ("aeiou".indexOf(ch) >= 0) v++; else c++;
    //         }
    //     }
    //     return "Nguyen am = " + v + ", Phu am = " + c;
    // }

    // ========== BAI 18: Chuan hoa chuoi (Viet hoa dau moi tu) - Input: str - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String chuanHoaChuoi(String str) throws RemoteException {
    //     if (str == null || str.trim().isEmpty()) return "";
    //     String[] words = str.trim().toLowerCase().split("\\s+");
    //     StringBuilder sb = new StringBuilder();
    //     for (String w : words) {
    //         if (!w.trim().isEmpty()) {
    //             sb.append(Character.toUpperCase(w.charAt(0))).append(w.substring(1)).append(" ");
    //         }
    //     }
    //     return sb.toString().trim();
    // }

    // ========== BAI 19: Kiem tra chuoi Palindrome (Doi xung) - Input: str - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public boolean isPalindrome(String str) throws RemoteException {
    //     if (str == null) return false;
    //     String clean = str.replaceAll("\\s+", "").toLowerCase();
    //     String rev = new StringBuilder(clean).reverse().toString();
    //     return clean.equals(rev);
    // }

    // ========== BAI 20: Tinh giai thua (n!) - Input: n - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public long giaiThua(int n) throws RemoteException {
    //     if (n < 0) throw new IllegalArgumentException("n phai >= 0");
    //     long f = 1;
    //     for (int i = 2; i <= n; i++) f *= i;
    //     return f;
    // }

    // ========== BAI 21: Tinh tong cac chu so - Input: 12345 - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public int tongCacChuSo(String numberStr) throws RemoteException {
    //     if (numberStr == null) return 0;
    //     int sum = 0;
    //     for (char ch : numberStr.trim().toCharArray()) {
    //         if (Character.isDigit(ch)) sum += ch - '0';
    //     }
    //     return sum;
    // }

    // ========== BAI 22: Tinh tong danh sach so - Input: "1,2,3,4,5" - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public double tongDanhSachSo(String inputNumbers) throws RemoteException {
    //     if (inputNumbers == null || inputNumbers.trim().isEmpty()) return 0;
    //     String[] tokens = inputNumbers.trim().split("[ ,\\s]+");
    //     double sum = 0;
    //     for (String s : tokens) if (!s.trim().isEmpty()) sum += Double.parseDouble(s.trim());
    //     return sum;
    // }

    // ========== BAI 23: Tim Min va Max cua danh sach so - Input: "5,2,9,1" - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String timMinMax(String inputNumbers) throws RemoteException {
    //     if (inputNumbers == null || inputNumbers.trim().isEmpty()) return "Danh sach rong";
    //     String[] tokens = inputNumbers.trim().split("[ ,\\s]+");
    //     List<Double> list = new ArrayList<>();
    //     for (String s : tokens) if (!s.trim().isEmpty()) list.add(Double.parseDouble(s.trim()));
    //     if (list.isEmpty()) return "Danh sach rong";
    //     double min = list.get(0), max = list.get(0);
    //     for (double num : list) { if (num < min) min = num; if (num > max) max = num; }
    //     return String.format("Min=%.4f, Max=%.4f", min, max);
    // }

    // ========== BAI 24: Kiem tra chan le - Input: n - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String kiemTraChanLe(long n) throws RemoteException {
    //     return (n % 2 == 0) ? "So chan" : "So le";
    // }

    // ========== BAI 25: Chuyen chuoi sang IN HOA - Input: str - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String inHoa(String str) throws RemoteException {
    //     return (str == null) ? "" : str.toUpperCase();
    // }

    // ========== BAI 26: Chuyen chuoi sang in thuong - Input: str - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String inThuong(String str) throws RemoteException {
    //     return (str == null) ? "" : str.toLowerCase();
    // }

    // ========== BAI 27: Dem tong so ky tu (co space va khong space) - Input: str - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String demKyTu(String str) throws RemoteException {
    //     if (str == null) return "TongKyTu=0, KhongTinhSpace=0";
    //     int all = str.length();
    //     int noSpace = str.replace(" ", "").length();
    //     return "TongKyTu=" + all + ", KhongTinhSpace=" + noSpace;
    // }

    // ========== BAI 28: Dien tich Hinh Chu Nhat - Input: dai, rong - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public double dienTichHCN(double dai, double rong) throws RemoteException {
    //     return dai * rong;
    // }

    // ========== BAI 29: Dien tich Hinh Tron - Input: r - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public double dienTichHinhTron(double r) throws RemoteException {
    //     if (r < 0) throw new IllegalArgumentException("Ban kinh phai >= 0");
    //     return Math.PI * r * r;
    // }

    // ========== BAI 30: Dien tich Hinh Thang - Input: a, b, h - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public double dienTichHinhThang(double a, double b, double h) throws RemoteException {
    //     if (h < 0) throw new IllegalArgumentException("Chieu cao phai >= 0");
    //     return (a + b) * h / 2.0;
    // }

    // ========== BAI 31: Chu vi Hinh Vuong - Input: side - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public double chuViHinhVuong(double side) throws RemoteException {
    //     return 4 * side;
    // }

    // ========== BAI 32: Chu vi Hinh Chu Nhat - Input: dai, rong - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public double chuViHCN(double dai, double rong) throws RemoteException {
    //     return 2 * (dai + rong);
    // }

    // ========== BAI 33: [ĐỀ THI GIỮA KỲ CÂU 1] Chuyen so thanh chu - Input: "3432" - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String doiSoThanhChu(String numberStr) throws RemoteException {
    //     if (numberStr == null || numberStr.trim().isEmpty()) return "Chuoi rong";
    //     String[] words = {"không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"};
    //     StringBuilder sb = new StringBuilder();
    //     for (char ch : numberStr.trim().toCharArray()) {
    //         if (ch >= '0' && ch <= '9') sb.append(words[ch - '0']).append(" ");
    //         else return "Chuoi chua ky tu khong phai chu so!";
    //     }
    //     return numberStr.trim() + ": " + sb.toString().trim();
    // }

    // ========== BAI 34: [ĐỀ THI GIỮA KỲ CÂU 2] Tim thong tin theo Email - Input: "abcd1234@gmail.com" - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String timNguoiDungTheoEmail(String email) throws RemoteException {
    //     if (email == null) return "Email khong hop le";
    //     Map<String, String> userDb = new HashMap<>();
    //     userDb.put("abcd1234@gmail.com", "HenryFord 825 893 5382");
    //     userDb.put("nguyenvana@gmail.com", "Nguyen Van A 0912345678");
    //     userDb.put("tranthib@gmail.com", "Tran Thi B 0987654321");
    //     File uFile = new File("users.txt");
    //     if (uFile.exists()) {
    //         try (BufferedReader br = new BufferedReader(new FileReader(uFile))) {
    //             String line;
    //             while ((line = br.readLine()) != null) {
    //                 String[] p = line.split("[=:]", 2);
    //                 if (p.length == 2) userDb.put(p[0].trim().toLowerCase(), p[1].trim());
    //             }
    //         } catch (Exception ignored) {}
    //     }
    //     String key = email.trim().toLowerCase();
    //     if (userDb.containsKey(key)) return email.trim() + " và " + userDb.get(key);
    //     return email.trim() + " -> Khong tim thay nguoi dung";
    // }

    // ========== BAI 35: [THỰC HÀNH LAB 5] Sap xep day so - Input: "11 22 4 25 28 3" - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String sapXepDaySo(String inputNumbers) throws RemoteException {
    //     try {
    //         String[] tokens = inputNumbers.trim().split("[ ,\\s]+");
    //         List<Double> list = new ArrayList<>();
    //         for (String t : tokens) if (!t.trim().isEmpty()) list.add(Double.parseDouble(t));
    //         if (list.isEmpty()) return "Loi: Danh sach so rong";
    //         List<Double> asc = new ArrayList<>(list); Collections.sort(asc);
    //         List<Double> desc = new ArrayList<>(list); desc.sort(Collections.reverseOrder());
    //         return "Chuoi nhan duoc: " + inputNumbers.trim() +
    //                "\nChuoi sap giam dan: " + desc +
    //                "\nChuoi sap tang dan: " + asc;
    //     } catch (Exception e) {
    //         return "Loi: " + e.getMessage();
    //     }
    // }

    // ========== BAI 36: [THỰC HÀNH TUẦN 3] Doc file van ban tren Server - Input: "users.txt" - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String docFile(String fileName) throws RemoteException {
    //     File f = new File(fileName);
    //     if (!f.exists()) return "Loi: File '" + fileName + "' khong ton tai tren Server!";
    //     StringBuilder sb = new StringBuilder();
    //     try (BufferedReader br = new BufferedReader(new FileReader(f))) {
    //         String line;
    //         while ((line = br.readLine()) != null) sb.append(line).append("\n");
    //         return sb.toString();
    //     } catch (Exception e) {
    //         return "Loi khi doc file: " + e.getMessage();
    //     }
    // }

    // ========== BAI 37: [THỰC HÀNH TUẦN 1 & 3 - ⚠️ CẦN SinhVien.java] Tim sinh vien theo ma - Input: "SV01" ==========
    // @Override
    // public SinhVien timSinhVienTheoMa(String maSV) throws RemoteException {
    //     List<SinhVien> ds = new ArrayList<>();
    //     ds.add(new SinhVien("SV01", "Nguyen Van An", 8.5));
    //     ds.add(new SinhVien("SV02", "Tran Thi Binh", 7.2));
    //     ds.add(new SinhVien("SV03", "Le Van Cuong", 9.0));
    //     if (maSV == null) return null;
    //     for (SinhVien sv : ds) {
    //         if (sv.getMaSV().equalsIgnoreCase(maSV.trim())) return sv;
    //     }
    //     return null;
    // }

    // Helper: UCLN (can dung cho Bai 13)
    // private static long gcd(long a, long b) {
    //     while (b != 0) { long t = a % b; a = b; b = t; }
    //     return Math.abs(a);
    // }
}
