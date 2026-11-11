# TÀI LIỆU PHOTO MANG VÀO PHÒNG THI: CHƯƠNG 4 (CFG & PDA)

## TRỌNG TÂM VÍ DỤ 3.8 (CHUYỂN PDA SANG CFG) & BỘ BÀI MẪU 2 VÍ DỤ MỌI DẠNG

*(Bản cô đọng, rõ ràng từng bước - Tra cứu nhanh trong phòng kiểm tra)*

> **HƯỚNG DẪN DÀNH CHO BẠN KHI LÀM BÀI:**
>
> - Tài liệu này thiết kế để **PHOTO HOẶC MANG VÀO PHÒNG KIỂM TRA MỞ**.
> - Bố cục: Gồm phần **Trọng tâm đặc biệt Ví dụ 3.8 (chắc chắn thi)** + 5 dạng bài còn lại, **mỗi dạng đúng 2 bài tập mẫu chuẩn 100% đề thi của thầy**.
> - Ký hiệu chuẩn: Chuỗi rỗng là `ε`, bước chuyển hình trạng là `⊢`, dẫn xuất là `⇒`.

---

# PHẦN 1: TRỌNG TÂM ĐẶC BIỆT - VÍ DỤ 3.8: CHUYỂN PDA SANG CFG

### 1.1. BẢN CHẤT CỰC DỄ HIỂU CỦA PHÉP BIẾN ĐỔI:

- Trong Otomat đẩy xuống (PDA), máy vừa đổi trạng thái vừa đẩy/rút ngăn xếp.
- Để chuyển sang Văn phạm phi ngữ cảnh (CFG), ta tạo ra các biến có dạng:
  ```text
  [q, Z, p]
  ```
- **Ý NGHĨA BIẾN (Hình ảnh đoàn tàu):**
  + Biến `[q, Z, p]` đại diện cho tất cả các chuỗi ký hiệu đầu vào đưa máy từ **ga đi `q`**, **dọn sạch ký hiệu `Z` ở đỉnh ngăn xếp**, và **cập bến ga đến `p`**.
  + Nếu máy có `n` trạng thái và `m` ký hiệu ngăn xếp, số lượng biến dạng này là: `n × m × n`.
    *(Ví dụ có 2 trạng thái q0, q1 và 2 ký hiệu ngăn xếp Z0, Z ==> có 2 × 2 × 2 = 8 biến + biến bắt đầu S = 9 biến)*.

---

### 1.2. CÔNG THỨC 3 BƯỚC THẦN THÁNH TẠO LUẬT SINH:

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                   3 BƯỚC TẠO LUẬT SINH TỪ PDA SANG CFG                      │
├─────────────────────────────────────────────────────────────────────────────┤
│ BƯỚC 1 (Luật xuất phát từ S):                                               │
│    Với mọi trạng thái q ∈ Q:                                                │
│    ==> S → [q0, z0, q]                                                      │
│    (Xuất phát từ q0 với đáy z0, kết thúc tại bất kỳ ga q nào).              │
│                                                                             │
│ BƯỚC 2 (Khi ngăn xếp bị XÓA RỖNG - POP ra ε):                               │
│    Nếu (p, ε) ∈ δ(q, a, Z)  (với a là ký tự vào hoặc ε):                    │
│    ==> [q, Z, p] → a                                                        │
│                                                                             │
│ BƯỚC 3 (Khi ngăn xếp bị THAY THẾ bằng chuỗi Y1 Y2 ... Yk):                  │
│    Nếu (p, Y1 Y2 ... Yk) ∈ δ(q, a, Z):                                      │
│    Quy tắc "Toa tàu nối đuôi nhau":                                         │
│    ==> [q, Z, rk] → a [p, Y1, r1] [r1, Y2, r2] ... [rk-1, Yk, rk]          │
│    (với mọi trạng thái r1, r2, ..., rk ∈ Q).                                │
│                                                                             │
│    * Trường hợp k = 1 (thay 1 ký hiệu Y1):                                  │
│      [q, Z, r1] → a [p, Y1, r1]     (với mọi r1 ∈ Q)                        │
│    * Trường hợp k = 2 (thay 2 ký hiệu Y1 Y2):                               │
│      [q, Z, r2] → a [p, Y1, r1] [r1, Y2, r2]     (với mọi r1, r2 ∈ Q)       │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 1.3. LỜI GIẢI MẪU 10/10 CHI TIẾT VÍ DỤ 3.8 (SLIDE 59-62)

*(ĐÂY LÀ BÀI THẦY CHO KIỂM TRA - CHÉP ĐÚNG TỪNG DÒNG DƯỚI ĐÂY)*

**ĐỀ BÀI (Slide 59):**
Xây dựng văn phạm phi ngữ cảnh `G` để sinh ra `N(A)`, khi:

```text
A = ({q0, q1}, {a, b}, {Z0, Z}, δ, q0, Z0, ∅)
```

và hàm chuyển `δ` được xác định như sau:

1. `δ(q0, b, Z0) = {(q0, Z Z0)}`
2. `δ(q0, ε, Z0) = {(q0, ε)}`
3. `δ(q0, b, Z)  = {(q0, Z Z)}`
4. `δ(q0, a, Z)  = {(q1, Z)}`
5. `δ(q1, b, Z)  = {(q1, ε)}`
6. `δ(q1, a, Z0) = {(q0, Z0)}`

---

#### BÀI LÀM TỪNG BƯỚC CHUẨN ĐI THI:

#### Bước 1: Khai báo tập biến không kết thúc (V_N)

Tập trạng thái `Q = {q0, q1}` (2 trạng thái); tập ký hiệu ngăn xếp `Γ = {Z0, Z}` (2 ký hiệu).
Tập biến `V_N` gồm biến bắt đầu `S` và `2 × 2 × 2 = 8` biến dạng `[trạng_thái, ký_hiệu_ngăn_xếp, trạng_thái]`:

```text
V_N = { S, 
        [q0, Z0, q0], [q0, Z0, q1], 
        [q0, Z, q0],  [q0, Z, q1], 
        [q1, Z0, q0], [q1, Z0, q1], 
        [q1, Z, q0],  [q1, Z, q1] }
```

#### Bước 2: Tạo các quy tắc xuất phát từ biến S (Bước 1 của công thức)

Vì `Q = {q0, q1}` và đỉnh ban đầu là `Z0`, ta có 2 luật:

- **P1:** `S → [q0, Z0, q0]`
- **P2:** `S → [q0, Z0, q1]`

#### Bước 3: Tạo các quy tắc từ 6 bước chuyển của hàm δ

##### • Xét bước chuyển 1: `δ(q0, b, Z0) = {(q0, Z Z0)}`

- Ở đây: `q = q0`, đọc chữ `b`, đỉnh ngăn xếp là `Z0`. Trạng thái đến là `q0`, ngăn xếp thay bằng 2 ký hiệu `Y1 = Z` và `Y2 = Z0` (k=2).
- Áp dụng công thức `[q0, Z0, r2] → b [q0, Z, r1] [r1, Z0, r2]` với 4 cặp `(r1, r2) ∈ {q0, q1} × {q0, q1}`:
  + Cặp `(r1 = q0, r2 = q0)`: **P3:** `[q0, Z0, q0] → b [q0, Z, q0] [q0, Z0, q0]`
  + Cặp `(r1 = q1, r2 = q0)`: **P4:** `[q0, Z0, q0] → b [q0, Z, q1] [q1, Z0, q0]`
  + Cặp `(r1 = q0, r2 = q1)`: **P5:** `[q0, Z0, q1] → b [q0, Z, q0] [q0, Z0, q1]`
  + Cặp `(r1 = q1, r2 = q1)`: **P6:** `[q0, Z0, q1] → b [q0, Z, q1] [q1, Z0, q1]`

##### • Xét bước chuyển 2: `δ(q0, ε, Z0) = {(q0, ε)}`

- Ở đây: ngăn xếp bị xóa rỗng về `ε`, đọc ký hiệu `ε`.
- Áp dụng công thức xóa rỗng:
  + **P7:** `[q0, Z0, q0] → ε`

##### • Xét bước chuyển 3: `δ(q0, b, Z) = {(q0, Z Z)}`

- Ở đây: `q = q0`, đọc chữ `b`, đỉnh là `Z`. Trạng thái đến `q0`, ngăn xếp thay bằng 2 ký hiệu `Y1 = Z, Y2 = Z` (k=2).
- Áp dụng công thức `[q0, Z, r2] → b [q0, Z, r1] [r1, Z, r2]` với 4 cặp `(r1, r2)`:
  + Cặp `(r1 = q0, r2 = q0)`: **P8:** `[q0, Z, q0] → b [q0, Z, q0] [q0, Z, q0]`
  + Cặp `(r1 = q1, r2 = q0)`: **P9:** `[q0, Z, q0] → b [q0, Z, q1] [q1, Z, q0]`
  + Cặp `(r1 = q0, r2 = q1)`: **P10:** `[q0, Z, q1] → b [q0, Z, q0] [q0, Z, q1]`
  + Cặp `(r1 = q1, r2 = q1)`: **P11:** `[q0, Z, q1] → b [q0, Z, q1] [q1, Z, q1]`

##### • Xét bước chuyển 4: `δ(q0, a, Z) = {(q1, Z)}`

- Ở đây: `q = q0`, đọc chữ `a`, đỉnh là `Z`. Trạng thái đến `q1`, ngăn xếp thay bằng đúng 1 ký hiệu `Y1 = Z` (k=1).
- Áp dụng công thức `[q0, Z, r1] → a [q1, Z, r1]` với `r1 ∈ {q0, q1}`:
  + Khi `r1 = q0`: **P12:** `[q0, Z, q0] → a [q1, Z, q0]`
  + Khi `r1 = q1`: **P13:** `[q0, Z, q1] → a [q1, Z, q1]`

##### • Xét bước chuyển 5: `δ(q1, b, Z) = {(q1, ε)}`

- Ở đây: ngăn xếp bị xóa rỗng về `ε`, đọc ký tự `b`, đến trạng thái `q1`.
- Áp dụng công thức xóa rỗng:
  + **P14:** `[q1, Z, q1] → b`

##### • Xét bước chuyển 6: `δ(q1, a, Z0) = {(q0, Z0)}`

- Ở đây: `q = q1`, đọc chữ `a`, đỉnh là `Z0`. Trạng thái đến `q0`, ngăn xếp thay bằng đúng 1 ký hiệu `Y1 = Z0` (k=1).
- Áp dụng công thức `[q1, Z0, r1] → a [q0, Z0, r1]` với `r1 ∈ {q0, q1}`:
  + Khi `r1 = q0`: **P15:** `[q1, Z0, q0] → a [q0, Z0, q0]`
  + Khi `r1 = q1`: **P16:** `[q1, Z0, q1] → a [q0, Z0, q1]`

---

#### TỔNG HỢP VĂN PHẠM KẾT QUẢ G = <, V_N, S, P >:

Tập luật sinh `P` gồm đúng **16 quy tắc từ P1 đến P16**:

```text
P1 : S → [q0, Z0, q0]
P2 : S → [q0, Z0, q1]

P3 : [q0, Z0, q0] → b [q0, Z, q0] [q0, Z0, q0]
P4 : [q0, Z0, q0] → b [q0, Z, q1] [q1, Z0, q0]
P5 : [q0, Z0, q1] → b [q0, Z, q0] [q0, Z0, q1]
P6 : [q0, Z0, q1] → b [q0, Z, q1] [q1, Z0, q1]

P7 : [q0, Z0, q0] → ε

P8 : [q0, Z, q0] → b [q0, Z, q0] [q0, Z, q0]
P9 : [q0, Z, q0] → b [q0, Z, q1] [q1, Z, q0]
P10: [q0, Z, q1] → b [q0, Z, q0] [q0, Z, q1]
P11: [q0, Z, q1] → b [q0, Z, q1] [q1, Z, q1]

P12: [q0, Z, q0] → a [q1, Z, q0]
P13: [q0, Z, q1] → a [q1, Z, q1]

P14: [q1, Z, q1] → b

P15: [q1, Z0, q0] → a [q0, Z0, q0]
P16: [q1, Z0, q1] → a [q0, Z0, q1]
```

*(Đúng 100% từng chữ và ký hiệu theo Slide 60, 61, 62 của thầy!)*

---

### 1.4. VÍ DỤ BỔ TRỢ: CHUYỂN PDA 1 TRẠNG THÁI SANG CFG

*(Để bạn hiểu thấu bản chất nếu đề đổi thành PDA 1 trạng thái q)*

**ĐỀ BÀI:** Cho PDA `A = ({q}, {a, b}, {Z0, Z}, δ, q, Z0, ∅)` nhận diện chuỗi có:

1. `δ(q, a, Z0) = {(q, Z Z0)}`
2. `δ(q, a, Z)  = {(q, Z Z)}`
3. `δ(q, b, Z)  = {(q, ε)}`
4. `δ(q, ε, Z0) = {(q, ε)}`
   Hãy chuyển sang văn phạm CFG tương đương.

**BÀI LÀM:**

- Chỉ có 1 trạng thái `q`, 2 ký hiệu ngăn xếp `{Z0, Z}` ==> Chỉ có 2 biến dạng `[q, Z, p]`:
  Đặt `A = [q, Z0, q]` và `B = [q, Z, q]`.
- Luật xuất phát: `S → [q, Z0, q]` (tức `S → A`).
- Từ bước chuyển 1 (`δ(q, a, Z0) = {(q, Z Z0)}`):
  `[q, Z0, q] → a [q, Z, q] [q, Z0, q]`  ==> `A → a B A`.
- Từ bước chuyển 2 (`δ(q, a, Z) = {(q, Z Z)}`):
  `[q, Z, q] → a [q, Z, q] [q, Z, q]`    ==> `B → a B B`.
- Từ bước chuyển 3 (`δ(q, b, Z) = {(q, ε)}`):
  `[q, Z, q] → b`                        ==> `B → b`.
- Từ bước chuyển 4 (`δ(q, ε, Z0) = {(q, ε)}`):
  `[q, Z0, q] → ε`                       ==> `A → ε`.

**KẾT QUẢ VĂN PHẠM THU GỌN:**

```text
S → A
A → a B A | ε
B → a B B | b
```

*(Nhìn vào ví dụ 1 trạng thái này bạn sẽ thấy ngay công thức đoàn tàu cực kỳ dễ hiểu!).*

---

# PHẦN 2: DẠNG 1 - CÂY SUY DẪN & CHỨNG MINH VĂN PHẠM NHẬP NHẰNG

> **CÔNG THỨC CHỨNG MINH NHẬP NHẰNG:**
> Tìm **1 chuỗi `w`** có **2 cây suy dẫn khác nhau** (hoặc 2 dẫn xuất trái nhất khác nhau) ⇒ Kết luận văn phạm nhập nhằng.

---

### VÍ DỤ 1.1 (Slide 31): Chứng minh S → SbS | a nhập nhằng

**BÀI LÀM:**

1. Chọn chuỗi `w = "ababa" ∈ L(G)`.
2. Vẽ 2 cây suy dẫn khác nhau:

- **Cây 1 (Nhánh trái kết thúc trước):**

```text
            S
         ┌──┼──┐
         S  b  S
         │   ┌─┼─┐
         a   S b S
             │   │
             a   a
```

- **Cây 2 (Nhánh trái mở rộng tiếp):**

```text
            S
         ┌──┼──┐
         S  b  S
       ┌─┼─┐   │
       S b S   a
       │   │
       a   a
```

3. Cả 2 cây đều sinh ra `ababa` ⇒ **Văn phạm G là NHẬP NHẰNG**.

---

### VÍ DỤ 1.2 (Slide 29): Biểu thức số học S → S + S | S * S | a | b

**BÀI LÀM:**

1. Chọn chuỗi `w = "a + b * a"`.
2. Vẽ 2 cây suy dẫn khác nhau:

- **Cây 1 (Ưu tiên nhân):**

```text
         S
      ┌──┼──┐
      S  +  S
      │   ┌─┼─┐
      a   S * S
          │   │
          b   a
```

- **Cây 2 (Ưu tiên cộng):**

```text
         S
      ┌──┼──┐
      S  *  S
    ┌─┼─┐   │
    S + S   a
    │   │
    a   b
```

3. Cùng chuỗi `a + b * a` có 2 cây suy dẫn khác nhau ⇒ **Văn phạm G là NHẬP NHẰNG**.

---

# PHẦN 3: DẠNG 2 - RÚT GỌN VĂN PHẠM PHI NGỮ CẢNH (4 BƯỚC CHUẨN)

> **THỨ TỰ BẮT BUỘC:**
> `B1: Khử ε ==> B2: Khử đơn vị (A → B) ==> B3: Khử vô sinh (loại 1) ==> B4: Khử không đến được (loại 2)`.

---

### VÍ DỤ 2.1 (Slide 15 + 22): Khử ε và quy tắc đơn vị

**ĐỀ BÀI:** Rút gọn văn phạm có `P = { S → AB, A → aA | ε, B → bB | ε }`.

**BÀI LÀM:**

- **Bước 1 (Khử ε):**
  + Biến triệt tiêu: `NULL = {A, B, S}` (vì `A → ε, B → ε` kéo theo `S → AB → ε`).
  + Tổ hợp các trường hợp:
    * `S → AB`: khi `B=ε` ra `A`, khi `A=ε` ra `B`, khi cả 2 khác `ε` ra `AB` ⇒ `S → AB | A | B`.
    * `A → aA | ε`: khi `A=ε` ra `a` ⇒ `A → aA | a`.
    * `B → bB | ε`: khi `B=ε` ra `b` ⇒ `B → bB | b`.
  + Tập luật sau khi bỏ `ε`:
    `S → AB | A | B; A → aA | a; B → bB | b`.
- **Bước 2 (Khử quy tắc đơn vị S → A và S → B):**
  + Thay `S → A` bằng các luật của `A`: `S → aA | a`.
  + Thay `S → B` bằng các luật của `B`: `S → bB | b`.
- **Bước 3, 4:** Không có ký hiệu thừa.

**KẾT QUẢ:**

```text
S → AB | aA | a | bB | b
A → aA | a
B → bB | b
```

---

### VÍ DỤ 2.2 (Slide 33 - Câu i): Khử vô sinh và không đến được

**ĐỀ BÀI:** Rút gọn văn phạm:

```text
S → aAa
A → Sb | bCC | DaA
C → abb | DD
E → aC
D → aDA
```

**BÀI LÀM:**

- Không có `ε`-quy tắc và quy tắc đơn vị.
- **Bước 1: Khử ký hiệu VÔ SINH (không sinh ra terminal):**
  + `C → abb` ⇒ `C` sinh được terminal.
  + Biến `D`: chỉ có luật `D → aDA` (đệ quy vô tận, không có luật dừng) ⇒ `D` là biến VÔ SINH.
  + Xóa `D` và mọi luật chứa `D` (`A → DaA`, `C → DD`, `D → aDA`).
  + Các luật còn lại: `S → aAa; A → Sb | bCC; C → abb; E → aC`.
- **Bước 2: Khử ký hiệu KHÔNG ĐẾN ĐƯỢC (từ S):**
  + Từ `S → aAa` đến được `A`.
  + Từ `A → bCC` đến được `C`.
  + Biến `E` không hề xuất hiện ở vế phải của bất kỳ luật nào dẫn từ `S` ⇒ `E` KHÔNG ĐẾN ĐƯỢC.
  + Xóa `E` và luật `E → aC`.

**KẾT QUẢ:**

```text
S → aAa
A → Sb | bCC
C → abb
```

---

# PHẦN 4: DẠNG 3 - ĐƯA VĂN PHẠM VỀ DẠNG CHUẨN CHOMSKY (CNF)

> **MỤC TIÊU:** Đưa mọi luật về 1 trong 2 dạng: `A → BC` (2 biến) hoặc `A → a` (1 terminal).

---

### VÍ DỤ 3.1 (Slide 26): Đưa về CNF

**ĐỀ BÀI:** Tìm CNF của văn phạm: `S → aAbB; A → aA | a; B → bB | b`.

**BÀI LÀM:**

1. Văn phạm không có `ε`, không có đơn vị, không có ký hiệu thừa.
2. **Cô lập terminal ở vế phải dài:**
   Đặt `Xa → a` và `Xb → b`. Thay vào các luật:
   `S → Xa A Xb B`
   `A → Xa A | a`
   `B → Xb B | b`
3. **Cắt ngắn vế phải dài ≥ 3:**
   `S → Xa A Xb B` có 4 biến, tách bằng `C1, C2`:
   `S → Xa C1`
   `C1 → A C2`
   `C2 → Xb B`

**KẾT QUẢ CNF:**

```text
S → Xa C1
C1 → A C2
C2 → Xb B
A → Xa A | a
B → Xb B | b
Xa → a
Xb → b
```

---

### VÍ DỤ 3.2 (Slide 24-25): Đưa về CNF có chứa luật đơn vị

**ĐỀ BÀI:** Đưa về CNF: `S → A | ABA; A → aA | a | B; B → bB | b`.

**BÀI LÀM:**

1. Khử quy tắc đơn vị `S → A` và `A → B`:
   + Từ `B → bB | b` thay vào `A → B` ⇒ `A → aA | a | bB | b`.
   + Thay các luật của `A` vào `S → A` ⇒ `S → ABA | aA | a | bB | b`.
2. Cô lập terminal: Đặt `Xa → a, Xb → b`:
   `S → ABA | Xa A | a | Xb B | b`
   `A → Xa A | a | Xb B | b`
   `B → Xb B | b`
3. Cắt ngắn luật 3 biến `S → ABA`:
   `S → A C; C → B A`.

**KẾT QUẢ CNF:**

```text
S → AC | Xa A | a | Xb B | b
C → BA
A → Xa A | a | Xb B | b
B → Xb B | b
Xa → a
Xb → b
```

---

# PHẦN 5: DẠNG 4 - THIẾT KẾ PDA TRỰC TIẾP & VIẾT VẾT CHẠY

---

### VÍ DỤ 4.1 (Slide 48): PDA nhận L = & Vết chạy

**THIẾT KẾ PDA (Đoán nhận bằng ngăn xếp rỗng):**
`A = < {q0, q1}, {a, b}, {a, z0}, δ, q0, z0, ∅ >`:

```text
1. δ(q0, a, z0) = {(q0, a z0)}   [Đọc 'a' đầu, đẩy 'a' vào]
2. δ(q0, a, a)  = {(q0, a a)}    [Đọc các 'a' sau, đẩy thêm 'a']
3. δ(q0, b, a)  = {(q1, ε)}      [Đọc 'b' đầu, sang q1, pop 1 'a']
4. δ(q1, b, a)  = {(q1, ε)}      [Đọc các 'b' sau, pop 1 'a']
5. δ(q1, ε, z0) = {(q1, ε)}      [Xóa đáy z0 khi đọc xong]
```

**VẾT CHẠY KIỂM TRA CHUỖI w = "aabb":**

```text
  (q0, aabb, z0)
⊢ (q0, abb, a z0)     [theo luật 1, đọc 'a']
⊢ (q0, bb, a a z0)    [theo luật 2, đọc 'a']
⊢ (q1, b, a z0)       [theo luật 3, đọc 'b', pop 'a']
⊢ (q1, ε, z0)         [theo luật 4, đọc 'b', pop 'a']
⊢ (q1, ε, ε)          [theo luật 5, đọc ε, pop z0 ==> Ngăn xếp rỗng!]
===> CHẤP NHẬN chuỗi aabb.
```

---

### VÍ DỤ 4.2 (Slide 36-37): PDA nhận Palindrome có tâm w c w^R

**THIẾT KẾ PDA:**
`A = < {q0, q1}, {a, b, c}, {a, b, z0}, δ, q0, z0, ∅ >`:

```text
// Nửa đầu: Đọc gì đẩy nấy vào ngăn xếp
δ(q0, a, Z) = {(q0, a Z)};  δ(q0, b, Z) = {(q0, b Z)}  (với Z ∈ {z0, a, b})

// Gặp tâm 'c': Đổi sang q1, giữ nguyên ngăn xếp
δ(q0, c, Z) = {(q1, Z)}

// Nửa sau: Đọc vào so khớp với đỉnh ngăn xếp
δ(q1, a, a) = {(q1, ε)};    δ(q1, b, b) = {(q1, ε)}

// Xóa đáy z0:
δ(q1, ε, z0) = {(q1, ε)}
```

**VẾT CHẠY KIỂM TRA CHUỖI w = "bacab":**

```text
  (q0, bacab, z0)
⊢ (q0, acab, b z0)
⊢ (q0, cab, a b z0)
⊢ (q1, ab, a b z0)     [gặp tâm 'c', đổi sang q1]
⊢ (q1, b, b z0)        [đọc 'a' khớp đỉnh 'a', pop 'a']
⊢ (q1, ε, z0)          [đọc 'b' khớp đỉnh 'b', pop 'b']
⊢ (q1, ε, ε)           [pop z0 ==> Ngăn xếp rỗng!]
===> CHẤP NHẬN chuỗi bacab.
```

---

# PHẦN 6: DẠNG 5 - CHUYỂN CFG SANG PDA (TUYỆT CHIÊU 1 TRẠNG THÁI)

---

### VÍ DỤ 5.1 (Slide 56 - Ví dụ 3.7): Chuyển CFG sang PDA rỗng N(A)

**ĐỀ BÀI:** Chuyển văn phạm sau sang PDA:

```text
S → 0BB
B → 0S | 1S | 0
```

Kiểm tra xem chuỗi `w = "010000"` có thuộc `N(A)` hay không?

**BÀI LÀM:**

1. **Thiết lập PDA 1 trạng thái q:**
   `A = ({q}, {0, 1}, {S, B, 0, 1}, δ, q, S, ∅)` với `δ`:

   - Mở rộng biến:
     `R1: δ(q, ε, S) = {(q, 0BB)}`
     `R2: δ(q, ε, B) = {(q, 0S), (q, 1S), (q, 0)}`
   - Triệt tiêu terminal:
     `R3: δ(q, 0, 0) = {(q, ε)}`
     `R4: δ(q, 1, 1) = {(q, ε)}`
2. **Vết chạy kiểm tra `w = 010000`:**

   ```text
     (q, 010000, S)
   ⊢ (q, 010000, 0BB)     [R1: mở S thành 0BB]
   ⊢ (q, 10000, BB)       [R3: đọc 0, triệt tiêu 0]
   ⊢ (q, 10000, 1SB)      [R2: mở B thành 1S]
   ⊢ (q, 0000, SB)        [R4: đọc 1, triệt tiêu 1]
   ⊢ (q, 0000, 0BBB)      [R1: mở S thành 0BB]
   ⊢ (q, 000, BBB)        [R3: đọc 0, triệt tiêu 0]
   ⊢ (q, 000, 0BB)        [R2: mở B thành 0]
   ⊢ (q, 00, BB)          [R3: đọc 0, triệt tiêu 0]
   ⊢ (q, 00, 0B)          [R2: mở B thành 0]
   ⊢ (q, 0, B)            [R3: đọc 0, triệt tiêu 0]
   ⊢ (q, 0, 0)            [R2: mở B thành 0]
   ⊢ (q, ε, ε)            [R3: đọc 0, triệt tiêu 0 ==> RỖNG!]
   ```

   **Kết luận:** `010000 ∈ N(A)`.

---

### VÍ DỤ 5.2 (Slide 65 - Bài 3.11): CFG Palindrome sang PDA

**ĐỀ BÀI:** Chuyển `P = { S → aSa | bSb | cSc | d }` sang PDA theo ngăn xếp rỗng.

**BÀI LÀM:**
`A = ({q}, {a, b, c, d}, {S, a, b, c, d}, δ, q, S, ∅)`:

- `δ(q, ε, S) = {(q, aSa), (q, bSb), (q, cSc), (q, d)}`
- `δ(q, a, a) = {(q, ε)}`
- `δ(q, b, b) = {(q, ε)}`
- `δ(q, c, c) = {(q, ε)}`
- `δ(q, d, d) = {(q, ε)}`
  *(Siêu ngắn gọn, viết đúng 6 dòng là đạt điểm tối đa!).*

---

# PHẦN 7: BẢNG TỔNG KẾT KHẮC CỐT GHI TÂM KHI LÀM BÀI THI

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CHECKLIST 5 ĐIỀU ĂN TRỌN ĐIỂM KIỂM TRA                   │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. PDA SANG CFG (VÍ DỤ 3.8):                                                │
│    - Số biến: 1 biến S + (|Q| x |Γ| x |Q|) biến bộ ba [q, Z, p].            │
│    - Luật S: S → [q0, z0, q] với mọi q ∈ Q.                                 │
│    - Xóa rỗng (p, ε): [q, Z, p] → a.                                        │
│    - Đẩy 2 biến (p, Y1 Y2): [q, Z, r2] → a [p, Y1, r1] [r1, Y2, r2].        │
│                                                                             │
│ 2. CFG SANG PDA RỖNG: Dùng PDA 1 trạng thái q duy nhất!                     │
│    - Biến: δ(q, ε, A) = {(q, α)}.                                           │
│    - Terminal: δ(q, a, a) = {(q, ε)}.                                       │
│                                                                             │
│ 3. RÚT GỌN VĂN PHẠM: Phải làm đúng thứ tự 4 bước:                           │
│    Khử ε ==> Khử đơn vị ==> Khử vô sinh ==> Khử không đến được.             │
│                                                                             │
│ 4. CHOMSKY CNF: Phải đưa về đúng 2 dạng A → BC hoặc A → a.                 │
│                                                                             │
│ 5. VẾT CHẠY HÌNH TRẠNG: Mỗi bước viết rõ (trạng_thái, chuỗi_còn, ngăn_xếp)  │
│    kèm chú thích luật áp dụng bên cạnh.                                     │
└─────────────────────────────────────────────────────────────────────────────┘
```
