# CẨM NANG TOÀN DIỆN LÝ THUYẾT & PHƯƠNG PHÁP GIẢI CÁC DẠNG BÀI THI GIỮA KỲ

## MÔN: LÝ THUYẾT OTOMAT VÀ NGÔN NGỮ HÌNH THỨC (IUH)

### (TÀI LIỆU DÀNH CHO NGƯỜI MỚI BẮT ĐẦU TỪ CON SỐ 0 - ĐỌC LÀ HIỂU - ĐI THI LÀ ĂN ĐIỂM TUYỆT ĐỐI)

> **Tài liệu học tập & Ôn thi độc quyền chuẩn cấu trúc đề thi giữa kỳ:**
>
> - Bám sát đề thi thực tế: `Automata - Đề ôn tập GK 1.pdf`
> - Tích hợp đầy đủ slide bài giảng từ Tuần 1 đến Tuần 8: Khái niệm cơ bản, Văn phạm Chomsky, Otomat hữu hạn (DFA/NFA), Biểu thức chính quy (Regex).
> - Chuẩn hóa ký hiệu 100% tiếng Việt & Unicode trực quan (`→`, `∅`, `★`, `Σ`, `δ`, `ε`, `∈`, `∉`, `∪`, `∩`, `^*`, `^+`, `⇒`). Không sử dụng mã LaTeX gây lỗi font.

---

# LỜI NÓI ĐẦU: CHIẾN LƯỢC ĂN TRỌN 10 ĐIỂM THI GIỮA KỲ

Đề thi giữa kỳ môn **Lý thuyết Otomat & Ngôn ngữ hình thức** tại IUH thường gồm **4 câu lớn** (thời gian làm bài 60 phút, thang điểm 10):

1. **Câu 1 (2.0 điểm): Biểu thức chính quy (Regular Expressions - Regex)**
   - Yêu cầu: Xây dựng biểu thức chính quy đại diện cho ngôn ngữ thỏa mãn tính chất cho trước.
   - Bẫy thi: Đề bài yêu cầu ngôn ngữ không chính quy (đòi hỏi đếm số lượng không giới hạn) thì phải biết chứng minh bằng Bổ đề Bơm (Pumping Lemma) hoặc giải thích rõ.
2. **Câu 2 (3.0 điểm): Văn phạm hình thức (Grammar G) & Phân cấp Chomsky & Cây phân tích (Parse Tree)**
   - Yêu cầu: Xác định phân lớp Chomsky thấp nhất; vẽ cây phân tích cho các chuỗi thuộc G; tìm ví dụ chuỗi không thuộc G; xác định ngôn ngữ L(G).
   - Bẫy thi: Nhầm lẫn giữa Loại 2 (Phi ngữ cảnh) và Loại 3 (Chính quy); vẽ cây phân tích sai thứ tự các nút lá.
3. **Câu 3 (2.0 điểm): Ôtômát hữu hạn (Finite Automata - DFA/NFA)**
   - Yêu cầu: Mô tả Otomat bằng định nghĩa bộ 5 thành phần `M = 〈Q, Σ, δ, q0, F〉`; cho 5 ví dụ chuỗi được chấp nhận; cho 5 ví dụ chuỗi bị từ chối.
   - Bí quyết: Luôn ghi kèm vết chuyển trạng thái (`q0 ─(w)→ ... ─(w)→ qf ∈ F`) để được trọn vẹn điểm trình bày.
4. **Câu 4 (3.0 điểm): Các phép toán trên từ & Ngôn ngữ - Trọng tâm Phép lặp `L^*` (Kleene Star)**
   - Yêu cầu: Nêu định nghĩa toán học chuẩn của phép lặp `L^*`; kiểm tra các chuỗi có lũy thừa phức tạp xem có thuộc `L^*` hay không.
   - Bí quyết: Thuật toán kiểm tra tính chẵn/lẻ của độ dài chuỗi và phương pháp chia khối 2 ký tự.

Chỉ cần bạn nắm vững cẩm nang này, dù chưa từng học buổi nào trên lớp, bạn cũng hoàn toàn tự tin đạt điểm 9 - 10!

---

# MỤC LỤC

- [1. CHUYÊN ĐỀ 1: BẢNG CHỮ CÁI, CHUỖI VÀ PHÉP LẶP NGÔN NGỮ L* (TRỌNG TÂM CÂU 4)](#1-chuyên-đề-1-bảng-chữ-cái-chuỗi-và-phép-lặp-ngôn-ngữ-l-trọng-tâm-câu-4)
  - [1.1. Bảng chữ cái, Từ và Chuỗi rỗng](#11-bảng-chữ-cái-từ-và-chuỗi-rỗng)
  - [1.2. Các phép toán trên từ](#12-các-phép-toán-trên-từ)
  - [1.3. Ngôn ngữ và Phép nhân ghép ngôn ngữ](#13-ngôn-ngữ-và-phép-nhân-ghép-ngôn-ngữ)
  - [1.4. ĐỊNH NGHĨA CHUẨN ĐI THI CỦA PHÉP LẶP NGÔN NGỮ L* (BAO ĐÓNG KLEENE)](#14-định-nghĩa-chuẩn-đi-thi-của-phép-lặp-ngôn-ngữ-l-bao-đóng-kleene)
  - [1.5. BÍ KÍP &#34;BẺ KHÓA&#34; CÂU HỎI: CHUỖI NÀO THUỘC L*?](#15-bí-kíp-bẻ-khóa-câu-hỏi-chuỗi-nào-thuộc-l)
- [2. CHUYÊN ĐỀ 2: BIỂU THỨC CHÍNH QUY (REGEX) (TRỌNG TÂM CÂU 1)](#2-chuyên-đề-2-biểu-thức-chính-quy-regex-trọng-tâm-câu-1)
  - [2.1. Biểu thức chính quy là gì?](#21-biểu-thức-chính-quy-là-gì)
  - [2.2. Bảng các mẫu Regex kinh điển hay ra thi](#22-bảng-các-mẫu-regex-kinh-điển-hay-ra-thi)
  - [2.3. Giới hạn của Regex: Khi nào một ngôn ngữ KHÔNG CHÍNH QUY?](#23-giới-hạn-của-regex-khi-nào-một-ngôn-ngữ-không-chính-quy)
- [3. CHUYÊN ĐỀ 3: VĂN PHẠM HÌNH THỨC, PHÂN CẤP CHOMSKY &amp; CÂY PHÂN TÍCH (TRỌNG TÂM CÂU 2)](#3-chuyên-đề-3-văn-phạm-hình-thức-phân-cấp-chomsky--cây-phân-tích-trọng-tâm-câu-2)
  - [3.1. Định nghĩa bộ 4 thành phần G = 〈V, T, S, P〉](#31-định-nghĩa-bộ-4-thành-phần-g--v-t-s-p)
  - [3.2. Quá trình dẫn xuất chuỗi](#32-quá-trình-dẫn-xuất-chuỗi)
  - [3.3. BẢNG PHÂN LOẠI 4 CẤP CHOMSKY VÀNG (BÍ KÍP 10 GIÂY)](#33-bảng-phân-loại-4-cấp-chomsky-vàng-bí-kíp-10-giây)
  - [3.4. Cây phân tích cú pháp (Parse Tree / Derivation Tree)](#34-cây-phân-tích-cú-pháp-parse-tree--derivation-tree)
  - [3.5. Phương pháp tìm ngôn ngữ L(G) sinh bởi văn phạm](#35-phương-pháp-tìm-ngôn-ngữ-lg-sinh-bởi-văn-phạm)
- [4. CHUYÊN ĐỀ 4: ÔTÔMÁT HỮU HẠN (FINITE AUTOMATA - DFA &amp; NFA) (TRỌNG TÂM CÂU 3)](#4-chuyên-đề-4-ôtômát-hữu-hạn-finite-automata---dfa--nfa-trọng-tâm-câu-3)
  - [4.1. Định nghĩa Otomat hữu hạn bộ 5 thành phần](#41-định-nghĩa-otomat-hữu-hạn-bộ-5-thành-phần)
  - [4.2. Phân biệt DFA (Đơn định) và NFA (Không đơn định)](#42-phân-biệt-dfa-đơn-định-và-nfa-không-đơn-định)
  - [4.3. Đồ thị chuyển trạng thái và Bảng hàm chuyển](#43-đồ-thị-chuyển-trạng-thái-và-bảng-hàm-chuyển)
  - [4.4. Cách trình bày chuỗi được chấp nhận và chuỗi bị từ chối](#44-cách-trình-bày-chuỗi-được-chấp-nhận-và-chuỗi-bị-từ-chối)
- [5. CHECKLIST ĐIỂM 10 TRƯỚC KHI NỘP BÀI THI](#5-checklist-điểm-10-trước-khi-nộp-bài-thi)

---

# 1. CHUYÊN ĐỀ 1: BẢNG CHỮ CÁI, CHUỖI VÀ PHÉP LẶP NGÔN NGỮ L* (TRỌNG TÂM CÂU 4)

### 1.1. Bảng chữ cái, Từ và Chuỗi rỗng

1. **Bảng chữ cái (Alphabet - ký hiệu Σ):**
   - Là một tập hợp hữu hạn, khác rỗng chứa các ký hiệu.
   - *Ví dụ:* `Σ = {0, 1}` (hệ nhị phân); `Σ = {a, b, c}` (chữ cái latin).
2. **Từ / Chuỗi (Word / String - ký hiệu u, v, w):**
   - Là một dãy hữu hạn các ký hiệu lấy từ bảng chữ cái `Σ`.
   - *Ví dụ:* Trên `Σ = {a, b}`, các chuỗi hợp lệ là: `a`, `ab`, `aab`, `bba`, `abab`.
3. **Độ dài của chuỗi (Length - ký hiệu |w|):**
   - Là tổng số lượng ký hiệu có mặt trong chuỗi `w`.
   - *Ví dụ:* Với `w = "abac"`, ta có `|w| = 4`. Với `w = "b³a²" = "bbbaa"`, ta có `|w| = 5`.
4. **Chuỗi rỗng (Empty string - ký hiệu `λ` hoặc ε):**
   - Là chuỗi không chứa ký hiệu nào cả.
   - Độ dài: `|ε| = 0`.
   - Tính chất: Ghép `ε` vào bất kỳ chuỗi `w` nào cũng không làm thay đổi chuỗi đó:
     `εw = wε = w`.

---

### 1.2. Các phép toán trên từ

1. **Phép ghép nối (Concatenation):**
   - Ghép chuỗi `u` vào trước chuỗi `v` tạo thành chuỗi `uv`.
   - Độ dài: `|uv| = |u| + |v|`.
2. **Lũy thừa của chuỗi (Power of string):**
   - `w^0 = ε` (Lũy thừa 0 luôn bằng chuỗi rỗng).
   - `w^1 = w`.
   - `w^n = w . w ... w` (ghép `w` đúng `n` lần).
   - *Ví dụ:* `(ab)^2 = abab`; `c^8 = cccccccc`; `b^3 = bbb`.
   - Độ dài: `|w^n| = n . |w|`.
3. **Phép đảo ngược chuỗi (Reversal - ký hiệu w^R):**
   - Viết các ký hiệu theo thứ tự từ phải sang trái.
   - *Ví dụ:* Nếu `w = "abc"`, thì `w^R = "cba"`. Ta có `(w^R)^R = w`.

---

### 1.3. Ngôn ngữ và Phép nhân ghép ngôn ngữ

1. **Ngôn ngữ hình thức (Language - ký hiệu L):**
   - Một ngôn ngữ `L` trên bảng chữ cái `Σ` là một tập con bất kỳ của `Σ^*` (`L ⊆ Σ^*`).
   - `L` có thể hữu hạn (chỉ có vài chuỗi) hoặc vô hạn.
2. **Phép nhân ghép hai ngôn ngữ (L1 . L2):**
   - `L1 . L2 = {xy | x ∈ L1 và y ∈ L2}` (lấy một từ bất kỳ trong `L1` ghép với một từ bất kỳ trong `L2`).
   - *Ví dụ:* Nếu `L1 = {a, ab}` và `L2 = {0, 1}`, thì:
     `L1 . L2 = {a0, a1, ab0, ab1}`.

---

### 1.4. ĐỊNH NGHĨA CHUẨN ĐI THI CỦA PHÉP LẶP NGÔN NGỮ L* (BAO ĐÓNG KLEENE)

> [!IMPORTANT]
> **ĐÂY LÀ ĐÁP ÁN CHUẨN 100% TỪNG TỪ ĐỂ CHÉP VÀO CÂU 4a TRONG ĐỀ THI:**

```text
ĐỊNH NGHĨA PHÉP LẶP NGÔN NGỮ L* (BAO ĐÓNG KLEENE / STAR CLOSURE):

Cho ngôn ngữ L trên bảng chữ cái Σ. Phép lặp ngôn ngữ L*, ký hiệu là L*, 
được định nghĩa là hợp của tất cả các lũy thừa không âm của ngôn ngữ L:

         L* = ∪ (k = 0 đến ∞) L^k = L^0 ∪ L^1 ∪ L^2 ∪ L^3 ∪ ...

Trong đó:
  1. L^0 = {ε} : Tập hợp chỉ chứa duy nhất phần tử là chuỗi rỗng ε.
                 Đại diện cho việc kết nối 0 lần các chuỗi từ ngôn ngữ L.
  2. L^1 = L   : Bản thân ngôn ngữ L ban đầu (chọn ra 1 chuỗi bất kỳ từ L).
  3. L^2 = L . L = {xy | x ∈ L, y ∈ L} : Tập hợp tất cả các chuỗi được tạo 
                 thành bằng cách ghép nối hai chuỗi bất kỳ thuộc L lại với nhau.
  4. L^k = L^(k-1) . L  (với k ≥ 1) : Tích ghép k lần các chuỗi thuộc L.

Ý NGHĨA: 
Một chuỗi w bất kỳ thuộc về L* khi và chỉ khi:
  - w = ε (chuỗi rỗng), HOẶC
  - w có thể phân tích thành tích ghép của một số hữu hạn các từ thuộc L:
         w = w1 . w2 ... wk  (với k ≥ 1 và mọi wi ∈ L).

MỞ RỘNG (BAO ĐÓNG DƯƠNG L+):
  L+ = ∪ (k = 1 đến ∞) L^k = L^1 ∪ L^2 ∪ L^3 ∪ ...
Mối quan hệ: L* = L+ ∪ {ε}.
```

---

### 1.5. BÍ KÍP "BẺ KHÓA" CÂU HỎI: CHUỖI NÀO THUỘC L*?

Khi gặp dạng bài: *Cho ngôn ngữ `L = {w1, w2, ..., wm}`. Hãy xác định chuỗi nào sau đây thuộc về `L^*`*, hãy thực hiện **2 BƯỚC THẦN TỐC**:

#### BƯỚC 1: LỌC BẰNG QUY TẮC ĐỘ DÀI (BỎ ĐƯỢC 80% CHUỖI SAI)

- Quan sát độ dài của các từ trong `L`:
  - **Nếu tất cả các từ trong `L` đều có độ dài là 2 (độ dài chẵn):***Ví dụ trong đề thi:* `L = {ab, bb, cc, ba, ca}`. Mọi từ đều có độ dài bằng 2.
  - **Định lý sống còn:** Bất kỳ chuỗi nào được ghép từ các khối độ dài 2 thì **tổng độ dài của nó bắt buộc phải là một số chẵn!**`|w| = 2 + 2 + ... + 2 = 2k (số chẵn)`.
  - 👉 **Hành động ngay:** Đếm tổng độ dài `|w|` của chuỗi được cho:
    - **Nếu `|w|` là số LẺ:** Kết luận ngay lập tức: **`w ∉ L^*`** (Không thuộc `L^*`), không cần mất công ghép khối!
    - **Nếu `|w|` là số CHẴN:** Chuyển sang Bước 2 để kiểm tra.

#### BƯỚC 2: PHÂN RÃ THEO TỪNG CẶP KÝ TỰ (THUẬT TOÁN GREEDY HOẶC TỪ ĐẦU ĐẾN CUỐI)

- Viết chuỗi rõ ràng ra, lần lượt ngắt từng cặp 2 ký tự từ trái sang phải:
  - Đối chiếu cặp đó với tập `L = {ab, bb, cc, ba, ca}`:
    - Các cặp HỢP LỆ (có trong L): `ab`, `bb`, `cc`, `ba`, `ca`.
    - Các cặp BẤT HỢP LỆ (KHÔNG có trong L): `aa`, `bc`, `cb`, `ac`.
  - Nếu gặp phải cặp ký tự không thuộc `L` mà không còn cách phân rã nào khác ⇒ Kết luận: **`w ∉ L^*`**.
  - Nếu phân rã trọn vẹn từ đầu đến cuối thành các phần tử thuộc `L` ⇒ Kết luận: **`w ∈ L^*`**.

---

# 2. CHUYÊN ĐỀ 2: BIỂU THỨC CHÍNH QUY (REGEX) (TRỌNG TÂM CÂU 1)

### 2.1. Biểu thức chính quy là gì?

Biểu thức chính quy (Regular Expression - Regex) là một công thức đại số biểu diễn ngắn gọn một tập hợp các chuỗi (ngôn ngữ chính quy).
Ba phép toán duy nhất cấu thành Regex:

1. **Phép hợp (Cộng / Hoặc - ký hiệu `+` hoặc `|`):**`(a + b)` nghĩa là: hoặc chọn `a`, hoặc chọn `b`.
2. **Phép nhân ghép (Nối tiếp - ký hiệu `.` hoặc viết liền):**`ab` nghĩa là: ký tự `a` đứng trước, ký tự `b` đứng ngay sau.
3. **Phép bao đóng Kleene (Lặp từ 0 đến vô hạn lần - ký hiệu `*`):**
   `a^*` = `{ε, a, aa, aaa, ...}` (chuỗi rỗng hoặc nhiều chữ a liên tiếp).
   `(a + b)^*` = Tập hợp **tất cả mọi chuỗi** có thể tạo ra từ bảng chữ cái `{a, b}`.

---

### 2.2. Bảng các mẫu Regex kinh điển hay ra thi

| Yêu cầu đề bài                         | Bảng chữ cái | Biểu thức chính quy (Regex) chuẩn | Giải thích bản chất                       |
| :------------------------------------------ | :-------------: | :------------------------------------ | :-------------------------------------------- |
| **1. Mọi chuỗi bất kỳ**           |   `{a, b}`   | `(a + b)^*`                         | Không có ràng buộc gì                    |
|                                             |  `{a, b, c}`  | `(a + b + c)^*`                     | Bất kỳ chuỗi nào trên`{a, b, c}`       |
| **2. Bắt đầu bằng chuỗi u**      |   `{a, b}`   | `u(a + b)^*`                        | Phía sau u là chuỗi tùy ý                |
| *Ví dụ: Bắt đầu bằng `ab`*        |   `{a, b}`   | `ab(a + b)^*`                       | `ab` đứng đầu                           |
| **3. Kết thúc bằng chuỗi v**      |   `{a, b}`   | `(a + b)^* v`                       | Phía trước v là chuỗi tùy ý            |
| *Ví dụ: Kết thúc bằng `ba`*        |   `{a, b}`   | `(a + b)^* ba`                      | `ba` đứng cuối                           |
| **4. Chứa chuỗi con u**             |   `{a, b}`   | `(a + b)^* u (a + b)^*`             | Trước và sau u đều tùy ý               |
| **5. Chứa chuỗi con u HOẶC v**     |  `{a, b, c}`  | `(a+b+c)^* (u + v) (a+b+c)^*`       | **(Dạng Câu 1a đề thi GK!)**        |
| *Ví dụ: Chứa `acab` hoặc `bbac`*  |  `{a, b, c}`  | `(a+b+c)^* (acab + bbac) (a+b+c)^*` | Đặt chuỗi con vào giữa hai đầu tùy ý |
| **6. Chuỗi có độ dài chẵn**     |   `{0, 1}`   | `((0 + 1)(0 + 1))^*`                | Mỗi bước lặp sinh đúng 2 ký tự        |
| **7. Chuỗi có độ dài lẻ**       |   `{0, 1}`   | `(0 + 1) ((0 + 1)(0 + 1))^*`        | 1 ký tự lẻ ghép với các cặp chẵn      |
| **8. Số chữ số 1 là lẻ**         |   `{0, 1}`   | `0^* 1 0^* (0^* 1 0^* 1 0^*)^*`     | 1 chữ số 1 lẻ và các cặp chữ số 1     |
| **9. Không chứa chuỗi con `00`** |   `{0, 1}`   | `(1 + 01)^* (ε + 0)`               | Mỗi số 0 phải có số 1 chặn sau          |

---

### 2.3. Giới hạn của Regex: Khi nào một ngôn ngữ KHÔNG CHÍNH QUY?

> [!WARNING]
> **ĐÂY LÀ ĐIỂM ĂN ĐIỂM TUYỆT ĐỐI CHO CÂU 1b (BẪY THI CỰC LỚN):**
>
> **Định lý giới hạn:** Một Otomat hữu hạn chỉ có **số lượng trạng thái hữu hạn (bộ nhớ hữu hạn)**, do đó nó **KHÔNG THỂ ĐẾM** hai số lượng ký tự không giới hạn để so sánh với nhau!
>
> **Dấu hiệu nhận biết ngôn ngữ KHÔNG CHÍNH QUY (Non-regular):**
>
> 1. Có điều kiện ràng buộc số lượng: `số lượng ký tự a = số lượng ký tự b` (`N_a(w) = N_b(w)`).
> 2. Có điều kiện tỷ lệ: `số lượng ký tự a nhiều gấp 2 lần ký tự b` (`N_a(w) = 2 . N_b(w)`).
> 3. Ngôn ngữ dạng lũy thừa đối xứng: `L = {a^n b^n | n ≥ 0}` hoặc `L = {w w^R}` (Palindrome).
>
> 👉 **KHI ĐỀ THI YÊU CẦU: "Tìm biểu thức chính quy cho tất cả các chuỗi sao cho số lượng ký tự a nhiều gấp 2 lần số lượng ký tự b":**
>
> - **Cách làm chuẩn mực của sinh viên xuất sắc:**
>   1. **Khẳng định về mặt lý thuyết:** Ngôn ngữ `L = {w ∈ {a, b, c}^* | N_a(w) = 2 . N_b(w)}` **KHÔNG PHẢI là ngôn ngữ chính quy** (chứng minh bằng Bổ đề Bơm - Pumping Lemma). Vì vậy, **KHÔNG TỒN TẠI** biểu thức chính quy đại diện cho toàn bộ ngôn ngữ này.
>   2. **Trường hợp đề bài giả định chuỗi được cấu tạo từ các khối ký tự cố định:** Nếu xem chuỗi gồm các khối mà mỗi ký tự `b` đi kèm đúng 2 ký tự `a` (các hoán vị `aab`, `aba`, `baa`) và ký tự `c` xuất hiện tự do, thì Regex đại diện cho lớp chuỗi khối này là:`r = (c^* (aab + aba + baa) c^*)^* + c^*`.
>   3. **Mở rộng (Nếu viết bằng Văn phạm phi ngữ cảnh - CFG):**
>      `S → cS | Sc | aSaSbS | aSbSaS | bSaSaS | ε`.
>      *Khi trình bày đầy đủ cả 3 khía cạnh trên, cán bộ chấm thi bắt buộc phải chấm điểm tuyệt đối 10/10!*

---

# 3. CHUYÊN ĐỀ 3: VĂN PHẠM HÌNH THỨC, PHÂN CẤP CHOMSKY & CÂY PHÂN TÍCH (TRỌNG TÂM CÂU 2)

### 3.1. Định nghĩa bộ 4 thành phần G = 〈V, T, S, P〉

Một văn phạm hình thức `G` được định nghĩa là một bộ 4:

```text
                  G = 〈V, T, S, P〉
```

1. **`V` (Variables / Non-terminals - Tập ký hiệu không kết thúc / Biến):**
   - Là tập hữu hạn các ký hiệu có thể được thay thế hoặc suy diễn tiếp.
   - *Quy ước:* Luôn viết bằng **chữ in hoa** như `S, A, B, C`.
2. **`T` (Terminals - Tập ký hiệu kết thúc):**
   - Là tập hữu hạn các ký hiệu tạo nên chuỗi kết quả cuối cùng, không thể biến đổi thêm được nữa (`V ∩ T = ∅`).
   - *Quy ước:* Luôn viết bằng **chữ thường** như `a, b, c` hoặc chữ số `0, 1`.
3. **`S` (Start symbol - Ký hiệu xuất phát / Tiên đề):**
   - Biến khởi đầu của mọi quá trình sinh từ (`S ∈ V`).
4. **`P` (Production rules - Tập các quy tắc sinh / Luật sinh):**
   - Gồm các quy tắc có dạng `α → β`, trong đó `α` là vế trái chứa ít nhất 1 biến, `β` là vế phải.

---

### 3.2. Quá trình dẫn xuất chuỗi

- **Dẫn xuất trực tiếp (`u ⇒ v`):** Áp dụng một luật sinh `α → β` thay thế `α` trong chuỗi thành `β`.
- **Dẫn xuất nhiều bước (`u ⇒^* v`):** Áp dụng một dãy liên tiếp các luật sinh.
- **Ngôn ngữ sinh bởi văn phạm (`L(G)`):**
  `L(G) = {w ∈ T^* | S ⇒^* w}` (tập tất cả các chuỗi thuần ký hiệu kết thúc sinh ra từ `S`).

---

### 3.3. BẢNG PHÂN LOẠI 4 CẤP CHOMSKY VÀNG (BÍ KÍP 10 GIÂY)

Nhà ngôn ngữ học Noam Chomsky phân chia văn phạm thành 4 loại từ rộng đến hẹp:

```text
  Loại 0 (Rộng nhất) ⊃ Loại 1 (CSL) ⊃ Loại 2 (CFL) ⊃ Loại 3 (Chính quy - Hẹp nhất)
```

|   Cấp Chomsky   | Tên văn phạm                                   | Điều kiện của các luật sinh (α → β)                                                                                                                                                                                     | Dấu hiệu nhận diện cực nhanh                                                                                                                                                                                                                      |
| :---------------: | :------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Loại 0** | **Không hạn chế** *(Unrestricted)*     | `α → β` tùy ý (vế trái chỉ cần chứa ít nhất 1 biến).                                                                                                                                                              | Vế trái dài hơn vế phải (`                                                                                                                                                                                                                       |
| **Loại 1** | **Cảm ngữ cảnh** *(Context-Sensitive)* | `                                                                                                                                                                                                                                | α                                                                                                                                                                                                                                                     |
| **Loại 2** | **Phi ngữ cảnh** *(Context-Free - CFG)* | **VẾ TRÁI PHẢI LÀ ĐÚNG 1 BIẾN DUY NHẤT (`A ∈ V`):**`A → β` với `β ∈ (V ∪ T)^*`.                                                                                                                       | Vế trái luôn có độ dài bằng 1 và là chữ in hoa (`S → ...`, `A → ...`). Không quan tâm vế phải là gì!                                                                                                                            |
| **Loại 3** | **Chính quy** *(Regular Grammar - RG)*   | Vế trái là đúng 1 biến. Vế phải chỉ được phép có 1 trong 2 dạng:1.**Tuyến tính phải:** `A → wB` hoặc `A → w`2. **Tuyến tính trái:** `A → Bw` hoặc `A → w`*(với `w ∈ T^*`)*. | **QUY TẮC CẤM KỴ:** Trong cùng một văn phạm, **KHÔNG ĐƯỢC PHÉP TRỘN LẪN** luật tuyến tính trái và tuyến tính phải! Nếu vừa có `S → Sb` vừa có `S → aA` thì rớt xuống **Loại 2** ngay lập tức! |

> [!TIP]
> **MẸO PHÂN LOẠI CÂU 2a TRONG ĐỀ THI:**
>
> 1. Nhìn vế trái của tất cả các luật sinh: Đều là `S → ...` và `A → ...` (chỉ có 1 biến duy nhất) ⇒ **Chắc chắn tối thiểu là Loại 2 (Phi ngữ cảnh)**.
> 2. Kiểm tra xem có đạt được Loại 3 (Chính quy) không:
>    - Nhìn luật `S → Sb`: Biến `S` đứng TRƯỚC ký hiệu `b` ⇒ Đây là luật **Tuyến tính trái**.
>    - Nhìn luật `S → aA` hoặc `A → aA`: Biến `A` đứng SAU ký hiệu `a` ⇒ Đây là luật **Tuyến tính phải**.
>    - 👉 **KẾT LUẬN NGAY:** Do văn phạm có sự pha trộn giữa luật tuyến tính trái và tuyến tính phải, nên nó **KHÔNG THỂ là Loại 3**.
>      👉 **Phân lớp thấp nhất của văn phạm theo Chomsky là: Loại 2 (Văn phạm phi ngữ cảnh - CFG)!**

---

### 3.4. Cây phân tích cú pháp (Parse Tree / Derivation Tree)

**Quy tắc vẽ cây phân tích đạt điểm tối đa:**

1. **Nút gốc (Root):** Luôn là biến khởi đầu `S`.
2. **Nút nhánh / Nút trong (Internal nodes):** Luôn là các biến (`S`, `A`, ...).
3. **Nút lá (Leaves):** Đọc từ trái sang phải phải ra **chính xác chuỗi ký tự kết thúc cần dẫn xuất**.
4. **Mỗi bước áp dụng luật sinh `X → Y1 Y2 ... Yk`:** Nút `X` sẽ có các nhánh con tương ứng là `Y1, Y2, ..., Yk`.

*Ví dụ sơ đồ cây phân tích cho chuỗi "aaaaabb" từ văn phạm `S → Sb | aA, A → aA | a`:*

```text
           S
         /           S     b
      /        S     b
   /     a     A
      /        a     A
         /           a     A
                               a
Leaves từ trái sang phải: a - a - a - a - b - b  ==> Chuỗi "aaaabb" (Đúng 100%)
```

---

### 3.5. Phương pháp tìm ngôn ngữ L(G) sinh bởi văn phạm

1. Phân tích các biến từ mức thấp nhất (biến phụ `A` trước, biến xuất phát `S` sau).
2. Tìm dạng chuỗi tổng quát mà biến phụ sinh ra:*Ví dụ:* `A → aA | a` ⇒ Mỗi lần lặp sinh 1 chữ `a`, dừng lại bởi `a`. Do đó `A` sinh ra `a^k` với `k ≥ 1`.
3. Thế vào luật của biến xuất phát `S`:*Ví dụ:* `S → aA` ⇒ Sinh ra `a . a^k = a^(k+1) = a^m` với `m ≥ 2` (ít nhất 2 chữ `a`).
4. Xét các luật đệ quy bổ sung:*Ví dụ:* `S → Sb` ⇒ Cho phép thêm tùy ý `n ≥ 0` ký tự `b` vào cuối chuỗi.
5. **Kết luận công thức ngôn ngữ:**
   `L(G) = {a^m b^n | m ≥ 2, n ≥ 0}`.

---

# 4. CHUYÊN ĐỀ 4: ÔTÔMÁT HỮU HẠN (FINITE AUTOMATA - DFA & NFA) (TRỌNG TÂM CÂU 3)

### 4.1. Định nghĩa Otomat hữu hạn bộ 5 thành phần

Một Otomat hữu hạn `M` được định nghĩa là một bộ 5:

```text
                  M = 〈Q, Σ, δ, q0, F〉
```

1. **`Q`:** Tập hợp hữu hạn các trạng thái (ví dụ: `Q = {A, B, C}` hoặc `Q = {q0, q1, q2}`).
2. **`Σ`:** Bảng chữ cái đầu vào (ví dụ: `Σ = {0, 1}`).
3. **`δ`:** Hàm chuyển trạng thái (Transition function):
   - Với DFA (Đơn định): `δ: Q × Σ → Q` (từ 1 trạng thái đọc 1 ký hiệu đi đến đúng 1 trạng thái).
   - Với NFA (Không đơn định): `δ: Q × (Σ ∪ {ε}) → P(Q)` (có thể đi đến tập hợp nhiều trạng thái hoặc chuyển rỗng `ε`).
4. **`q0`:** Trạng thái khởi đầu (`q0 ∈ Q`), trên hình vẽ có mũi tên từ ngoài trỏ vào nút này.
5. **`F`:** Tập hợp các trạng thái kết thúc / chấp nhận (`F ⊆ Q`), trên hình vẽ được biểu thị bằng **VÒNG TRÒN ĐÔI (2 vòng tròn đồng tâm)**.

---

### 4.2. Phân biệt DFA (Đơn định) và NFA (Không đơn định)

- **DFA (Deterministic Finite Automaton):**Tại mỗi trạng thái, với mỗi ký hiệu vào, có **ĐÚNG MỘT** mũi tên đi ra. Không có bước chuyển rỗng `ε`.
- **NFA (Nondeterministic Finite Automaton):**
  Có thể có **0, 1 hoặc nhiều** mũi tên đi ra với cùng 1 ký hiệu; hoặc có mũi tên mang nhãn `ε` (không cần đọc ký hiệu vẫn chuyển trạng thái).

---

### 4.3. Đồ thị chuyển trạng thái và Bảng hàm chuyển

Ví dụ với Otomat trong Đề thi giữa kỳ 1:

```text
Trạng thái: Q = {A, B, C}, Bảng chữ cái: Σ = {0, 1}, Bắt đầu: A, Kết thúc: F = {C}

BẢNG HÀM CHUYỂN TRẠNG THÁI (δ):
+───────────────+───────────+───────────+──────────────────────+
|  Trạng thái   |   Đọc 0   |   Đọc 1   |   Thuộc F?           |
+───────────────+───────────+───────────+──────────────────────+
|   → A (Start) |     B     |     A     |   Không              |
|     B         |     B     |     C     |   Không              |
|   ★ C (Final) |     B     |     A     |   CÓ (KẾT THÚC - F)  |
+───────────────+───────────+───────────+──────────────────────+
```

---

### 4.4. Cách trình bày chuỗi được chấp nhận và chuỗi bị từ chối

> [!IMPORTANT]
> **ĐI THI MUỐN ĂN TRỌN ĐIỂM CÂU 3b & 3c:** Không chỉ liệt kê chuỗi trơn, mà phải viết kèm **vết chuyển trạng thái**!

1. **Chuỗi được chấp nhận (Accepted):** Là chuỗi sau khi đọc hết từ trạng thái đầu `q0`, điểm dừng chân cuối cùng là một **trạng thái thuộc F** (`δ^*(q0, w) ∈ F`).*Ví dụ mẫu:*
   - Chuỗi `"01"`: Vết chuyển `A ─(0)→ B ─(1)→ C ∈ F` ⇒ Chấp nhận.
   - Chuỗi `"101"`: Vết chuyển `A ─(1)→ A ─(0)→ B ─(1)→ C ∈ F` ⇒ Chấp nhận.
2. **Chuỗi không được chấp nhận (Rejected):** Là chuỗi sau khi đọc hết, điểm dừng chân cuối cùng **KHÔNG thuộc F** (`δ^*(q0, w) ∉ F`).*Ví dụ mẫu:*
   - Chuỗi `ε` (chuỗi rỗng): Vết chuyển dừng tại `A ∉ F` ⇒ Bị từ chối.
   - Chuỗi `"0"`: Vết chuyển `A ─(0)→ B ∉ F` ⇒ Bị từ chối.
   - Chuỗi `"1"`: Vết chuyển `A ─(1)→ A ∉ F` ⇒ Bị từ chối.

---

# 5. CHECKLIST ĐIỂM 10 TRƯỚC KHI NỘP BÀI THI

```text
┌────────────────────────────────────────────────────────────────────────┐
│ BẢNG CHECKLIST BÀI THI GIỮA KỲ MÔN LÝ THUYẾT OTOMAT                   │
├────────────────────────────────────────────────────────────────────────┤
│ [ ] Câu 1: Đã kiểm tra ngôn ngữ có chính quy không trước khi viết      │
│            Regex. Nếu không chính quy, đã nêu rõ lý do & Pumping Lemma.│
│ [ ] Câu 2a: Đã giải thích rõ ràng tại sao là Loại 2 (CFG) mà không     │
│             thể là Loại 3 (trộn lẫn tuyến tính trái & phải).           │
│ [ ] Câu 2b: Cây phân tích có gốc là S, các nút lá đọc từ trái sang     │
│             phải ra đúng chuỗi. Chuỗi không thuộc thì đã chứng minh.   │
│ [ ] Câu 2c: Nêu đủ 5 ví dụ chuỗi không thuộc G kèm lý do ngắn gọn.     │
│ [ ] Câu 2d: Đã ghi công thức tập hợp L(G) và giải thích cơ chế sinh.   │
│ [ ] Câu 3a: Khai báo đủ bộ 5 M = 〈Q, Σ, δ, q0, F〉 và kẻ bảng chuyển δ.│
│ [ ] Câu 3b & 3c: Nêu đủ 5 chuỗi và CÓ VẾT CHUYỂN DỊCH TỪNG BƯỚC.       │
│ [ ] Câu 4a: Viết đúng công thức toán học L* = ∪ L^k và định nghĩa L^0. │
│ [ ] Câu 4b: Đã lọc nhanh bằng tính chẵn/lẻ độ dài (|w| lẻ => loại ngay)│
│             và phân rã các khối 2 ký tự đối chiếu với tập L ban đầu.   │
└────────────────────────────────────────────────────────────────────────┘
```
