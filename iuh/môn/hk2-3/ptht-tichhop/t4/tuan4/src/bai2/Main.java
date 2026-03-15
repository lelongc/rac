package bai2;

import java.io.File;

public class Main {
    public static void main(String[] args) throws Exception {
        // Lấy thư mục bin/bai2 (nơi chứa .class)
        String binDir = new File(Main.class.getResource("Main.class").toURI()).getParent();
        // Đổi bin → src để lưu file vào thư mục source
        String dir = binDir.replace(File.separator + "bin" + File.separator,
                                    File.separator + "src" + File.separator);
        System.out.println("Luu file vao: " + dir);

        //c1 extends Thread
        //FileTWrite t1 = new FileTWrite(dir + File.separator + "file1.txt");
        //FileTWrite t2 = new FileTWrite(dir + File.separator + "file2.txt");
        //FileTWrite t3 = new FileTWrite(dir + File.separator + "file3.txt");
        //t1.start(); t2.start(); t3.start();

        //c2 implements Runnable
        Thread t1 = new Thread(new FileTWrite(dir + File.separator + "file11.txt"));
        Thread t2 = new Thread(new FileTWrite(dir + File.separator + "file22.txt"));
        Thread t3 = new Thread(new FileTWrite(dir + File.separator + "file33.txt"));

        t1.start();
        t2.start();
        t3.start();
    }
}