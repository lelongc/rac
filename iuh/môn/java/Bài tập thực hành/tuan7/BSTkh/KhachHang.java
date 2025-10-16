package BSTkh;

public class KhachHang {
    private int id;
    private String ten;
    private int tuoi;
    private String gend;
    private String email;
    private String phone;
    
    public KhachHang(int id, String ten, int tuoi, String gend, String email, String phone) {
        super();
        this.id = id;
        this.ten = ten;
        this.tuoi = validateTuoi(tuoi);
        this.gend = validateGioiTinh(gend);
        this.email = email;
        this.phone = phone;
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
    
    private static String generateEmail(String ten) {
        return ten.toLowerCase().replace(" ", ".") + "@email.com";
    }
    
    private static String generatePhone() {
        return "09" + String.format("%08d", (int)(Math.random() * 100000000));
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
