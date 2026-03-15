package bai2;
import java.io.File;

public class TestPath {
    public static void main(String[] args) throws Exception {
        // Cách 1: getResource
        try {
            String d1 = new File(TestPath.class.getResource("TestPath.class").toURI()).getParent();
            System.out.println("getResource: " + d1);
        } catch (Exception e) { System.out.println("getResource ERROR: " + e); }

        // Cách 2: getProtectionDomain
        try {
            String d2 = new File(TestPath.class.getProtectionDomain().getCodeSource().getLocation().toURI()).getPath();
            System.out.println("getProtection: " + d2);
        } catch (Exception e) { System.out.println("getProtection ERROR: " + e); }

        // Cách 3: user.dir (thư mục hiện tại khi chạy lệnh)
        System.out.println("user.dir: " + System.getProperty("user.dir"));
    }
}
