import java.net.URISyntaxException;

public class Main {
      public static void main(String[] args) throws InterruptedException, URISyntaxException {
            String outputDir = new java.io.File(Main.class.getProtectionDomain().getCodeSource().getLocation().toURI()).getPath();
            
            FileThreadWriter[] t = new FileThreadWriter[3];
            for (int i = 0; i < 3; i++) {
                  String filePath = outputDir + java.io.File.separator + "file" + (i + 1) + ".txt";
                  t[i] = new FileThreadWriter(filePath, 10);
                  t[i].setName("T" + (i + 1));
                  t[i].start();
            }
            for (FileThreadWriter thread : t)
                  thread.join();
      }
}