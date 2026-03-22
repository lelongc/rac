package BaiTapThread;

public class FileBuffer {
    private boolean hasNewData = false;

    public synchronized void writeData(String data) throws InterruptedException {
        while (hasNewData) {
            wait();
        }
        System.out.println("Writer ghi: " + data);
        hasNewData = true;
        notifyAll();
    }

    public synchronized void readData() throws InterruptedException {
        while (!hasNewData) {
            wait();
        }
        System.out.println("Reader doc du lieu moi nhat (Da xu ly).");
        hasNewData = false;
        notifyAll();
    }
}
