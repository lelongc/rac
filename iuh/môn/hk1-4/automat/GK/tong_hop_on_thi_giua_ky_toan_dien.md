# CẨM NANG TOÀN DIỆN ÔN THI GIỮA KỲ MÔN LÝ THUYẾT OTOMAT & NGÔN NGỮ HÌNH THỨC
## ĐẠI HỌC CÔNG NGHIỆP TP. HỒ CHÍ MINH (IUH) - KHOA CÔNG NGHỆ THÔNG TIN
### (FILE MASTER TỔNG HỢP 100% LÝ THUYẾT, PHƯƠNG PHÁP, VÍ DỤ TRỰC QUAN & TOÀN BỘ ĐỀ THI, PHIẾU ÔN CỦA THẦY)

> **HƯỚNG DẪN SỬ DỤNG TÀI LIỆU:**
> - Đây là **FILE TỔNG HỢP DUY NHẤT** kết hợp trọn vẹn toàn bộ kiến thức từ các Slide bài giảng của trường (Tuần 1 đến Tuần 8), Đề ôn tập giữa kỳ chính thức (Automata - Đề ôn tập GK 1.pdf), và Phiếu ôn tập giữa kỳ mới nhất của giảng viên (	hem/Automata - Bài ôn tập GK.pdf & Automata - Bài ôn tập GK - hướng dẫn giải.pdf).
> - Tài liệu được tổ chức theo từng **Chuyên đề thi thực tế**. Mỗi chuyên đề đi liền 3 phần:
>   1. **Lý thuyết bản chất & Mẹo nhớ nhanh trực quan** (hình tượng hóa Lego, trò chơi nhảy ô, mẹo nhận diện 10 giây).
>   2. **Phương pháp giải & Mẫu trình bày chuẩn đi thi** (barem chấm điểm của IUH để đạt trọn điểm 10/10).
>   3. **Giải chi tiết 100% tất cả các bài tập thi** (từ Đề GK 1, Bộ bài tập 1 đến 9 của thầy, và các bài tập tương đương dự phòng).
> - Chuẩn hóa ký hiệu 100% tiếng Việt & Unicode trực quan (→, ∅, ★, Σ, δ, ε, ∈, ∉, ∪, ∩, ^*, ^+, ⇒, <, >). Không bị lỗi font, không có mã LaTeX khó đọc. Ký hiệu chuỗi rỗng dùng thống nhất là ε.

---

# MỤC LỤC TỔNG THỂ

- [CHUYÊN ĐỀ 1: BẢNG CHỮ CÁI, CHUỖI, PHÉP LẶP NGÔN NGỮ L* VÀ LŨY THỪA](#chuyên-đề-1-bảng-chữ-cái-chuỗi-phép-lặp-ngôn-ngữ-l-và-lũy-thừa)
  - [1.1. Bản chất lý thuyết qua mô hình Lego trực quan](#11-bản-chất-lý-thuyết-qua-mô-hình-lego-trực-quan)
  - [1.2. Phép đảo chuỗi w^R, Chuỗi đối xứng (Palindrome) & Thứ tự từ điển](#12-phép-đảo-chuỗi-wr-chuỗi-đối-xứng-palindrome--thứ-tự-từ-điển)
  - [1.3. Lũy thừa ngôn ngữ L^k và Định nghĩa chuẩn đi thi của Kleene Star L*](#13-lũy-thừa-ngôn-ngữ-lk-và-định-nghĩa-chuẩn-đi-thi-của-kleene-star-l)
  - [1.4. Bí kíp giải dạng bài 'Kiểm tra chuỗi có thuộc L* hay không?'](#14-bí-kíp-giải-dạng-bài-kiểm-tra-chuỗi-có-thuộc-l-hay-không)
  - [1.5. BÀI THI THỰC TẾ 1: Câu 4 Đề ôn tập GK 1 (Đề chính thức 3.0 điểm)](#15-bài-thi-thực-tế-1-câu-4-đề-ôn-tập-gk-1-đề-chính-thức-30-điểm)
  - [1.6. BÀI THI THỰC TẾ 2: Bài 8 Phiếu ôn tập của thầy (L = {ab, bb, cc, ba, ca})](#16-bài-thi-thực-tế-2-bài-8-phiếu-ôn-tập-của-thầy-l--ab-bb-cc-ba-ca)
  - [1.7. Các bài tập tương đương tự luyện có đáp án](#17-các-bài-tập-tương-đương-tự-luyện-có-đáp-án)

- [CHUYÊN ĐỀ 2: BIỂU THỨC CHÍNH QUY (REGULAR EXPRESSION - RE)](#chuyên-đề-2-biểu-thức-chính-quy-regular-expression---re)
  - [2.1. Bản chất của Biểu thức chính quy qua các khối hình học](#21-bản-chất-của-biểu-thức-chính-quy-qua-các-khối-hình-học)
  - [2.2. Bảng 10 mẫu thiết kế RE kinh điển hay ra thi nhất](#22-bảng-10-mẫu-thiết-kế-re-kinh-điển-hay-ra-thi-nhất)
  - [2.3. BÀI THI THỰC TẾ 1: Câu 1 Đề ôn tập GK 1 (Phân tích bẫy thi & 3 góc nhìn Câu 1b)](#23-bài-thi-thực-tế-1-câu-1-đề-ôn-tập-gk-1-phân-tích-bẫy-thi--3-góc-nhìn-câu-1b)
  - [2.4. BÀI THI THỰC TẾ 2: Bài 1 Phiếu ôn tập của thầy (8 câu RE trọng điểm)](#24-bài-thi-thực-tế-2-bài-1-phiếu-ôn-tập-của-thầy-8-câu-re-trọng-điểm)
  - [2.5. BÀI THI THỰC TẾ 3: Bài 2 Phiếu ôn tập của thầy (Đọc và phân tích 5 RE)](#25-bài-thi-thực-tế-3-bài-2-phiếu-ôn-tập-của-thầy-đọc-và-phân-tích-5-re)
  - [2.6. Giới hạn của RE: Khi nào ngôn ngữ KHÔNG CHÍNH QUY? (Pumping Lemma)](#26-giới-hạn-của-re-khi-nào-ngôn-ngữ-không-chính-quy-pumping-lemma)
  - [2.7. Các bài tập tương đương tự luyện có đáp án](#27-các-bài-tập-tương-đương-tự-luyện-có-đáp-án)

- [CHUYÊN ĐỀ 3: VĂN PHẠM HÌNH THỨC, PHÂN CẤP CHOMSKY, CÂY PHÂN TÍCH & L(G)](#chuyên-đề-3-văn-phạm-hình-thức-phân-cấp-chomsky-cây-phân-tích--lg)
  - [3.1. Bản chất văn phạm qua ví dụ đời thường](#31-bản-chất-văn-phạm-qua-ví-dụ-đời-thường)
  - [3.2. Bảng phân cấp Chomsky 10 giây nhận diện ăn trọn điểm](#32-bảng-phân-cấp-chomsky-10-giây-nhận-diện-ăn-trọn-điểm)
  - [3.3. Phương pháp tìm chuỗi tổng quát, công thức tham số L(G) và vẽ cây phân tích](#33-phương-pháp-tìm-chuỗi-tổng-quát-công-thức-tham-số-lg-và-vẽ-cây-phân-tích)
  - [3.4. BÀI THI THỰC TẾ 1: Câu 2 Đề ôn tập GK 1 (Đề chính thức 3.0 điểm)](#34-bài-thi-thực-tế-1-câu-2-đề-ôn-tập-gk-1-đề-chính-thức-30-điểm)
  - [3.5. BÀI THI THỰC TẾ 2: Bài 3 Phiếu ôn tập của thầy (CFG sinh Non-regular)](#35-bài-thi-thực-tế-2-bài-3-phiếu-ôn-tập-của-thầy-cfg-sinh-non-regular)
  - [3.6. BÀI THI THỰC TẾ 3: Bài 4 Phiếu ôn tập của thầy (CFG sinh Regular - Điểm nhấn cốt lõi)](#36-bài-thi-thực-tế-3-bài-4-phiếu-ôn-tập-của-thầy-cfg-sinh-regular---điểm-nhấn-cốt-lõi)
  - [3.7. Các bài tập tương đương tự luyện có đáp án](#37-các-bài-tập-tương-đương-tự-luyện-có-đáp-án)

- [CHUYÊN ĐỀ 4: ÔTÔMÁT HỮU HẠN (DFA, NFA, BẢNG CHUYỂN, RE ↔ AUTOMATA ↔ VĂN PHẠM)](#chuyên-đề-4-ôtômát-hữu-hạn-dfa-nfa-bảng-chuyển-re--automata--văn-phạm)
  - [4.1. Bản chất Otomat: Cỗ máy nhận dạng chuỗi qua trò chơi nhảy ô](#41-bản-chất-otomat-cỗ-máy-nhận-dạng-chuỗi-qua-trò-chơi-nhảy-ô)
  - [4.2. Định nghĩa hình thức bộ 5 thành phần & Bảng hàm chuyển](#42-định-nghĩa-hình-thức-bộ-5-thành-phần--bảng-hàm-chuyển)
  - [4.3. BÀI THI THỰC TẾ 1: Câu 3 Đề ôn tập GK 1 (Đọc DFA từ hình ảnh đề thi)](#43-bài-thi-thực-tế-1-câu-3-đề-ôn-tập-gk-1-đọc-dfa-từ-hình-ảnh-đề-thi)
  - [4.4. BÀI THI THỰC TẾ 2: Bài 5 Phiếu ôn tập của thầy (Chuyển 5 RE sang Automata)](#44-bài-thi-thực-tế-2-bài-5-phiếu-ôn-tập-của-thầy-chuyển-5-re-sang-automata)
  - [4.5. BÀI THI THỰC TẾ 3: Bài 6 Phiếu ôn tập của thầy (Đọc Automata từ Bảng chuyển)](#45-bài-thi-thực-tế-3-bài-6-phiếu-ôn-tập-của-thầy-đọc-automata-từ-bảng-chuyển)
  - [4.6. BÀI THI THỰC TẾ 4: Bài 7 Phiếu ôn tập của thầy (Tự thiết kế 4 DFA kinh điển)](#46-bài-thi-thực-tế-4-bài-7-phiếu-ôn-tập-của-thầy-tự-thiết-kế-4-dfa-kinh-điển)
  - [4.7. BÀI THI THỰC TẾ 5: Bài 9 Phiếu ôn tập của thầy (Mô phỏng bài thi 20 phút & Chuyển DFA sang Văn phạm)](#47-bài-thi-thực-tế-5-bài-9-phiếu-ôn-tập-của-thầy-mô-phỏng-bài-thi-20-phút--chuyển-dfa-sang-văn-phạm)
  - [4.8. Bổ trợ nâng cao: Thuật toán chuyển NFA sang DFA & Tối thiểu hóa DFA](#48-bổ-trợ-nâng-cao-thuật-toán-chuyển-nfa-sang-dfa--tối-thiểu-hóa-dfa)

- [CHUYÊN ĐỀ 5: CHIẾN LƯỢC PHÒNG THI & CHECKLIST 10 ĐIỂM CỦA GIẢNG VIÊN](#chuyên-đề-5-chiến-lược-phòng-thi--checklist-10-điểm-của-giảng-viên)
  - [5.1. Sáu nguyên tắc vàng đúc kết từ giảng viên](#51-sáu-nguyên-tắc-vàng-đúc-kết-từ-giảng-viên)
  - [5.2. Bảng tổng hợp các bẫy đề thi hay gài và cách né bẫy](#52-bảng-tổng-hợp-các-bẫy-đề-thi-hay-gài-và-cách-né-bẫy)
  - [5.3. Bảng Checklist 12 kỹ năng trước khi vào phòng thi](#53-bảng-checklist-12-kỹ-năng-trước-khi-vào-phòng-thi)

---


---

# CHUYÊN ĐỀ 1: BẢNG CHỮ CÁI, CHUỖI, PHÉP LẶP NGÔN NGỮ L* VÀ LŨY THỪA

---

## 1.1. Bản chất lý thuyết qua mô hình Lego trực quan

### [TRỰC QUAN] Hình dung dễ hiểu:
- **Bảng chữ cái (Σ):** Là một **hộp xếp hình Lego** chỉ chứa một số loại mảnh ghép cơ bản nhất định. Ví dụ:
  + Hộp nhị phân: `Σ = {0, 1}` (chỉ có mảnh số 0 và mảnh số 1).
  + Hộp chữ cái: `Σ = {a, b, c}` (có 3 loại mảnh: a, b, c).
- **Từ / Chuỗi (w):** Là một **mô hình Lego hoàn chỉnh** được lắp ghép từ các mảnh trong hộp. Ví dụ: `ab`, `abc`, `01101`.
- **Độ dài chuỗi (|w|):** Là tổng số lượng mảnh ghép có trong mô hình. Ví dụ:
  + `|abc| = 3`
  + `|(ab)^3| = 2 × 3 = 6`
- **Chuỗi rỗng (ε):** Là **chiếc bàn trống trơn, chưa gắn mảnh Lego nào cả**.
  + Độ dài chuỗi rỗng: `|ε| = 0`.
  + Chuỗi rỗng là phần tử trung hòa của phép ghép chuỗi: Ghép bàn trống vào bất kỳ mô hình nào thì mô hình đó vẫn giữ nguyên kích thước:
    `ε . w = w . ε = w` (với mọi chuỗi `w`).

---

## 1.2. Phép đảo chuỗi w^R, Chuỗi đối xứng (Palindrome) & Thứ tự từ điển

### 1. Phép đảo chuỗi (`w^R`):
- Viết các ký hiệu của chuỗi theo thứ tự ngược lại từ phải sang trái.
- *Ví dụ:* `(abc)^R = cba`, `(01101)^R = 10110`.
- **Định lý đảo của tích ghép:** `(u . v)^R = v^R . u^R` (đảo ngược của một chuỗi ghép bằng tích các chuỗi con đảo ngược theo thứ tự ngược lại).

### 2. Chuỗi đối xứng (Palindrome):
- Một chuỗi `w` được gọi là đối xứng (Palindrome) khi và chỉ khi đọc xuôi hay đọc ngược đều hoàn toàn như nhau:
  `w = w^R`
- *Ví dụ:* `aa`, `aba`, `abba`, `10101`, `radar`.

### 3. Quy tắc sắp xếp chuỗi theo Thứ tự từ điển (Lexicographical Order):
Khi đề thi yêu cầu liệt kê các chuỗi ngắn nhất theo thứ tự từ điển:
- **Nguyên tắc 1 (Ưu tiên độ dài):** Chuỗi có độ dài ngắn hơn luôn đứng trước chuỗi có độ dài dài hơn (`|u| < |v| ⇒ u` đứng trước `v`).
  + Chuỗi rỗng `ε` có độ dài bằng 0 nên luôn luôn đứng đầu tiên.
- **Nguyên tắc 2 (Cùng độ dài):** So sánh theo thứ tự bảng chữ cái thông thường (ví dụ: `a` đứng trước `b`, `0` đứng trước `1`).
- *Ví dụ trên `Σ = {a, b}`:*
  `ε, a, b, aa, ab, ba, bb, aaa, aab, aba, abb, baa, bab, bba, bbb, ...`

---

## 1.3. Lũy thừa ngôn ngữ L^k và Định nghĩa chuẩn đi thi của Kleene Star L*

### 1. Phép nhân ghép ngôn ngữ (Concatenation):
Cho hai ngôn ngữ `L1` và `L2`. Tích của chúng là tập hợp tất cả các chuỗi có dạng ghép một từ của `L1` với một từ của `L2`:
```text
L1 . L2 = { u . v | u ∈ L1, v ∈ L2 }
```

### 2. Lũy thừa của một ngôn ngữ (`L^k`):
- **Lũy thừa 0:** `L^0 = { ε }` (Tập hợp chỉ chứa duy nhất chuỗi rỗng `ε`, KHÔNG PHẢI tập rỗng `∅`).
- **Lũy thừa 1:** `L^1 = L` (Chính ngôn ngữ ban đầu).
- **Lũy thừa 2:** `L^2 = L . L` (Ghép 2 từ bất kỳ thuộc `L`).
- **Lũy thừa k:** `L^k = L . L^(k-1)` (Ghép `k` từ bất kỳ thuộc `L`).

### 3. ĐỊNH NGHĨA TOÁN HỌC CHUẨN ĐI THI CỦA PHÉP LẶP KLEENE STAR (`L^*`):
> **Định nghĩa hình thức chuẩn (Chép nguyên văn vào bài thi để lấy trọn điểm):**
> Cho ngôn ngữ `L` trên bảng chữ cái `Σ`. Phép lặp ngôn ngữ `L^*` (Kleene star hay Bao đóng Kleene) là hợp của tất cả các lũy thừa không âm của `L`:
> ```text
> L* = ⋃ (k = 0 đến ∞) L^k = L^0 ∪ L^1 ∪ L^2 ∪ L^3 ∪ ...
> ```
> Hay nói cách khác:
> ```text
> L* = { w1 w2 ... wk | k ≥ 0 và wi ∈ L với mọi i = 1, 2, ..., k }
> ```
> (Quy ước: Khi `k = 0`, tích rỗng chính là chuỗi rỗng `ε`).

- **Phép cộng Kleene (`L^+` - Bao đóng dương):**
  `L^+ = ⋃ (k = 1 đến ∞) L^k = L^1 ∪ L^2 ∪ L^3 ∪ ... = L^* loại bỏ chuỗi rỗng ε` (nếu `ε ∉ L`).
  Mối quan hệ: `L^* = L^+ ∪ { ε }`.

---

## 1.4. Bí kíp giải dạng bài "Kiểm tra chuỗi có thuộc L* hay không?"

Khi gặp bài toán: *"Cho tập từ cơ sở `L`. Hỏi chuỗi `w` có thuộc `L^*` hay không?"*, hãy áp dụng tuần tự 2 bước thần tốc sau:

```text
       [Chuỗi w cần kiểm tra]
                 |
                 v
   +-----------------------------+
   | BƯỚC 1: KIỂM TRA ĐỘ DÀI     |
   | - Mọi từ trong L có độ dài  |
   |   bằng d không?             |
   +-----------------------------+
         /                /
     ĐÚNG                 SAI
       /                    /
      v                      v
|w| chia hết cho d?     Tiến hành Bước 2 ngay
   /       /
  CÓ        KHÔNG
  /           /
 v             v
Tiến hành     KẾT LUẬN NGAY:
Bước 2        w KHÔNG THUỘC L* (100% ăn trọn điểm)
```

- **Bước 1 (Kiểm tra độ dài - Bộ lọc 3 giây):**
  + Nếu tất cả các từ trong `L` đều có độ dài bằng nhau là `d` (ví dụ `d = 2` trong các bài thi IUH: `L = {ab, ba, ac, ca, bc, cb}` hoặc `L = {ab, bb, cc, ba, ca}`):
  + Thì mọi chuỗi `w ∈ L^*` BẮT BUỘC phải có độ dài là một bội số của `d`:
    `|w| = k × d`
  + Do đó, nếu `|w|` không chia hết cho `d` (độ dài lẻ khi `d = 2`), ta **kết luận ngay lập tức `w ∉ L^*`** mà không cần mất công phân tích chuỗi!
- **Bước 2 (Phân rã chuỗi từ trái qua phải):**
  + Nếu độ dài thỏa mãn, ta phân tách chuỗi thành các khối độ dài `d` từ trái sang phải.
  + Kiểm tra xem từng khối có nằm trong danh sách từ của `L` hay không.
  + Nếu tất cả các khối đều thuộc `L` ⇒ **`w ∈ L^*`**.
  + Nếu có bất kỳ một khối nào không thuộc `L` và không còn cách phân tách nào khác ⇒ **`w ∉ L^*`**.

---

## 1.5. BÀI THI THỰC TẾ 1: Câu 4 Đề ôn tập GK 1 (Đề chính thức 3.0 điểm)

**ĐỀ BÀI CHÍNH THỨC (Trích Đề GK 1):**
Cho ngôn ngữ `L = {ab, ba, ac, ca, bc, cb}` trên bảng chữ cái `Σ = {a, b, c}`.
a) (1.0 điểm) Trình bày định nghĩa toán học của phép lặp ngôn ngữ `L^*`.
b) (2.0 điểm) Xác định chuỗi nào dưới đây thuộc `L^*`:
1. `w1 = (ab)^3 c^4 ba^2`
2. `w2 = (ab)^2 c^4 bac b^3 ac^2`
3. `w3 = (ab)^3 c^8 bac b^3 ac^2`
4. `w4 = b^3 a^2 b^3 (ac)^2 ab`
5. `w5 = b^5 a^3 b^3 (abc)^2 ab`
6. `w6 = b^7 a^2 b^3 (ac)^2 aab`

---

### LỜI GIẢI MẪU CHUẨN 10/10 ĐI THI:

#### Lời giải Câu 4a:
```text
BÀI LÀM CÂU 4a:

Định nghĩa toán học của phép lặp ngôn ngữ L* (Kleene Star):
Cho ngôn ngữ L xác định trên bảng chữ cái Σ. Phép lặp ngôn ngữ L* là tập hợp 
tất cả các chuỗi thu được bằng cách ghép nối một số hữu hạn (k ≥ 0) các từ tùy ý 
thuộc L.

Công thức toán học hình thức:
          L* = ⋃ (k = 0 đến ∞) L^k = L^0 ∪ L^1 ∪ L^2 ∪ L^3 ∪ ...

Trong đó các lũy thừa của L được định nghĩa quy nạp như sau:
  - L^0 = { ε }  (với ε là chuỗi rỗng)
  - L^1 = L
  - L^(k+1) = L^k . L = { u . v | u ∈ L^k, v ∈ L }  (với k ≥ 1)

Nói cách khác:
          L* = { w1 w2 ... wk | k ≥ 0 và wi ∈ L với mọi i = 1, 2, ..., k }
(Quy ước khi k = 0, tích rỗng chính là chuỗi rỗng ε ∈ L*).
```

---

#### Lời giải Câu 4b:
```text
BÀI LÀM CÂU 4b:

Xét ngôn ngữ cơ sở: L = {ab, ba, ac, ca, bc, cb} trên Σ = {a, b, c}.
Nhận xét tiên quyết:
Mọi từ u ∈ L đều có độ dài đúng bằng 2:
          |ab| = |ba| = |ac| = |ca| = |bc| = |cb| = 2.
Do đó, một chuỗi w bất kỳ thuộc L* (w = u1 u2 ... uk với ui ∈ L) bắt buộc phải có độ dài:
          |w| = |u1| + |u2| + ... + |uk| = 2 × k  (với k ≥ 0 là số nguyên).
Điều kiện cần: Độ dài |w| của mọi chuỗi thuộc L* BẮT BUỘC PHẢI LÀ MỘT SỐ CHẴN.
Nếu chuỗi có độ dài LẺ, chuỗi đó chắc chắn KHÔNG THUỘC L*.

Ta tiến hành kiểm tra từng chuỗi:

1. Xét chuỗi w1 = (ab)^3 c^4 ba^2:
   - Tính độ dài:
     |w1| = 3 × |ab| + 4 × |c| + 1 × |b| + 2 × |a|
          = 3 × 2 + 4 × 1 + 1 + 2 = 6 + 4 + 1 + 2 = 13 (SỐ LẺ).
   - Kết luận: Vì độ dài |w1| = 13 là số lẻ, chuỗi w1 KHÔNG THUỘC L*.

2. Xét chuỗi w2 = (ab)^2 c^4 bac b^3 ac^2:
   - Tính độ dài:
     |w2| = 2 × 2 + 4 + 3 + 3 + 1 + 4 = 4 + 4 + 3 + 3 + 1 + 4 = 19 (SỐ LẺ).
   - Kết luận: Vì độ dài |w2| = 19 là số lẻ, chuỗi w2 KHÔNG THUỘC L*.

3. Xét chuỗi w3 = (ab)^3 c^8 bac b^3 ac^2:
   - Tính độ dài:
     |w3| = 3 × 2 + 8 + 3 + 3 + 1 + 4 = 6 + 8 + 3 + 3 + 1 + 4 = 25 (SỐ LẺ)
     (Nếu ac^2 hiểu là a . c^2 thì độ dài là 6 + 8 + 3 + 3 + 3 = 23 - SỐ LẺ).
   - Kết luận: Dù hiểu theo cách nào thì |w3| là số lẻ, chuỗi w3 KHÔNG THUỘC L*.

4. Xét chuỗi w4 = b^3 a^2 b^3 (ac)^2 ab:
   - Tính độ dài:
     |w4| = 3 + 2 + 3 + (2 × 2) + 2 = 14 (SỐ CHẴN).
   - Kiểm tra phân hoạch thành các cặp 2 ký tự:
     Khai triển chuỗi: w4 = b b b a a b b b a c a c a b
     Phân tích từ trái sang phải:
       + Khối 1: bb ∉ L  (Trong L không có từ bb).
       + Nếu cố gắng tách lệch để khớp ba: b . (bb) . (aa) ... đều chứa khối không thuộc L.
       + Cụ thể: w4 có cụm bbb (3 chữ b liên tiếp) và aaa/aab, không thể phân rã thành các từ của L.
   - Kết luận: Chuỗi w4 KHÔNG THUỘC L*.

5. Xét chuỗi w5 = b^5 a^3 b^3 (abc)^2 ab:
   - Tính độ dài:
     |w5| = 5 + 3 + 3 + (2 × 3) + 2 = 19 (SỐ LẺ).
   - Kết luận: Vì độ dài |w5| = 19 là số lẻ, chuỗi w5 KHÔNG THUỘC L*.

6. Xét chuỗi w6 = b^7 a^2 b^3 (ac)^2 aab:
   - Tính độ dài:
     |w6| = 7 + 2 + 3 + 4 + 3 = 19 (SỐ LẺ).
   - Kết luận: Vì độ dài |w6| = 19 là số lẻ, chuỗi w6 KHÔNG THUỘC L*.

BẢNG TỔNG HỢP KẾT QUẢ ĐI THI:
| STT | Chuỗi w | Độ dài | Tính chẵn lẻ | Khả năng phân rã vào L | KẾT LUẬN |
|:---:|:---|:---:|:---:|:---|:---:|
| 1 | (ab)^3 c^4 ba^2 | 13 | LẺ | Không thể (độ dài lẻ) | KHÔNG THUỘC L* |
| 2 | (ab)^2 c^4 bac b^3 ac^2 | 19 | LẺ | Không thể (độ dài lẻ) | KHÔNG THUỘC L* |
| 3 | (ab)^3 c^8 bac b^3 ac^2 | 23/25 | LẺ | Không thể (độ dài lẻ) | KHÔNG THUỘC L* |
| 4 | b^3 a^2 b^3 (ac)^2 ab | 14 | CHẴN | Chứa khối bb ∉ L | KHÔNG THUỘC L* |
| 5 | b^5 a^3 b^3 (abc)^2 ab | 19 | LẺ | Không thể (độ dài lẻ) | KHÔNG THUỘC L* |
| 6 | b^7 a^2 b^3 (ac)^2 aab | 19 | LẺ | Không thể (độ dài lẻ) | KHÔNG THUỘC L* |

KẾT LUẬN CHUNG: Trong cả 6 chuỗi đề thi cho, KHÔNG CÓ CHUỖI NÀO THUỘC L*.
```

---

## 1.6. BÀI THI THỰC TẾ 2: Bài 8 Phiếu ôn tập của thầy (L = {ab, bb, cc, ba, ca})

**ĐỀ BÀI (Trích Phiếu ôn tập của giảng viên):**
Cho `L = {ab, bb, cc, ba, ca}` trên `Σ = {a, b, c}`.
1. Xác định chuỗi nào dưới đây thuộc `L^*` và chỉ ra phân hoạch cụ thể nếu thuộc:
   `ab`, `abba`, `abbaca`, `bbccab`, `cabaab`, `abcabb`, `babbca`, `ababbbcc`, `cacaab`, `abbcc`.
2. Xác định các tập hợp `L^0, L^1, L^2` và số lượng chuỗi khác nhau có trong `L^2`.

---

### LỜI GIẢI MẪU CHUẨN 10/10 ĐI THI:

#### 1. Kiểm tra 10 chuỗi và phân hoạch cụ thể:
Nhận xét: Mọi từ trong `L` đều có độ dài bằng 2. Do đó chuỗi thuộc `L^*` bắt buộc phải có độ dài chẵn và phân tách được thành các từ của `L`.

| Chuỗi `w` | Độ dài `|w|` | Tính chẵn lẻ | Phân hoạch thành các từ của `L` | KẾT LUẬN |
| :--- | :---: | :---: | :--- | :---: |
| `ab` | 2 | Chẵn | `ab` (∈ L) | **THUỘC `L^*`** |
| `abba` | 4 | Chẵn | `ab . ba` (cả 2 từ đều ∈ L) | **THUỘC `L^*`** |
| `abbaca` | 6 | Chẵn | `ab . ba . ca` (cả 3 từ đều ∈ L) | **THUỘC `L^*`** |
| `bbccab` | 6 | Chẵn | `bb . cc . ab` (cả 3 từ đều ∈ L) | **THUỘC `L^*`** |
| `cabaab` | 6 | Chẵn | `ca . ba . ab` (cả 3 từ đều ∈ L) | **THUỘC `L^*`** |
| `abcabb` | 6 | Chẵn | `ab . ca . bb` (cả 3 từ đều ∈ L) | **THUỘC `L^*`** |
| `babbca` | 6 | Chẵn | `ba . bb . ca` (cả 3 từ đều ∈ L) | **THUỘC `L^*`** |
| `ababbbcc` | 8 | Chẵn | `ab . ab . bb . cc` (cả 4 từ đều ∈ L) | **THUỘC `L^*`** |
| `cacaab` | 6 | Chẵn | `ca . ca . ab` (cả 3 từ đều ∈ L) | **THUỘC `L^*`** |
| `abbcc` | 5 | **LẺ** | Tách theo cặp: `ab` - `bc` - `c` (bị lẻ chữ c cuối và `bc ∉ L`) | **KHÔNG THUỘC** |

#### 2. Xác định các lũy thừa L^0, L^1, L^2:
- **Lũy thừa 0:**
  `L^0 = { ε }` (Chỉ chứa duy nhất chuỗi rỗng `ε`).
- **Lũy thừa 1:**
  `L^1 = L = { ab, bb, cc, ba, ca }`.
- **Lũy thừa 2 (`L^2 = L . L`):**
  Ghép từng từ trong `L` với toàn bộ 5 từ trong `L`:
  + Ghép từ `ab`: `abab`, `abbb`, `abcc`, `abba`, `abca`
  + Ghép từ `bb`: `bbab`, `bbbb`, `bbcc`, `bbba`, `bbca`
  + Ghép từ `cc`: `ccab`, `ccbb`, `cccc`, `ccba`, `ccca`
  + Ghép từ `ba`: `baab`, `babb`, `bacc`, `baba`, `baca`
  + Ghép từ `ca`: `caab`, `cabb`, `cacc`, `caba`, `caca`

- **Chứng minh số chuỗi khác nhau trong `L^2` là 25 chuỗi:**
  + Mọi chuỗi sinh ra đều có độ dài 4 (`|u . v| = 2 + 2 = 4`).
  + Cách phân rã một chuỗi độ dài 4 thành 2 khối độ dài 2 là duy nhất (2 ký tự đầu là từ thứ nhất, 2 ký tự sau là từ thứ hai).
  + Vì tập `L` có 5 từ phân biệt, có 5 cách chọn từ đầu và 5 cách chọn từ sau:
    `5 × 5 = 25` cặp từ phân biệt.
  + Do tính duy nhất của phép ghép chuỗi độ dài cố định, không có bất kỳ hai cặp nào cho ra kết quả trùng nhau.
  + **KẾT LUẬN:** Trong `L^2` có chính xác **25 chuỗi phân biệt**.

---

## 1.7. Các bài tập tương đương tự luyện có đáp án

### Bài 1.7.1: Cho `L = {01, 10, 11}` trên bảng chữ cái `{0, 1}`
- **Câu hỏi:** Kiểm tra các chuỗi sau có thuộc `L^*` không: `w1 = 011011`, `w2 = 10011`, `w3 = 111001`, `w4 = (01)^3 (11)^2`.
- **Đáp án:**
  + `w1`: `|w1| = 6` (chẵn), tách thành `01 . 10 . 11` (đều ∈ L) ⇒ **THUỘC `L^*`**.
  + `w2`: `|w2| = 5` (lẻ) ⇒ **KHÔNG THUỘC `L^*`**.
  + `w3`: `|w3| = 6` (chẵn), tách thành `11 . 10 . 01` (đều ∈ L) ⇒ **THUỘC `L^*`**.
  + `w4`: gồm 3 khối `01` và 2 khối `11` ⇒ **THUỘC `L^*`**.

### Bài 1.7.2: Cho `L = {a, ab}` trên bảng chữ cái `{a, b}`
- **Câu hỏi:**
  a) Xác định `L^0, L^1, L^2`.
  b) Chuỗi `aabaab` và chuỗi `bba` có thuộc `L^*` không?
- **Đáp án:**
  + a) `L^0 = {ε}`; `L^1 = {a, ab}`; `L^2 = {aa, aab, aba, abab}` (có 4 chuỗi).
  + b) `aabaab = a . ab . a . ab` ⇒ **THUỘC `L^*`**.
       `bba`: Từ đầu tiên là `b`, nhưng mọi từ trong `L` đều bắt đầu bằng chữ `a` ⇒ **KHÔNG THUỘC `L^*`**.


---

# CHUYÊN ĐỀ 2: BIỂU THỨC CHÍNH QUY (REGULAR EXPRESSION - RE)

---

## 2.1. Bản chất của Biểu thức chính quy qua các khối hình học

### [TRỰC QUAN] Hình dung dễ hiểu:
Biểu thức chính quy (RE) giống như **bản thiết kế một dây chuyền đóng gói sản phẩm tự động**. Chỉ với 3 thao tác cơ bản, bạn có thể mô tả mọi cấu trúc chuỗi chính quy:
1. **Phép ghép nối (Concatenation - Đặt cạnh nhau):**
   - Viết liền: `ab` nghĩa là "nhặt mảnh `a`, sau đó nhặt tiếp mảnh `b`".
2. **Phép cộng / Hợp (Union / Choice - Dấu `+`):**
   - Viết `(a + b)` nghĩa là "được quyền CHỌN HOẶC `a` HOẶC `b`" (giống ngã rẽ 2 nhánh).
   - Viết `(a + b + c)` nghĩa là chọn 1 trong 3 ký tự.
3. **Phép lặp Kleene Star (Loop - Dấu `^*`):**
   - Viết `a^*` nghĩa là "lặp lại ký hiệu `a` tùy ý số lần (0 lần, 1 lần, 2 lần, 100 lần...)".
   - `0 lần` nghĩa là không nhặt mảnh nào, chính là chuỗi rỗng `ε`.
   - `(a + b)^*` nghĩa là: "ở mỗi lượt lặp, bạn tùy ý bốc hoặc `a` hoặc `b` bao nhiêu lần tùy thích". Đây là công thức đại diện cho **TẤT CẢ MỌI CHUỖI CÓ THỂ CÓ TRÊN {a, b}**.
   - `(a + b + c)^*` là đại diện cho **TẤT CẢ MỌI CHUỖI TRÊN {a, b, c}**.

### Thứ tự ưu tiên toán tử:
Khi đọc và viết RE, thứ tự ưu tiên từ cao xuống thấp là:
1. **Ưu tiên 1 (Cao nhất):** Dấu ngoặc tròn `(...)` và phép lặp `^*`.
2. **Ưu tiên 2 (Ở giữa):** Phép nhân ghép nối (viết liền).
3. **Ưu tiên 3 (Thấp nhất):** Phép cộng / phép hợp `+`.
- *Ví dụ:* `ab^*` nghĩa là `a` ghép với `b^*` (chữ `b` lặp, `a` không lặp). Muốn cả cụm `ab` lặp thì bắt buộc phải đóng ngoặc: `(ab)^*`.

---

## 2.2. Bảng 10 mẫu thiết kế RE kinh điển hay ra thi nhất

| STT | Yêu cầu đề bài | Công thức RE mẫu | Phân tích cơ chế hoạt động |
| :---: | :--- | :--- | :--- |
| **1** | Chứa chuỗi con `u` cố định trên `Σ` | `Σ^* u Σ^*` | Trước `u` và sau `u` có thể là chuỗi bất kỳ tùy ý. |
| **2** | Chứa chuỗi con `u` HOẶC chuỗi con `v` | `Σ^* (u + v) Σ^*` | Tách nhánh ở giữa: bọc `Σ^*` ở hai đầu. |
| **3** | Bắt đầu bằng `u` và kết thúc bằng `v` | `u Σ^* v` | Cố định `u` ở đầu, `v` ở cuối, ở giữa tùy ý. |
| **4** | Bắt đầu bằng `u1` hoặc `u2`, kết thúc bằng `v` | `(u1 + u2) Σ^* v` | Nhóm tiền tố trong ngoặc `(u1 + u2)`. |
| **5** | Mọi ký tự `b` đều đi thành cặp đôi `bb` | `(a + bb)^*` | Viên gạch chỉ có thể là `a` hoặc `bb`, không có `b` lẻ. |
| **6** | Số lượng ký tự `b` là một số chẵn | `a^* (b a^* b a^*)^*` | Mỗi vòng lặp thêm đúng 2 chữ `b`, xen kẽ `a` tùy ý. |
| **7** | Số lượng ký tự `b` là một số lẻ | `a^* b a^* (b a^* b a^*)^*` | Có 1 chữ `b` lẻ cố định, sau đó là các cặp `bb`. |
| **8** | KHÔNG chứa chuỗi con `bb` (không có 2 chữ b kề nhau) | `(a + ba)^* (ε + b)` | Sau mỗi chữ `b` phải có ngay `a`. Chữ `b` cuối cùng được đứng lẻ. |
| **9** | Độ dài chuỗi ít nhất là `k` ký tự | `Σ^k Σ^*` | Viết `k` lần `Σ` ghép liền, phía sau là `Σ^*`. |
| **10** | Dãy các khối tuần tự: tiền tố, lặp thân, hậu tố | `(tiền_tố) (thân)^* (hậu_tố)` | Phép ghép 3 khối nối tiếp nhau không phân nhánh. |

---

## 2.3. BÀI THI THỰC TẾ 1: Câu 1 Đề ôn tập GK 1 (Phân tích bẫy thi & 3 góc nhìn Câu 1b)

**ĐỀ BÀI CHÍNH THỨC (Trích Đề GK 1 - 2.0 điểm):**
Xét bảng chữ cái `Σ = {a, b, c}`. Hãy tìm biểu thức chính quy đại diện cho các ngôn ngữ sau đây:
a) (1.0 điểm) Tất cả các chuỗi có chứa chuỗi con `acab` hoặc `bbac`.
b) (1.0 điểm) Tất cả các chuỗi sao cho số lượng ký tự `a` nhiều gấp 2 lần số lượng ký tự `b` có trong chuỗi.

---

### LỜI GIẢI MẪU CHUẨN 10/10 ĐI THI:

#### Lời giải Câu 1a:
```text
BÀI LÀM CÂU 1a:

Xét bảng chữ cái Σ = {a, b, c}.
Tập hợp tất cả các chuỗi có thể tạo thành từ Σ được đại diện bởi biểu thức chính quy:
               (a + b + c)*

Chuỗi chứa chuỗi con "acab" hoặc "bbac" có dạng tổng quát:
  - Phía trước chuỗi con: là một chuỗi tùy ý thuộc Σ*, biểu diễn bởi (a + b + c)*
  - Ở giữa: là chuỗi con "acab" hoặc "bbac", biểu diễn bởi phép hợp (acab + bbac)
  - Phía sau chuỗi con: là một chuỗi tùy ý thuộc Σ*, biểu diễn bởi (a + b + c)*

Vậy biểu thức chính quy đại diện cho ngôn ngữ là:
               R = (a + b + c)* (acab + bbac) (a + b + c)*

(Hoặc có thể viết dưới dạng tách rời hai trường hợp tương đương:
               R = (a + b + c)* acab (a + b + c)* + (a + b + c)* bbac (a + b + c)*)
```

---

#### Lời giải Câu 1b (Phân tích bẫy thi & 3 góc nhìn ăn trọn điểm):
> [!IMPORTANT]
> **ĐÂY LÀ CÂU HỎI BẪY KINH ĐIỂN CỦA ĐỀ THI LÝ THUYẾT OTOMAT!**
> Ngôn ngữ yêu cầu đếm và so sánh số lượng không giới hạn giữa hai ký tự (`Na(w) = 2 . Nb(w)`) là **NGÔN NGỮ PHI CHÍNH QUY (NON-REGULAR LANGUAGE)**.
> Để đạt điểm tối đa dù người chấm theo trường phái lý thuyết toán chặt chẽ hay theo trường phái ứng dụng thực hành, hãy trình bày bài làm theo mẫu đa chiều dưới đây:

```text
BÀI LÀM CÂU 1b:

Ngôn ngữ cần biểu diễn là:
         L = { w ∈ {a, b, c}* | Na(w) = 2 . Nb(w) }
(trong đó Na(w), Nb(w) lần lượt là số lượng ký tự a và ký tự b có trong chuỗi w).

Ta phân tích và trình bày lời giải theo các góc nhìn chuyên môn:

1. XÉT THEO LÝ THUYẾT NGÔN NGỮ HÌNH THỨC CHẶT CHẼ (FORMAL LANGUAGE THEORY):
   Ngôn ngữ L đòi hỏi một cỗ máy nhận diện phải ghi nhớ và so sánh số lượng không 
   bị chặn giữa ký tự a và ký tự b (số chữ a luôn bằng 2 lần số chữ b).
   - Vì một Otomat hữu hạn (DFA/NFA) chỉ có hữu hạn trạng thái (bộ nhớ hữu hạn), 
     nó không thể đếm số lượng ký tự lớn tùy ý.
   - Theo Bổ đề Bơm (Pumping Lemma) cho ngôn ngữ chính quy, ngôn ngữ L là một 
     NGÔN NGỮ PHI CHÍNH QUY (NON-REGULAR LANGUAGE).
   - Do đó, trong lý thuyết hình thức cổ điển KHÔNG TỒN TẠI một Biểu thức chính quy 
     thuần túy (Standard Regular Expression) nào có thể biểu diễn chính xác hoàn toàn 
     tất cả các hoán vị vị trí của L.

2. XÉT THEO GÓC NHÌN BIỂU THỨC CHÍNH QUY THỰC HÀNH MỞ RỘNG (PCRE / REGEX HIỆN ĐẠI):
   Trong khoa học máy tính ứng dụng, Regular Expression được mở rộng với tính năng 
   Lookaround và Backreference. Biểu thức có thể viết để kiểm tra điều kiện này là:
         ^(?=(?:[^a]*a){2}(?:[^a]*a)*)(?!(?:[^a]*a)(?:(?:[^a]*a){2})*) ...

3. XÉT THEO GÓC NHÌN XẤP XỈ THEO KHỐI CỤC BỘ (LOCAL BALANCED BLOCKS):
   Nếu đề bài ngầm định số chữ a và b xuất hiện cân bằng theo từng khối tuần tự 
   (mỗi ký tự b đi kèm đúng 2 ký tự a lân cận, và các ký tự c xuất hiện tự do):
   - Mỗi khối cơ sở cân bằng gồm 1 chữ b và 2 chữ a có 3 hoán vị:
         (aab + aba + baa)
   - Kết hợp với ký tự c xuất hiện tùy ý ở mọi vị trí, ta có biểu thức chính quy:
         R = ( c* (aab + aba + baa) c* )* + c*
   (Hoặc nếu chỉ xét thứ tự đơn giản nhất a đứng trước b: R = (c* a a c* b c*)* + c*)

KẾT LUẬN:
Về mặt toán học hình thức, L là ngôn ngữ phi chính quy. 
Nếu câu hỏi yêu cầu biểu diễn gần đúng bằng các khối cơ bản, biểu thức đại diện là:
         R = ( c* (aab + aba + baa) c* )* + c*
```

---

## 2.4. BÀI THI THỰC TẾ 2: Bài 1 Phiếu ôn tập của thầy (8 câu RE trọng điểm)

**ĐỀ BÀI (Trích Phiếu ôn tập của giảng viên):**
Cho `Σ = {a, b, c}`. Viết RE cho:
(1) Chứa chuỗi con `abc`;
(2) Chứa `ab` hoặc `ca`;
(3) Bắt đầu bằng `a` và kết thúc bằng `bc`;
(4) Bắt đầu bằng `ab` hoặc `bc` và kết thúc bằng `a`.

Trên `Σ = {a, b}`:
(5) Mọi `b` xuất hiện thành từng cặp `bb`;
(6) Số lượng `b` là số chẵn;
(7) Không chứa chuỗi con `bb`;
(8) Bắt đầu bằng `a` hoặc `b`, tiếp theo 0 hoặc nhiều `ac`, và kết thúc bằng `abc`.
*(Với mỗi RE: cho 2 chuỗi thuộc và 2 chuỗi không thuộc).*

---

### LỜI GIẢI MẪU CHUẨN 10/10 ĐI THI:

```text
BÀI LÀM BÀI 1:

1. Chứa chuỗi con "abc" trên Σ = {a, b, c}:
   - Công thức: R = (a + b + c)* abc (a + b + c)*
   - 2 chuỗi thuộc: abc, aabcbc
   - 2 chuỗi không thuộc: ε, acb (sai thứ tự)

2. Chứa "ab" hoặc "ca" trên Σ = {a, b, c}:
   - Công thức: R = (a + b + c)* (ab + ca) (a + b + c)*
   - 2 chuỗi thuộc: ab, bca (chứa ca)
   - 2 chuỗi không thuộc: ε, ba (không chứa ab và không chứa ca)

3. Bắt đầu bằng "a" và kết thúc bằng "bc" trên Σ = {a, b, c}:
   - Công thức: R = a (a + b + c)* bc
   - 2 chuỗi thuộc: abc (khi phần giữa là ε), aabc
   - 2 chuỗi không thuộc: bc (thiếu a ở đầu), ab (không kết thúc bằng bc)

4. Bắt đầu bằng "ab" hoặc "bc" và kết thúc bằng "a" trên Σ = {a, b, c}:
   - Công thức: R = (ab + bc) (a + b + c)* a
   - 2 chuỗi thuộc: aba, bca
   - 2 chuỗi không thuộc: ab (không kết thúc bằng a), a (thiếu tiền tố ab hoặc bc)

5. Mọi "b" xuất hiện thành từng cặp "bb" trên {a, b}:
   - Phân tích: Không được có chữ b đứng đơn lẻ; các khối sinh ra chỉ là a hoặc bb.
   - Công thức: R = (a + bb)*
   - 2 chuỗi thuộc: ε, abb
   - 2 chuỗi không thuộc: b (lẻ 1 chữ b), bab (hai chữ b bị tách rời)

6. Số lượng "b" là số chẵn trên {a, b}:
   - Phân tích: Mỗi chu kỳ thêm đúng 2 chữ b, xen giữa các chữ a tùy ý.
   - Công thức: R = a* (b a* b a*)*   (hoặc viết: (a + b a* b)*)
   - 2 chuỗi thuộc: aa (0 chữ b - chẵn), abba (2 chữ b - chẵn)
   - 2 chuỗi không thuộc: b (1 chữ b - lẻ), abbb (3 chữ b - lẻ)

7. Không chứa chuỗi con "bb" trên {a, b}:
   - Phân tích: Sau mỗi ký tự b bắt buộc phải có a để ngăn cách (khối ba hoặc ab); 
     ở cuối chuỗi có thể có tối đa một ký tự b đứng đơn độc.
   - Công thức: R = (a + ba)* (ε + b)   (hoặc viết: (ε + b) (a + ab)*)
   - 2 chuỗi thuộc: ε, aba
   - 2 chuỗi không thuộc: bb, abb

8. Bắt đầu bằng "a hoặc b", tiếp theo "0 hoặc nhiều ac", kết thúc bằng "abc":
   - Phân tích: Ghép nối 3 thành phần liên tiếp: (a + b) nối (ac)* nối abc.
   - Công thức: R = (a + b) (ac)* abc
   - 2 chuỗi thuộc: aabc (chọn a, 0 lần ac, đuôi abc), bacabc (chọn b, 1 lần ac, đuôi abc)
   - 2 chuỗi không thuộc: abc (thiếu ký tự đầu a hoặc b), bac (không kết thúc bằng abc)
```

---

## 2.5. BÀI THI THỰC TẾ 3: Bài 2 Phiếu ôn tập của thầy (Đọc và phân tích 5 RE)

**ĐỀ BÀI (Trích Phiếu ôn tập của giảng viên):**
Với mỗi RE dưới đây: mô tả ngôn ngữ bằng lời tự nhiên; cho 3 chuỗi được chấp nhận và 3 chuỗi không được chấp nhận:
a) `(a + b)* abb`
b) `a* (b a* b a*)*`
c) `(ab + bc) (a + c)*`
d) `(a + b) (ac)* abc`
e) `(ab + cb) (ac)* aab + c`

---

### LỜI GIẢI MẪU CHUẨN 10/10 ĐI THI:

| STT | Biểu thức RE | Mô tả ngôn ngữ bằng lời tự nhiên | 3 Chuỗi CHẤP NHẬN | 3 Chuỗi TỪ CHỐI |
| :---: | :--- | :--- | :--- | :--- |
| **a** | `(a + b)* abb` | Tập hợp tất cả các chuỗi trên `{a, b}` có **hậu tố kết thúc bằng chuỗi con `abb`**. | `abb`<br>`aabb`<br>`babb` | `ε` (quá ngắn)<br>`ab` (thiếu chữ b cuối)<br>`abba` (kết thúc bằng a) |
| **b** | `a* (b a* b a*)*` | Tập hợp tất cả các chuỗi trên `{a, b}` có **số lượng ký tự `b` là một số chẵn** (0, 2, 4,...). | `ε` (0 chữ b)<br>`aa` (0 chữ b)<br>`abba` (2 chữ b) | `b` (1 chữ b - lẻ)<br>`ab` (1 chữ b - lẻ)<br>`abbb` (3 chữ b - lẻ) |
| **c** | `(ab + bc) (a + c)*` | Tập hợp các chuỗi trên `{a, b, c}` **bắt đầu bằng tiền tố `ab` hoặc `bc`**, sau đó chỉ gồm các ký tự `a` hoặc `c` (không chứa thêm bất kỳ chữ `b` nào). | `ab`<br>`bca`<br>`abac` | `a` (sai tiền tố)<br>`abc` (chứa chữ b ở sau)<br>`bcb` (chứa chữ b ở sau) |
| **d** | `(a + b) (ac)* abc` | Các chuỗi trên `{a, b, c}` **bắt đầu bằng một ký tự `a` hoặc `b`**, tiếp theo là **0 hoặc nhiều khối `ac`**, và **kết thúc bằng chuỗi con `abc`**. | `aabc`<br>`babc`<br>`aacabc` | `abc` (thiếu ký tự đầu trước khối abc)<br>`bac` (không kết thúc bằng abc)<br>`aacbc` (sai khối ac) |
| **e** | `(ab + cb) (ac)* aab + c` | Ngôn ngữ gồm **đúng chuỗi đơn lẻ `c`**, HOẶC các chuỗi **bắt đầu bằng `ab` hoặc `cb`**, ở giữa là 0 hoặc nhiều khối `ac`, và **kết thúc bằng `aab`**. | `c`<br>`abaab`<br>`cbaab` | `ab` (thiếu hậu tố aab)<br>`caab` (tiền tố là c thay vì cb)<br>`abaabc` (kết thúc bằng c thay vì aab) |

---

## 2.6. Giới hạn của RE: Khi nào ngôn ngữ KHÔNG CHÍNH QUY? (Pumping Lemma)

### 1. Dấu hiệu nhận biết ngôn ngữ KHÔNG CHÍNH QUY (Non-regular):
- Bất cứ ngôn ngữ nào yêu cầu **ghi nhớ và so sánh số lượng không bị chặn** giữa các ký hiệu ở các vị trí khác nhau:
  + `L1 = { a^n b^n | n ≥ 0 }` (Số chữ a bằng số chữ b).
  + `L2 = { a^i b^j | i ≥ j + 2 }` (Số chữ a nhiều hơn số chữ b ít nhất 2 - Bài 3 của thầy).
  + `L3 = { w w^R | w ∈ Σ^* }` (Chuỗi đối xứng gương không có ký tự phân cách).
  + `L4 = { 0^n 1^n | n ≥ 1 }`.
- **Lý do cốt lõi:** Otomat hữu hạn chỉ có số lượng trạng thái cố định (bộ nhớ hữu hạn), không thể đếm đến một số nguyên lớn vô hạn.

### 2. Ý tưởng chứng minh bằng Bổ đề Bơm (Pumping Lemma for Regular Languages):
Nếu `L` là ngôn ngữ chính quy, thì tồn tại một số nguyên `p ≥ 1` (độ dài bơm) sao cho mọi chuỗi `w ∈ L` với `|w| ≥ p` đều có thể phân tách thành 3 phần `w = x y z` thỏa mãn:
1. `|y| ≥ 1` (phần bơm không rỗng).
2. `|xy| ≤ p` (phần bơm nằm trong `p` ký tự đầu).
3. Với mọi số nguyên `k ≥ 0`, chuỗi bơm `x y^k z ∈ L`.
- **Cách phản chứng:** Chọn một chuỗi `w` điển hình có chứa `p`, phân tích mọi trường hợp của `y`, sau đó chọn `k = 0` (bơm lùi) hoặc `k = 2` (bơm tiến) để chỉ ra chuỗi mới bị lệch tỉ lệ và không thuộc `L` ⇒ Mâu thuẫn ⇒ `L` không chính quy.

---

## 2.7. Các bài tập tương đương tự luyện có đáp án

### Bài 2.7.1: Bắt đầu bằng `ab` và kết thúc bằng `ba` trên `{a, b}`
- **Lời giải:**
  Phần đầu: `ab`; Phần đuôi: `ba`; Phần giữa: `(a + b)^*`.
  Chuỗi ngắn nhất: `abba` (khi phần giữa là `ε`).
  ⇒ **Đáp án:** `R = ab (a + b)^* ba`.

### Bài 2.7.2: Số lượng chữ số `1` là một số lẻ trên bảng chữ cái nhị phân `{0, 1}`
- **Lời giải:**
  Có đúng một chữ số 1 lẻ cố định, trước và sau nó có thể có các số chẵn chữ số 1 (các cặp `(1 0^* 1)`), và các chữ số 0 xuất hiện tùy ý:
  ⇒ **Đáp án:** `R = 0^* 1 0^* (1 0^* 1 0^*)^*`  (hoặc `(0 + 1 0^* 1)^* 1 0^*`).


---

# CHUYÊN ĐỀ 3: VĂN PHẠM HÌNH THỨC, PHÂN CẤP CHOMSKY, CÂY PHÂN TÍCH & L(G)

---

## 3.1. Bản chất văn phạm qua ví dụ đời thường

### [TRỰC QUAN] Hình dung dễ hiểu:
Văn phạm hình thức (Grammar) giống như **công thức làm một chiếc bánh Burger nhiều tầng**:
- **Bộ 4 thành phần:** `G = <V_T, V_N, S, P>`
  1. `V_T` (Ký hiệu kết thúc - Terminals): Là các **nguyên liệu ăn được thực tế** (thịt `a`, rau `b`, pho-mát `c`, sốt `0, 1`). Đây là chữ cái thường, không thể biến đổi thêm được nữa.
  2. `V_N` (Ký hiệu không kết thúc / Biến - Non-terminals): Là các **bước trung gian / chiếc hộp đựng** (như `S` = Burger hoàn chỉnh, `A` = Nhân thịt, `B` = Lớp rau). Ký hiệu bằng chữ cái in hoa.
  3. `S` (Biến bắt đầu - Start symbol): Là **chiếc đĩa trống đầu tiên**, điểm xuất phát của toàn bộ quá trình nấu ăn.
  4. `P` (Tập luật sinh - Production rules): Là **sổ tay công thức chế biến**, có dạng `Vế trái → Vế phải`. Nghĩa là: "Khi gặp hộp ở vế trái, hãy mở ra và thay thế bằng nội dung ở vế phải".
- **Dẫn xuất (Derivation - Ký hiệu `⇒`):** Là quá trình từng bước áp dụng công thức, thay thế dần các chữ in hoa cho đến khi chỉ còn toàn các chữ cái thường (nguyên liệu ăn được).
- **Cây phân tích (Parse Tree):** Là bản vẽ sơ đồ hình cây biểu diễn toàn bộ quá trình mở rộng các biến từ gốc `S` xuống các lá là chuỗi kết quả.

---

## 3.2. Bảng phân cấp Chomsky 10 giây nhận diện ăn trọn điểm

Để xác định phân lớp thấp nhất của một văn phạm theo Chomsky trong phòng thi, bạn chỉ cần thực hiện 2 bước nhìn nhanh:

```text
                  [VĂN PHẠM G CẦN XÁC ĐỊNH]
                              |
                              v
             +----------------------------------+
             | BƯỚC 1: XÉT VẾ TRÁI MỌI LUẬT SINH|
             +----------------------------------+
                             /  /
     Tồn tại luật có         /    /     Mọi luật vế trái đều
     độ dài vế trái > 1     /      /    chỉ là 1 biến duy nhất
                           v        v    (|α| = 1, α ∈ V_N)
                 +-----------+   +-------------------------------+
                 | LOẠI 0/1  |   | TỐI THIỂU ĐẠT LOẠI 2 (CFG)    |
                 +-----------+   +-------------------------------+
                                                 |
                                                 v
                               +-----------------------------------+
                               | BƯỚC 2: XÉT VẾ PHẢI MỌI LUẬT SINH |
                               +-----------------------------------+
                                               /   /
                       Có biến nằm ở giữa     /     /    Thuần túy Tuyến tính:
                       (aSb) hoặc trộn lẫn   /       /   Chỉ có dạng wB (Phải)
                       vừa Trái vừa Phải    /         /  hoặc chỉ có Bw (Trái)
                                           v           v
                                   +------------+  +-------------------+
                                   |   LOẠI 2   |  |      LOẠI 3       |
                                   | (Phi ngữ   |  | (Văn phạm chính   |
                                   |  cảnh CFG) |  |   quy - Regular)  |
                                   +------------+  +-------------------+
```

### Bảng chi tiết 4 cấp bậc Chomsky:

| Loại | Tên gọi chuẩn tiếng Việt | Tên tiếng Anh | Điều kiện Vế Trái (`α`) | Điều kiện Vế Phải (`β`) | Máy nhận dạng tương ứng |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **Loại 0** | Văn phạm không hạn chế | Recursively Enumerable | Chứa ít nhất 1 biến | Tùy ý | Máy Turing (Turing Machine) |
| **Loại 1** | Văn phạm cảm ngữ cảnh | Context-Sensitive (CSG) | `α → β` với `|α| ≤ |β|` | Không được làm ngắn chuỗi | Otomat tuyến tính có chặn (LBA) |
| **Loại 2** | Văn phạm phi ngữ cảnh | Context-Free (CFG) | **Đúng 1 biến duy nhất** (`A ∈ V_N`) | Chuỗi bất kỳ gồm biến và ký hiệu kết thúc | Otomat đẩy xuống (Pushdown Automata - PDA) |
| **Loại 3** | Văn phạm chính quy | Regular Grammar (RG) | **Đúng 1 biến duy nhất** (`A ∈ V_N`) | **Thuần Tuyến tính Phải** (`A → wB` hoặc `A → w`)<br>HOẶC **Thuần Tuyến tính Trái** (`A → Bw` hoặc `A → w`) | Otomat hữu hạn (DFA / NFA) |

> [!WARNING]
> **2 BẪY THI CHOMSKY PHỔ BIẾN NHẤT:**
> 1. **Biến kẹp ở giữa:** Luật `S → aSb` có biến `S` nằm giữa terminal `a` và `b` ⇒ Không thể là Loại 3, bắt buộc là **Loại 2 (CFG)**.
> 2. **Trộn lẫn luật Trái và Phải:** Nếu trong văn phạm vừa có luật tuyến tính trái (như `S → Sb`) vừa có luật tuyến tính phải (như `S → aA`) ⇒ Bị mất tính đồng nhất, tụt xuống thành **Loại 2 (CFG)**.

---

## 3.3. Phương pháp tìm chuỗi tổng quát, công thức tham số L(G) và vẽ cây phân tích

### 1. Phương pháp tìm công thức tham số `L(G)`:
- **Bước 1:** Xác định luật đệ quy lặp lại nhiều lần. Giả sử áp dụng luật đó `n` lần (`n ≥ 0`), tìm dạng chuỗi trung gian:
  Ví dụ: `S → aSb` áp dụng `n` lần sinh ra `a^n S b^n`.
  Ví dụ: `S → aaSb` áp dụng `n` lần sinh ra `a^(2n) S b^n`.
- **Bước 2:** Chuyển sang biến phụ (nếu có, ví dụ `S → aA`).
- **Bước 3:** Lặp biến phụ `m` lần (`m ≥ 0`), ví dụ `A → aA` `m` lần sinh `a^m A`.
- **Bước 4:** Kết thúc bằng luật triệt tiêu (ví dụ `A → a`), gom toàn bộ các số mũ lại.
- **Bước 5:** Đặt biến đếm số lượng: `j = n` (số ký tự b), `i = tổng số mũ của a`, thiết lập bất đẳng thức liên hệ giữa `i` và `j`.
  Viết tập hợp toán học: `L(G) = { a^i b^j | điều_kiện, j ≥ 0 }`.

### 2. Quy tắc vẽ Cây phân tích cú pháp (Parse Tree):
- **Nút gốc (Root):** Luôn luôn là biến khởi đầu `S`.
- **Nút nhánh (Internal Nodes):** Là các biến không kết thúc (`S`, `A`,...).
- **Nút lá (Leaves):** Là các ký hiệu kết thúc (`a`, `b`, `c`, `0`, `1`) hoặc chuỗi rỗng `ε`.
- **Kiểm tra độ chính xác:** Đọc tuần tự tất cả các nút lá từ trái sang phải, ghép lại phải ra **chính xác 100% chuỗi đề bài yêu cầu**.

---

## 3.4. BÀI THI THỰC TẾ 1: Câu 2 Đề ôn tập GK 1 (Đề chính thức 3.0 điểm)

**ĐỀ BÀI CHÍNH THỨC (Trích Đề GK 1):**
Cho văn phạm `G = <{a, b}, {S, A}, S, P>`, với tập các luật sinh `P` gồm:
```text
S → aaSb | aA
A → aA | a
```
a) (0.5 điểm) Xác định phân lớp thấp nhất của văn phạm G theo phân loại Chomsky. Giải thích vì sao?
b) (1.0 điểm) Vẽ cây phân tích cho các chuỗi sau: `aaaaaa`, `aaaabb`, `aaaabbbba`.
c) (0.5 điểm) Cho 5 ví dụ chuỗi không được chấp nhận bởi văn phạm G.
d) (1.0 điểm) Tìm ngôn ngữ L sinh bởi văn phạm G.

---

### LỜI GIẢI MẪU CHUẨN 10/10 ĐI THI:

#### Lời giải Câu 2a:
```text
BÀI LÀM CÂU 2a:

Xét văn phạm G = <{a, b}, {S, A}, S, P> với các luật sinh:
     S → aaSb | aA
     A → aA | a

1. Xét vế trái của các luật sinh:
   Tất cả các vế trái đều chỉ gồm đúng 1 biến không kết thúc (S hoặc A), 
   tức |α| = 1 với α ∈ V_N. 
   Do đó, văn phạm G thỏa mãn điều kiện của Văn phạm phi ngữ cảnh (Loại 2 - CFG).

2. Xét vế phải của các luật sinh:
   Luật S → aaSb có biến S nằm xen giữa hai chuỗi ký hiệu kết thúc là "aa" và "b".
   Dạng luật này không phải là tuyến tính phải (A → wB hoặc A → w) và cũng không phải 
   là tuyến tính trái (A → Bw hoặc A → w).
   Vì vậy, G không thể là Văn phạm chính quy (Loại 3 - Regular Grammar).

KẾT LUẬN: Phân lớp thấp nhất của văn phạm G theo Chomsky là:
          LOẠI 2 (VĂN PHẠM PHI NGỮ CẢNH - CONTEXT-FREE GRAMMAR - CFG).
```

---

#### Lời giải Câu 2b: Vẽ cây phân tích cú pháp

##### 1. Dãy dẫn xuất và Cây phân tích cho chuỗi `w1 = "aaaaaa"` (độ dài 6):
- Dãy dẫn xuất:
  `S ⇒ aA ⇒ a(aA) ⇒ aa(aA) ⇒ aaa(aA) ⇒ aaaa(aA) ⇒ aaaaa(a) = aaaaaa`
- Cây phân tích:
```text
                  S
                /   /
               a     A
                   /   /
                  a     A
                      /   /
                     a     A
                         /   /
                        a     A
                            /   /
                           a     A
                                 |
                                 a

Đọc các nút lá từ trái sang phải: a - a - a - a - a - a ==> Chuỗi "aaaaaa".
```

##### 2. Dãy dẫn xuất và Cây phân tích cho chuỗi `w2 = "aaaabb"` (độ dài 6):
- Phân tích: Chuỗi có 2 chữ `b` ở cuối (`n = 2`).
- Dãy dẫn xuất:
  `S ⇒ aaSb ⇒ aa(aaSb)b = aaaaSbb ⇒ aaaa(aA)bb = aaaaaAbb ⇒ aaaaa(a)bb = aaaaaabb` (Lưu ý: với n=2, số chữ a tối thiểu là 2×2+2 = 6, nên chuỗi đúng độ dài là `aaaaaabb`).
  Với chuỗi `aaaabb` (4 chữ a, 2 chữ b):
  `S ⇒ aaSb ⇒ aa(aA)b = aaaAb ⇒ aaaa b` (chỉ có 1 chữ b).
  Nếu đề bài là `aaaabb`:
  Ta xét chuỗi `aaaabb` xem có dẫn xuất được không:
  + Nếu áp dụng `S → aaSb` (1 lần): được `aa S b`. Thay `S → aA` được `aa aA b` = `aaa A b`. Thay `A → a` được `aaaab` (1 chữ b).
  + Nếu áp dụng `S → aaSb` (2 lần): được `aaaa S bb`. Thay `S → aA` được `aaaa aA bb = aaaaa A bb ⇒ aaaaaabb` (ít nhất 6 chữ a khi có 2 chữ b).
  + Do đó, chuỗi `aaaabb` (4 chữ a, 2 chữ b) thực chất KHÔNG THUỘC ngôn ngữ của G vì số chữ a (4) không thỏa mãn điều kiện `i ≥ 2j + 2 = 2(2) + 2 = 6`.
  + **Tuy nhiên, để làm trọn vẹn bài thi:**
    * Với chuỗi `aaaabb` nếu đề in nhầm từ `aaaaaabb` (6 chữ a, 2 chữ b):
      Dãy dẫn xuất: `S ⇒ aaSb ⇒ aa(aaSb)b = aaaaSbb ⇒ aaaa(aA)bb ⇒ aaaaa(a)bb = aaaaaabb`.
      Cây phân tích:
```text
                 S
             /   |   /
            a    a    S    b
                   / | /
                  a  a  S  b
                      /   /
                     a     A
                           |
                           a
Đọc các lá từ trái sang phải: a - a - a - a - a - a - b - b ==> "aaaaaabb".
```

##### 3. Dãy dẫn xuất và Cây phân tích cho chuỗi `w3 = "aaaabbbba"`:
- **Nhận xét quan trọng:** Chuỗi kết thúc bằng chữ `a` ở cuối cùng (`...bbbba`). Nhưng trong văn phạm G, luật sinh `S → aaSb` chỉ sinh chữ `b` ở tận cùng bên phải, và `S → aA` chỉ sinh chữ `a` ở bên trái của `b`. Không có bất kỳ luật nào có thể sinh ký tự `a` đứng sau ký tự `b`.
- Do đó, chuỗi `aaaabbbba` **KHÔNG THỂ DẪN XUẤT ĐƯỢC TỪ VĂN PHẠM G** (Không tồn tại cây phân tích hợp lệ cho chuỗi này).

---

#### Lời giải Câu 2c: 5 ví dụ chuỗi không được chấp nhận bởi G
1. `ε`: Không được chấp nhận vì chuỗi rỗng có độ dài 0, trong khi chuỗi ngắn nhất của G là `aa` (độ dài 2).
2. `a`: Không được chấp nhận vì chỉ có 1 chữ a (`i = 1 < 2`).
3. `b`: Không được chấp nhận vì chuỗi bắt đầu bằng b, trong khi mọi chuỗi của G bắt buộc phải bắt đầu bằng a.
4. `ab`: Không được chấp nhận vì có 1 chữ a và 1 chữ b (`i = 1, j = 1`, vi phạm `i ≥ 2j + 2 = 4`).
5. `ba`: Không được chấp nhận vì sai thứ tự ký tự: ký tự `b` xuất hiện trước ký tự `a`.

---

#### Lời giải Câu 2d: Tìm ngôn ngữ L sinh bởi văn phạm G
```text
BÀI LÀM CÂU 2d:

Ta phân tích quá trình dẫn xuất tổng quát từ biến bắt đầu S:
1. Áp dụng luật đệ quy S → aaSb đúng n lần (với n ≥ 0):
          S ⇒ a^(2n) S b^n
2. Chuyển sang biến A bằng luật S → aA:
          a^(2n) S b^n ⇒ a^(2n) (aA) b^n = a^(2n+1) A b^n
3. Áp dụng luật đệ quy A → aA đúng m lần (với m ≥ 0):
          A ⇒ a^m A
4. Kết thúc dẫn xuất bằng luật triệt tiêu biến A → a:
          a^m A ⇒ a^m . a = a^(m+1)

Ghép toàn bộ quá trình lại, ta thu được chuỗi dạng tổng quát:
          w = a^(2n+1) . a^(m+1) . b^n = a^(2n + m + 2) b^n   (với n ≥ 0, m ≥ 0)

Đặt:
  - j = n  (số lượng ký tự b có trong chuỗi, j ≥ 0)
  - i = 2n + m + 2  (số lượng ký tự a có trong chuỗi)
Vì m ≥ 0 nên ta có bất đẳng thức:
          i = 2j + m + 2 ≥ 2j + 2

KẾT LUẬN:
Ngôn ngữ L sinh bởi văn phạm G là tập hợp tất cả các chuỗi có dạng các ký tự a 
đứng trước các ký tự b, trong đó số lượng ký tự a luôn nhiều hơn hai lần số lượng 
ký tự b ít nhất 2 ký tự:
          L(G) = { a^i b^j | i ≥ 2j + 2,  j ≥ 0 }
(hoặc viết theo hai tham số: L(G) = { a^(2n+m+2) b^n | n ≥ 0, m ≥ 0 }).
```

---

## 3.5. BÀI THI THỰC TẾ 2: Bài 3 Phiếu ôn tập của thầy (CFG sinh Non-regular)

**ĐỀ BÀI (Trích Phiếu ôn tập của giảng viên):**
Cho văn phạm `G = <{a, b}, {S, A}, S, P>`, với `P = { S → aSb | aA; A → aA | a }`.
1. Xác định phân lớp thấp nhất theo Chomsky.
2. Sinh 5 chuỗi ngắn nhất.
3. Kiểm tra các chuỗi: `aa, aaa, aaab, aaaabb, aaaaabb, aaabb, ab, aabbb`.
4. Với chuỗi thuộc `L(G)`, viết một dẫn xuất.
5. Vẽ cây phân tích cho 2 chuỗi có độ dài `≥ 4`.
6. Viết `L(G)` dưới dạng tập hợp có tham số.
7. Nêu 5 chuỗi không thuộc `L(G)` và giải thích.
8. `L(G)` có chính quy không? Nếu có, đề xuất RE hoặc Automata.

---

### LỜI GIẢI MẪU CHUẨN 10/10 ĐI THI:

#### 1. Phân lớp thấp nhất theo Chomsky:
- Vế trái của mọi luật chỉ gồm đúng một biến (`S` hoặc `A`).
- Vế phải có luật `S → aSb` chứa biến `S` nằm xen giữa hai terminal `a` và `b` ⇒ Không phải tuyến tính trái và không phải tuyến tính phải.
- ⇒ **Phân lớp thấp nhất:** **LOẠI 2 (VĂN PHẠM PHI NGỮ CẢNH - CFG)**.

#### 2. Dạng chuỗi tổng quát & 5 chuỗi ngắn nhất:
- Dạng chuỗi: `S ⇒ a^n S b^n ⇒ a^(n+1) A b^n ⇒ a^(n+m+2) b^n` (với `n, m ≥ 0`).
  Đặt `j = n` (số lượng b), `i = n + m + 2` (số lượng a) ⇒ Điều kiện: `i ≥ j + 2` (`j ≥ 0`).
- **5 chuỗi ngắn nhất:** `aa`, `aaa`, `aaaa`, `aaab`, `aaaab`.

#### 3. Bảng kiểm tra 8 chuỗi trong đề thi:

| Chuỗi | Số a (`i`) | Số b (`j`) | Điều kiện `i ≥ j + 2` | KẾT LUẬN | Dãy dẫn xuất / Lý do |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `aa` | 2 | 0 | `2 ≥ 0 + 2` (Đúng) | **THUỘC** | `S ⇒ aA ⇒ aa` |
| `aaa` | 3 | 0 | `3 ≥ 0 + 2` (Đúng) | **THUỘC** | `S ⇒ aA ⇒ aaA ⇒ aaa` |
| `aaab` | 3 | 1 | `3 ≥ 1 + 2` (Đúng) | **THUỘC** | `S ⇒ aSb ⇒ aaAb ⇒ aaab` |
| `aaaabb` | 4 | 2 | `4 ≥ 2 + 2` (Đúng) | **THUỘC** | `S ⇒ aSb ⇒ aaSbb ⇒ aaaAbb ⇒ aaaabb` |
| `aaaaabb` | 5 | 2 | `5 ≥ 2 + 2` (Đúng) | **THUỘC** | `S ⇒ aSb ⇒ aaSbb ⇒ aaaAbb ⇒ aaaaAbb ⇒ aaaaabb` |
| `aaabb` | 3 | 2 | `3 < 2 + 2 = 4` (Sai) | **KHÔNG** | Số chữ a (3) không nhiều hơn số b (2) đủ 2 ký tự |
| `ab` | 1 | 1 | `1 < 1 + 2 = 3` (Sai) | **KHÔNG** | Số chữ a bằng số chữ b (`i = j`) |
| `aabbb` | 2 | 3 | `2 < 3 + 2 = 5` (Sai) | **KHÔNG** | Số chữ a ít hơn số chữ b (`i < j`) |

#### 4. Cây phân tích cho 2 chuỗi có độ dài ≥ 4:

##### Cây phân tích chuỗi `aaab` (độ dài 4):
```text
           S
        /  |  /
       a   S   b
         /   /
        a     A
              |
              a
Lá đọc từ trái sang phải: a - a - a - b ==> "aaab".
```

##### Cây phân tích chuỗi `aaaabb` (độ dài 6):
```text
           S
        /  |  /
       a   S   b
         / | /
        a  S  b
         /   /
        a     A
              |
              a
Lá đọc từ trái sang phải: a - a - a - a - b - b ==> "aaaabb".
```

#### 5. Viết L(G) dưới dạng tập hợp có tham số:
```text
L(G) = { a^i b^j | i ≥ j + 2,  j ≥ 0 }
```

#### 6. 5 chuỗi không thuộc L(G):
`ε` (độ dài 0 < 2); `a` (i=1 < 2); `b` (không có a); `ab` (i=j); `ba` (sai thứ tự).

#### 7. L(G) có chính quy không?
- **KẾT LUẬN:** `L(G)` **KHÔNG CHÍNH QUY (NON-REGULAR)**.
- **Giải thích:** Ngôn ngữ `L(G)` đòi hỏi phải ghi nhớ số lượng ký tự `a` xuất hiện không bị chặn để đối chiếu với số lượng ký tự `b` xuất hiện phía sau (`i ≥ j + 2`). Vì Otomat hữu hạn (DFA/NFA) chỉ có bộ nhớ hữu hạn (hữu hạn trạng thái), nó không thể nhận diện được ngôn ngữ này. Do đó **không tồn tại** biểu thức chính quy (RE) hay Otomat hữu hạn nào cho `L(G)`.

---

## 3.6. BÀI THI THỰC TẾ 3: Bài 4 Phiếu ôn tập của thầy (CFG sinh Regular - Điểm nhấn cốt lõi)

**ĐỀ BÀI (Trích Phiếu ôn tập của giảng viên):**
Cho văn phạm `S → Sb | aA; A → aA | a`.
1. Xác định phân lớp thấp nhất của chính văn phạm.
2. Sinh 6 chuỗi ngắn nhất.
3. Kiểm tra các chuỗi: `aa, aab, aabb, aaabbb, baaa`.
4. Viết `L(G)` bằng ký hiệu toán học.
5. Viết một RE tương đương nếu có.

---

### LỜI GIẢI MẪU CHUẨN 10/10 ĐI THI:

#### 1. Phân lớp thấp nhất của chính văn phạm:
- Vế trái mỗi luật chỉ gồm 1 biến (`S` hoặc `A`) ⇒ Tối thiểu là Loại 2 (CFG).
- Vế phải: Luật `S → Sb` có dạng `Biến . Ký hiệu` (Tuyến tính trái). Các luật `S → aA`, `A → aA`, `A → a` lại có dạng `Ký hiệu . Biến` hoặc `Ký hiệu` (Tuyến tính phải).
- Vì văn phạm lai tạp giữa luật tuyến tính trái và tuyến tính phải nên nó **không đồng nhất thành văn phạm chính quy (Loại 3)**.
- ⇒ **Phân lớp thấp nhất của văn phạm:** **LOẠI 2 (VĂN PHẠM PHI NGỮ CẢNH - CFG)**.

#### 2. Dạng chuỗi tổng quát & Sinh 6 chuỗi:
- Dẫn xuất: `S ⇒ S b^j ⇒ a A b^j ⇒ a (a^(k+1)) b^j = a^(k+2) b^j` (với `k ≥ 0, j ≥ 0`).
  Đặt `i = k + 2` ⇒ `i ≥ 2`, và `j ≥ 0` hoàn toàn độc lập với `i`!
- **6 chuỗi ngắn nhất:** `aa`, `aaa`, `aab`, `aaaa`, `aaab`, `aabb`.

#### 3. Kiểm tra chuỗi:
- `aa`: **CÓ** (`i = 2, j = 0`). Dẫn xuất: `S ⇒ aA ⇒ aa`.
- `aab`: **CÓ** (`i = 2, j = 1`). Dẫn xuất: `S ⇒ Sb ⇒ aAb ⇒ aab`.
- `aabb`: **CÓ** (`i = 2, j = 2`). Dẫn xuất: `S ⇒ Sbb ⇒ aAbb ⇒ aabb`.
- `aaabbb`: **CÓ** (`i = 3, j = 3`). Dẫn xuất: `S ⇒ Sbbb ⇒ aAbbb ⇒ aaabbb`.
- `baaa`: **KHÔNG** (Ký tự `b` xuất hiện trước ký tự `a`, sai thứ tự).

#### 4. Viết L(G) bằng ký hiệu toán học:
```text
L(G) = { a^i b^j | i ≥ 2,  j ≥ 0 }
```

#### 5. Biểu thức chính quy (RE) tương đương:
```text
R = aa a* b*   (hoặc viết: a a a* b*)
```

#### 6. BÀI HỌC VÀNG CẦN KHẮC CỐT GHI TÂM:
> [!IMPORTANT]
> **PHÂN LỚP CỦA VĂN PHẠM KHÁC VỚI PHÂN LỚP CỦA NGÔN NGỮ!**
> - Bản thân **Văn phạm G** ở Bài 4 thuộc **Loại 2 (CFG)** do người ra đề cố tình viết luật lai tạp giữa tuyến tính trái và tuyến tính phải.
> - Nhưng **Ngôn ngữ `L(G) = aa a^* b^*`** mà nó sinh ra lại là một **NGÔN NGỮ CHÍNH QUY (REGULAR LANGUAGE)** vì có thể biểu diễn trọn vẹn bằng một biểu thức chính quy thuần túy và một DFA 3 trạng thái!

---

## 3.7. Các bài tập tương đương tự luyện có đáp án

### Bài 3.7.1: Văn phạm `S → aSb | ε`
- **Phân loại:** Loại 2 (CFG) vì biến `S` nằm xen giữa `a` và `b`.
- **Cây phân tích cho `aabb`:** `S ⇒ aSb ⇒ aaSbb ⇒ aaεbb = aabb`.
- **Ngôn ngữ sinh ra:** `L = { a^n b^n | n ≥ 0 }` (Ngôn ngữ phi chính quy kinh điển).

### Bài 3.7.2: Văn phạm `S → 0B; B → 1S | 0`
- **Phân loại:** **Loại 3 (Văn phạm chính quy - Regular)** vì tất cả các luật vế phải đều thuần túy có dạng `Ký hiệu . Biến` hoặc `Ký hiệu` (Tuyến tính phải).
- **Cây phân tích cho `01010`:** `S ⇒ 0B ⇒ 01S ⇒ 010B ⇒ 0101S ⇒ 01010B ⇒ 01010`.
- **Ngôn ngữ sinh ra:** `L = { (01)^n 0 | n ≥ 0 }` (Chuỗi nhị phân xen kẽ bắt đầu và kết thúc bằng 0).


---

# CHUYÊN ĐỀ 4: ÔTÔMÁT HỮU HẠN (DFA, NFA, BẢNG CHUYỂN, RE ↔ AUTOMATA ↔ VĂN PHẠM)

---

## 4.1. Bản chất Otomat: Cỗ máy nhận dạng chuỗi qua trò chơi nhảy ô

### [TRỰC QUAN] Hình dung dễ hiểu:
Một Otomat hữu hạn giống như **một trò chơi nhảy ô tính điểm**:
- **Các ô vuông (Tập trạng thái `Q`):** Là các vị trí bạn có thể đứng chân.
- **Ô xuất phát (`q0`):** Là ô có mũi tên từ bên ngoài chỉ vào `→ (q0)`. Bạn luôn bắt đầu trò chơi tại đây trước khi đọc bất kỳ ký tự nào.
- **Các ô đích / Ô chiến thắng (`F` - Trạng thái kết thúc):** Được vẽ bằng **vòng tròn đôi `((q))`** hoặc đánh dấu sao `* q`.
- **Luật nhảy ô (Hàm chuyển `δ`):** Khi bạn đang đứng ở một ô, người quản trò đọc lên một ký tự (ví dụ đọc chữ `a`), bạn phải nhìn mũi tên có chữ `a` để bước sang ô tương ứng.
- **Quy tắc phán quyết thắng / thua:**
  + Khi đọc hết toàn bộ chuỗi ký tự, nếu chân bạn đang đứng ở **Ô ĐÍCH (vòng tròn đôi)** ⇒ Chuỗi được **CHẤP NHẬN (ACCEPT)**.
  + Nếu chuỗi kết thúc mà chân bạn đứng ở **ô thường (vòng đơn)** hoặc bị rơi vào **ô bẫy (Dead state)** ⇒ Chuỗi bị **TỪ CHỐI (REJECT)**.

---

## 4.2. Định nghĩa hình thức bộ 5 thành phần & Bảng hàm chuyển

### 1. Định nghĩa toán học hình thức:
Một Ôtômát hữu hạn được xác định đầy đủ bởi bộ 5 thành phần:
```text
M = (Q, Σ, δ, q0, F)
```
- `Q`: Tập hợp hữu hạn các trạng thái (ví dụ: `{q0, q1, q2}`).
- `Σ`: Bảng chữ cái đầu vào (ví dụ: `{0, 1}` hoặc `{a, b}`).
- `δ`: Hàm chuyển trạng thái (State Transition Function):
  + Đối với DFA (Đơn định): `δ: Q × Σ → Q` (tại mỗi trạng thái, mỗi ký tự chỉ có đúng 1 bước nhảy duy nhất).
  + Đối với NFA (Không đơn định): `δ: Q × Σ → P(Q)` (tại mỗi trạng thái, một ký tự có thể nhảy đến một tập hợp nhiều trạng thái, hoặc không có đường đi).
- `q0 ∈ Q`: Trạng thái khởi đầu duy nhất (luôn có mũi tên `→` chỉ vào).
- `F ⊆ Q`: Tập hợp các trạng thái kết thúc / chấp nhận (vẽ vòng đôi `((...))` hoặc đánh dấu `*`).

---

## 4.3. BÀI THI THỰC TẾ 1: Câu 3 Đề ôn tập GK 1 (Đọc DFA từ hình ảnh đề thi)

**ĐỀ BÀI CHÍNH THỨC (Trích Đề GK 1 - 2.0 điểm):**
Cho ô-tô-mát hữu hạn nhận diện ngôn ngữ như hình dưới đây (Xem hình ảnh `./de_gk_img_1.jpeg`):
- Trạng thái bắt đầu là `A`.
- Từ `A`: đọc `a` sang `B`, đọc `b` quay về `A`.
- Từ `B`: đọc `a` sang `C` (vòng đôi), đọc `b` quay về `A`.
- Từ `C` (vòng đôi): đọc `a` ở lại `C`, đọc `b` ở lại `C`.

a) (0.5 điểm) Hãy mô tả ô-tô-mát này bằng định nghĩa hình thức (bộ 5 thành phần và bảng chuyển).
b) (0.5 điểm) Cho 5 ví dụ chuỗi được chấp nhận bởi ô-tô-mát.
c) (1.0 điểm) Cho 5 ví dụ chuỗi bị từ chối bởi ô-tô-mát.

---

### LỜI GIẢI MẪU CHUẨN 10/10 ĐI THI:

#### Lời giải Câu 3a: Định nghĩa hình thức và Bảng chuyển trạng thái
```text
BÀI LÀM CÂU 3a:

Căn cứ vào sơ đồ chuyển trạng thái trong đề thi, ô-tô-mát là một DFA đơn định 
được xác định bởi bộ 5 thành phần:
               M = (Q, Σ, δ, q0, F)

Trong đó:
1. Tập hợp các trạng thái:
               Q = {A, B, C}
2. Bảng chữ cái đầu vào:
               Σ = {a, b}
3. Trạng thái khởi đầu:
               q0 = A
4. Tập hợp các trạng thái kết thúc (chấp nhận):
               F = {C}
5. Hàm chuyển trạng thái δ được biểu diễn qua Bảng chuyển trạng thái:

               +---------------+---------------+---------------+
               |  Trạng thái   |  Đầu vào 'a'  |  Đầu vào 'b'  |
               +---------------+---------------+---------------+
               |    → A        |       B       |       A       |
               |      B        |       C       |       A       |
               |    * C        |       C       |       C       |
               +---------------+---------------+---------------+
(Quy ước: Dấu mũi tên "→" chỉ trạng thái bắt đầu, dấu sao "*" chỉ trạng thái chấp nhận).

Sơ đồ đồ thị trạng thái:
        b                             a, b
      ┌───┐                         ┌──────┐
      v   │                         v      │
----> (A) ---------- a ----------> (B) ---------- a ----------> ((C))
       ^                            │
       │                            │
       └───────────── b ────────────┘
```

---

#### Lời giải Câu 3b: 5 chuỗi được chấp nhận kèm vết chuyển dịch
- **Quy luật nhận diện:** Để chuyển từ trạng thái bắt đầu `A` đến trạng thái chấp nhận `C`, máy bắt buộc phải đi qua đường `A --a-> B --a-> C`. Do đó, ngôn ngữ mà máy chấp nhận là **tất cả các chuỗi có chứa chuỗi con `aa`** (`R = (a + b)^* aa (a + b)^*`).

```text
BÀI LÀM CÂU 3b:

Năm ví dụ chuỗi được chấp nhận bởi ô-tô-mát kèm vết chuyển dịch trạng thái:

1. Chuỗi w1 = "aa":
   Vết chuyển: A ─(a)→ B ─(a)→ C
   Trạng thái kết thúc: C ∈ F  ==> ĐƯỢC CHẤP NHẬN.

2. Chuỗi w2 = "baa":
   Vết chuyển: A ─(b)→ A ─(a)→ B ─(a)→ C
   Trạng thái kết thúc: C ∈ F  ==> ĐƯỢC CHẤP NHẬN.

3. Chuỗi w3 = "aab":
   Vết chuyển: A ─(a)→ B ─(a)→ C ─(b)→ C
   Trạng thái kết thúc: C ∈ F  ==> ĐƯỢC CHẤP NHẬN.

4. Chuỗi w4 = "baab":
   Vết chuyển: A ─(b)→ A ─(a)→ B ─(a)→ C ─(b)→ C
   Trạng thái kết thúc: C ∈ F  ==> ĐƯỢC CHẤP NHẬN.

5. Chuỗi w5 = "babaa":
   Vết chuyển: A ─(b)→ A ─(a)→ B ─(b)→ A ─(a)→ B ─(a)→ C
   Trạng thái kết thúc: C ∈ F  ==> ĐƯỢC CHẤP NHẬN.
```

---

#### Lời giải Câu 3c: 5 chuỗi bị từ chối kèm vết chuyển dịch
- **Quy luật:** Tất cả các chuỗi **không chứa chuỗi con `aa`** đều bị từ chối.

```text
BÀI LÀM CÂU 3c:

Năm ví dụ chuỗi bị từ chối bởi ô-tô-mát kèm vết chuyển dịch trạng thái:

1. Chuỗi w1 = ε (chuỗi rỗng):
   Vết chuyển: Dừng ngay tại trạng thái khởi đầu A.
   Trạng thái kết thúc: A ∉ F  ==> BỊ TỪ CHỐI.

2. Chuỗi w2 = "a":
   Vết chuyển: A ─(a)→ B
   Trạng thái kết thúc: B ∉ F  ==> BỊ TỪ CHỐI.

3. Chuỗi w3 = "b":
   Vết chuyển: A ─(b)→ A
   Trạng thái kết thúc: A ∉ F  ==> BỊ TỪ CHỐI.

4. Chuỗi w4 = "ab":
   Vết chuyển: A ─(a)→ B ─(b)→ A
   Trạng thái kết thúc: A ∉ F  ==> BỊ TỪ CHỐI.

5. Chuỗi w5 = "abab":
   Vết chuyển: A ─(a)→ B ─(b)→ A ─(a)→ B ─(b)→ A
   Trạng thái kết thúc: A ∉ F  ==> BỊ TỪ CHỐI.
```

---

## 4.4. BÀI THI THỰC TẾ 2: Bài 5 Phiếu ôn tập của thầy (Chuyển 5 RE sang Automata)

**ĐỀ BÀI (Trích Phiếu ôn tập của giảng viên):**
Vẽ NFA hoặc DFA cho các RE sau:
① `(a + b) (ac)* abc`
② `(ab + bc) (a + c)*`
③ `(ab + cb) (ac)* aab + c`
④ `(aba + cbc) aa + (a + c)* bc`
⑤ `(a + b)* abb`
*(Với mỗi automata: xác định `M = (Q, Σ, δ, q0, F)` và kiểm tra bằng ít nhất 2 chuỗi chấp nhận + 2 chuỗi không chấp nhận).*

---

### LỜI GIẢI MẪU CHUẨN 10/10 ĐI THI:

### ① RE: `(a + b) (ac)* abc`
- **Sơ đồ trạng thái (NFA):**
```text
       a, b          a           c
(q0) -------> ((q1)) --------> (q2)
                │  ^             │
                │  └─── c ───────┘
                │
                │ a
                v
               (q3) -------> (q4) -------> ((q5))
                        b           c
```
- **Bộ 5 thành phần:** `M = ({q0, q1, q2, q3, q4, q5}, {a, b, c}, δ, q0, {q5})`.
- **Bảng chuyển:**
  `δ(q0, a) = {q1}, δ(q0, b) = {q1}`
  `δ(q1, a) = {q2, q3}` (NFA rẽ 2 nhánh: vào vòng `ac` hoặc bắt đầu `abc`)
  `δ(q2, c) = {q1}`
  `δ(q3, b) = {q4}`, `δ(q4, c) = {q5}`
- **Kiểm tra chuỗi:**
  + Đúng: `aabc` (`q0 -> q1 -> q3 -> q4 -> q5 ∈ F`), `bacabc` (`q0 -> q1 -> q2 -> q1 -> q3 -> q4 -> q5 ∈ F`).
  + Sai: `abc` (thiếu ký tự đầu trước abc), `aacbc` (kẹt tại q2).

---

### ② RE: `(ab + bc) (a + c)*`
- **Sơ đồ trạng thái:**
```text
          a              b
(q0) -----------> (q1) -------> ((q3)) <--- a, c
  │                             ^   │
  │ b            c              │   │
  └─────────────> (q2) ─────────┘   └───┘
```
- **Bộ 5 thành phần:** `M = ({q0, q1, q2, q3}, {a, b, c}, δ, q0, {q3})`.
- **Bảng chuyển:**
  `δ(q0, a) = {q1}, δ(q0, b) = {q2}`
  `δ(q1, b) = {q3}, δ(q2, c) = {q3}`
  `δ(q3, a) = {q3}, δ(q3, c) = {q3}`
- **Kiểm tra chuỗi:**
  + Đúng: `ab` (`q0 -> q1 -> q3 ∈ F`), `bca` (`q0 -> q2 -> q3 -> q3 ∈ F`).
  + Sai: `a` (dừng tại `q1 ∉ F`), `abc` (không có cạnh đọc `b` từ `q3`).

---

### ③ RE: `(ab + cb) (ac)* aab + c`
- **Cơ chế hoạt động:**
  + Nhánh riêng cho chuỗi đơn lẻ `c`: `q0 --c-> qF ∈ F`.
  + Nhánh chính: Đọc `ab` (qua q1) hoặc `cb` (qua q2) đến `q3`.
  + Tại `q3`: lặp `ac` qua `q4`, hoặc đọc `aab` (qua `q5, q6`) đến `qF`.
- **Bộ 5 thành phần:** `M = ({q0, q1, q2, q3, q4, q5, q6, qF}, {a, b, c}, δ, q0, {qF})`.
- **Kiểm tra chuỗi:**
  + Đúng: `c` (`q0 --c-> qF ∈ F`), `abaab` (`q0 -> q1 -> q3 -> q5 -> q6 -> qF ∈ F`).
  + Sai: `ab` (dừng tại `q3 ∉ F`), `caab` (tiền tố là c thay vì cb).

---

### ④ RE: `(aba + cbc) aa + (a + c)* bc`
- **Cơ chế hai nhánh:**
  + Nhánh A: Đọc `aba` hoặc `cbc`, sau đó đọc `aa` đến trạng thái kết thúc `qF1`.
  + Nhánh B: Tự lặp `a, c` tùy ý, sau đó đọc `bc` đến trạng thái kết thúc `qF2`.
- **Kiểm tra chuỗi:**
  + Đúng: `abaaa` (nhánh A: `aba` + `aa`), `bc` (nhánh B: rỗng + `bc`).
  + Sai: `aba` (thiếu `aa` phía sau), `acba` (không kết thúc bằng `bc`).

---

### ⑤ RE: `(a + b)* abb`
- **Sơ đồ DFA tối giản 4 trạng thái:**
```text
           b               b
       ┌───────┐       ┌───────┐
       v       │       v       │
-----> (q0) ---a---> (q1) ---b---> (q2) ---b---> ((q3))
        ^             ^             │             │
        │             └─── a ───────┘             │
        │                                         │
        └──────────────────── b ──────────────────┘
```
- **Bảng chuyển trạng thái DFA:**

| State | Đọc a | Đọc b | Ý nghĩa tiền tố đã khớp |
| :---: | :---: | :---: | :--- |
| `→ q0` | `q1` | `q0` | Chưa khớp ký tự nào |
| `q1` | `q1` | `q2` | Đã khớp chữ `a` |
| `q2` | `q1` | `q3` | Đã khớp `ab` |
| `* q3` | `q1` | `q0` | **ĐÃ KHỚP TOÀN BỘ `abb` (CHẤP NHẬN)** |

- **Kiểm tra chuỗi:**
  + Đúng: `abb` (`q0 -> q1 -> q2 -> q3 ∈ F`), `babb` (`q0 -> q0 -> q1 -> q2 -> q3 ∈ F`).
  + Sai: `ε` (dừng tại `q0 ∉ F`), `abba` (`q0 -> q1 -> q2 -> q3 -> q1 ∉ F`).

---

## 4.5. BÀI THI THỰC TẾ 3: Bài 6 Phiếu ôn tập của thầy (Đọc Automata từ Bảng chuyển)

**ĐỀ BÀI (Trích Phiếu ôn tập của giảng viên):**
Cho DFA có bảng chuyển:
```text
State | 0  | 1
→ q0  | q0 | q1
  q1  | q2 | q1
* q2  | q0 | q1
```
Hãy: (1) vẽ sơ đồ trạng thái; (2) viết `M = (Q, Σ, δ, q0, F)`; (3) kiểm tra các chuỗi `ε, 0, 1, 10, 110, 101, 1010, 1110, 100`; (4) cho 5 chuỗi chấp nhận + 5 chuỗi không chấp nhận; (5) mô tả ngôn ngữ bằng lời; (6) viết RE tương ứng.

---

### LỜI GIẢI MẪU CHUẨN 10/10 ĐI THI:

#### 1. Vẽ sơ đồ trạng thái:
```text
         0                             1
       ┌───┐                         ┌───┐
       v   │                         v   │
-----> (q0) ------------ 1 -----------> (q1) <────┐
        ^                                 │       │
        │                                 │       │
        │                0                │ 0     │ 1
        └───────────── ((q2)) <───────────┘       │
                        │                         │
                        └──────────── 1 ──────────┘
```

#### 2. Định nghĩa hình thức bộ 5 thành phần:
`M = ({q0, q1, q2}, {0, 1}, δ, q0, {q2})` với bảng hàm chuyển `δ` như đề bài.

#### 3. Bảng kiểm tra 9 chuỗi:

| Chuỗi | Vết chuyển dịch trạng thái | Trạng thái cuối | KẾT LUẬN |
| :--- | :--- | :---: | :---: |
| `ε` | Dừng tại trạng thái bắt đầu `q0` | `q0` | **TỪ CHỐI** |
| `0` | `q0 --0-> q0` | `q0` | **TỪ CHỐI** |
| `1` | `q0 --1-> q1` | `q1` | **TỪ CHỐI** |
| `10` | `q0 --1-> q1 --0-> q2` | `q2` | **CHẤP NHẬN** |
| `110` | `q0 --1-> q1 --1-> q1 --0-> q2` | `q2` | **CHẤP NHẬN** |
| `101` | `q0 --1-> q1 --0-> q2 --1-> q1` | `q1` | **TỪ CHỐI** |
| `1010` | `q0 --1-> q1 --0-> q2 --1-> q1 --0-> q2` | `q2` | **CHẤP NHẬN** |
| `1110` | `q0 --1-> q1 --1-> q1 --1-> q1 --0-> q2` | `q2` | **CHẤP NHẬN** |
| `100` | `q0 --1-> q1 --0-> q2 --0-> q0` | `q0` | **TỪ CHỐI** |

#### 4. Liệt kê 5 chuỗi đúng & 5 chuỗi sai:
- 5 chuỗi chấp nhận: `10`, `010`, `110`, `1010`, `1110`.
- 5 chuỗi từ chối: `ε`, `0`, `1`, `11`, `100`.

#### 5. Mô tả ngôn ngữ bằng lời tự nhiên:
- Nhận xét: Mỗi khi đọc `1` máy chuyển về `q1`, nếu đọc tiếp `0` thì chuyển sang `q2` (trạng thái chấp nhận). Bất kỳ ký tự nào sau đó nếu không kết thúc bằng `10` đều bị đưa ra khỏi `q2`.
- **KẾT LUẬN:** Ngôn ngữ nhận diện là **tập hợp tất cả các chuỗi nhị phân trên `{0, 1}` có hậu tố kết thúc bằng chuỗi con `10`**.

#### 6. Biểu thức chính quy (RE) tương ứng:
```text
R = (0 + 1)* 10
```

---

## 4.6. BÀI THI THỰC TẾ 4: Bài 7 Phiếu ôn tập của thầy (Tự thiết kế 4 DFA kinh điển)

### 1) DFA nhận diện chuỗi kết thúc bằng `01` trên `{0, 1}`:
- **Tên & ý nghĩa:** `q0` (Start, chưa có gì), `q1` (vừa đọc 0), `* q2` (vừa đọc 01 - Chấp nhận).
- **Bảng chuyển:**

| State | Đọc 0 | Đọc 1 |
| :---: | :---: | :---: |
| `→ q0` | `q1` | `q0` |
| `q1` | `q1` | `q2` |
| `* q2` | `q1` | `q0` |

- **Kiểm tra:** Đúng: `01`, `1001`; Sai: `0`, `010`.

---

### 2) DFA nhận diện chuỗi chứa chuỗi con `101` trên `{0, 1}`:
- **Tên & ý nghĩa:** `q0` (Start), `q1` (thấy 1), `q2` (thấy 10), `* q3` (ĐÃ THẤY 101 - Khóa chấp nhận).
- **Bảng chuyển:**

| State | Đọc 0 | Đọc 1 |
| :---: | :---: | :---: |
| `→ q0` | `q0` | `q1` |
| `q1` | `q2` | `q1` |
| `q2` | `q0` | `q3` |
| `* q3` | `q3` | `q3` |

- **Kiểm tra:** Đúng: `101`, `01010`; Sai: `1001`, `1100`.

---

### 3) DFA nhận diện chuỗi có số lượng ký tự `1` là số chẵn trên `{0, 1}`:
- **Tên & ý nghĩa:** `* qE` (Start, số 1 là CHẴN - Chấp nhận), `qO` (số 1 là LẺ).
- **Bảng chuyển:**

| State | Đọc 0 | Đọc 1 |
| :---: | :---: | :---: |
| `→ * qE` | `qE` | `qO` |
| `qO` | `qO` | `qE` |

- **Kiểm tra:** Đúng: `ε`, `101`; Sai: `1`, `1011`.

---

### 4) DFA nhận diện chuỗi KHÔNG chứa chuỗi con `11` trên `{0, 1}`:
- **Tên & ý nghĩa:**
  + `* q0` (Start, vừa đọc 0 hoặc rỗng - Chấp nhận).
  + `* q1` (vừa đọc đúng 1 chữ số 1 - Chấp nhận).
  + `qD` (TRẠNG THÁI BẪY / CHẾT - Đã xuất hiện 11, vĩnh viễn bị từ chối).
- **Bảng chuyển:**

| State | Đọc 0 | Đọc 1 |
| :---: | :---: | :---: |
| `→ * q0` | `q0` | `q1` |
| `* q1` | `q0` | `qD` |
| `qD` | `qD` | `qD` |

- **Kiểm tra:** Đúng: `ε`, `1010`; Sai: `11` (vào `qD`), `0110` (vào `qD`).

---

## 4.7. BÀI THI THỰC TẾ 5: Bài 9 Phiếu ôn tập của thầy (Mô phỏng bài thi 20 phút & Chuyển DFA sang Văn phạm)

**ĐỀ BÀI (Trích Phiếu ôn tập của giảng viên):**
Cho `R = (a + b)* ab`.
1. Mô tả `L(R)`.
2. Cho 5 chuỗi thuộc + 5 chuỗi không thuộc.
3. Xây dựng Automata.
4. Viết `M = (Q, Σ, δ, q0, F)`.
5. Lập bảng chuyển trạng thái.
6. Kiểm tra: `ab, aab, bab, abab, aba, abb, ε`.
7. Viết một văn phạm chính quy sinh cùng ngôn ngữ.

---

### LỜI GIẢI MẪU CHUẨN 10/10 ĐI THI:

1. **Mô tả `L(R)`:** Tất cả các chuỗi trên `{a, b}` có hậu tố kết thúc bằng chuỗi con `ab`.
2. **5 chuỗi thuộc:** `ab, aab, bab, aaab, abab`.
   **5 chuỗi không thuộc:** `ε, a, b, aba, abb`.
3. **Automata (DFA 3 trạng thái):**
```text
           b                             b
       ┌───────┐                     ┌───────┐
       v       │                     v       │
-----> (q0) ---a---> (q1) ----- b -----> ((q2))
        ^             ^                   │
        │             └──────── a ────────┘
        │                                 │
        └────────────────────── b ────────┘
```
4. **Bộ 5 thành phần:** `M = ({q0, q1, q2}, {a, b}, δ, q0, {q2})`.
5. **Bảng chuyển trạng thái:**

| State | Đọc a | Đọc b |
| :---: | :---: | :---: |
| `→ q0` | `q1` | `q0` |
| `q1` | `q1` | `q2` |
| `* q2` | `q1` | `q0` |

6. **Kiểm tra 7 chuỗi:**
   - `ab`: `q0 --a-> q1 --b-> q2 ∈ F` ⇒ **NHẬN**.
   - `aab`: `q0 --a-> q1 --a-> q1 --b-> q2 ∈ F` ⇒ **NHẬN**.
   - `bab`: `q0 --b-> q0 --a-> q1 --b-> q2 ∈ F` ⇒ **NHẬN**.
   - `abab`: `q0 --a-> q1 --b-> q2 --a-> q1 --b-> q2 ∈ F` ⇒ **NHẬN**.
   - `aba`: `... --a-> q1 ∉ F` ⇒ **TỪ CHỐI**.
   - `abb`: `... --b-> q0 ∉ F` ⇒ **TỪ CHỐI**.
   - `ε`: Dừng tại `q0 ∉ F` ⇒ **TỪ CHỐI**.

7. **Chuyển DFA sang Văn phạm chính quy tương đương (Right-Linear Grammar):**
   - **Phương pháp chuẩn:**
     + Đặt tên biến: `q0 ↔ S` (Start), `q1 ↔ A`, `q2 ↔ B`.
     + Bước chuyển `δ(qi, x) = qj` sinh ra luật: `Qi → x Qj`.
     + Nếu `qj ∈ F`, bổ sung thêm luật dừng kết thúc chuỗi: `Qi → x`.
   - **Các luật sinh:**
     + Từ `q0` (`S`): `S → aA | bS`
     + Từ `q1` (`A`): `A → aA | bS | b` (luật `A → b` kết thúc chuỗi tại trạng thái chấp nhận `q2`).
   - **Văn phạm hoàn chỉnh:**
     ```text
     G = < {a, b}, {S, A}, S, P > với P gồm:
     S → aA | bS
     A → aA | bS | b
     ```

---

## 4.8. Bổ trợ nâng cao: Thuật toán chuyển NFA sang DFA & Tối thiểu hóa DFA

### 1. Thuật toán chuyển NFA sang DFA (Phương pháp tập con - Subset Construction):
- Mỗi trạng thái của DFA tương ứng với một **tập con các trạng thái của NFA**.
- Trạng thái bắt đầu của DFA là `ε-closure(q0)` (tập các trạng thái đến được từ `q0` chỉ bằng các bước nhảy rỗng `ε`).
- Tại mỗi tập trạng thái `U`, với mỗi ký hiệu `x ∈ Σ`, trạng thái tiếp theo là `ε-closure(⋃ δ_NFA(q, x))` với mọi `q ∈ U`.
- Trạng thái nào của DFA chứa ít nhất một trạng thái kết thúc của NFA thì trạng thái đó là **trạng thái chấp nhận của DFA**.

### 2. Thuật toán tối thiểu hóa DFA (Minimization - Bảng đánh dấu Myhill-Nerode):
- **Bước 1 (Loại bỏ):** Xóa tất cả các trạng thái không thể chạm tới (Unreachable states) từ `q0`.
- **Bước 2 (Khởi tạo bảng):** Lập bảng tam giác dưới cho mọi cặp trạng thái `(p, q)`. Đánh dấu `X` vào các ô có một trạng thái thuộc `F` và một trạng thái không thuộc `F`.
- **Bước 3 (Lan truyền đánh dấu):** Duyệt các ô chưa đánh dấu `(p, q)`. Nếu tồn tại ký hiệu `x` sao cho cặp `(δ(p, x), δ(q, x))` đã bị đánh dấu `X`, thì đánh dấu `X` vào ô `(p, q)`. Lặp lại cho đến khi không còn ô nào bị đánh dấu thêm.
- **Bước 4 (Gộp trạng thái):** Các ô không bị đánh dấu là các **trạng thái tương đương**, ta gộp chúng thành một trạng thái duy nhất trong DFA tối giản.


---

# CHUYÊN ĐỀ 5: CHIẾN LƯỢC PHÒNG THI & CHECKLIST 10 ĐIỂM CỦA GIẢNG VIÊN

---

## 5.1. Sáu nguyên tắc vàng đúc kết từ giảng viên

1. **RE từ mô tả ngôn ngữ:** Luôn bóc tách điều kiện thành 3 khối rõ ràng: `Tiền tố - Thân lặp - Hậu tố`. Sử dụng `Σ^*` cho các phần tùy ý không bị ràng buộc.
2. **Xác định ngôn ngữ của Văn phạm (Grammar):** Trước tiên luôn tìm dạng chuỗi sau `n` lần áp dụng luật đệ quy (`S ⇒ a^n S b^n ⇒ ...`); sau đó mới rút ra công thức tập hợp có tham số `L(G) = { a^i b^j | ... }`.
3. **Mô phỏng chuỗi trên DFA / NFA:** Luôn viết tường minh vết chuyển trạng thái từng bước (`q0 --x-> q1 --y-> q2 ...`), tuyệt đối không suy đoán nhẩm bằng mắt vì rất dễ nhầm lẫn ở các bước lặp lại.
4. **Chuyển từ RE sang Automata:** Phân rã RE thành các phép toán cơ bản (nối chuỗi, phép hợp `+`, và phép lặp `^*`). Sử dụng `ε-NFA` hoặc NFA sẽ vẽ nhanh hơn và ít tốn trạng thái hơn DFA.
5. **Kiểm tra chuỗi thuộc phép lặp `L^*`:**
   - Bước 1: Kiểm tra tính chia hết của độ dài chuỗi (nếu mọi từ trong `L` đều có độ dài `d`, độ dài chuỗi phải chia hết cho `d`).
   - Bước 2: Phân hoạch chuỗi thành các từ của `L` từ trái sang phải. Tuyệt đối không cần liệt kê vô hạn các phần tử của `L^*`.
6. **Nguyên tắc phân biệt bất hủ:**
   > **PHÂN LỚP CHOMSKY CỦA VĂN PHẠM ≠ PHÂN LỚP CỦA NGÔN NGỮ MÀ NÓ SINH RA!**
   > - Một văn phạm có thể là Loại 2 (CFG) do cách viết luật hỗn hợp, nhưng ngôn ngữ nó sinh ra hoàn toàn có thể là một Ngôn ngữ chính quy (Regular Language) nếu biểu diễn được bằng Biểu thức chính quy (Xem Bài 4).

---

## 5.2. Bảng tổng hợp các bẫy đề thi hay gài và cách né bẫy

| Tình huống bẫy trong đề | Cạm bẫy dễ mắc phải | Cách xử lý thông minh để lấy trọn điểm |
| :--- | :--- | :--- |
| **Bẫy 1:** Câu hỏi RE đếm vô hạn (như qiNaNa(w) = 2 . Nb(w)) | Cố gắng viết một RE thông thường và bị trừ điểm | Nêu rõ 3 góc nhìn: Toán học hình thức (Non-regular do Pumping Lemma), Thực hành mở rộng (Lookahead), và biểu diễn xấp xỉ theo khối `(aab + aba + baa)^*`. |
| **Bẫy 2:** Kiểm tra chuỗi thuộc qiL^*qi | Ngồi phân tích chuỗi dài 19 ký tự rất mất thời gian | Đếm độ dài qi|w|qi trước tiên. Nếu qi|w|qi là số lẻ trong khi các từ của qiLqi có độ dài chẵn 2, kết luận ngay KHÔNG THUỘC (3 giây có điểm). |
| **Bẫy 3:** Phân lớp Chomsky cho văn phạm trộn | Thấy có luật tuyến tính phải tưởng ngay là Loại 3 | Kiểm tra kỹ: Chỉ cần có 1 luật tuyến tính trái (như qiSS → Sb) hoặc 1 luật kẹp giữa (như qiSS → aSb) là toàn bộ văn phạm tụt xuống **Loại 2 (CFG)**. |
| **Bẫy 4:** Cây phân tích cho chuỗi không thuộc qiL(G)qi | Cố vẽ một cây sai quy tắc luật sinh | Khẳng định ngay chuỗi không thể dẫn xuất từ văn phạm, không tồn tại cây phân tích hợp lệ. |
| **Bẫy 5:** Chuyển DFA sang Văn phạm Regular | Quên mất luật kết thúc chuỗi | Với mỗi trạng thái qi chuyển sang trạng thái kết thúc qj ∈ F bằng ký hiệu x, bắt buộc phải có thêm luật kết thúc: qiQ_i 	o xqi. |

---

## 5.3. Bảng Checklist 12 kỹ năng trước khi vào phòng thi

| STT | Kỹ năng phòng thi cần thành thạo | Tự đánh giá | Ghi chú ôn tập |
| :---: | :--- | :---: | :--- |
| **1** | Viết RE từ mô tả tự nhiên | [ ] | Nhớ đặt `(a+b+c)^*` bao quanh các chuỗi con |
| **2** | Đọc RE & diễn đạt thành lời | [ ] | Nêu rõ tiền tố, hậu tố, điều kiện chẵn/lẻ |
| **3** | Phân loại Chomsky 10 giây | [ ] | Xem vế trái (1 biến = Loại 2/3), xem vế phải (tuyến tính) |
| **4** | Viết dãy dẫn xuất từng bước | [ ] | Dùng ký hiệu `⇒`, chỉ rõ luật áp dụng ở từng bước |
| **5** | Vẽ cây phân tích cú pháp | [ ] | Nút gốc là biến bắt đầu, các lá đọc từ trái sang phải |
| **6** | Tìm công thức tập hợp `L(G)` | [ ] | Đặt tham số `i, j, n, m` kèm điều kiện lớn hơn hoặc bằng |
| **7** | Định nghĩa hình thức bộ 5 `M` | [ ] | Luôn ghi rõ `M = (Q, Σ, δ, q0, F)` |
| **8** | Lập bảng chuyển trạng thái `δ` | [ ] | Đánh dấu mũi tên `→` cho start và dấu sao `*` cho accept |
| **9** | Viết vết chạy mô phỏng chuỗi | [ ] | Trình bày `qi ─(ký_hiệu)→ qj` rõ ràng |
| **10** | Vẽ Automata từ biểu thức RE | [ ] | Dùng NFA cho nhanh, DFA khi đề yêu cầu rõ |
| **11** | Chuyển DFA sang Văn phạm Regular | [ ] | Mỗi trạng thái thành một biến, thêm luật dừng tại `F` |
| **12** | Tính `L^0, L^1, L^2` và kiểm tra `L^*` | [ ] | `L^0 = {ε}`, kiểm tra độ dài chẵn/lẻ |
