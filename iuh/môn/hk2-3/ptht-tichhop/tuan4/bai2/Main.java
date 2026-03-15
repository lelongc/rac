package bai2;
//c1 
//public class Main {
//    public static void main(String[] args) {
//        FileTWrite t1 = new FileTWrite("file1.txt");
//        FileTWrite t2 = new FileTWrite("file2.txt");
//        FileTWrite t3 = new FileTWrite("file3.txt");
//
//        t1.start();
//        t2.start();
//        t3.start();
//    }
//}
//c2 
public class Main {
    public static void main(String[] args) {
        Thread t1 = new Thread(new FileTWrite("file11.txt"));
        Thread t2 = new Thread(new FileTWrite("file22.txt"));
        Thread t3 = new Thread(new FileTWrite("file33.txt"));

        t1.start();
        t2.start();
        t3.start();
    }
}