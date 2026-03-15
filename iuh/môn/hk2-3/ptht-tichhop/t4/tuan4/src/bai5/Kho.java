package bai5;
public class Kho {
    private int sucChua;
    private int tonKho = 0;

    public Kho(int sucChua) {
        this.sucChua = sucChua;
    }

    public synchronized void nhapKho(int soLuong, String tenNguoi) throws InterruptedException {
        while (tonKho + soLuong > sucChua) {
            System.out.println(tenNguoi + " muon nhap " + soLuong + ". khong du cho , wait nhap kho...");
            wait();
        }
        tonKho += soLuong;
        System.out.println(tenNguoi + " da nhap " + soLuong + ". Tồn kho: " + tonKho);
        notifyAll();
    }

    public synchronized void xuatKho(int soLuong, String tenNguoi) throws InterruptedException {
        while (tonKho < soLuong) {
            System.out.println(tenNguoi + " muon xuat " + soLuong + ". khong du hang , cho xuat kho...");
            wait();
        }
        tonKho -= soLuong;
        System.out.println(tenNguoi + " da xuat " + soLuong + ". ton kho: " + tonKho);
        notifyAll();
    }

    public synchronized int getTonKho() {
        return tonKho;
    }
}