package InetAddress_CoBan;

import java.net.InetAddress;
import java.net.UnknownHostException;

public class DomainInfo {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Vui long truyen ten mien. Vd: java DomainInfo google.com");
            return;
        }
        String domain = args[0];
        try {
            InetAddress address = InetAddress.getByName(domain);
            System.out.println("Hostname: " + address.getHostName());
            System.out.println("Dia chi IP: " + address.getHostAddress());
        } catch (UnknownHostException e) {
            System.out.println("Khong the phan giai ten mien: " + domain);
        }
    }
}
