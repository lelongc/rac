// ============================================================
// MODULE 2 – THREAD (extends Thread / implements Runnable)
// Dùng khi đề: "Tạo thread xử lý tác vụ song song, ghi file..."
// Ghép với: M3 (đồng bộ), M5/M6 (ClientHandler là thread)
// ============================================================
import java.io.*;
import java.util.Random;

// ── CÁCH 1: extends Thread ───────────────────────────────────
class MyTask extends Thread {
    private String taskName;
    private int    count;

    public MyTask(String taskName, int count) {
        this.taskName = taskName;
        this.count    = count;
        // this.setName(taskName); // đặt tên thread (tuỳ)
    }

    @Override
    public void run() {
        try {
            for (int i = 1; i <= count; i++) {
                System.out.println("[" + taskName + "] buoc " + i);
                // TODO: thêm xử lý thực tế ở đây
                Thread.sleep(200);          // giả lập tốn thời gian
            }
            System.out.println("[" + taskName + "] XONG");
        } catch (InterruptedException e) {
            System.out.println("[" + taskName + "] bi ngat");
        }
    }
}

// ── CÁCH 2: implements Runnable (linh hoạt hơn) ──────────────
class FileWriter_R implements Runnable {    // TODO: đổi tên
    private String filename;

    public FileWriter_R(String filename) {
        this.filename = filename;
    }

    @Override
    public void run() {
        Random rand = new Random();
        try (FileWriter fw = new FileWriter(filename)) {
            for (int i = 0; i < 10; i++) {
                fw.write(rand.nextInt(1000) + "\n");
                Thread.sleep(100);
            }
            System.out.println(Thread.currentThread().getName() + " ghi xong: " + filename);
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}

// ── MAIN ─────────────────────────────────────────────────────
public class M2_Thread {
    public static void main(String[] args) throws InterruptedException {

        // --- Cách 1: extends Thread ---
        MyTask t1 = new MyTask("T1", 5);
        MyTask t2 = new MyTask("T2", 5);
        t1.start();
        t2.start();
        t1.join();   // chờ t1 xong rồi mới tiếp
        t2.join();
        System.out.println("Ca hai thread da xong");

        // --- Cách 2: implements Runnable ---
        // Thread r1 = new Thread(new FileWriter_R("file1.txt"), "Writer1");
        // Thread r2 = new Thread(new FileWriter_R("file2.txt"), "Writer2");
        // r1.start(); r2.start();
        // r1.join();  r2.join();
    }
}
