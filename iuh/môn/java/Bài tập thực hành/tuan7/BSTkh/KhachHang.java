package BSTkh;

import java.util.regex.Pattern;

public class KhachHang {
    private int id;
    private String ten;
    private int tuoi;
    private String gend;
    private String email;
    private String phone;
    
    // Regex patterns
    private static final Pattern EMAIL_PATTERN = Pattern.compile("^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$");
    private static final Pattern PHONE_PATTERN = Pattern.compile("^(09|08|07|03)\\d{8}$");
    
    public KhachHang(int id, String ten, int tuoi, String gend, String email, String phone) {
        super();
        this.id = id;
        this.ten = ten;
        this.tuoi = validateTuoi(tuoi);
        this.gend = validateGioiTinh(gend);
        this.email = validateEmail(email);
        this.phone = validatePhone(phone);
    }
    
    // Constructor cũ để tương thích
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
    
    private String validateEmail(String email) {
        if (email == null || !EMAIL_PATTERN.matcher(email).matches()) {
            throw new IllegalArgumentException("Email không hợp lệ. Email nhập: " + email);
        }
        return email;
    }
    
    private String validatePhone(String phone) {
        if (phone == null || !PHONE_PATTERN.matcher(phone).matches()) {
            throw new IllegalArgumentException("Số điện thoại không hợp lệ. Phải có 10 số bắt đầu 09/08/07/03. Phone nhập: " + phone);
        }
        return phone;
    }
    
    private static String generateEmail(String ten) {
        // Chuyển về lowercase, thay khoảng trắng thành dấu chấm, loại bỏ ký tự đặc biệt
        String emailName = ten.toLowerCase()
                             .replaceAll("\\s+", ".")
                             .replaceAll("[^a-z0-9.]", "");
        return emailName + "@email.com";
    }
    
    private static String generatePhone() {
        String[] prefixes = {"09", "08", "07", "03"};
        String prefix = prefixes[(int)(Math.random() * prefixes.length)];
        return prefix + String.format("%08d", (int)(Math.random() * 100000000));
    }

    // Getters
    public int getId() {
        return id;
    }

    public String getTen() {
        return ten;
    }

    public int getTuoi() {
        return tuoi;
    }

    public String getGend() {
        return gend;
    }
    
    public String getEmail() {
        return email;
    }
    
    public String getPhone() {
        return phone;
    }

    @Override
    public String toString() {
        return String.format("KhachHang [id=%d, ten=%s, tuoi=%d, gend=%s, email=%s, phone=%s]", 
                           id, ten, tuoi, gend, email, phone);
    }
}
