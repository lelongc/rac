package eg;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ex3 {
    public static void main(String[] args) {
        
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(isr);
        

        System.out.println("--- Chuong trinh doc van ban (BufferedReader) ---");
        System.out.println("Nhap noi dung (Go 'exit' hoac 'quit' de dung):");

        while (true) {
            try {
                
                String line = br.readLine();

               
                if (line == null || line.equalsIgnoreCase("exit") || line.equalsIgnoreCase("quit")) {
                    System.out.println("Dang thoat...");
                    break;
                }

              
                System.out.println("Ket qua: " + line);

            } catch (IOException ie) {
                System.out.println("Co loi xay ra: " + ie.getMessage());
                break;
            }
        }

      
        try {
            br.close();
            isr.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        
        System.out.println("Chuong trinh ket thuc.");
    }
}