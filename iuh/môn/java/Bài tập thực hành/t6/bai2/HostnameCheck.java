import java.net.InetAddress;
import java.net.UnknownHostException;
import java.util.Scanner;

public class HostnameCheck {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Nhập hostname cần kiểm tra: ");
        String hostname = scanner.nextLine().trim();

        try {
            InetAddress[] addresses = InetAddress.getAllByName(hostname);
            System.out.println("Hostname \"" + hostname + "\" tồn tại.");
            System.out.println("Danh sách địa chỉ IP:");
            for (InetAddress addr : addresses) {
                System.out.println("  " + addr.getHostAddress());
            }
        } catch (UnknownHostException e) {
            System.out.println("Hostname \"" + hostname + "\" không tồn tại.");
        } finally {
            scanner.close();
        }
    }
}
