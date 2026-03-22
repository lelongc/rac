package BaiTapThread;

import java.util.Random;

public class NguoiSanXuat extends Thread {
    private Kho kho;
    private String tenSP;

    public NguoiSanXuat(Kho kho, String tenSP) {
        this.kho = kho;
        this.tenSP = tenSP;
    }

    @Override
    public void run() {
        Random rand = new Random();
        try {
            for (int i = 0; i < 5; i++) {
                int n = 1 + rand.nextInt(5); 
                kho.nhapKho(n, tenSP);
                Thread.sleep(500 + rand.nextInt(1000));
            }
        } catch (InterruptedException e) {
            System.out.println(tenSP + " ket thuc dot xuan xuat.");
        }
    }
}
