package bai1;


public class MyThread extends Thread {
    String name;
    int n;

    MyThread(String name, int n) {
        this.name = name;
        this.n = n;
        System.out.println("Thread " + name + " has been created ...!");
        start();
    }

    @Override
    public void run() {
        for (int i = 0; i < n; i++) {
            System.out.println("Hello, I'm " + name);
            System.out.println("I go to bed now, bye bye ... wow ...");
        }
    }

    public static void main(String[] args) {
        int n = 1000;
        int nt = 4;
        for (int i = 0; i < nt; i++) {
            MyThread t = new MyThread("Thread" + i, n);
        }
    }
}