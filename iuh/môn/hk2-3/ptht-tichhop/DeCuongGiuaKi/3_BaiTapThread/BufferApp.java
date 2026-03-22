package BaiTapThread;

import java.util.Scanner;

class BufferToanXuy {
    private int buffer;
    private boolean hasData = false;
    private boolean isFinished = false;

    public synchronized void put(int n) {
        while (hasData && !isFinished) {
            try { wait(); } catch (InterruptedException e) {}
        }
        buffer = n;
        hasData = true;
        if (n == -1) {
            isFinished = true;
        }
        notifyAll();
    }

    public synchronized int get() {
        while (!hasData && !isFinished) {
            try { wait(); } catch (InterruptedException e) {}
        }
        hasData = false;
        notifyAll();
        return buffer;
    }

    public boolean isFinished() {
        return isFinished && !hasData;
    }
}

class Thread1Nhap extends Thread {
    private BufferToanXuy buffer;
    public Thread1Nhap(BufferToanXuy b) { this.buffer = b; }

    public void run() {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.print("Nhap so nguyen (go -1 de thoat): ");
            int n = scanner.nextInt();
            buffer.put(n);
            if (n == -1) {
                System.out.println("Thread 1 da dung nhap!");
                break;
            }
        }
    }
}

class Thread2TinhTong extends Thread {
    private BufferToanXuy buffer;
    public Thread2TinhTong(BufferToanXuy b) { this.buffer = b; }

    public void run() {
        int sum = 0;
        while (true) {
            int n = buffer.get();
            if (n == -1) {
                System.out.println("Thread 2 da nhan lenh ket thuc. Tong cuoi cung la: " + sum);
                break;
            }
            sum += n;
            System.out.println("Thread 2: Da lay so " + n + ". Tong hien tai = " + sum);
        }
    }
}

public class BufferApp {
    public static void main(String[] args) {
        BufferToanXuy buffer = new BufferToanXuy();
        Thread1Nhap t1 = new Thread1Nhap(buffer);
        Thread2TinhTong t2 = new Thread2TinhTong(buffer);
        
        t1.start();
        t2.start();
    }
}
