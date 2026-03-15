package bai3;
//c1
//public class Main {
//    public static void main(String[] args) {
//        FileTReader t1 = new FileTReader("file1.txt");
//        FileTReader t2 = new FileTReader("file2.txt");
//        FileTReader t3 = new FileTReader("file3.txt");
//
//        t1.start();
//        t2.start();
//        t3.start();
//    }
//}
//c2
public class Main {
    public static void main(String[] args) {
        Thread t1 = new Thread(new FileTReader("file11.txt"));
        Thread t2 = new Thread(new FileTReader("file22.txt"));
        Thread t3 = new Thread(new FileTReader("file33.txt"));

        t1.start();
        t2.start();
        t3.start();
    }
}