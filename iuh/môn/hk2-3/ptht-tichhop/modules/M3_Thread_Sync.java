// ============================================================
// MODULE 3 – THREAD ĐỒNG BỘ (synchronized + wait/notifyAll)
// Dùng khi đề: "Producer-Consumer, Kho, Buffer đọc-ghi"
// Ghép với: M2 (thread), M1 (object được share)
// ============================================================

// ── SHARED RESOURCE (Kho / Buffer) ───────────────────────────
class SharedResource {                  // TODO: đổi tên (Kho, Buffer,...)
    private int    capacity;            // sức chứa tối đa
    private int    current = 0;         // giá trị hiện tại

    public SharedResource(int capacity) {
        this.capacity = capacity;
    }

    // PRODUCER gọi: nhập / ghi
    public synchronized void produce(int amount, String who) throws InterruptedException {
        while (current + amount > capacity) {   // chờ khi đầy
            System.out.println(who + " cho (day)...");
            wait();
        }
        current += amount;
        System.out.println(who + " +=" + amount + "  | hien tai: " + current);
        notifyAll();
    }

    // CONSUMER gọi: xuất / đọc
    public synchronized void consume(int amount, String who) throws InterruptedException {
        while (current < amount) {              // chờ khi thiếu
            System.out.println(who + " cho (thieu)...");
            wait();
        }
        current -= amount;
        System.out.println(who + " -=" + amount + "  | hien tai: " + current);
        notifyAll();
    }

    public synchronized int getCurrent() { return current; }
}

// ── PRODUCER THREAD ──────────────────────────────────────────
class Producer extends Thread {
    private SharedResource res;
    private String name;

    public Producer(SharedResource res, String name) {
        this.res  = res;
        this.name = name;
    }

    @Override
    public void run() {
        java.util.Random rand = new java.util.Random();
        try {
            for (int i = 0; i < 8; i++) {       // TODO: số lần sản xuất
                int amt = 1 + rand.nextInt(3);
                res.produce(amt, name);
                Thread.sleep(300 + rand.nextInt(500));
            }
        } catch (InterruptedException e) {
            System.out.println(name + " ket thuc.");
        }
    }
}

// ── CONSUMER THREAD ──────────────────────────────────────────
class Consumer extends Thread {
    private SharedResource res;
    private String name;

    public Consumer(SharedResource res, String name) {
        this.res  = res;
        this.name = name;
    }

    @Override
    public void run() {
        java.util.Random rand = new java.util.Random();
        try {
            for (int i = 0; i < 8; i++) {       // TODO: số lần tiêu thụ
                int amt = 1 + rand.nextInt(3);
                res.consume(amt, name);
                Thread.sleep(400 + rand.nextInt(600));
            }
        } catch (InterruptedException e) {
            System.out.println(name + " ket thuc.");
        }
    }
}

// ── MAIN ─────────────────────────────────────────────────────
public class M3_Thread_Sync {
    public static void main(String[] args) throws InterruptedException {
        SharedResource kho = new SharedResource(10); // sức chứa 10

        Producer p1 = new Producer(kho, "P1");
        Producer p2 = new Producer(kho, "P2");
        Consumer c1 = new Consumer(kho, "C1");
        Consumer c2 = new Consumer(kho, "C2");

        p1.start(); p2.start();
        c1.start(); c2.start();

        p1.join(); p2.join();
        c1.join(); c2.join();
        System.out.println("Xong. Ton kho cuoi: " + kho.getCurrent());
    }
}
