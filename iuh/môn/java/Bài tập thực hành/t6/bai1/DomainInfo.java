import java.net.InetAddress;

public class DomainInfo {
    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Cách dùng: java DomainInfo <domain>");
            System.out.println("Ví dụ: java DomainInfo google.com");
            return;
        }
        String domain = args[0];
        try {
            InetAddress address = InetAddress.getByName(domain);
            System.out.println("Hostname : " + address.getHostName());
            System.out.println("Địa chỉ IP: " + address.getHostAddress());
        } catch (Exception e) {
            System.out.println("Không thể phân giải tên miền: " + domain);
            System.out.println("Lỗi: " + e.getMessage());
        }
    }
}
