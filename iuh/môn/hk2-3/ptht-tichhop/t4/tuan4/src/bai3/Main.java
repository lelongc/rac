package bai3;

import java.io.File;
import java.io.FileWriter;

public class Main {
    public static void main(String[] args) throws Exception {
        // Lấy thư mục bin/bai3, đổi bin → src để lưu vào thư mục source
        String binDir = new File(Main.class.getResource("Main.class").toURI()).getParent();
        String dir = binDir.replace(File.separator + "bin" + File.separator,
                                    File.separator + "src" + File.separator);
        System.out.println("Luu file vao: " + dir);

        // Tạo sẵn 3 file mẫu để đọc
        String[] files = {
            dir + File.separator + "file11.txt",
            dir + File.separator + "file22.txt",
            dir + File.separator + "file33.txt"
        };
        for (int i = 0; i < files.length; i++) {
            try (FileWriter fw = new FileWriter(files[i])) {
                for (int j = 1; j <= 5; j++) {
                    fw.write("file" + (i + 1) + " dong " + j + "\n");
                }
            }
        }

        //c1 extends Thread
        //FileTReader t1 = new FileTReader(files[0]);
        //FileTReader t2 = new FileTReader(files[1]);
        //FileTReader t3 = new FileTReader(files[2]);
        //t1.start(); t2.start(); t3.start();

        //c2 implements Runnable
        Thread t1 = new Thread(new FileTReader(files[0]));
        Thread t2 = new Thread(new FileTReader(files[1]));
        Thread t3 = new Thread(new FileTReader(files[2]));

        t1.start();
        t2.start();
        t3.start();
    }
}