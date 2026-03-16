package bai3;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class BufferApp {

    private static final Queue<Integer> buffer = new LinkedList<>();
    private static boolean done = false;
    private static final Object lock = new Object();


    static class Producer extends Thread {
        @Override
        public void run() {
            Scanner scanner = new Scanner(System.in);
            System.out.println("Thread 1 (Producer): nhap cac so nguyen (nhap -1 de dung):");
            while (true) {
                System.out.print("nhap so: ");
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

 
    static class Consumer extends Thread {
        @Override
        public void run() {
            int sum = 0;
            System.out.println("Thread 2 (Consumer): dang tinh tong...");
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
                System.out.println("  lay duoc: " + num + " | tong hien tai: " + sum);
            }
            System.out.println("tong các so da nhap: " + sum);
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