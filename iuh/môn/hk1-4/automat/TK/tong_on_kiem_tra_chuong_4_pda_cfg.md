# TÀI LIỆU ÔN TẬP & MANG VÀO PHÒNG KIỂM TRA CHƯƠNG 4: NGÔN NGỮ PHI NGỮ CẢNH (CFG) & ÔTÔMÁT ĐẨY XUỐNG (PDA)
## (TỔNG HỢP TOÀN BỘ LÝ THUYẾT TINH GỌN, THUẬT TOÁN BỎ TÚI & BÀI TẬP GIẢI MẪU 10/10)

> **HƯỚNG DẪN DÀNH CHO BẠN KHI LÀM BÀI KIỂM TRA:**
> - Tài liệu này được biên soạn bám sát 100% Slide bài giảng Tuần 11 & 12 (Chương 4) của thầy.
> - **Nguyên tắc "3 Không":** Không lý thuyết hàn lâm dài dòng - Không công thức thừa - Không giải tắt gây mất điểm.
> - **Ký hiệu chuẩn hóa theo bài giảng:**
>   + Chuỗi rỗng: `ε` (Epsilon).
>   + Bước dẫn xuất của văn phạm: `⇒` (dẫn xuất trực tiếp) và `⇒*` (dẫn xuất nhiều bước).
>   + Dẫn xuất trái nhất: `⇒_lm`; Dẫn xuất phải nhất: `⇒_rm`.
>   + Bước chuyển hình trạng của Otomat đẩy xuống (PDA): `⊢` (1 bước) và `⊢*` (nhiều bước).
>   + Ngăn xếp (Stack / PDS): Trong tài liệu này quy ước viết theo chuẩn slide của thầy: `(q, w, α)` với `w` là chuỗi vào còn lại, `α` là ngăn xếp.

---

# MỤC LỤC CÁC DẠNG BÀI CHƯƠNG 4

- [PHẦN 1: BẢN CHẤT CỐT LÕI CHƯƠNG 4 (HIỂU TRONG 3 PHÚT)](#phần-1-bản-chất-cốt-lõi-chương-4-hiểu-trong-3-phút)
- [PHẦN 2: DẠNG 1 - CÂY SUY DẪN & CHỨNG MINH VĂN PHẠM NHẬP NHẰNG](#phần-2-dạng-1---cây-suy-dẫn--chứng-minh-văn-phạm-nhập-nhằng)
  + [1.1. Cây suy dẫn đầy đủ & Cách vẽ cây chuẩn 10/10](#11-cây-suy-dẫn-đầy-đủ--cách-vẽ-cây-chuẩn-1010)
  + [1.2. Dẫn xuất trái nhất (Leftmost) & Dẫn xuất phải nhất (Rightmost)](#12-dẫn-xuất-trái-nhất-leftmost--dẫn-xuất-phải-nhất-rightmost)
  + [1.3. Chứng minh văn phạm nhập nhằng (đa nghĩa - Ambiguity)](#13-chứng-minh-văn-phạm-nhập-nhằng-đa-nghĩa---ambiguity)
  + [1.4. Bài tập mẫu giải chi tiết (Slide 31, Slide 29, Slide 32)](#14-bài-tập-mẫu-giải-chi-tiết)
- [PHẦN 3: DẠNG 2 - RÚT GỌN VĂN PHẠM PHI NGỮ CẢNH (4 BƯỚC CHUẨN)](#phần-3-dạng-2---rút-gọn-văn-phạm-phi-ngữ-cảnh-4-bước-chuẩn)
  + [2.1. Thứ tự 4 bước bắt buộc theo slide bài giảng](#21-thứ-tự-4-bước-bắt-buộc-theo-slide-bài-giảng)
  + [2.2. Bước 1: Khử ε-quy tắc (Null productions)](#22-bước-1-khử-ε-quy-tắc-null-productions)
  + [2.3. Bước 2: Khử quy tắc đơn vị (Unit productions A → B)](#23-bước-2-khử-quy-tắc-đơn-vị-unit-productions-a--b)
  + [2.4. Bước 3: Khử ký hiệu vô sinh (Non-generating / Vô dụng loại 1)](#24-bước-3-khử-ký-hiệu-vô-sinh-non-generating--vô-dụng-loại-1)
  + [2.5. Bước 4: Khử ký hiệu không đến được (Unreachable / Vô dụng loại 2)](#25-bước-4-khử-ký-hiệu-không-đến-được-unreachable--vô-dụng-loại-2)
  + [2.6. Giải chi tiết trọn bộ Bài tập Slide 33 (Câu i, ii, iii)](#26-giải-chi-tiết-trọn-bộ-bài-tập-slide-33)
- [PHẦN 4: DẠNG 3 - ĐƯA VĂN PHẠM VỀ DẠNG CHUẨN CHOMSKY (CNF)](#phần-4-dạng-3---đưa-văn-phạm-về-dạng-chuẩn-chomsky-cnf)
  + [3.1. Định nghĩa Dạng chuẩn Chomsky](#31-định-nghĩa-dạng-chuẩn-chomsky)
  + [3.2. Thuật toán 5 bước biến đổi](#32-thuật-toán-5-bước-biến-đổi)
  + [3.3. Bài tập mẫu giải chi tiết (Slide 26 & Slide 24-25)](#33-bài-tập-mẫu-giải-chi-tiết-cnf)
- [PHẦN 5: DẠNG 4 - OTOMAT ĐẨY XUỐNG (PDA): ĐỊNH NGHĨA & VẾT CHẠY](#phần-5-dạng-4---otomat-đẩy-xuống-pda-định-nghĩa--vết-chạy)
  + [4.1. Bộ 7 thành phần của PDA](#41-bộ-7-thành-phần-của-pda)
  + [4.2. Hai cơ chế đoán nhận: Ngăn xếp rỗng N(A) vs Trạng thái kết thúc T(A)](#42-hai-cơ-chế-đoán-nhận-ngăn-xếp-rỗng-na-vs-trạng-thái-kết-thúc-ta)
  + [4.3. Cách viết vết chạy hình trạng (⊢) đạt điểm tối đa](#43-cách-viết-vết-chạy-hình-trạng--đạt-điểm-tối-đa)
- [PHẦN 6: DẠNG 5 - THIẾT KẾ PDA TRỰC TIẾP CHO CÁC NGÔN NGỮ KINH ĐIỂN](#phần-6-dạng-5---thiết-kế-pda-trực-tiếp-cho-các-ngôn-ngữ-kinh-điển)
  + [5.1. Ngôn ngữ a^n b^n (n ≥ 1)](#51-ngôn-ngữ-an-bn)
  + [5.2. Ngôn ngữ a^n b^(2n) (n ≥ 1)](#52-ngôn-ngữ-an-b2n)
  + [5.3. Ngôn ngữ Palindrome đối xứng có tâm w c w^R](#53-ngôn-ngữ-palindrome-đối-xứng-có-tâm-w-c-wr)
  + [5.4. Ngôn ngữ số chữ a bằng số chữ b: Na(w) = Nb(w)](#54-ngôn-ngữ-số-chữ-a-bằng-số-chữ-b)
  + [5.5. Ngôn ngữ a^n b^m c^n (Slide 52) & a^m b^n với m > n](#55-ngôn-ngữ-an-bm-cn-slide-52--am-bn-với-m--n)
- [PHẦN 7: DẠNG 6 - CHUYỂN ĐỔI GIỮA CFG VÀ PDA (TUYỆT CHIÊU 1 TRẠNG THÁI)](#phần-7-dạng-6---chuyển-đổi-giữa-cfg-và-pda)
  + [6.1. Tuyệt chiêu CFG sang PDA theo Ngăn xếp rỗng N(A) (1 trạng thái duy nhất)](#61-tuyệt-chiêu-cfg-sang-pda-theo-ngăn-xếp-rỗng-na)
  + [6.2. Chuyển CFG sang PDA theo Trạng thái kết thúc T(A) (3 trạng thái)](#62-chuyển-cfg-sang-pda-theo-trạng-thái-kết-thúc-ta)
  + [6.3. Chuyển PDA sang CFG (Quy tắc biến [q, Z, p])](#63-chuyển-pda-sang-cfg-quy-tắc-biến-q-z-p)
- [PHẦN 8: DẠNG 7 - GIẢI CHI TIẾT 100% BÀI TẬP LỚN CUỐI SLIDE (3.9, 3.10, 3.11)](#phần-8-dạng-7---giải-chi-tiết-100-bài-tập-lớn-cuối-slide)
  + [8.1. Giải trọn vẹn Bài tập 3.9 (Slide 63)](#81-giải-trọn-vẹn-bài-tập-39)
  + [8.2. Giải trọn vẹn Bài tập 3.10 (Slide 64) - 5 câu hỏi](#82-giải-trọn-vẹn-bài-tập-310)
  + [8.3. Giải trọn vẹn Bài tập 3.11 (Slide 65) - 4 câu hỏi](#83-giải-trọn-vẹn-bài-tập-311)
- [PHẦN 9: BẢNG TỔNG KẾT & 5 BẪY THI CẦN NÉ ĐỂ ĐẠT 10 ĐIỂM](#phần-9-bảng-tổng-kết--5-bẫy-thi-cần-né-để-đạt-10-điểm)

---

# PHẦN 1: BẢN CHẤT CỐT LÕI CHƯƠNG 4 (HIỂU TRONG 3 PHÚT)

### 1. Văn phạm phi ngữ cảnh (CFG) là gì?
- Là văn phạm mà **vế trái của MỌI luật sinh chỉ có ĐÚNG 1 biến** (`A → α`).
- Tại sao gọi là "phi ngữ cảnh" (Context-Free)? Vì biến `A` có thể thay thế bằng `α` ở bất kỳ đâu, bất chấp ký tự đứng trước hay đứng sau nó là gì (không phụ thuộc ngữ cảnh xung quanh).

### 2. Tại sao Otomat hữu hạn (DFA/NFA) "bó tay" và phải sinh ra PDA?
- DFA/NFA chỉ có **bộ nhớ hữu hạn** (các trạng thái). Khi gặp bài toán cần đếm số lượng không giới hạn như `a^n b^n` (số `a` bằng số `b`), DFA không thể nhớ nổi đã đọc bao nhiêu chữ `a`.
- **Otomat đẩy xuống (PDA = Pushdown Automata):** Là một DFA/NFA được **gắn thêm một NGĂN XẾP (Stack / PDS)** vô hạn bộ nhớ hoạt động theo cơ chế **LIFO (Vào sau - Ra trước)**.
  + Đọc chữ `a` ⇒ Đẩy (PUSH) `a` vào ngăn xếp.
  + Đọc chữ `b` ⇒ Lấy (POP) `a` ra khỏi ngăn xếp.
  + Hết chuỗi, nếu ngăn xếp trống trơn (hoặc về trạng thái kết thúc) ⇒ **CHẤP NHẬN**. Cực kỳ đơn giản!

### 3. Hai cơ chế đoán nhận chuỗi của PDA:
1. **Đoán nhận bằng Ngăn xếp rỗng (Empty stack - `N(A)`):** Chuỗi được chấp nhận khi đọc xong toàn bộ chuỗi đầu vào VÀ ngăn xếp trở thành rỗng (không quan tâm đang ở trạng thái nào).
2. **Đoán nhận bằng Trạng thái kết thúc (Final state - `T(A)`):** Chuỗi được chấp nhận khi đọc xong chuỗi vào VÀ máy dừng tại một trạng thái thuộc tập kết thúc `F` (ngăn xếp còn gì kệ nó).
*(Hai cơ chế này tương đương nhau về sức mạnh: N(A) = T(B)).*


---

# PHẦN 2: DẠNG 1 - CÂY SUY DẪN & CHỨNG MINH VĂN PHẠM NHẬP NHẰNG

### 1.1. Cây suy dẫn đầy đủ & Cách vẽ cây chuẩn 10/10:
- **Định nghĩa:** Cây suy dẫn đầy đủ trong CFG `G = <Σ, Δ, S, P>` là cây có:
  + Gốc (Root): luôn là biến bắt đầu `S`.
  + Đỉnh trong (Internal nodes): mang nhãn là các biến không kết thúc thuộc `Δ` (hoặc `V_N`).
  + Đỉnh lá (Leaves): mang nhãn là các ký hiệu kết thúc thuộc `Σ` (hoặc `V_T`) hoặc chuỗi rỗng `ε`.
  + Nếu nút cha `A` có các con từ trái sang phải là `B1, B2, ..., Bk` thì `A → B1 B2 ... Bk` phải là một quy tắc thuộc `P`.
  + **Kết quả của cây:** Đọc tất cả các lá từ trái sang phải ra chuỗi `w ∈ L(G)`.

### 1.2. Dẫn xuất trái nhất (Leftmost) & Dẫn xuất phải nhất (Rightmost):
- **Dẫn xuất trái nhất (`⇒_lm`):** Ở mỗi bước, luôn chọn **biến nằm ngoài cùng bên trái** trong chuỗi để áp dụng luật sinh thay thế trước.
- **Dẫn xuất phải nhất (`⇒_rm`):** Ở mỗi bước, luôn chọn **biến nằm ngoài cùng bên phải** trong chuỗi để áp dụng luật sinh thay thế trước.

### 1.3. Chứng minh văn phạm nhập nhằng (đa nghĩa - Ambiguity):
- **Định nghĩa:** Một văn phạm phi ngữ cảnh `G` được gọi là **nhập nhằng (đa nghĩa)** nếu tồn tại **ít nhất một chuỗi `w ∈ L(G)`** mà:
  + Có **từ 2 cây suy dẫn khác nhau**, HOẶC:
  + Có **từ 2 dẫn xuất trái nhất khác nhau** (hoặc 2 dẫn xuất phải nhất khác nhau).
- **Mẹo tìm chuỗi làm bằng chứng khi đi thi:**
  + Nếu văn phạm có toán tử kết hợp như `S → S + S | S * S` hoặc `S → SbS`: Hãy chọn chuỗi có **từ 2 toán tử trở lên** (ví dụ `ababa`, `a + b * c`, `a * b + a * b`).

---

### 1.4. BÀI TẬP MẪU GIẢI CHI TIẾT (CHUẨN SLIDE)

#### BÀI TẬP MẪU 1.1 (Slide 31): Chứng minh văn phạm nhập nhằng
**ĐỀ BÀI:** Chỉ ra rằng văn phạm `G` có các quy tắc sau là nhập nhằng:
```text
S → SbS | a
```

**BÀI LÀM CHUẨN ĐI THI:**
1. **Chọn chuỗi kiểm tra:** Xét chuỗi `w = "ababa" ∈ L(G)`.
2. **Chỉ ra 2 cây suy dẫn khác nhau sinh ra cùng chuỗi `w`:**

- **Cây suy dẫn 1:** (Nhánh trái kết thúc trước, mở rộng nhánh phải)
```text
            S
         ┌──┼──┐
         S  b  S
         │   ┌─┼─┐
         a   S b S
             │   │
             a   a
(Đọc lá từ trái sang phải: a - b - a - b - a = "ababa")
```
Dẫn xuất trái nhất 1: `S ⇒_lm SbS ⇒_lm abS ⇒_lm abSbS ⇒_lm ababS ⇒_lm ababa`.

- **Cây suy dẫn 2:** (Nhánh trái mở rộng tiếp, nhánh phải kết thúc trước)
```text
            S
         ┌──┼──┐
         S  b  S
       ┌─┼─┐   │
       S b S   a
       │   │
       a   a
(Đọc lá từ trái sang phải: a - b - a - b - a = "ababa")
```
Dẫn xuất trái nhất 2: `S ⇒_lm SbS ⇒_lm SbSbS ⇒_lm abSbS ⇒_lm ababS ⇒_lm ababa`.

3. **KẾT LUẬN:** Chuỗi `w = ababa` có 2 cây suy dẫn hoàn toàn khác nhau (tương ứng với 2 dẫn xuất trái nhất khác nhau) trong văn phạm `G`.  
⇒ **Vậy văn phạm G là NHẬP NHẰNG (ĐA NGHĨA).**

---

#### BÀI TẬP MẪU 1.2 (Slide 29 & Slide 14): Biểu thức số học & Cây dẫn xuất
**ĐỀ BÀI:** Cho trước văn phạm `G` có các quy tắc:
```text
S → S + S | S * S
S → a | b
```
a) Tìm cây dẫn xuất cho kết quả `a * b + a * b ∈ L(G)`.  
b) Chứng minh văn phạm này là nhập nhằng.

**BÀI LÀM CHUẨN ĐI THI:**
- **Ý a: Vẽ cây dẫn xuất cho chuỗi `a * b + a * b`:**
```text
               S
          ┌────┼────┐
          S    +    S
       ┌──┼──┐   ┌──┼──┐
       S  *  S   S  *  S
       │     │   │     │
       a     b   a     b
(Đọc lá từ trái sang phải: a * b + a * b)
```
Dãy dẫn xuất trái nhất tương ứng:
`S ⇒ S + S ⇒ S * S + S ⇒ a * S + S ⇒ a * b + S ⇒ a * b + S * S ⇒ a * b + a * S ⇒ a * b + a * b`.

- **Ý b: Chứng minh G là nhập nhằng:**
Xét chuỗi ngắn `w = a + b * a`. Ta có 2 cây suy dẫn khác nhau:
+ Cây 1 (Ưu tiên nhân): Gốc là `+`, nút con là `a` và `b * a` (thực hiện phép nhân trước).
+ Cây 2 (Ưu tiên cộng): Gốc là `*`, nút con là `a + b` và `a` (thực hiện phép cộng trước).  
⇒ Tồn tại 2 cây suy dẫn cho cùng 1 chuỗi nên văn phạm `G` là nhập nhằng.

---

#### BÀI TẬP MẪU 1.3 (Slide 32): Chứng minh văn phạm 2 biến nhập nhằng
**ĐỀ BÀI:** Chỉ ra rằng văn phạm `G` có các quy tắc sau là nhập nhằng:
```text
S → a | abS | aAb
A → bS | aAAb
```

**BÀI LÀM CHUẨN ĐI THI:**
1. **Chọn chuỗi kiểm tra:** Xét chuỗi `w = "ababb"` (hoặc `w = ababa`).
Xét chuỗi `w = "abab"`:
- Dẫn xuất 1: `S ⇒ abS ⇒ aba` (dùng luật `S → abS`, sau đó `S → a`).
- Dẫn xuất 2: `S ⇒ aAb ⇒ a(bS)b ⇒ ab(a)b = abab` (dùng luật `S → aAb`, sau đó `A → bS`, rồi `S → a`).
2. Hai cây suy dẫn tương ứng:
- Cây 1:
```text
       S
     ┌─┼─┐
     a b S
         │
         a
```
- Cây 2:
```text
         S
      ┌──┼──┐
      a  A  b
       ┌─┴─┐
       b   S
           │
           a
```
3. **KẾT LUẬN:** Chuỗi `abab` có 2 cây suy dẫn khác nhau trong `G` ⇒ **Văn phạm G là nhập nhằng.**

---

# PHẦN 3: DẠNG 2 - RÚT GỌN VĂN PHẠM PHI NGỮ CẢNH (4 BƯỚC CHUẨN)

### 2.1. Thứ tự 4 bước bắt buộc theo slide bài giảng (Slide 27-28):
Để không sinh ra các luật dư thừa mới, bạn **BẮT BUỘC** phải tuân thủ đúng thứ tự 4 bước sau:
```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                       THỨ TỰ RÚT GỌN CHUẨN CỦA THẦY                         │
│ BƯỚC 1: Loại bỏ các ε-quy tắc (luật sinh rỗng A → ε).                        │
│ BƯỚC 2: Loại bỏ các quy tắc đơn vị (A → B với A, B là biến).                │
│ BƯỚC 3: Loại bỏ ký hiệu VÔ SINH (Biến vô dụng 1 - không sinh ra từ kết thúc).│
│ BƯỚC 4: Loại bỏ ký hiệu KHÔNG ĐẾN ĐƯỢC (Biến vô dụng 2 - không đi tới từ S). │
└─────────────────────────────────────────────────────────────────────────────┘
```
> [!IMPORTANT]
> **LÝ DO TẠI SAO PHẢI THEO THỨ TỰ NÀY (Slide 28):**
> 1. Khử `ε` có thể sinh ra quy tắc đơn vị mới ⇒ Vì vậy phải khử `ε` trước rồi mới khử đơn vị.
> 2. Khử đơn vị không sinh ra `ε` mới.
> 3. Khử vô sinh (loại 1) có thể sinh ra ký hiệu không đến được (loại 2) ⇒ Vì vậy phải khử vô sinh trước rồi mới khử không đến được.
> 4. Khử không đến được không bao giờ sinh ra ký hiệu vô sinh mới.

---

### 2.2. BƯỚC 1: Khử ε-quy tắc (Null productions)

#### Thuật toán:
1. **Tìm tập biến triệt tiêu (Nullable variables) `NULL`:**
   - Ban đầu: tập `NULL` gồm các biến có luật trực tiếp `A → ε`.
   - Lặp lại: Nếu có luật `B → X1 X2 ... Xk` mà TẤT CẢ các `Xi` đều đã thuộc `NULL` ⇒ Thêm `B` vào `NULL`.
   - Dừng khi không thể thêm biến nào nữa vào `NULL`.
2. **Tạo tập luật mới `P'`:**
   - Với mỗi luật sinh trong `P`, lần lượt xét các trường hợp các biến thuộc `NULL` bị triệt tiêu (bằng `ε`) hoặc giữ nguyên.
   - Xóa bỏ tất cả các luật dạng `A → ε` ban đầu.
   - *(Lưu ý: Nếu `S ∈ NULL`, tức là `ε ∈ L(G)`, thì thêm biến bắt đầu mới `S0 → S | ε`).*

#### Ví dụ mẫu (Slide 22):
Cho `P = { S → AB, A → aA | ε, B → bB | ε }`.
- Bước 1: `A → ε, B → ε` ⇒ A, B ∈ NULL. Vì `S → AB` mà cả `A, B ∈ NULL` nên `S ∈ NULL`.
  Vậy `NULL = {S, A, B}`.
- Bước 2: Thay thế tổ hợp:
  + Từ `S → AB`: khi `B = ε` ta được `S → A`; khi `A = ε` ta được `S → B`; khi cả 2 khác `ε` ta có `S → AB`. Vậy: `S → AB | A | B`.
  + Từ `A → aA | ε`: khi `A = ε` ta được `A → a`; khi `A` giữ nguyên ta có `A → aA`. Xóa `A → ε`. Vậy: `A → aA | a`.
  + Từ `B → bB | ε`: tương tự được `B → bB | b`.
- Kết quả không còn `ε`:
  `P' = { S → AB | A | B, A → aA | a, B → bB | b }`.

---

### 2.3. BƯỚC 2: Khử quy tắc đơn vị (Unit productions A → B)

#### Thuật toán:
1. **Tìm tất cả các cặp đơn vị `(A, B)` sao cho `A ⇒* B`:**
   - Mọi biến đều có `A ⇒* A`.
   - Nếu có `A → B` thì có cặp `(A, B)`.
   - Nếu có `A ⇒* B` và `B → C` thì có cặp `(A, C)`.
2. **Tạo tập luật mới `P'`:**
   - Với mỗi cặp `(A, B)`, nếu trong văn phạm có luật không đơn vị `B → α` (với `α` không phải là 1 biến đơn) ⇒ Thêm luật `A → α` vào `P'`.
   - Xóa sạch tất cả các luật đơn vị `A → B`.

#### Ví dụ mẫu (Slide 20):
Cho `P = { S → AB, A → a, B → C | b, C → D, D → E, E → a }`.
- Các luật đơn vị: `B → C, C → D, D → E`.
- Dãy biến đổi: `B ⇒ C ⇒ D ⇒ E ⇒ a`.
- Suy ra từ `B` dẫn xuất được: `B ⇒* a` và `B → b`.
- Thay thế trực tiếp:
  `B → a | b`.
- Xóa các biến `C, D, E` (vì không còn luật nào trỏ vào chúng).
- Kết quả: `P' = { S → AB, A → a, B → a | b }`.

---

### 2.4. BƯỚC 3: Khử ký hiệu VÔ SINH (Biến không sinh ra từ kết thúc)

#### Khái niệm:
Biến `A` gọi là **vô sinh** nếu từ `A` không bao giờ dẫn xuất ra được chuỗi ký hiệu kết thúc (`A ⇏* w ∈ Σ*`).

#### Thuật toán tìm tập biến sinh `GEN`:
- **Bước khởi tạo `GEN_0`:** Gồm các biến có luật sinh trực tiếp ra chuỗi chỉ chứa ký hiệu kết thúc:
  `GEN_0 = { A | A → w ∈ Σ* }`.
- **Bước lặp `GEN_(k+1)`:** Thêm biến `B` nếu `B → α` mà mọi ký hiệu trong `α` đều là ký hiệu kết thúc hoặc các biến đã nằm trong `GEN_k`:
  `GEN_(k+1) = GEN_k ∪ { B | B → α ∈ (Σ ∪ GEN_k)* }`.
- Dừng khi không thêm được biến nào.
- **Xóa bỏ:** Mọi biến **KHÔNG THUỘC `GEN`** và **TẤT CẢ CÁC LUẬT CÓ CHỨA BIẾN ĐÓ** (ở cả vế trái lẫn vế phải).

---

### 2.5. BƯỚC 4: Khử ký hiệu KHÔNG ĐẾN ĐƯỢC (Unreachable)

#### Khái niệm:
Ký hiệu `X` gọi là **không đến được** nếu từ biến bắt đầu `S` không bao giờ dẫn xuất ra chuỗi có chứa `X` (`S ⇏* α X β`).

#### Thuật toán tìm tập ký hiệu đến được `REACH`:
- **Bước khởi tạo `REACH_0`:** `REACH_0 = { S }`.
- **Bước lặp `REACH_(k+1)`:** Thêm tất cả các ký hiệu (cả biến lẫn terminal) xuất hiện ở **VẾ PHẢI** của các luật có vế trái thuộc `REACH_k`.
- Dừng khi không thêm được ký hiệu nào nữa.
- **Xóa bỏ:** Mọi ký hiệu **KHÔNG THUỘC `REACH`** và tất cả các luật chứa chúng.

---

### 2.6. GIẢI CHI TIẾT TRỌN BỘ BÀI TẬP SLIDE 33

#### BÀI TẬP 33 (i):
**ĐỀ BÀI:** Rút gọn văn phạm `G` có các quy tắc:
```text
S → aAa
A → Sb | bCC | DaA
C → abb | DD
E → aC
D → aDA
```

**BÀI LÀM TỪNG BƯỚC CHUẨN 10/10:**
- Văn phạm không có `ε`-quy tắc và không có quy tắc đơn vị.
- **Bước 1: Khử ký hiệu vô sinh (Loại 1):**
  + Tìm tập `GEN`:
    * Xét luật sinh ra terminal: `C → abb` ⇒ `C ∈ GEN_0`.
    * Xét biến `D`: chỉ có luật `D → aDA`, không có luật nào dừng ra terminal, và `D` phụ thuộc chính `D` ⇒ `D` là biến vô sinh! (`D ∉ GEN`).
    * Xét `C`: có `C → abb`, nên `C ∈ GEN`.
    * Xét `A`: có `A → bCC` (vì `C ∈ GEN` nên `bCC` sinh ra terminal) ⇒ `A ∈ GEN`.
    * Xét `S`: có `S → aAa` (vì `A ∈ GEN`) ⇒ `S ∈ GEN`.
    * Xét `E`: có `E → aC` ⇒ `E ∈ GEN`.
    Vậy `GEN = {S, A, C, E}`. Biến vô sinh duy nhất là `D`.
  + **Xóa biến vô sinh `D`:** Xóa mọi luật chứa `D` (`A → DaA`, `C → DD`, `D → aDA`).
  + Các luật còn lại:
    ```text
    S → aAa
    A → Sb | bCC
    C → abb
    E → aC
    ```
- **Bước 2: Khử ký hiệu không đến được (Loại 2):**
  + Tìm tập `REACH` xuất phát từ `S`:
    * `REACH_0 = { S }`
    * Từ `S → aAa` ⇒ `REACH_1 = { S, A, a }`
    * Từ `A → Sb | bCC` ⇒ `REACH_2 = { S, A, C, a, b }`
    * Từ `C → abb` ⇒ không sinh thêm ký hiệu mới.
    * Ký hiệu `E` hoàn toàn không xuất hiện ở vế phải của bất kỳ luật nào dẫn từ `S` ⇒ `E` không đến được (`E ∉ REACH`).
  + **Xóa ký hiệu `E`:** Xóa biến `E` và luật `E → aC`.

**KẾT QUẢ VĂN PHẠM RÚT GỌN:**
```text
S → aAa
A → Sb | bCC
C → abb
```

---

#### BÀI TẬP 33 (ii):
**ĐỀ BÀI:** Rút gọn văn phạm `G` có các quy tắc:
```text
S → aAa
A → bBB
B → ab
C → aB
```

**BÀI LÀM TỪNG BƯỚC CHUẨN 10/10:**
- Không có `ε`-quy tắc và quy tắc đơn vị.
- **Bước 1: Khử ký hiệu vô sinh:**
  + `B → ab` ⇒ `B ∈ GEN`.
  + `A → bBB` ⇒ `A ∈ GEN`.
  + `S → aAa` ⇒ `S ∈ GEN`.
  + `C → aB` ⇒ `C ∈ GEN`.
  ⇒ Mọi biến đều sinh (`GEN = {S, A, B, C}`), không có biến vô sinh.
- **Bước 2: Khử ký hiệu không đến được:**
  + `REACH_0 = { S }`
  + Từ `S → aAa` ⇒ thêm `A, a`.
  + Từ `A → bBB` ⇒ thêm `B, b`.
  + Từ `B → ab` ⇒ không thêm gì mới.
  + Biến `C` không hề xuất hiện ở vế phải của chuỗi dẫn xuất từ `S` ⇒ `C ∉ REACH`.
  + Xóa biến `C` và luật `C → aB`.

**KẾT QUẢ VĂN PHẠM RÚT GỌN:**
```text
S → aAa
A → bBB
B → ab
```

---

#### BÀI TẬP 33 (iii):
**ĐỀ BÀI:** Rút gọn văn phạm `G` có các quy tắc:
```text
S → AB | CA
B → BC | AB
A → a
C → aB | b
```

**BÀI LÀM TỪNG BƯỚC CHUẨN 10/10:**
- Không có `ε`-quy tắc và quy tắc đơn vị.
- **Bước 1: Khử ký hiệu vô sinh (Loại 1):**
  + Khởi tạo: `A → a` ⇒ `A ∈ GEN`; `C → b` ⇒ `C ∈ GEN`.
  + Xét biến `B`: các luật của `B` là `B → BC` và `B → AB`. Ở cả 2 luật, vế phải đều chứa `B`. Biến `B` không có bất kỳ đường nào để triệt tiêu biến `B` thành terminal ⇒ `B` là biến vô sinh! (`B ∉ GEN`).
  + Xóa bỏ biến vô sinh `B` và tất cả các luật chứa `B`:
    * Xóa luật `S → AB` (chứa B)
    * Xóa luật `B → BC`, `B → AB`
    * Xóa luật `C → aB` (chứa B)
  + Các luật còn lại:
    ```text
    S → CA
    A → a
    C → b
    ```
- **Bước 2: Khử ký hiệu không đến được (Loại 2):**
  + Từ `S → CA` đến được cả `C, A, a, b`. Tất cả các biến đều đến được.

**KẾT QUẢ VĂN PHẠM RÚT GỌN:**
```text
S → CA
A → a
C → b
(Văn phạm này sinh ra đúng duy nhất 1 chuỗi: w = ba).
```

---

# PHẦN 4: DẠNG 3 - ĐƯA VĂN PHẠM VỀ DẠNG CHUẨN CHOMSKY (CNF)

### 3.1. Định nghĩa Dạng chuẩn Chomsky (Slide 23):
Văn phạm phi ngữ cảnh `G` ở **Dạng chuẩn Chomsky (CNF - Chomsky Normal Form)** nếu mọi quy tắc sinh trong `P` CHỈ CÓ 1 TRONG 2 DẠNG sau:
```text
A → BC    (vế phải gồm đúng 2 BIẾN)
HOẶC
A → a     (vế phải gồm đúng 1 KÝ HIỆU KẾT THÚC)
```
*(Trong đó A, B, C là các biến không kết thúc; a là ký hiệu kết thúc).*

---

### 3.2. Thuật toán 5 bước đưa CFG về dạng chuẩn Chomsky:

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                    5 BƯỚC ĐƯA VỀ DẠNG CHUẨN CHOMSKY (CNF)                   │
│ Bước 1: Khử ε-quy tắc (luật sinh rỗng).                                     │
│ Bước 2: Khử quy tắc đơn vị (A → B).                                         │
│ Bước 3: Khử ký hiệu thừa (vô sinh trước, không đến được sau).              │
│ Bước 4: Cô lập ký hiệu kết thúc ở vế phải có độ dài ≥ 2.                    │
│         (Thay mỗi chữ 'a' bằng biến mới Xa và thêm luật Xa → a).            │
│ Bước 5: Cắt ngắn vế phải có độ dài ≥ 3 thành chuỗi các luật có đúng 2 biến. │
│         (A → B1 B2 ... Bk thay bằng A → B1 C1; C1 → B2 C2...).              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 3.3. BÀI TẬP MẪU GIẢI CHI TIẾT CNF (CHUẨN SLIDE)

#### BÀI TẬP CNF 1 (Slide 26):
**ĐỀ BÀI:** Tìm dạng chuẩn Chomsky (CNF) của văn phạm `G` có các quy tắc:
```text
S → aAbB
A → aA | a
B → bB | b
```

**BÀI LÀM TỪNG BƯỚC CHUẨN 10/10:**
- **Bước 1, 2, 3:** Văn phạm không có `ε`-quy tắc, không có quy tắc đơn vị, không có ký hiệu thừa.
- **Bước 4: Cô lập ký hiệu kết thúc ở vế phải dài:**
  + Các ký hiệu kết thúc `a, b` xuất hiện trong các vế phải có độ dài ≥ 2 (như `aAbB, aA, bB`).
  + Ta đặt các biến mới:
    * `Xa → a` (thay thế cho terminal `a`)
    * `Xb → b` (thay thế cho terminal `b`)
  + Thay thế vào văn phạm, ta được:
    ```text
    S → Xa A Xb B
    A → Xa A | a
    B → Xb B | b
    Xa → a
    Xb → b
    ```
- **Bước 5: Cắt ngắn vế phải dài hơn 2 biến:**
  + Quy tắc `S → Xa A Xb B` có vế phải dài 4 biến. Ta cắt thành:
    * `S → Xa C1`
    * `C1 → A C2`
    * `C2 → Xb B`
    *(Với C1, C2 là các biến mới được thêm vào tập biến Δ)*.

**KẾT QUẢ VĂN PHẠM DẠNG CHUẨN CHOMSKY (CNF):**
```text
S → Xa C1
C1 → A C2
C2 → Xb B
A → Xa A | a
B → Xb B | b
Xa → a
Xb → b
```
*(Kiểm tra: Mọi luật sinh đều có dạng A → BC hoặc A → a. Đạt 100% chuẩn Chomsky!)*

---

#### BÀI TẬP CNF 2 (Slide 24-25):
**ĐỀ BÀI:** Đưa văn phạm `G` sau về dạng chuẩn Chomsky:
```text
S → A | ABA
A → aA | a | B
B → bB | b
```

**BÀI LÀM TỪNG BƯỚC CHUẨN 10/10:**
- **Bước 1:** Không có `ε`-quy tắc.
- **Bước 2: Khử các quy tắc đơn vị:**
  + Quy tắc đơn vị gồm: `S → A` và `A → B`.
  + Chuỗi đơn vị:
    * Từ `B`: có các luật không đơn vị `B → bB | b`.
    * Từ `A → B` ⇒ thêm các luật của `B` vào `A`: `A → bB | b`. Vậy `A → aA | a | bB | b`.
    * Từ `S → A` ⇒ thêm các luật của `A` vào `S`: `S → aA | a | bB | b`.
    * Luật ban đầu của `S`: `S → ABA`.
  + Sau khi xóa luật đơn vị, tập luật là:
    ```text
    S → ABA | aA | a | bB | b
    A → aA | a | bB | b
    B → bB | b
    ```
- **Bước 3:** Không có ký hiệu thừa.
- **Bước 4: Cô lập ký hiệu kết thúc ở vế phải:**
  + Đặt `Xa → a` và `Xb → b`. Thay vào các luật dài:
    ```text
    S → ABA | Xa A | a | Xb B | b
    A → Xa A | a | Xb B | b
    B → Xb B | b
    Xa → a
    Xb → b
    ```
- **Bước 5: Cắt ngắn vế phải dài hơn 2 biến:**
  + Luật `S → ABA` có độ dài 3. Ta tách bằng biến mới `C`:
    * `S → A C`
    * `C → B A`

**KẾT QUẢ VĂN PHẠM DẠNG CHUẨN CHOMSKY (CNF):**
```text
S → AC | Xa A | a | Xb B | b
C → BA
A → Xa A | a | Xb B | b
B → Xb B | b
Xa → a
Xb → b
```

---

# PHẦN 5: DẠNG 4 - OTOMAT ĐẨY XUỐNG (PDA): ĐỊNH NGHĨA & VẾT CHẠY

### 4.1. Bộ 7 thành phần của PDA (Slide 39):
Một Otomat đẩy xuống (PDA) là một bộ 7 hình thức:
```text
A = < Q, Σ, Γ, δ, q0, z0, F >
```
Trong đó:
1. `Q`: Tập hữu hạn các trạng thái.
2. `Σ`: Bảng chữ cái đầu vào (ký hiệu vào).
3. `Γ` (hoặc `Δ`): Bảng chữ cái ngăn xếp (các ký hiệu được phép lưu trong ngăn xếp PDS).
4. `q0 ∈ Q`: Trạng thái khởi đầu.
5. `z0 ∈ Γ`: Ký hiệu đáy ngăn xếp ban đầu.
6. `F ⊆ Q`: Tập hợp các trạng thái kết thúc (chấp nhận).
7. `δ`: Hàm chuyển trạng thái: `Q × (Σ ∪ {ε}) × Γ → 2^(Q × Γ*)`.

---

### 4.2. Ý nghĩa hàm chuyển & Các thao tác ngăn xếp:
Đẳng thức bước chuyển:
```text
δ(q, a, Z) = { (p, γ) }
```
**Ý nghĩa:** Khi máy đang ở trạng thái `q`, đọc ký hiệu đầu vào `a` (nếu `a = ε` thì không dịch đầu đọc), và ký hiệu ở **đỉnh ngăn xếp là `Z`**:
- Máy chuyển sang trạng thái mới là `p`.
- Thay thế ký hiệu đỉnh `Z` bằng chuỗi `γ`.

**3 Thao tác ngăn xếp cốt lõi cần nhớ:**
- **Lấy ra (POP):** `γ = ε` ⇒ Xóa ký hiệu `Z` ở đỉnh ngăn xếp (ngăn xếp ngắn đi 1 phần tử).
- **Giữ nguyên (NO-OP):** `γ = Z` ⇒ Đỉnh ngăn xếp vẫn giữ nguyên là `Z`.
- **Đẩy vào (PUSH):** `γ = XZ` ⇒ Đẩy thêm ký hiệu `X` vào đỉnh ngăn xếp, đè lên trên `Z`. (Nếu `γ = XYZ` thì `X` ở trên cùng, rồi đến `Y`, rồi đến `Z`).

---

### 4.3. Hai cơ chế đoán nhận chuỗi:
1. **Đoán nhận bằng Ngăn xếp rỗng (Empty stack - `N(A)`):**
   ```text
   N(A) = { w ∈ Σ* | (q0, w, z0) ⊢* (p, ε, ε) với p ∈ Q tùy ý }
   ```
   *(Chuỗi vào đọc hết VÀ ngăn xếp trống rỗng).*
2. **Đoán nhận bằng Trạng thái kết thúc (Final state - `T(A)`):**
   ```text
   T(A) = { w ∈ Σ* | (q0, w, z0) ⊢* (p, ε, γ) với p ∈ F }
   ```
   *(Chuỗi vào đọc hết VÀ máy dừng tại một trạng thái chấp nhận thuộc F, ngăn xếp còn lại gì không quan trọng).*

---

### 4.4. Cách viết vết chạy hình trạng (⊢) ăn trọn điểm (Slide 44, 48, 57):
Mỗi tình huống tức thời (hình trạng) của PDA được viết dưới dạng bộ 3:
```text
(trạng_thái_hiện_tại, phần_chuỗi_vào_chưa_đọc, các_ký_hiệu_trong_ngăn_xếp)
```
Ký hiệu `⊢` biểu diễn một bước chuyển hình trạng; `⊢*` biểu diễn nhiều bước chuyển liên tiếp.

#### BÀI TẬP VẾT CHẠY MẪU 1 (Slide 48):
Cho PDA `A = < {q0, q1, q2}, {a, b}, {z0, z1}, δ, q0, z0, {q2} >` với:
```text
δ(q0, ε, z0) = {(q0, ε)}
δ(q0, a, z0) = {(q1, z0 z1)}
δ(q1, a, z1) = {(q1, z1 z1)}
δ(q1, b, z1) = {(q2, ε)}
δ(q2, b, z1) = {(q2, ε)}
δ(q2, ε, z0) = {(q0, ε)}
```
*(Ngôn ngữ mà A đoán nhận là N(A) = T(A) = { a^n b^n | n ≥ 0 }).*

**Yêu cầu:** Viết vết chạy kiểm tra chuỗi `w1 = aabb` và chuỗi `w2 = abaab`.

**BÀI LÀM TRÌNH BÀY ĐI THI:**
1. **Kiểm tra chuỗi w1 = "aabb":**
   ```text
   (q0, aabb, z0)
   ⊢ (q1, abb, z0 z1)       [Đọc 'a', đỉnh z0 thay bằng z0 z1: đẩy z1 vào]
   ⊢ (q1, bb, z0 z1 z1)     [Đọc 'a', đỉnh z1 thay bằng z1 z1: đẩy thêm z1 vào]
   ⊢ (q2, b, z0 z1)         [Đọc 'b', đỉnh z1 thay bằng ε: lấy z1 ra]
   ⊢ (q2, ε, z0)            [Đọc 'b', đỉnh z1 thay bằng ε: lấy z1 ra]
   ⊢ (q0, ε, ε)             [Đọc ε, đỉnh z0 thay bằng ε: lấy z0 ra]
   ```
   **Kết luận:** Đọc hết chuỗi vào `ε` và ngăn xếp rỗng `ε` ⇒ Chuỗi `aabb ∈ N(A)`. Dừng tại `q2` trước đó cũng thỏa `q2 ∈ F` ⇒ `aabb ∈ T(A)`. Chuỗi **ĐƯỢC CHẤP NHẬN**.

2. **Kiểm tra chuỗi w2 = "abaab":**
   ```text
   (q0, abaab, z0)
   ⊢ (q1, baab, z0 z1)      [Đọc 'a', đẩy z1 vào]
   ⊢ (q2, aab, z0)          [Đọc 'b', lấy z1 ra, ngăn xếp còn lại z0]
   ```
   Tại hình trạng `(q2, aab, z0)`: Ký tự tiếp theo là `a`, đỉnh ngăn xếp là `z0`. Hàm chuyển không có bước chuyển `δ(q2, a, z0)` nào được định nghĩa!  
   Máy bị kẹt (treo), không thể đọc tiếp chuỗi vào `aab` và ngăn xếp chưa rỗng.  
   **Kết luận:** Chuỗi `abaab ∉ N(A)` và `abaab ∉ T(A)`. Chuỗi **BỊ TỪ CHỐI**.

---

#### BÀI TẬP VẾT CHẠY MẪU 2 (Slide 51 - Bài 3.4):
**ĐỀ BÀI:** Xét PDA `A = ({q0, q1}, {a, b}, {a, Z0}, δ, q0, Z0, ∅)` với:
```text
R1: δ(q0, a, Z0) = {(q0, a Z0)}
R2: δ(q0, a, a)  = {(q0, a a)}
R3: δ(q0, b, a)  = {(q1, ε)}
R4: δ(q1, b, a)  = {(q1, ε)}
R5: δ(q1, ε, a)  = {(q1, ε)}
```
Xác định `N(A)` và kiến thiết PDA `B` để `T(B) = N(A)`.

**BÀI LÀM CHUẨN 10/10:**
1. **Phân tích cơ chế hoạt động:**
   - Tại `q0`: mỗi khi đọc ký tự `a`, máy đẩy 1 ký hiệu `a` vào ngăn xếp (R1, R2). Nếu đọc `n` chữ `a` thì trong ngăn xếp có `n` chữ `a` trên đáy `Z0`.
   - Gặp ký tự `b` đầu tiên: máy chuyển sang `q1` và xóa 1 chữ `a` khỏi ngăn xếp (R3).
   - Tại `q1`: tiếp tục đọc `b` và mỗi lần đọc 1 chữ `b` thì xóa 1 chữ `a` (R4). Giả sử đọc `m` chữ `b`, lúc này đã xóa `m` chữ `a`.
   - Luật R5: `δ(q1, ε, a) = {(q1, ε)}` cho phép tự động xóa các chữ `a` còn lại trong ngăn xếp mà không cần đọc thêm ký hiệu vào nào!
   - Tuy nhiên, đáy `Z0` **không có luật nào để xóa** (không có `δ(..., ε, Z0) = {(..., ε)}`).
   - Do đó, ngăn xếp **không bao giờ rỗng được hoàn toàn** vì luôn còn lại ký hiệu đáy `Z0`!
   - ⇒ **Kết luận:** `N(A) = ∅` (Không có chuỗi nào được chấp nhận theo ngăn xếp rỗng).
2. **Kiến thiết PDA B để đoán nhận theo trạng thái kết thúc T(B):**
   - Thêm trạng thái kết thúc `qf`, thêm bước chuyển khi đáy `Z0` lộ diện thì nhảy sang `qf`:
     `δ(q1, ε, Z0) = {(qf, ε)}` với `F = {qf}`.

---

# PHẦN 6: DẠNG 5 - THIẾT KẾ PDA TRỰC TIẾP CHO CÁC NGÔN NGỮ KINH ĐIỂN

### 5.1. Ngôn ngữ L1 = { a^n b^n | n ≥ 1 } (Đoán nhận bằng ngăn xếp rỗng):
- **Nguyên lý:** Mỗi chữ `a` đẩy 1 ký hiệu vào ngăn xếp; mỗi chữ `b` lấy 1 ký hiệu ra.
- **Xây dựng PDA:** `A = < {q0, q1}, {a, b}, {a, z0}, δ, q0, z0, ∅ >` với các luật `δ`:
  ```text
  1. δ(q0, a, z0) = {(q0, a z0)}    [Đọc chữ 'a' đầu tiên, đẩy 'a' vào đè lên đáy z0]
  2. δ(q0, a, a)  = {(q0, a a)}     [Đọc các chữ 'a' tiếp theo, đẩy tiếp 'a' vào]
  3. δ(q0, b, a)  = {(q1, ε)}       [Gặp chữ 'b' đầu tiên, chuyển sang q1 và lấy 1 chữ 'a' ra]
  4. δ(q1, b, a)  = {(q1, ε)}       [Tại q1, mỗi chữ 'b' lấy tiếp 1 chữ 'a' ra]
  5. δ(q1, ε, z0) = {(q1, ε)}       [Hết chữ 'b', đáy z0 lộ diện, xóa z0 để ngăn xếp rỗng]
  ```

---

### 5.2. Ngôn ngữ L2 = { a^n b^(2n) | n ≥ 1 } (Số b gấp đôi số a - Slide 52 Bài 3.5b):
- **Nguyên lý:** Vì số `b` gấp đôi số `a`, nên mỗi khi đọc 1 chữ `a`, ta **đẩy 2 ký hiệu `A`** vào ngăn xếp. Sau đó mỗi khi đọc 1 chữ `b`, ta lấy 1 ký hiệu `A` ra.
- **Xây dựng PDA:** `A = < {q0, q1}, {a, b}, {A, z0}, δ, q0, z0, ∅ >`:
  ```text
  1. δ(q0, a, z0) = {(q0, A A z0)}  [Đọc 1 chữ 'a', đẩy 2 chữ 'A' vào]
  2. δ(q0, a, A)  = {(q0, A A A)}   [Mỗi chữ 'a' tiếp theo, đỉnh là A, thay bằng A A A: thêm 2 chữ A]
  3. δ(q0, b, A)  = {(q1, ε)}       [Gặp chữ 'b' đầu tiên, sang q1, lấy 1 chữ A ra]
  4. δ(q1, b, A)  = {(q1, ε)}       [Mỗi chữ 'b' tiếp theo, lấy 1 chữ A ra]
  5. δ(q1, ε, z0) = {(q1, ε)}       [Lấy đáy z0 ra để làm rỗng ngăn xếp]
  ```

---

### 5.3. Ngôn ngữ Palindrome đối xứng có tâm L3 = { w c w^R | w ∈ {a, b}* } (Slide 36-37):
- **Nguyên lý:**
  + Ở nửa đầu `w`: Đọc ký tự nào (`a` hoặc `b`) thì đẩy chính ký hiệu đó vào ngăn xếp.
  + Gặp ký tự tâm `c`: Đổi trạng thái từ `q0` sang `q1`, không thay đổi ngăn xếp.
  + Ở nửa sau `w^R`: Đọc ký tự vào và so sánh với đỉnh ngăn xếp. Nếu giống nhau thì xóa khỏi ngăn xếp (POP).
- **Xây dựng PDA:** `A = < {q0, q1}, {a, b, c}, {a, b, z0}, δ, q0, z0, ∅ >`:
  ```text
  // Giai đoạn 1: Đọc w và đẩy vào ngăn xếp
  δ(q0, a, z0) = {(q0, a z0)},     δ(q0, b, z0) = {(q0, b z0)}
  δ(q0, a, a)  = {(q0, a a)},      δ(q0, b, a)  = {(q0, b a)}
  δ(q0, a, b)  = {(q0, a b)},      δ(q0, b, b)  = {(q0, b b)}

  // Giai đoạn 2: Gặp tâm 'c', đổi trạng thái
  δ(q0, c, z0) = {(q1, z0)},       δ(q0, c, a) = {(q1, a)},       δ(q0, c, b) = {(q1, b)}

  // Giai đoạn 3: Đọc w^R và so khớp
  δ(q1, a, a)  = {(q1, ε)}         [Đọc 'a' khớp với 'a' ở đỉnh ==> lấy ra]
  δ(q1, b, b)  = {(q1, ε)}         [Đọc 'b' khớp với 'b' ở đỉnh ==> lấy ra]

  // Giai đoạn 4: Hết chuỗi, làm rỗng ngăn xếp
  δ(q1, ε, z0) = {(q1, ε)}
  ```

---

### 5.4. Ngôn ngữ số chữ a bằng số chữ b: Na(w) = Nb(w) (Slide 50 Ví dụ 3.5):
- **Nguyên lý:** Ngăn xếp lưu độ lệch số lượng:
  + Nếu số `a` nhiều hơn, ngăn xếp lưu toàn `a`.
  + Nếu số `b` nhiều hơn, ngăn xếp lưu toàn `b`.
  + Gặp ký hiệu cùng loại 	o Đẩy thêm vào.
  + Gặp ký hiệu khác loại 	o Triệt tiêu lẫn nhau (POP).
- **Xây dựng PDA (1 trạng thái q duy nhất):** `B = < {q}, {a, b}, {z0, a, b}, δ, q, z0, ∅ >`:
  ```text
  δ(q, a, z0) = {(q, a z0)},       δ(q, b, z0) = {(q, b z0)}
  δ(q, a, a)  = {(q, a a)},        δ(q, b, b)  = {(q, b b)}
  δ(q, a, b)  = {(q, ε)},          δ(q, b, a)  = {(q, ε)}
  δ(q, ε, z0) = {(q, ε)}
  ```

---

### 5.5. Ngôn ngữ L = { a^n b^m c^n | m, n ≥ 1 } (Slide 52 Bài 3.5a):
- **Nguyên lý:** Số lượng `a` bằng số lượng `c`; số lượng `b` ở giữa độc lập (`m ≥ 1`).
  + Đọc `a`: Đẩy `a` vào ngăn xếp (trạng thái `q0`).
  + Đọc `b`: Chuyển sang trạng thái `q1`, đọc các chữ `b` tùy ý mà **không đụng chạm vào ngăn xếp**.
  + Đọc `c`: Chuyển sang trạng thái `q2`, mỗi chữ `c` lấy 1 chữ `a` ra.
- **Xây dựng PDA:** `A = < {q0, q1, q2}, {a, b, c}, {a, z0}, δ, q0, z0, ∅ >`:
  ```text
  // 1. Đọc a, đẩy vào ngăn xếp:
  δ(q0, a, z0) = {(q0, a z0)}
  δ(q0, a, a)  = {(q0, a a)}

  // 2. Gặp b đầu tiên, sang q1 (giữ nguyên đỉnh a):
  δ(q0, b, a)  = {(q1, a)}

  // 3. Đọc tiếp các chữ b tại q1 (giữ nguyên đỉnh a):
  δ(q1, b, a)  = {(q1, a)}

  // 4. Gặp c đầu tiên, sang q2 và lấy 1 chữ a ra:
  δ(q1, c, a)  = {(q2, ε)}

  // 5. Đọc tiếp các chữ c tại q2, mỗi chữ c lấy 1 chữ a ra:
  δ(q2, c, a)  = {(q2, ε)}

  // 6. Xóa đáy z0 khi đọc hết chuỗi:
  δ(q2, ε, z0) = {(q2, ε)}
  ```

---

### 5.6. Ngôn ngữ L = { a^m b^n | m > n ≥ 1 } (Slide 52 Bài 3.5d):
- **Nguyên lý:** Số chữ `a` nhiều hơn số chữ `b` ít nhất 1 chữ (`m > n`).
  + Đọc `a` đẩy vào ngăn xếp. Đọc `b` lấy `a` ra.
  + Đọc hết `b`, trong ngăn xếp **bắt buộc phải còn ít nhất 1 chữ `a`** (thỏa mãn `m > n`).
  + Dùng bước chuyển `ε` để tự động dọn sạch các chữ `a` còn thừa và xóa đáy `z0`.
- **Xây dựng PDA:** `A = < {q0, q1, q2}, {a, b}, {a, z0}, δ, q0, z0, ∅ >`:
  ```text
  // Đọc a đẩy vào:
  δ(q0, a, z0) = {(q0, a z0)}
  δ(q0, a, a)  = {(q0, a a)}

  // Đọc b lấy a ra:
  δ(q0, b, a)  = {(q1, ε)}
  δ(q1, b, a)  = {(q1, ε)}

  // Đọc hết b, ngăn xếp còn ít nhất 1 chữ 'a', sang q2 để dọn dẹp:
  δ(q1, ε, a)  = {(q2, ε)}    [Bắt buộc phải có bước này để khẳng định còn dư 'a']
  δ(q2, ε, a)  = {(q2, ε)}    [Dọn hết các chữ 'a' còn lại nếu m - n > 1]
  δ(q2, ε, z0) = {(q2, ε)}    [Xóa đáy z0 làm rỗng ngăn xếp]
  ```

---

# PHẦN 7: DẠNG 6 - CHUYỂN ĐỔI GIỮA CFG VÀ PDA (TUYỆT CHIÊU 1 TRẠNG THÁI)

### 6.1. Tuyệt chiêu CFG sang PDA theo Ngăn xếp rỗng N(A) (1 TRẠNG THÁI DUY NHẤT):
Đây là phương pháp **nhanh nhất, dễ làm nhất và hay thi nhất** trong các bài kiểm tra chương 4.

#### CÔNG THỨC RÁP VÀO LÀ CÓ ĐIỂM:
Cho CFG `G = < Σ, Δ, S, P >`.  
Xây dựng PDA `A = < {q}, Σ, Σ ∪ Δ, δ, q, S, ∅ >` gồm **duy nhất 1 trạng thái `q`**, đỉnh ngăn xếp khởi đầu là biến `S`, đoán nhận bằng ngăn xếp rỗng.  
Hàm chuyển `δ` được lập theo đúng 2 nhóm quy tắc:
```text
1. Nhóm quy tắc mở rộng biến (đọc ε):
   Với mỗi quy tắc A → α trong P của CFG:
   ==> δ(q, ε, A) = { (q, α) }

2. Nhóm quy tắc triệt tiêu ký hiệu kết thúc (đọc terminal):
   Với mỗi ký hiệu kết thúc a ∈ Σ:
   ==> δ(q, a, a) = { (q, ε) }
```

---

#### BÀI TẬP MẪU THỰC CHIẾN (Slide 56 - Ví dụ 3.7):
**ĐỀ BÀI:** Xây dựng ôtômát đẩy xuống `A` tương đương với văn phạm phi ngữ cảnh có các quy tắc:
```text
S → 0BB
B → 0S | 1S | 0
```
Kiểm tra xem chuỗi `w = 010^4 = "010000"` có thuộc `N(A)` hay không?

**BÀI LÀM CHUẨN 10/10:**
1. **Định nghĩa PDA A:**
   ```text
   A = ({q}, {0, 1}, {S, B, 0, 1}, δ, q, S, ∅)
   ```
   Trong đó hàm chuyển `δ` gồm:
   - Mở rộng biến `S`:
     `R1: δ(q, ε, S) = {(q, 0BB)}`
   - Mở rộng biến `B`:
     `R2: δ(q, ε, B) = {(q, 0S), (q, 1S), (q, 0)}`
   - Triệt tiêu ký hiệu kết thúc:
     `R3: δ(q, 0, 0) = {(q, ε)}`
     `R4: δ(q, 1, 1) = {(q, ε)}`

2. **Kiểm tra chuỗi `w = 010000` (Viết vết chạy hình trạng):**
   ```text
   (q, 010000, S)
   ⊢ (q, 010000, 0BB)       [Theo R1, mở S thành 0BB]
   ⊢ (q, 10000, BB)         [Theo R3, đọc số 0 đầu, triệt tiêu 0 ở đỉnh]
   ⊢ (q, 10000, 1SB)        [Theo R2, mở B đầu tiên thành 1S]
   ⊢ (q, 0000, SB)          [Theo R4, đọc số 1, triệt tiêu 1 ở đỉnh]
   ⊢ (q, 0000, 0BBB)        [Theo R1, mở S thành 0BB ==> ngăn xếp thành 0BBB]
   ⊢ (q, 000, BBB)          [Theo R3, đọc số 0, triệt tiêu 0 ở đỉnh]
   ⊢ (q, 000, 0BB)          [Theo R2, mở B thành 0]
   ⊢ (q, 00, BB)            [Theo R3, đọc số 0, triệt tiêu 0]
   ⊢ (q, 00, 0B)            [Theo R2, mở B thành 0]
   ⊢ (q, 0, B)              [Theo R3, đọc số 0, triệt tiêu 0]
   ⊢ (q, 0, 0)              [Theo R2, mở B cuối cùng thành 0]
   ⊢ (q, ε, ε)              [Theo R3, đọc số 0 cuối, triệt tiêu 0 ==> Ngăn xếp rỗng!]
   ```
   **Kết luận:** Đọc hết chuỗi và ngăn xếp trở thành rỗng ⇒ **010000 ∈ N(A)**.

---

### 6.2. Chuyển CFG sang PDA theo Trạng thái kết thúc T(A) (Slide 54 - Định lý 3.1):
Nếu đề bài yêu cầu đoán nhận theo **Trạng thái kết thúc `T(A)`**, ta xây dựng PDA 3 trạng thái `{q0, q1, q2}`:
```text
A = < {q0, q1, q2}, Σ, Σ ∪ Δ ∪ {%}, δ, q0, S, {q2} >
```
Trong đó `%` là ký hiệu đáy ngăn xếp phụ mới, các bước chuyển:
1. Đặt đáy `%` và nạp biến `S`:
   `δ(q0, ε, S) = {(q1, %S)}`
2. Mở rộng biến `A` theo luật `A → α`:
   `δ(q1, ε, A) = {(q1, α^R)}`  *(lưu ý lộn ngược chuỗi α^R vào ngăn xếp)*
3. Triệt tiêu terminal:
   `δ(q1, a, a) = {(q1, ε)}` với mọi `a ∈ Σ`
4. Khi gặp đáy `%`, chuyển sang trạng thái kết thúc `q2`:
   `δ(q1, ε, %) = {(q2, %)}`

---

### 6.3. Chuyển PDA sang CFG (Quy tắc biến [q, Z, p]) (Slide 58-62):
- **Ý nghĩa biến:** Biến có dạng `[q, Z, p]` đại diện cho tập các chuỗi đưa PDA từ trạng thái `q` với ký hiệu đỉnh ngăn xếp `Z` sang trạng thái `p` và xóa bỏ `Z`.
- **Tập quy tắc của văn phạm sinh ra:**
  1. Luật xuất phát:
     `S → [q0, z0, q]` với mọi `q ∈ Q`.
  2. Với mỗi bước chuyển `(p, ε) ∈ δ(q, a, Z)`:
     `[q, Z, p] → a`
  3. Với mỗi bước chuyển `(p, Y1 Y2 ... Yk) ∈ δ(q, a, Z)`:
     Với mọi bộ trạng thái `r1, r2, ..., rk ∈ Q`:
     `[q, Z, rk] → a [p, Y1, r1] [r1, Y2, r2] ... [rk-1, Yk, rk]`

---

# PHẦN 8: DẠNG 7 - GIẢI CHI TIẾT 100% BÀI TẬP LỚN CUỐI SLIDE (3.9, 3.10, 3.11)

---

### 8.1. BÀI TẬP 3.9 (Slide 63):
**ĐỀ BÀI:** Xây dựng văn phạm phi ngữ cảnh sinh ra các ngôn ngữ sau và sau đó xây dựng các PDA để đoán nhận chúng bằng kho đẩy xuống rỗng:
a) `La = { a^n b^n | n ≥ 1 } ∪ { a^m b^(2m) | m ≥ 1 }`
b) `Lb = { a^n b^m c^n | m, n ≥ 1 } ∪ { a^n c^n | n ≥ 1 }`
c) `Lc = { a^n b^m c^m d^n | m, n ≥ 1 }`

**BÀI LÀM CHI TIẾT:**

#### Câu a: `La = { a^n b^n | n ≥ 1 } ∪ { a^m b^(2m) | m ≥ 1 }`
1. **Xây dựng CFG:**
   - Dùng biến `S1` sinh `{a^n b^n | n ≥ 1}`: `S1 → aS1b | ab`.
   - Dùng biến `S2` sinh `{a^m b^(2m) | m ≥ 1}`: `S2 → aS2bb | abb`.
   - Biến xuất phát `S` rẽ 2 nhánh:
     ```text
     S → S1 | S2
     S1 → aS1b | ab
     S2 → aS2bb | abb
     ```
2. **Xây dựng PDA đoán nhận theo ngăn xếp rỗng (Phương pháp 1 trạng thái):**
   `A = ({q}, {a, b}, {S, S1, S2, a, b}, δ, q, S, ∅)` với `δ`:
   - Mở rộng biến:
     `δ(q, ε, S)  = {(q, S1), (q, S2)}`
     `δ(q, ε, S1) = {(q, aS1b), (q, ab)}`
     `δ(q, ε, S2) = {(q, aS2bb), (q, abb)}`
   - Triệt tiêu terminal:
     `δ(q, a, a)  = {(q, ε)}`
     `δ(q, b, b)  = {(q, ε)}`

---

#### Câu b: `Lb = { a^n b^m c^n | m, n ≥ 1 } ∪ { a^n c^n | n ≥ 1 }`
1. **Xây dựng CFG:**
   - Nhánh 1: có `b` ở giữa (`m ≥ 1`), số `a` bằng số `c` (`n ≥ 1`): `S1 → aS1c | aBc; B → bB | b`.
   - Nhánh 2: không có `b` (`a^n c^n` với `n ≥ 1`): `S2 → aS2c | ac`.
   - Gom lại:
     ```text
     S → S1 | S2
     S1 → aS1c | aBc
     B → bB | b
     S2 → aS2c | ac
     ```
2. **Xây dựng PDA:**
   `A = ({q}, {a, b, c}, {S, S1, S2, B, a, b, c}, δ, q, S, ∅)`:
   - Mở rộng:
     `δ(q, ε, S)  = {(q, S1), (q, S2)}`
     `δ(q, ε, S1) = {(q, aS1c), (q, aBc)}`
     `δ(q, ε, B)  = {(q, bB), (q, b)}`
     `δ(q, ε, S2) = {(q, aS2c), (q, ac)}`
   - Triệt tiêu:
     `δ(q, a, a) = {(q, ε)}; δ(q, b, b) = {(q, ε)}; δ(q, c, c) = {(q, ε)}`

---

#### Câu c: `Lc = { a^n b^m c^m d^n | m, n ≥ 1 }`
1. **Xây dựng CFG:**
   - Cặp `(a, d)` bọc ngoài, cặp `(b, c)` nằm bên trong:
     ```text
     S → aSd | aAd
     A → bAc | bc
     ```
2. **Xây dựng PDA:**
   `A = ({q}, {a, b, c, d}, {S, A, a, b, c, d}, δ, q, S, ∅)`:
   - `δ(q, ε, S) = {(q, aSd), (q, aAd)}`
   - `δ(q, ε, A) = {(q, bAc), (q, bc)}`
   - `δ(q, a, a) = {(q, ε)}; δ(q, b, b) = {(q, ε)}; δ(q, c, c) = {(q, ε)}; δ(q, d, d) = {(q, ε)}`

---

### 8.2. BÀI TẬP 3.10 (Slide 64):
**ĐỀ BÀI:** Cho ngôn ngữ phi ngữ cảnh `L = { a^n c b^m c d^k | n > m > 0, k > 0 }`.
(i) Tìm văn phạm phi ngữ cảnh `G` để sinh ra `L` (`L(G) = L`).
(ii) Chỉ ra một dẫn xuất chứng tỏ từ `a^3 c b^2 c d^2` được sinh ra bởi `G`.
(iii) Xây dựng cây cú pháp của từ `a^3 c b^2 c d^2`.
(iv) Xây dựng ôtômát đẩy xuống `A` để đoán nhận `L`.
(v) Chỉ ra một dẫn xuất chứng tỏ từ `a^3 c b^2 c d^2` được đoán nhận bởi `A`.

**BÀI LÀM CHUẨN 10/10:**

#### Ý (i): Tìm văn phạm CFG G
- Phân tích: `n > m > 0` nghĩa là `n = m + p` với `p ≥ 1`.
  Chuỗi có dạng: `a^p a^m c b^m c d^k`.
  + Phần `a^m c b^m`: sinh bởi biến `M`: `M → aMb | acb` (với `m ≥ 1`).
  + Phần `a^p` đệm thêm vào đầu (`p ≥ 1`): `A → aA | aM`.
  + Phần `c d^k` ở đuôi (`k ≥ 1`): `D → c K; K → dK | d`.
- **Tập luật sinh P:**
  ```text
  S → A D
  A → aA | aM
  M → aMb | acb
  D → cK
  K → dK | d
  ```

#### Ý (ii): Dẫn xuất sinh ra từ `w = a^3 c b^2 c d^2` (n=3, m=2, k=2):
```text
S ⇒ A D
  ⇒ aM D           (chọn p = 1: 1 chữ 'a' dư)
  ⇒ a(aMb) D       (lần 1 của M)
  ⇒ aa(acb)b D     (lần 2 dừng: M → acb)
  = aaacbb D       (được a^3 c b^2)
  ⇒ aaacbb cK      (D → cK)
  ⇒ aaacbb cdK     (K → dK)
  ⇒ aaacbb cdd     (K → d)
  = a^3 c b^2 c d^2
```

#### Ý (iii): Cây cú pháp của từ `a^3 c b^2 c d^2`:
```text
                     S
          ┌──────────┴──────────┐
          A                     D
       ┌──┴──┐               ┌──┴──┐
       a     M               c     K
          ┌──┼──┐               ┌──┴──┐
          a  M  b               d     K
          ┌──┼──┐                     │
          a  c  b                     d
(Đọc lá từ trái qua phải: a - a - a - c - b - b - c - d - d = a^3 c b^2 c d^2)
```

#### Ý (iv): Xây dựng PDA A đoán nhận L:
Sử dụng phương pháp CFG sang PDA theo ngăn xếp rỗng:
`A = ({q}, {a, b, c, d}, {S, A, M, D, K, a, b, c, d}, δ, q, S, ∅)` với `δ`:
- Mở rộng biến:
  `δ(q, ε, S) = {(q, AD)}`
  `δ(q, ε, A) = {(q, aA), (q, aM)}`
  `δ(q, ε, M) = {(q, aMb), (q, acb)}`
  `δ(q, ε, D) = {(q, cK)}`
  `δ(q, ε, K) = {(q, dK), (q, d)}`
- Triệt tiêu terminal:
  `δ(q, x, x) = {(q, ε)}` với mọi `x ∈ {a, b, c, d}`.

#### Ý (v): Vết chạy hình trạng chứng minh `a^3 c b^2 c d^2 ∈ N(A)`:
```text
  (q, aaacbbcdd, S)
⊢ (q, aaacbbcdd, AD)
⊢ (q, aaacbbcdd, aMD)
⊢ (q, aacbbcdd, MD)
⊢ (q, aacbbcdd, aMbD)
⊢ (q, acbbcdd, MbD)
⊢ (q, acbbcdd, acbbD)
⊢ (q, cbbcdd, cbbD)
⊢ (q, bbcdd, bbD)
⊢ (q, bcdd, bD)
⊢ (q, cdd, D)
⊢ (q, cdd, cK)
⊢ (q, dd, K)
⊢ (q, dd, dK)
⊢ (q, d, K)
⊢ (q, d, d)
⊢ (q, ε, ε)   ===> Ngăn xếp rỗng, đoán nhận thành công!
```

---

### 8.3. BÀI TẬP 3.11 (Slide 65):
**ĐỀ BÀI:** Cho văn phạm phi ngữ cảnh `G` có tập các quy tắc `P = { S → aSa | bSb | cSc | d }`.
(i) Tìm ngôn ngữ `L = L(G)`.
(ii) Xây dựng ôtômát đẩy xuống `A` để đoán nhận `L` theo ngăn xếp rỗng (`L(G) = N(A)`).
(iii) Cho `w1 = aababbccdccbbabaa` và `w2 = ababbcccdbbabaa`. Chỉ ra rằng `w1 ∈ L(G), w1 ∈ N(A)`, còn `w2 ∉ L(G), w2 ∉ N(A)`.
(iv) Xây dựng cây cú pháp của xâu `w1`.

**BÀI LÀM CHUẨN 10/10:**

#### Ý (i): Tìm ngôn ngữ L(G)
- Mỗi lần áp dụng luật đệ quy `S → x S x` (với `x ∈ {a, b, c}`), ta thêm ký hiệu `x` ở đầu và ký hiệu `x` ở đuôi đối xứng nhau.
- Bước dừng duy nhất là `S → d` đặt ký tự `d` ở chính giữa tâm chuỗi.
- ⇒ **Ngôn ngữ sinh ra là:**
  ```text
  L(G) = { w d w^R | w ∈ {a, b, c}* }
  (Tập các chuỗi Palindrome đối xứng qua ký tự tâm 'd' trên bảng chữ cái {a, b, c}).
  ```

#### Ý (ii): Xây dựng PDA A đoán nhận theo ngăn xếp rỗng N(A):
- **Cách 1 (Tuyệt chiêu 1 trạng thái):**
  `A = ({q}, {a, b, c, d}, {S, a, b, c, d}, δ, q, S, ∅)`:
  + `δ(q, ε, S) = {(q, aSa), (q, bSb), (q, cSc), (q, d)}`
  + `δ(q, x, x) = {(q, ε)}` với mọi `x ∈ {a, b, c, d}`.

- **Cách 2 (PDA 2 trạng thái theo cơ chế đẩy/rút ngăn xếp):**
  `A' = ({q0, q1}, {a, b, c, d}, {a, b, c, z0}, δ, q0, z0, ∅)`:
  + Tại `q0` (nửa đầu): đọc `x ∈ {a, b, c}`, đẩy `x` vào ngăn xếp: `δ(q0, x, Z) = {(q0, xZ)}`.
  + Gặp tâm `d`: đổi sang `q1`, giữ nguyên ngăn xếp: `δ(q0, d, Z) = {(q1, Z)}`.
  + Tại `q1` (nửa sau): đọc `x ∈ {a, b, c}`, nếu đỉnh là `x` thì xóa: `δ(q1, x, x) = {(q1, ε)}`.
  + Xóa đáy `z0`: `δ(q1, ε, z0) = {(q1, ε)}`.

#### Ý (iii): Kiểm tra 2 chuỗi w1 và w2:
1. **Xét chuỗi w1 = "aababbccdccbbabaa":**
   - Ký tự tâm là `d`.
   - Nửa trước: `u = aababbcc` (độ dài 8).
   - Nửa sau: `v = ccbbabaa` (độ dài 8).
   - Đảo ngược nửa trước: `u^R = (aababbcc)^R = ccbbabaa = v`.
   - Vì `w1 = u d u^R` nên **w1 ∈ L(G)** và **w1 ∈ N(A)**.
2. **Xét chuỗi w2 = "ababbcccdbbabaa":**
   - Ký tự tâm là `d`.
   - Nửa trước: `u = ababbccc` (độ dài 8, có 3 chữ 'c' ở đuôi).
   - Nửa sau: `v = bbabaa` (độ dài 6).
   - Độ dài hai nửa không bằng nhau (8 ≠ 6) và `u^R ≠ v`.
   - Do đó **w2 ∉ L(G)** và **w2 ∉ N(A)**.

#### Ý (iv): Cây cú pháp của xâu w1:
Chuỗi `w1 = a a b a b b c c d c c b b a b a a`:
```text
                               S
                            ┌──┼──┐
                            a  S  a
                            ┌──┼──┐
                            a  S  a
                            ┌──┼──┐
                            b  S  b
                            ┌──┼──┐
                            a  S  a
                            ┌──┼──┐
                            b  S  b
                            ┌──┼──┐
                            b  S  b
                            ┌──┼──┐
                            c  S  c
                            ┌──┼──┐
                            c  S  c
                               │
                               d
(Đọc lá từ trái sang phải: a-a-b-a-b-b-c-c - d - c-c-b-b-a-b-a-a = w1)
```

---

# PHẦN 9: BẢNG TỔNG KẾT & 5 BẪY THI CẦN NÉ ĐỂ ĐẠT 10 ĐIỂM

### 9.1. BẢNG TRA CỨU CÔNG THỨC 10 GIÂY:

| Tên Dạng Bài | Quy Tắc Cốt Lõi | Mẹo Kiểm Tra Nhanh |
| :--- | :--- | :--- |
| **Cây suy dẫn** | Gốc = S, Nút trong = Biến, Lá = Terminal / ε | Đọc lá từ trái sang phải phải ra đúng chuỗi w |
| **Nhập nhằng** | Tìm 1 chuỗi có 2 cây suy dẫn khác nhau | Chọn chuỗi có từ 2 toán tử trở lên (ababa, a+b*c) |
| **Khử ε** | Tìm NULL = { A ; A ⇒* ε }, sinh tổ hợp không có biến NULL | Nếu S ∈ NULL thì thêm S0 → S / ε |
| **Khử đơn vị** | Tìm cặp A ⇒* B, thay B → α vào A | Xóa sạch luật đơn vị A → B |
| **Khử vô sinh** | Biến không bao giờ sinh ra terminal | Khởi tạo từ biến có luật sinh terminal, lan truyền ngược |
| **Khử không đến** | Ký hiệu không chạm tới được từ S | Khởi tạo từ {S}, lan truyền xuôi theo vế phải |
| **Chomsky CNF** | A → BC hoặc A → a | Cô lập terminal ở luật dài (Xa → a), rồi cắt đôi vế phải |
| **CFG → PDA (rỗng)** | 1 trạng thái q duy nhất | δ(q, ε, A) = {(q, α)} và δ(q, a, a) = {(q, ε)} |
| **Vết chạy PDA** | (trạng thái, chuỗi còn lại, ngăn xếp) ⊢ ... | Kết thúc: (p, ε, ε) nếu rỗng, hoặc (p, ε, γ) với p ∈ F |

---

### 9.2. 5 BẪY THI "CHẾT NGƯỜI" CẦN NÉ ĐỂ ĐẠT 10 ĐIỂM:

1. **BẪY 1: Rút gọn văn phạm SAI THỨ TỰ:**
   - Nếu đề bài yêu cầu "Rút gọn văn phạm", tuyệt đối **KHÔNG ĐƯỢC** làm theo cảm tính.
   - Thầy chấm theo barem thứ tự 4 bước:
     `Khử ε ==> Khử đơn vị ==> Khử vô sinh ==> Khử không đến được`.
   - Làm sai thứ tự (ví dụ khử không đến được trước vô sinh) sẽ sinh ra biến thừa mới và bị trừ 50% số điểm!

2. **BẪY 2: Nhầm lẫn giữa N(A) (ngăn xếp rỗng) và T(A) (trạng thái kết thúc):**
   - Nếu đề bài ghi `N(A)`: Không cần quan tâm dừng ở trạng thái nào, miễn là chuỗi vào đọc hết `ε` VÀ ngăn xếp trống trơn `ε`.
   - Nếu đề bài ghi `T(A)`: Phải dừng tại trạng thái thuộc `F`, trong ngăn xếp còn gì cũng được.
   - Đừng bao giờ nhầm lẫn 2 điều kiện này khi kết luận chuỗi được chấp nhận hay từ chối!

3. **BẪY 3: Quên trường hợp chuỗi rỗng khi khử ε-quy tắc:**
   - Sau khi khử `ε`, nếu biến xuất phát `S` thuộc tập triệt tiêu `NULL` (nghĩa là `ε ∈ L(G)`), bạn phải bổ sung thêm biến bắt đầu mới `S0` và luật:
     `S0 → S | ε`.
   - Nếu quên `S0 → ε`, văn phạm mới sẽ bị mất chuỗi rỗng `ε` và bị trừ điểm.

4. **BẪY 4: Cố vẽ PDA nhiều trạng thái phức tạp khi chuyển từ CFG:**
   - Khi đề bài yêu cầu "Xây dựng PDA đoán nhận ngôn ngữ sinh bởi văn phạm CFG", hãy dùng ngay **Phương pháp 1 trạng thái duy nhất** (Slide 56).
   - Đừng cố vẽ nhiều trạng thái vì rất dễ viết thiếu bước chuyển và bị trừ điểm. Cách 1 trạng thái là chuẩn giáo trình 100% và luôn được điểm tuyệt đối!

5. **BẪY 5: Viết vết chạy (⊢) thiếu lý do hoặc đoán nhẩm:**
   - Khi viết vết chạy `(q, w, α) ⊢ (q', w', α')`, hãy ghi chú bên cạnh: áp dụng luật nào (`R1, R2...`), đọc ký tự gì, lấy cái gì ra khỏi ngăn xếp.
   - Giám khảo sẽ nhìn vào từng dòng biến đổi để chấm điểm thành phần!
