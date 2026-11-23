# TỔNG HỢP LÝ THUYẾT HỆ THỐNG PHÂN TÁN (CHƯƠNG 1)
**Tài liệu ôn thi Cuối kỳ - Môn: Phát triển hệ thống phân tán (IUH)**  
*Sinh viên: Lê Thành Long - MSSV: 23630851*

---

## I. TỔNG QUAN & ĐỊNH NGHĨA

### 1. Hệ thống phân tán (Distributed System) là gì?
* **Định nghĩa của Andrew S. Tanenbaum**: Hệ thống phân tán là một tập hợp các máy tính độc lập (autonomous computers) xuất hiện đối với người dùng như một **hệ thống đơn nhất** (single coherent system).
* **Định nghĩa của George Coulouris**: Là hệ thống trong đó các thành phần phần cứng hoặc phần mềm đặt tại các máy tính kết nối mạng truyền thông và phối hợp các hành động của chúng **chỉ bằng cách truyền thông điệp (message passing)**.

### 2. 3 Đặc tính cơ bản cốt lõi (Core Characteristics)
Mọi hệ thống phân tán đều phải đối mặt với 3 đặc tính bất biến:
1. **Tính song song / Đồng thời (Concurrency)**:
   - Các tiến trình/chương trình chạy đồng thời trên nhiều máy tính khác nhau.
   - Nhiều tác vụ cùng thao tác chia sẻ tài nguyên chung (dữ liệu, phần cứng) mà không được gây xung đột hay mất nhất quán.
2. **Lỗi độc lập của các thành phần (Independent Failure of Components)**:
   - Một máy tính, tiến trình, hoặc liên kết mạng có thể bị lỗi, sập (crash) mà không làm sụp đổ toàn bộ hệ thống.
   - Các nút khác vẫn tiếp tục hoạt động bình thường và hệ thống phải có cơ chế chịu lỗi, cách ly sự cố.
3. **Không có đồng hồ toàn cục (Lack of a Global Clock)**:
   - Không tồn tại một chiếc đồng hồ chuẩn duy nhất chung cho toàn hệ thống để xác định thời gian tuyệt đối chính xác giữa các sự kiện xảy ra ở các máy khác nhau.
   - Sự đồng bộ hóa và thứ tự các sự kiện chỉ có thể dựa trên việc trao đổi thông điệp (Logical Clock / Lamport Timestamps).

---

## II. 8 THÁCH THỨC LỚN KHI XÂY DỰNG HỆ THỐNG PHÂN TÁN

| STT | Thách thức | Nội dung chi tiết | Giải pháp kỹ thuật |
| :---: | :--- | :--- | :--- |
| **1** | **Heterogeneity**<br>*(Tính đa dạng / không đồng nhất)* | Khác biệt về mạng truyền thông, phần cứng máy tính, hệ điều hành (Windows, Linux, macOS), ngôn ngữ lập trình (Java, C#, Python), định dạng biểu diễn dữ liệu (Big-Endian vs Little-Endian). | Sử dụng **Middleware** (lớp phần mềm trung gian như RMI, CORBA, Web Services) và định dạng chuẩn (JSON, XML). |
| **2** | **Openness**<br>*(Tính mở)* | Khả năng mở rộng, tích hợp thêm các dịch vụ, phần cứng, phần mềm mới mà không phá vỡ hệ thống sẵn có. | Xuất bản các giao diện chuẩn (Standard Interfaces / APIs), đảm bảo tính tương tác (Interoperability) và tính khả chuyển (Portability). |
| **3** | **Security Enforcement**<br>*(An ninh & Bảo mật)* | Bảo vệ tài nguyên chống truy cập trái phép, nghe lén, giả mạo dữ liệu khi truyền trên mạng công cộng. | Ba trụ cột CIA: **Confidentiality** (Mã hóa SSL/TLS, AES), **Integrity** (Chữ ký số, Hash SHA-256), **Availability** (Chống DDoS, cân bằng tải) + Xác thực (Authentication) & Phân quyền (Authorization). |
| **4** | **Scalability**<br>*(Khả năng mở rộng)* | Hệ thống vẫn duy trì hiệu năng tốt khi số lượng người dùng và tài nguyên tăng đột biến. | Mở rộng theo chiều ngang (Scale Out - thêm máy), Caching, Phân vùng dữ liệu (Partitioning/Sharding), Tránh thuật toán tập trung (Centralized algorithms) và cổ chai hiệu năng. |
| **5** | **Failure Handling**<br>*(Xử lý lỗi)* | Lỗi là điều không thể tránh khỏi trong môi trường phân tán (đứt cáp, máy chủ chết, timeout). | 5 cơ chế: Phát hiện lỗi (Detecting), Che giấu lỗi (Masking), Chịu lỗi (Tolerating), Phục hồi (Recovery), Dư thừa phần cứng/dữ liệu (Redundancy). |
| **6** | **Concurrency Management**<br>*(Quản lý đồng thời)* | Nhiều người dùng đồng thời đọc/ghi vào cùng một tài nguyên chia sẻ. | Cơ chế đồng bộ hóa (Synchronization), khóa (Locks), loại trừ tương hỗ (Mutual Exclusion), xử lý giao dịch ACID. |
| **7** | **Transparency**<br>*(Tính trong suốt)* | Che giấu sự phân tán về mặt vật lý, logic đối với người dùng và lập trình viên. | Cung cấp giao diện trừu tượng để lập trình viên tương tác như gọi hàm nội bộ (Local Call). |
| **8** | **Quality of Service (QoS)**<br>*(Chất lượng dịch vụ)* | Đảm bảo các chỉ số kỹ thuật về độ tin cậy (Reliability), thời gian đáp ứng (Latency/Response Time), thông lượng (Throughput). | Cấp phát tài nguyên động, dự phòng băng thông, giới hạn tải (Rate Limiting). |

---

## III. 8 DẠNG TRONG SUỐT (TRANSPARENCIES - ISO/ODP)

Tính trong suốt là mục tiêu hàng đầu giúp hệ thống phân tán dễ sử dụng như một hệ thống máy tính cục bộ đơn nhất.

| Dạng trong suốt | Tên tiếng Anh | Ý nghĩa cốt lõi | Ví dụ minh họa |
| :---: | :--- | :--- | :--- |
| **1** | **Access transparency** | Che giấu sự khác biệt về định dạng dữ liệu và phương thức truy cập. Truy cập tài nguyên cục bộ hay từ xa đều dùng cú pháp như nhau. | Lệnh `read()` đọc file trên ổ cứng máy tính hoặc trên máy chủ NFS từ xa đều dùng cùng một hàm. Java RMI gọi hàm từ xa như gọi hàm cục bộ. |
| **2** | **Location transparency** | Che giấu vị trí vật lý của tài nguyên. Người dùng truy cập không cần biết tài nguyên nằm ở máy nào, thành phố nào. | Truy cập `https://google.com` hoặc `http://server/api/products` mà không cần biết địa chỉ IP thật của máy chủ lưu trữ ở đâu. |
| **3** | **Concurrency transparency** | Che giấu sự cạnh tranh tài nguyên giữa nhiều tiến trình đồng thời mà không làm hỏng dữ liệu. | Hai khách hàng cùng rút tiền ở cây ATM khác nhau từ cùng một tài khoản ngân hàng, hệ thống khóa và trừ tiền chính xác. |
| **4** | **Replication transparency** | Che giấu việc tài nguyên được nhân bản thành nhiều bản sao tại nhiều nơi để tăng tốc độ và dự phòng sự cố. | Một video YouTube hay file ảnh CDN được copy ra 10 server toàn cầu, người xem bấm xem mà không biết mình đang tải từ bản sao nào. |
| **5** | **Failure transparency** | Che giấu lỗi phần cứng/mạng, cho phép ứng dụng tiếp tục hoàn thành nhiệm vụ dù một số thành phần bị sự cố. | Khi gửi email hoặc thanh toán, nếu một máy chủ chết, hệ thống tự động định tuyến sang máy chủ dự phòng mà người dùng không bị báo lỗi. |
| **6** | **Mobility (Migration) transparency** | Che giấu việc tài nguyên hoặc tiến trình di chuyển từ máy tính này sang máy tính khác trong khi đang hoạt động. | Người dùng dùng điện thoại di chuyển từ trạm phát sóng Wi-Fi này sang Wi-Fi khác hoặc chuyển vùng 4G mà cuộc gọi không bị ngắt. |
| **7** | **Performance transparency** | Che giấu việc hệ thống tự động tái cấu trúc, thêm bớt máy tính, cân bằng tải khi lưu lượng tăng giảm đột ngột. | Hệ thống tự động phân phối tải CPU, thêm server ảo khi có flash-sale mà người dùng không cảm nhận thấy độ trễ tăng. |
| **8** | **Scaling transparency** | Cho phép hệ thống mở rộng quy mô (thêm người dùng, dữ liệu, thiết bị) mà không cần thay đổi kiến trúc hoặc thuật toán ứng dụng. | Mạng Internet mở rộng từ vài nghìn máy tính lên hàng tỷ thiết bị mà giao thức DNS và TCP/IP vẫn giữ nguyên nguyên lý hoạt động. |

---

## IV. CÁC MÔ HÌNH KIẾN TRÚC PHÂN TÁN (DISTRIBUTED ARCHITECTURES)

### 1. Mô hình Client - Server
* **Đặc điểm**: Phân chia vai trò rõ ràng giữa nút yêu cầu dịch vụ (**Client**) và nút cung cấp dịch vụ (**Server**).
* **Phân cấp tầng**:
  - **2-Tier (2 tầng)**: Client (Giao diện + Xử lý) kết nối trực tiếp đến Database Server. Dễ xây dựng nhưng khó mở rộng, kém bảo mật.
  - **3-Tier (3 tầng)**: 
    * *Tầng 1 - Presentation*: Giao diện người dùng (Browser, Mobile App).
    * *Tầng 2 - Application / Business Logic*: Máy chủ xử lý logic nghiệp vụ (Spring Boot, Node.js).
    * *Tầng 3 - Data Storage*: Cơ sở dữ liệu (MySQL, MongoDB, Oracle).
  - **Multi-tier / N-Tier**: Bổ sung thêm API Gateway, Load Balancer, Cache Redis, Message Queue.

### 2. Mô hình Ngang hàng (Peer-to-Peer - P2P)
* **Đặc điểm**: Mọi nút trong mạng (Peers) đều bình đẳng, vừa đóng vai trò là Client (tiêu thụ tài nguyên), vừa là Server (cung cấp tài nguyên).
* **Ưu điểm**: Khả năng mở rộng cực cao, không có điểm lỗi đơn lẻ (No Single Point of Failure).
* **Ứng dụng**: BitTorrent, Blockchain (Bitcoin, Ethereum), Skype thời kỳ đầu.

### 3. Khái niệm Middleware (Phần mềm trung gian)
* **Định nghĩa**: Lớp phần mềm nằm giữa Hệ điều hành / Mạng phần cứng bên dưới và Ứng dụng phân tán bên trên.
* **Vai trò**: Che giấu tính không đồng nhất (Heterogeneity), cung cấp các giao thức gọi hàm từ xa (RPC, RMI) hoặc nhắn tin (JMS, Message Queue, Web Services).

---

## V. 8 SAI LẦM KINH ĐIỂN VỀ TÍNH TOÁN PHÂN TÁN (THE 8 FALLACIES - L. PETER DEUTSCH)

Khi lập trình viên chuyển từ ứng dụng đơn khối (Monolith) sang phân tán, họ thường mắc 8 giả định sai lầm sau:
1. **The network is reliable** *(Mạng luôn đáng tin cậy)*: Sai, dây cáp có thể đứt, wifi mất tín hiệu, gói tin bị rơi.
2. **Latency is zero** *(Độ trễ truyền mạng bằng 0)*: Sai, gọi hàm nội bộ mất nano-giây, gọi qua mạng mất từ vài mili-giây đến vài giây.
3. **Bandwidth is infinite** *(Băng thông là vô hạn)*: Sai, đường truyền mạng có giới hạn tải, dữ liệu lớn gây tắc nghẽn.
4. **The network is secure** *(Mạng là tuyệt đối an toàn)*: Sai, đường truyền mạng luôn có nguy cơ bị nghe lén, MITM, chèn mã độc.
5. **Topology doesn't change** *(Cấu trúc liên kết mạng không bao giờ đổi)*: Sai, router có thể khởi động lại, IP đổi động, máy tính thêm bớt liên tục.
6. **There is one administrator** *(Chỉ có một người quản trị duy nhất)*: Sai, mỗi hệ thống do các tổ chức/công ty khác nhau quản lý cấu hình khác nhau.
7. **Transport cost is zero** *(Chi phí vận chuyển dữ liệu bằng 0)*: Sai, chi phí phần cứng mạng, băng thông đám mây, CPU đóng/mở gói serialization đều tốn kém.
8. **The network is homogeneous** *(Mạng là đồng nhất về chủng loại)*: Sai, mạng gồm vô vàn thiết bị khác nhau của Cisco, TP-Link, hệ điều hành Android, iOS, Linux, Windows.

---

## VI. ĐA LUỒNG (MULTI-THREADING) TRONG HỆ THỐNG PHÂN TÁN

### 1. Tại sao Server phân tán bắt buộc phải dùng Multi-threading?
- **Tránh nghẽn (Non-blocking)**: Nếu server đơn luồng (Single-thread), khi đang phục vụ Client 1 (hoặc đợi I/O đọc ổ cứng), tất cả Client khác sẽ bị treo cứng.
- **Tận dụng tối đa phần cứng**: CPU hiện đại có nhiều nhân (Multi-core), đa luồng giúp chạy song song trên các core.
- **Tăng thông lượng (Throughput)**: Phục vụ hàng nghìn request/giây cùng lúc.

### 2. Các cách tạo luồng trong Java
1. **Kế thừa lớp `Thread`**:
   - `class MyThread extends Thread { public void run() { ... } }`
   - Nhược điểm: Java chỉ hỗ trợ đơn kế thừa, không kế thừa thêm class khác được.
2. **Cài đặt interface `Runnable` (Khuyên dùng)**:
   - `class MyTask implements Runnable { public void run() { ... } }`
   - Ưu điểm: Tách biệt logic công việc với việc quản lý luồng, kế thừa thoải mái.
3. **Cài đặt interface `Callable<T>` kết hợp `ExecutorService`**:
   - Trả về kết quả thông qua đối tượng `Future<T>`.
   - Quản lý tái sử dụng luồng bằng **Thread Pool** (`Executors.newFixedThreadPool(n)`), tránh chi phí khởi tạo luồng mới liên tục.

---

## VII. BỘ CÂU HỎI ÔN THI LÝ THUYẾT CHƯƠNG 1 (TRÚNG ĐỀ THI IUH)

**Câu 1: Trình bày định nghĩa hệ thống phân tán và nêu 3 đặc trưng cơ bản.**
> *Đáp án*: 
> - Hệ thống phân tán là tập hợp các máy tính độc lập liên kết mạng, giao tiếp và phối hợp với nhau chỉ bằng cách truyền thông điệp, hiển thị trước người dùng như một hệ thống đơn nhất.
> - 3 đặc trưng cốt lõi: (1) Tính đồng thời (Concurrency); (2) Lỗi độc lập của các thành phần (Independent failure); (3) Không có đồng hồ toàn cục (Lack of a global clock).

**Câu 2: Phân biệt Access Transparency và Location Transparency.**
> *Đáp án*:
> - **Access Transparency**: Che giấu sự khác biệt về cách thức truy cập dữ liệu (truy cập cục bộ hay từ xa đều dùng cùng lệnh/hàm).
> - **Location Transparency**: Che giấu vị trí vật lý của tài nguyên (truy cập tài nguyên bằng tên/URL định danh duy nhất mà không cần biết máy chủ đặt ở đâu).

**Câu 3: Nêu giải pháp giải quyết thách thức Tính không đồng nhất (Heterogeneity).**
> *Đáp án*: Sử dụng phần mềm trung gian (**Middleware**) như Java RMI, Web Services (REST/SOAP) và sử dụng các chuẩn định dạng dữ liệu trung gian độc lập nền tảng như **JSON, XML**.

**Câu 4: So sánh mở rộng theo chiều dọc (Scale Up) và chiều ngang (Scale Out).**
> *Đáp án*:
> - **Scale Up (Chiều dọc)**: Nâng cấp phần cứng của một máy chủ duy nhất (tăng RAM, CPU, SSD). Dễ cấu hình nhưng có giới hạn phần cứng và chi phí rất đắt, vẫn bị điểm lỗi đơn lẻ.
> - **Scale Out (Chiều ngang)**: Bổ sung thêm nhiều máy chủ giá rẻ vào cụm phân tán và dùng Load Balancer chia tải. Chi phí linh hoạt, khả năng mở rộng gần như không giới hạn, chịu lỗi tốt.

**Câu 5: Tại sao trong hệ thống phân tán không thể sử dụng đồng hồ vật lý toàn cục?**
> *Đáp án*: Do sự chênh lệch thạch anh đồng hồ phần cứng của mỗi máy tính (Clock Drift) và độ trễ ngẫu nhiên không thể dự đoán của đường truyền mạng khi đồng bộ giờ. Do đó, người ta phải dùng đồng hồ logic (Logical Clocks) để xác định thứ tự quan hệ trước-sau ("happened-before") của các sự kiện.
