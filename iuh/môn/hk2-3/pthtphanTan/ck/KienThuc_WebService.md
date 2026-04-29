# KIẾN THỨC WEB SERVICE - ÔN THI CUỐI KỲ

---

## 1. KHÁI NIỆM WEB SERVICE

**Web Service** là một hệ thống phần mềm được thiết kế để hỗ trợ giao tiếp giữa các máy tính (machine-to-machine) qua mạng Internet.

- Web Service cho phép các ứng dụng viết bằng **các ngôn ngữ khác nhau**, chạy trên **các nền tảng khác nhau** có thể giao tiếp với nhau.
- Giao tiếp thông qua các **giao thức chuẩn** (HTTP, SOAP, REST).
- Web Service là nền tảng của kiến trúc **SOA (Service-Oriented Architecture)**.

---

## 2. CÁC LOẠI WEB SERVICE

### 2.1 SOAP Web Service (Simple Object Access Protocol)

| Đặc điểm | Chi tiết |
|---|---|
| Giao thức | SOAP (dựa trên XML) |
| Định dạng thông điệp | XML |
| Mô tả dịch vụ | WSDL (Web Service Description Language) |
| Đăng ký/Tra cứu | UDDI (Universal Description, Discovery and Integration) |
| Vận chuyển | HTTP, SMTP, TCP... |
| Ưu điểm | Chuẩn hóa cao, bảo mật tốt, hỗ trợ giao dịch phức tạp |
| Nhược điểm | Nặng nề, XML verbose, chậm hơn REST |

### 2.2 RESTful Web Service (Representational State Transfer)

| Đặc điểm | Chi tiết |
|---|---|
| Giao thức | HTTP thuần (GET, POST, PUT, DELETE) |
| Định dạng dữ liệu | JSON (phổ biến) hoặc XML |
| Kiến trúc | Stateless (không lưu trạng thái) |
| Ưu điểm | Nhẹ, nhanh, dễ phát triển, phổ biến |
| Nhược điểm | Ít chuẩn hóa hơn SOAP, bảo mật tùy triển khai |

---

## 3. KIẾN TRÚC WEB SERVICE

### 3.1 Kiến trúc SOAP Web Service

```
┌──────────────┐         ┌───────────────┐         ┌──────────────┐
│  Service     │ Publish  │    UDDI       │  Find    │  Service     │
│  Provider    │ ──────►  │  Registry     │ ◄──────  │  Requestor   │
│  (Server)    │         │  (Danh bạ)    │         │  (Client)    │
└──────┬───────┘         └───────────────┘         └──────┬───────┘
       │                                                   │
       │              Bind (Kết nối & Gọi)                 │
       └───────────────────────────────────────────────────┘
                    SOAP Messages (XML qua HTTP)
```

**3 vai trò chính:**
1. **Service Provider (Nhà cung cấp):** Tạo và triển khai Web Service, đăng ký vào UDDI.
2. **Service Registry (Bộ đăng ký):** Danh bạ trung tâm. Provider đăng ký dịch vụ, Requestor tra cứu.
3. **Service Requestor (Người yêu cầu):** Tra cứu UDDI, tìm dịch vụ cần, kết nối và gọi.

**3 thao tác chính:**
1. **Publish (Đăng ký):** Provider đăng ký dịch vụ vào Registry.
2. **Find (Tìm kiếm):** Requestor tìm dịch vụ trong Registry.
3. **Bind (Kết nối):** Requestor kết nối trực tiếp với Provider để gọi dịch vụ.

### 3.2 Các thành phần kỹ thuật SOAP

| Thành phần | Vai trò |
|---|---|
| **SOAP** | Giao thức truyền thông điệp dạng XML giữa Client và Server qua HTTP |
| **WSDL** | File XML mô tả dịch vụ: có những phương thức nào, tham số gì, kiểu dữ liệu gì, endpoint ở đâu |
| **UDDI** | Dịch vụ danh bạ toàn cầu để đăng ký và tìm kiếm Web Service |
| **XML** | Định dạng dữ liệu chuẩn cho thông điệp SOAP và WSDL |

---

## 4. SO SÁNH SOAP vs REST

| Tiêu chí | SOAP | REST |
|---|---|---|
| Giao thức | SOAP (giao thức riêng) | HTTP thuần |
| Định dạng | Chỉ XML | JSON, XML, Text... |
| Tốc độ | Chậm hơn (XML nặng) | Nhanh hơn (JSON nhẹ) |
| Độ phức tạp | Cao | Thấp |
| Mô tả dịch vụ | WSDL (bắt buộc) | Không bắt buộc (có Swagger/OpenAPI) |
| Trạng thái | Có thể Stateful | Stateless |
| Bảo mật | WS-Security (mạnh) | HTTPS + OAuth (linh hoạt) |
| Phù hợp | Enterprise, ngân hàng, bảo hiểm | Web app, mobile app, microservice |

---

## 5. SO SÁNH WEB SERVICE vs RMI

| Tiêu chí | Web Service | RMI |
|---|---|---|
| Ngôn ngữ | Đa ngôn ngữ (Java, C#, Python...) | Chỉ Java ↔ Java |
| Giao thức | HTTP/SOAP/REST | TCP (JRMP) |
| Định dạng | XML/JSON (text) | Serialized Java Objects (binary) |
| Interoperability | Rất cao (đa nền tảng) | Chỉ JVM |
| Hiệu năng | Chậm hơn (overhead HTTP/XML) | Nhanh hơn (binary trực tiếp) |
| Tường lửa | Dễ vượt (dùng port 80/443) | Khó vượt (port tùy chỉnh) |
| Sử dụng | Hệ thống mở, tích hợp đa hệ thống | Hệ thống Java nội bộ |

---

## 6. JAX-WS: JAVA API FOR XML WEB SERVICES (SOAP)

JAX-WS là API chuẩn của Java để xây dựng và sử dụng SOAP Web Service.

### 6.1 Tạo Web Service (Server)

```java
import javax.jws.WebService;
import javax.jws.WebMethod;
import javax.xml.ws.Endpoint;

@WebService  // Đánh dấu đây là Web Service
public class CalculatorService {

    @WebMethod  // Đánh dấu đây là phương thức được expose ra ngoài
    public int cong(int a, int b) {
        return a + b;
    }

    @WebMethod
    public int tru(int a, int b) {
        return a - b;
    }

    @WebMethod
    public int nhan(int a, int b) {
        return a * b;
    }

    @WebMethod
    public double chia(int a, int b) {
        if (b == 0) throw new ArithmeticException("Khong the chia cho 0");
        return (double) a / b;
    }

    @WebMethod
    public boolean kiemTraNguyenTo(int n) {
        if (n <= 1) return false;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) return false;
        }
        return true;
    }

    @WebMethod
    public long tinhGiaiThua(int n) {
        long result = 1;
        for (int i = 2; i <= n; i++) result *= i;
        return result;
    }

    @WebMethod
    public String daoChuoi(String text) {
        return new StringBuilder(text).reverse().toString();
    }

    @WebMethod
    public String sapXepTangDan(String numbers) {
        String[] parts = numbers.trim().split("[,\\s]+");
        java.util.List<Double> list = new java.util.ArrayList<>();
        for (String s : parts) list.add(Double.parseDouble(s.trim()));
        java.util.Collections.sort(list);
        return list.toString();
    }

    // MAIN: Khởi động Web Service
    public static void main(String[] args) {
        String url = "http://localhost:8080/calculator";
        Endpoint.publish(url, new CalculatorService());
        System.out.println("Web Service dang chay tai: " + url);
        System.out.println("WSDL tai: " + url + "?wsdl");
    }
}
```

**Giải thích:**
- `@WebService`: Đánh dấu class là 1 Web Service.
- `@WebMethod`: Đánh dấu phương thức được công bố (expose) cho client gọi.
- `Endpoint.publish(url, obj)`: Triển khai Web Service tại URL chỉ định.
- Sau khi chạy, truy cập `http://localhost:8080/calculator?wsdl` để xem mô tả WSDL.

### 6.2 Tạo Client gọi Web Service

**Cách 1: Dùng wsimport (tự sinh code từ WSDL)**
```bash
wsimport -s src -p com.client http://localhost:8080/calculator?wsdl
```
Lệnh này tự động sinh ra các class Stub để client gọi:

```java
// Client tự sinh từ wsimport
public class WebServiceClient {
    public static void main(String[] args) {
        // Class CalculatorServiceService và CalculatorService được sinh ra bởi wsimport
        CalculatorServiceService service = new CalculatorServiceService();
        CalculatorService calc = service.getCalculatorServicePort();

        // Gọi phương thức từ xa
        System.out.println("3 + 5 = " + calc.cong(3, 5));
        System.out.println("10 / 3 = " + calc.chia(10, 3));
        System.out.println("17 la so nguyen to: " + calc.kiemTraNguyenTo(17));
    }
}
```

**Cách 2: Gọi trực tiếp bằng URL (không cần wsimport)**
```java
import javax.xml.namespace.QName;
import javax.xml.ws.Service;
import java.net.URL;

public class DirectClient {
    public static void main(String[] args) throws Exception {
        // 1. Đường dẫn WSDL
        URL wsdlUrl = new URL("http://localhost:8080/calculator?wsdl");

        // 2. QName xác định dịch vụ (namespace + tên service trong WSDL)
        QName qname = new QName("http://yourpackage/", "CalculatorServiceService");

        // 3. Tạo Service proxy
        Service service = Service.create(wsdlUrl, qname);

        // 4. Lấy port (tương tự như Stub)
        // CalculatorService ở đây là Interface mà bạn tự tạo khớp với server
        // hoặc dùng class được sinh ra từ wsimport
        CalculatorService calc = service.getPort(CalculatorService.class);

        // 5. Gọi phương thức
        System.out.println("Ket qua: " + calc.cong(10, 20));
    }
}
```

---

## 7. CẤU TRÚC THÔNG ĐIỆP SOAP

```xml
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">

    <!-- Header: Thông tin bổ sung (bảo mật, routing...) - TÙY CHỌN -->
    <soap:Header>
        <auth:token>abc123</auth:token>
    </soap:Header>

    <!-- Body: Nội dung chính (request hoặc response) - BẮT BUỘC -->
    <soap:Body>
        <cal:cong>
            <a>10</a>
            <b>20</b>
        </cal:cong>
    </soap:Body>

</soap:Envelope>
```

| Phần | Bắt buộc | Vai trò |
|---|---|---|
| **Envelope** | Có | Phần tử gốc, bao bọc toàn bộ thông điệp |
| **Header** | Không | Chứa thông tin phụ: xác thực, routing, transaction |
| **Body** | Có | Chứa nội dung chính: tên method, tham số, kết quả |
| **Fault** | Không | Nằm trong Body, chứa thông tin lỗi khi xử lý thất bại |

---

## 8. WSDL (Web Service Description Language)

WSDL là file XML mô tả chi tiết Web Service, gồm các phần:

| Phần tử WSDL | Mô tả |
|---|---|
| `<types>` | Định nghĩa kiểu dữ liệu (dùng XML Schema) |
| `<message>` | Mô tả thông điệp vào/ra cho mỗi operation |
| `<portType>` | Nhóm các operation (tương tự Interface trong Java) |
| `<binding>` | Xác định giao thức và định dạng dữ liệu cụ thể (SOAP/HTTP) |
| `<service>` | Xác định endpoint (URL) để gọi dịch vụ |

---

## 9. LƯU Ý KHI LÀM BÀI THI WEB SERVICE

| Lưu ý | Chi tiết |
|---|---|
| Annotation | `@WebService` trên class, `@WebMethod` trên phương thức. Thiếu là không expose được. |
| Endpoint | `Endpoint.publish(url, obj)` để triển khai. URL phải đúng format `http://host:port/path`. |
| WSDL | Sau khi Server chạy, truy cập `url?wsdl` để xem mô tả dịch vụ. |
| Thứ tự chạy | **Server trước → Client sau** (giống RMI). |
| Lỗi thường gặp | Sai URL, sai QName namespace, Server chưa chạy. |
| So với RMI | Web Service dùng HTTP/XML (đa ngôn ngữ) - RMI dùng TCP/Binary (chỉ Java). |

---

## 10. BẢNG TỔNG HỢP SO SÁNH 3 CÔNG NGHỆ PHÂN TÁN

| Tiêu chí | Socket | RMI | Web Service |
|---|---|---|---|
| Mức trừu tượng | Thấp | Trung bình | Cao |
| Ngôn ngữ | Đa ngôn ngữ | Chỉ Java | Đa ngôn ngữ |
| Giao thức | TCP/UDP | JRMP (TCP) | HTTP/SOAP/REST |
| Định dạng dữ liệu | Byte/Text | Java Object | XML/JSON |
| Tính tương tác | Tùy triển khai | Chỉ JVM | Rất cao (chuẩn mở) |
| Firewall | Khó (port tùy ý) | Khó | Dễ (port 80/443) |
| Độ phức tạp cài đặt | Cao | Trung bình | Thấp (có công cụ hỗ trợ) |
| Hiệu năng | Nhanh nhất | Nhanh | Chậm nhất |
| Phù hợp | Game, chat, file transfer | Hệ thống Java nội bộ | Tích hợp đa hệ thống |
