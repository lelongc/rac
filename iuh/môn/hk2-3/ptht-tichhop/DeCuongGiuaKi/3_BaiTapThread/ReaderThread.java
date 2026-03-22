package BaiTapThread;

public class ReaderThread extends Thread {
    private FileBuffer buffer;

    public ReaderThread(FileBuffer buffer) {
        this.buffer = buffer;
    }

    @Override
    public void run() {
        try {
            for (int i = 1; i <= 5; i++) {
                buffer.readData();
                Thread.sleep(800);
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
