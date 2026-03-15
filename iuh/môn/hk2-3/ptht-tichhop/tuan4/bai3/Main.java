package bai3;

import java.io.File;
import java.io.FileWriter;

public class Main {
    public static void main(String[] args) throws Exception {
        // Lấy thư mục chứa Main.class (= thư mục bai3)
        String dir = new File(Main.class.getResource("Main.class").toURI()).getParent();

        // Tạo sẵn 3 file mẫu trong bai3/ để đọc
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
        System.out.println("Da tao file mau trong: " + dir);

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