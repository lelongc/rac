package File_Folder;

import java.util.Scanner;

public class BaiTapTuan1_Logic {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("=== CHON BAI TAP TUAN 1 (BO COMMENT DE CHAY) ===");
        
        // =========================================================================
        // BAI 1: IN HELLO WORLD
        // =========================================================================
        /*
        System.out.println("Hello, World!");
        */

        // =========================================================================
        // BAI 2: NHAP TEN VA IN RA
        // =========================================================================
        /*
        System.out.println("What's your name?");
        String str = scanner.nextLine();
        System.out.println("Hi, I am " + str);
        */

        // =========================================================================
        // BAI 3: TINH TONG 2 SO A VA B
        // =========================================================================
        /*
        System.out.print("Vui long nhap so hang thu nhat: ");
        int soA = scanner.nextInt();
        System.out.print("Vui long nhap so hang thu hai: ");
        int soB = scanner.nextInt();
        int kq = soA + soB;
        System.out.println("Tinh tong [" + soA + " + " + soB + "] = " + kq);
        */

        // =========================================================================
        // BAI 4: KIEM TRA SO CHAN/LE
        // =========================================================================
        /*
        System.out.println(">> Kiem tra so chan le <<");
        System.out.print("Vui long nhap so can kiem tra: ");
        int so = scanner.nextInt();
        if (so % 2 == 0) {
            System.out.println("So " + so + " la so chan.");
        } else {
            System.out.println("So " + so + " la so le.");
        }
        */

        // =========================================================================
        // BAI 5: IN RA THANG BANG TIENG ANH
        // =========================================================================
        /*
        boolean isrun = true;
        while (isrun) {
            System.out.print("Vui long nhap thang: ");
            int thang = scanner.nextInt();
            switch (thang) {
                case 1: System.out.println("January"); break;
                case 2: System.out.println("February"); break;
                case 3: System.out.println("March"); break;
                case 4: System.out.println("April"); break;
                case 5: System.out.println("May"); break;
                case 6: System.out.println("June"); break;
                case 7: System.out.println("July"); break;
                case 8: System.out.println("August"); break;
                case 9: System.out.println("September"); break;
                case 10: System.out.println("October"); break;
                case 11: System.out.println("November"); break;
                case 12: System.out.println("December"); break;
                default:
                    isrun = false;
                    System.out.println("STOP");
                    break;
            }
        }
        */
        
        scanner.close();
    }
}
