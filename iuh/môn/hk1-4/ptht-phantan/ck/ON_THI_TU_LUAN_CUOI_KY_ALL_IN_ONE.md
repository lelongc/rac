# TÀI LIỆU ÔN THI TỰ LUẬN CUỐI KỲ: HỆ THỐNG PHÂN TÁN & WEB SERVICE JAVA (ALL-IN-ONE)
## MÔN: PHÁT TRIỂN HỆ THỐNG PHÂN TÁN (DISTRIBUTED SYSTEMS) - IUH
**Họ tên SV: Lê Thành Long | MSSV: 23630851**  
*(Tài liệu chuẩn hóa in giấy mang vào phòng thi - Bao quát 100% nội dung ôn tập: Lý thuyết Hệ thống phân tán Chương 1 + Lý thuyết Web Service Java toàn tập + Khung Code chuẩn chép mọi bài thực hành b7, b8, TK2 + Bộ 15 câu hỏi tự luận chuẩn barem điểm 10)*

---

# MỤC LỤC TỔNG QUAN

- [PHẦN 1: LÝ THUYẾT HỆ THỐNG PHÂN TÁN (CHƯƠNG 1)](#phần-1-lý-thuyết-hệ-thống-phân-tán-chương-1)
  * [1.1. Định nghĩa Hệ thống phân tán (Tanenbaum & Coulouris)](#11-định-nghĩa-hệ-thống-phân-tán)
  * [1.2. 3 Đặc tính bất biến cốt lõi (Concurrency, Independent Failure, Lack of Global Clock)](#12-3-đặc-tính-bất-biến-cốt-lõi)
  * [1.3. Ứng dụng thực tế & Nền tảng chia sẻ tài nguyên Web](#13-ứng-dụng-thực-tế--nền-tảng-chia-sẻ-tài-nguyên-web)
  * [1.4. 8 Thách thức lớn khi xây dựng HT phân tán & Giải pháp kỹ thuật](#14-8-thách-thức-lớn-khi-xây-dựng-hệ-thống-phân-tán)
  * [1.5. 8 Dạng trong suốt (Transparencies - ISO/ODP)](#15-8-dạng-trong-suốt-transparencies)
  * [1.6. Các mô hình kiến trúc phân tán (Client-Server, P2P, Middleware)](#16-các-mô-hình-kiến-trúc-phân-tán)
  * [1.7. 8 Giả định sai lầm kinh điển về tính toán phân tán (The 8 Fallacies)](#17-8-sai-lầm-kinh-điển-về-tính-toán-phân-tán)
  * [1.8. Đa luồng (Multi-threading) trong HT phân tán & 3 cách tạo luồng Java](#18-đa-luồng-multi-threading-trong-hệ-thống-phân-tán)
  * [1.9. Mở rộng chiều dọc (Scale Up) vs Chiều ngang (Scale Out)](#19-mở-rộng-chiều-dọc-scale-up-vs-chiều-ngang-scale-out)
- [PHẦN 2: LÝ THUYẾT WEB SERVICE JAVA TOÀN TẬP (CHƯƠNG CUỐI)](#phần-2-lý-thuyết-web-service-java-toàn-tập)
  * [2.1. Web Service là gì? Mô hình kiến trúc SOA (3 Thực thể & 3 Thao tác)](#21-web-service-là-gì-mô-hình-kiến-trúc-soa)
  * [2.2. Tổng hợp dịch vụ (Service Composition - Travel Agent Service)](#22-tổng-hợp-dịch-vụ-service-composition)
  * [2.3. Giao thức SOAP (Cấu trúc Envelope, Header, Body, Fault & Ràng buộc HTTP POST)](#23-giao-thức-soap)
  * [2.4. Ngôn ngữ mô tả WSDL (5 thành phần chính & 6 mô hình trao đổi MEP)](#24-ngôn-ngữ-mô-tả-wsdl)
  * [2.5. Thư mục dịch vụ UDDI (4 cấu trúc dữ liệu chính)](#25-thư-mục-dịch-vụ-uddi)
  * [2.6. Bảo mật Web Services (XML Signature & XML Encryption)](#26-bảo-mật-web-services-xml-security)
  * [2.7. Bảng so sánh toàn diện 10 tiêu chí: SOAP vs RESTful](#27-bảng-so-sánh-toàn-diện-10-tiêu-chí-soap-vs-restful)
  * [2.8. 6 Nguyên tắc ràng buộc kiến trúc REST (Roy Fielding) & Vai trò của Stateless](#28-6-nguyên-tắc-ràng-buộc-kiến-trúc-rest)
  * [2.9. Bảng ánh xạ CRUD <-> HTTP Methods & Tính Safe / Idempotent](#29-bảng-ánh-xạ-crud---http-methods)
  * [2.10. Bảng mã trạng thái phản hồi chuẩn (HTTP Status Codes)](#210-bảng-mã-trạng-thái-phản-hồi-chuẩn-http-status-codes)
  * [2.11. Kiến trúc Spring Boot MVC, Bean, IoC, DI, @Controller vs @RestController](#211-kiến-trúc-spring-boot-mvc)
  * [2.12. Bảng tổng hợp ý nghĩa các Annotation Spring Web quan trọng nhất](#212-bảng-tổng-hợp-ý-nghĩa-các-annotation-spring-web)
  * [2.13. Dạng câu hỏi kinh điển: "Cần bổ sung gì để trở thành Web Service?"](#213-dạng-câu-hỏi-kinh-điển-cần-bổ-sung-gì-để-trở-thành-web-service)
  * [2.14. Đóng gói Docker & Kiểm thử API (cURL vs Postman vs MockMvc)](#214-đóng-gói-docker--kiểm-thử-api)
- [PHẦN 3: KHUNG CODE CHUẨN ĐA NĂNG (CHÉP MỌI ĐỀ THI TỪ B7, B8, TK2)](#phần-3-khung-code-chuẩn-đa-năng-chép-mọi-đề-thi)
  * [3.1. Bảng tra cứu hoán đổi Entity (Product, Student, Employee, Book, Order)](#31-bảng-tra-cứu-hoán-đổi-entity)
  * [3.2. KHUNG 1: Dạng Tối Giản 2 Lớp (Model + Controller) - Chuẩn bài b7 & TK2](#32-khung-1-dạng-tối-giản-2-lớp-chuẩn-b7--tk2)
  * [3.3. KHUNG 2: Dạng Chuẩn Doanh Nghiệp 3 Tầng + Exception Handler - Chuẩn bài b8](#33-khung-2-dạng-chuẩn-doanh-nghiệp-3-tầng--exception-chuẩn-b8)
  * [3.4. KHUNG 3: Cấu hình Maven (pom.xml), Properties & Main Application](#34-khung-3-cấu-hình-maven-properties--main-application)
  * [3.5. KHUNG 4: Đóng gói Dockerfile & docker-compose.yml](#35-khung-4-đóng-gói-dockerfile--docker-composeyml)
  * [3.6. KHUNG 5: Bộ lệnh cURL kiểm thử toàn bộ Endpoint](#36-khung-5-bộ-lệnh-curl-kiểm-thử-toàn-bộ-endpoint)
- [PHẦN 4: BỘ 15 CÂU HỎI VÀ ĐÁP ÁN TỰ LUẬN TỔNG HỢP (ĐIỂM 10)](#phần-4-bộ-15-câu-hỏi-và-đáp-án-tự-luận-tổng-hợp)

---

# PHẦN 1: LÝ THUYẾT HỆ THỐNG PHÂN TÁN (CHƯƠNG 1)

## 1.1. Định nghĩa Hệ thống phân tán
* **Định nghĩa của Andrew S. Tanenbaum**: Hệ thống phân tán là một tập hợp các máy tính độc lập (autonomous computers) xuất hiện đối với người dùng như một **hệ thống đơn nhất** (single coherent system).
* **Định nghĩa của George Coulouris**: Là hệ thống trong đó các thành phần phần cứng hoặc phần mềm đặt tại các máy tính kết nối mạng truyền thông và phối hợp các hành động của chúng **chỉ bằng cách truyền thông điệp (message passing)**.
* **Mục tiêu chính**: Chia sẻ tài nguyên (Resource Sharing) - bao gồm phần cứng, phần mềm, dữ liệu - một cách kinh tế, an toàn, tin cậy và hiệu quả cao.

---

## 1.2. 3 Đặc tính bất biến cốt lõi (Core Characteristics)
Mọi hệ thống phân tán đều phải đối mặt với 3 đặc tính bất biến sau:
1. **Tính song song / Đồng thời (Concurrency)**:
   - Các tiến trình/chương trình chạy đồng thời trên nhiều máy tính khác nhau.
   - Nhiều tác vụ cùng thao tác chia sẻ tài nguyên chung (dữ liệu, CPU, bộ nhớ) mà không được gây xung đột, race condition hay mất nhất quán dữ liệu.
2. **Lỗi độc lập của các thành phần (Independent Failure of Components)**:
   - Một máy tính, tiến trình hoặc đường truyền mạng có thể bị lỗi, sập (crash) mà không làm sụp đổ toàn bộ hệ thống.
   - Các nút khác vẫn tiếp tục hoạt động bình thường; hệ thống phải có cơ chế chịu lỗi (fault tolerance), phát hiện và cô lập sự cố.
3. **Không có đồng hồ toàn cục (Lack of a Global Clock)**:
   - Không tồn tại một chiếc đồng hồ chuẩn duy nhất chung cho toàn hệ thống để xác định thời gian tuyệt đối chính xác giữa các sự kiện xảy ra ở các máy khác nhau (do Clock Drift của thạch anh phần cứng và độ trễ ngẫu nhiên của đường truyền).
   - Sự đồng bộ hóa và thứ tự các sự kiện chỉ có thể dựa trên việc trao đổi thông điệp (Logical Clock / Lamport Timestamps).

---

## 1.3. Ứng dụng thực tế & Nền tảng chia sẻ tài nguyên Web

### 1. Bảng ứng dụng thực tế:
| Lĩnh vực | Ứng dụng tiêu biểu |
| :--- | :--- |
| **Tài chính & Thương mại** | Thương mại điện tử (Amazon, Shopee), Ngân hàng trực tuyến (Internet Banking), Giao dịch chứng khoán. |
| **Mạng xã hội & Tìm kiếm** | Công cụ tìm kiếm Web (Google), Wikipedia, Mạng xã hội (Facebook, TikTok). |
| **Giải trí đa phương tiện** | Game online nhiều người chơi (MMORPG), Streaming video/nhạc (YouTube, Netflix, Spotify). |
| **Y tế (Healthcare)** | Hồ sơ bệnh án điện tử trực tuyến, Hệ thống chẩn đoán và giám sát bệnh nhân từ xa. |
| **Giáo dục** | Hệ thống E-learning, Môi trường học tập ảo (VLE), Quản lý đào tạo tín chỉ trực tuyến. |
| **Vận tải & Định vị** | Hệ thống định vị vệ tinh GPS, Dịch vụ bản đồ số (Google Maps), Ứng dụng đặt xe công nghệ (Grab). |
| **Khoa học & Kỹ thuật** | Điện toán lưới (Grid Computing), Tính toán cụm hiệu năng cao (HPC) mô phỏng khí hậu. |
| **Môi trường & IoT** | Mạng cảm biến không dây (Sensor Networks) cảnh báo sớm động đất, lũ lụt, sóng thần. |

### 2. Các ví dụ về kiến trúc hệ thống phân tán:
1. **Internet & Intranet**: Mạng toàn cầu kết nối hàng tỷ thiết bị thông qua bộ giao thức TCP/IP.
2. **Điện toán di động & phổ biến (Mobile & Ubiquitous Computing)**: Smartphone, thiết bị IoT đeo thông minh kết nối qua 4G/5G, Wi-Fi, Bluetooth.
3. **Điện toán đám mây (Cloud Computing)**: Cung cấp tài nguyên tính toán (IaaS), nền tảng (PaaS), phần mềm (SaaS) qua Internet (AWS, Azure, GCP).
4. **World Wide Web & Web Services**: Nền tảng chia sẻ tài nguyên toàn cầu dựa trên chuẩn URL (`http://host[:port][/path][?query]`), giao thức truyền tin HTTP (Request-Reply), trình duyệt Web và các Web Service REST/SOAP.

---

## 1.4. 8 Thách thức lớn khi xây dựng Hệ thống phân tán

| STT | Thách thức | Nội dung chi tiết | Giải pháp kỹ thuật |
| :---: | :--- | :--- | :--- |
| **1** | **Heterogeneity**<br>*(Tính không đồng nhất)* | Khác biệt về mạng, phần cứng, hệ điều hành (Windows, Linux, macOS), ngôn ngữ lập trình (Java, C#, Python), định dạng dữ liệu (Big-Endian vs Little-Endian). | Sử dụng **Middleware** (RMI, Web Services) và định dạng dữ liệu trung gian chuẩn hóa (**JSON, XML**). |
| **2** | **Openness**<br>*(Tính mở)* | Khả năng mở rộng, tích hợp thêm các dịch vụ, phần cứng, phần mềm mới mà không phá vỡ hệ thống sẵn có. | Xuất bản các giao diện chuẩn (Standard APIs / WSDL / OpenAPI), đảm bảo tính tương tác (Interoperability) và khả chuyển (Portability). |
| **3** | **Security Enforcement**<br>*(An ninh & Bảo mật)* | Bảo vệ tài nguyên chống truy cập trái phép, nghe lén, giả mạo dữ liệu khi truyền trên mạng công cộng. | Ba trụ cột CIA: **Confidentiality** (Mã hóa SSL/TLS, AES), **Integrity** (Chữ ký số, SHA-256), **Availability** (Chống DDoS) + Xác thực & Phân quyền (JWT, OAuth2). |
| **4** | **Scalability**<br>*(Khả năng mở rộng)* | Hệ thống vẫn duy trì hiệu năng tốt khi số lượng người dùng và tài nguyên tăng lên hàng triệu node. | Mở rộng theo chiều ngang (**Scale Out**), Caching (Redis), Phân vùng dữ liệu (Sharding/Partitioning), tránh cổ chai tập trung. |
| **5** | **Failure Handling**<br>*(Xử lý lỗi)* | Lỗi là điều tất yếu xảy ra trong môi trường phân tán (đứt cáp, máy chủ sập, timeout). | 5 cơ chế: Phát hiện lỗi (Heartbeat/Ping), Che giấu lỗi (Retry), Chịu lỗi (Fault Tolerance), Phục hồi (Recovery/Log), Dư thừa (Redundancy). |
| **6** | **Concurrency Management**<br>*(Quản lý đồng thời)* | Nhiều người dùng đồng thời đọc/ghi vào cùng một tài nguyên chia sẻ. | Đồng bộ hóa (Synchronization), khóa (Locks), loại trừ tương hỗ (Mutual Exclusion), xử lý giao dịch phân tán tuân thủ tính chất ACID. |
| **7** | **Transparency**<br>*(Tính trong suốt)* | Che giấu sự phân tán về mặt vật lý, logic đối với người dùng và lập trình viên. | Cung cấp giao diện trừu tượng để lập trình viên tương tác như gọi hàm nội bộ cục bộ (Local Call). |
| **8** | **Quality of Service (QoS)**<br>*(Chất lượng dịch vụ)* | Đảm bảo các chỉ số kỹ thuật về độ tin cậy (Reliability), thời gian đáp ứng (Latency), thông lượng (Throughput). | Cấp phát tài nguyên động, dự phòng băng thông, giới hạn tải (Rate Limiting), cân bằng tải (Load Balancing). |

---

## 1.5. 8 Dạng trong suốt (Transparencies - ISO/ODP)

Tính trong suốt là mục tiêu tối thượng giúp người dùng và lập trình viên nhìn nhận hệ thống phân tán như một hệ máy đơn nhất.

| Dạng trong suốt | Tên tiếng Anh | Ý nghĩa cốt lõi | Ví dụ minh họa thực tế |
| :---: | :--- | :--- | :--- |
| **1** | **Access transparency** | Che giấu sự khác biệt về định dạng dữ liệu và phương thức truy cập. Truy cập cục bộ hay từ xa đều dùng cùng một cú pháp. | Lệnh đọc file `read()` trên ổ cứng máy tính hay trên máy chủ mạng NFS từ xa đều dùng chung một hàm. RMI gọi hàm từ xa như hàm nội bộ. |
| **2** | **Location transparency** | Che giấu vị trí vật lý của tài nguyên. Truy cập tài nguyên bằng tên định danh duy nhất mà không cần biết máy chủ đặt ở đâu. | Truy cập `https://google.com` hoặc endpoint API `/api/products` mà không cần biết địa chỉ IP thực tế của máy chủ lưu trữ. |
| **3** | **Concurrency transparency** | Che giấu sự cạnh tranh tài nguyên giữa nhiều tiến trình đồng thời mà không làm hỏng dữ liệu. | Hai người cùng rút tiền ở 2 cây ATM khác nhau từ cùng một tài khoản ngân hàng, hệ thống khóa và trừ tiền chính xác. |
| **4** | **Replication transparency** | Che giấu việc tài nguyên được nhân bản thành nhiều bản sao tại nhiều nơi để tăng tốc độ và dự phòng sự cố. | Một video YouTube hay file ảnh CDN được copy ra 20 server toàn cầu, người xem bấm xem mà không biết mình đang tải từ bản sao nào. |
| **5** | **Failure transparency** | Che giấu lỗi phần cứng/mạng, cho phép ứng dụng tiếp tục hoàn thành nhiệm vụ dù một số thành phần bị sự cố. | Khi gửi request, nếu máy chủ chính bị chết, Load Balancer tự động định tuyến sang máy chủ dự phòng mà người dùng không nhận thấy lỗi. |
| **6** | **Mobility transparency** | Che giấu việc tài nguyên hoặc tiến trình di chuyển từ máy tính này sang máy tính khác trong khi đang hoạt động. | Người dùng dùng điện thoại di chuyển từ trạm phát Wi-Fi này sang Wi-Fi khác hoặc chuyển trạm BTS 4G/5G mà cuộc gọi không bị ngắt. |
| **7** | **Performance transparency** | Che giấu việc hệ thống tự động tái cấu trúc, thêm bớt máy tính, cân bằng tải khi lưu lượng tăng giảm đột ngột. | Hệ thống tự động phân phối tải CPU, thêm server ảo (Auto-scaling) khi có đợt Flash Sale mà người dùng không cảm nhận thấy độ trễ tăng. |
| **8** | **Scaling transparency** | Cho phép hệ thống mở rộng quy mô (thêm người dùng, dữ liệu, thiết bị) mà không cần thay đổi kiến trúc hoặc thuật toán ứng dụng. | Mạng Internet mở rộng từ vài nghìn máy lên hàng tỷ thiết bị mà giao thức DNS và TCP/IP vẫn giữ nguyên nguyên lý hoạt động. |

---

## 1.6. Các mô hình kiến trúc phân tán

### 1. Mô hình Client - Server:
* Phân chia vai trò rõ ràng giữa nút yêu cầu dịch vụ (**Client**) và nút cung cấp dịch vụ (**Server**).
* **Phân cấp tầng**:
  - **2-Tier (2 tầng)**: Client (Giao diện + Xử lý) kết nối trực tiếp đến Database Server. Dễ xây dựng nhưng khó mở rộng, kém bảo mật.
  - **3-Tier (3 tầng)**: 
    * *Tầng 1 - Presentation*: Giao diện người dùng (Browser, Mobile App).
    * *Tầng 2 - Application / Business Logic*: Máy chủ xử lý logic nghiệp vụ (Spring Boot, Node.js).
    * *Tầng 3 - Data Storage*: Cơ sở dữ liệu (MySQL, MongoDB, Oracle).
  - **Multi-tier / Microservices**: Bổ sung thêm API Gateway, Load Balancer, Cache Redis, Message Queue.

### 2. Mô hình Ngang hàng (Peer-to-Peer - P2P):
* Mọi nút trong mạng (**Peers**) đều bình đẳng, vừa đóng vai trò là Client (tiêu thụ tài nguyên), vừa là Server (cung cấp tài nguyên).
* **Ưu điểm**: Khả năng mở rộng cực cao, không có điểm lỗi đơn lẻ (No Single Point of Failure).
* **Ứng dụng**: BitTorrent, Mạng phân tán Blockchain (Bitcoin, Ethereum).

### 3. Khái niệm Middleware (Phần mềm trung gian):
* **Định nghĩa**: Lớp phần mềm nằm giữa Hệ điều hành / Mạng phần cứng bên dưới và Ứng dụng phân tán bên trên.
* **Vai trò**: Che giấu tính không đồng nhất (Heterogeneity), cung cấp giao diện lập trình cấp cao và các giao thức gọi hàm từ xa (RPC, RMI) hoặc dịch vụ Web (SOAP, RESTful).

---

## 1.7. 8 Sai lầm kinh điển về tính toán phân tán (The 8 Fallacies - L. Peter Deutsch)

Khi lập trình viên chuyển từ ứng dụng đơn khối (Monolith) sang phân tán, họ thường mắc 8 giả định sai lầm sau:
1. **The network is reliable** *(Mạng luôn đáng tin cậy)*: Sai, dây cáp có thể đứt, wifi mất tín hiệu, gói tin bị rơi.
2. **Latency is zero** *(Độ trễ truyền mạng bằng 0)*: Sai, gọi hàm nội bộ mất nano-giây, gọi qua mạng mất từ vài mili-giây đến vài giây.
3. **Bandwidth is infinite** *(Băng thông là vô hạn)*: Sai, đường truyền mạng có giới hạn tải, dữ liệu lớn gây tắc nghẽn.
4. **The network is secure** *(Mạng là tuyệt đối an toàn)*: Sai, đường truyền mạng luôn có nguy cơ bị nghe lén, MITM, chèn mã độc.
5. **Topology doesn't change** *(Cấu trúc mạng không bao giờ đổi)*: Sai, router có thể khởi động lại, IP đổi động, máy tính thêm bớt liên tục.
6. **There is one administrator** *(Chỉ có một người quản trị duy nhất)*: Sai, mỗi hệ thống do các tổ chức/công ty khác nhau quản lý cấu hình khác nhau.
7. **Transport cost is zero** *(Chi phí vận chuyển dữ liệu bằng 0)*: Sai, chi phí phần cứng mạng, băng thông đám mây, CPU đóng/mở gói serialization đều tốn kém.
8. **The network is homogeneous** *(Mạng là đồng nhất về chủng loại)*: Sai, mạng gồm vô vàn thiết bị khác nhau của Cisco, TP-Link, hệ điều hành Android, iOS, Linux, Windows.

---

## 1.8. Đa luồng (Multi-threading) trong Hệ thống phân tán

### 1. Tại sao Server phân tán bắt buộc phải dùng Multi-threading?
- **Tránh nghẽn (Non-blocking)**: Nếu server đơn luồng (Single-thread), khi đang phục vụ Client 1 (hoặc đợi I/O đọc ổ cứng/CSDL), tất cả Client khác sẽ bị treo cứng.
- **Tận dụng tối đa phần cứng**: CPU hiện đại có nhiều nhân (Multi-core), đa luồng giúp chạy song song trên các core.
- **Tăng thông lượng (Throughput)**: Phục vụ hàng nghìn request/giây cùng lúc.

### 2. 3 Cách tạo luồng trong Java:
1. **Kế thừa lớp `Thread`**:
   - `class MyThread extends Thread { public void run() { ... } }`
   - *Nhược điểm*: Java chỉ hỗ trợ đơn kế thừa, không kế thừa thêm class khác được.
2. **Cài đặt interface `Runnable` (Khuyên dùng)**:
   - `class MyTask implements Runnable { public void run() { ... } }`
   - *Ưu điểm*: Tách biệt logic công việc với việc quản lý luồng, kế thừa thoải mái.
3. **Cài đặt interface `Callable<T>` kết hợp `ExecutorService`**:
   - Trả về kết quả thông qua đối tượng `Future<T>`.
   - Quản lý tái sử dụng luồng bằng **Thread Pool** (`Executors.newFixedThreadPool(n)`), tránh chi phí khởi tạo luồng mới liên tục.

---

## 1.9. Mở rộng chiều dọc (Scale Up) vs Chiều ngang (Scale Out)

| Tiêu chí | Scale Up (Mở rộng theo chiều dọc) | Scale Out (Mở rộng theo chiều ngang) |
| :--- | :--- | :--- |
| **Bản chất** | Nâng cấp phần cứng của một máy chủ duy nhất (Thêm RAM, CPU nhiều nhân hơn, lắp ổ cứng NVMe). | Bổ sung thêm nhiều máy chủ giá rẻ vào cụm (Cluster) và dùng Load Balancer phân phối tải. |
| **Chi phí** | Chi phí tăng theo hàm mũ (phần cứng siêu máy chủ cực đắt). | Chi phí tối ưu, tận dụng máy chủ phổ thông hoặc thuê máy ảo đám mây linh hoạt. |
| **Giới hạn** | Có giới hạn trần vật lý của bo mạch chủ / CPU. | Khả năng mở rộng gần như vô hạn (chỉ cần thêm máy vào cụm). |
| **Độ tin cậy** | Kém: Vẫn tồn tại điểm lỗi đơn lẻ (Single Point of Failure). Máy chủ hỏng là toàn bộ hệ thống sập. | Rất cao: Chịu lỗi tốt. Nếu 1 máy chủ chết, các máy chủ khác vẫn tiếp tục gánh tải. |
| **Độ phức tạp** | Rất thấp: Ứng dụng không cần thay đổi kiến trúc mã nguồn. | Cao: Ứng dụng phải được thiết kế **Stateless (Phi trạng thái)** và cần đồng bộ CSDL. |

---

# PHẦN 2: LÝ THUYẾT WEB SERVICE JAVA TOÀN TẬP

## 2.1. Web Service là gì? Mô hình kiến trúc SOA

### 1. Định nghĩa Web Service:
* **Web Service (Dịch vụ Web)** là một thành phần phần mềm cung cấp dịch vụ thông qua mạng máy tính, cho phép các ứng dụng viết bằng các ngôn ngữ khác nhau (Java, C#, Python, JavaScript) chạy trên các hệ điều hành khác nhau (Windows, Linux, macOS) có thể giao tiếp và trao đổi dữ liệu qua các giao thức chuẩn (**HTTP**, **JSON**, **XML**).
* Bản chất: Web Service là giải pháp hiện đại thay thế cho các cơ chế RPC và Java RMI truyền thống, vượt qua được rào cản tường lửa (Firewall) vì hoạt động trực tiếp trên cổng Web tiêu chuẩn (Port 80/HTTP, 443/HTTPS, 8080).

### 2. Mô hình kiến trúc hướng dịch vụ (SOA - Service Oriented Architecture):
Mô hình SOA gồm **3 Thực thể (Roles)** và **3 Thao tác (Operations)**:

```text
                  ┌───────────────────────────────┐
                  │    Service Registry (UDDI)    │
                  └───────────────┬───────────────┘
                                ▲   │
                   1. Publish  │   │  2. Find
                               │   ▼
┌────────────────────────┐                ┌────────────────────────┐
│    Service Provider    │◄───────────────┤    Service Consumer    │
│     (Nhà cung cấp)     │    3. Bind     │     (Bên yêu cầu)      │
└────────────────────────┘                └────────────────────────┘
```

- **3 Thực thể (Roles)**:
  1. **Service Provider** (Nhà cung cấp): Xây dựng Web Service, phát hành bản mô tả dịch vụ (WSDL) và công bố lên Registry.
  2. **Service Requester / Consumer** (Bên yêu cầu): Ứng dụng client tìm kiếm dịch vụ trên Registry và gửi yêu cầu gọi dịch vụ.
  3. **Service Registry / Broker** (Nơi đăng ký): Thư mục lưu trữ danh bạ, địa chỉ và thông số kỹ thuật của các dịch vụ (ví dụ: UDDI).
- **3 Thao tác (Operations)**:
  1. **Publish** (Xuất bản): Provider đăng ký thông tin dịch vụ lên Registry.
  2. **Find** (Tìm kiếm): Consumer tra cứu Registry để tìm dịch vụ phù hợp.
  3. **Bind** (Ràng buộc / Gọi): Consumer kết nối trực tiếp đến Provider để thực thi dịch vụ.

---

## 2.2. Tổng hợp dịch vụ (Service Composition)
- **Khái niệm**: Là cơ chế kết hợp nhiều Web Service đơn lẻ, độc lập để tạo thành một quy trình nghiệp vụ phức hợp cấp cao.
- **Ví dụ kinh điển (Travel Agent Service - Đại lý du lịch)**:
  - Khi người dùng gửi yêu cầu đặt chuyến du lịch trọn gói, hệ thống tự động điều phối gọi đồng thời 3 dịch vụ Web độc lập:
    1. *Flight Booking Service*: Đặt vé máy bay.
    2. *Hotel Booking Service*: Đặt phòng khách sạn.
    3. *Car Rental Service*: Thuê xe tự lái đưa đón.
  - Kết quả được tổng hợp lại và xác nhận thành 1 giao dịch duy nhất cho khách hàng.

---

## 2.3. Giao thức SOAP (Simple Object Access Protocol)

SOAP là giao thức truyền thông dựa trên XML, dùng để đóng gói thông điệp trao đổi giữa Client và Server.

### Cấu trúc thông điệp SOAP (SOAP Envelope):
Thông điệp SOAP gồm một phần tử gốc `<env:Envelope>` chứa:
1. `<env:Header>` *(Tùy chọn)*: Chứa các thông tin tiêu đề như token xác thực, định tuyến, giao dịch phân tán.
2. `<env:Body>` *(Bắt buộc)*: Chứa nội dung chính của thông điệp yêu cầu (tên hàm, tham số) hoặc kết quả trả về, hoặc thẻ `<env:Fault>` khi xảy ra lỗi.

### Mẫu gói tin SOAP Request gửi qua HTTP POST:
```http
POST /examples/calculator HTTP/1.1
Host: www.example.com
Content-Type: application/soap+xml; charset=utf-8
SOAPAction: "http://www.example.com/calculator#add"

<env:Envelope xmlns:env="http://www.w3.org/2003/05/soap-envelope">
    <env:Header>
        <m:AuthToken xmlns:m="http://www.example.com/security">XYZ-12345</m:AuthToken>
    </env:Header>
    <env:Body>
        <m:add xmlns:m="http://www.example.com/calculator">
            <m:a>10</m:a>
            <m:b>20</m:b>
        </m:add>
    </env:Body>
</env:Envelope>
```

### Tại sao SOAP bắt buộc dùng phương thức HTTP POST?
1. **Dữ liệu XML phức tạp và có kích thước lớn**: Thẻ `<env:Envelope>` có kích thước lớn, vượt quá giới hạn độ dài của URL trong phương thức `GET`.
2. **GET không có Body chuẩn**: Phương thức `GET` theo đặc tả HTTP không mang phần thân dữ liệu (Message Body), trong khi SOAP bắt buộc phải bọc payload trong thẻ `<env:Body>`.
3. **Mục đích gọi hàm từ xa (RPC)**: SOAP gửi lệnh thực thi hàm trên máy chủ, có thể làm thay đổi trạng thái hệ thống, nên không được dùng `GET` (vốn là phương thức chỉ đọc và an toàn).

---

## 2.4. Ngôn ngữ mô tả WSDL (Web Services Description Language)

WSDL là tài liệu XML dùng để mô tả chi tiết: Dịch vụ cung cấp những thao tác nào? Tham số truyền vào là gì? Kiểu dữ liệu ra sao? Địa chỉ truy cập ở đâu?

### 5 Thành phần cốt lõi của tài liệu WSDL:
1. `<types>`: Định nghĩa các kiểu dữ liệu sử dụng trong thông điệp (dựa trên chuẩn XML Schema Definition - XSD).
2. `<message>`: Định nghĩa cấu trúc dữ liệu của các thông điệp truyền đi (Request) và nhận về (Response).
3. `<portType>`: Tập hợp các thao tác (Operations) mà dịch vụ hỗ trợ (tương đương với một Interface trong Java).
4. `<binding>`: Quy định giao thức truyền thông cụ thể và định dạng mã hóa cho từng thao tác (ví dụ: SOAP qua HTTP).
5. `<service>`: Định nghĩa địa chỉ mạng thực tế (Endpoint URL) để gọi dịch vụ (thông qua thẻ con `<port>`).

### 6 Mô hình trao đổi thông điệp (MEP - Message Exchange Patterns) trong WSDL:
1. **In-Only**: Client chỉ gửi thông điệp tới Server, không nhận phản hồi (Một chiều - One-way).
2. **Robust In-Only**: Client gửi tới Server; Server không trả dữ liệu thành công nhưng có phản hồi nếu xảy ra lỗi (Fault).
3. **In-Out**: Client gửi yêu cầu, Server bắt buộc trả lời kết quả (Mô hình Request-Response tiêu chuẩn).
4. **In-Optional-Out**: Client gửi yêu cầu; Server có thể trả về thông điệp kết quả hoặc không trả về gì.
5. **Out-Only**: Server chủ động gửi thông điệp tới Client (Notification), không cần phản hồi.
6. **Out-In**: Server chủ động gửi thông điệp tới Client và chờ nhận thông điệp phản hồi từ Client.

---

## 2.5. Thư mục dịch vụ UDDI (Universal Description, Discovery and Integration)

UDDI đóng vai trò là "Cuốn danh bạ điện thoại kỹ thuật số" cho các dịch vụ Web, gồm **4 Cấu trúc dữ liệu chính**:
1. `businessEntity`: Chứa thông tin về doanh nghiệp cung cấp dịch vụ (Tên công ty, địa chỉ, số liên lạc - Trang trắng/White Pages).
2. `businessService`: Chứa danh sách các dịch vụ mà doanh nghiệp cung cấp (Mô tả nghiệp vụ - Trang vàng/Yellow Pages).
3. `bindingTemplate`: Chứa thông tin kỹ thuật để kết nối và gọi dịch vụ, như địa chỉ URL Endpoint (Trang xanh/Green Pages).
4. `tModel` (Technical Model): Chứa bản thiết kế thông số kỹ thuật, quy định dịch vụ tuân theo giao thức hoặc WSDL nào.

---

## 2.6. Bảo mật Web Services (XML Security)

Do thông điệp XML truyền qua nhiều trung gian (Proxies, Gateways), WS-Security cung cấp bảo mật ở tầng thông điệp (Message-level security):
* **XML Signature (Chữ ký số XML)**:
  - Đảm bảo tính toàn vẹn (Integrity) và tính chống chối bỏ (Non-repudiation).
  - Cho phép ký số lên toàn bộ tài liệu hoặc chỉ ký một phần tử XML cụ thể (ví dụ: chỉ ký thẻ `<PaymentInfo>`).
* **XML Encryption (Mã hóa XML)**:
  - Đảm bảo tính bí mật (Confidentiality).
  - Cho phép mã hóa từng phần dữ liệu nhạy cảm (như thẻ tín dụng), giúp các máy chủ trung gian vẫn đọc được thông tin định tuyến ở Header mà không lộ dữ liệu bí mật.

---

## 2.7. Bảng so sánh toàn diện 10 tiêu chí: SOAP vs RESTful

| STT | Tiêu chí so sánh | SOAP (Simple Object Access Protocol) | RESTful (Representational State Transfer) |
| :---: | :--- | :--- | :--- |
| **1** | **Bản chất** | Là một **Giao thức (Protocol)** có quy chuẩn nghiêm ngặt bởi W3C. | Là một **Phong cách kiến trúc (Architectural Style)** dựa trên chuẩn HTTP. |
| **2** | **Định dạng dữ liệu** | **Chỉ dùng XML** duy nhất. | Đa dạng: **JSON** (phổ biến nhất), XML, HTML, Plain Text. |
| **3** | **Độ phức tạp / Băng thông** | Cồng kềnh, tiêu tốn nhiều băng thông do thẻ XML và Envelope lớn. | Nhẹ, xử lý nhanh, tiết kiệm băng thông tối đa. |
| **4** | **Giao thức vận chuyển** | Độc lập: Chạy trên HTTP, HTTPS, SMTP, FTP, TCP, JMS. | Gắn liền trực tiếp với **HTTP / HTTPS**. |
| **5** | **Giao diện mô tả dịch vụ** | Bắt buộc phải có tài liệu hợp đồng **WSDL**. | Không bắt buộc, thường dùng **OpenAPI / Swagger**. |
| **6** | **Cơ chế Caching** | Không hỗ trợ Caching tự nhiên vì luôn gửi qua HTTP POST. | Hỗ trợ Caching cực tốt qua HTTP Headers (`Cache-Control`, `ETag`). |
| **7** | **Bảo mật** | Hỗ trợ chuẩn doanh nghiệp cấp cao **WS-Security**, ACID Transactions. | Sử dụng **HTTPS, JWT, OAuth2, API Key**. |
| **8** | **Xử lý lỗi** | Tích hợp sẵn chuẩn thẻ `<env:Fault>` trong SOAP Body. | Dựa trực tiếp vào **HTTP Status Codes** (400, 404, 500) kèm JSON lỗi. |
| **9** | **Khả năng gọi từ Client** | Khó khăn trên trình duyệt JavaScript và Mobile do phân tích XML phức tạp. | Cực kỳ đơn giản, tối ưu cho ứng dụng Web SPA, Mobile App (React, Flutter). |
| **10** | **Trường hợp sử dụng** | Ngân hàng, Tài chính, Viễn thông, Giao dịch bảo mật cấp cao. | Mạng xã hội, Thương mại điện tử, Dịch vụ công cộng, Microservices. |

---

## 2.8. 6 Nguyên tắc ràng buộc kiến trúc REST (Roy Fielding)

Một hệ thống muốn được công nhận là **RESTful chuẩn mực** phải thỏa mãn 6 nguyên tắc ràng buộc:

1. **Client - Server (Khách - Chủ tách biệt)**:
   - Tách rời giao diện người dùng (Client) và logic lưu trữ dữ liệu (Server).
   - Client và Server có thể phát triển độc lập, viết bằng hai ngôn ngữ khác nhau mà không ảnh hưởng lẫn nhau.
2. **Stateless (Phi trạng thái - CỐT LÕI)**:
   - Server **không lưu trữ bất kỳ trạng thái phiên làm việc nào của Client (No Session State)** giữa các yêu cầu.
   - Mỗi Request từ Client gửi lên phải chứa **đầy đủ mọi thông tin cần thiết** để Server hiểu và xử lý (bao gồm dữ liệu và Token xác thực).
   - *Tầm quan trọng đối với Scale Out*: Vì Server không lưu session, Load Balancer có thể chuyển Request bất kỳ tới bất kỳ Server nào trong cụm mà không sợ mất phiên làm việc.
3. **Cacheable (Khả năng lưu bộ đệm)**:
   - Các phản hồi phải tự định nghĩa là có thể lưu đệm (cacheable) hay không để Client/Proxy tái sử dụng kết quả, giảm tải cho Server.
4. **Uniform Interface (Giao diện đồng nhất)**:
   - Là nguyên tắc quan trọng nhất phân biệt REST với các kiến trúc mạng khác:
     * Định danh tài nguyên qua URI chuẩn (ví dụ: `/api/products/1`).
     * Thao tác tài nguyên qua các phương thức HTTP chuẩn (GET, POST, PUT, DELETE).
     * Thông điệp tự mô tả (Self-descriptive messages qua `Content-Type: application/json`).
     * HATEOAS (Hypermedia As The Engine Of Application State): Trả về các liên kết hướng dẫn hành động tiếp theo.
5. **Layered System (Hệ thống phân tầng)**:
   - Client không thể biết nó đang kết nối trực tiếp đến Server cuối hay qua các tầng trung gian (Load Balancer, Proxy, API Gateway, CDN).
6. **Code on Demand (Mã theo yêu cầu - Tùy chọn)**:
   - Server có thể tạm thời mở rộng tính năng của Client bằng cách gửi mã thực thi (như JavaScript, Applet) về cho Client chạy.

---

## 2.9. Bảng ánh xạ CRUD <-> HTTP Methods

| Thao tác dữ liệu | Phương thức HTTP | Ý nghĩa chức năng | Tính Safe? | Tính Idempotent? | Status Code trả về |
| :---: | :---: | :--- | :---: | :---: | :---: |
| **Read (Đọc)** | **`GET`** | Lấy danh sách hoặc chi tiết tài nguyên. | **CÓ** | **CÓ** | `200 OK` hoặc `404 Not Found` |
| **Create (Tạo mới)** | **`POST`** | Tạo mới một tài nguyên trên hệ thống. | **KHÔNG** | **KHÔNG** | `201 Created` |
| **Update (Cập nhật)** | **`PUT`** | Thay thế/Cập nhật toàn bộ tài nguyên. | **KHÔNG** | **CÓ** | `200 OK` hoặc `204 No Content` |
| **Patch (Sửa một phần)** | **`PATCH`** | Cập nhật một vài trường thông tin. | **KHÔNG** | **KHÔNG** | `200 OK` |
| **Delete (Xóa)** | **`DELETE`** | Xóa tài nguyên khỏi hệ thống. | **KHÔNG** | **CÓ** | `200 OK` hoặc `204 No Content` |

### Khái niệm An toàn (Safe) và Bất biến (Idempotent):
- **Safe (An toàn)**: Phương thức khi gọi **không làm thay đổi trạng thái dữ liệu** trên máy chủ (chỉ đọc). `GET`, `HEAD`, `OPTIONS` là Safe.
- **Idempotent (Bất biến / Cùng kết quả)**: Thực hiện gọi phương thức đó **1 lần hay N lần liên tiếp với cùng tham số** thì trạng thái dữ liệu trên hệ thống và kết quả trả về là như nhau.
  - `GET`, `PUT`, `DELETE` là Idempotent.
  - `POST` **KHÔNG Idempotent** vì gửi 10 lần `POST` sẽ tạo ra 10 bản ghi mới khác nhau.

---

## 2.10. Bảng mã trạng thái phản hồi chuẩn (HTTP Status Codes)

| Mã Code | Tên chuẩn tiếng Anh | Ý nghĩa thực tế khi chấm bài thi |
| :---: | :--- | :--- |
| **200** | **OK** | Yêu cầu thành công. Dùng cho `GET`, `PUT`, `DELETE`. |
| **201** | **Created** | Tạo mới tài nguyên thành công. Trả về cho `POST`. |
| **204** | **No Content** | Xử lý thành công nhưng không có dữ liệu trả về (thường dùng cho `DELETE`). |
| **400** | **Bad Request** | Dữ liệu Client gửi lên sai định dạng cú pháp JSON hoặc thiếu trường bắt buộc. |
| **401** | **Unauthorized** | Chưa xác thực danh tính (thiếu Token hoặc sai mật khẩu). |
| **403** | **Forbidden** | Đã xác thực nhưng không đủ quyền hạn truy cập tài nguyên. |
| **404** | **Not Found** | Không tìm thấy ID tài nguyên được yêu cầu. |
| **405** | **Method Not Allowed** | Endpoint không hỗ trợ phương thức HTTP này (ví dụ gửi `POST` vào link chỉ nhận `GET`). |
| **500** | **Internal Server Error** | Lỗi sập mã nguồn logic phía Server (NullPointerException, lỗi CSDL). |

---

## 2.11. Kiến trúc Spring Boot MVC

```text
HTTP Request          ┌───────────────────────────┐
────────────────────► │  DispatcherServlet (Front)│
                      └─────────────┬─────────────┘
                                    │ Phân phối (Mapping)
                                    ▼
                      ┌───────────────────────────┐
                      │ @RestController           │
                      └─────────────┬─────────────┘
                                    │ Gọi nghiệp vụ (@Autowired)
                                    ▼
                      ┌───────────────────────────┐
                      │ @Service (Business Logic) │
                      └─────────────┬─────────────┘
                                    │ Truy xuất dữ liệu
                                    ▼
                      ┌───────────────────────────┐
                      │ In-Memory List / Database │
                      └───────────────────────────┘
```

### Các khái niệm cốt lõi:
1. **Spring Bean**: Là đối tượng được khởi tạo, lắp ráp, cấu hình và quản lý hoàn toàn tự động bởi Spring IoC Container.
2. **IoC (Inversion of Control - Đảo ngược điều khiển)**: Thay vì lập trình viên tự dùng từ khóa `new` để tạo đối tượng, quyền điều khiển vòng đời đối tượng được giao toàn bộ cho Spring Framework.
3. **DI (Dependency Injection - Tiêm phụ thuộc)**: Cơ chế Spring tự động đưa (bơm) các Bean phụ thuộc vào lớp cần sử dụng thông qua Annotation `@Autowired` (Field Injection hoặc Constructor Injection).
4. **So sánh `@Controller` vs `@RestController`**:
   - `@Controller`: Trả về tên file giao diện (HTML/JSP View Template) cho bộ View Resolver render.
   - `@RestController` = `@Controller` + `@ResponseBody`: Mọi giá trị trả về của các phương thức được tự động chuyển đổi thành **dữ liệu JSON/XML** và ghi trực tiếp vào HTTP Response Body.

---

## 2.12. Bảng tổng hợp ý nghĩa các Annotation Spring Web

| Annotation | Vị trí đặt | Ý nghĩa và tác dụng |
| :--- | :--- | :--- |
| `@SpringBootApplication` | Trước class `main` | Kích hoạt tự động cấu hình (Auto-configuration) và quét component (Component Scan). |
| `@RestController` | Trước Controller class | Khai báo đây là RESTful Web Controller, tự động serialize kết quả trả về sang JSON. |
| `@RequestMapping("/path")`| Trước class hoặc method | Định nghĩa đường dẫn gốc (Base URI) cho các API bên trong. |
| `@GetMapping` | Trước method | Xử lý yêu cầu HTTP GET (đọc dữ liệu). |
| `@PostMapping` | Trước method | Xử lý yêu cầu HTTP POST (thêm mới dữ liệu). |
| `@PutMapping("/{id}")` | Trước method | Xử lý yêu cầu HTTP PUT (cập nhật toàn phần). |
| `@DeleteMapping("/{id}")` | Trước method | Xử lý yêu cầu HTTP DELETE (xóa dữ liệu). |
| `@PathVariable` | Trước tham số hàm | Trích xuất biến nằm trực tiếp trên đường dẫn URL (ví dụ: `/products/{id}`). |
| `@RequestBody` | Trước tham số hàm | Giải mã chuỗi JSON từ HTTP Request Body thành đối tượng Java Model tương ứng. |
| `@RequestParam` | Trước tham số hàm | Lấy tham số truy vấn nằm sau dấu `?` trên URL (ví dụ: `/search?name=dell`). |
| `@Service` | Trước Service class | Đánh dấu tầng xử lý nghiệp vụ (Business Service), đăng ký thành Spring Bean. |
| `@Autowired` | Trước thuộc tính/hàm | Cơ chế tiêm phụ thuộc (Dependency Injection) tự động. |
| `@RestControllerAdvice` | Trước Exception class | Bắt và xử lý ngoại lệ tập trung cho toàn bộ ứng dụng REST API. |
| `@ExceptionHandler` | Trước method bắt lỗi | Chỉ định loại ngoại lệ cụ thể cần xử lý (ví dụ: `NotFoundException.class`). |
| `@ResponseStatus` | Trước method bắt lỗi | Thiết lập mã HTTP Status trả về khi xảy ra ngoại lệ (ví dụ: `HttpStatus.NOT_FOUND`). |

---

## 2.13. Dạng câu hỏi kinh điển: "Cần bổ sung gì để trở thành Web Service?"

Khi đề bài đưa một đoạn mã Java thuần (POJO/DAO) và hỏi: *"Cần bổ sung những gì để biến đoạn mã trên thành một Web Service RESTful hoàn chỉnh?"*

> **BỘ 4 BƯỚC TRẢ LỜI ĐẠT ĐIỂM TỐI ĐA**:
> 1. **Bổ sung thư viện phụ thuộc (Dependencies)**: Khai báo thư viện `spring-boot-starter-web` trong file cấu hình `pom.xml` (Maven) để tích hợp Spring MVC và nhúng sẵn máy chủ Web nhúng (Embedded Tomcat Server trên port 8080).
> 2. **Khai báo bộ điều khiển REST Controller**:
>    - Tạo lớp Controller và đánh dấu annotation `@RestController`.
>    - Gắn `@RequestMapping("/api/resources")` để định danh URI tài nguyên.
> 3. **Ánh xạ các phương thức CRUD với các HTTP Methods**:
>    - Bổ sung `@GetMapping`, `@PostMapping`, `@PutMapping`, `@DeleteMapping`.
>    - Dùng `@RequestBody` để nhận dữ liệu JSON gửi lên.
>    - Dùng `@PathVariable` để hứng ID từ URL.
> 4. **Tạo lớp khởi động ứng dụng (Main Application)**:
>    - Tạo một class chứa hàm `public static void main(String[] args)` được đánh dấu annotation `@SpringBootApplication`.
>    - Gọi hàm `SpringApplication.run(Application.class, args);` để khởi chạy máy chủ.

---

## 2.14. Đóng gói Docker & Kiểm thử API

### 1. File `Dockerfile` chuẩn cho ứng dụng Spring Boot (Cổng 8080):
```dockerfile
# Sử dụng base image Java 21 gọn nhẹ
FROM eclipse-temurin:21-jre-alpine

# Đặt thư mục làm việc bên trong container
WORKDIR /app

# Sao chép file jar sau khi đã build vào container
COPY target/*.jar app.jar

# Khai báo mở cổng mạng 8080
EXPOSE 8080

# Lệnh khởi chạy ứng dụng khi container bắt đầu chạy
ENTRYPOINT ["java", "-jar", "app.jar"]
```

### 2. Các lệnh Docker cần ghi nhớ:
* Build Image: `docker build -t product-service:1.0 .`
* Chạy Container: `docker run -d -p 8080:8080 --name my-product-app product-service:1.0`
* Xem log: `docker logs -f my-product-app`

---

# PHẦN 3: KHUNG CODE CHUẨN ĐA NĂNG (CHÉP MỌI ĐỀ THI TỪ B7, B8, TK2)

## 3.1. Bảng tra cứu hoán đổi Entity

| Đề bài yêu cầu | Tên Class Model | Các trường dữ liệu cơ bản (Fields) |
| :--- | :--- | :--- |
| **Sản phẩm (Product)** *(TK2, b8)* | `Product` | `Long id; String name; Double price;` |
| **Sinh viên (Student)** *(b7)* | `Student` | `Long id; String name; Integer age;` |
| **Nhân viên (Employee)** | `Employee`| `Long id; String name; Double salary;` |
| **Sách (Book)** | `Book` | `Long id; String title; String author;` |
| **Đơn hàng (Order)** | `Order` | `Long id; String customerName; Double totalAmount;` |

---

## 3.2. KHUNG 1: Dạng Tối Giản 2 Lớp (Model + Controller) - Chuẩn bài b7 & TK2

### 1. File Model: `Product.java`
```java
package com.example.model;

public class Product {
    private Long id;
    private String name;
    private Double price;

    public Product() {}

    public Product(Long id, String name, Double price) {
        this.id = id;
        this.name = name;
        this.price = price;
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public Double getPrice() { return price; }
    public void setPrice(Double price) { this.price = price; }
}
```

### 2. File Controller: `ProductController.java`
```java
package com.example.controller;

import com.example.model.Product;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.concurrent.CopyOnWriteArrayList;
import java.util.concurrent.atomic.AtomicLong;

@RestController
@RequestMapping("/api/products")
public class ProductController {

    // Danh sach luu trong bo nho Thread-safe
    private final List<Product> list = new CopyOnWriteArrayList<>();
    private final AtomicLong idCounter = new AtomicLong(1);

    // Constructor khoi tao du lieu mau
    public ProductController() {
        list.add(new Product(idCounter.getAndIncrement(), "Laptop Dell", 15000000.0));
        list.add(new Product(idCounter.getAndIncrement(), "Chuot Logitech", 500000.0));
    }

    // 1. GET ALL: Lay toan bo danh sach
    @GetMapping
    public ResponseEntity<List<Product>> getAll() {
        return ResponseEntity.ok(list);
    }

    // 2. GET BY ID: Lay chi tiet theo ID
    @GetMapping("/{id}")
    public ResponseEntity<Product> getById(@PathVariable Long id) {
        return list.stream()
                .filter(p -> p.getId().equals(id))
                .findFirst()
                .map(ResponseEntity::ok)
                .orElse(ResponseEntity.notFound().build());
    }

    // 3. POST: Them moi tai nguyen (Tra ve 201 Created)
    @PostMapping
    public ResponseEntity<Product> create(@RequestBody Product p) {
        if (p.getId() == null) {
            p.setId(idCounter.getAndIncrement());
        }
        list.add(p);
        return ResponseEntity.status(HttpStatus.CREATED).body(p);
    }

    // 4. PUT: Cap nhat tai nguyen theo ID
    @PutMapping("/{id}")
    public ResponseEntity<Product> update(@PathVariable Long id, @RequestBody Product newP) {
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i).getId().equals(id)) {
                newP.setId(id);
                list.set(i, newP);
                return ResponseEntity.ok(newP);
            }
        }
        return ResponseEntity.notFound().build();
    }

    // 5. DELETE: Xoa tai nguyen theo ID
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> delete(@PathVariable Long id) {
        boolean removed = list.removeIf(p -> p.getId().equals(id));
        return removed ? ResponseEntity.noContent().build() : ResponseEntity.notFound().build();
    }
}
```

---

## 3.3. KHUNG 2: Dạng Chuẩn Doanh Nghiệp 3 Tầng + Exception - Chuẩn bài b8

### 1. File Ngoại lệ: `ResourceNotFoundException.java`
```java
package com.example.exception;

import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ResponseStatus;

@ResponseStatus(HttpStatus.NOT_FOUND)
public class ResourceNotFoundException extends RuntimeException {
    public ResourceNotFoundException(String message) {
        super(message);
    }
}
```

### 2. File Xử lý ngoại lệ tập trung: `GlobalExceptionHandler.java`
```java
package com.example.exception;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

import java.time.LocalDateTime;
import java.util.HashMap;
import java.util.Map;

@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity<Map<String, Object>> handleNotFound(ResourceNotFoundException ex) {
        Map<String, Object> body = new HashMap<>();
        body.put("timestamp", LocalDateTime.now());
        body.put("status", HttpStatus.NOT_FOUND.value());
        body.put("error", "Not Found");
        body.put("message", ex.getMessage());
        return new ResponseEntity<>(body, HttpStatus.NOT_FOUND);
    }
}
```

### 3. File Tầng Dịch vụ: `ProductService.java`
```java
package com.example.service;

import com.example.exception.ResourceNotFoundException;
import com.example.model.Product;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.concurrent.CopyOnWriteArrayList;
import java.util.concurrent.atomic.AtomicLong;

@Service
public class ProductService {
    private final List<Product> list = new CopyOnWriteArrayList<>();
    private final AtomicLong idGen = new AtomicLong(1);

    public ProductService() {
        list.add(new Product(idGen.getAndIncrement(), "Ban Phim Co", 1200000.0));
    }

    public List<Product> findAll() { return list; }

    public Product findById(Long id) {
        return list.stream()
                .filter(p -> p.getId().equals(id))
                .findFirst()
                .orElseThrow(() -> new ResourceNotFoundException("Not found ID: " + id));
    }

    public Product save(Product p) {
        if (p.getId() == null) p.setId(idGen.getAndIncrement());
        list.add(p);
        return p;
    }

    public Product update(Long id, Product p) {
        Product existing = findById(id);
        existing.setName(p.getName());
        existing.setPrice(p.getPrice());
        return existing;
    }

    public void delete(Long id) {
        Product existing = findById(id);
        list.remove(existing);
    }
}
```

### 4. File Controller gọi Service: `ProductController.java`
```java
package com.example.controller;

import com.example.model.Product;
import com.example.service.ProductService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/products")
public class ProductController {

    @Autowired
    private ProductService service;

    @GetMapping
    public List<Product> getAll() { return service.findAll(); }

    @GetMapping("/{id}")
    public Product getById(@PathVariable Long id) { return service.findById(id); }

    @PostMapping
    public ResponseEntity<Product> create(@RequestBody Product p) {
        return ResponseEntity.status(HttpStatus.CREATED).body(service.save(p));
    }

    @PutMapping("/{id}")
    public Product update(@PathVariable Long id, @RequestBody Product p) {
        return service.update(id, p);
    }

    @DeleteMapping("/{id}")
    @ResponseStatus(HttpStatus.NO_CONTENT)
    public void delete(@PathVariable Long id) { service.delete(id); }
}
```

---

## 3.4. KHUNG 3: Cấu hình Maven (pom.xml), Properties & Main Application

### 1. File cấu hình: `pom.xml` (Tối giản nhất)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         https://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.2.5</version>
    </parent>

    <groupId>com.example</groupId>
    <artifactId>rest-api</artifactId>
    <version>1.0.0</version>

    <properties>
        <java.version>21</java.version>
    </properties>

    <dependencies>
        <!-- Dependency duy nhất cần thiết cho REST Web Service -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <plugin>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-maven-plugin</artifactId>
            </plugin>
        </plugins>
    </build>
</project>
```

### 2. File cấu hình: `application.properties`
```properties
server.port=8080
spring.application.name=product-service
```

### 3. File khởi động: `Application.java`
```java
package com.example;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Application {
    public static void main(String[] args) {
        SpringApplication.run(Application.class, args);
    }
}
```

---

## 3.5. KHUNG 4: Đóng gói Dockerfile & docker-compose.yml

### 1. File `Dockerfile`:
```dockerfile
FROM eclipse-temurin:21-jre-alpine
WORKDIR /app
COPY target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
```

### 2. File `docker-compose.yml`:
```yaml
version: '3.8'
services:
  web-service:
    build: .
    ports:
      - "8080:8080"
    restart: always
```

---

## 3.6. KHUNG 5: Bộ lệnh cURL kiểm thử toàn bộ Endpoint

```bash
# 1. Lay danh sach tat ca san pham
curl -X GET http://localhost:8080/api/products

# 2. Lay chi tiet san pham theo ID
curl -X GET http://localhost:8080/api/products/1

# 3. Them moi san pham (POST)
curl -X POST http://localhost:8080/api/products \
     -H "Content-Type: application/json" \
     -d "{\"name\": \"Ban Phim Co\", \"price\": 1200000.0}"

# 4. Cap nhat san pham (PUT)
curl -X PUT http://localhost:8080/api/products/1 \
     -H "Content-Type: application/json" \
     -d "{\"name\": \"Laptop Dell XPS\", \"price\": 25000000.0}"

# 5. Xoa san pham theo ID (DELETE)
curl -X DELETE http://localhost:8080/api/products/1

# 6. Test loi 404 Not Found
curl -X GET http://localhost:8080/api/products/999
```

---

# PHẦN 4: BỘ 15 CÂU HỎI VÀ ĐÁP ÁN TỰ LUẬN TỔNG HỢP

### Câu 1: Trình bày định nghĩa Hệ thống phân tán và phân tích 3 đặc trưng cơ bản.
> **Đáp án chuẩn**:
> - **Định nghĩa**: Hệ thống phân tán là một tập hợp các máy tính độc lập liên kết qua mạng truyền thông, phối hợp và giao tiếp với nhau chỉ bằng cách truyền thông điệp (message passing), xuất hiện trước mắt người dùng như một hệ thống đơn nhất (single coherent system).
> - **3 Đặc trưng cơ bản**:
>   1. *Tính đồng thời (Concurrency)*: Các tiến trình chạy đồng thời trên nhiều nút mạng, chia sẻ tài nguyên chung mà không gây xung đột dữ liệu.
>   2. *Lỗi độc lập của các thành phần (Independent Failure)*: Mỗi máy tính, tiến trình hay liên kết mạng có thể bị lỗi độc lập mà không làm sụp đổ toàn bộ hệ thống; các nút khác vẫn hoạt động bình thường.
>   3. *Không có đồng hồ toàn cục (Lack of a Global Clock)*: Không có một chiếc đồng hồ chuẩn duy nhất chung cho toàn hệ thống để đo mốc thời gian tuyệt đối chính xác giữa các sự kiện xảy ra ở các máy khác nhau (do Clock Drift phần cứng và độ trễ ngẫu nhiên của mạng). Thứ tự sự kiện chỉ được thiết lập qua trao đổi thông điệp (đồng hồ logic Lamport).

---

### Câu 2: Phân tích 8 dạng trong suốt (Transparencies). So sánh Access Transparency và Location Transparency.
> **Đáp án chuẩn**:
> - **8 Dạng trong suốt**: Access, Location, Concurrency, Replication, Failure, Mobility (Migration), Performance, Scaling (Xem chi tiết bảng mục 1.5).
> - **So sánh Access vs Location Transparency**:
>   * *Access Transparency*: Che giấu sự khác biệt về biểu diễn dữ liệu và giao thức truy cập. Cho dù tài nguyên nằm ngay trên máy cục bộ hay ở máy chủ từ xa thì người dùng/chương trình đều dùng chung một cú pháp lệnh/hàm để gọi (ví dụ: hàm `read()` file cục bộ và file mạng NFS).
>   * *Location Transparency*: Che giấu vị trí vật lý trong không gian của tài nguyên. Người dùng truy cập tài nguyên thông qua tên định danh duy nhất (URL) mà không cần biết máy chủ lưu trữ tài nguyên đó đặt ở đâu, thuộc thành phố nào hay địa chỉ IP là gì (ví dụ: truy cập `google.com` hoặc `/api/products`).

---

### Câu 3: Nêu giải pháp giải quyết thách thức Tính không đồng nhất (Heterogeneity). Phân tích vai trò của Middleware.
> **Đáp án chuẩn**:
> - **Thách thức Heterogeneity**: Môi trường phân tán chứa sự khác biệt đa dạng về phần cứng máy tính, hệ điều hành (Windows, Linux, macOS), ngôn ngữ lập trình (Java, C#, Python), giao thức mạng và định dạng biểu diễn dữ liệu (Big-Endian vs Little-Endian).
> - **Giải pháp**:
>   1. Sử dụng lớp phần mềm trung gian (**Middleware**) như Java RMI, Web Services (SOAP, RESTful) để cung cấp giao diện lập trình cấp cao đồng nhất.
>   2. Sử dụng các định dạng chuẩn hóa trung gian độc lập nền tảng như **JSON** và **XML**.
> - **Vai trò của Middleware**: Đóng vai trò là lớp đệm nằm giữa Hệ điều hành/Mạng và Ứng dụng. Middleware trừu tượng hóa toàn bộ sự khác biệt của hạ tầng bên dưới, cung cấp cơ chế đóng gói/giải mã thông điệp (Marshalling/Unmarshalling) và gọi hàm từ xa xuyên suốt giữa các ngôn ngữ khác nhau.

---

### Câu 4: So sánh Mở rộng theo chiều dọc (Scale Up) và Mở rộng theo chiều ngang (Scale Out).
> **Đáp án chuẩn**:
> - **Scale Up (Chiều dọc)**: Nâng cấp phần cứng của một máy chủ duy nhất (tăng dung lượng RAM, CPU nhiều nhân hơn, ổ cứng NVMe). Ưu điểm: Đơn giản, ứng dụng giữ nguyên không cần viết lại mã nguồn. Nhược điểm: Chi phí cực kỳ đắt, bị giới hạn trần công nghệ phần cứng, vẫn tồn tại điểm lỗi đơn lẻ (Single Point of Failure - server hỏng là hệ thống chết).
> - **Scale Out (Chiều ngang)**: Bổ sung thêm nhiều máy chủ phổ thông giá rẻ vào cụm (Cluster) và phân phối tải thông qua Load Balancer. Ưu điểm: Khả năng mở rộng gần như vô hạn, độ sẵn sàng cao, chịu lỗi tốt (1 máy chết các máy khác vẫn phục vụ bình thường). Nhược điểm: Kiến trúc phức tạp, đòi hỏi ứng dụng phải thiết kế Phi trạng thái (Stateless) và đồng bộ dữ liệu.

---

### Câu 5: Tại sao trong hệ thống phân tán không thể sử dụng đồng hồ vật lý toàn cục?
> **Đáp án chuẩn**:
> - Trong hệ thống phân tán, mỗi máy tính sở hữu một bộ dao động thạch anh riêng biệt để tính giờ. Tốc độ dao động này luôn có sự sai lệch nhỏ do nhiệt độ, điện áp và tuổi thọ linh kiện (gọi là hiện tượng **Clock Drift**).
> - Khi các máy tính cố gắng đồng bộ giờ qua mạng (như dùng giao thức NTP), gói tin truyền qua mạng luôn chịu **độ trễ ngẫu nhiên không thể dự đoán trước** (Network Latency Jitter), dẫn đến việc không thể đảm bảo độ chính xác tuyệt đối ở mức micro-giây.
> - Do đó, hệ thống phân tán không thể dựa vào đồng hồ vật lý để xác định thứ tự tuyệt đối của các sự kiện, mà phải sử dụng **Đồng hồ logic (Logical Clocks)** của Leslie Lamport dựa trên quan hệ nhân quả "xảy ra trước" (happened-before relation `->`).

---

### Câu 6: Phân tích 3 thực thể (Roles) và 3 thao tác (Operations) trong mô hình SOA.
> **Đáp án chuẩn**:
> - **3 Thực thể (Roles)**:
>   1. *Service Provider*: Xây dựng và phát hành Web Service, biên soạn bản mô tả WSDL và đăng ký thông tin lên Service Registry.
>   2. *Service Consumer / Requester*: Ứng dụng khách tra cứu Registry để tìm dịch vụ, sau đó kết nối và gọi dịch vụ trực tiếp từ Provider.
>   3. *Service Registry*: Nơi lưu trữ danh mục dịch vụ tập trung (ví dụ: UDDI).
> - **3 Thao tác (Operations)**:
>   1. *Publish*: Provider đưa mô tả dịch vụ lên Registry.
>   2. *Find*: Consumer gửi yêu cầu tra cứu dịch vụ trên Registry.
>   3. *Bind*: Consumer kết nối trực tiếp đến Provider theo thông tin tìm được để gửi dữ liệu và nhận kết quả.

---

### Câu 7: Phân tích cấu trúc thông điệp SOAP và giải thích lý do tại sao SOAP bắt buộc dùng HTTP POST?
> **Đáp án chuẩn**:
> - **Cấu trúc SOAP**: Bọc trong thẻ gốc `<env:Envelope>`, gồm 2 phần tử chính:
>   * `<env:Header>` *(tùy chọn)*: Chứa metadata (xác thực Token, định tuyến, giao dịch).
>   * `<env:Body>` *(bắt buộc)*: Chứa nội dung chính của hàm/tham số gọi từ xa hoặc dữ liệu trả về, hoặc thẻ `<env:Fault>` khi có lỗi xảy ra.
> - **Lý do dùng HTTP POST**:
>   1. Kích thước payload XML của SOAP rất lớn, vượt quá giới hạn độ dài của URL trên phương thức `GET`.
>   2. Phương thức `GET` theo đặc tả HTTP không hỗ trợ gửi kèm Request Body, trong khi SOAP bắt buộc phải chứa nội dung trong thẻ `<env:Body>`.
>   3. Bản chất SOAP là gọi hàm từ xa (RPC), có thể làm thay đổi trạng thái dữ liệu phía máy chủ nên không được dùng `GET` (chỉ đọc).

---

### Câu 8: So sánh 10 tiêu chí toàn diện giữa kiến trúc SOAP và RESTful.
> **Đáp án chuẩn**: Trình bày chính xác bảng so sánh 10 tiêu chí tại **Mục 2.7** (Bản chất, Định dạng dữ liệu, Băng thông, Giao thức truyền tải, WSDL vs OpenAPI, Caching, Bảo mật WS-Security vs HTTPS/JWT, Xử lý lỗi, Gọi từ Client và Trường hợp sử dụng thực tế).

---

### Câu 9: Phân tích nguyên tắc Stateless trong REST và chứng minh vai trò trong việc mở rộng quy mô (Scale Out).
> **Đáp án chuẩn**:
> - **Nguyên tắc Stateless**: Máy chủ Web không lưu trữ bất kỳ trạng thái hay phiên làm việc (Session) nào của Client trong bộ nhớ giữa các lần gọi API. Mỗi Request gửi lên từ Client phải chứa đầy đủ mọi thông tin cần thiết để Server xử lý (dữ liệu nghiệp vụ kèm Access Token xác thực).
> - **Chứng minh vai trò trong Scale Out**:
>   * Nếu Server lưu Session: Client 1 đăng nhập vào Server A, thì mọi Request tiếp theo bắt buộc phải gửi vào đúng Server A (Sticky Session). Nếu Server A sập hoặc quá tải, Client 1 bị mất phiên làm việc.
>   * Với kiến trúc Stateless: Mọi Server trong cụm (Server A, B, C) đều có khả năng xử lý bất kỳ Request nào độc lập. Bộ cân bằng tải (Load Balancer) có thể phân phối Request tới bất kỳ máy chủ rảnh rỗi nào. Khi lưu lượng tăng đột biến, ta chỉ cần bật thêm Server mới vào cụm là hệ thống lập tức mở rộng được mà không cần đồng bộ trạng thái Session.

---

### Câu 10: Trình bày bảng ánh xạ CRUD <-> HTTP Methods, tính Safe, Idempotent và các mã HTTP Status Code.
> **Đáp án chuẩn**:
> - Trình bày chính xác bảng ánh xạ tại **Mục 2.9**: Create (`POST` - 201), Read (`GET` - 200, Safe & Idempotent), Update (`PUT` - 200/204, Idempotent), Patch (`PATCH` - 200), Delete (`DELETE` - 200/204, Idempotent).
> - Giải thích rõ: Safe là không thay đổi dữ liệu máy chủ; Idempotent là gọi 1 lần hay nhiều lần liên tiếp với cùng dữ liệu đều cho kết quả và trạng thái dữ liệu như nhau.
> - Trình bày các mã trạng thái quan trọng tại **Mục 2.10**: 200 OK, 201 Created, 204 No Content, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 405 Method Not Allowed, 500 Internal Server Error.

---

### Câu 11: So sánh `@Controller` và `@RestController` trong kiến trúc Spring Boot MVC.
> **Đáp án chuẩn**:
> - `@Controller`: Là annotation truyền thống dùng trong mô hình MVC hiển thị trang web. Các phương thức trả về tên của View Template (HTML/JSP), được bộ View Resolver phân giải để hiển thị giao diện người dùng.
> - `@RestController`: Là annotation chuyên dụng cho việc xây dựng Web Service RESTful. Nó là sự kết hợp của:
>   $$\text{@RestController} = \text{@Controller} + \text{@ResponseBody}$$
> - Khi dùng `@RestController`, Spring tự động biến đổi (serialize) đối tượng trả về (như Model, List) thành chuỗi dữ liệu **JSON hoặc XML** thông qua thư viện Jackson, và ghi trực tiếp vào phần thân của HTTP Response (`Response Body`), không thông qua View Resolver.

---

### Câu 12: Trình bày ý nghĩa của Spring IoC Container và cơ chế Dependency Injection (@Autowired).
> **Đáp án chuẩn**:
> - **IoC Container (Inversion of Control)**: Là bộ chứa quản lý toàn bộ vòng đời (khởi tạo, cấu hình, liên kết, hủy bỏ) của các đối tượng trong ứng dụng (gọi là các **Spring Bean**). Giúp đảo ngược quyền kiểm soát: lập trình viên không cần tự gọi `new MyService()`, mà Spring sẽ tự tạo và quản lý.
> - **Dependency Injection (DI)**: Là cơ chế mà một đối tượng nhận các đối tượng phụ thuộc của nó từ bên ngoài (thay vì tự khởi tạo bên trong lớp).
> - **Annotation `@Autowired`**: Được dùng để hướng dẫn Spring tự động tìm kiếm Bean tương thích trong IoC Container và tiêm (inject) vào thuộc tính hoặc hàm khởi tạo (Constructor) của lớp đang cần sử dụng.

---

### Câu 13: Trình bày kỹ thuật xử lý ngoại lệ tập trung với `@RestControllerAdvice` và `@ExceptionHandler`.
> **Đáp án chuẩn**:
> - **Vấn đề**: Nếu dùng khối `try-catch` trong từng hàm của Controller, code sẽ bị phân mảnh, trùng lặp và khó bảo trì.
> - **Giải pháp**: Sử dụng cơ chế xử lý ngoại lệ tập trung:
>   * `@RestControllerAdvice`: Đánh dấu một lớp đóng vai trò là nơi chặn bắt (Interception) toàn bộ các lỗi phát sinh từ tất cả các `@RestController` trong ứng dụng.
>   * `@ExceptionHandler(TênNgoạiLệ.class)`: Đặt trước phương thức trong lớp Advice để chỉ định cụ thể loại lỗi cần xử lý (ví dụ: `ResourceNotFoundException`). Phương thức này trả về đối tượng `ResponseEntity` chứa mã HTTP Status chuẩn (như `404 Not Found`) kèm chuỗi JSON mô tả chi tiết lỗi (timestamp, status, message).

---

### Câu 14: Quy trình đóng gói ứng dụng Spring Boot với Dockerfile và kiểm thử với lệnh cURL.
> **Đáp án chuẩn**:
> 1. **Quy trình build và đóng gói**:
>    - Biên dịch dự án ra file JAR: `mvn clean package`
>    - Viết file `Dockerfile` sử dụng base image `eclipse-temurin:21-jre-alpine`, sao chép file JAR vào và mở cổng `EXPOSE 8080`.
>    - Build Docker Image: `docker build -t product-service:1.0 .`
>    - Chạy Docker Container: `docker run -d -p 8080:8080 --name product-app product-service:1.0`
> 2. **Kiểm thử với cURL**:
>    - Lấy dữ liệu: `curl -X GET http://localhost:8080/api/products`
>    - Thêm mới: `curl -X POST http://localhost:8080/api/products -H "Content-Type: application/json" -d "{\"name\":\"Chuot\",\"price\":200.0}"`
>    - Xóa: `curl -X DELETE http://localhost:8080/api/products/1`

---

### Câu 15: Bài toán lập trình hoàn chỉnh (Model, Controller CRUD an toàn đa luồng, Application, Dockerfile) theo chuẩn đề thi IUH.
> **Đáp án chuẩn**:
> Trình bày đầy đủ 4 đoạn code chuẩn (Model `Product.java`, Controller `ProductController.java` dùng `CopyOnWriteArrayList` và `AtomicLong`, `Application.java`, và `Dockerfile`) đúng như mẫu tại **Mục 3.2** và **Mục 3.5**.
