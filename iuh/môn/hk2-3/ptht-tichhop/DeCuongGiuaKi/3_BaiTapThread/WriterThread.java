package BaiTapThread;

public class WriterThread extends Thread {
    private FileBuffer buffer;

    public WriterThread(FileBuffer buffer) {
        this.buffer = buffer;
    }

    @Override
    public void run() {
        try {
            for (int i = 1; i <= 5; i++) {
                String data = "Du lieu thu " + i;
                buffer.writeData(data);
                Thread.sleep(500); 
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
