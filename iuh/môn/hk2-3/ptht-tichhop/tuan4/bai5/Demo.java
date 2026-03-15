package bai5;

public class Demo {
    public static void main(String[] args) {
        Kho kho = new Kho(10);

        NguoiSanXuat nsx1 = new NguoiSanXuat(kho, "NSX01");
        NguoiSanXuat nsx2 = new NguoiSanXuat(kho, "NSX02");
        NguoiTieuDung ntd1 = new NguoiTieuDung(kho, "NTD01");
        NguoiTieuDung ntd2 = new NguoiTieuDung(kho, "NTD02");

        nsx1.start();
        nsx2.start();
        ntd1.start();
        ntd2.start();
    }
}