import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class BufferApp {

    private static final Queue<Integer> buffer = new LinkedList<>();
    private static boolean done = false;
    private static final Object lock = new Object();

    // Thread 1: nhận số từ bàn phím, đưa vào buffer; dừng khi nhập -1
    static class Producer extends Thread {
        @Override
        public void run() {
            Scanner scanner = new Scanner(System.in);
            System.out.println("Thread 1 (Producer): Nhập các số nguyên (nhập -1 để dừng):");
            while (true) {
                System.out.print("Nhập số: ");
                int num = scanner.nextInt();
                synchronized (lock) {
                    buffer.offer(num);
                    lock.notify();
                    if (num == -1) {
                        done = true;
                        break;
                    }
                }
            }
            scanner.close();
        }
    }

    // Thread 2: lấy số từ buffer, tính tổng
    static class Consumer extends Thread {
        @Override
        public void run() {
            int sum = 0;
            System.out.println("Thread 2 (Consumer): đang tính tổng...");
            while (true) {
                int num;
                synchronized (lock) {
                    while (buffer.isEmpty() && !done) {
                        try {
                            lock.wait();
                        } catch (InterruptedException e) {
                            Thread.currentThread().interrupt();
                            return;
                        }
                    }
                    if (buffer.isEmpty()) break;
                    num = buffer.poll();
                }
                if (num == -1) break;
                sum += num;
                System.out.println("  Lấy được: " + num + " | Tổng hiện tại: " + sum);
            }
            System.out.println("Tổng các số đã nhập: " + sum);
        }
    }

    public static void main(String[] args) throws InterruptedException {
        Thread producer = new Producer();
        Thread consumer = new Consumer();

        consumer.start();
        producer.start();

        producer.join();
        consumer.join();
    }
}
