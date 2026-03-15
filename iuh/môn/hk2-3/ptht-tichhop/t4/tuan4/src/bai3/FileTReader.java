package bai3;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
//c1
//public class FileTReader extends Thread {
//    private String filename;
//
//    public FileTReader(String filename) {
//        this.filename = filename;
//    }
//
//    @Override
//    public void run() {
//        System.out.println("doc file: " + filename);
//        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
//            String line;
//            while((line = br.readLine()) != null) {
//                System.out.println("[" + filename + "] " + line);
//            }
//        } catch (IOException e) {
//            System.out.println("khong doc duoc file: " + filename);
//            e.printStackTrace();
//        }
//    }
//}

//c2

public class FileTReader implements Runnable {
    private String filename;

    public FileTReader(String filename) {
        this.filename = filename;
    }

    @Override
    public void run() {
        System.out.println("doc file: " + filename);
        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            String line;
            while((line = br.readLine()) != null) {
                System.out.println("[" + filename + "] " + line);
            }
        } catch (IOException e) {
            System.out.println("khong doc duoc file: " + filename);
            e.printStackTrace();
        }
    }
}