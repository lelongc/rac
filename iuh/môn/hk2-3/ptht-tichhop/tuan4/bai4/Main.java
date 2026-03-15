package bai4;

import java.io.File;

public class Main {
    public static void main(String[] args) throws Exception {
        // Lấy thư mục chứa Main.class (= thư mục bai4)
        String dir = new File(Main.class.getResource("Main.class").toURI()).getParent();

        String filename = dir + File.separator + "shared_file.txt";
        new File(filename).delete();

        FileBuffer buf = new FileBuffer(filename);

        FileWriterThread writer = new FileWriterThread(buf, 10);
        FileReaderThread reader = new FileReaderThread(buf, 10);

        writer.start();
        reader.start();
    }
}