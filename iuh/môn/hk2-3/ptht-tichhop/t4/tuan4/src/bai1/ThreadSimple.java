package bai1;


public class ThreadSimple extends Thread {

    @Override
    public void run() {
        System.out.println("Thread is running...");
    }

    public static void main(String[] args) {
        ThreadSimple t1 = new ThreadSimple();
        t1.start();
    }
}