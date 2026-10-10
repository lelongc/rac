package gkmodule;

import java.util.*;

public class DataHelper {

    // 1. Tách chuỗi dữ liệu (cách nhau bởi khoảng trắng hoặc dấu phẩy) thành List<Double>
    public static List<Double> parseNumbers(String input) {
        List<Double> list = new ArrayList<>();
        if (input == null || input.trim().isEmpty()) return list;
        String[] tokens = input.trim().split("[ ,\\s]+");
        for (String t : tokens) {
            try {
                if (!t.trim().isEmpty()) {
                    list.add(Double.parseDouble(t.trim()));
                }
            } catch (NumberFormatException ignored) {}
        }
        return list;
    }

    // 2. Định dạng danh sách số ra chuỗi (nếu là số nguyên thì không in .0)
    public static String formatList(List<? extends Number> list) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < list.size(); i++) {
            double v = list.get(i).doubleValue();
            if (v == (long) v) {
                sb.append((long) v);
            } else {
                sb.append(v);
            }
            if (i < list.size() - 1) sb.append(" ");
        }
        return sb.toString();
    }

    // 3. Tính tổng danh sách số
    public static double sum(List<Double> list) {
        double s = 0;
        for (double d : list) s += d;
        return s;
    }

    // 4. Tính trung bình cộng
    public static double avg(List<Double> list) {
        if (list.isEmpty()) return 0;
        return sum(list) / list.size();
    }

    // 5. Tìm giá trị lớn nhất (Max)
    public static double max(List<Double> list) {
        if (list.isEmpty()) return 0;
        return Collections.max(list);
    }

    // 6. Tìm giá trị nhỏ nhất (Min)
    public static double min(List<Double> list) {
        if (list.isEmpty()) return 0;
        return Collections.min(list);
    }

    // 7. Sắp xếp tăng dần
    public static List<Double> sortAsc(List<Double> list) {
        List<Double> result = new ArrayList<>(list);
        Collections.sort(result);
        return result;
    }

    // 8. Sắp xếp giảm dần
    public static List<Double> sortDesc(List<Double> list) {
        List<Double> result = new ArrayList<>(list);
        result.sort(Collections.reverseOrder());
        return result;
    }

    // 9. Lọc danh sách chỉ lấy số chẵn
    public static List<Integer> filterEven(List<Integer> list) {
        List<Integer> evens = new ArrayList<>();
        for (int n : list) if (n % 2 == 0) evens.add(n);
        return evens;
    }

    // 10. Lọc danh sách chỉ lấy số lẻ
    public static List<Integer> filterOdd(List<Integer> list) {
        List<Integer> odds = new ArrayList<>();
        for (int n : list) if (n % 2 != 0) odds.add(n);
        return odds;
    }
}
