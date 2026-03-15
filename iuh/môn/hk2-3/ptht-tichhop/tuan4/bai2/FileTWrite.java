package bai2;

import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;
//c1 kế thừa Thread
//public class FileTWrite extends Thread {
//    private String filename;
//
//    public FileTWrite(String filename) {
//        this.filename = filename;
//    }
//
//    @Override
//    public void run() {
//        Random rand = new Random();
//        try (FileWriter fw = new FileWriter(filename)) {
//            for (int i = 0; i < 10; i++) {
//                int num = rand.nextInt(100); 
//                fw.write(num + "\n");
//            }
//            System.out.println("da ghi file: " + filename);
//        } catch (IOException e) {
//            e.printStackTrace();
//        }
//    }
//}



//c2 interface Runnable
public class FileTWrite implements Runnable {
    private String filename;

    public FileTWrite(String filename) {
        this.filename = filename;
    }

    @Override
    public void run() {
        Random rand = new Random();
        try (FileWriter fw = new FileWriter(filename)) {
            for (int i = 0; i < 10; i++) {
                int num = rand.nextInt(100); 
                fw.write(num + "\n");
            }
            System.out.println("da ghi: " + filename);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}