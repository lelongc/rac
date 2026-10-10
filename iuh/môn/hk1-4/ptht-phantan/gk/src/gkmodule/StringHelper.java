package gkmodule;

import java.text.SimpleDateFormat;
import java.util.Date;

public class StringHelper {

    // 1. Mã hóa Caesar (Dịch chuyển ký tự theo khóa K) - Rất hay gặp trong đề thi an toàn / phân tán
    public static String caesarEncrypt(String text, int key) {
        StringBuilder sb = new StringBuilder();
        for (char c : text.toCharArray()) {
            if (Character.isUpperCase(c)) {
                sb.append((char) ('A' + (c - 'A' + key + 26) % 26));
            } else if (Character.isLowerCase(c)) {
                sb.append((char) ('a' + (c - 'a' + key + 26) % 26));
            } else {
                sb.append(c);
            }
        }
        return sb.toString();
    }

    // 2. Giải mã Caesar (Dịch ngược theo khóa K)
    public static String caesarDecrypt(String text, int key) {
        return caesarEncrypt(text, -key);
    }

    // 3. Lấy thời gian hiện tại định dạng "yyyy-MM-dd HH:mm:ss" (Server trả về ngày giờ)
    public static String getNow() {
        return new SimpleDateFormat("yyyy-MM-dd HH:mm:ss").format(new Date());
    }

    // 4. Kiểm tra Email hợp lệ bằng Regex
    public static boolean isValidEmail(String email) {
        if (email == null) return false;
        return email.matches("^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$");
    }

    // 5. Kiểm tra Số điện thoại Việt Nam hợp lệ (10 chữ số, bắt đầu bằng 0)
    public static boolean isValidPhone(String phone) {
        if (phone == null) return false;
        return phone.replaceAll("\\s+", "").matches("^0[0-9]{9}$");
    }

    // 6. Kiểm tra chuỗi có phải toàn là số hay không
    public static boolean isDigits(String str) {
        if (str == null || str.trim().isEmpty()) return false;
        return str.trim().matches("^\\d+$");
    }

    // 7. Chuẩn hóa họ tên (Viết hoa chữ cái đầu, xóa khoảng trắng thừa)
    public static String formatName(String name) {
        if (name == null) return "";
        String[] words = name.trim().toLowerCase().split("\\s+");
        StringBuilder sb = new StringBuilder();
        for (String w : words) {
            if (!w.trim().isEmpty()) {
                sb.append(Character.toUpperCase(w.charAt(0))).append(w.substring(1)).append(" ");
            }
        }
        return sb.toString().trim();
    }
}
