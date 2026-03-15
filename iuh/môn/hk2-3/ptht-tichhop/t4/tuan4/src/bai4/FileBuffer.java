package bai4;

public class FileBuffer {
    private boolean hasNewData = false;
    public final String filename;

    public FileBuffer(String filename) {
        this.filename = filename;
    }

   
    public synchronized void writeLine(String line) throws InterruptedException, java.io.IOException {
        while (hasNewData) {
            wait();
        }
        try (java.io.FileWriter fw = new java.io.FileWriter(filename, true)) {
            fw.write(line + "\n");
        }
        System.out.println("Writer ghi: " + line);
        hasNewData = true;
        notifyAll();
    }

  
    public synchronized String readNewLine(int lastLineIdx) throws InterruptedException, java.io.IOException {
        while (!hasNewData) {
            wait();
        }

        java.util.List<String> lines = new java.util.ArrayList<>();
        try (java.io.BufferedReader br = new java.io.BufferedReader(new java.io.FileReader(filename))) {
            String line;
            while ((line = br.readLine()) != null) {
                lines.add(line);
            }
        }
        String out = "";
        if (lastLineIdx < lines.size()) {
            out = lines.get(lastLineIdx);
        }

        hasNewData = false;
        notifyAll();
        return out;
    }
}