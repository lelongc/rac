package bai4;
public class FileReaderThread extends Thread {
    private FileBuffer buffer;
    private int soLan;

    public FileReaderThread(FileBuffer buffer, int soLan) {
        this.buffer = buffer;
        this.soLan = soLan;
    }

    @Override
    public void run() {
        int lineIndex = 0;
        try {
            for (int i = 1; i <= soLan; i++) {
                String line = buffer.readNewLine(lineIndex++);
                System.out.println("Reader doc: " + line);
                Thread.sleep(400); 
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}