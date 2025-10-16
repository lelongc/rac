package BSTkh;

import java.util.regex.Pattern;

public class KhachHang {
    private int id;
    private String ten;
    private int tuoi;
    private String gend;
    private String email;
    private String phone;

    // Khách hàng là nút cây
    private KhachHang trai;
    private KhachHang phai;
    
    private static final Pattern EMAIL_PATTERN =
            Pattern.compile("^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$");
    private static final Pattern PHONE_PATTERN =
            Pattern.compile("^(09|08|07|03)\\d{8}$");
    
    public KhachHang(int id, String ten, int tuoi, String gend, String email, String phone) {
        super();
        this.id = id;
        this.ten = ten;
        this.tuoi = validateTuoi(tuoi);
        this.gend = validateGioiTinh(gend);
        this.email = validateEmail(email);
        this.phone = validatePhone(phone);
    }
    

    public KhachHang(int id, String ten, int tuoi, String gend) {
        this(id, ten, tuoi, gend, generateEmail(ten), generatePhone());
    }
    
    private int validateTuoi(int tuoi) {
        if (tuoi < 18) {
            throw new IllegalArgumentException("Tuổi khách hàng phải >= 18. Tuổi nhập: " + tuoi);
        }
        return tuoi;
    }
    
    private String validateGioiTinh(String gioiTinh) {
        if (!gioiTinh.equalsIgnoreCase("Male") && !gioiTinh.equalsIgnoreCase("Female")) {
            throw new IllegalArgumentException("Giới tính phải là 'Male' hoặc 'Female'. Giá trị nhập: " + gioiTinh);
        }
        return gioiTinh;
    }

    private static String generateEmail(String ten) {
        String emailName = ten.toLowerCase()
                             .replaceAll("\\s+", ".")
                             .replaceAll("[^a-z0-9.]", "")
                             .replaceAll("\\.+", ".")
                             .replaceAll("^\\.|\\.$", "");
        return emailName + "@email.com";
    }
    
    private static String generatePhone() {
        String[] prefixes = {"09", "08", "07", "03"};
        String prefix = prefixes[(int)(Math.random() * prefixes.length)];
        String randomNumbers = String.format("%08d", (int)(Math.random() * 100000000));
        String phone = prefix + randomNumbers;
        return phone.replaceAll("(\\d{2})(\\d{8})", "$1$2");
    }

    // Getters
    public int getId() { return id; }
    public String getTen() { return ten; }
    public int getTuoi() { return tuoi; }
    public String getGend() { return gend; }
    public String getEmail() { return email; }
    public String getPhone() { return phone; }

    // Setters có kiểm tra regex
    public void setEmail(String email) { this.email = validateEmail(email); }
    public void setPhone(String phone) { this.phone = validatePhone(phone); }

    // Con trỏ nút trái/phải
    public KhachHang getTrai() { return trai; }
    public KhachHang getPhai() { return phai; }
    public void setTrai(KhachHang trai) { this.trai = trai; }
    public void setPhai(KhachHang phai) { this.phai = phai; }

    // Validators
    private String validateEmail(String email) {
        if (email == null || !EMAIL_PATTERN.matcher(email.trim()).matches()) {
            throw new IllegalArgumentException("Email không hợp lệ (vd: user@example.com).");
        }
        return email.trim();
    }

    private String validatePhone(String phone) {
        if (phone == null) {
            throw new IllegalArgumentException("Số điện thoại không được null.");
        }
        String normalized = phone.replaceAll("\\s+", ""); // bỏ khoảng trắng
        if (!PHONE_PATTERN.matcher(normalized).matches()) {
            throw new IllegalArgumentException("SĐT không hợp lệ. Yêu cầu: bắt đầu 09/08/07/03 + 8 số (tổng 10 số).");
        }
        return normalized;
    }

    @Override
    public String toString() {
        return String.format("KhachHang [id=%d, ten=%s, tuoi=%d, gend=%s, email=%s, phone=%s]", 
                           id, ten, tuoi, gend, email, phone);
    }
}
