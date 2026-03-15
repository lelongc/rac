package tuan1;

import java.io.*;

public class ex5 {
    public static void main(String[] args) throws IOException {
        // InputStream (byte) → InputStreamReader (byte→char) → BufferedReader (buffer + dòng)
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out, true);

        pw.print("Nhap vao mot thang (1-12): "); pw.flush();
        int month = Integer.parseInt(br.readLine());
        String monthName;

        switch (month) {
            case 1:  monthName = "January";   break;
            case 2:  monthName = "February";  break;
            case 3:  monthName = "March";     break;
            case 4:  monthName = "April";     break;
            case 5:  monthName = "May";       break;
            case 6:  monthName = "June";      break;
            case 7:  monthName = "July";      break;
            case 8:  monthName = "August";    break;
            case 9:  monthName = "September"; break;
            case 10: monthName = "October";   break;
            case 11: monthName = "November";  break;
            case 12: monthName = "December";  break;
            default: monthName = "Thang khong hop le!"; break;
        }

        pw.println("Ten tieng Anh: " + monthName);
    }
}