package BaiTapThread;

import java.io.*;

public class FileTReader extends Thread {
    private String tenTapTin;

    public FileTReader(String tenTapTin) {
        this.tenTapTin = tenTapTin;
    }

    @Override
    public void run() {
        File file = new File(tenTapTin);
        if (!file.exists()) {
            System.out.println(Thread.currentThread().getName() + " Loi: File " + tenTapTin + " ko ton tai!");
            return;
        }

        try (BufferedReader br = new BufferedReader(new FileReader(file))) {
            String line;
            System.out.println(Thread.currentThread().getName() + " BAT DAU DOC " + tenTapTin);
            while ((line = br.readLine()) != null) {
                System.out.println(Thread.currentThread().getName() + " doc duoc tu " + tenTapTin + ": " + line);
                Thread.sleep(500);
            }
            System.out.println(Thread.currentThread().getName() + " HOAN THANH DOC TỪ " + tenTapTin);
        } catch (IOException | InterruptedException e) {
            System.err.println("Loi khi doc file: " + e.getMessage());
        }
    }
}
