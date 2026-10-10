package gkrmi;

import java.io.Serializable;

public class SinhVien implements Serializable {
    private static final long serialVersionUID = 1L;

    private String maSV;
    private String hoTen;
    private double diemTB;

    public SinhVien() {
    }

    public SinhVien(String maSV, String hoTen, double diemTB) {
        this.maSV = maSV;
        this.hoTen = hoTen;
        this.diemTB = diemTB;
    }

    public String getMaSV() {
        return maSV;
    }

    public void setMaSV(String maSV) {
        this.maSV = maSV;
    }

    public String getHoTen() {
        return hoTen;
    }

    public void setHoTen(String hoTen) {
        this.hoTen = hoTen;
    }

    public double getDiemTB() {
        return diemTB;
    }

    public void setDiemTB(double diemTB) {
        this.diemTB = diemTB;
    }

    public String rank() {
        if (diemTB >= 8.5) return "Xuat sac";
        if (diemTB >= 7.0) return "Kha / Gioi";
        if (diemTB >= 5.0) return "Trung binh";
        return "Yeu";
    }

    @Override
    public String toString() {
        return "SinhVien [Ma=" + maSV + ", HoTen=" + hoTen + ", DiemTB=" + diemTB + ", XepLoai=" + rank() + "]";
    }
}
