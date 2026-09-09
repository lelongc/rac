# BÍ KÍP TÂM LÝ & KỸ NĂNG ỨNG BIẾN KHI BỊ HỎI CÂU KHÓ
### CHIẾN THUẬT PHÒNG THI ĐẠT ĐIỂM CAO DÀNH CHO SINH VIÊN IUH

> **Tình huống thực tế:** Rất nhiều sinh viên code rất tốt nhưng khi vào phòng thi bị giảng viên hỏi dồn dập thì mất bình tĩnh, run rẩy, ấp úng và bị đánh giá thấp. Ngược lại, có những bạn nắm chắc tâm lý, biết cách ứng biến thông minh thì luôn đạt **điểm 9 - 10**.  
> File này chia sẻ toàn bộ các "mẹo thực chiến" giúp bạn làm chủ bàn thi vấn đáp từ giây đầu tiên!

---

## 🧘 1. TÂM LÝ PHÒNG THI: GIẢNG VIÊN THỰC SỰ MUỐN GÌ?

Trước khi vào thi, hãy ghi nhớ 3 sự thật này:
1. **Giảng viên không phải là "kẻ thù" muốn đánh trượt bạn:** Thầy cô hỏi khó là để kiểm tra xem bạn **có thực sự hiểu dự án hay không**, hay là thuê người làm hộ, hoặc copy code mà không hiểu.
2. **Thái độ quyết định 50% điểm số:** Một sinh viên ăn mặc gọn gàng, dạ thưa lễ phép, tự tin nhìn thẳng, nhận lỗi khiêm tốn và biết lắng nghe sẽ luôn được chấm nương tay hơn một sinh viên cộc lốc hoặc tranh cãi tay đôi với thầy cô.
3. **Không ai biết hết 100% mọi thứ:** Kể cả lập trình viên đi làm 5 năm đôi khi cũng phải tra Google. Điều quan trọng không phải là bạn thuộc làu làu từng ký tự, mà là bạn **hiểu tư duy luồng dữ liệu (Architecture & Data Flow)**.

---

## ⏱️ 2. NGHỆ THUẬT "CÂU GIỜ THÔNG MINH" KHI BỊ BẤT NGỜ (10 - 15 GIÂY)

Khi giảng viên đưa ra một câu hỏi hóc búa mà bạn chưa nghĩ ra câu trả lời ngay, **tuyệt đối không được im lặng** (im lặng quá 5 giây sẽ tạo cảm giác bạn không biết gì). Hãy áp dụng các câu thoại câu giờ chuyên nghiệp:

### Câu thoại 1 (Chuyên nghiệp & Điềm tĩnh):
> 🗣️ *"Dạ thưa thầy/cô, câu hỏi này của thầy/cô chạm đúng vào một bài toán kiến trúc mà nhóm em đã cân nhắc rất nhiều trong quá trình thiết kế hệ thống..."*  
*(Nói câu này mất 5 giây, não bạn có thời gian định thần lại để nhớ kiến thức).*

### Câu thoại 2 (Chuyển sang hành động mở máy tính):
> 🗣️ *"Dạ thưa thầy/cô, để câu trả lời được chính xác và trực quan nhất, em xin phép được mở đúng đoạn mã nguồn trong IntelliJ lên để vừa chỉ vào code vừa giải thích cho thầy/cô nghe ạ."*  
*(Trong lúc nhấn `Double Shift` mở file, bạn có thêm 5-7 giây để đọc lướt lại code).*

### Câu thoại 3 (Nhờ giảng viên làm rõ câu hỏi):
> 🗣️ *"Dạ thưa thầy/cô, ý thầy/cô đang muốn hỏi về cách xử lý luồng dữ liệu ở tầng Controller hay là thuật toán truy vấn ở tầng Service/Repository ạ?"*  
*(Vừa thể hiện mình hiểu sâu các tầng, vừa hướng giảng viên vào phần mình nắm chắc nhất).*

---

## 🚨 3. XỬ LÝ "HIỆU ỨNG DEMO" (DEMO EFFECT - ĐỘT NHIÊN BỊ LỖI KHI ĐANG THI)

Đây là cơn ác mộng lớn nhất: Ở nhà chạy mượt mà, nhưng vừa bước lên bàn thi bấm nút thì web báo lỗi hoặc quay tròn!  
**Đừng hoảng loạn! Hãy làm đúng 4 bước sau:**

```
[Bị lỗi trên màn hình]
       │
       ▼
Bước 1: Không bấm chuột loạn xạ! Hít sâu 1 hơi, mỉm cười nhẹ.
       │
       ▼
Bước 2: Nhấn phím F12 ➔ Mở tab Console hoặc Network.
       │
       ▼
Bước 3: Nhìn vào mã lỗi HTTP (401, 403, 500) hoặc thông báo đỏ.
       │
       ▼
Bước 4: Giải thích bằng chuyên môn đỉnh cao trước khi sửa.
```

### Các tình huống lỗi hay gặp nhất và cách "chém gió" cứu nguy:
1. **Lỗi `401 Unauthorized` hoặc `403 Forbidden`:**
   - **Cách giải thích:** *"Dạ thưa thầy/cô, đây là cơ chế bảo mật của Token JWT. Vì em đã đăng nhập từ sáng để chuẩn bị thi nên thời hạn sống của Token (`exp: 1h`) đã hết hạn. Hệ thống Spring Security đã chặn lại đúng theo thiết kế Stateless để bảo vệ dữ liệu. Em chỉ cần đăng nhập lại là xong ngay ạ."*  
   ➔ Giảng viên sẽ khen bạn hiểu cơ chế bảo mật JWT!
2. **Lỗi trùng Username hoặc bài viết không hiện:**
   - **Cách giải thích:** *"Dạ do nhóm em vừa chạy bài test tự động trước đó nên dữ liệu này đã tồn tại trong CSDL. Em xin phép đổi sang một tên mới để demo luồng chuẩn ạ."*
3. **Trình duyệt bị đơ cache:**
   - **Cách xử lý:** Nhấn tổ hợp phím **`Ctrl + Shift + R`** (Hard Reload) hoặc mở cửa sổ Ẩn danh (`Ctrl + Shift + N`).

---

## 🎯 4. KỸ THUẬT "CHUYỂN HƯỚNG KHÉO LÉO" (PIVOT) VỀ VÙNG TỰ TIN

Nếu giảng viên hỏi vào một ngóc ngách code quá sâu mà bạn lỡ quên:
1. **Trả lời ngắn gọn bản chất chung:** Trả lời những gì mình biết về mặt ý niệm (1-2 câu).
2. **Bắc cầu (Bridge) sang phần thế mạnh:** Khéo léo nối sang phần mình học thuộc lòng:
   - *"Dạ phần này chủ yếu là logic hỗ trợ, nhưng điểm cốt lõi nhất sau khi xử lý xong bước này là hệ thống sẽ chuyển dữ liệu sang tầng **Spring Security để mã hóa JWT HS512**..."*
   - *"Dạ ở phần này, điều mà nhóm em tâm đắc nhất là việc áp dụng **MapStruct** và **Xử lý ngoại lệ tập trung @ControllerAdvice** để dữ liệu trả về luôn tuân thủ chuẩn `ApiResponse`..."*
3. Lúc này, giảng viên sẽ bị cuốn theo chủ đề mới mà bạn vừa mở ra và hỏi tiếp vào phần bạn đang nắm chắc như lòng bàn tay!

---

## 🚫 5. NHỮNG ĐIỀU TUYỆT ĐỐI KHÔNG NÊN NÓI TRƯỚC HỘI ĐỒNG

| ❌ Câu Nói "Tự Sát" (Bị Trừ Điểm Nặng) | ✅ Câu Nói Thông Minh Thay Thế |
| :--- | :--- |
| *"Dạ phần này em không biết, do bạn Dương / bạn Dũng làm chứ không phải em làm."* | *"Dạ trong phân công nhóm, bạn Dương phụ trách chính phần này, nhưng em cũng đã nắm được luồng tổng thể là nó chạy từ Controller sang Service để..."* |
| *"Dạ cái này em copy trên mạng về chạy được là được chứ em cũng không rõ."* | *"Dạ phần này nhóm em tham khảo kiến trúc chuẩn từ tài liệu chính thức của Spring Boot và thư viện Nimbus JOSE JWT, sau đó tùy biến lại cho phù hợp với đề tài BTL."* |
| *"Thầy/cô nói sai rồi, code em vẫn chạy bình thường mà!"* | *"Dạ thưa thầy/cô, có thể cách hiểu hoặc trường hợp biên này nhóm em chưa lường trước hết, em xin ghi nhận ý kiến của thầy/cô để cập nhật và hoàn thiện đồ án tốt hơn ạ."* |
| *"Dạ em không biết nói gì nữa."* | *"Dạ về phần này em xin phép trình bày thêm về luồng tương tác với CSDL ở tầng JPA để làm rõ hơn được không ạ?"* |

---

## 🏆 6. NGUYÊN TẮC VÀNG TRƯỚC GIỜ RA TRẬN

1. **Ngủ đủ giấc đêm trước ngày thi:** Đi thi với một cái đầu tỉnh táo sẽ giúp bạn nhớ lại 90% những gì đã đọc trong 41 file tài liệu này.
2. **Khởi động sẵn máy tính trước 15 phút:**
   - Bật sẵn IntelliJ IDEA, project `blog-website-main` đã bấm Run màu xanh.
   - Mở sẵn 2 tab trình duyệt Chrome: 1 tab trang chủ `http://localhost:8080/`, 1 tab ẩn danh để sẵn sàng demo 2 tài khoản tương tác cùng lúc.
   - Mở sẵn cửa sổ H2 Console `http://localhost:8080/h2-console` để khi thầy cô bảo xem DB là bấm Connect được ngay.
3. **Tin tưởng vào bản thân:** Bạn đã có trong tay bộ tài liệu giải thích chi tiết từng dòng code toàn diện nhất. Hãy tự tin bước vào phòng thi và mang điểm 10 về! 🎓🌟
