package tuan2b;

public class PhuongTien {
    String hangSanXuat;
    int namSanXuat;
    double giaBan;

    public PhuongTien(String hangSanXuat, int namSanXuat, double giaBan) {
        this.hangSanXuat = hangSanXuat;
        this.namSanXuat = namSanXuat;
        this.giaBan = giaBan;
    }

    public void hienThiThongTin() {
        System.out.println("Hang: " + hangSanXuat + ", Nam: " + namSanXuat + ", Gia: " + giaBan);
    }
}
