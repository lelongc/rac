package bai4;

import java.io.FileWriter;
import java.util.Random;

public class FileWriterThread extends Thread {
    private FileBuffer buffer;
    private int soLan;

    public FileWriterThread(FileBuffer buffer, int soLan) {
        this.buffer = buffer;
        this.soLan = soLan;
    }

    @Override
    public void run() {
        try {
            for (int i = 1; i <= soLan; i++) {
                String data = "dong so " + i + ": " + (int)(Math.random()*100);
                buffer.writeLine(data);
                Thread.sleep(300);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}