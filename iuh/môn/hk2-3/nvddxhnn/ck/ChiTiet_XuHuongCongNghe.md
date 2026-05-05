# ĐỀ CƯƠNG ÔN TẬP CHUYÊN SÂU: 9 XU HƯỚNG CÔNG NGHỆ & NGHỀ NGHIỆP TƯƠNG LAI
*(Phiên bản Cực kỳ chi tiết kèm Case Study & Ví dụ thực tế)*

Tài liệu này được biên soạn mở rộng với các ví dụ thực tiễn trong công nghiệp (Industry Use Cases), kiến trúc hệ thống và công cụ chuyên sâu. Mục tiêu là giúp bạn không chỉ học thuộc lòng mà có thể **phân tích, thuyết trình và bảo vệ ý kiến** trong kỳ thi hoặc phỏng vấn.

---

## 01. KỸ SƯ IoT (Internet of Things - Internet Vạn Vật)

### 1. Bản chất (Là gì?)
Kỹ sư IoT thiết kế một hệ sinh thái kết nối thế giới vật lý và thế giới số. Một hệ thống IoT tiêu chuẩn gồm 4 lớp:
1.  **Lớp thiết bị (Edge/Device):** Các cảm biến (Sensor) và bộ chấp hành (Actuator).
2.  **Lớp mạng (Network):** Các Gateway dùng sóng Wi-Fi, LoRa, 5G để gửi dữ liệu.
3.  **Lớp trung tâm (Cloud):** Lưu trữ và xử lý hàng triệu bản ghi gửi lên mỗi giây.
4.  **Lớp ứng dụng (Application):** App trên điện thoại hoặc Web Dashboard cho người dùng.

### 2. Giải quyết vấn đề gì? (Ví dụ thực tế cụ thể)
IoT giải quyết bài toán **thu thập dữ liệu không giới hạn và tự động hóa điều khiển vật lý**.

*   **Ví dụ 1 - Nông nghiệp thông minh (Smart Agriculture):** Trong một mô hình nhà màng trồng dưa lưới, kỹ sư IoT lắp đặt cảm biến nhiệt độ, độ ẩm đất, và cường độ sáng. Khi cảm biến phát hiện độ ẩm đất giảm xuống dưới 40%, vi điều khiển sẽ gửi tín hiệu kích hoạt máy bơm nước nhỏ giọt chạy đúng 10 phút rồi tự tắt. **Giá trị:** Tiết kiệm 50% lượng nước và phân bón, không cần người trực tiếp đi tưới.
*   **Ví dụ 2 - Chuỗi cung ứng lạnh (Cold Chain Logistics):** Khi vận chuyển Vaccine COVID-19, nhiệt độ phải luôn ở mức âm 70 độ C. Một thiết bị IoT gắn trong thùng lạnh sẽ liên tục đo nhiệt độ và định vị GPS, gửi về trung tâm mỗi 5 phút qua sóng 5G/4G. Nếu nhiệt độ tăng lên âm 60 độ, hệ thống sẽ hú còi tại buồng lái để tài xế kiểm tra, đồng thời báo động về trụ sở chính.

### 3. Cần chuẩn bị gì?
*   **Phần cứng:** Nắm vững kiến trúc vi điều khiển ESP8266/ESP32, Raspberry Pi, Arduino.
*   **Điện tử cơ bản:** Biết đọc sơ đồ mạch, hàn mạch, kiến thức về nguồn điện, trở, tụ, giao tiếp I2C, SPI.
*   **Giao thức Mạng IoT:** **MQTT** (Giao thức Publish/Subscribe tiêu chuẩn cho IoT vì rất nhẹ), CoAP, Bluetooth Low Energy (BLE), LoRaWAN (truyền sóng xa hàng chục km trong nông nghiệp/rừng).
*   **Lập trình:** C/C++ (chạy trên chip nhúng), Python.
*   **Cloud IoT:** AWS IoT Core hoặc Microsoft Azure IoT Hub.

---

## 02. KỸ SƯ VR/AR/XR (Thực tế ảo / Tăng cường / Mở rộng)

### 1. Bản chất (Là gì?)
Là chuyên gia về **Điện toán không gian (Spatial Computing)**.
*   **VR:** Đeo kính bịt kín mắt (Meta Quest, Apple Vision Pro), đưa người dùng vào thế giới 3D ảo 100%. (3DoF: Chỉ xoay đầu; 6DoF: Xoay đầu và bước đi trong không gian).
*   **AR:** Dùng camera điện thoại hoặc kính kính trong suốt (HoloLens) để chiếu vật thể 3D lơ lửng trong phòng khách thật của bạn.

### 2. Giải quyết vấn đề gì? (Ví dụ thực tế cụ thể)
XR giải quyết rủi ro, chi phí của thế giới vật lý và giới hạn của màn hình 2D phẳng.

*   **Ví dụ 1 - Đào tạo Y khoa (VR):** Sinh viên y khoa có thể đeo kính VR để thực hành mổ tim 3D. Họ có thể cắt sai tĩnh mạch, bệnh nhân ảo sẽ chảy máu, hệ thống sẽ trừ điểm. Sinh viên làm đi làm lại 100 lần mà không gây hậu quả thật. **Giá trị:** Không rủi ro tính mạng, chi phí 0 đồng cho vật tư y tế.
*   **Ví dụ 2 - Bán lẻ nội thất IKEA (AR):** Khách hàng muốn mua ghế Sofa nhưng sợ không vừa phòng khách. Họ mở app IKEA, chỉ camera điện thoại xuống sàn nhà, một chiếc Sofa 3D tỷ lệ 1:1 sẽ hiện ra ngay trong phòng. Khách hàng có thể đi vòng quanh xem nó có hợp màu sơn tường không trước khi bấm "Đặt hàng".
*   **Ví dụ 3 - Sửa chữa công nghiệp (AR):** Thợ cơ khí đeo kính HoloLens nhìn vào động cơ máy bay. Kính sẽ tự động quét, nhận diện phụ tùng và hiện mũi tên 3D chỉ đúng con ốc cần vặn, kèm theo cảnh báo nhiệt độ.

### 3. Cần chuẩn bị gì?
*   **Engine lõi:** **Unity 3D** (chiếm 60-70% thị phần XR hiện nay) hoặc **Unreal Engine** (đồ họa chân thực siêu cấp).
*   **Toán học Không gian:** Đại số tuyến tính, Quaternion (Toán học xoay 3D), Vector.
*   **Thư viện/SDK:** ARCore (Google), ARKit (Apple iOS), Vuforia, OpenXR.
*   **Đồ họa (Cơ bản):** Hiểu quy trình tạo Mesh, Material, Shader, Texture, Lighting.
*   **UI/UX Không gian:** Thiết kế nút bấm lơ lửng trên không trung sao cho người dùng có thể dùng tay (Hand Tracking) để chạm vào.

---

## 03. KỸ SƯ BẢO MẬT (Cybersecurity)

### 1. Bản chất (Là gì?)
Là những chuyên gia bảo vệ tài sản số (Digital Assets). Mảng này chia làm 2 phe chính:
*   **Red Team (Offensive):** Những người được thuê để "hack" hợp pháp vào hệ thống công ty nhằm tìm ra lỗ hổng.
*   **Blue Team (Defensive):** Những người xây thành, dựng Firewall, phân tích log để bắt quả tang Hacker.

### 2. Giải quyết vấn đề gì? (Ví dụ thực tế cụ thể)
Giải quyết bài toán sống còn: Khủng hoảng niềm tin, rò rỉ dữ liệu, tổn thất hàng triệu USD.

*   **Ví dụ 1 - Lỗ hổng Ngân hàng số (Web Security):** Một kỹ sư Pentest (Red Team) kiểm tra App ngân hàng X. Họ phát hiện lỗ hổng IDOR (Tham chiếu đối tượng trực tiếp). Bằng cách sửa tham số `id_nguoinhan=123` thành `id_nguoinhan=999` trên thanh URL, họ xem được số dư tài khoản của người khác. Kỹ sư sẽ báo lỗi này cho Dev sửa ngay lập tức trước khi Hacker thật phát hiện ra.
*   **Ví dụ 2 - Tấn công Ransomware (Mã độc tống tiền):** Hacker lừa nhân viên bệnh viện click vào link lạ, thả mã độc mã hóa toàn bộ hồ sơ bệnh án, đòi 1 triệu USD tiền chuộc. Kỹ sư SOC (Blue Team) sử dụng hệ thống SIEM để phát hiện một đoạn mã khả nghi đang chạy mã hóa file số lượng lớn. Hệ thống tự động cách ly máy tính đó khỏi mạng nội bộ ngay ở giây thứ 5, cứu được toàn bộ hệ thống bệnh viện.

### 3. Cần chuẩn bị gì?
*   **Mạng (Networking):** Nắm vững cách các gói tin TCP/IP, UDP, ICMP bay lượn. Hiểu cơ chế hoạt động của DNS, DHCP, Proxies, VPN.
*   **Hệ điều hành:** Master Command Line của **Linux** (Kali Linux, Parrot OS). Hiểu cấu trúc Windows Registry, Active Directory (nơi quản lý hàng ngàn máy tính của doanh nghiệp).
*   **Chuẩn bảo mật:** OWASP Top 10 (10 lỗ hổng Web nguy hiểm nhất thế giới), MITRE ATT&CK framework (Bách khoa toàn thư về các ngón đòn của Hacker).
*   **Công cụ:** Nmap (quét cổng), Burp Suite (Bắt và sửa gói tin Web), Metasploit, Wireshark.
*   **Lập trình:** Python để viết tool quét tự động, SQL (để hiểu SQL Injection).

---

## 04. KỸ SƯ BLOCKCHAIN

### 1. Bản chất (Là gì?)
Xây dựng một cơ sở dữ liệu **Phân tán (Distributed Ledger)**. Khác với Database truyền thống (SQL) có quyền "Sửa, Xóa" do một người quản trị nắm giữ, Blockchain chỉ cho phép "Thêm mới" dữ liệu. Một khi dữ liệu được đóng thành Khối (Block) và móc nối lại với nhau bằng Hàm băm mật mã học (Hash), **không ai (kể cả tổng giám đốc) có quyền sửa hay xóa**.

### 2. Giải quyết vấn đề gì? (Ví dụ thực tế cụ thể)
Xóa bỏ sự phụ thuộc vào lòng tin đối với con người hoặc tổ chức trung gian (Ngân hàng, Nhà nước, Sàn giao dịch).

*   **Ví dụ 1 - Hợp đồng thông minh bảo hiểm nông nghiệp (Smart Contract):** Nông dân mua bảo hiểm hạn hán bằng Smart Contract trên nền tảng Ethereum. Hợp đồng tự động lấy dữ liệu từ Cơ quan Khí tượng Quốc gia. Nếu trời không mưa liên tục 60 ngày, đoạn code `if (days_without_rain >= 60) { transferFunds(farmerAddress); }` sẽ tự động chạy, tiền bồi thường đổ thẳng vào ví nông dân trong 2 giây mà không cần nhân viên bảo hiểm xuống thẩm định, ký giấy tờ rườm rà.
*   **Ví dụ 2 - Truy xuất nguồn gốc nông sản sạch:** Một hộp sữa Vinamilk được cấp 1 mã QR Blockchain. Từ người nông dân vắt sữa, người lái xe tải chở sữa, đến nhà máy đóng gói, mỗi bước đều ký điện tử đưa lên Blockchain. Khách hàng ở siêu thị quét mã QR sẽ biết chính xác hộp sữa vắt lúc mấy giờ, nuôi ở trang trại nào. Không ai có thể làm giả dữ liệu vì nó đã được đồng thuận bởi hàng ngàn máy tính trên mạng.

### 3. Cần chuẩn bị gì?
*   **Kiến trúc:** Hiểu Máy ảo Ethereum (EVM), thuật toán đồng thuận Proof of Work (PoW) vs Proof of Stake (PoS), Public Key/Private Key (Mật mã bất đối xứng).
*   **Ngôn ngữ Smart Contract:** **Solidity** (Tuyệt đối quan trọng để code trên hệ sinh thái Ethereum, BNB Chain). Biết thêm Rust (cho Solana).
*   **Phát triển Web3 (Dapp):** Dùng ReactJS/Node.js kết hợp với thư viện **Web3.js** hoặc **Ethers.js** để làm cầu nối giữa giao diện Web và Smart Contract.
*   **Công cụ Tester/Deploy:** Hardhat, Truffle, Remix IDE, ví MetaMask.

---

## 05. KỸ SƯ ML/AI (Machine Learning / Trí tuệ nhân tạo)

### 1. Bản chất (Là gì?)
Chuyển từ lập trình dựa trên Quy tắc (Rule-based: Cứ A thì ra B) sang lập trình dựa trên Dữ liệu (Data-driven). Kỹ sư ML cho máy tính xem hàng vạn ví dụ (Data), yêu cầu máy tính tự tìm ra quy luật thống kê (Pattern), từ đó tạo ra một phương trình khổng lồ (Mô hình/Model) để dự đoán những dữ liệu chưa từng thấy.

### 2. Giải quyết vấn đề gì? (Ví dụ thực tế cụ thể)
Giải quyết các bài toán liên quan đến sự phức tạp không giới hạn của môi trường thực tế (giọng nói, hình ảnh, thị hiếu con người).

*   **Ví dụ 1 - Thị giác máy tính (Computer Vision) trong Y tế:** Lập trình viên không thể viết lệnh `if` để nhận diện bệnh ung thư phổi vì mỗi tấm phim X-Quang một khác. Kỹ sư AI cung cấp cho mô hình mạng nơ-ron sâu (Deep Learning) 100,000 bức ảnh phổi có khối u và 100,000 bức ảnh phổi khỏe mạnh. Mô hình tự học cách nhận diện bóng mờ của khối u. Nay bác sĩ chụp 1 tấm X-quang mới, AI mất 1 giây để kết luận "95% có dấu hiệu ung thư giai đoạn 1".
*   **Ví dụ 2 - Hệ thống Gợi ý của Netflix (Recommendation System):** Dựa vào lịch sử bạn hay xem phim hành động, có diễn viên Tom Cruise, và hay xem hết vào lúc 10h đêm. Mô hình AI (Collaborative Filtering) tìm kiếm hàng triệu người có hành vi giống bạn và suy ra bộ phim bạn có xác suất bấm vào xem cao nhất để đưa lên trang chủ. (Tính năng này tạo ra hàng tỷ USD doanh thu cho Netflix/Shopee).

### 3. Cần chuẩn bị gì?
*   **Nền tảng Toán (Bắt buộc phải giỏi):**
    *   *Đại số tuyến tính:* Ma trận, Tích vô hướng (để máy tính tính toán song song).
    *   *Giải tích:* Đạo hàm, Gradient Descent (để mô hình tự "sửa sai" sau mỗi vòng lặp học).
    *   *Xác suất thống kê:* Các phân phối, giá trị kỳ vọng.
*   **Lập trình:** **Python** (C++. CUDA nếu làm sâu về lõi).
*   **Khung làm việc (Frameworks):** Scikit-learn (Machine Learning), **TensorFlow / PyTorch** (Deep Learning).
*   **Kiến thức mô hình:** CNN (Xử lý ảnh), RNN/LSTM/Transformer (Xử lý chuỗi, ngôn ngữ).

---

## 06. KỸ SƯ DỮ LIỆU (Data Engineer)

### 1. Bản chất (Là gì?)
Xây dựng hệ thống đường ống dẫn dữ liệu (Data Pipeline). Nếu công ty là một nhà máy, Data Engineer là người thiết kế hệ thống ống dẫn, bơm nước từ sông (dữ liệu thô từ các App, Web, Database máy chủ), qua bộ lọc làm sạch (ETL/ELT), rồi đổ vào một bể chứa khổng lồ đạt chuẩn (Data Warehouse) để đội ngũ Phân tích (Data Analyst) dùng nước đó pha trà, nấu ăn (làm báo cáo).

### 2. Giải quyết vấn đề gì? (Ví dụ thực tế cụ thể)
Giải quyết 3 chữ V của Big Data: Volume (Khối lượng khổng lồ), Velocity (Tốc độ tạo ra nhanh), Variety (Đa dạng chuẩn loại: chữ, ảnh, video).

*   **Ví dụ 1 - Tính tiền cước Surge Pricing của Grab/Uber (Velocity):** Cứ mỗi 1 giây, hàng trăm ngàn tài xế gửi tọa độ GPS lên hệ thống. Không cơ sở dữ liệu SQL nào chịu nổi việc `INSERT` 100,000 dòng/giây. Kỹ sư Dữ liệu dùng **Apache Kafka** để hứng luồng dữ liệu thời gian thực (Streaming Data), tính toán ngay lập tức số lượng tài xế vs hành khách tại Quận 1, từ đó AI ra quyết định tăng giá cước gấp đôi (Surge Pricing).
*   **Ví dụ 2 - Báo cáo ngân hàng (Volume & Variety):** Ngân hàng có dữ liệu nằm rải rác: Lịch sử quẹt thẻ Visa (hệ thống Oracle), lịch sử chuyển khoản (App Mobile), lịch sử chat với tổng đài hỗ trợ (file Text). Kỹ sư dữ liệu viết script gom tự động tất cả "rác" này mỗi đêm (Batch Processing), chuẩn hóa định dạng ngày tháng, xóa dữ liệu rỗng, đưa vào kho **Google BigQuery**. Sáng hôm sau, Giám đốc mở Dashboard PowerBI lên là có số liệu chính xác để báo cáo rủi ro.

### 3. Cần chuẩn bị gì?
*   **Ngôn ngữ truy vấn (SQL):** Phải là bậc thầy về SQL (Window Functions, CTEs, tối ưu Index).
*   **Ngôn ngữ lập trình:** Python (Pandas), Scala, Java.
*   **Xử lý Dữ liệu lớn (Big Data):** **Apache Spark** (Xử lý dữ liệu phân tán trong RAM nhanh gấp 100 lần Hadoop).
*   **Streaming Data (Dữ liệu thời gian thực):** Apache Kafka, Flink.
*   **Luồng công việc (Orchestration):** Apache Airflow (lên lịch: 12h đêm tự lấy dữ liệu, 1h sáng làm sạch, 2h sáng cảnh báo lỗi).
*   **Cloud Data Warehouse:** Snowflake, Amazon Redshift, Google BigQuery.

---

## 07. KỸ SƯ CLOUD (Điện toán đám mây)

### 1. Bản chất (Là gì?)
Kiến trúc sư của các "máy chủ ảo". Thay vì công ty phải bỏ 2 tỷ đồng xây phòng lạnh, mua Server cục sắt Dell/HP, đấu nối dây mạng, thì Kỹ sư Cloud chỉ cần ngồi ở quán cafe, mở trình duyệt Web và thuê hạ tầng siêu khủng của Amazon, Google, Microsoft ở mức giá theo giờ. Họ cấu hình kiến trúc để các Server này liên kết với nhau an toàn.

### 2. Giải quyết vấn đề gì? (Ví dụ thực tế cụ thể)
*   **Ví dụ 1 - Khả năng co giãn vô hạn (Scalability) của Shopee:** Ngày thường, Shopee chỉ cần 50 Server để phục vụ web. Nhưng đến 0h00 ngày Sale 11/11, lượng người truy cập tăng gấp 100 lần. Kỹ sư Cloud cấu hình tính năng Auto-Scaling (Tự động mở rộng). Đúng 23h59, hệ thống tự động đẻ ra thêm 5,000 Server. Nếu dùng máy chủ vật lý, Shopee sẽ chết đứng. Hết ngày 11/11, hệ thống tự hủy 5,000 Server đó để không tốn tiền điện của công ty.
*   **Ví dụ 2 - Phục hồi thảm họa (Disaster Recovery):** Công ty đặt máy chủ ở Nhật Bản. Đột nhiên một trận động đất lớn làm mất điện toàn thành phố, Data Center sập hoàn toàn. Nhưng vì Kỹ sư Cloud đã cấu hình Multi-Region (Đa vùng), toàn bộ dữ liệu database lập tức được hệ thống Load Balancer chuyển hướng chạy sang cụm máy chủ dự phòng ở Singapore chỉ trong 5 phút. Web công ty vẫn hoạt động bình thường, khách hàng không hề hay biết.

### 3. Cần chuẩn bị gì?
*   **Nền tảng (Platform):** **AWS (Amazon Web Services)** chiếm thị phần lớn nhất thế giới. Học hiểu EC2 (Máy ảo), S3 (Lưu trữ file như Google Drive nhưng cho lập trình), RDS (Database ảo).
*   **Kiến thức Mạng hệ thống:** VPC (Virtual Private Cloud - tạo mạng riêng trên mây), Subnet, Định tuyến (Routing), Firewall.
*   **Điều phối Container:** Nắm rất vững Docker và đặc biệt là **Kubernetes (K8s)** - công nghệ điều phối hệ thống tỷ USD của Google.
*   **Infrastructure as Code (IaC):** Chuyển từ "click chuột tạo Server" sang "viết code tạo Server" bằng **Terraform** hoặc AWS CloudFormation.

---

## 08. KỸ SƯ DevOps (Development & Operations)

### 1. Bản chất (Là gì?)
"Thợ xây đường cao tốc". Trong quá khứ, Team Lập trình (Dev) code xong, vứt một cục file sang cho Team Vận hành (Ops) tự cài đặt lên máy chủ. Sự khác biệt môi trường khiến phần mềm thường xuyên chết ngắc. Kỹ sư DevOps xây dựng các đường ống tự động (CI/CD Pipeline). Dev vừa nhấn nút `git push`, code lập tức chạy tự động qua máy test, đóng gói tự động, và bay thẳng lên Server thật mà không cần con người đụng tay vào.

### 2. Giải quyết vấn đề gì? (Ví dụ thực tế cụ thể)
*   **Ví dụ 1 - Ám ảnh "Lỗi môi trường":** Lập trình viên dùng máy Mac chạy Node.js v18. Máy chủ lại cài Ubuntu chạy Node.js v14. Đưa code lên lỗi toàn bộ. DevOps sử dụng **Docker** để nhốt code, Node.js v18 và hệ điều hành cần thiết vào một cái "Container" (Giống container chở hàng). Cục container này mang đi máy Mac, máy Windows hay máy chủ Cloud chạy đều giống nhau 100%. Xóa sổ câu nói "Works on my machine" (Máy tôi vẫn chạy bình thường mà!).
*   **Ví dụ 2 - Triển khai tự động (Continuous Deployment - CD):** Facebook cập nhật tính năng mới hàng trăm lần mỗi ngày mà web không bao giờ sập. Đó là nhờ DevOps. Kỹ sư cài đặt quy trình CI/CD. Nếu Dev đẩy code chứa lỗi, hệ thống Test tự động (Jenkins/GitLab CI) sẽ phát hiện lỗi, đánh dấu X đỏ tực, chặn không cho đẩy lên Server. Nếu code ngon, hệ thống sẽ đẩy lên Server bằng chiến lược Blue-Green (Tắt server cũ đi từ từ, bật server mới lên từ từ), người dùng không bị gián đoạn dù chỉ 1 giây.

### 3. Cần chuẩn bị gì?
*   **Lõi của hệ thống:** **Linux** (Không biết lệnh Linux thì không thể làm DevOps).
*   **Mã nguồn & CI/CD Tool:** Git, GitHub Actions, GitLab CI/CD, Jenkins.
*   **Công nghệ Container hóa (Vô cùng quan trọng):** **Docker** (Đóng gói ứng dụng) và **Kubernetes** (Quản lý hàng ngàn Docker cùng lúc).
*   **Giám sát Hệ thống (Observability):** Khi có lỗi 500 giữa hàng vạn Microservices, làm sao biết ở đâu? Dùng Prometheus (thu thập chỉ số RAM/CPU), Grafana (vẽ biểu đồ), ELK Stack (Tìm kiếm chữ "Error" trong hàng tỷ dòng log file của server).

---

## 09. KỸ SƯ GenAI (AI Tổng quát / AI Tạo sinh)

### 1. Bản chất (Là gì?)
Nếu Kỹ sư AI truyền thống làm các bài toán "Phân loại" (Đây là chó hay mèo?) thì Kỹ sư GenAI làm bài toán "Tạo sinh" (Hãy vẽ cho tôi một bức ảnh con mèo mặc áo giáp đang đánh đàn). Họ tận dụng sức mạnh khổng lồ của các **Mô hình ngôn ngữ lớn (LLM)** như GPT-4, LLaMA 3, Claude 3.5 để xây dựng các phần mềm có khả năng hiểu, tư duy ngữ cảnh và sáng tạo nội dung y như con người.

### 2. Giải quyết vấn đề gì? (Ví dụ thực tế cụ thể)
*   **Ví dụ 1 - Hệ thống RAG (Retrieval-Augmented Generation) cho Pháp lý:** Một công ty Luật có 100,000 trang hợp đồng và luật các năm. ChatGPT bình thường sẽ nói bậy (Hallucination) hoặc không biết nội bộ công ty. Kỹ sư GenAI biến 100,000 trang này thành dạng số (Vector Embeddings) nhét vào Vector Database. Khi sếp hỏi: "Hợp đồng với công ty Vinamilk năm 2021 có điều khoản phạt vi phạm bao nhiêu %?". Hệ thống sẽ tự dò tìm 3 trang PDF liên quan nhất, ném cho LLM đọc và LLM trả lời "Theo trang 45 hợp đồng ABC, phạt 8%", kèm theo link tải đúng trang PDF đó.
*   **Ví dụ 2 - Đại lý AI tự trị (AI Agents):** Trợ lý ảo thời mới. Bạn gõ: "Chuẩn bị cho tôi slide thuyết trình về tình hình thị trường xe điện Q1/2024". AI Agent sẽ tự động lập kế hoạch: 
    1. Bật trình duyệt, tự động tìm kiếm "Báo cáo xe điện Q1 2024 pdf".
    2. Đọc 10 bài báo bằng công cụ Web Scraper.
    3. Tổng hợp số liệu.
    4. Viết mã Python để vẽ biểu đồ và tạo ra 1 file Powerpoint hoàn chỉnh tải về máy tính bạn. Không cần sự can thiệp của con người.

### 3. Cần chuẩn bị gì?
*   **Kiến thức Nền tảng:** Python, hiểu cấu trúc Transformer, Tokenization.
*   **Kỹ thuật lõi hiện đại:**
    *   **Prompt Engineering:** Kỹ thuật điều khiển AI. Viết Prompt theo cấu trúc Zero-shot, Few-shot, Chain-of-Thought ("Let's think step by step").
    *   **Kiến trúc RAG:** Nắm vững quy trình Chunking (chia nhỏ tài liệu), Embedding (chuyển chữ thành ma trận số).
    *   **Fine-tuning (Tinh chỉnh):** Lấy một LLM mã nguồn mở nhẹ (như Llama 3 8B), huấn luyện thêm trên tập dữ liệu ngành Y khoa để nó trở thành bác sĩ AI thu nhỏ chạy trên máy tính nội bộ không cần Internet.
*   **Bộ khung công cụ (Frameworks):** **LangChain**, LlamaIndex, OpenAI API, HuggingFace.
*   **Cơ sở dữ liệu Vector (Vector DB):** Pinecone, Milvus, ChromaDB, Qdrant (Dùng để lưu trữ ý nghĩa ngữ nghĩa của câu chữ dưới dạng toán học).
