package BaiTapThread;

import java.util.Random;

public class NguoiTieuDung extends Thread {
    private Kho kho;
    private String tenKH;

    public NguoiTieuDung(Kho kho, String tenKH) {
        this.kho = kho;
        this.tenKH = tenKH;
    }

    @Override
    public void run() {
        Random rand = new Random();
        try {
            for (int i = 0; i < 5; i++) {
                int m = 1 + rand.nextInt(5);
                kho.xuatKho(m, tenKH);
                Thread.sleep(700 + rand.nextInt(1000)); 
            }
        } catch (InterruptedException e) {
            System.out.println(tenKH + " ket thuc dot tieu dung.");
        }
    }
}
