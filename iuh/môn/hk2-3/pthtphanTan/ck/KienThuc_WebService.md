# KIẾN THỨC WEB SERVICE (Spring Boot REST) - ÔN THI CUỐI KỲ

---

## 1. KHÁI NIỆM WEB SERVICE

**Web Service** là một hệ thống phần mềm hỗ trợ giao tiếp giữa các máy tính qua mạng Internet.

- Cho phép các ứng dụng viết bằng **ngôn ngữ khác nhau**, chạy trên **nền tảng khác nhau** giao tiếp được với nhau.
- Giao tiếp qua **giao thức chuẩn** (HTTP).
- **RESTful Web Service**: Dùng HTTP thuần (GET, POST, PUT, DELETE), dữ liệu trả về dạng **JSON**.

---

## 2. KIẾN TRÚC REST (Representational State Transfer)

| Đặc điểm           | Chi tiết                                                    |
| ---------------------- | ------------------------------------------------------------ |
| Giao thức             | HTTP thuần (GET, POST, PUT, DELETE)                         |
| Định dạng dữ liệu | JSON (phổ biến) hoặc XML                                  |
| Kiến trúc            | **Stateless** (Server không lưu trạng thái Client) |
| URL                    | Mỗi tài nguyên có 1 URL riêng (endpoint)                |

### Các HTTP Method:

| Method           | Ý nghĩa            | Ví dụ                        |
| ---------------- | -------------------- | ------------------------------ |
| **GET**    | Lấy dữ liệu       | `GET /api/tinh/cong?a=3&b=5` |
| **POST**   | Gửi dữ liệu mới  | `POST /api/tinh` + body JSON |
| **PUT**    | Cập nhật dữ liệu | `PUT /api/tinh/1`            |
| **DELETE** | Xóa dữ liệu       | `DELETE /api/tinh/1`         |

---

## 3. CẤU TRÚC PROJECT SPRING BOOT

```
project/
├── src/main/java/com/example/demo/
│   ├── DemoApplication.java          ← Main (khởi chạy)
│   ├── controller/
│   │   └── TinhToanController.java   ← REST Controller (nhận request)
│   ├── service/
│   │   └── TinhToanService.java      ← Logic xử lý
│   └── model/
│       └── KetQua.java               ← Model trả về JSON
├── src/main/resources/
│   └── application.properties        ← Cấu hình (port, database...)
└── pom.xml                           ← Dependencies
```

---

## 4. CÁC ANNOTATION QUAN TRỌNG (THUỘC LÒNG)

| Annotation                  | Đặt ở          | Vai trò                                              |
| --------------------------- | ----------------- | ----------------------------------------------------- |
| `@SpringBootApplication`  | Class main        | Đánh dấu đây là ứng dụng Spring Boot          |
| `@RestController`         | Class controller  | Đánh dấu class là REST API (trả JSON tự động) |
| `@RequestMapping("/api")` | Class controller  | Đặt prefix URL chung cho cả class                  |
| `@GetMapping("/path")`    | Method            | Xử lý request HTTP GET                              |
| `@PostMapping("/path")`   | Method            | Xử lý request HTTP POST                             |
| `@RequestParam`           | Tham số method   | Nhận tham số từ URL query (`?a=3&b=5`)           |
| `@PathVariable`           | Tham số method   | Nhận tham số từ URL path (`/cong/3/5`)           |
| `@RequestBody`            | Tham số method   | Nhận dữ liệu JSON từ body request                 |
| `@Service`                | Class service     | Đánh dấu class chứa logic nghiệp vụ             |
| `@Autowired`              | Field/Constructor | Tự động inject (tiêm) dependency                  |

---

## 5. CODE MẪU: DỊCH VỤ TÍNH TOÁN (ĐỦ CÁC DẠNG)

### 5.1 File `DemoApplication.java` (Main - Khởi chạy)

```java
package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class DemoApplication {
    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }
}
```

---

### 5.2 File `KetQua.java` (Model - Đối tượng trả về JSON)

```java
package com.example.demo.model;

public class KetQua {
    private String phepTinh;
    private String ketQua;
    private String moTa;

    public KetQua() {}

    public KetQua(String phepTinh, String ketQua, String moTa) {
        this.phepTinh = phepTinh;
        this.ketQua = ketQua;
        this.moTa = moTa;
    }

    // Getter và Setter (BẮT BUỘC để Spring chuyển sang JSON)
    public String getPhepTinh() { return phepTinh; }
    public void setPhepTinh(String phepTinh) { this.phepTinh = phepTinh; }

    public String getKetQua() { return ketQua; }
    public void setKetQua(String ketQua) { this.ketQua = ketQua; }

    public String getMoTa() { return moTa; }
    public void setMoTa(String moTa) { this.moTa = moTa; }
}
```

Khi trả về từ Controller, Spring tự chuyển thành JSON:

```json
{
    "phepTinh": "3 + 5",
    "ketQua": "8",
    "moTa": "Phep cong 2 so"
}
```

---

### 5.3 File `TinhToanService.java` (Service - Logic xử lý)

```java
package com.example.demo.service;

import org.springframework.stereotype.Service;
import java.util.*;

@Service
public class TinhToanService {

    // Cộng 2 số
    public double cong(double a, double b) {
        return a + b;
    }

    // Trừ 2 số
    public double tru(double a, double b) {
        return a - b;
    }

    // Nhân 2 số
    public double nhan(double a, double b) {
        return a * b;
    }

    // Chia 2 số
    public double chia(double a, double b) {
        if (b == 0) throw new ArithmeticException("Khong the chia cho 0");
        return a / b;
    }

    // Kiểm tra số nguyên tố
    public boolean laSoNguyenTo(long n) {
        if (n < 2) return false;
        for (long i = 2; i * i <= n; i++) {
            if (n % i == 0) return false;
        }
        return true;
    }

    // Giai thừa
    public long giaiThua(int n) {
        if (n < 0) throw new IllegalArgumentException("n phai >= 0");
        long result = 1;
        for (int i = 2; i <= n; i++) result *= i;
        return result;
    }

    // Fibonacci
    public String fibonacci(int n) {
        if (n < 0) return "n phai >= 0";
        StringBuilder sb = new StringBuilder();
        long a = 0, b = 1;
        for (int i = 0; i <= n; i++) {
            if (i > 0) sb.append(", ");
            sb.append(a);
            long c = a + b; a = b; b = c;
        }
        return sb.toString();
    }

    // ƯCLN - BCNN
    public Map<String, Long> uclnBcnn(long a, long b) {
        a = Math.abs(a); b = Math.abs(b);
        long x = a, y = b;
        while (y != 0) { long t = x % y; x = y; y = t; }
        long ucln = Math.abs(x);
        long bcnn = (a == 0 || b == 0) ? 0 : (a / ucln) * b;
        Map<String, Long> result = new LinkedHashMap<>();
        result.put("UCLN", ucln);
        result.put("BCNN", bcnn);
        return result;
    }

    // Đảo chuỗi
    public String daoChuoi(String text) {
        return new StringBuilder(text).reverse().toString();
    }

    // Sắp xếp tăng dần
    public List<Double> sapXepTangDan(String numbers) {
        String[] parts = numbers.trim().split("[,\\s]+");
        List<Double> list = new ArrayList<>();
        for (String s : parts) list.add(Double.parseDouble(s.trim()));
        Collections.sort(list);
        return list;
    }

    // Thống kê từ
    public Map<String, Integer> thongKeTu(String text) {
        String[] words = text.toLowerCase().trim().split("\\s+");
        Map<String, Integer> map = new LinkedHashMap<>();
        for (String w : words) {
            if (!w.isBlank()) map.put(w, map.getOrDefault(w, 0) + 1);
        }
        return map;
    }

    // Quy đổi tiền tệ
    public String quyDoiTienTe(double amount, String from, String to) {
        Map<String, Double> rate = new HashMap<>();
        rate.put("VND", 1.0);
        rate.put("USD", 25000.0);
        rate.put("EUR", 27000.0);
        rate.put("JPY", 170.0);
        from = from.toUpperCase(); to = to.toUpperCase();
        if (!rate.containsKey(from) || !rate.containsKey(to))
            return "Chi ho tro: VND, USD, EUR, JPY";
        double vnd = amount * rate.get(from);
        return String.format("%.4f %s", vnd / rate.get(to), to);
    }
}
```

---

### 5.4 File `TinhToanController.java` (Controller - Nhận request)

```java
package com.example.demo.controller;

import com.example.demo.model.KetQua;
import com.example.demo.service.TinhToanService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import java.util.*;

@RestController
@RequestMapping("/api/tinh")
public class TinhToanController {

    @Autowired
    private TinhToanService service;

    // ===== PHÉP TÍNH CƠ BẢN =====

    // GET http://localhost:8080/api/tinh/cong?a=3&b=5
    @GetMapping("/cong")
    public KetQua cong(@RequestParam double a, @RequestParam double b) {
        double kq = service.cong(a, b);
        return new KetQua(a + " + " + b, String.valueOf(kq), "Phep cong");
    }

    // GET http://localhost:8080/api/tinh/tru?a=10&b=3
    @GetMapping("/tru")
    public KetQua tru(@RequestParam double a, @RequestParam double b) {
        double kq = service.tru(a, b);
        return new KetQua(a + " - " + b, String.valueOf(kq), "Phep tru");
    }

    // GET http://localhost:8080/api/tinh/nhan?a=4&b=5
    @GetMapping("/nhan")
    public KetQua nhan(@RequestParam double a, @RequestParam double b) {
        double kq = service.nhan(a, b);
        return new KetQua(a + " * " + b, String.valueOf(kq), "Phep nhan");
    }

    // GET http://localhost:8080/api/tinh/chia?a=10&b=3
    @GetMapping("/chia")
    public KetQua chia(@RequestParam double a, @RequestParam double b) {
        double kq = service.chia(a, b);
        return new KetQua(a + " / " + b, String.valueOf(kq), "Phep chia");
    }

    // ===== DÙNG PathVariable (tham số trong URL) =====

    // GET http://localhost:8080/api/tinh/nguyento/17
    @GetMapping("/nguyento/{n}")
    public KetQua nguyenTo(@PathVariable long n) {
        boolean kq = service.laSoNguyenTo(n);
        return new KetQua("isPrime(" + n + ")",
                String.valueOf(kq),
                kq ? "La so nguyen to" : "Khong phai so nguyen to");
    }

    // GET http://localhost:8080/api/tinh/giaithua/5
    @GetMapping("/giaithua/{n}")
    public KetQua giaiThua(@PathVariable int n) {
        long kq = service.giaiThua(n);
        return new KetQua(n + "!", String.valueOf(kq), "Giai thua");
    }

    // GET http://localhost:8080/api/tinh/fibonacci/10
    @GetMapping("/fibonacci/{n}")
    public KetQua fibonacci(@PathVariable int n) {
        String kq = service.fibonacci(n);
        return new KetQua("Fibonacci(" + n + ")", kq, "Day Fibonacci");
    }

    // ===== DÙNG RequestParam nhiều tham số =====

    // GET http://localhost:8080/api/tinh/ucln-bcnn?a=24&b=36
    @GetMapping("/ucln-bcnn")
    public Map<String, Long> uclnBcnn(@RequestParam long a, @RequestParam long b) {
        return service.uclnBcnn(a, b);
    }

    // GET http://localhost:8080/api/tinh/quidoi?amount=100&from=USD&to=VND
    @GetMapping("/quidoi")
    public KetQua quyDoi(@RequestParam double amount,
                         @RequestParam String from,
                         @RequestParam String to) {
        String kq = service.quyDoiTienTe(amount, from, to);
        return new KetQua(amount + " " + from + " -> " + to, kq, "Quy doi tien te");
    }

    // ===== DÙNG POST + RequestBody (nhận JSON) =====

    // POST http://localhost:8080/api/tinh/daochuoi
    // Body: { "text": "Hello World" }
    @PostMapping("/daochuoi")
    public KetQua daoChuoi(@RequestBody Map<String, String> body) {
        String text = body.get("text");
        String kq = service.daoChuoi(text);
        return new KetQua("reverse(\"" + text + "\")", kq, "Dao chuoi");
    }

    // POST http://localhost:8080/api/tinh/sapxep
    // Body: { "numbers": "5,2,9,1,7" }
    @PostMapping("/sapxep")
    public List<Double> sapXep(@RequestBody Map<String, String> body) {
        return service.sapXepTangDan(body.get("numbers"));
    }

    // POST http://localhost:8080/api/tinh/thongke
    // Body: { "text": "phat trien he thong phat trien" }
    @PostMapping("/thongke")
    public Map<String, Integer> thongKe(@RequestBody Map<String, String> body) {
        return service.thongKeTu(body.get("text"));
    }
}
```

---

## 6. CÁCH CHẠY VÀ TEST

### 6.1 Chạy Server

```bash
mvn spring-boot:run
```

Hoặc chạy `DemoApplication.java` trực tiếp trong Eclipse/IntelliJ.

Server chạy tại: `http://localhost:8080`

### 6.2 Test bằng trình duyệt (GET)

Mở trình duyệt, gõ thẳng URL:

```
http://localhost:8080/api/tinh/cong?a=3&b=5
http://localhost:8080/api/tinh/nguyento/17
http://localhost:8080/api/tinh/giaithua/5
http://localhost:8080/api/tinh/fibonacci/10
http://localhost:8080/api/tinh/ucln-bcnn?a=24&b=36
http://localhost:8080/api/tinh/quidoi?amount=100&from=USD&to=VND
```

### 6.3 Test bằng Postman hoặc curl (POST)

```bash
# Đảo chuỗi
curl -X POST http://localhost:8080/api/tinh/daochuoi \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello World"}'

# Sắp xếp
curl -X POST http://localhost:8080/api/tinh/sapxep \
  -H "Content-Type: application/json" \
  -d '{"numbers": "5,2,9,1,7"}'

# Thống kê từ
curl -X POST http://localhost:8080/api/tinh/thongke \
  -H "Content-Type: application/json" \
  -d '{"text": "phat trien he thong phat trien"}'
```

### 6.4 Kết quả JSON mẫu

**GET** `/api/tinh/cong?a=3&b=5`:

```json
{
    "phepTinh": "3.0 + 5.0",
    "ketQua": "8.0",
    "moTa": "Phep cong"
}
```

**GET** `/api/tinh/nguyento/17`:

```json
{
    "phepTinh": "isPrime(17)",
    "ketQua": "true",
    "moTa": "La so nguyen to"
}
```

**POST** `/api/tinh/thongke` + body `{"text": "phat trien he thong phat trien"}`:

```json
{
    "phat": 2,
    "trien": 2,
    "he": 1,
    "thong": 1
}
```

---

## 8. SO SÁNH 3 CÔNG NGHỆ (Socket vs RMI vs Web Service)

| Tiêu chí             | Socket (TCP)     | RMI                      | Web Service (REST)                |
| ---------------------- | ---------------- | ------------------------ | --------------------------------- |
| Mức trừu tượng     | Thấp            | Trung bình              | Cao                               |
| Ngôn ngữ             | Đa ngôn ngữ   | Chỉ Java                | Đa ngôn ngữ                    |
| Giao thức             | TCP/UDP          | JRMP (TCP)               | HTTP                              |
| Định dạng dữ liệu | Byte/Text        | Java Object              | **JSON**                    |
| Cách gọi             | Đọc/ghi stream | Gọi hàm trực tiếp    | Gọi qua **URL endpoint**  |
| Framework              | Không cần      | JDK built-in             | **Spring Boot**             |
| Port                   | Tùy ý          | Tùy ý                  | **8080** (mặc định)      |
| Test                   | Telnet/Code      | Code                     | **Trình duyệt / Postman** |
| Phù hợp              | Chat, game       | Hệ thống Java nội bộ | **API cho mọi client**     |

---

## 9. LƯU Ý KHI LÀM BÀI THI

| Lưu ý                            | Chi tiết                                                                                  |
| ---------------------------------- | ------------------------------------------------------------------------------------------ |
| `@RestController`                | PHẢI có, nếu dùng `@Controller` thì phải thêm `@ResponseBody` trên mỗi method |
| `@GetMapping` / `@PostMapping` | GET cho lấy dữ liệu đơn giản, POST cho gửi dữ liệu phức tạp (JSON body)         |
| `@RequestParam`                  | Nhận tham số từ `?key=value` trên URL                                                |
| `@PathVariable`                  | Nhận tham số từ `/path/{value}` trên URL                                             |
| `@RequestBody`                   | Nhận JSON object từ body (chỉ dùng với POST/PUT)                                      |
| Port                               | Mặc định `8080`, đổi trong `application.properties`: `server.port=9090`         |
| JSON tự động                    | Spring Boot tự chuyển Object → JSON khi trả về,**KHÔNG CẦN** gọi thủ công  |
| Getter/Setter                      | Model class**BẮT BUỘC** có getter/setter để Spring serialize sang JSON          |
| Dependency                         | Chỉ cần `spring-boot-starter-web` là đủ cho REST API                                |
