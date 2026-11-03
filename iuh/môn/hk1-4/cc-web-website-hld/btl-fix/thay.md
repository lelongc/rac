
## PHẦN 1: Ghi lại lời thoại giữa Thầy và Bạn

### 1. Về Lược đồ lớp (Class Diagram), Code First và Kiểm thử (00:00 – 02:15)

* **Thầy:** "...cơ sở dữ liệu có lược đồ lớp. Sơ đồ lớp không có thấy... Lược đồ lớp ở bên đây. Đúng không? Làm gì có cái chuyện mà sơ đồ lớp cho Database. Hiểu không? Em làm Code First hả?"^^
* **Bạn:** "Dạ."^^
* **Thầy:** "Code First như vậy thì cái này học trên lớp rồi, nó phải đi từ cái lược đồ Logical đúng không? `One-to-Many`, `Many-to-Many` rồi `One-to-One` đúng không? Còn cái lược đồ này (lược đồ vật lý) nó phải là `One-to-Many` hết. Hiểu không?"^^
* **Thầy:** "Chương 4 là Phát triển và Triển khai. Như vậy phần triển khai là cài đặt như thế nào đúng không? Rồi cái phần Kiểm thử và Kết quả đạt được. Hiểu không? Kết quả đạt được, kiểm thử em có thể dùng Postman hoặc em dùng Unit Test hay dùng cái gì đó đúng không? Học Công nghệ phần mềm là bao giờ cũng phải có cái chương đó. Thì như vậy em mới có cái trải nghiệm, em rèn luyện để em nâng nó lên thành một cái cuốn khóa luận tốt nghiệp, hiểu không?"^^
* **Thầy:** "Rồi cái đường Sequence (Lược đồ tuần tự) này không thấy cái trục **Lifeline** (đường gạch đứt nét dọc). Đây nè, thời gian sống của đối tượng nè. Không có mấy cái này là người ta đánh rớt từ cái vòng gửi xe à! Rồi Kết luận và hướng phát triển đâu? Kết quả đạt được gộp chung với Chương 4 là *Kiểm thử và Kết quả đạt được* ha. Rồi cái phần Chương 5 (hoặc mục cuối) là về *Kết luận và Hướng phát triển* ha, ghi mấy dòng thôi."^^

### 2. Về In ấn, Phạm vi đề tài và Luồng đi từ Nghiệp vụ ra Sơ đồ (02:16 – 04:30)

* **Thầy:** *(Xem bìa và trang in)* "Bao nhiêu trang đây? Ok, không cần cái tờ này nha. Đơn giản thôi, cái này không cần in màu luôn. In cái tờ bìa kia được rồi ha."^^
* **Thầy:** "Phạm vi đề tài sao không thấy giới thiệu? Đề tài, phạm vi đề tài, bao gồm có những chức năng gì, sử dụng công nghệ là gì... Người ta không biết đề tài em làm cái gì, bao gồm những chức năng gì. Rồi mô tả cái phần cơ bản về đề tài đã làm cho người ta ha."^^
* **Thầy:** "Phạm vi đề tài có nghĩa là: ví dụ cũng là phần mềm quản lý bệnh viện, nhưng mà quản lý tới cấp độ nào? Có quản lý tới hồ sơ bệnh án điện tử không? Có quản lý đến thanh toán phí tự động không? Hiểu không? Đề tài ở mức nào, rồi giới thiệu luôn sơ qua về  **quy trình nghiệp vụ** . Từ cái quy trình nghiệp vụ mới ra  **Use Case** . Chứ Use Case ở đâu ra? Rồi từ Use Case mới đến  **Lược đồ lớp (Class Diagram)** . Và từ Lược đồ lớp mới xác định các thực thể, xác định mối quan hệ thực thể rồi nếu em dùng Database First hay Code First... Code First thì em có phần thiết kế mối quan hệ Logical, tức là  **ERD** ."^^

### 3. Về Cách đặt tên Chương và Lỗi làm tắt ở sơ đồ ERD (04:31 – 07:45)

* **Thầy:** "Chương 3 làm gì có ai đi đặt cái chương là  *'Chương Lược đồ lớp'* ! Chương 1 là gì? Nhớ lại coi. Giới thiệu đúng không?"^^
* **Bạn:** "Dạ."^^
* **Thầy:** "Chương 2: Phân tích thiết kế."^^
* **Bạn:** "Phân tích và thiết kế."^^
* **Thầy:** "Chương 3: Thực hiện, triển khai. Chương 4: Kiểm thử. Đúng không? Em không có lưu ý thành ra em không có rõ. Cái cuốn khóa luận tốt nghiệp nó phải vậy đó."^^
* **Bạn:** "Em đâu biết đâu. Dạ."^^
* **Thầy:** "Chứ ai đi đặt cái chương  *'Lược đồ lớp'* ! Để coi từ từ... Lược đồ tuần tự... tương đối đúng ha. Ok."^^
* **Thầy:** "Rồi cái **ERD** này ở đâu ra cái này? Cái này làm tắt nè, em vô em phang vô luôn nè! Đúng ra là giữa cái này với cái này nó có mối quan hệ, chưa có cái bảng trung gian này đâu. Rồi bắt đầu mới ra cái này. Hai cái tương đương nhưng mà cái này là cái đi sau. Hiểu không? Chứ `Many-to-Many` làm sao mà vẽ được lược đồ cơ sở dữ liệu vật lý, hiểu không? Em làm đúng mà làm tắt! Phải có cái bước trước đó là chưa có cái bảng trung gian này."^^
* **Thầy:** "Ví dụ `Student` với lại `Subject`, là nó có mối quan hệ trực tiếp luôn là `Many-to-Many`. Một `Student` có nhiều `Subject`, một `Subject` có nhiều `Student` được chưa?"^^
* **Bạn:** "Dạ."^^
* **Thầy:** "Triển khai theo phương pháp ERD thì nó ra cái **hình thoi** ở giữa. Và từ cái lược đồ có hình thoi (`Many-to-Many`) đó thì nó mới tách ra là `One-to-Many` và `Many-to-One` (thực thể kết hợp/bảng trung gian). Và từ `One-to-Many` đó mới ra được cái  **Lược đồ vật lý (Physical Diagram)** , tức là lược đồ cài đặt trên cơ sở dữ liệu — là **lược đồ thiết kế** đó. Còn mấy cái ERD trước đó nó vẫn là  **lược đồ phân tích** ."^^

### 4. Về Cấu trúc 4 Chương chuẩn và Lỗi "chỉ quăng hình, không có chữ" (07:46 – 10:30)

* **Thầy:** "Bất cứ một khóa luận nào cũng phải có  *Phân tích thiết kế* , rồi mới đến *Thực hiện* (tức là code đó), *Triển khai* (là cài đặt), xong rồi đến *Kiểm thử* — đúng theo các giai đoạn của phát triển phần mềm: Lấy yêu cầu **$\rightarrow$** Phân tích **$\rightarrow$** Thiết kế **$\rightarrow$** Code **$\rightarrow$** Cài đặt **$\rightarrow$** Kiểm thử. Bây giờ chia làm **4 chương** cho nó gọn nha, không có nhiều:"^^
  * **Chương 1:** Giới thiệu (Đề tài, tổng quan, phạm vi đề tài)^^.
  * **Chương 2:** Phân tích và Thiết kế^^.
  * **Chương 3:** Thực hiện và Triển khai^^.
  * **Chương 4:** Kiểm thử và Kết quả đạt được^^.
  * *(Phần Kết luận và Hướng phát triển để ở cuối, khỏi tách thành chương lớn cũng được)*^^.
* **Thầy:** "Trời, tự nhiên cái lên tới Chương 7! Từ Chương 3, Chương 5, Chương 6... Lược đồ vật lý Chương 6..."^^
* **Bạn:** "Tại vì em nghĩ là cái kết quả... Chương 6 là cái Physical..."^^
* **Thầy:** "Ờ, mà một cái chương xong rồi paste cái hình vô không có nói gì hết trơn! Em làm vầy là thầy Chiến chửi thầy chết! Ổng chửi thầy banh xác luôn á! Mà các bạn không chịu sửa là thầy đưa cho thầy Chiến chấm nha, cho ổng khỏi chửi thầy."^^
* **Thầy:** "Em thấy cái cuốn của bạn kia làm còn đỡ hơn em. Hai em thì rất giỏi về kỹ thuật, trình bày (vẽ sơ đồ) thì đúng hết nhưng mà cuốn khóa luận phải có chữ nghĩa, **phải có cái phần thịt, có phần xương. Em vô em quăng cái phần xương không à!** Cái chương gì mà có cái hình không à, là sao?"^^
* **Bạn:** "Dạ, vậy em trình bày sao cái chỗ này cho nó hợp lý thầy? Cái chỗ này em nên trình bày sao?"^^
* **Thầy:** "Cái này là Lược đồ vật lý đúng không? Để thầy nói cho nghe, cái này có phải là lược đồ thiết kế không? Hay là lược đồ phân tích?"^^
* **Bạn:** "Thiết kế ạ."^^
* **Thầy:** "Cái này là lược đồ thiết kế, đúng! Thì em để trong chương Thiết kế (Chương 2: Phân tích thiết kế)."^^

### 5. Kiểm tra kiến thức Phân tích vs. Thiết kế và Lời dặn cuối (10:31 – 12:15)

* **Thầy:** "Rồi 2 cái Lược đồ tuần tự (Sequence Diagram) nó nằm ở trong chương nào?"^^
* **Bạn:** "Thiết kế ạ, Chương 2."^^
* **Thầy:** "Đúng rồi, chương Thiết kế. **Cái gì mà mình dựa vào đó để thực hiện (code) là Thiết kế. Mà để ra được cái bản thiết kế đó, trước đó phải Phân tích.** Trong UML người ta hỏi mình muốn làm Phân tích hay Thiết kế. Vậy Use Case là phân tích hay thiết kế?"^^
* **Bạn:** "Use Case là phân tích thầy."^^
* **Thầy:** "Đúng rồi! Lược đồ lớp (Class Diagram) là phân tích hay thiết kế?"^^
* **Bạn:** "Dạ thiết kế thầy."^^
* **Thầy:** "Đúng rồi, chính xác! Em hiểu hết, vậy tại sao em trình bày gì mà như thế này không ai chấp nhận được! Và em nên nhớ này, ở trường đại học,  **cuốn báo cáo tỷ trọng điểm nó cao hơn 50%** . Ngay cả khóa luận tốt nghiệp nha, chỉ cần em sai một chữ thôi, sai ngữ pháp thôi là người ta trả cuốn này về luôn. Tụi em phải rèn luyện nha. Còn không là thầy giao cho thầy Chiến với thầy Minh chấm nha."^^
* **Bạn:** "Dạ thôi vậy để em sửa lại ha... Bốn chương..."^^
* **Thầy:** "Cái này là một cái cơ hội để mình trải nghiệm, rèn luyện sau này... Bạn này về mặt kỹ thuật là nắm hết á, nhưng mà trình bày không thể chấp nhận được!"^^

*(Đoạn cuối từ 12:15 – 14:43 là lúc bạn ra ngoài hành lang trao đổi với các bạn cùng lớp về việc đi xuống phòng máy lúc 9h và chia sẻ chuyện lượm nhầm mẫu báo cáo cũ trên mạng nên chia chương bị sai)*^^.
