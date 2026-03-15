package eg;

import java.io.OutputStream;
import java.io.PrintWriter;

public class ex4 {
    public static void main(String[] args) {
        OutputStream os = System.out;
        
        
        PrintWriter pw = new PrintWriter(os, true);

        pw.write("This is a string using write() \r\n");

        pw.println("This is a line using println()");

        
        pw.write("Bye! Bye! (No newline here)");

        
        pw.flush();

                                      
        pw.close();
    }
}