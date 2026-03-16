package bai2;

import java.net.InetAddress;
import java.net.UnknownHostException;
import java.util.Scanner;

public class HostnameCheck {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("nhap host name kiem tra: ");
        String hostname = scanner.nextLine().trim();

        try {
            InetAddress[] addresses = InetAddress.getAllByName(hostname);
            System.out.println("Hostname \"" + hostname + "\" ton tai.");
            System.out.println("Danh sach dia chi ip:");
            for (InetAddress addr : addresses) {
                System.out.println("  " + addr.getHostAddress());
            }
        } catch (UnknownHostException e) {
            System.out.println("Hostname \"" + hostname + "\" khong ton tai.");
        } finally {
            scanner.close();
        }
    }
}