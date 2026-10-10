package gkmodule;

import java.io.*;
import java.util.*;

public class FileHelper {

    // 1. Đọc toàn bộ nội dung file text thành 1 chuỗi String
    public static String readFile(String fileName) {
        File file = new File(fileName);
        if (!file.exists()) return "File khong ton tai: " + fileName;
        StringBuilder sb = new StringBuilder();
        try (BufferedReader br = new BufferedReader(new FileReader(file))) {
            String line;
            while ((line = br.readLine()) != null) {
                sb.append(line).append("\n");
            }
            return sb.toString();
        } catch (IOException e) {
            return "Loi doc file: " + e.getMessage();
        }
    }

    // 2. Đọc file text thành danh sách các dòng (List<String>)
    public static List<String> readLines(String fileName) {
        List<String> lines = new ArrayList<>();
        File file = new File(fileName);
        if (!file.exists()) return lines;
        try (BufferedReader br = new BufferedReader(new FileReader(file))) {
            String line;
            while ((line = br.readLine()) != null) {
                if (!line.trim().isEmpty()) {
                    lines.add(line.trim());
                }
            }
        } catch (IOException ignored) {}
        return lines;
    }

    // 3. Ghi đè chuỗi String vào file text (tạo file mới nếu chưa có)
    public static boolean writeFile(String fileName, String content) {
        try (PrintWriter pw = new PrintWriter(new FileWriter(fileName))) {
            pw.print(content);
            return true;
        } catch (IOException e) {
            System.err.println("Loi ghi file: " + e.getMessage());
            return false;
        }
    }

    // 4. Ghi nối tiếp (Append) vào cuối file (thường dùng để ghi Log, lịch sử chat)
    public static boolean appendFile(String fileName, String content) {
        try (PrintWriter pw = new PrintWriter(new FileWriter(fileName, true))) {
            pw.println(content);
            return true;
        } catch (IOException e) {
            System.err.println("Loi ghi log: " + e.getMessage());
            return false;
        }
    }

    // 5. Đọc file Key-Value (ví dụ: email=thongtin hoặc email:thongtin như file users.txt)
    public static Map<String, String> readKeyValueFile(String fileName) {
        Map<String, String> map = new HashMap<>();
        File file = new File(fileName);
        if (!file.exists()) return map;
        try (BufferedReader br = new BufferedReader(new FileReader(file))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] parts = line.split("[=:]", 2);
                if (parts.length == 2) {
                    map.put(parts[0].trim().toLowerCase(), parts[1].trim());
                }
            }
        } catch (IOException ignored) {}
        return map;
    }

    // 6. Copy file bằng Byte Streams (Bài thực hành Tuần 3 - MyCopy)
    public static boolean copyFile(String srcPath, String destPath) {
        try (FileInputStream fis = new FileInputStream(srcPath);
             FileOutputStream fos = new FileOutputStream(destPath)) {
            byte[] buffer = new byte[4096];
            int length;
            while ((length = fis.read(buffer)) > 0) {
                fos.write(buffer, 0, length);
            }
            return true;
        } catch (IOException e) {
            System.err.println("Loi copy file: " + e.getMessage());
            return false;
        }
    }

    // 7. Ghi đối tượng Serializable ra file nhị phân .dat (Bài thực hành Tuần 3 - ObjectStream)
    public static boolean writeObject(String fileName, Object obj) {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(fileName))) {
            oos.writeObject(obj);
            return true;
        } catch (IOException e) {
            System.err.println("Loi ghi Object: " + e.getMessage());
            return false;
        }
    }

    // 8. Đọc đối tượng Serializable từ file nhị phân .dat (Bài thực hành Tuần 3 - ObjectStream)
    public static Object readObject(String fileName) {
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(fileName))) {
            return ois.readObject();
        } catch (Exception e) {
            System.err.println("Loi doc Object: " + e.getMessage());
            return null;
        }
    }
}
