package thread;

// CÁCH 3: Dùng sleep() và join()
public class C3_ThreadSleepJoin extends Thread {
    String tenThread;

    public C3_ThreadSleepJoin(String tenThread) {
        this.tenThread = tenThread;
    }

    @Override
    public void run() {
        for (int i = 1; i <= 3; i++) {
            System.out.println(tenThread + " - buoc " + i);
            try {
                Thread.sleep(500); // ngủ 500ms giữa mỗi bước
            } catch (InterruptedException e) {
                System.out.println(tenThread + " bi ngat!");
            }
        }
        System.out.println(tenThread + " da xong!");
    }

    public static void main(String[] args) throws InterruptedException {
        System.out.println("=== sleep() va join() ===");

        C3_ThreadSleepJoin t1 = new C3_ThreadSleepJoin("T1");
        C3_ThreadSleepJoin t2 = new C3_ThreadSleepJoin("T2");
        C3_ThreadSleepJoin t3 = new C3_ThreadSleepJoin("T3");

        t1.start();
        t2.start();
        t3.start();

        // join(): main chờ t1, t2, t3 chạy xong mới tiếp tục
        t1.join();
        t2.join();
        t3.join();

        System.out.println("Tat ca thread da xong! Main ket thuc.");
    }
}
