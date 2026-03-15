package eg;

import java.io.IOException;
import java.io.InputStream;

public class ex2 {
    public static void main(String[] args) {
        InputStream is = System.in;
        System.out.println("nhap noi dung bat ki:");

        while (true) {
            try {
                int num = is.available();        
                if (num > 0) {
                    byte[] b = new byte[num];
                    int result = is.read(b);                          
                    if (result == -1) break;
                    
                    String s = new String(b); 
                    System.out.print("ban da nhap: " + s);
                } else {
                    
                    Thread.sleep(500); 
                    System.out.print(".");
                }
            } catch (IOException | InterruptedException ie) {
                System.out.println("Error: " + ie);
            }
        }
    }
}