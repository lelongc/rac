package thread;

// CÁCH 1: Kế thừa Thread
public class C1_ExtendsThread extends Thread {
    String tenThread;
    int soLan;

    public C1_ExtendsThread(String tenThread, int soLan) {
        this.tenThread = tenThread;
        this.soLan = soLan;
        System.out.println("Da tao: " + tenThread);
    }

    @Override
    public void run() {
        for (int i = 1; i <= soLan; i++) {
            System.out.println(tenThread + " - lan thu " + i);
        }
        System.out.println(tenThread + " da hoan thanh!");
    }

    public static void main(String[] args) {
        System.out.println("=== CACH 1: extends Thread ===");

        C1_ExtendsThread t1 = new C1_ExtendsThread("Thread-A", 3);
        C1_ExtendsThread t2 = new C1_ExtendsThread("Thread-B", 3);
        C1_ExtendsThread t3 = new C1_ExtendsThread("Thread-C", 3);

        // Bắt đầu chạy song song
        t1.start();
        t2.start();
        t3.start();

        System.out.println("Main thread tiep tuc chay...");
    }
}
