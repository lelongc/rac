package BaiTapThread;

public class Main {
    public static void main(String[] args) {
        System.out.println("===== CHON BAI TAP TUAN 4 THREAD (BO COMMENT DE CHAY) =====");
        
        // =========================================================================
        // CAU HINH THU MUC LUU FILE (DE FILE KHONG BI LAC RA NGOAI KHI CHAY ECLIPSE)
        // =========================================================================
        String DIR = "DeCuongGiuaKi/3_BaiTapThread/";

        // =========================================================================
        // DANG 0: HUONG DAN CO BAN (TAO KHOI DONG THREAD BANG THREAD HOAC RUNNABLE)
        // =========================================================================
        /*
        // Cach 1: Extends Thread (Da xay dung san class Thread con)
        Thread t1 = new Thread() {
            @Override
            public void run() {
                System.out.println("Cach 1 (Thread): Dang chay...");
            }
        };
        t1.start();

        // Cach 2: Implements Runnable
        Runnable r1 = new Runnable() {
            @Override
            public void run() {
                System.out.println("Cach 2 (Runnable): Dang chay...");
            }
        };
        Thread t2 = new Thread(r1);
        t2.start();
        */

        // =========================================================================
        // DANG 1 (Bai 2): Viet so ngau nhien vao 3 tap tin bang 3 Thread rieng biet
        // =========================================================================
        /*
        FileTWriter w1 = new FileTWriter(DIR + "file1.txt");
        FileTWriter w2 = new FileTWriter(DIR + "file2.txt");
        FileTWriter w3 = new FileTWriter(DIR + "file3.txt");
        w1.start(); w2.start(); w3.start();
        */

        // =========================================================================
        // DANG 2 (Bai 3): Doc noi dung 3 tap tin bang 3 Thread rieng biet
        // =========================================================================
        /*
        FileTReader r1 = new FileTReader(DIR + "file1.txt");
        FileTReader r2 = new FileTReader(DIR + "file2.txt");
        FileTReader r3 = new FileTReader(DIR + "file3.txt");
        r1.start(); r2.start(); r3.start();
        */

        // =========================================================================
        // DANG 3 (Bai 4): Dong bo hoa Doc/Ghi cung 1 file (Wait/Notify buffer)
        // =========================================================================
        /*
        FileBuffer buffer = new FileBuffer();
        WriterThread writer = new WriterThread(buffer);
        ReaderThread reader = new ReaderThread(buffer);
        writer.start();
        reader.start();
        */

        // =========================================================================
        // DANG 4 (Bai 5): Nguoi San Xuat - Nguoi Tieu Dung (Producer - Consumer)
        // =========================================================================
        /*
        DemoProducerConsumer.main(null);
        */

        // =========================================================================
        // DANG 5 (Tuan 6 / Thread): Vung nho dem nhap ban phim & tinh tong
        // =========================================================================
        /*
        BufferApp.main(null);
        */
    }
}
