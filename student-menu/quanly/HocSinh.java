package quanly;

import java.io.Serializable;

public class HocSinh implements Serializable {
    private static final long serialVersionUID = 1L;

    private String maHS;
    private String tenHS;
    private double diem;
    private String xepLoai;

    // THAY ĐỔI: Constructor không còn tự kiểm tra điểm
    public HocSinh(String maHS, String tenHS, double diem) {
        this.maHS = maHS;
        this.tenHS = tenHS;
        this.diem = diem;
        this.capNhatXepLoai(); // Xếp loại vẫn được tự động cập nhật
    }

    // Getters
    public String getMaHS() { return maHS; }
    public String getTenHS() { return tenHS; }
    public double getDiem() { return diem; }
    public String getXepLoai() { return xepLoai; }
    
    // Setters
    public void setDiem(double diem) {
        this.diem = diem;
        this.capNhatXepLoai();
    }
    
    private void capNhatXepLoai() {
        if (this.diem >= 8.5) this.xepLoai = "Gioi";
        else if (this.diem >= 6.5) this.xepLoai = "Kha";
        else if (this.diem >= 5.0) this.xepLoai = "Trung Binh";
        else this.xepLoai = "Yeu";
    }

    @Override
    public String toString() {
        return String.format("%-10s | %-25s | %-10.2f | %-15s", 
                             maHS, tenHS, diem, xepLoai);
    }
}