package BaiTapThread;

public class Main {
    public static void main(String[] args) {
        System.out.println("===== CHON BAI TAP TUAN 4 THREAD (BO COMMENT DE CHAY) =====");
        
        // =========================================================================
        // DANG 1 (Bai 2): Viet so ngau nhien vao 3 tap tin bang 3 Thread rieng biet
        // =========================================================================
        /*
        FileTWriter w1 = new FileTWriter("file1.txt");
        FileTWriter w2 = new FileTWriter("file2.txt");
        FileTWriter w3 = new FileTWriter("file3.txt");
        w1.start(); w2.start(); w3.start();
        */

        // =========================================================================
        // DANG 2 (Bai 3): Doc noi dung 3 tap tin bang 3 Thread rieng biet
        // =========================================================================
        /*
        FileTReader r1 = new FileTReader("file1.txt");
        FileTReader r2 = new FileTReader("file2.txt");
        FileTReader r3 = new FileTReader("file3.txt");
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
