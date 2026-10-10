package gkmodule;

import java.io.*;
import java.util.*;

public class RandomHelper {

    private static final Random rand = new Random();

    // 1. Sinh số nguyên ngẫu nhiên trong đoạn [min, max]
    public static int randomInt(int min, int max) {
        return min + rand.nextInt(max - min + 1);
    }

    // 2. Sinh số thực ngẫu nhiên trong đoạn [min, max]
    public static double randomDouble(double min, double max) {
        return min + (max - min) * rand.nextDouble();
    }

    // 3. Sinh danh sách N số nguyên ngẫu nhiên trong đoạn [min, max]
    public static List<Integer> randomList(int count, int min, int max) {
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < count; i++) {
            list.add(randomInt(min, max));
        }
        return list;
    }

    // 4. Sinh chuỗi N số ngẫu nhiên cách nhau khoảng trắng (vd: "12 85 43 9 77")
    // Dùng để test ngay cho bài Lab 5 Sắp xếp dãy số
    public static String randomNumbersString(int count, int min, int max) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < count; i++) {
            sb.append(randomInt(min, max));
            if (i < count - 1) sb.append(" ");
        }
        return sb.toString();
    }

    // 5. Sinh N số ngẫu nhiên rồi GHI THẲNG VÀO FILE TEXT (đề thi rất hay yêu cầu bài này!)
    public static boolean generateRandomNumbersToFile(String fileName, int count, int min, int max) {
        try (PrintWriter pw = new PrintWriter(new FileWriter(fileName))) {
            for (int i = 0; i < count; i++) {
                pw.print(randomInt(min, max));
                if (i < count - 1) pw.print(" ");
            }
            pw.println();
            return true;
        } catch (IOException e) {
            System.err.println("Loi ghi file: " + e.getMessage());
            return false;
        }
    }

    // 6. Sinh chuỗi chữ cái ngẫu nhiên dài N ký tự
    public static String randomString(int length) {
        String chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < length; i++) {
            sb.append(chars.charAt(rand.nextInt(chars.length())));
        }
        return sb.toString();
    }
}
