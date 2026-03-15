package eg;

import java.io.IOException;
import java.io.InputStream;

public class ex1 {
    public static void main(String args[]) {
        InputStream is = System.in;                            
        System.out.println("nhap cac ki tu ( 'q' de thoat):");
        
        while(true) {
            try {
                int ch = is.read();
                if(ch == -1 || ch == 'q') break;

     
                if (ch >= 32) { 
                    System.out.println("Ký tự vừa nhập: " + (char)ch);
                }
            } catch (IOException ie) {
                System.out.println("Error: " + ie);
            }
        }
    }
}