package BaiTapThread;

public class Main {
    public static void main(String[] args) {
        FileBuffer buffer = new FileBuffer();

        WriterThread writer = new WriterThread(buffer);
        ReaderThread reader = new ReaderThread(buffer);

        writer.start();
        reader.start();
    }
}
