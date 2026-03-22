package OOP_IOStream;

public class DongVat {
    protected String loai;
    protected String ten;
    protected int tuoi;

    public DongVat(String loai, String ten, int tuoi) {
        this.loai = loai;
        this.ten = ten;
        this.tuoi = tuoi;
    }

    public void inThongTin() {
        System.out.println("Loai: " + loai + " | Ten: " + ten + " | Tuoi: " + tuoi);
    }
    public void an() { System.out.println(ten + " dang an..."); }
    public void ngu() { System.out.println(ten + " dang ngu..."); }
    public void taoAmThanh() { System.out.println(ten + " dang tao am thanh..."); }
}
