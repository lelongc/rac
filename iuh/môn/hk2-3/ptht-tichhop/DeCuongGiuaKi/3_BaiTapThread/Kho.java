package BaiTapThread;

public class Kho {
    private int sucChua;
    private int tonKho = 0;

    public Kho(int sucChua) {
        this.sucChua = sucChua;
    }

    public synchronized void nhapKho(int soLuong, String tenNguoi) throws InterruptedException {
        while (tonKho + soLuong > sucChua) {
            System.out.println(tenNguoi + " muon nhap " + soLuong + ". Kho day, dang doi...");
            wait();
        }
        tonKho += soLuong;
        System.out.println(tenNguoi + " da nhap " + soLuong + ". Ton kho hien tai: " + tonKho);
        notifyAll();
    }

    public synchronized void xuatKho(int soLuong, String tenNguoi) throws InterruptedException {
        while (tonKho < soLuong) {
            System.out.println(tenNguoi + " muon xuat " + soLuong + ". Kho thieu, dang doi...");
            wait();
        }
        tonKho -= soLuong;
        System.out.println(tenNguoi + " da xuat " + soLuong + ". Ton kho hien tai: " + tonKho);
        notifyAll();
    }
}
