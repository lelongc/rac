package InetAddress_CoBan;

import java.net.InetAddress;
import java.net.UnknownHostException;

public class HostnameCheck {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.out.println("Vui long truyen hostname. Vd: java HostnameCheck google.com");
            return;
        }
        String hostname = args[0];
        try {
            InetAddress[] addresses = InetAddress.getAllByName(hostname);
            System.out.println("Hostname '" + hostname + "' ton tai. Danh sach IP:");
            for (InetAddress addr : addresses) {
                System.out.println("- " + addr.getHostAddress());
            }
        } catch (UnknownHostException e) {
            System.out.println("Hostname '" + hostname + "' khong ton tai hoac khong the phan giai.");
        }
    }
}
