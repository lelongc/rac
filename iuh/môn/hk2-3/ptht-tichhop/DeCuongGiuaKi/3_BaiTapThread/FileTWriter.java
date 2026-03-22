package BaiTapThread;

import java.io.*;
import java.util.Random;

public class FileTWriter extends Thread {
    private String tenTapTin;

    public FileTWriter(String tenTapTin) {
        this.tenTapTin = tenTapTin;
    }

    @Override
    public void run() {
        try (PrintWriter pw = new PrintWriter(new FileWriter(tenTapTin))) {
            Random rand = new Random();
            for (int i = 0; i < 10; i++) {
                int n = rand.nextInt(100);
                pw.println(n);
                System.out.println(Thread.currentThread().getName() + " da ghi so: " + n + " vao " + tenTapTin);
                Thread.sleep(500); 
            }
            System.out.println(Thread.currentThread().getName() + " HOAN THANH GHI VÀO " + tenTapTin);
        } catch (IOException | InterruptedException e) {
            System.err.println("Loi khi ghi file: " + e.getMessage());
        }
    }
}
