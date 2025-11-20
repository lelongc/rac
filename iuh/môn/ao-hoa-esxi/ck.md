```

```

### Câu 1: So sánh VMware ESXi và VMware Workstation

| Tiêu chí             | VMware ESXi                                                                                                     | VMware Workstation                                                                                               |
| :------------------- | :-------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------- |
| **Kiến trúc**        | **Bare-metal (Type 1 Hypervisor):** Cài đặt trực tiếp lên phần cứng máy chủ vật lý, không cần hệ điều hành nền. | **Hosted (Type 2 Hypervisor):** Cài đặt như một phần mềm ứng dụng trên nền hệ điều hành có sẵn (Windows, Linux). |
| **Hiệu suất**        | **Rất cao:** Do truy xuất trực tiếp phần cứng, không qua lớp trung gian OS.                                     | **Trung bình/Thấp:** Do phải đi qua lớp OS của máy trạm (Host OS) nên tốn tài nguyên và có độ trễ.               |
| **Quản lý**          | Quản lý tập trung qua vCenter Server hoặc giao diện Web (Host Client).                                          | Quản lý trực tiếp trên giao diện phần mềm tại máy cài đặt.                                                       |
| **Phạm vi ứng dụng** | Môi trường doanh nghiệp (Enterprise), trung tâm dữ liệu (Data Center), chạy các Server quan trọng 24/7.         | Môi trường cá nhân, thử nghiệm (Lab), phát triển phần mềm (Dev/Test), học tập.                                   |

---

### Câu 2: Kiến trúc tổng quát và thành phần chính của VMware ESXi

Kiến trúc của ESXi được thiết kế tối giản để đảm bảo hiệu năng và bảo mật.

**Các thành phần chính:**

1. **VMkernel:**
   - **Vai trò:** Là nhân (kernel) của hệ điều hành ảo hóa, thành phần quan trọng nhất.
   - **Chức năng:** Trực tiếp quản lý phần cứng (CPU, RAM, Disk, Network) và lập lịch (scheduling) tài nguyên cho các máy ảo. Nó đóng vai trò cầu nối giữa VM và phần cứng vật lý.
2. **Virtualization Layer (Lớp ảo hóa):**
   - **Vai trò:** Tạo ra môi trường ảo độc lập.
   - **Chức năng:** Cung cấp các thiết bị phần cứng ảo (vCPU, vRAM, vSwitch...) cho từng máy ảo, giúp máy ảo "nghĩ" rằng nó đang chạy trên máy thật.
3. **User World (Management Agents):**
   - **Vai trò:** Môi trường quản lý.
   - **Chức năng:** Chứa các tiến trình quản trị như `hostd` (quản lý máy chủ), `vpxa` (kết nối với vCenter), giúp quản trị viên cấu hình ESXi thông qua giao diện dòng lệnh hoặc giao diện web.
4. **Hardware Drivers:**
   - Các trình điều khiển thiết bị được tích hợp vào VMkernel để giao tiếp với phần cứng vật lý.

---

### Câu 3: Sơ đồ kiến trúc VMware ESXi Server

![1763620296629](image/ck/1763620296629.png)
**Giải thích sơ đồ:**

- **Tầng dưới cùng (Hardware):** Là máy chủ vật lý (CPU, RAM, NIC, HBA).
- **Tầng giữa (Hypervisor - ESXi):** VMkernel chạy trực tiếp trên Hardware. Nó kiểm soát mọi yêu cầu từ trên xuống. Bên cạnh VMkernel là các Management Agents để người dùng điều khiển.
- **Tầng trên cùng (Virtual Machines):** Các máy ảo chạy trên nền tảng ảo hóa. Chúng không tương tác trực tiếp với phần cứng mà phải đi qua VMkernel.

---

### Câu 4: Cơ chế quản lý tài nguyên trên ESXi

**Các loại tài nguyên quản lý:** CPU, Memory (RAM), Storage (Disk I/O), và Network (Bandwidth).

**Các khái niệm quản lý tài nguyên:**

1. **Resource Pool (Bể tài nguyên):**
   - Là một phương pháp gom nhóm tài nguyên. Bạn có thể chia tổng tài nguyên của máy chủ thành các "bể" nhỏ (ví dụ: Bể cho Kế toán, Bể cho IT) và gán các VM vào đó để dễ quản lý phân cấp.
2. **Reservation (Đặt trước - Đảm bảo tối thiểu):**
   - Là lượng tài nguyên **tối thiểu** được đảm bảo dành riêng cho một VM hoặc Resource Pool.
   - _Ví dụ:_ Reservation 4GB RAM nghĩa là VM luôn luôn có sẵn 4GB để dùng, hệ thống không bao giờ lấy đi, ngay cả khi VM đang tắt (ở một số cấu hình) hoặc rảnh rỗi.
3. **Limit (Giới hạn - Mức trần):**
   - Là lượng tài nguyên **tối đa** mà VM được phép sử dụng.
   - _Ví dụ:_ Limit 2GHz CPU. Dù máy chủ vật lý còn dư rất nhiều CPU, VM này cũng không bao giờ được chạy quá 2GHz.
4. **Shares (Cổ phần - Độ ưu tiên):**
   - Chỉ có tác dụng khi hệ thống bị **tranh chấp tài nguyên** (quá tải).
   - VM nào có chỉ số Shares cao hơn (High) sẽ được ưu tiên cấp phát tài nguyên nhiều hơn so với VM có Shares thấp (Low) khi tài nguyên khan hiếm.

---

### Câu 5: Cơ chế phân phối CPU và RAM

**1. Cơ chế phân phối:**

- **CPU:** ESXi sử dụng bộ lập lịch (Scheduler) để chia nhỏ thời gian sử dụng CPU vật lý thành các lát cắt (time slices) và phân phối cho các vCPU của máy ảo.
- **RAM:** ESXi cấp phát RAM khi VM yêu cầu. Nếu RAM vật lý cạn kiệt, ESXi sử dụng các kỹ thuật thu hồi bộ nhớ như: _Transparent Page Sharing (TPS)_ (chia sẻ trang nhớ giống nhau), _Ballooning_ (vay mượn RAM từ VM rảnh), _Compression_ (nén RAM), hoặc _Swapping_ (chuyển RAM xuống ổ cứng).

**2. Vai trò của VMkernel:**

- VMkernel hoạt động như một "Cảnh sát giao thông". Nó nhận tất cả các yêu cầu tính toán từ hàng loạt máy ảo, sắp xếp hàng đợi và quyết định máy ảo nào được truy xuất vào CPU/RAM vật lý tại thời điểm nào dựa trên chính sách đã cấu hình (Shares, Reservation).

**3. Khi nhiều VM yêu cầu cùng một tài nguyên (Tranh chấp - Contention):**

- Nếu tổng yêu cầu < Tài nguyên vật lý: Mọi VM đều được đáp ứng đầy đủ.
- Nếu tổng yêu cầu > Tài nguyên vật lý (Nghẽn):
  - VMkernel sẽ kiểm tra **Reservation** trước để đảm bảo mức tối thiểu cho các VM quan trọng.
  - Phần tài nguyên còn lại sẽ được chia dựa trên tỷ lệ **Shares**. VM có Shares `High` sẽ nhận được tài nguyên gấp đôi `Normal` và gấp 4 lần `Low`.

Chào bạn, dưới đây là nội dung trả lời tiếp theo cho các câu hỏi từ 6 đến 10, tập trung vào kiến trúc và bảo mật của VMware ESXi và Hyper-V.

---

### Câu 6: Sơ đồ và Quản lý tài nguyên (CPU, RAM, Storage)

![1763621371143](image/ck/1763621371143.png)

**Giải thích các thành phần trong sơ đồ:**

1. **Tài nguyên Vật lý (Physical Resources):** Đây là phần cứng thật (CPU Cores, RAM module, Ổ cứng HDD/SSD).
2. **Bộ lập lịch và quản lý (Resource Scheduler - VMkernel):** Nằm ở giữa.
   - **CPU Scheduler:** Chia nhỏ thời gian xử lý của CPU vật lý và gán cho các vCPU của máy ảo.
   - **Memory Manager:** Quản lý bảng trang nhớ (Page table), ánh xạ RAM ảo của VM sang RAM vật lý. Sử dụng kỹ thuật _Ballooning_ để thu hồi RAM khi thiếu.
   - **Storage Stack:** Quản lý hệ thống file VMFS, điều phối luồng dữ liệu đọc/ghi (I/O) xuống ổ cứng.
3. **Tài nguyên Ảo (Virtual Resources):** Là những gì hệ điều hành máy ảo nhìn thấy (ví dụ: VM thấy mình có 4GB RAM, nhưng thực tế là do VMkernel ánh xạ từ phần cứng lên).

---

### Câu 7: Các mối đe dọa bảo mật trong hệ thống ảo hóa

**1. Các mối đe dọa chính:**

- **VM Escape (Thoát khỏi máy ảo):** Đây là mối nguy hiểm nghiêm trọng nhất. Tin tặc chiếm quyền kiểm soát một máy ảo (Guest), sau đó lợi dụng lỗ hổng của lớp ảo hóa để "thoát" ra ngoài và tấn công trực tiếp vào máy chủ vật lý (Host) hoặc các VM khác.
- **VM Hopping:** Tin tặc tấn công một máy ảo yếu, sau đó dùng nó làm bàn đạp để nhảy sang tấn công các máy ảo khác nằm trên cùng một máy chủ vật lý (do dùng chung vSwitch hoặc cấu hình mạng lỏng lẻo).
- **Resource Exhaustion (Tấn công từ chối dịch vụ - DoS):** Một máy ảo bị nhiễm mã độc cố tình chiếm dụng 100% CPU/RAM/Disk I/O, khiến máy chủ vật lý bị treo và làm tê liệt toàn bộ các máy ảo khác.
- **Rogue VM (Máy ảo lạ):** Kẻ xấu tạo ra một máy ảo trái phép trong hệ thống để đánh cắp dữ liệu hoặc nghe lén luồng mạng.

**Ví dụ minh họa:**
Một Web Server (VM1) bị lộ lỗ hổng SQL Injection. Hacker xâm nhập VM1. Nếu ESXi chưa được vá lỗi bảo mật, hacker khai thác lỗi tràn bộ đệm của ESXi từ VM1 để chiếm quyền `root` của ESXi Host. Từ đó, hacker xóa sạch toàn bộ các VM khác (Database, Mail...) đang chạy trên Host đó.

---

### Câu 8: Cơ chế và phương pháp bảo mật chính trên ESXi

**1. Cơ chế bảo vệ:**

- **Bảo vệ Hệ thống (Host Level):**
  - **Lockdown Mode:** Chế độ này chặn mọi truy cập điều khiển từ xa trực tiếp vào Host, buộc quản trị viên phải đi qua vCenter Server (nơi có kiểm soát quyền chặt chẽ hơn).
  - **ESXi Firewall:** Tường lửa tích hợp sẵn chặn các cổng (port) không cần thiết, chỉ mở các port dịch vụ quản lý.
- **Bảo vệ Mạng (Network Level):**
  - **vLAN (Virtual LAN):** Phân tách các luồng dữ liệu (ví dụ: traffic quản lý tách biệt hoàn toàn với traffic của máy ảo).
  - **Security Policy trên vSwitch:** Chặn các chế độ nguy hiểm như _Promiscuous Mode_ (chặn nghe lén) và _MAC Address Changes_ (chặn giả mạo MAC).
- **Bảo vệ Máy ảo (VM Level):**
  - **VMware Tools:** Cập nhật driver và bản vá lỗi thường xuyên.
  - **UEFI Secure Boot:** Đảm bảo máy ảo chỉ khởi động các OS đã được xác thực, chống lại rootkit.

**2. Công cụ hỗ trợ:**

- **vCenter Server:** Quản lý tập trung, phân quyền (Role-based Access Control).
- **VMware NSX:** Giải pháp bảo mật mạng nâng cao (Micro-segmentation).

---

### Câu 9: Sơ đồ kiến trúc bảo mật trên ESXi Server

![1763621645307](image/ck/1763621645307.png)

**Giải thích các lớp bảo vệ:**

1. **Management Interface Layer (Lớp quản lý):** Kiểm soát ai được login vào hệ thống. Sử dụng mã hóa (SSL/TLS) cho các kết nối vSphere Client/Web Client.
2. **Network Layer (Lớp mạng):** Sử dụng vSwitch và Firewall ảo để kiểm soát luồng gói tin ra/vào Host và giữa các VM.
3. **Host/Hypervisor Layer (Lớp lõi):** Nơi VMkernel hoạt động. Được bảo vệ bằng cách tắt SSH, tắt Shell khi không dùng, và chỉ chạy các service tối thiểu (giảm bề mặt tấn công).
4. **Hardware Layer (Lớp phần cứng):** Sử dụng TPM (Trusted Platform Module) để mã hóa và xác thực tính toàn vẹn của phần cứng khi khởi động.

---

### Câu 10: Kiến trúc tổng quan của Hyper-V

**1. Kiến trúc tổng quan:**
Hyper-V sử dụng kiến trúc **Microkernelized (Vi nhân)** loại 1 (Bare-metal). Điểm đặc biệt là Hyper-V dựa vào một phân vùng đặc biệt gọi là "Parent Partition" để quản lý driver thiết bị.

**2. Các thành phần chính và vai trò:**

- **Hypervisor Layer (Lớp siêu giám sát):** Chạy trực tiếp trên phần cứng (Ring -1). Nó quản lý việc phân chia CPU và bộ nhớ cho các phân vùng.
- **Root Partition (Parent Partition - Phân vùng cha):**
  - Đây là hệ điều hành Windows Server đầu tiên được cài đặt (chính là OS bạn dùng để bật Hyper-V).
  - **Vai trò:** Quản lý ngăn xếp ảo hóa (Virtualization Stack), chứa các trình điều khiển thiết bị thực (Drivers) và tạo/quản lý các phân vùng con.
- **Child Partitions (Guest Partitions - Phân vùng con):**
  - Đây chính là các Máy ảo (VM).
  - **Vai trò:** Chạy hệ điều hành khách (Guest OS). Các VM này không truy cập trực tiếp phần cứng mà giao tiếp qua VMBus.
- **VMBus:**
  - **Vai trò:** Kênh liên lạc tốc độ cao giữa Phân vùng cha và Phân vùng con để truyền tải các yêu cầu phần cứng (như ghi đĩa, gửi gói tin mạng).

### Câu 11: So sánh Kiến trúc ảo hóa Hyper-V và VMware ESXi

**1. Bảng so sánh chi tiết:**

| **Tiêu chí**               | **VMware ESXi**                                                                                              | **Microsoft Hyper-V**                                                                                                               |
| -------------------------- | ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Kiến trúc Lõi (Kernel)** | **Monolithic (Nguyên khối):**Các driver thiết bị được tích hợp trực tiếp vào trong VMkernel.                 | **Microkernelized (Vi nhân):**Driver thiết bị nằm ở phân vùng cha (Parent Partition/Management OS), không nằm trong lớp Hypervisor. |
| **Quản lý VM**             | Quản lý qua**vCenter Server**(tập trung) hoặc Host Client (đơn lẻ). Giao diện web là chủ đạo.                | Quản lý qua**System Center (SCVMM)**hoặc**Hyper-V Manager** . Giao diện Windows native là chủ đạo.                                  |
| **Tính năng bảo mật**      | Sử dụng VM Encryption, Secure Boot, TPM 2.0. Mô hình phân quyền RBAC rất chặt chẽ.                           | Nổi bật với**Shielded VMs**(mã hóa VM để Admin Host không xem được dữ liệu bên trong), Guarded Fabric.                              |
| **Khả năng mở rộng**       | Rất cao, thường dẫn đầu về hỗ trợ số lượng vCPU/RAM khổng lồ cho 1 VM. Chuẩn công nghiệp cho Enterprise lớn. | Đã tiệm cận ESXi, hỗ trợ tốt cho hầu hết nhu cầu doanh nghiệp vừa và lớn.                                                           |

**2. Đánh giá ưu/nhược điểm của Hyper-V so với ESXi:**

- **Ưu điểm của Hyper-V:**
  - **Chi phí:** Đi kèm miễn phí với bản quyền Windows Server. Tiết kiệm chi phí đáng kể nếu doanh nghiệp đã dùng hệ sinh thái Microsoft.
  - **Dễ sử dụng:** Giao diện quen thuộc với quản trị viên Windows.
  - **Tương thích:** Hỗ trợ driver phần cứng cực tốt vì chạy trên nền Windows.
- **Nhược điểm:**
  - **Hiệu suất:** Do kiến trúc Microkernelized, các lệnh I/O phải đi qua phân vùng cha (Parent Partition) nên độ trễ có thể cao hơn ESXi (truy cập trực tiếp) một chút.
  - **Bảo trì:** Cần vá lỗi (patch) cả hệ điều hành Windows ở phân vùng cha, gây gián đoạn nhiều hơn (trừ khi có Cluster).

---

### Câu 12: Sơ đồ kiến trúc Hyper-V và giải thích

**Sơ đồ kiến trúc Hyper-V**

![1763621826189](image/ck/1763621826189.png)

**Giải thích cách hoạt động:**

1. **Hypervisor:** Là lớp phần mềm mỏng chạy trực tiếp trên phần cứng, chia cắt tài nguyên vật lý thành các phân vùng (Partition).
2. **Parent Partition (Phân vùng cha):** Đây là hệ điều hành quản lý (Windows Server). Nó chứa các trình điều khiển thiết bị thực và **VSP (Virtualization Service Provider)** .
3. **Child Partition (Phân vùng con - Máy ảo):** Chứa **VSC (Virtualization Service Client)** . Khi máy ảo cần ghi dữ liệu xuống đĩa cứng, nó không làm trực tiếp mà gửi yêu cầu qua đường ống tốc độ cao gọi là **VMBus** .
4. **VMBus:** Nhận yêu cầu từ VSC (ở máy con), chuyển sang VSP (ở máy cha). Máy cha sẽ dùng driver thực để ghi xuống ổ cứng vật lý rồi trả kết quả lại.

---

### Câu 13: Tổng quan về Ảo hóa

1. Ảo hóa là gì?
   Là công nghệ cho phép tạo ra các phiên bản ảo (virtual) của tài nguyên máy tính (như phần cứng, hệ điều hành, thiết bị lưu trữ) trên một nền tảng vật lý duy nhất. Nó giúp một máy chủ vật lý chạy được nhiều máy chủ ảo độc lập cùng lúc.
2. **Các loại ảo hóa:**
   - **Ảo hóa Máy chủ (Server Virtualization):** Phổ biến nhất (Hyper-V, ESXi).
   - **Ảo hóa Mạng (Network Virtualization):** VLAN, SDN.
   - **Ảo hóa Lưu trữ (Storage Virtualization):** SAN, vSAN.
   - **Ảo hóa Ứng dụng (Application Virtualization):** Docker, App-V.
   - **Ảo hóa Máy trạm (Desktop Virtualization - VDI).**
3. **Ưu điểm:**
   - **Tiết kiệm chi phí:** Giảm số lượng máy chủ vật lý cần mua, giảm tiền điện, điều hòa.
   - **Linh hoạt:** Triển khai máy chủ mới trong vài phút thay vì vài ngày.
   - **An toàn & Khôi phục:** Dễ dàng sao lưu (Backup), chụp nhanh (Snapshot) và khôi phục thảm họa.

---

### Câu 14: Các loại tài nguyên quản lý trên Hyper-V

**Các loại tài nguyên chính:**

1. **CPU (Bộ vi xử lý):** Quản lý dưới dạng vCPU. Có thể giới hạn số lượng core và tỷ lệ sử dụng cho mỗi VM.
2. **RAM (Bộ nhớ):** Quản lý dung lượng bộ nhớ cấp cho VM. Có thể là tĩnh (Static) hoặc động (Dynamic).
3. **Disk (Lưu trữ):** Sử dụng các file định dạng `.vhdx` hoặc `.vhd` để làm ổ cứng ảo. Quản lý dung lượng và tốc độ đọc ghi (IOPS).
4. **Network (Mạng):** Sử dụng **vSwitch** (Virtual Switch) để kết nối VM ra mạng ngoài hoặc kết nối các VM với nhau.

**Vai trò của việc quản lý tài nguyên:**

- **Đảm bảo hiệu suất:** Ngăn chặn một VM chiếm dụng hết tài nguyên làm treo các VM khác.
- **Tối ưu chi phí:** Tận dụng tối đa phần cứng, không để lãng phí tài nguyên nhàn rỗi.
- **Cam kết chất lượng dịch vụ (QoS):** Đảm bảo các VM quan trọng (như Database) luôn có đủ tài nguyên để chạy mượt mà.

---

### Câu 15: Phân bổ và Tối ưu hóa tài nguyên trong Hyper-V

**1. Cách phân bổ (Allocation):**

- **CPU:** Vào Settings của VM -> Processor -> Chọn số lượng vCPU (Number of virtual processors).
  - _Lưu ý:_ Không nên gán tổng vCPU của các VM vượt quá số luồng (Threads) của CPU vật lý quá nhiều (tỷ lệ an toàn 2:1 hoặc 4:1).
- **RAM:** Vào Settings -> Memory -> Điền số RAM khởi động (Startup RAM).

**2. Các tính năng Tối ưu hóa (Optimization):**

- **Dynamic Memory (Bộ nhớ động):** Đây là tính năng quan trọng nhất để tiết kiệm RAM.
  - _Startup RAM:_ RAM khi bật máy.
  - _Minimum RAM:_ Mức thấp nhất VM có thể co lại khi hệ thống thiếu RAM.
  - _Maximum RAM:_ Mức tối đa VM được phép dùng (để tránh tràn bộ nhớ Host).
  - _Memory Buffer:_ Phần trăm bộ nhớ đệm dự phòng để cấp ngay khi VM cần gấp (mặc định 20%).
- **Resource Control (Kiểm soát tài nguyên - CPU):**
  - _Virtual Machine Reserve (Dự trữ):_ % CPU tối thiểu luôn dành riêng cho VM này.
  - _Virtual Machine Limit (Giới hạn):_ % CPU tối đa VM được dùng (ví dụ: set 50% để VM không bao giờ làm nóng máy quá mức).
  - _Relative Weight (Trọng số):_ Độ ưu tiên (mặc định 100). VM nào có Weight cao hơn sẽ được ưu tiên dùng CPU khi hệ thống quá tải.
