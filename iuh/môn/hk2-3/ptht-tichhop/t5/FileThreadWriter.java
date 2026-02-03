import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

public class FileThreadWriter extends Thread {
      private String fileName;
      private int count;

      public FileThreadWriter(String fileName, int count) {
            this.fileName = fileName;
            this.count = count;
      }

      @Override
      public void run() {
            Random random = new Random();
            try (FileWriter writer = new FileWriter(fileName)) {
                  for (int i = 0; i < count; i++) {
                        writer.write(random.nextInt(1000) + "\n");
                        Thread.sleep(100);
                  }
                  System.out.println(getName() + " xong");
            } catch (IOException | InterruptedException e) {
                  e.printStackTrace();
            }
      }
}