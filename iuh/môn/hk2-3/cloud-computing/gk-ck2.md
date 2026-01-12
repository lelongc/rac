Câu hỏi ôn tập
Câu 1: Thế nào là dịch vụ SaaS, PaaS, IaaS. 

Câu 2: Nêu các ưu và khuyết  điểm của mô hình dịch vụ SaaS? Hãy cho ví dụ về dịch vụ và các nhà cung cấp cụ thể?

Câu 3: Nêu các ưu và khuyết  điểm của mô hình dịch vụ PaaS?

Câu 4: Trình bày các đặc điểm trên mô hình IaaS(compute, storage, network, database, monitoring and autoscale)

Câu 5: Trình bày các tính năng cơ bản của OWNCLOUD?

Câu 6: Trình bày cấu trúc lưu trữ của OWNCLOUD?

Câu 7: Hãy trình bày ngắn gọn các dịch vụ đã triển khai trên nền tảng Google Cloud Platform, Microsoft Azure  và Amazone Web Service

Chào bạn, tệp bạn cung cấp chỉ chứa danh sách câu hỏi ôn tập mà không có câu trả lời. Dựa trên kiến thức chung về điện toán đám mây, tôi xin trả lời các câu hỏi của bạn như sau:

---

### **Câu 1: Thế nào là dịch vụ SaaS, PaaS, IaaS?**

Đây là ba mô hình dịch vụ chính của điện toán đám mây:

*   **SaaS (Software as a Service - Phần mềm như một dịch vụ):** Cung cấp các ứng dụng phần mềm hoàn chỉnh mà người dùng có thể truy cập qua internet, thường thông qua trình duyệt web. Người dùng không cần quản lý hạ tầng, nền tảng hay cài đặt phần mềm.
    *   **Ví dụ:** Gmail, Microsoft 365, Dropbox, Salesforce.

*   **PaaS (Platform as a Service - Nền tảng như một dịch vụ):** Cung cấp một nền tảng cho phép khách hàng phát triển, chạy và quản lý ứng dụng mà không cần xây dựng và duy trì hạ tầng phức tạp. Nhà cung cấp sẽ lo phần hệ điều hành, máy chủ, và mạng.
    *   **Ví dụ:** Heroku, Google App Engine, AWS Elastic Beanstalk.

*   **IaaS (Infrastructure as a Service - Hạ tầng như một dịch vụ):** Cung cấp các tài nguyên điện toán cơ bản được ảo hóa qua internet, bao gồm máy chủ ảo (compute), lưu trữ (storage) và mạng (network). Đây là mô hình linh hoạt nhất, cho phép người dùng toàn quyền kiểm soát hệ điều hành và ứng dụng.
    *   **Ví dụ:** Amazon EC2 (máy chủ ảo), Google Compute Engine, Microsoft Azure VMs.

### **Câu 2: Nêu các ưu và khuyết điểm của mô hình dịch vụ SaaS? Hãy cho ví dụ về dịch vụ và các nhà cung cấp cụ thể?**

*   **Ưu điểm:**
    *   **Chi phí thấp:** Không tốn chi phí đầu tư ban đầu cho phần cứng hoặc bản quyền phần mềm, chỉ trả phí thuê bao.
    *   **Dễ sử dụng:** Không cần cài đặt, bảo trì hay cập nhật; người dùng có thể truy cập ngay lập tức qua trình duyệt.
    *   **Truy cập mọi nơi:** Dữ liệu được lưu trữ trên đám mây, có thể truy cập từ bất kỳ thiết bị nào có internet.
    *   **Tự động cập nhật:** Nhà cung cấp tự động cập nhật và vá lỗi phần mềm.

*   **Khuyết điểm:**
    *   **Ít khả năng tùy chỉnh:** Người dùng bị giới hạn trong các tính năng và cấu hình mà nhà cung cấp đưa ra.
    *   **Phụ thuộc vào nhà cung cấp (Vendor Lock-in):** Việc di chuyển dữ liệu sang một dịch vụ khác có thể khó khăn.
    *   **Yêu cầu kết nối Internet:** Không có internet sẽ không thể sử dụng được dịch vụ.
    *   **Bảo mật:** Dữ liệu của bạn được lưu trữ trên máy chủ của bên thứ ba, gây lo ngại về quyền riêng tư và bảo mật.

*   **Ví dụ về dịch vụ và nhà cung cấp:**
    *   **Email & Office:** Google Workspace (Gmail, Docs), Microsoft 365 (Outlook, Word online).
    *   **CRM (Quản lý quan hệ khách hàng):** Salesforce.
    *   **Lưu trữ file:** Dropbox, Google Drive.
    *   **Hội họp trực tuyến:** Zoom, Google Meet.

### **Câu 3: Nêu các ưu và khuyết điểm của mô hình dịch vụ PaaS?**

*   **Ưu điểm:**
    *   **Phát triển nhanh:** Cung cấp môi trường được xây dựng sẵn, giúp lập trình viên tập trung vào việc viết mã thay vì quản lý hạ tầng.
    *   **Giảm sự phức tạp:** Nhà cung cấp quản lý hệ điều hành, bản vá, và bảo trì, giảm gánh nặng cho đội ngũ phát triển.
    *   **Linh hoạt và có thể mở rộng:** Dễ dàng mở rộng tài nguyên khi ứng dụng phát triển.
    *   **Hỗ trợ đa dạng:** Nhiều nền tảng PaaS hỗ trợ nhiều ngôn ngữ lập trình và framework.

*   **Khuyết điểm:**
    *   **Ràng buộc nhà cung cấp (Vendor Lock-in):** Ứng dụng được xây dựng trên một nền tảng PaaS cụ thể có thể khó di chuyển sang nền tảng khác.
    *   **Giới hạn về tùy chỉnh:** Lập trình viên bị giới hạn bởi các công cụ, ngôn ngữ và hệ điều hành mà nhà cung cấp hỗ trợ.
    *   **Rủi ro bảo mật:** Dù nhà cung cấp bảo mật nền tảng, nhưng lỗi trong mã nguồn ứng dụng vẫn là trách nhiệm của người dùng.

### **Câu 4: Trình bày các đặc điểm trên mô hình IaaS**

Mô hình IaaS cung cấp các khối xây dựng cơ bản cho điện toán đám mây:

*   **Compute (Tính toán):** Cung cấp các máy chủ ảo (Virtual Machines - VMs) với khả năng tùy chọn cấu hình CPU, RAM. Người dùng có toàn quyền kiểm soát hệ điều hành và các phần mềm cài đặt trên đó.
*   **Storage (Lưu trữ):** Cung cấp nhiều loại lưu trữ khác nhau như *Object Storage* (để lưu trữ file, backup), *Block Storage* (dùng làm ổ đĩa cho máy chủ ảo), và *File Storage*.
*   **Network (Mạng):** Cho phép người dùng tạo các mạng ảo (VPC - Virtual Private Cloud), định cấu hình tường lửa (firewall), dải IP, subnet, và cân bằng tải (load balancer) để kết nối và bảo vệ các tài nguyên.
*   **Database (Cơ sở dữ liệu):** Cung cấp dịch vụ cơ sở dữ liệu được quản lý (Managed Database), giúp tự động hóa các tác vụ quản trị như cài đặt, sao lưu, và cập nhật.
*   **Monitoring and Autoscale (Giám sát và Tự động mở rộng):**
    *   **Monitoring:** Cung cấp công cụ để theo dõi hiệu suất (CPU, RAM, network traffic) của các tài nguyên.
    *   **Autoscale:** Tự động tăng hoặc giảm số lượng máy chủ dựa trên các quy tắc được định sẵn (ví dụ: tăng số lượng máy chủ khi CPU sử dụng vượt 80%), giúp tối ưu hiệu suất và chi phí.

### **Câu 5: Trình bày các tính năng cơ bản của OWNCLOUD?**

ownCloud là một nền tảng mã nguồn mở cho phép bạn tự xây dựng một dịch vụ lưu trữ và chia sẻ file tương tự như Google Drive hay Dropbox nhưng trên chính máy chủ của mình.

*   **Lưu trữ và đồng bộ hóa file:** Cho phép tải lên, lưu trữ và đồng bộ file giữa nhiều thiết bị (máy tính, điện thoại) và người dùng.
*   **Chia sẻ file và thư mục:** Dễ dàng chia sẻ file với người dùng khác trong hệ thống hoặc qua một liên kết công khai (có thể đặt mật khẩu và ngày hết hạn).
*   **Truy cập mọi nơi:** Cung cấp giao diện web và ứng dụng cho máy tính/di động để truy cập dữ liệu từ bất cứ đâu.
*   **Bảo mật và kiểm soát:** Vì tự host, bạn có toàn quyền kiểm soát dữ liệu của mình. Hỗ trợ mã hóa dữ liệu trên máy chủ và trên đường truyền.
*   **Lịch, Danh bạ và Mail:** Tích hợp các ứng dụng để đồng bộ Lịch (CalDAV) và Danh bạ (CardDAV).
*   **Khả năng mở rộng:** Có thể thêm nhiều tính năng mới thông qua kho ứng dụng (marketplace) của ownCloud.

### **Câu 6: Trình bày cấu trúc lưu trữ của OWNCLOUD?**

Cấu trúc lưu trữ của ownCloud được thiết kế để tách biệt siêu dữ liệu (metadata) và dữ liệu thực tế (file content):

1.  **Cơ sở dữ liệu (Database):**
    *   ownCloud sử dụng một cơ sở dữ liệu (như MySQL, PostgreSQL) để lưu trữ tất cả thông tin *siêu dữ liệu*.
    *   Siêu dữ liệu bao gồm: cấu trúc cây thư mục, thông tin người dùng, các hoạt động chia sẻ, bình luận, phiên bản file (versioning), và các thông tin quản lý khác.
    *   Việc này giúp truy vấn và quản lý thông tin nhanh chóng mà không cần duyệt qua hệ thống file vật lý.

2.  **Thư mục dữ liệu (Data Directory):**
    *   Đây là nơi nội dung thực tế của các file được lưu trữ trên hệ thống file của máy chủ.
    *   Cấu trúc thư mục này được tổ chức theo người dùng. Mỗi người dùng có một thư mục riêng chứa tất cả các file và thư mục con của họ.
    *   ownCloud cũng lưu trữ các phiên bản cũ của file và file trong thùng rác tại đây.

Sự tách biệt này giúp ownCloud quản lý hiệu quả một lượng lớn file và người dùng, đồng thời hỗ trợ các tính năng phức tạp như chia sẻ và phiên bản.

### **Câu 7: Hãy trình bày ngắn gọn các dịch vụ đã triển khai trên nền tảng Google Cloud Platform, Microsoft Azure và Amazon Web Service**

Đây là ba nhà cung cấp đám mây hàng đầu với hàng trăm dịch vụ. Dưới đây là một số dịch vụ tiêu biểu cho các tác vụ phổ biến:

| Loại dịch vụ | **Amazon Web Services (AWS)** | **Microsoft Azure** | **Google Cloud Platform (GCP)** |
| :--- | :--- | :--- | :--- |
| **Máy chủ ảo** | Amazon EC2 | Azure Virtual Machines | Google Compute Engine (GCE) |
| **Lưu trữ đối tượng** | Amazon S3 | Azure Blob Storage | Google Cloud Storage |
| **Cơ sở dữ liệu SQL** | Amazon RDS | Azure SQL Database | Google Cloud SQL |
| **Cơ sở dữ liệu NoSQL**| Amazon DynamoDB | Azure Cosmos DB | Google Cloud Firestore/Bigtable |
| **Thực thi mã (Serverless)** | AWS Lambda | Azure Functions | Google Cloud Functions |
| **AI / Machine Learning**| Amazon SageMaker | Azure Machine Learning | Google AI Platform / Vertex AI |
| **Mạng riêng ảo** | Amazon VPC | Azure Virtual Network | Google Virtual Private Cloud (VPC)|
| **Containers** | Amazon EKS (Kubernetes) | Azure Kubernetes Service (AKS) | Google Kubernetes Engine (GKE) |
