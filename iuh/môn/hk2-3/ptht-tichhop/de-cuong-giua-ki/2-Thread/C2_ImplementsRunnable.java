package thread;

// CÁCH 2: Implements Runnable
public class C2_ImplementsRunnable implements Runnable {
    String tenThread;
    int soLan;

    public C2_ImplementsRunnable(String tenThread, int soLan) {
        this.tenThread = tenThread;
        this.soLan = soLan;
    }

    @Override
    public void run() {
        for (int i = 1; i <= soLan; i++) {
            System.out.println(tenThread + " - lan thu " + i);
        }
        System.out.println(tenThread + " da hoan thanh!");
    }

    public static void main(String[] args) {
        System.out.println("=== CACH 2: implements Runnable ===");

        C2_ImplementsRunnable r1 = new C2_ImplementsRunnable("Runnable-A", 3);
        C2_ImplementsRunnable r2 = new C2_ImplementsRunnable("Runnable-B", 3);

        // Truyền Runnable vào Thread để chạy
        Thread t1 = new Thread(r1);
        Thread t2 = new Thread(r2);

        t1.start();
        t2.start();
    }
}
