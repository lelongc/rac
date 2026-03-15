package bai4;
import java.io.File;


public class Main {
    public static void main(String[] args) {
        String filename = "shared_file.txt";
        new File(filename).delete();

        FileBuffer buf = new FileBuffer(filename);

        FileWriterThread writer = new FileWriterThread(buf, 10);
        FileReaderThread reader = new FileReaderThread(buf, 10);

        writer.start();
        reader.start();
    }
}