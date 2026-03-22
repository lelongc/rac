package InetAddress_CoBan;

import java.io.*;
import java.net.*;
import java.util.Scanner;

public class InetLogic {
    public static void execute() {
        Scanner scanner = new Scanner(System.in);
        System.out.println("===== CHON BAI TAP TUAN 6 INETADDRESS (BO COMMENT TRONG CLASS NAY DE CHAY) =====");
        
        // =========================================================================
        // DANG 1 (Bài 1): Nhập tên máy (domain) tu ban phim -> In ra IP
        // =========================================================================
        /*
        try {
            System.out.print("Nhap ten may (vd: google.com): ");
            String domain = scanner.nextLine();
            InetAddress address = InetAddress.getByName(domain);
            System.out.println("-> IP cua " + domain + " la: " + address.getHostAddress());
        } catch (UnknownHostException e) {
            System.out.println("Khong the tim thay IP cua ten may nay!");
        }
        */

        // =========================================================================
        // DANG 2 (Bài 2): Kiem tra xem mot dia chi IP co phai la may cuc bo hay khong
        // =========================================================================
        /*
        try {
            System.out.print("Nhap dia chi IP (vd: 127.0.0.1 hoac 8.8.8.8): ");
            String ip = scanner.nextLine();
            InetAddress address = InetAddress.getByName(ip);
            if (address.isLoopbackAddress() || address.isAnyLocalAddress() || address.isLinkLocalAddress()) {
                System.out.println("-> " + ip + " LA dia chi may cuc bo (Local/Loopback).");
            } else {
                System.out.println("-> " + ip + " KHONG PHAI la dia chi may cuc bo.");
            }
        } catch (UnknownHostException e) {
            System.out.println("IP khong hop le!");
        }
        */

        // =========================================================================
        // DANG 3 (Bài 3): Cho biet TAT CA cac dia chi IP cua mot ten may
        // =========================================================================
        /*
        try {
            System.out.print("Nhap ten may de tim tat ca danh sach IP (vd: facebook.com): ");
            String domainMulti = scanner.nextLine();
            InetAddress[] addresses = InetAddress.getAllByName(domainMulti);
            System.out.println("-> Danh sach cac IP cua " + domainMulti + ":");
            for (int i = 0; i < addresses.length; i++) {
                System.out.println("   IP " + (i+1) + ": " + addresses[i].getHostAddress());
            }
        } catch (UnknownHostException e) {
            System.out.println("Khong the phan giai ten may!");
        }
        */

        // =========================================================================
        // DANG 4 (Bài 4): Doc file ips.txt chua danh sach [IP] hoac [Domain].
        // -> IP thi xuat ra Domain, Domain thi xuat ra IP
        // =========================================================================
        /*
        String dir = "DeCuongGiuaKi/6_InetAddress_CoBan/";
        File file = new File(dir + "ips.txt");
        if (!file.exists()) {
            System.out.println("Chua co file ips.txt de chay. Vui long tao ips.txt voi vai ten mien/IP ben trong.");
        } else {
            try (BufferedReader br = new BufferedReader(new FileReader(file))) {
                String line;
                System.out.println("-> DO DU LIEU TU FILE " + file.getName() + ":");
                while ((line = br.readLine()) != null) {
                    line = line.trim();
                    if (line.isEmpty()) continue;
                    try {
                        InetAddress addr = InetAddress.getByName(line);
                        // Kiem tra thu ky tu dau: neu la chu so thi kha nang do la IP -> Xuat Name
                        if (Character.isDigit(line.charAt(0))) {
                            System.out.println("[IP] " + line + " -> [DOMAIN] " + addr.getHostName());
                        } else {
                            // Cung co the tra IP
                            System.out.println("[DOMAIN] " + line + " -> [IP] " + addr.getHostAddress());
                        }
                    } catch (UnknownHostException ex) {
                        System.out.println("Loi phan giai cho dong: " + line);
                    }
                }
            } catch (IOException e) {
                System.out.println("Loi ghi/doc file: " + e.getMessage());
            }
        }
        */

        scanner.close();
    }
}
