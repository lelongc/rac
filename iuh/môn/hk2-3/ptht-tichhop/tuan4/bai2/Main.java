package bai2;

import java.io.File;

public class Main {
    public static void main(String[] args) throws Exception {
        // Lấy thư mục chứa Main.class (= thư mục bai2)
        String dir = new File(Main.class.getResource("Main.class").toURI()).getParent();

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