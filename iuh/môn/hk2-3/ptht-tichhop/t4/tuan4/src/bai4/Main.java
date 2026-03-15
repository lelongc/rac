package bai4;

import java.io.File;

public class Main {
    public static void main(String[] args) throws Exception {
        // Lấy thư mục bin/bai4, đổi bin → src để lưu vào thư mục source
        String binDir = new File(Main.class.getResource("Main.class").toURI()).getParent();
        String dir = binDir.replace(File.separator + "bin" + File.separator,
                                    File.separator + "src" + File.separator);
        System.out.println("Luu file vao: " + dir);

        String filename = dir + File.separator + "shared_file.txt";
        new File(filename).delete();

        FileBuffer buf = new FileBuffer(filename);

        FileWriterThread writer = new FileWriterThread(buf, 10);
        FileReaderThread reader = new FileReaderThread(buf, 10);

        writer.start();
        reader.start();
    }
}