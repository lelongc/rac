# CẨM NANG & TỔNG HỢP CODE ÔN THI GIỮA KỲ (GK) TOÀN TẬP
### MÔN: PHÁT TRIỂN HỆ THỐNG PHÂN TÁN (IUH)

---

## 📑 MỤC LỤC CHI TIẾT

- [I. HƯỚNG DẪN KHI ĐI THI & CẨM NANG PHÒNG THI](#i-hướng-dẫn-khi-đi-thi--cẩm-nang-phòng-thi)
  - [1. Quy trình tạo dự án khi thi trong phòng máy](#1-quy-trình-tạo-dự-án-khi-thi-trong-phòng-máy)
  - [2. Quy tắc nộp bài không bị thừa file](#2-quy-tắc-nộp-bài-không-bị-thừa-file)
  - [3. So sánh nhanh TCP vs UDP vs RMI](#3-so-sánh-nhanh-tcp-vs-udp-vs-rmi)
  - [4. Cách xuất file Markdown này sang PDF để in ấn](#4-cách-xuất-file-markdown-này-sang-pdf-để-in-ấn)
- [II. GÓI TIỆN ÍCH DÙNG CHUNG (gkmodule)](#ii-gói-tiện-ích-dùng-chung-gkmodule)
  - [1. RandomHelper.java (Sinh số/chuỗi ngẫu nhiên, ghi file số ngẫu nhiên)](#1-randomhelperjava)
  - [2. FileHelper.java (Đọc/ghi file text, line, key-value, copy stream, ObjectStream)](#2-filehelperjava)
  - [3. StringHelper.java (Mã hóa Caesar, ngày giờ, regex email/phone, chuẩn hóa họ tên)](#3-stringhelperjava)
  - [4. DataHelper.java (Tách số, format list, sum/avg/max/min, sort, filter chẵn lẻ)](#4-datahelperjava)
- [III. LẬP TRÌNH SOCKET TCP (gk)](#iii-lập-trình-socket-tcp-gk)
  - [1. Kiến trúc luồng xử lý TCP](#1-kiến-trúc-luồng-xử-lý-tcp)
  - [2. Server.java](#2-tcpserverjava)
  - [3. Client.java](#3-tcpclientjava)
  - [4. ThreadProcess.java (Chứa 35 dạng bài toán thuật toán)](#4-tcpthreadprocessjava)
- [IV. LẬP TRÌNH SOCKET UDP (gkudp)](#iv-lập-trình-socket-udp-gkudp)
  - [1. Cơ chế DatagramPacket & DatagramSocket](#1-cơ-chế-datagrampacket--datagramsocket)
  - [2. Server.java](#2-udpserverjava)
  - [3. Client.java](#3-udpclientjava)
  - [4. ThreadProcess.java](#4-udpthreadprocessjava)
- [V. LẬP TRÌNH PHÒNG CHAT BROADCAST MULTI-CLIENT (gkchat)](#v-lập-trình-phòng-chat-broadcast-multi-client-gkchat)
  - [1. Cơ chế Broadcast & Quản lý danh sách Client](#1-cơ-chế-broadcast--quản-lý-danh-sách-client)
  - [2. ChatServer.java](#2-chatserverjava)
  - [3. ChatClient.java](#3-chatclientjava)
- [VI. LẬP TRÌNH ĐỐI TƯỢNG PHÂN TÁN RMI (gkrmi)](#vi-lập-trình-đối-tượng-phân-tán-rmi-gkrmi)
  - [1. Quy tắc sống còn về file SinhVien.java](#1-quy-tắc-sống-còn-về-file-sinhvienjava)
  - [2. Bảng tra cứu 37 bài toán RMI đồng bộ 1-1](#2-bảng-tra-cứu-37-bài-toán-rmi-đồng-bộ-1-1)
  - [3. SinhVien.java (Đối tượng truyền qua mạng)](#3-sinhvienjava)
  - [4. IRemoteService.java (Interface khai báo 37 bài)](#4-iremoteservicejava)
  - [5. RMIServer.java (Khởi tạo Registry & Rebind)](#5-rmiserverjava)
  - [6. RemoteServiceImpl.java (Cài đặt chi tiết 37 bài toán)](#6-remoteserviceimpljava)
  - [7. RMIClient.java (Giao tiếp Console chi tiết 37 bài toán)](#7-rmiclientjava)
- [VII. BẢNG TỔNG HỢP CÔNG THỨC & THUẬT TOÁN THI GIỮA KỲ](#vii-bảng-tổng-hợp-công-thức--thuật-toán-thi-giữa-kỳ)

---

## I. HƯỚNG DẪN KHI ĐI THI & CẨM NANG PHÒNG THI

### 1. Quy trình tạo dự án khi thi trong phòng máy
1. Mở Eclipse trong phòng máy: **File -> New -> Java Project**.
2. Đặt tên Project theo đúng quy định của giám thị (ví dụ: `23630851_LeThanhLong_GK`).
3. Mở thư mục code này trên máy thi, copy folder package tương ứng dán vào thư mục `src` của dự án vừa tạo:
   - Đề ra **TCP Socket** $\rightarrow$ Copy folder `gk` vào `src`.
   - Đề ra **UDP Socket** $\rightarrow$ Copy folder `gkudp` vào `src`.
   - Đề ra **RMI** $\rightarrow$ Copy folder `gkrmi` vào `src`. *(Lưu ý xóa `SinhVien.java` nếu đề không yêu cầu)*.
   - Đề ra **Chat Broadcast** $\rightarrow$ Copy folder `gkchat` vào `src`.
4. Trong Eclipse, nhấn phím **F5** (Refresh) để nạp code.
5. Uncomment đúng **1 bài toán** mà đề yêu cầu.
6. Chạy Server trước $\rightarrow$ Chạy Client sau $\rightarrow$ Nhập dữ liệu test $\rightarrow$ Nộp bài.

---

### 2. Quy tắc nộp bài không bị thừa file
- **Đối với TCP (`gk`) và UDP (`gkudp`):**
  - Chỉ gồm 3 file: `Server.java`, `Client.java`, `ThreadProcess.java`.
  - Không có bất kỳ file phụ nào, không lo bị trừ điểm nộp thừa.
- **Đối với RMI (`gkrmi`):**
  - **Nếu đề ra BÀI 1 ĐẾN BÀI 36:** 👉 **Xóa ngay file `SinhVien.java`!** Dự án vẫn biên dịch và chạy 100% mượt mà, bài nộp sạch sẽ.
  - **Chỉ khi nào đề yêu cầu:** *"Xây dựng lớp SinhVien và truyền đối tượng qua mạng RMI"* thì mới giữ lại `SinhVien.java` và uncomment Bài 37.
- **Đối với gói `gkmodule`:**
  - **KHÔNG NỘP** nguyên package `gkmodule`!
  - Chỉ mở file trong `gkmodule` ra, copy đúng hàm mình cần (ví dụ: hàm sinh số ngẫu nhiên ghi ra file, hoặc hàm đọc file text) rồi dán vào `ThreadProcess.java` hoặc `RemoteServiceImpl.java`.

---

### 3. So sánh nhanh TCP vs UDP vs RMI

| Tiêu chí | TCP Socket | UDP Socket | Java RMI |
| :--- | :--- | :--- | :--- |
| **Gói Java** | `java.net.Socket`, `ServerSocket` | `java.net.DatagramSocket`, `DatagramPacket` | `java.rmi.*`, `java.rmi.registry.*` |
| **Giao thức** | Hướng kết nối (Tin cậy, Streams) | Phi kết nối (Gói tin độc lập, nhanh) | Lập trình hướng đối tượng từ xa RPC |
| **Luồng dữ liệu** | `BufferedReader`, `PrintWriter` | Mảng byte `byte[] buf` | Gọi hàm từ xa trực tiếp như gọi hàm local |
| **Cổng mặc định** | 5000 | 5000 | 1099 |
| **Phát hiện thoát** | Đọc chuỗi `"EXIT"` $\rightarrow$ `break` | Kiểm tra chuỗi `"EXIT"` $\rightarrow$ `break` | Client kết thúc hàm `main` |

---

### 4. Cách xuất file Markdown này sang PDF để in ấn
- **Cách 1 (Bằng VS Code - Khuyên dùng):**
  1. Cài Extension **Markdown PDF** (`yzane.markdown-pdf`) trong VS Code.
  2. Mở file `.md` này lên, bấm chuột phải vào nội dung $\rightarrow$ Chọn **Markdown PDF: Export (pdf)**.
  3. File PDF sẽ được tạo ngay cùng thư mục, định dạng cực đẹp có phân trang và tô màu code.
- **Cách 2 (Bằng trình duyệt Chrome/Edge):**
  1. Trong VS Code, mở Preview (`Ctrl + Shift + V`).
  2. Chuột phải vào bản Preview $\rightarrow$ Chọn Print hoặc bấm `Ctrl + P`.
  3. Ở mục Máy in chọn **Save as PDF** (Lưu dưới dạng PDF), chọn khổ A4, bật "Background graphics" (Đồ họa nền) để có màu code $\rightarrow$ Bấm Save.

---

## II. GÓI TIỆN ÍCH DÙNG CHUNG (gkmodule)

> Gói tiện ích này giúp bạn xử lý ngay các câu hỏi phụ của đề thi (như: sinh số ngẫu nhiên rồi ghi file, mã hóa Caesar, đọc file `users.txt`, v.v.). **Chỉ cần copy hàm cần thiết vào bài làm!**

### 1. RandomHelper.java
```java
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
```

---

### 2. FileHelper.java
```java
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

    // 4. Ghi nối tiếp (Append) vào cuối file (ghi Log, lịch sử chat)
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

    // 7. Ghi đối tượng Serializable ra file nhị phân .dat (Tuần 3 - ObjectStream)
    public static boolean writeObject(String fileName, Object obj) {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(fileName))) {
            oos.writeObject(obj);
            return true;
        } catch (IOException e) {
            System.err.println("Loi ghi Object: " + e.getMessage());
            return false;
        }
    }

    // 8. Đọc đối tượng Serializable từ file nhị phân .dat (Tuần 3 - ObjectStream)
    public static Object readObject(String fileName) {
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(fileName))) {
            return ois.readObject();
        } catch (Exception e) {
            System.err.println("Loi doc Object: " + e.getMessage());
            return null;
        }
    }
}
```

---

### 3. StringHelper.java
```java
package gkmodule;

import java.text.SimpleDateFormat;
import java.util.Date;

public class StringHelper {

    // 1. Mã hóa Caesar (Dịch chuyển ký tự theo khóa K)
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

    // 3. Lấy thời gian hiện tại định dạng "yyyy-MM-dd HH:mm:ss"
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

    // 6. Kiểm tra chuỗi có phải toàn là chữ số hay không
    public static boolean isDigits(String str) {
        if (str == null || str.trim().isEmpty()) return false;
        return str.trim().matches("^\\d+$");
    }

    // 7. Chuẩn hóa họ tên (Viết hoa chữ cái đầu mỗi từ)
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
```

---

### 4. DataHelper.java
```java
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
```

---

## III. LẬP TRÌNH SOCKET TCP (gk)

### 1. Kiến trúc luồng xử lý TCP
- **`Server.java`**: Tạo `ServerSocket(5000)`, trong vòng lặp `while (true)` gọi `.accept()`. Mỗi Client kết nối đến sẽ tạo ra một luồng riêng `ThreadProcess` giúp Server phục vụ đồng thời nhiều Client (Multi-Threaded).
- **`Client.java`**: Tạo `Socket("127.0.0.1", 5000)`, dùng `Scanner` đọc từ bàn phím, gửi qua `PrintWriter`, nhận phản hồi từ `BufferedReader`.
- **`ThreadProcess.java`**: Đọc dữ liệu từ Socket Client, gọi hàm `processData(data)` để xử lý theo đúng thuật toán của đề, rồi ghi kết quả trả về cho Client.

---

### 2. TCP `Server.java`
```java
package gk;

import java.net.ServerSocket;
import java.net.Socket;

public class Server {
    static final int PORT = 5000;

    public static void main(String[] args) throws Exception {
        try (ServerSocket ss = new ServerSocket(PORT)) {
            System.out.println("TCP Server listening on port " + PORT);
            int clientId = 0;
            while (true) {
                Socket s = ss.accept();
                clientId++;
                new ThreadProcess(s, clientId).start();
            }
        }
    }
}
```

---

### 3. TCP `Client.java`
```java
package gk;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.Scanner;

public class Client {
    static final String HOST = "127.0.0.1";
    static final int PORT = 5000;

    public static void main(String[] args) throws Exception {
        try (Socket s = new Socket(HOST, PORT);
             BufferedReader in = new BufferedReader(new InputStreamReader(s.getInputStream()));
             PrintWriter out = new PrintWriter(s.getOutputStream(), true);
             Scanner sc = new Scanner(System.in)) {

            System.out.println(in.readLine());
            while (true) {
                System.out.print("> ");
                String data = sc.nextLine();
                out.println(data);
                System.out.println(in.readLine());
                if ("EXIT".equalsIgnoreCase(data.trim())) break;
            }
        }
    }
}
```

---

### 4. TCP `ThreadProcess.java`
```java
package gk;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.*;

public class ThreadProcess extends Thread {
    private final Socket s;
    private final int clientId;

    public ThreadProcess(Socket s, int clientId) {
        this.s = s;
        this.clientId = clientId;
    }

    @Override
    public void run() {
        try (BufferedReader in = new BufferedReader(new InputStreamReader(s.getInputStream()));
             PrintWriter out = new PrintWriter(s.getOutputStream(), true)) {

            out.println("Connected. Send data or EXIT.");
            String line;
            while ((line = in.readLine()) != null) {
                line = line.trim();
                if ("EXIT".equalsIgnoreCase(line)) {
                    out.println("Bye");
                    break;
                }
                out.println(processData(line));
            }
        } catch (Exception e) {
            System.out.println("Client #" + clientId + " error: " + e.getMessage());
        }
    }

    // ====================================================================
    // KHI THI: UNCOMMENT BAI CAN LAM, XOA HOAC COMMENT CAC BAI KHAC
    // ====================================================================
    public static String processData(String data) {
        try {
            String[] a = data.trim().split("[ ,\\s]+");
            
            // ========== BAI 1: Tam giac - Input: "a b c" (vd: 3 4 5) [MAC DINH BAT] ==========
            if (a.length != 3) return "Nhap: a b c";
            double x = Double.parseDouble(a[0]), y = Double.parseDouble(a[1]), z = Double.parseDouble(a[2]);
            if (!(x > 0 && y > 0 && z > 0 && x + y > z && x + z > y && y + z > x)) return "Khong phai tam giac";
            double p = x + y + z;
            double s = Math.sqrt((p / 2) * (p / 2 - x) * (p / 2 - y) * (p / 2 - z));
            return String.format("Tam giac hop le | Chu vi=%.2f | Dien tich=%.2f", p, s);

            // ========== BAI 2: So phuc - Input: "op a b c d" (ADD/SUB/MUL/DIV a+bi c+di) ==========
//             if (a.length != 5) return "Nhap: op a b c d";
//             String op = a[0].toUpperCase();
//             double ar = Double.parseDouble(a[1]), ai = Double.parseDouble(a[2]);
//             double br = Double.parseDouble(a[3]), bi = Double.parseDouble(a[4]);
//             double rr = 0, ri = 0;
//             if (op.equals("ADD")) { rr = ar + br; ri = ai + bi; }
//             else if (op.equals("SUB")) { rr = ar - br; ri = ai - bi; }
//             else if (op.equals("MUL")) { rr = ar * br - ai * bi; ri = ar * bi + ai * br; }
//             else if (op.equals("DIV")) {
//                 double den = br * br + bi * bi;
//                 if (den == 0) return "Loi chia 0";
//                 rr = (ar * br + ai * bi) / den; ri = (ai * br - ar * bi) / den;
//             } else return "op chi ADD|SUB|MUL|DIV";
//             return String.format("%.4f%+.4fi", rr, ri);

            // ========== BAI 3: Fibonacci - Input: "n" (vd: 10) ==========
//             int n = Integer.parseInt(data.trim());
//             if (n < 0) return "n phai >= 0";
//             if (n == 0) return "0";
//             if (n == 1) return "1";
//             long fib_a = 0, fib_b = 1;
//             for (int i = 2; i <= n; i++) { long c = fib_a + fib_b; fib_a = fib_b; fib_b = c; }
//             return String.valueOf(fib_b);

            // ========== BAI 4: Quy doi tien te - Input: "amount from to" (100 USD VND) ==========
//             if (a.length != 3) return "Nhap: amount from to";
//             double amount = Double.parseDouble(a[0]);
//             String from = a[1].toUpperCase(), to = a[2].toUpperCase();
//             Map<String, Double> rate = new HashMap<>();
//             rate.put("VND", 1.0); rate.put("USD", 25000.0); rate.put("EUR", 27000.0); rate.put("JPY", 170.0);
//             if (!rate.containsKey(from) || !rate.containsKey(to)) return "Chi ho tro: VND USD EUR JPY";
//             double vnd = amount * rate.get(from);
//             return String.format("%.4f %s", vnd / rate.get(to), to);

            // ========== BAI 5: Nguyen to - Input: "n" ==========
//             long n = Long.parseLong(data.trim());
//             if (n < 2) return "Khong phai so nguyen to";
//             for (long i = 2; i * i <= n; i++) if (n % i == 0) return "Khong phai so nguyen to";
//             return "La so nguyen to";

            // ========== BAI 6: Sap xep tang dan - Input: "5,2,9,1" or "5 2 9 1" ==========
//             List<Double> list = new ArrayList<>();
//             for (String s : a) if (!s.trim().isEmpty()) list.add(Double.parseDouble(s.trim()));
//             Collections.sort(list);
//             return list.toString();

            // ========== BAI 7: Sap xep giam dan - Input: "5,2,9,1" ==========
//             List<Double> list = new ArrayList<>();
//             for (String s : a) if (!s.trim().isEmpty()) list.add(Double.parseDouble(s.trim()));
//             list.sort((x, y) -> Double.compare(y, x));
//             return list.toString();

            // ========== BAI 8: Thong ke tu - Input: "phat trien he thong phat trien" ==========
//             String[] w = data.toLowerCase().trim().split("\\s+");
//             Map<String, Integer> map = new LinkedHashMap<>();
//             for (String x : w) if (!x.trim().isEmpty()) map.put(x, map.getOrDefault(x, 0) + 1);
//             return map.toString();

            // ========== BAI 9: Sap xep chuoi theo chu cai - Input: "zebra,apple,cat" ==========
//             String[] arr = data.split(",");
//             List<String> list = new ArrayList<>();
//             for (String s : arr) list.add(s.trim());
//             Collections.sort(list);
//             return list.toString();

            // ========== BAI 10: Dao chuoi ==========
//             return new StringBuilder(data).reverse().toString();

            // ========== BAI 11: Ngat chuoi - Input: "a-b-c-d|-" ==========
//             String[] p = data.split("\\|", 2);
//             if (p.length != 2) return "Nhap: text|delimiter";
//             return Arrays.toString(p[0].split(java.util.regex.Pattern.quote(p[1])));

            // ========== BAI 12: UCLN BCNN - Input: "a b" (24 36) ==========
//             if (a.length != 2) return "Nhap: a b";
//             long x = Math.abs(Long.parseLong(a[0])), y = Math.abs(Long.parseLong(a[1]));
//             if (x == 0 && y == 0) return "UCLN=0, BCNN=0";
//             long g = gcd(x, y);
//             long l = (x == 0 || y == 0) ? 0 : (x / g) * y;
//             return "UCLN=" + g + ", BCNN=" + l;

            // ========== BAI 13: PT bac 1 - Input: "a b" => ax+b=0 ==========
//             if (a.length != 2) return "Nhap: a b";
//             double A = Double.parseDouble(a[0]), B = Double.parseDouble(a[1]);
//             if (A == 0 && B == 0) return "Vo so nghiem";
//             if (A == 0) return "Vo nghiem";
//             return String.format("x=%.6f", -B / A);

            // ========== BAI 14: PT bac 2 - Input: "a b c" => ax^2+bx+c=0 ==========
//             if (a.length != 3) return "Nhap: a b c";
//             double A = Double.parseDouble(a[0]), B = Double.parseDouble(a[1]), C = Double.parseDouble(a[2]);
//             if (A == 0) {
//                 if (B == 0 && C == 0) return "Vo so nghiem";
//                 if (B == 0) return "Vo nghiem";
//                 return String.format("x=%.6f", -C / B);
//             }
//             double delta = B * B - 4 * A * C;
//             if (delta < 0) return "Vo nghiem thuc";
//             if (delta == 0) return String.format("x1=x2=%.6f", -B / (2 * A));
//             double x1 = (-B + Math.sqrt(delta)) / (2 * A);
//             double x2 = (-B - Math.sqrt(delta)) / (2 * A);
//             return String.format("x1=%.6f, x2=%.6f", x1, x2);

            // ========== BAI 15: Tong 1..n - Input: "n" ==========
//             long n = Long.parseLong(data.trim());
//             if (n < 0) return "n phai >= 0";
//             return String.valueOf(n * (n + 1) / 2);

            // ========== BAI 16: Dem nguyen am phu am - Input: "mot chuoi" ==========
//             int vowel = 0, consonant = 0;
//             String s = data.toLowerCase();
//             for (char c : s.toCharArray()) {
//                 if (c >= 'a' && c <= 'z') {
//                     if ("aeiou".indexOf(c) >= 0) vowel++; else consonant++;
//                 }
//             }
//             return "NguyenAm=" + vowel + ", PhuAm=" + consonant;

            // ========== BAI 17: Chuan hoa chuoi - Input: "  phat  trien HE thong  " ==========
//             String[] w = data.trim().toLowerCase().split("\\s+");
//             StringBuilder sb = new StringBuilder();
//             for (String word : w) if (!word.trim().isEmpty()) {
//                 sb.append(Character.toUpperCase(word.charAt(0))).append(word.substring(1)).append(' ');
//             }
//             return sb.toString().trim();

            // ========== BAI 18: Palindrome - Input: "racecar" ==========
//             String s = data.replaceAll("\\s+", "").toLowerCase();
//             String r = new StringBuilder(s).reverse().toString();
//             return s.equals(r) ? "Palindrome" : "Khong palindrome";

            // ========== BAI 19: Giai thua - Input: "n" ==========
//             int n = Integer.parseInt(data.trim());
//             if (n < 0) return "n phai >= 0";
//             long f = 1;
//             for (int i = 2; i <= n; i++) f *= i;
//             return String.valueOf(f);

            // ========== BAI 20: Tong chu so - Input: "12345" ==========
//             String s = data.trim();
//             int sum = 0;
//             for (char c : s.toCharArray()) {
//                 if (Character.isDigit(c)) sum += c - '0';
//                 else if (c != '-') return "Chi nhap so nguyen";
//             }
//             return String.valueOf(sum);

            // ========== BAI 21: Tong danh sach so - Input: "1,2,3,4,5" ==========
//             List<Double> list = new ArrayList<>();
//             for (String s : a) if (!s.trim().isEmpty()) list.add(Double.parseDouble(s.trim()));
//             double sum = 0;
//             for (double num : list) sum += num;
//             return String.format("Tong=%.4f", sum);

            // ========== BAI 22: Min Max - Input: "5,2,9,1" ==========
//             List<Double> list = new ArrayList<>();
//             for (String s : a) if (!s.trim().isEmpty()) list.add(Double.parseDouble(s.trim()));
//             if (list.isEmpty()) return "Danh sach rong";
//             double min = list.get(0), max = list.get(0);
//             for (double num : list) { if (num < min) min = num; if (num > max) max = num; }
//             return String.format("Min=%.4f, Max=%.4f", min, max);

            // ========== BAI 23: Chan le - Input: "n" ==========
//             long n = Long.parseLong(data.trim());
//             return (n % 2 == 0) ? "So chan" : "So le";

            // ========== BAI 24: In hoa ==========
//             return data.toUpperCase();

            // ========== BAI 25: In thuong ==========
//             return data.toLowerCase();

            // ========== BAI 26: Dem ky tu - Input: "abc de" ==========
//             int all = data.length();
//             int noSpace = data.replace(" ", "").length();
//             return "TongKyTu=" + all + ", KhongTinhSpace=" + noSpace;

            // ========== BAI 27: Dien tich HCN - Input: "width height" or "3,4" ==========
//             if (a.length != 2) return "Nhap: width height";
//             double w = Double.parseDouble(a[0]), h = Double.parseDouble(a[1]);
//             return String.format("Dien tich HCN=%.4f", w * h);

            // ========== BAI 28: Dien tich hinh tron - Input: "r" (vd: 3) ==========
//             double r = Double.parseDouble(data.trim());
//             if (r < 0) return "Ban kinh phai >= 0";
//             return String.format("Dien tich hinh tron=%.4f", Math.PI * r * r);

            // ========== BAI 29: Dien tich hinh thang - Input: "a b h" (vd: 3 4 5) ==========
//             if (a.length != 3) return "Nhap: a b h";
//             double A = Double.parseDouble(a[0]), B = Double.parseDouble(a[1]), H = Double.parseDouble(a[2]);
//             if (H < 0) return "Chieu cao phai >= 0";
//             return String.format("Dien tich hinh thang=%.4f", (A + B) * H / 2.0);

            // ========== BAI 30: Chu vi hinh vuong - Input: "side" (vd: 4) ==========
//             double side = Double.parseDouble(data.trim());
//             return String.format("Chu vi hinh vuong=%.4f", 4 * side);

            // ========== BAI 31: Chu vi HCN - Input: "width height" (vd: 3 4) ==========
//             if (a.length != 2) return "Nhap: width height";
//             double w = Double.parseDouble(a[0]), h = Double.parseDouble(a[1]);
//             return String.format("Chu vi HCN=%.4f", 2 * (w + h));

            // ========== BAI 32: ĐỀ THI GIỮA KỲ CÂU 1 - Chuyển số thành chữ - Input: "3432" ==========
//             String numStr = data.trim();
//             String[] numWords = {"không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"};
//             StringBuilder sbNum = new StringBuilder();
//             boolean valid = true;
//             for (char ch : numStr.toCharArray()) {
//                 if (ch >= '0' && ch <= '9') sbNum.append(numWords[ch - '0']).append(" ");
//                 else { valid = false; break; }
//             }
//             if (!valid) return "Chuỗi chứa ký tự không phải số!";
//             return numStr + ": " + sbNum.toString().trim();

            // ========== BAI 33: ĐỀ THI GIỮA KỲ CÂU 2 - Tìm thông tin theo Email - Input: "abcd1234@gmail.com" ==========
//             Map<String, String> userDb = new HashMap<>();
//             userDb.put("abcd1234@gmail.com", "HenryFord 825 893 5382");
//             userDb.put("nguyenvana@gmail.com", "Nguyen Van A 0912345678");
//             userDb.put("tranthib@gmail.com", "Tran Thi B 0987654321");
//             String queryEmail = data.trim().toLowerCase();
//             if (userDb.containsKey(queryEmail)) return data.trim() + " và " + userDb.get(queryEmail);
//             return data.trim() + " -> Không tìm thấy người dùng";

            // ========== BAI 34: THỰC HÀNH LAB 5 - Sắp xếp dãy số - Input: "11 22 4 25 28 3" ==========
//             List<Double> numList = new ArrayList<>();
//             for (String s : a) if (!s.trim().isEmpty()) numList.add(Double.parseDouble(s.trim()));
//             if (numList.isEmpty()) return "Dãy số rỗng";
//             List<Double> ascL = new ArrayList<>(numList);
//             Collections.sort(ascL);
//             List<Double> descL = new ArrayList<>(numList);
//             descL.sort(Collections.reverseOrder());
//             return "Chuỗi nhận được: " + data.trim() + " | Sắp giảm dần: " + descL + " | Sắp tăng dần: " + ascL;

            // ========== BAI 35: THỰC HÀNH LAB 1 - Xếp loại sinh viên - Input: "SV01 Nguyen Van An 8.5" ==========
//             if (a.length < 3) return "Nhap: MaSV HoTen DiemTB";
//             double score = Double.parseDouble(a[a.length - 1]);
//             String rank = (score >= 8.5) ? "Xuat sac" : (score >= 7.0) ? "Kha/Gioi" : (score >= 5.0) ? "Trung binh" : "Yeu";
//             return "Thong tin: " + data.trim() + " | Xep loai: " + rank;

        } catch (Exception e) {
            return "Loi: " + e.getMessage();
        }
    }

    // Helper: UCLN
    static long gcd(long a, long b) {
        while (b != 0) { long t = a % b; a = b; b = t; }
        return Math.abs(a);
    }
}
```

---

## IV. LẬP TRÌNH SOCKET UDP (gkudp)

### 1. Cơ chế DatagramPacket & DatagramSocket
- UDP là giao thức phi kết nối (Connectionless).
- Dữ liệu gửi đi và nhận về luôn đóng gói trong đối tượng `DatagramPacket(byte[] buf, int length, InetAddress addr, int port)`.
- Gói `gkudp` sử dụng chung thuật toán xử lý với TCP thông qua file `ThreadProcess.java` của riêng UDP.

---

### 2. UDP `Server.java`
```java
package gkudp;

import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.nio.charset.StandardCharsets;

public class Server {
    static final int PORT = 5000;

    public static void main(String[] args) throws Exception {
        try (DatagramSocket ds = new DatagramSocket(PORT)) {
            System.out.println("UDP Server listening on port " + PORT);
            byte[] buf = new byte[8192];
            while (true) {
                DatagramPacket req = new DatagramPacket(buf, buf.length);
                ds.receive(req);
                String msg = new String(req.getData(), 0, req.getLength(), StandardCharsets.UTF_8);
                if ("HELLO".equalsIgnoreCase(msg.trim())) {
                    byte[] hi = "Connected. Send data or EXIT.".getBytes(StandardCharsets.UTF_8);
                    ds.send(new DatagramPacket(hi, hi.length, req.getAddress(), req.getPort()));
                    continue;
                }
                if ("EXIT".equalsIgnoreCase(msg.trim())) {
                    byte[] bye = "Bye".getBytes(StandardCharsets.UTF_8);
                    ds.send(new DatagramPacket(bye, bye.length, req.getAddress(), req.getPort()));
                    continue;
                }
                String resp = ThreadProcess.processData(msg);
                byte[] out = resp.getBytes(StandardCharsets.UTF_8);
                DatagramPacket reply = new DatagramPacket(out, out.length, req.getAddress(), req.getPort());
                ds.send(reply);
            }
        }
    }
}
```

---

### 3. UDP `Client.java`
```java
package gkudp;

import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.nio.charset.StandardCharsets;
import java.util.Scanner;

public class Client {
    static final String HOST = "127.0.0.1";
    static final int PORT = 5000;

    public static void main(String[] args) throws Exception {
        try (DatagramSocket ds = new DatagramSocket();
             Scanner sc = new Scanner(System.in)) {

            InetAddress ip = InetAddress.getByName(HOST);
            byte[] buf = new byte[8192];
            byte[] hello = "HELLO".getBytes(StandardCharsets.UTF_8);
            ds.send(new DatagramPacket(hello, hello.length, ip, PORT));

            DatagramPacket welcome = new DatagramPacket(buf, buf.length);
            ds.receive(welcome);
            System.out.println(new String(welcome.getData(), 0, welcome.getLength(), StandardCharsets.UTF_8));

            while (true) {
                System.out.print("> ");
                String data = sc.nextLine();
                byte[] out = data.getBytes(StandardCharsets.UTF_8);
                ds.send(new DatagramPacket(out, out.length, ip, PORT));

                DatagramPacket resp = new DatagramPacket(buf, buf.length);
                ds.receive(resp);
                System.out.println(new String(resp.getData(), 0, resp.getLength(), StandardCharsets.UTF_8));

                if ("EXIT".equalsIgnoreCase(data.trim())) break;
            }
        }
    }
}
```

---

### 4. UDP `ThreadProcess.java`
*(Tương tự file `ThreadProcess.java` bên TCP, chứa toàn bộ 35 bài toán từ Tam giác, Số phức, PTB1, PTB2, Chuyển số thành chữ, Email, đến Xếp loại sinh viên).*

---

## V. LẬP TRÌNH PHÒNG CHAT BROADCAST MULTI-CLIENT (gkchat)

### 1. Cơ chế Broadcast & Quản lý danh sách Client
- Đề thi Tuần 4 rất hay ra bài xây dựng phòng Chat Client-Server.
- Server dùng `Vector<ClientHandler> clients = new Vector<>();` (Vector là Thread-safe) để lưu tất cả các kết nối.
- Khi một Client gửi tin nhắn, hàm `broadcast(msg, sender)` sẽ lặp qua danh sách và chuyển tiếp tin nhắn cho **tất cả các Client khác** (ngoại trừ người gửi).
- Client có 2 luồng riêng biệt: Luồng con chuyên lắng nghe tin nhắn Server trả về (`receiver.start()`), luồng chính đọc bàn phím gửi lên Server.

---

### 2. Chat `ChatServer.java`
```java
package gkchat;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.Vector;

public class ChatServer {
    public static final int PORT = 10008;
    private static final Vector<ClientHandler> clients = new Vector<>();
    private static int clientCount = 0;

    public static void main(String[] args) {
        System.out.println("=== TCP CHAT SERVER (MULTI-CLIENT BROADCAST) ===");
        System.out.println("Dang lang nghe ket noi tai cong " + PORT + "...");

        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
            while (true) {
                Socket socket = serverSocket.accept();
                clientCount++;
                String clientName = "Client_" + clientCount;
                System.out.println(clientName + " da ket noi tu: " + socket.getInetAddress());

                ClientHandler handler = new ClientHandler(socket, clientName);
                clients.add(handler);
                handler.start();
            }
        } catch (IOException e) {
            System.err.println("Loi Server: " + e.getMessage());
        }
    }

    public static void broadcast(String message, ClientHandler sender) {
        for (ClientHandler client : clients) {
            if (client != sender) {
                client.sendMessage(message);
            }
        }
    }

    public static void removeClient(ClientHandler client) {
        clients.remove(client);
        System.out.println(client.getClientName() + " da roi phong chat. So luong con lai: " + clients.size());
        broadcast("[" + client.getClientName() + "] da roi phong chat.", null);
    }

    static class ClientHandler extends Thread {
        private final Socket socket;
        private final String clientName;
        private BufferedReader in;
        private PrintWriter out;

        public ClientHandler(Socket socket, String clientName) {
            this.socket = socket;
            this.clientName = clientName;
        }

        public String getClientName() {
            return clientName;
        }

        public void sendMessage(String msg) {
            if (out != null) {
                out.println(msg);
            }
        }

        @Override
        public void run() {
            try {
                in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                out = new PrintWriter(socket.getOutputStream(), true);

                out.println("=== Chao mung " + clientName + " den voi phong chat ===");
                out.println("Go tin nhan va Enter de tro chuyen. Go 'bye' hoac 'exit' de thoat.");
                broadcast("[" + clientName + "] da tham gia phong chat!", this);

                String line;
                while ((line = in.readLine()) != null) {
                    line = line.trim();
                    if (line.equalsIgnoreCase("exit") || line.equalsIgnoreCase("bye")) {
                        break;
                    }
                    System.out.println("[" + clientName + "]: " + line);
                    broadcast(clientName + ": " + line, this);
                }
            } catch (IOException e) {
                System.out.println(clientName + " mat ket noi.");
            } finally {
                removeClient(this);
                try {
                    if (in != null) in.close();
                    if (out != null) out.close();
                    if (socket != null) socket.close();
                } catch (IOException ignored) {}
            }
        }
    }
}
```

---

### 3. Chat `ChatClient.java`
```java
package gkchat;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.Scanner;

public class ChatClient {
    public static final String HOST = "127.0.0.1";
    public static final int PORT = 10008;

    public static void main(String[] args) {
        System.out.println("Dang ket noi toi Chat Server (" + HOST + ":" + PORT + ")...");

        try (Socket socket = new Socket(HOST, PORT)) {
            System.out.println("Ket noi thanh cong!\n");

            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
            Scanner scanner = new Scanner(System.in);

            // Luong 1: Lang nghe tin nhan tu Server gui ve
            Thread receiver = new Thread(() -> {
                try {
                    String serverMsg;
                    while ((serverMsg = in.readLine()) != null) {
                        System.out.println(serverMsg);
                    }
                } catch (IOException e) {
                    System.out.println("Da ngat ket noi voi Server.");
                }
            });
            receiver.setDaemon(true);
            receiver.start();

            // Luong 2 (chinh): Doc tu ban phim va gui len Server
            while (true) {
                String input = scanner.nextLine();
                out.println(input);
                if (input.equalsIgnoreCase("exit") || input.equalsIgnoreCase("bye")) {
                    break;
                }
            }

            scanner.close();
            System.out.println("Da roi khoi phong chat.");
        } catch (IOException e) {
            System.err.println("Loi ket noi: " + e.getMessage());
        }
    }
}
```

---

## VI. LẬP TRÌNH ĐỐI TƯỢNG PHÂN TÁN RMI (gkrmi)

### 1. Quy tắc sống còn về file `SinhVien.java`
- Trong gói `gkrmi`, có tổng cộng 5 file: `RMIServer.java`, `RMIClient.java`, `IRemoteService.java`, `RemoteServiceImpl.java`, và `SinhVien.java`.
- **NẾU ĐỀ THI RA BẤT KỲ BÀI NÀO TỪ BÀI 1 ĐẾN BÀI 36:**
  👉 **HÃY XÓA NGAY FILE `SinhVien.java`!**
  Dự án hoàn toàn KHÔNG BỊ LỖI, biên dịch và chạy 100% mượt mà, giúp bài nộp **sạch sẽ, KHÔNG THỪA BẤT KỲ FILE NÀO**.
- **Chỉ khi nào đề yêu cầu:** *"Xây dựng lớp đối tượng Sinh viên (hoặc truyền nhận đối tượng qua mạng RMI)"* thì mới giữ lại file `SinhVien.java` và uncomment Bài 37.

---

### 2. Bảng tra cứu 37 bài toán RMI đồng bộ 1-1

| STT | Tên bài toán RMI | Cần file `SinhVien.java`? | Thao tác khi thi |
| :---: | :--- | :---: | :--- |
| **BÀI 1** | **Máy tính 4 phép tính (+, -, *, /)** | ❌ **KHÔNG** | Mặc định đang bật. Chạy được ngay. |
| **BÀI 2** | **Tính tam giác** (Heron từ $a, b, c$) | ❌ **KHÔNG** | Uncomment Bài 2, comment Bài 1 |
| **BÀI 3** | **Số phức** (ADD, SUB, MUL, DIV) | ❌ **KHÔNG** | Uncomment Bài 3, comment Bài 1 |
| **BÀI 4** | **Số Fibonacci / In dãy Fibonacci** | ❌ **KHÔNG** | Uncomment Bài 4, comment Bài 1 |
| **BÀI 5** | **Quy đổi tiền tệ** (VND, USD, EUR, JPY) | ❌ **KHÔNG** | Uncomment Bài 5, comment Bài 1 |
| **BÀI 6** | **Kiểm tra số nguyên tố** (Prime check) | ❌ **KHÔNG** | Uncomment Bài 6, comment Bài 1 |
| **BÀI 7** | **Sắp xếp tăng dần danh sách số** | ❌ **KHÔNG** | Uncomment Bài 7, comment Bài 1 |
| **BÀI 8** | **Sắp xếp giảm dần danh sách số** | ❌ **KHÔNG** | Uncomment Bài 8, comment Bài 1 |
| **BÀI 9** | **Thống kê số lần xuất hiện của từ** | ❌ **KHÔNG** | Uncomment Bài 9, comment Bài 1 |
| **BÀI 10** | **Sắp xếp chuỗi từ theo bảng chữ cái** | ❌ **KHÔNG** | Uncomment Bài 10, comment Bài 1 |
| **BÀI 11** | **Đảo ngược chuỗi** | ❌ **KHÔNG** | Uncomment Bài 11, comment Bài 1 |
| **BÀI 12** | **Ngắt chuỗi theo ký tự phân cách** | ❌ **KHÔNG** | Uncomment Bài 12, comment Bài 1 |
| **BÀI 13** | **UCLN và BCNN** ($a, b$) | ❌ **KHÔNG** | Uncomment Bài 13, comment Bài 1 |
| **BÀI 14** | **Giải phương trình bậc 1** ($ax+b=0$) | ❌ **KHÔNG** | Uncomment Bài 14, comment Bài 1 |
| **BÀI 15** | **Giải phương trình bậc 2** ($ax^2+bx+c=0$) | ❌ **KHÔNG** | Uncomment Bài 15, comment Bài 1 |
| **BÀI 16** | **Tính tổng 1..n** | ❌ **KHÔNG** | Uncomment Bài 16, comment Bài 1 |
| **BÀI 17** | **Đếm nguyên âm và phụ âm** | ❌ **KHÔNG** | Uncomment Bài 17, comment Bài 1 |
| **BÀI 18** | **Chuẩn hóa chuỗi** (Viết hoa đầu mỗi từ) | ❌ **KHÔNG** | Uncomment Bài 18, comment Bài 1 |
| **BÀI 19** | **Kiểm tra Palindrome** (Chuỗi đối xứng) | ❌ **KHÔNG** | Uncomment Bài 19, comment Bài 1 |
| **BÀI 20** | **Tính giai thừa** ($n!$) | ❌ **KHÔNG** | Uncomment Bài 20, comment Bài 1 |
| **BÀI 21** | **Tính tổng các chữ số** (vd: `12345` -> `15`) | ❌ **KHÔNG** | Uncomment Bài 21, comment Bài 1 |
| **BÀI 22** | **Tính tổng danh sách số** | ❌ **KHÔNG** | Uncomment Bài 22, comment Bài 1 |
| **BÀI 23** | **Tìm Min và Max của danh sách số** | ❌ **KHÔNG** | Uncomment Bài 23, comment Bài 1 |
| **BÀI 24** | **Kiểm tra chẵn lẻ** | ❌ **KHÔNG** | Uncomment Bài 24, comment Bài 1 |
| **BÀI 25** | **Chuyển chuỗi sang IN HOA** | ❌ **KHÔNG** | Uncomment Bài 25, comment Bài 1 |
| **BÀI 26** | **Chuyển chuỗi sang in thường** | ❌ **KHÔNG** | Uncomment Bài 26, comment Bài 1 |
| **BÀI 27** | **Đếm tổng số ký tự** (có và không space) | ❌ **KHÔNG** | Uncomment Bài 27, comment Bài 1 |
| **BÀI 28** | **Tính diện tích Hình chữ nhật** | ❌ **KHÔNG** | Uncomment Bài 28, comment Bài 1 |
| **BÀI 29** | **Tính diện tích Hình tròn** | ❌ **KHÔNG** | Uncomment Bài 29, comment Bài 1 |
| **BÀI 30** | **Tính diện tích Hình thang** | ❌ **KHÔNG** | Uncomment Bài 30, comment Bài 1 |
| **BÀI 31** | **Tính chu vi Hình vuông** | ❌ **KHÔNG** | Uncomment Bài 31, comment Bài 1 |
| **BÀI 32** | **Tính chu vi Hình chữ nhật** | ❌ **KHÔNG** | Uncomment Bài 32, comment Bài 1 |
| **BÀI 33** | **[ĐỀ THI GK CÂU 1] Chuyển số thành chữ** | ❌ **KHÔNG** | Uncomment Bài 33, comment Bài 1 |
| **BÀI 34** | **[ĐỀ THI GK CÂU 2] Tìm thông tin theo Email** | ❌ **KHÔNG** | Uncomment Bài 34, comment Bài 1 |
| **BÀI 35** | **[THỰC HÀNH LAB 5] Sắp xếp dãy số** (chuỗi gốc, giảm, tăng) | ❌ **KHÔNG** | Uncomment Bài 35, comment Bài 1 |
| **BÀI 36** | **[THỰC HÀNH TUẦN 3] Đọc nội dung file text từ Server** | ❌ **KHÔNG** | Uncomment Bài 36, comment Bài 1 |
| **BÀI 37** | **[THỰC HÀNH TUẦN 1 & 3] Tìm đối tượng Sinh viên theo mã** | ✅ **CẦN DUY NHẤT BÀI NÀY** | Giữ file `SinhVien.java`, uncomment Bài 37 |

---

### 3. RMI `SinhVien.java`
```java
package gkrmi;

import java.io.Serializable;

// ⚠️ LƯU Ý KHI ĐI THI:
// - File này CHỈ DÙNG DUY NHẤT KHI ĐỀ RA [BÀI 37: ĐỐI TƯỢNG SINH VIÊN].
// - NẾU ĐỀ RA BẤT KỲ BÀI NÀO KHÁC (BÀI 1 ĐẾN BÀI 36):
//   -> HÃY XÓA THẲNG TAY FILE NÀY ĐI (DELETE SinhVien.java)!
//   -> Dự án vẫn biên dịch và chạy 100% bình thường, không bị thừa file khi nộp!
public class SinhVien implements Serializable {
    private static final long serialVersionUID = 1L;

    private String maSV;
    private String hoTen;
    private double diemTB;

    public SinhVien() {
    }

    public SinhVien(String maSV, String hoTen, double diemTB) {
        this.maSV = maSV;
        this.hoTen = hoTen;
        this.diemTB = diemTB;
    }

    public String getMaSV() {
        return maSV;
    }

    public void setMaSV(String maSV) {
        this.maSV = maSV;
    }

    public String getHoTen() {
        return hoTen;
    }

    public void setHoTen(String hoTen) {
        this.hoTen = hoTen;
    }

    public double getDiemTB() {
        return diemTB;
    }

    public void setDiemTB(double diemTB) {
        this.diemTB = diemTB;
    }

    public String getXepLoai() {
        if (diemTB >= 8.5) return "Xuat sac";
        if (diemTB >= 7.0) return "Kha / Gioi";
        if (diemTB >= 5.0) return "Trung binh";
        return "Yeu";
    }

    @Override
    public String toString() {
        return String.format("SinhVien [MaSV=%s, HoTen=%s, DiemTB=%.2f, XepLoai=%s]",
                maSV, hoTen, diemTB, getXepLoai());
    }
}
```

---

### 4. RMI `IRemoteService.java`
```java
package gkrmi;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface IRemoteService extends Remote {

    // ========== BAI 1: May tinh 4 phep tinh (+, -, *, /) - [MAC DINH BAT] [KHONG CAN SinhVien.java] ==========
    int add(int a, int b) throws RemoteException;
    int sub(int a, int b) throws RemoteException;
    int mul(int a, int b) throws RemoteException;
    double div(int a, int b) throws RemoteException;

    // ========== BAI 2: Tam giac (Chu vi, dien tich Heron) - Input: a, b, c - [KHONG CAN SinhVien.java] ==========
    // String tinhTamGiac(double a, double b, double c) throws RemoteException;

    // ========== BAI 3: So phuc (ADD/SUB/MUL/DIV) - Input: op, ar, ai, br, bi - [KHONG CAN SinhVien.java] ==========
    // String soPhuc(String op, double ar, double ai, double br, double bi) throws RemoteException;

    // ========== BAI 4: So Fibonacci / In day Fibonacci - Input: n - [KHONG CAN SinhVien.java] ==========
    // String fibonacci(int n) throws RemoteException;

    // ========== BAI 5: Quy doi tien te - Input: amount, from, to (USD, EUR, JPY, VND) - [KHONG CAN SinhVien.java] ==========
    // String quyDoiTienTe(double amount, String from, String to) throws RemoteException;

    // ========== BAI 6: Kiem tra so nguyen to - Input: n - [KHONG CAN SinhVien.java] ==========
    // boolean isPrime(long n) throws RemoteException;

    // ========== BAI 7: Sap xep tang dan danh sach so - Input: "5,2,9,1" - [KHONG CAN SinhVien.java] ==========
    // String sapXepTangDan(String inputNumbers) throws RemoteException;

    // ========== BAI 8: Sap xep giam dan danh sach so - Input: "5,2,9,1" - [KHONG CAN SinhVien.java] ==========
    // String sapXepGiamDan(String inputNumbers) throws RemoteException;

    // ========== BAI 9: Thong ke so lan xuat hien cua tu - Input: str - [KHONG CAN SinhVien.java] ==========
    // String thongKeTu(String str) throws RemoteException;

    // ========== BAI 10: Sap xep chuoi theo chu cai - Input: "zebra,apple,cat" - [KHONG CAN SinhVien.java] ==========
    // String sapXepChuoiTheoChuCai(String str) throws RemoteException;

    // ========== BAI 11: Dao nguoc chuoi - Input: str - [KHONG CAN SinhVien.java] ==========
    // String daoChuoi(String str) throws RemoteException;

    // ========== BAI 12: Ngat chuoi theo ky tu phan cach - Input: text, delimiter - [KHONG CAN SinhVien.java] ==========
    // String ngatChuoi(String text, String delimiter) throws RemoteException;

    // ========== BAI 13: UCLN va BCNN - Input: a, b - [KHONG CAN SinhVien.java] ==========
    // String uclnVaBcnn(long a, long b) throws RemoteException;

    // ========== BAI 14: Giai phuong trinh bac 1 (ax + b = 0) - Input: a, b - [KHONG CAN SinhVien.java] ==========
    // String giaiPTBac1(double a, double b) throws RemoteException;

    // ========== BAI 15: Giai phuong trinh bac 2 (ax^2 + bx + c = 0) - Input: a, b, c - [KHONG CAN SinhVien.java] ==========
    // String giaiPTBac2(double a, double b, double c) throws RemoteException;

    // ========== BAI 16: Tinh tong 1..n - Input: n - [KHONG CAN SinhVien.java] ==========
    // long tong1DenN(long n) throws RemoteException;

    // ========== BAI 17: Dem nguyen am va phu am - Input: str - [KHONG CAN SinhVien.java] ==========
    // String demNguyenAmPhuAm(String str) throws RemoteException;

    // ========== BAI 18: Chuan hoa chuoi (Viet hoa dau moi tu) - Input: str - [KHONG CAN SinhVien.java] ==========
    // String chuanHoaChuoi(String str) throws RemoteException;

    // ========== BAI 19: Kiem tra chuoi Palindrome (Doi xung) - Input: str - [KHONG CAN SinhVien.java] ==========
    // boolean isPalindrome(String str) throws RemoteException;

    // ========== BAI 20: Tinh giai thua (n!) - Input: n - [KHONG CAN SinhVien.java] ==========
    // long giaiThua(int n) throws RemoteException;

    // ========== BAI 21: Tinh tong cac chu so - Input: 12345 - [KHONG CAN SinhVien.java] ==========
    // int tongCacChuSo(String numberStr) throws RemoteException;

    // ========== BAI 22: Tinh tong danh sach so - Input: "1,2,3,4,5" - [KHONG CAN SinhVien.java] ==========
    // double tongDanhSachSo(String inputNumbers) throws RemoteException;

    // ========== BAI 23: Tim Min va Max cua danh sach so - Input: "5,2,9,1" - [KHONG CAN SinhVien.java] ==========
    // String timMinMax(String inputNumbers) throws RemoteException;

    // ========== BAI 24: Kiem tra chan le - Input: n - [KHONG CAN SinhVien.java] ==========
    // String kiemTraChanLe(long n) throws RemoteException;

    // ========== BAI 25: Chuyen chuoi sang IN HOA - Input: str - [KHONG CAN SinhVien.java] ==========
    // String inHoa(String str) throws RemoteException;

    // ========== BAI 26: Chuyen chuoi sang in thuong - Input: str - [KHONG CAN SinhVien.java] ==========
    // String inThuong(String str) throws RemoteException;

    // ========== BAI 27: Dem tong so ky tu (co space va khong space) - Input: str - [KHONG CAN SinhVien.java] ==========
    // String demKyTu(String str) throws RemoteException;

    // ========== BAI 28: Dien tich Hinh Chu Nhat - Input: dai, rong - [KHONG CAN SinhVien.java] ==========
    // double dienTichHCN(double dai, double rong) throws RemoteException;

    // ========== BAI 29: Dien tich Hinh Tron - Input: r - [KHONG CAN SinhVien.java] ==========
    // double dienTichHinhTron(double r) throws RemoteException;

    // ========== BAI 30: Dien tich Hinh Thang - Input: a, b, h - [KHONG CAN SinhVien.java] ==========
    // double dienTichHinhThang(double a, double b, double h) throws RemoteException;

    // ========== BAI 31: Chu vi Hinh Vuong - Input: side - [KHONG CAN SinhVien.java] ==========
    // double chuViHinhVuong(double side) throws RemoteException;

    // ========== BAI 32: Chu vi Hinh Chu Nhat - Input: dai, rong - [KHONG CAN SinhVien.java] ==========
    // double chuViHCN(double dai, double rong) throws RemoteException;

    // ========== BAI 33: [ĐỀ THI GIỮA KỲ CÂU 1] Chuyen so thanh chu - Input: "3432" - [KHONG CAN SinhVien.java] ==========
    // String doiSoThanhChu(String numberStr) throws RemoteException;

    // ========== BAI 34: [ĐỀ THI GIỮA KỲ CÂU 2] Tim thong tin theo Email - Input: "abcd1234@gmail.com" - [KHONG CAN SinhVien.java] ==========
    // String timNguoiDungTheoEmail(String email) throws RemoteException;

    // ========== BAI 35: [THỰC HÀNH LAB 5] Sap xep day so - Input: "11 22 4 25 28 3" - [KHONG CAN SinhVien.java] ==========
    // String sapXepDaySo(String inputNumbers) throws RemoteException;

    // ========== BAI 36: [THỰC HÀNH TUẦN 3] Doc file van ban tren Server - Input: "users.txt" - [KHONG CAN SinhVien.java] ==========
    // String docFile(String fileName) throws RemoteException;

    // ========== BAI 37: [THỰC HÀNH TUẦN 1 & 3 - ⚠️ CẦN SinhVien.java] Tim sinh vien theo ma - Input: "SV01" ==========
    // SinhVien timSinhVienTheoMa(String maSV) throws RemoteException;
}
```

---

### 5. RMI `RMIServer.java`
```java
package gkrmi;

import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

public class RMIServer {
    public static final int PORT = 1099;
    public static final String SERVICE_NAME = "RemoteService";

    public static void main(String[] args) {
        try {
            // Tự động tạo Registry tại cổng 1099 (hoặc dùng registry đang mở)
            try {
                LocateRegistry.createRegistry(PORT);
                System.out.println("RMI Registry duoc tao tai cong " + PORT);
            } catch (Exception e) {
                System.out.println("RMI Registry da ton tai tai cong " + PORT);
            }

            // Khởi tạo đối tượng Remote Service
            IRemoteService service = new RemoteServiceImpl();

            // Dang ky doi tuong vao Registry
            String rmiUrl = "rmi://localhost:" + PORT + "/" + SERVICE_NAME;
            Naming.rebind(rmiUrl, service);

            System.out.println("==================================================");
            System.out.println("  RMI SERVER DA KHOI DONG THANH CONG!");
            System.out.println("  Dich vu dang phuc vu tai: " + rmiUrl);
            System.out.println("==================================================");
        } catch (Exception e) {
            System.err.println("Loi Server: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
```

---

### 6. RMI `RemoteServiceImpl.java`
```java
package gkrmi;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.*;

public class RemoteServiceImpl extends UnicastRemoteObject implements IRemoteService {
    private static final long serialVersionUID = 1L;

    public RemoteServiceImpl() throws RemoteException {
        super();
    }

    // ========== BAI 1: May tinh 4 phep tinh (+, -, *, /) - [MAC DINH BAT] [KHONG CAN SinhVien.java] ==========
    @Override
    public int add(int a, int b) throws RemoteException {
        return a + b;
    }

    @Override
    public int sub(int a, int b) throws RemoteException {
        return a - b;
    }

    @Override
    public int mul(int a, int b) throws RemoteException {
        return a * b;
    }

    @Override
    public double div(int a, int b) throws RemoteException {
        if (b == 0) throw new ArithmeticException("Khong the chia cho 0!");
        return (double) a / b;
    }

    // ========== BAI 2: Tam giac (Chu vi, dien tich Heron) - Input: a, b, c - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String tinhTamGiac(double a, double b, double c) throws RemoteException {
    //     if (!(a > 0 && b > 0 && c > 0 && a + b > c && a + c > b && b + c > a)) {
    //         return "Khong phai tam giac hop le!";
    //     }
    //     double p = a + b + c;
    //     double s = Math.sqrt((p / 2) * (p / 2 - a) * (p / 2 - b) * (p / 2 - c));
    //     return String.format("Tam giac hop le | Chu vi=%.2f | Dien tich=%.2f", p, s);
    // }

    // ========== BAI 3: So phuc (ADD/SUB/MUL/DIV) - Input: op, ar, ai, br, bi - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String soPhuc(String op, double ar, double ai, double br, double bi) throws RemoteException {
    //     String operation = (op == null) ? "" : op.trim().toUpperCase();
    //     double rr = 0, ri = 0;
    //     if (operation.equals("ADD")) { rr = ar + br; ri = ai + bi; }
    //     else if (operation.equals("SUB")) { rr = ar - br; ri = ai - bi; }
    //     else if (operation.equals("MUL")) { rr = ar * br - ai * bi; ri = ar * bi + ai * br; }
    //     else if (operation.equals("DIV")) {
    //         double den = br * br + bi * bi;
    //         if (den == 0) return "Loi chia 0";
    //         rr = (ar * br + ai * bi) / den; ri = (ai * br - ar * bi) / den;
    //     } else return "Toan tu chi chap nhan ADD|SUB|MUL|DIV";
    //     return String.format("%.4f%+.4fi", rr, ri);
    // }

    // ========== BAI 4: So Fibonacci / In day Fibonacci - Input: n - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String fibonacci(int n) throws RemoteException {
    //     if (n < 0) return "n phai >= 0";
    //     if (n == 0) return "0";
    //     if (n == 1) return "0, 1 (F1 = 1)";
    //     long fibA = 0, fibB = 1;
    //     StringBuilder sb = new StringBuilder("0, 1");
    //     for (int i = 2; i <= n; i++) {
    //         long c = fibA + fibB;
    //         sb.append(", ").append(c);
    //         fibA = fibB;
    //         fibB = c;
    //     }
    //     return "F(" + n + ") = " + fibB + " | Day: " + sb.toString();
    // }

    // ========== BAI 5: Quy doi tien te - Input: amount, from, to (USD, EUR, JPY, VND) - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String quyDoiTienTe(double amount, String from, String to) throws RemoteException {
    //     Map<String, Double> rates = new HashMap<>();
    //     rates.put("VND", 1.0); rates.put("USD", 25000.0); rates.put("EUR", 27000.0); rates.put("JPY", 170.0);
    //     String f = (from == null) ? "" : from.trim().toUpperCase();
    //     String t = (to == null) ? "" : to.trim().toUpperCase();
    //     if (!rates.containsKey(f) || !rates.containsKey(t)) return "Chi ho tro tien te: VND, USD, EUR, JPY";
    //     double inVnd = amount * rates.get(f);
    //     double res = inVnd / rates.get(t);
    //     return String.format("%.2f %s = %.4f %s", amount, f, res, t);
    // }

    // ========== BAI 6: Kiem tra so nguyen to - Input: n - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public boolean isPrime(long n) throws RemoteException {
    //     if (n < 2) return false;
    //     for (long i = 2; i * i <= n; i++) if (n % i == 0) return false;
    //     return true;
    // }

    // ========== BAI 7: Sap xep tang dan danh sach so - Input: "5,2,9,1" - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String sapXepTangDan(String inputNumbers) throws RemoteException {
    //     if (inputNumbers == null || inputNumbers.trim().isEmpty()) return "Danh sach rong";
    //     String[] tokens = inputNumbers.trim().split("[ ,\\s]+");
    //     List<Double> list = new ArrayList<>();
    //     for (String s : tokens) if (!s.trim().isEmpty()) list.add(Double.parseDouble(s.trim()));
    //     Collections.sort(list);
    //     return "Tang dan: " + list.toString();
    // }

    // ========== BAI 8: Sap xep giam dan danh sach so - Input: "5,2,9,1" - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String sapXepGiamDan(String inputNumbers) throws RemoteException {
    //     if (inputNumbers == null || inputNumbers.trim().isEmpty()) return "Danh sach rong";
    //     String[] tokens = inputNumbers.trim().split("[ ,\\s]+");
    //     List<Double> list = new ArrayList<>();
    //     for (String s : tokens) if (!s.trim().isEmpty()) list.add(Double.parseDouble(s.trim()));
    //     list.sort(Collections.reverseOrder());
    //     return "Giam dan: " + list.toString();
    // }

    // ========== BAI 9: Thong ke so lan xuat hien cua tu - Input: str - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String thongKeTu(String str) throws RemoteException {
    //     if (str == null || str.trim().isEmpty()) return "Chuoi rong";
    //     String[] words = str.toLowerCase().trim().split("\\s+");
    //     Map<String, Integer> map = new LinkedHashMap<>();
    //     for (String w : words) if (!w.trim().isEmpty()) map.put(w, map.getOrDefault(w, 0) + 1);
    //     return map.toString();
    // }

    // ========== BAI 10: Sap xep chuoi theo chu cai - Input: "zebra,apple,cat" - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String sapXepChuoiTheoChuCai(String str) throws RemoteException {
    //     if (str == null || str.trim().isEmpty()) return "Chuoi rong";
    //     String[] words = str.split("[ ,\\s]+");
    //     List<String> list = new ArrayList<>();
    //     for (String w : words) if (!w.trim().isEmpty()) list.add(w.trim());
    //     Collections.sort(list);
    //     return list.toString();
    // }

    // ========== BAI 11: Dao nguoc chuoi - Input: str - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String daoChuoi(String str) throws RemoteException {
    //     if (str == null) return "";
    //     return new StringBuilder(str).reverse().toString();
    // }

    // ========== BAI 12: Ngat chuoi theo ky tu phan cach - Input: text, delimiter - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String ngatChuoi(String text, String delimiter) throws RemoteException {
    //     if (text == null) return "Chuoi rong";
    //     if (delimiter == null || delimiter.isEmpty()) delimiter = " ";
    //     String[] parts = text.split(java.util.regex.Pattern.quote(delimiter));
    //     return Arrays.toString(parts);
    // }

    // ========== BAI 13: UCLN va BCNN - Input: a, b - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String uclnVaBcnn(long a, long b) throws RemoteException {
    //     long x = Math.abs(a), y = Math.abs(b);
    //     long g = gcd(x, y);
    //     long l = (x == 0 || y == 0) ? 0 : (x / g) * y;
    //     return "UCLN=" + g + ", BCNN=" + l;
    // }

    // ========== BAI 14: Giai phuong trinh bac 1 (ax + b = 0) - Input: a, b - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String giaiPTBac1(double a, double b) throws RemoteException {
    //     if (a == 0 && b == 0) return "Vo so nghiem";
    //     if (a == 0) return "Vo nghiem";
    //     return String.format("Nghiem x = %.4f", -b / a);
    // }

    // ========== BAI 15: Giai phuong trinh bac 2 (ax^2 + bx + c = 0) - Input: a, b, c - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String giaiPTBac2(double a, double b, double c) throws RemoteException {
    //     if (a == 0) {
    //         if (b == 0 && c == 0) return "Vo so nghiem";
    //         if (b == 0) return "Vo nghiem";
    //         return String.format("Nghiem x = %.4f", -c / b);
    //     }
    //     double delta = b * b - 4 * a * c;
    //     if (delta < 0) return "Phuong trinh vo nghiem thuc";
    //     if (delta == 0) return String.format("Nghiem kep x1 = x2 = %.4f", -b / (2 * a));
    //     double x1 = (-b + Math.sqrt(delta)) / (2 * a);
    //     double x2 = (-b - Math.sqrt(delta)) / (2 * a);
    //     return String.format("x1 = %.4f, x2 = %.4f", x1, x2);
    // }

    // ========== BAI 16: Tinh tong 1..n - Input: n - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public long tong1DenN(long n) throws RemoteException {
    //     if (n < 0) return 0;
    //     return n * (n + 1) / 2;
    // }

    // ========== BAI 17: Dem nguyen am va phu am - Input: str - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String demNguyenAmPhuAm(String str) throws RemoteException {
    //     if (str == null) return "Chuoi rong";
    //     int v = 0, c = 0;
    //     String s = str.toLowerCase();
    //     for (char ch : s.toCharArray()) {
    //         if (ch >= 'a' && ch <= 'z') {
    //             if ("aeiou".indexOf(ch) >= 0) v++; else c++;
    //         }
    //     }
    //     return "Nguyen am = " + v + ", Phu am = " + c;
    // }

    // ========== BAI 18: Chuan hoa chuoi (Viet hoa dau moi tu) - Input: str - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String chuanHoaChuoi(String str) throws RemoteException {
    //     if (str == null || str.trim().isEmpty()) return "";
    //     String[] words = str.trim().toLowerCase().split("\\s+");
    //     StringBuilder sb = new StringBuilder();
    //     for (String w : words) {
    //         if (!w.trim().isEmpty()) {
    //             sb.append(Character.toUpperCase(w.charAt(0))).append(w.substring(1)).append(" ");
    //         }
    //     }
    //     return sb.toString().trim();
    // }

    // ========== BAI 19: Kiem tra chuoi Palindrome (Doi xung) - Input: str - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public boolean isPalindrome(String str) throws RemoteException {
    //     if (str == null) return false;
    //     String clean = str.replaceAll("\\s+", "").toLowerCase();
    //     String rev = new StringBuilder(clean).reverse().toString();
    //     return clean.equals(rev);
    // }

    // ========== BAI 20: Tinh giai thua (n!) - Input: n - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public long giaiThua(int n) throws RemoteException {
    //     if (n < 0) throw new IllegalArgumentException("n phai >= 0");
    //     long f = 1;
    //     for (int i = 2; i <= n; i++) f *= i;
    //     return f;
    // }

    // ========== BAI 21: Tinh tong cac chu so - Input: 12345 - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public int tongCacChuSo(String numberStr) throws RemoteException {
    //     if (numberStr == null) return 0;
    //     int sum = 0;
    //     for (char ch : numberStr.trim().toCharArray()) {
    //         if (Character.isDigit(ch)) sum += ch - '0';
    //     }
    //     return sum;
    // }

    // ========== BAI 22: Tinh tong danh sach so - Input: "1,2,3,4,5" - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public double tongDanhSachSo(String inputNumbers) throws RemoteException {
    //     if (inputNumbers == null || inputNumbers.trim().isEmpty()) return 0;
    //     String[] tokens = inputNumbers.trim().split("[ ,\\s]+");
    //     double sum = 0;
    //     for (String s : tokens) if (!s.trim().isEmpty()) sum += Double.parseDouble(s.trim());
    //     return sum;
    // }

    // ========== BAI 23: Tim Min va Max cua danh sach so - Input: "5,2,9,1" - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String timMinMax(String inputNumbers) throws RemoteException {
    //     if (inputNumbers == null || inputNumbers.trim().isEmpty()) return "Danh sach rong";
    //     String[] tokens = inputNumbers.trim().split("[ ,\\s]+");
    //     List<Double> list = new ArrayList<>();
    //     for (String s : tokens) if (!s.trim().isEmpty()) list.add(Double.parseDouble(s.trim()));
    //     if (list.isEmpty()) return "Danh sach rong";
    //     double min = list.get(0), max = list.get(0);
    //     for (double num : list) { if (num < min) min = num; if (num > max) max = num; }
    //     return String.format("Min=%.4f, Max=%.4f", min, max);
    // }

    // ========== BAI 24: Kiem tra chan le - Input: n - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String kiemTraChanLe(long n) throws RemoteException {
    //     return (n % 2 == 0) ? "So chan" : "So le";
    // }

    // ========== BAI 25: Chuyen chuoi sang IN HOA - Input: str - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String inHoa(String str) throws RemoteException {
    //     return (str == null) ? "" : str.toUpperCase();
    // }

    // ========== BAI 26: Chuyen chuoi sang in thuong - Input: str - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String inThuong(String str) throws RemoteException {
    //     return (str == null) ? "" : str.toLowerCase();
    // }

    // ========== BAI 27: Dem tong so ky tu (co space va khong space) - Input: str - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String demKyTu(String str) throws RemoteException {
    //     if (str == null) return "TongKyTu=0, KhongTinhSpace=0";
    //     int all = str.length();
    //     int noSpace = str.replace(" ", "").length();
    //     return "TongKyTu=" + all + ", KhongTinhSpace=" + noSpace;
    // }

    // ========== BAI 28: Dien tich Hinh Chu Nhat - Input: dai, rong - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public double dienTichHCN(double dai, double rong) throws RemoteException {
    //     return dai * rong;
    // }

    // ========== BAI 29: Dien tich Hinh Tron - Input: r - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public double dienTichHinhTron(double r) throws RemoteException {
    //     if (r < 0) throw new IllegalArgumentException("Ban kinh phai >= 0");
    //     return Math.PI * r * r;
    // }

    // ========== BAI 30: Dien tich Hinh Thang - Input: a, b, h - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public double dienTichHinhThang(double a, double b, double h) throws RemoteException {
    //     if (h < 0) throw new IllegalArgumentException("Chieu cao phai >= 0");
    //     return (a + b) * h / 2.0;
    // }

    // ========== BAI 31: Chu vi Hinh Vuong - Input: side - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public double chuViHinhVuong(double side) throws RemoteException {
    //     return 4 * side;
    // }

    // ========== BAI 32: Chu vi Hinh Chu Nhat - Input: dai, rong - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public double chuViHCN(double dai, double rong) throws RemoteException {
    //     return 2 * (dai + rong);
    // }

    // ========== BAI 33: [ĐỀ THI GIỮA KỲ CÂU 1] Chuyen so thanh chu - Input: "3432" - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String doiSoThanhChu(String numberStr) throws RemoteException {
    //     if (numberStr == null || numberStr.trim().isEmpty()) return "Chuoi rong";
    //     String[] words = {"không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"};
    //     StringBuilder sb = new StringBuilder();
    //     for (char ch : numberStr.trim().toCharArray()) {
    //         if (ch >= '0' && ch <= '9') sb.append(words[ch - '0']).append(" ");
    //         else return "Chuoi chua ky tu khong phai chu so!";
    //     }
    //     return numberStr.trim() + ": " + sb.toString().trim();
    // }

    // ========== BAI 34: [ĐỀ THI GIỮA KỲ CÂU 2] Tim thong tin theo Email - Input: "abcd1234@gmail.com" - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String timNguoiDungTheoEmail(String email) throws RemoteException {
    //     if (email == null) return "Email khong hop le";
    //     Map<String, String> userDb = new HashMap<>();
    //     userDb.put("abcd1234@gmail.com", "HenryFord 825 893 5382");
    //     userDb.put("nguyenvana@gmail.com", "Nguyen Van A 0912345678");
    //     userDb.put("tranthib@gmail.com", "Tran Thi B 0987654321");
    //     File uFile = new File("users.txt");
    //     if (uFile.exists()) {
    //         try (BufferedReader br = new BufferedReader(new FileReader(uFile))) {
    //             String line;
    //             while ((line = br.readLine()) != null) {
    //                 String[] p = line.split("[=:]", 2);
    //                 if (p.length == 2) userDb.put(p[0].trim().toLowerCase(), p[1].trim());
    //             }
    //         } catch (Exception ignored) {}
    //     }
    //     String key = email.trim().toLowerCase();
    //     if (userDb.containsKey(key)) return email.trim() + " và " + userDb.get(key);
    //     return email.trim() + " -> Khong tim thay nguoi dung";
    // }

    // ========== BAI 35: [THỰC HÀNH LAB 5] Sap xep day so - Input: "11 22 4 25 28 3" - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String sapXepDaySo(String inputNumbers) throws RemoteException {
    //     try {
    //         String[] tokens = inputNumbers.trim().split("[ ,\\s]+");
    //         List<Double> list = new ArrayList<>();
    //         for (String t : tokens) if (!t.trim().isEmpty()) list.add(Double.parseDouble(t));
    //         if (list.isEmpty()) return "Loi: Danh sach so rong";
    //         List<Double> asc = new ArrayList<>(list); Collections.sort(asc);
    //         List<Double> desc = new ArrayList<>(list); desc.sort(Collections.reverseOrder());
    //         return "Chuoi nhan duoc: " + inputNumbers.trim() +
    //                "\nChuoi sap giam dan: " + desc +
    //                "\nChuoi sap tang dan: " + asc;
    //     } catch (Exception e) {
    //         return "Loi: " + e.getMessage();
    //     }
    // }

    // ========== BAI 36: [THỰC HÀNH TUẦN 3] Doc file van ban tren Server - Input: "users.txt" - [KHONG CAN SinhVien.java] ==========
    // @Override
    // public String docFile(String fileName) throws RemoteException {
    //     File f = new File(fileName);
    //     if (!f.exists()) return "Loi: File '" + fileName + "' khong ton tai tren Server!";
    //     StringBuilder sb = new StringBuilder();
    //     try (BufferedReader br = new BufferedReader(new FileReader(f))) {
    //         String line;
    //         while ((line = br.readLine()) != null) sb.append(line).append("\n");
    //         return sb.toString();
    //     } catch (Exception e) {
    //         return "Loi khi doc file: " + e.getMessage();
    //     }
    // }

    // ========== BAI 37: [THỰC HÀNH TUẦN 1 & 3 - ⚠️ CẦN SinhVien.java] Tim sinh vien theo ma - Input: "SV01" ==========
    // @Override
    // public SinhVien timSinhVienTheoMa(String maSV) throws RemoteException {
    //     List<SinhVien> ds = new ArrayList<>();
    //     ds.add(new SinhVien("SV01", "Nguyen Van An", 8.5));
    //     ds.add(new SinhVien("SV02", "Tran Thi Binh", 7.2));
    //     ds.add(new SinhVien("SV03", "Le Van Cuong", 9.0));
    //     if (maSV == null) return null;
    //     for (SinhVien sv : ds) {
    //         if (sv.getMaSV().equalsIgnoreCase(maSV.trim())) return sv;
    //     }
    //     return null;
    // }

    // Helper: UCLN (can dung cho Bai 13)
    // private static long gcd(long a, long b) {
    //     while (b != 0) { long t = a % b; a = b; b = t; }
    //     return Math.abs(a);
    // }
}
```

---

### 7. RMI `RMIClient.java`
```java
package gkrmi;

import java.rmi.Naming;
import java.util.Scanner;

public class RMIClient {
    public static final String HOST = "localhost";
    public static final int PORT = 1099;
    public static final String SERVICE_NAME = "RemoteService";

    public static void main(String[] args) {
        String rmiUrl = "rmi://" + HOST + ":" + PORT + "/" + SERVICE_NAME;

        try {
            System.out.println("Dang ket noi toi Server tai: " + rmiUrl);
            IRemoteService service = (IRemoteService) Naming.lookup(rmiUrl);
            System.out.println("Ket noi thanh cong!\n");

            Scanner scanner = new Scanner(System.in);

            // ========== BAI 1: May tinh 4 phep tinh (+, -, *, /) - [MAC DINH BAT] [KHONG CAN SinhVien.java] ==========
            System.out.println("=== BÀI 1: MÁY TÍNH 4 PHÉP TÍNH ===");
            System.out.print("Nhap so thu nhat (a): ");
            int a = scanner.nextInt();
            System.out.print("Nhap so thu hai (b): ");
            int b = scanner.nextInt();
            System.out.println(a + " + " + b + " = " + service.add(a, b));
            System.out.println(a + " - " + b + " = " + service.sub(a, b));
            System.out.println(a + " * " + b + " = " + service.mul(a, b));
            try {
                System.out.println(a + " / " + b + " = " + service.div(a, b));
            } catch (Exception e) {
                System.out.println("Loi: " + e.getMessage());
            }

            // ========== BAI 2: Tam giac (Chu vi, dien tich Heron) - Input: a, b, c - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 2: TÍNH TAM GIÁC ===");
            // System.out.print("Nhap canh a: "); double a = scanner.nextDouble();
            // System.out.print("Nhap canh b: "); double b = scanner.nextDouble();
            // System.out.print("Nhap canh c: "); double c = scanner.nextDouble();
            // System.out.println("Ket qua: " + service.tinhTamGiac(a, b, c));

            // ========== BAI 3: So phuc (ADD/SUB/MUL/DIV) - Input: op, ar, ai, br, bi - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 3: SỐ PHỨC ===");
            // System.out.print("Nhap phep tinh (ADD/SUB/MUL/DIV): "); String op = scanner.nextLine().trim();
            // System.out.print("Nhap phan thuc a: "); double ar = scanner.nextDouble();
            // System.out.print("Nhap phan ao a: "); double ai = scanner.nextDouble();
            // System.out.print("Nhap phan thuc b: "); double br = scanner.nextDouble();
            // System.out.print("Nhap phan ao b: "); double bi = scanner.nextDouble();
            // System.out.println("Ket qua: " + service.soPhuc(op, ar, ai, br, bi));

            // ========== BAI 4: So Fibonacci / In day Fibonacci - Input: n - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 4: FIBONACCI ===");
            // System.out.print("Nhap n: "); int n = scanner.nextInt();
            // System.out.println("Ket qua: " + service.fibonacci(n));

            // ========== BAI 5: Quy doi tien te - Input: amount, from, to (USD, EUR, JPY, VND) - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 5: QUY ĐỔI TIỀN TỆ ===");
            // System.out.print("Nhap so tien: "); double amt = scanner.nextDouble();
            // scanner.nextLine();
            // System.out.print("Tu loai tien (VND, USD, EUR, JPY): "); String from = scanner.nextLine().trim();
            // System.out.print("Sang loai tien (VND, USD, EUR, JPY): "); String to = scanner.nextLine().trim();
            // System.out.println("Ket qua: " + service.quyDoiTienTe(amt, from, to));

            // ========== BAI 6: Kiem tra so nguyen to - Input: n - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 6: KIỂM TRA SỐ NGUYÊN TỐ ===");
            // System.out.print("Nhap n: "); long n = scanner.nextLong();
            // System.out.println(n + (service.isPrime(n) ? " la so nguyen to" : " khong phai so nguyen to"));

            // ========== BAI 7: Sap xep tang dan danh sach so - Input: "5,2,9,1" - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 7: SẮP XẾP TĂNG DẦN ===");
            // System.out.print("Nhap danh sach so (vd: 5,2,9,1 hoac 5 2 9 1): ");
            // String nums = scanner.nextLine().trim();
            // System.out.println("Ket qua: " + service.sapXepTangDan(nums));

            // ========== BAI 8: Sap xep giam dan danh sach so - Input: "5,2,9,1" - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 8: SẮP XẾP GIẢM DẦN ===");
            // System.out.print("Nhap danh sach so (vd: 5,2,9,1 hoac 5 2 9 1): ");
            // String nums = scanner.nextLine().trim();
            // System.out.println("Ket qua: " + service.sapXepGiamDan(nums));

            // ========== BAI 9: Thong ke so lan xuat hien cua tu - Input: str - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 9: THỐNG KÊ TỪ ===");
            // System.out.print("Nhap chuoi van ban: ");
            // String text = scanner.nextLine().trim();
            // System.out.println("Ket qua: " + service.thongKeTu(text));

            // ========== BAI 10: Sap xep chuoi theo chu cai - Input: "zebra,apple,cat" - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 10: SẮP XẾP CHUỖI THEO BẢNG CHỮ CÁI ===");
            // System.out.print("Nhap chuoi cac tu (vd: zebra,apple,cat): ");
            // String text = scanner.nextLine().trim();
            // System.out.println("Ket qua: " + service.sapXepChuoiTheoChuCai(text));

            // ========== BAI 11: Dao nguoc chuoi - Input: str - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 11: ĐẢO NGƯỢC CHUỖI ===");
            // System.out.print("Nhap chuoi: ");
            // String text = scanner.nextLine();
            // System.out.println("Ket qua dao: " + service.daoChuoi(text));

            // ========== BAI 12: Ngat chuoi theo ky tu phan cach - Input: text, delimiter - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 12: NGẮT CHUỖI ===");
            // System.out.print("Nhap chuoi: "); String text = scanner.nextLine();
            // System.out.print("Nhap ky tu phan cach (delimiter): "); String delim = scanner.nextLine();
            // System.out.println("Ket qua: " + service.ngatChuoi(text, delim));

            // ========== BAI 13: UCLN va BCNN - Input: a, b - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 13: UCLN VÀ BCNN ===");
            // System.out.print("Nhap so a: "); long a = scanner.nextLong();
            // System.out.print("Nhap so b: "); long b = scanner.nextLong();
            // System.out.println("Ket qua: " + service.uclnVaBcnn(a, b));

            // ========== BAI 14: Giai phuong trinh bac 1 (ax + b = 0) - Input: a, b - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 14: GIẢI PHƯƠNG TRÌNH BẬC 1 ===");
            // System.out.print("Nhap he so a: "); double a = scanner.nextDouble();
            // System.out.print("Nhap he so b: "); double b = scanner.nextDouble();
            // System.out.println("Ket qua: " + service.giaiPTBac1(a, b));

            // ========== BAI 15: Giai phuong trinh bac 2 (ax^2 + bx + c = 0) - Input: a, b, c - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 15: GIẢI PHƯƠNG TRÌNH BẬC 2 ===");
            // System.out.print("Nhap he so a: "); double a = scanner.nextDouble();
            // System.out.print("Nhap he so b: "); double b = scanner.nextDouble();
            // System.out.print("Nhap he so c: "); double c = scanner.nextDouble();
            // System.out.println("Ket qua: " + service.giaiPTBac2(a, b, c));

            // ========== BAI 16: Tinh tong 1..n - Input: n - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 16: TÍNH TỔNG 1 ĐẾN N ===");
            // System.out.print("Nhap n: "); long n = scanner.nextLong();
            // System.out.println("Tong 1 den " + n + " = " + service.tong1DenN(n));

            // ========== BAI 17: Dem nguyen am va phu am - Input: str - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 17: ĐẾM NGUYÊN ÂM VÀ PHỤ ÂM ===");
            // System.out.print("Nhap chuoi: "); String text = scanner.nextLine();
            // System.out.println("Ket qua: " + service.demNguyenAmPhuAm(text));

            // ========== BAI 18: Chuan hoa chuoi (Viet hoa dau moi tu) - Input: str - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 18: CHUẨN HÓA CHUỖI ===");
            // System.out.print("Nhap chuoi can chuan hoa: "); String text = scanner.nextLine();
            // System.out.println("Ket qua: " + service.chuanHoaChuoi(text));

            // ========== BAI 19: Kiem tra chuoi Palindrome (Doi xung) - Input: str - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 19: KIỂM TRA PALINDROME ===");
            // System.out.print("Nhap chuoi: "); String text = scanner.nextLine();
            // System.out.println("Ket qua: " + (service.isPalindrome(text) ? "La chuoi Palindrome" : "Khong phai Palindrome"));

            // ========== BAI 20: Tinh giai thua (n!) - Input: n - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 20: TÍNH GIAI THỪA ===");
            // System.out.print("Nhap n: "); int n = scanner.nextInt();
            // System.out.println(n + "! = " + service.giaiThua(n));

            // ========== BAI 21: Tinh tong cac chu so - Input: 12345 - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 21: TỔNG CÁC CHỮ SỐ ===");
            // System.out.print("Nhap so nguyen: "); String numStr = scanner.nextLine().trim();
            // System.out.println("Tong cac chu so = " + service.tongCacChuSo(numStr));

            // ========== BAI 22: Tinh tong danh sach so - Input: "1,2,3,4,5" - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 22: TỔNG DANH SÁCH SỐ ===");
            // System.out.print("Nhap day so (vd: 1,2,3,4,5 hoac 1 2 3): "); String nums = scanner.nextLine().trim();
            // System.out.println("Tong = " + service.tongDanhSachSo(nums));

            // ========== BAI 23: Tim Min va Max cua danh sach so - Input: "5,2,9,1" - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 23: TÌM MIN VÀ MAX ===");
            // System.out.print("Nhap day so (vd: 5,2,9,1 hoac 5 2 9 1): "); String nums = scanner.nextLine().trim();
            // System.out.println("Ket qua: " + service.timMinMax(nums));

            // ========== BAI 24: Kiem tra chan le - Input: n - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 24: KIỂM TRA CHẴN LẺ ===");
            // System.out.print("Nhap n: "); long n = scanner.nextLong();
            // System.out.println("Ket qua: " + service.kiemTraChanLe(n));

            // ========== BAI 25: Chuyen chuoi sang IN HOA - Input: str - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 25: IN HOA ===");
            // System.out.print("Nhap chuoi: "); String text = scanner.nextLine();
            // System.out.println("Ket qua: " + service.inHoa(text));

            // ========== BAI 26: Chuyen chuoi sang in thuong - Input: str - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 26: IN THƯỜNG ===");
            // System.out.print("Nhap chuoi: "); String text = scanner.nextLine();
            // System.out.println("Ket qua: " + service.inThuong(text));

            // ========== BAI 27: Dem tong so ky tu (co space va khong space) - Input: str - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 27: ĐẾM KÝ TỰ ===");
            // System.out.print("Nhap chuoi: "); String text = scanner.nextLine();
            // System.out.println("Ket qua: " + service.demKyTu(text));

            // ========== BAI 28: Dien tich Hinh Chu Nhat - Input: dai, rong - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 28: DIỆN TÍCH HÌNH CHỮ NHẬT ===");
            // System.out.print("Nhap chieu dai: "); double dai = scanner.nextDouble();
            // System.out.print("Nhap chieu rong: "); double rong = scanner.nextDouble();
            // System.out.println("Dien tich HCN = " + service.dienTichHCN(dai, rong));

            // ========== BAI 29: Dien tich Hinh Tron - Input: r - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 29: DIỆN TÍCH HÌNH TRÒN ===");
            // System.out.print("Nhap ban kinh r: "); double r = scanner.nextDouble();
            // System.out.println("Dien tich Hinh Tron = " + service.dienTichHinhTron(r));

            // ========== BAI 30: Dien tich Hinh Thang - Input: a, b, h - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 30: DIỆN TÍCH HÌNH THANG ===");
            // System.out.print("Nhap day lon a: "); double a = scanner.nextDouble();
            // System.out.print("Nhap day be b: "); double b = scanner.nextDouble();
            // System.out.print("Nhap chieu cao h: "); double h = scanner.nextDouble();
            // System.out.println("Dien tich Hinh Thang = " + service.dienTichHinhThang(a, b, h));

            // ========== BAI 31: Chu vi Hinh Vuong - Input: side - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 31: CHU VI HÌNH VUÔNG ===");
            // System.out.print("Nhap canh hinh vuong: "); double side = scanner.nextDouble();
            // System.out.println("Chu vi Hinh Vuong = " + service.chuViHinhVuong(side));

            // ========== BAI 32: Chu vi Hinh Chu Nhat - Input: dai, rong - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 32: CHU VI HÌNH CHỮ NHẬT ===");
            // System.out.print("Nhap chieu dai: "); double dai = scanner.nextDouble();
            // System.out.print("Nhap chieu rong: "); double rong = scanner.nextDouble();
            // System.out.println("Chu vi HCN = " + service.chuViHCN(dai, rong));

            // ========== BAI 33: [ĐỀ THI GIỮA KỲ CÂU 1] Chuyen so thanh chu - Input: "3432" - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 33: CHUYỂN SỐ THÀNH CHỮ ===");
            // System.out.print("Nhap chuoi chu so (vd: 3432): ");
            // String num = scanner.nextLine().trim();
            // System.out.println("Ket qua: " + service.doiSoThanhChu(num));

            // ========== BAI 34: [ĐỀ THI GIỮA KỲ CÂU 2] Tim thong tin theo Email - Input: "abcd1234@gmail.com" - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 34: TÌM THÔNG TIN THEO EMAIL ===");
            // System.out.print("Nhap email can tim (vd: abcd1234@gmail.com): ");
            // String email = scanner.nextLine().trim();
            // System.out.println("Ket qua: " + service.timNguoiDungTheoEmail(email));

            // ========== BAI 35: [THỰC HÀNH LAB 5] Sap xep day so - Input: "11 22 4 25 28 3" - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 35: SẮP XẾP DÃY SỐ ===");
            // System.out.print("Nhap day so cach nhau khoang trang (vd: 11 22 4 25 28 3): ");
            // String daySo = scanner.nextLine().trim();
            // System.out.println("Ket qua:\n" + service.sapXepDaySo(daySo));

            // ========== BAI 36: [THỰC HÀNH TUẦN 3] Doc file van ban tren Server - Input: "users.txt" - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 36: ĐỌC FILE VĂN BẢN TRÊN SERVER ===");
            // System.out.print("Nhap ten file can doc (vd: users.txt): ");
            // String fName = scanner.nextLine().trim();
            // System.out.println("--- NOI DUNG FILE ---\n" + service.docFile(fName));

            // ========== BAI 37: [THỰC HÀNH TUẦN 1 & 3 - ⚠️ CẦN SinhVien.java] Tim sinh vien theo ma - Input: "SV01" ==========
            // System.out.println("=== BÀI 37: TÌM SINH VIÊN THEO MÃ ===");
            // System.out.print("Nhap ma SV (vd: SV01): ");
            // String maSV = scanner.nextLine().trim();
            // SinhVien sv = service.timSinhVienTheoMa(maSV);
            // if (sv != null) System.out.println("Tim thay: " + sv);
            // else System.out.println("Khong tim thay sinh vien!");

            scanner.close();
        } catch (Exception e) {
            System.err.println("Loi Client: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
```

---

## VII. BẢNG TỔNG HỢP CÔNG THỨC & THUẬT TOÁN THI GIỮA KỲ

| STT | Dạng bài toán | Ý tưởng thuật toán cốt lõi | Lưu ý đặc biệt |
| :---: | :--- | :--- | :--- |
| **1** | **Máy tính (+, -, *, /)** | Nhận toán tử và 2 số, kiểm tra `b == 0` khi chia | Bắt ngoại lệ `ArithmeticException` |
| **2** | **Tam giác Heron** | $p = a+b+c$; $S = \sqrt{\frac{p}{2}(\frac{p}{2}-a)(\frac{p}{2}-b)(\frac{p}{2}-c)}$ | Kiểm tra BĐT tam giác: $a+b>c$, $a+c>b$, $b+c>a$ |
| **3** | **Số phức** | $(a+bi)(c+di) = (ac-bd) + (ad+bc)i$; Chia nhân liên hợp mẫu $c^2+d^2$ | Kiểm tra mẫu số khác 0 |
| **4** | **Fibonacci** | Vòng lặp: `c = a + b; a = b; b = c;` | Xử lý $n=0$, $n=1$, $n \ge 2$ |
| **5** | **Quy đổi tiền** | Lưu tỷ giá vào `Map<String, Double>` theo VND | Chuẩn hóa mã tiền `.toUpperCase()` |
| **6** | **Số nguyên tố** | Duyệt từ 2 đến $\sqrt{n}$, nếu $n \% i == 0$ thì loại | $n < 2$ không phải số nguyên tố |
| **7** | **Sắp xếp dãy số** | `Collections.sort(list)` (tăng); `list.sort(reverseOrder())` (giảm) | Tách chuỗi bằng regex `[ ,\\s]+` |
| **8** | **Thống kê từ** | `Map<String, Integer> map = new LinkedHashMap<>()` | `.toLowerCase()`, split bằng `\\s+` |
| **9** | **Đảo chuỗi** | `new StringBuilder(str).reverse().toString()` | Xử lý chuỗi rỗng/null |
| **10** | **UCLN & BCNN** | Thuật toán Euclid: `while(b!=0){ t=a%b; a=b; b=t; }`; $BCNN = \frac{a \times b}{UCLN}$ | Lấy trị tuyệt đối `Math.abs()` |
| **11** | **PT bậc 1** | $ax + b = 0 \Rightarrow x = -b/a$ | $a=0, b=0 \Rightarrow$ VSN; $a=0, b \ne 0 \Rightarrow$ VN |
| **12** | **PT bậc 2** | $\Delta = b^2 - 4ac$; $\Delta < 0$ VN, $\Delta = 0$ nghiệm kép, $\Delta > 0$ 2 nghiệm | Nếu $a=0$ gọi lại giải PT bậc 1 |
| **13** | **Palindrome** | Xóa khoảng trắng, so sánh chuỗi gốc với chuỗi đảo ngược | `.replaceAll("\\s+", "").toLowerCase()` |
| **14** | **Giai thừa** | $n! = 1 \times 2 \times \dots \times n$ | Dùng kiểu `long` để tránh tràn số |
| **15** | **Tổng chữ số** | Lặp qua `toCharArray()`, nếu là `Character.isDigit` thì cộng `ch - '0'` | Bỏ qua dấu âm nếu có |
| **16** | **Chuyển số thành chữ** | Mảng từ `{"không", "một", "hai", ..., "chín"}` mapping theo ký tự | Đề thi GK Câu 1 hay ra dạng này |
| **17** | **Tra cứu Email** | Lưu DB trong `Map` hoặc đọc từ file `users.txt` bằng `split("[=:]", 2)` | Đề thi GK Câu 2 hay ra dạng này |
| **18** | **Đọc file Server** | `BufferedReader` đọc từng dòng hoặc `FileHelper.readFile()` | Kiểm tra `file.exists()` |
| **19** | **Đối tượng SinhVien** | `class SinhVien implements Serializable` | Cần `serialVersionUID`, getter/setter |
