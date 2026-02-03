public class Main {
      public static void main(String[] args) throws InterruptedException {
            FileThreadWriter[] t = new FileThreadWriter[3];
            for (int i = 0; i < 3; i++) {
                  t[i] = new FileThreadWriter("file" + (i + 1) + ".txt", 10);
                  t[i].setName("T" + (i + 1));
                  t[i].start();
            }
            for (FileThreadWriter thread : t)
                  thread.join();
      }
}