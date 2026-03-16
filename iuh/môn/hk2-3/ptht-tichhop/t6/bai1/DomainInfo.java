package bai1;

import java.net.InetAddress;

public class DomainInfo {
    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("cach dung: java DomainInfo <domain>");
            System.out.println("vd: java bai1.DomainInfo google.com");
            return;
        }
        String domain = args[0];
        try {
            InetAddress address = InetAddress.getByName(domain);
            System.out.println("Hostname : " + address.getHostName());
            System.out.println("dia chi ip: " + address.getHostAddress());
        } catch (Exception e) {
            System.out.println("khong the phan giai ten mien: " + domain);
            System.out.println("loi: " + e.getMessage());
        }
    }
}