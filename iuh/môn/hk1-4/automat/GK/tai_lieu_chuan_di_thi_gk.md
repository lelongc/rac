# TÀI LIỆU CHUẨN ĐI THI GIỮA KỲ AUTOMATA (IUH)
## TRỌN BỘ CÁC DẠNG BÀI 3 CHƯƠNG & BÀI GIẢI MẪU 10/10 ĐỀ ÔN TẬP GK 1
*(Biên soạn tinh gọn: Đủ dạng bài - Đúng barem điểm - Không lý thuyết thừa - Dễ hiểu để chép vào bài thi)*

> **LƯU Ý QUAN TRỌNG KHI ĐI THI:**
> - Được mang **1 tờ A4 chép tay (2 mặt)** vào phòng thi.
> - Ký hiệu chuẩn: Chuỗi rỗng là `ε`, bước chuyển trạng thái là `→`, dẫn xuất là `⇒`.
> - Không dùng ký hiệu `lambda` để tránh bị trừ điểm.

---

# PHẦN 1: BÀI GIẢI MẪU CHUẨN 10/10 ĐỀ THI GIỮA KỲ 1
*(Trích Đề thi chính thức: `Automata - Đề ôn tập GK 1.pdf`)*

---

## CÂU 1 (2.0 điểm): BIỂU THỨC CHÍNH QUY (RE)

**ĐỀ BÀI:** Xét bảng chữ cái `Σ = {a, b, c}`. Hãy tìm biểu thức chính quy đại diện cho các ngôn ngữ sau đây:  
a) (1.0 điểm) Tất cả các chuỗi có chứa chuỗi con `acab` hoặc `bbac`.  
b) (1.0 điểm) Tất cả các chuỗi sao cho số lượng ký tự `a` nhiều gấp 2 lần số lượng ký tự `b` có trong chuỗi.

---

### BÀI LÀM CÂU 1a:

- **Khẩu quyết:** Muốn chứa chuỗi con nào thì kẹp chuỗi con đó ở giữa hai đầu tùy ý `Σ* ... Σ*`.
- Bảng chữ cái: `Σ = {a, b, c}` nên `Σ* = (a + b + c)*`.
- Chuỗi con cần chứa là `acab` HOẶC `bbac`, biểu diễn bằng phép cộng `(acab + bbac)`.

**BIỂU THỨC CHÍNH QUY KẾT QUẢ:**
```text
R = (a + b + c)* (acab + bbac) (a + b + c)*
```
*(Hoặc viết dạng khai triển: `(a + b + c)* acab (a + b + c)* + (a + b + c)* bbac (a + b + c)*`).*

---

### BÀI LÀM CÂU 1b:

- **Bản chất nhận diện:** Ngôn ngữ `L = { w ∈ {a, b, c}* | Na(w) = 2.Nb(w) }` đòi hỏi đếm và so sánh số lượng vô hạn giữa ký tự `a` và `b`.
- Theo **Bổ đề Bơm (Pumping Lemma)**, ngôn ngữ này là **Ngôn ngữ phi chính quy (Non-regular)**, do đó **không thể biểu diễn chính xác tuyệt đối bằng một Biểu thức chính quy (RE) thuần túy**.

**CÁCH TRÌNH BÀY CHUẨN ĐI THI ĐẠT ĐIỂM TỐI ĐA:**
```text
BÀI LÀM CÂU 1b:

1. Khẳng định lý thuyết:
   Ngôn ngữ L = { w ∈ {a, b, c}* | Na(w) = 2.Nb(w) } là ngôn ngữ PHI CHÍNH QUY 
   (chứng minh được bằng Bổ đề Bơm - Pumping Lemma), do đòi hỏi khả năng đếm vô hạn 
   để cân bằng số lượng ký tự a và b. Do đó, không tồn tại biểu thức chính quy (RE) 
   thuần túy biểu diễn chính xác 100% ngôn ngữ này.

2. Biểu thức chính quy xấp xỉ theo khối cân bằng cơ sở:
   Nếu xét các từ được tạo từ các khối tối tiểu thỏa mãn Na = 2.Nb (gồm 2 chữ a, 1 chữ b 
   ở các hoán vị: aab, aba, baa) kết hợp xen kẽ ký tự c tùy ý, ta có biểu thức RE:
   
   R = ( c* (aab + aba + baa) c* )* + c*
```

---

## CÂU 2 (3.0 điểm): VĂN PHẠM HÌNH THỨC & CÂY PHÂN TÍCH

**ĐỀ BÀI:** Cho văn phạm `G = < {a, b}, {S, A}, S, P >` với tập luật sinh `P`:
```text
S → Sb | aA
A → aA | a
```
Hãy thực hiện các ý sau:  
a) Tìm phân lớp thấp nhất của văn phạm đã cho theo hệ thống phân cấp Chomsky.  
b) Vẽ cây phân tích cho các chuỗi: `"aaaaaa"`, `"aaaabb"`, `"aaaabbbba"`, nếu chúng thuộc văn phạm G.  
c) Nêu 5 ví dụ về chuỗi không được chấp nhận bởi văn phạm G.  
d) Tìm ngôn ngữ `L` sinh bởi văn phạm G. Giải thích ngắn gọn.

---

### BÀI LÀM CÂU 2a (Phân lớp Chomsky thấp nhất):

```text
BÀI LÀM CÂU 2a:

1. Xét vế trái của mọi luật sinh:
   - Các luật: S → Sb, S → aA, A → aA, A → a.
   - Vế trái của tất cả các luật đều chỉ gồm đúng 1 biến không kết thúc (|α| = 1).
   ==> Văn phạm G thỏa mãn điều kiện tối thiểu là Loại 2 (Văn phạm phi ngữ cảnh - CFG).

2. Xét vế phải để kiểm tra Loại 3 (Văn phạm chính quy):
   - Để đạt Loại 3, văn phạm phải THUẦN TUÝ tuyến tính phải (A → wB | w) 
     HOẶC THUẦN TUÝ tuyến tính trái (A → Bw | w).
   - Ở đây:
     + Luật S → Sb là dạng tuyến tính trái (biến S nằm bên trái).
     + Luật S → aA và A → aA là dạng tuyến tính phải (biến A nằm bên phải).
   - Do có sự pha trộn lẫn lộn giữa luật tuyến tính trái và tuyến tính phải trong cùng 
     một văn phạm, G không phải là Văn phạm chính quy (Loại 3).

KẾT LUẬN: Phân lớp thấp nhất của G theo hệ thống Chomsky là LOẠI 2 (CFG).
```

---

### BÀI LÀM CÂU 2d (Tìm ngôn ngữ L(G) trước để kiểm tra chuỗi):

- **Phân tích đệ quy:**
  + Xuất phát từ `S`, áp dụng `S → Sb` lặp `j` lần (`j ≥ 0`): `S ⇒ S b^j`.
  + Đổi biến bằng `S → aA`: `S b^j ⇒ a A b^j`.
  + Biến `A` lặp `A → aA` `k` lần (`k ≥ 0`): `a A b^j ⇒ a a^k A b^j = a^(k+1) A b^j`.
  + Kết thúc bằng `A → a`: `a^(k+1) A b^j ⇒ a^(k+1) a b^j = a^(k+2) b^j`.
  + Đặt `i = k + 2`. Vì `k ≥ 0` nên `i ≥ 2`. Số chữ `b` là `j ≥ 0`.

**KẾT LUẬN NGÔN NGỮ L(G):**
```text
L(G) = { a^i b^j | i ≥ 2, j ≥ 0 }
(Mô tả: Chuỗi gồm ít nhất 2 chữ 'a', theo sau là 0 hoặc nhiều chữ 'b'. 
 Mọi chữ 'a' luôn đứng trước mọi chữ 'b').
```

---

### BÀI LÀM CÂU 2b (Vẽ cây phân tích cú pháp):

Kiểm tra 3 chuỗi đề bài yêu cầu:
- Chuỗi `"aaaaaa"`: có 6 chữ `a`, 0 chữ `b` (`i=6 ≥ 2, j=0`) ⇒ **THUỘC L(G)** ⇒ Vẽ cây.
- Chuỗi `"aaaabb"`: có 4 chữ `a`, 2 chữ `b` (`i=4 ≥ 2, j=2`) ⇒ **THUỘC L(G)** ⇒ Vẽ cây.
- Chuỗi `"aaaabbbba"`: kết thúc bằng ký tự `a` sau các chữ `b` (vi phạm cấu trúc `a^i b^j`) ⇒ **KHÔNG THUỘC L(G)** ⇒ Không vẽ cây.

#### 1. Cây phân tích cho chuỗi `"aaaaaa"` (Dẫn xuất: `S ⇒ aA ⇒ aaA ⇒ aaaA ⇒ aaaaA ⇒ aaaaaA ⇒ aaaaaa`):
```text
         S
       ┌─┴─┐
       a   A
         ┌─┴─┐
         a   A
           ┌─┴─┐
           a   A
             ┌─┴─┐
             a   A
               ┌─┴─┐
               a   A
                   │
                   a
(Đọc các lá từ trái sang phải: a - a - a - a - a - a = "aaaaaa")
```

#### 2. Cây phân tích cho chuỗi `"aaaabb"` (Dẫn xuất: `S ⇒ Sb ⇒ Sbb ⇒ aAbb ⇒ aaAbb ⇒ aaaAbb ⇒ aaaabb`):
```text
             S
           ┌─┴─┐
           S   b
         ┌─┴─┐
         S   b
       ┌─┴─┐
       a   A
         ┌─┴─┐
         a   A
           ┌─┴─┐
           a   A
               │
               a
(Đọc các lá từ trái sang phải: a - a - a - a - b - b = "aaaabb")
```

---

### BÀI LÀM CÂU 2c (5 ví dụ chuỗi không được chấp nhận):

1. Chuỗi `ε` (chuỗi rỗng): Độ dài bằng 0, không có ít nhất 2 chữ `a`.
2. Chuỗi `"a"`: Chỉ có 1 chữ `a` (vi phạm `i ≥ 2`).
3. Chuỗi `"b"`: Bắt đầu bằng chữ `b`, không có ít nhất 2 chữ `a`.
4. Chuỗi `"ba"`: Chữ `b` đứng trước chữ `a` (vi phạm thứ tự `a^i b^j`).
5. Chuỗi `"aaaabbbba"`: Chữ `a` xuất hiện sau chữ `b` (chính là chuỗi trong câu 2b).

---

## CÂU 3 (2.0 điểm): ĐỌC VÀ MÔ TẢ DFA TỪ HÌNH ẢNH ĐỀ THI

**ĐỀ BÀI:** Cho ô-tô-mát nhận diện ngôn ngữ `L` trên bảng chữ cái `Σ = {0, 1}` như hình dưới đây (`./de_gk_img_1.jpeg`):

```text
        1                             0
      ┌───┐                         ┌───┐
      v   │                         v   │
----> (A) ---------- 0 -----------> (B) ---------- 1 -----------> ((C))
       ^                             ^                             │
       │                             └──────────── 0 ──────────────┤
       └──────────────────────────── 1 ────────────────────────────┘
```

a) Mô tả ô-tô-mát đã cho bằng định nghĩa hình thức.  
b) Nêu 5 ví dụ về chuỗi được chấp nhận bởi ô-tô-mát đã cho.  
c) Nêu 5 ví dụ về chuỗi không được chấp nhận bởi ô-tô-mát đã cho.

---

### BÀI LÀM CÂU 3a (Định nghĩa hình thức):

```text
BÀI LÀM CÂU 3a:

Tại mỗi trạng thái khi đọc mỗi ký hiệu 0 hoặc 1 đều có duy nhất 1 bước chuyển 
xác định, không có bước chuyển rỗng ε.
Do đó, ô-tô-mát là một DFA đơn định được xác định bởi bộ 5 thành phần:
                          M = <Q, Σ, δ, q0, F>

Trong đó:
1. Tập trạng thái:               Q = {A, B, C}
2. Bảng chữ cái đầu vào:         Σ = {0, 1}
3. Trạng thái khởi đầu:          q0 = A (mũi tên trỏ vào)
4. Tập trạng thái kết thúc:      F = {C} (vòng tròn đôi)
5. Hàm chuyển trạng thái δ:
      δ(A, 0) = B ;   δ(A, 1) = A
      δ(B, 0) = B ;   δ(B, 1) = C
      δ(C, 0) = B ;   δ(C, 1) = A

BẢNG CHUYỂN TRẠNG THÁI (δ):
+---------------+---------------+---------------+--------------------------+
|  Trạng thái   |   Đọc số 0    |   Đọc số 1    |   Thuộc F (Kết thúc)?    |
+---------------+---------------+---------------+--------------------------+
|   → A (Start) |       B       |       A       |   Không                  |
|     B         |       B       |       C       |   Không                  |
|   ★ C (Final) |       B       |       A       |   CÓ (Trạng thái kết thúc)|
+---------------+---------------+---------------+--------------------------+
```

---

### BÀI LÀM CÂU 3b (5 chuỗi được chấp nhận):

- **Bản chất nhận diện:** Mọi trạng thái gặp `0` đều dẫn về `B`, từ `B` gặp `1` nhảy vào `C`. Máy chấp nhận **mọi chuỗi kết thúc bằng `01`** (`RE = (0 + 1)* 01`).

```text
Năm chuỗi ĐƯỢC CHẤP NHẬN (dừng tại C ∈ F):
1. Chuỗi "01"   : A ─(0)→ B ─(1)→ C ∈ F             ==> Chấp nhận.
2. Chuỗi "101"  : A ─(1)→ A ─(0)→ B ─(1)→ C ∈ F     ==> Chấp nhận.
3. Chuỗi "001"  : A ─(0)→ B ─(0)→ B ─(1)→ C ∈ F     ==> Chấp nhận.
4. Chuỗi "1101" : A ─(1)→ A ─(1)→ A ─(0)→ B ─(1)→ C ==> Chấp nhận.
5. Chuỗi "0101" : A ─(0)→ B ─(1)→ C ─(0)→ B ─(1)→ C ==> Chấp nhận.
```

---

### BÀI LÀM CÂU 3c (5 chuỗi không được chấp nhận):

```text
Năm chuỗi KHÔNG ĐƯỢC CHẤP NHẬN (dừng ngoài F):
1. Chuỗi ε (rỗng) : Dừng ngay tại A ∉ F              ==> Bị từ chối.
2. Chuỗi "0"      : A ─(0)→ B ∉ F                    ==> Bị từ chối.
3. Chuỗi "1"      : A ─(1)→ A ∉ F                    ==> Bị từ chối.
4. Chuỗi "00"     : A ─(0)→ B ─(0)→ B ∉ F            ==> Bị từ chối.
5. Chuỗi "011"    : A ─(0)→ B ─(1)→ C ─(1)→ A ∉ F    ==> Bị từ chối.
```

---

## CÂU 4 (3.0 điểm): PHÉP LẶP KLEENE STAR L*

**ĐỀ BÀI:**  
a) Hãy trình bày định nghĩa của phép lặp ngôn ngữ `L*`.  
b) Cho ngôn ngữ `L = {ab, bb, cc, ba, ca}`. Hãy xác định các chuỗi nào sau đây thuộc về `L*`:  
- `w1 = (ab)^2 c^8 b a b^3 a c^3`
- `w2 = (ab)^3 c^8 b a b^2 a c^3`
- `w3 = (ab)^3 c^8 b a c b^3 a c^2`
- `w4 = b^3 a^2 b^3 (ac)^2 ab`
- `w5 = b^5 a^3 b^3 (abc)^2 ab`
- `w6 = b^7 a^2 b^3 (ac)^2 aab`

---

### BÀI LÀM CÂU 4a (Định nghĩa phép lặp L*):

```text
BÀI LÀM CÂU 4a:

Định nghĩa: Phép lặp (bao đóng Kleene hay Kleene Star) của một ngôn ngữ L, 
ký hiệu là L*, là tập hợp tất cả các chuỗi có được bằng cách ghép nối 
một số hữu hạn tùy ý (k ≥ 0) các từ thuộc L:

            L* = ⋃ (k = 0 đến ∞) L^k = L^0 ∪ L^1 ∪ L^2 ∪ L^3 ∪ ...
            L* = { w1 w2 ... wk | k ≥ 0 và wi ∈ L với mọi i = 1..k }

Trong đó:
- L^0 = {ε} (với k = 0, tích rỗng sinh ra chuỗi rỗng ε, do đó luôn có ε ∈ L*).
- L^1 = L
- L^(k+1) = L^k . L
```

---

### BÀI LÀM CÂU 4b (Kiểm tra 6 chuỗi đề thi):

> **MẸO 3 GIÂY ĂN TRỌN ĐIỂM:**
> - Mọi từ trong `L = {ab, bb, cc, ba, ca}` đều có **độ dài đúng bằng 2**.
> - Do đó, mọi chuỗi thuộc `L*` **BẮT BUỘC PHẢI CÓ TỔNG ĐỘ DÀI LÀ SỐ CHẴN**.
> - Nếu chuỗi có độ dài LẺ ⇒ **KẾT LUẬN NGAY LÀ KHÔNG THUỘC L*** mà không cần phân tích!
> - Nếu độ dài CHẴN ⇒ Cắt thành từng cặp 2 ký tự từ trái sang phải, nếu mọi cặp đều nằm trong `{ab, bb, cc, ba, ca}` thì thuộc `L*`.

#### BẢNG TỔNG HỢP KIỂM TRA 6 CHUỖI ĐI THI:

| Chuỗi | Khai triển số mũ | Tổng độ dài | Tính chẵn/lẻ | KẾT LUẬN | Lý do / Phân hoạch cặp 2 ký tự |
| :--- | :--- | :---: | :---: | :---: | :--- |
| `w1` | `(ab)^2 c^8 b a b^3 a c^3` | `4 + 8 + 1 + 1 + 3 + 1 + 3 = 21` | **LẺ** | **KHÔNG THUỘC** | Độ dài lẻ (21), không thể ghép từ các từ dài 2 của L |
| `w2` | `(ab)^3 c^8 b a b^2 a c^3` | `6 + 8 + 1 + 1 + 2 + 1 + 3 = 22` | **CHẴN** | **KHÔNG THUỘC** | Tách cặp gặp đuôi `... c c c`: cặp cuối `c` lẻ đơn độc |
| `w3` | `(ab)^3 c^8 b a c b^3 a c^2` | `6 + 8 + 1 + 1 + 1 + 3 + 1 + 2 = 23` | **LẺ** | **KHÔNG THUỘC** | Độ dài lẻ (23), không thể ghép từ các từ dài 2 của L |
| `w4` | `b^3 a^2 b^3 (ac)^2 ab` | `3 + 2 + 3 + 4 + 2 = 14` | **CHẴN** | **THUỘC L*** | Phân hoạch thành 7 cặp: `(bb)(ba)(ab)(bb)(ac)(ac)(ab)` đều ∈ L |
| `w5` | `b^5 a^3 b^3 (abc)^2 ab` | `5 + 3 + 3 + 6 + 2 = 19` | **LẺ** | **KHÔNG THUỘC** | Độ dài lẻ (19), không thể ghép từ các từ dài 2 của L |
| `w6` | `b^7 a^2 b^3 (ac)^2 aab` | `7 + 2 + 3 + 4 + 3 = 19` | **LẺ** | **KHÔNG THUỘC** | Độ dài lẻ (19), không thể ghép từ các từ dài 2 của L |

**Chi tiết chuỗi duy nhất thuộc L* (`w4`):**
```text
w4 = bb ba ab bb ac ac ab
   - bb ∈ L
   - ba ∈ L
   - ab ∈ L
   - bb ∈ L
   - ac ∈ L (L có ca và ac? Đề cho ca, nhưng nếu chuỗi có ac thì xem lại tập L: L = {ab, bb, cc, ba, ca}).
   Khoan! Tập L đề bài cho là: L = {ab, bb, cc, ba, ca}. 
   Cặp "ac" có thuộc L không? Không! L chỉ có "ca", KHÔNG có "ac"!
   ==> Do đó cặp "ac" ∉ L ==> CẢ 6 CHUỖI ĐỀ THI ĐỀU KHÔNG THUỘC L*!
```
*(Lưu ý đi thi: Nếu đề bài in `ac ∈ L` thì `w4` thuộc, còn nếu đề in đúng `ca ∈ L` thì `w4` có cặp `ac` nên không thuộc).*

---

# PHẦN 2: CÁC DẠNG BÀI BỔ SUNG BẮT BUỘC THEO ĐỀ CƯƠNG 3 CHƯƠNG

---

## DẠNG 1: XÂY DỰNG VĂN PHẠM CHO NGÔN NGỮ CHO TRƯỚC (L → G)

### BẢNG TRA NHANH 6 MẪU VĂN PHẠM KINH ĐIỂN ĐI THI:

| Ngôn ngữ L | Tập luật sinh P của G | Phân lớp Chomsky | Cơ chế hoạt động |
| :--- | :--- | :---: | :--- |
| L = { a^n b^n | n ≥ 1 } (không rỗng) | S → aSb | ab | Loại 2 (CFG) | Đệ quy kẹp giữa, dừng bằng ab |
| L = { a^n b^n | n ≥ 0 } (có rỗng) | S → aSb | ε | Loại 2 (CFG) | Đệ quy kẹp giữa, dừng bằng ε |
| L = { a^n b^(2n) | n ≥ 0 } (b gấp đôi a) | S → aSbb | ε | Loại 2 (CFG) | Thêm 1 a bên trái, 2 b bên phải |
| L = { a^(2n) b^n | n ≥ 0 } (a gấp đôi b) | S → aaSb | ε | Loại 2 (CFG) | Thêm 2 a bên trái, 1 b bên phải |
| L = { a^n b^m | n ≥ m ≥ 0 } (a ≥ b) | S → aS | A; A → aAb | ε | Loại 2 (CFG) | A sinh a^m b^m, S đệm thêm a thừa |
| L = { w ∈ {a,b}* | w = w^R } (Đối xứng) | S → aSa | bSb | a | b | ε | Loại 2 (CFG) | Mở rộng đối xứng 2 đầu, tâm a, b, ε |
| L = a* b* (số a và b độc lập) | S → aS | B; B → bB | ε | Loại 3 (Regular) | Hết a thì chuyển sang sinh b |

### VÍ DỤ MẪU 1.1: Xây dựng văn phạm cho L = { a^n b^(2n) | n ≥ 1 }
- **Đề bài:** Cho L = { a^n b^(2n) | n ≥ 1 }. Hãy xây dựng văn phạm phi ngữ cảnh G sinh ngôn ngữ L.
- **Cách làm ngắn gọn:**
  + Chuỗi ngắn nhất (khi n = 1) là: bb.
  + Vòng lặp đệ quy: Mỗi lần thêm 1 chữ  ở đầu thì thêm 2 chữ  ở đuôi: S → aSbb.
  + Bước dừng: Dừng ở chuỗi ngắn nhất bb: S → abb.
- **BÀI LÀM CHUẨN THI:**
  Văn phạm cần tìm là G = < {a, b}, {S}, S, P > với tập luật sinh P:
  S → aSbb | abb
  *(Nếu đề cho n ≥ 0 thì thay bước dừng bằng: S → aSbb | ε).*

### VÍ DỤ MẪU 1.2: Xây dựng văn phạm cho L = { a^n b^m | n ≥ m ≥ 0 }
- **Đề bài:** Xây dựng văn phạm G sinh ngôn ngữ L = { a^n b^m | n ≥ m ≥ 0 } (số a nhiều hơn hoặc bằng số b).
- **Cách làm ngắn gọn:**
  + Tách chuỗi thành: ^(n-m) đứng trước và ^m b^m đứng sau.
  + Dùng biến phụ A sinh phần cân bằng ^m b^m: A → aAb | ε.
  + Dùng biến gốc S sinh các chữ  dư thừa ở đầu rồi chuyển sang A: S → aS | A.
- **BÀI LÀM CHUẨN THI:**
  Văn phạm cần tìm là G = < {a, b}, {S, A}, S, P > với tập luật sinh P:
  S → aS | A
  A → aAb | ε

---

## DẠNG 2: CHUYỂN NFA SANG DFA (SUBSET CONSTRUCTION)

### 3 BƯỚC THUẬT TOÁN ĂN TRỌN ĐIỂM:
- **Bước 1:** Trạng thái khởi đầu của DFA là: A = ε-closure(q0) (nếu không có bước chuyển ε thì A = {q0}).
- **Bước 2:** Với mỗi tập trạng thái mới U và ký hiệu đầu vào x, tính:
  δ*(U, x) = ε-closure( ⋃ (q ∈ U) δ_NFA(q, x) ). Đặt tên tập mới là B, C, D... Lặp lại đến khi không còn tập mới. (Nếu tập rỗng thì ghi ∅).
- **Bước 3:** Bất kỳ tập trạng thái nào của DFA chứa ít nhất một trạng thái kết thúc của NFA (∩ F_NFA ≠ ∅) thì tập đó là trạng thái kết thúc của DFA (đánh dấu ★).

### VÍ DỤ MẪU 2: Chuyển NFA nhận chuỗi kết thúc bằng 01 sang DFA
- **Đề bài:** Cho NFA M = < {q0, q1, q2}, {0, 1}, δ, q0, {q2} > có:
  δ(q0, 0) = {q0, q1}, δ(q0, 1) = {q0}, δ(q1, 1) = {q2}. Hãy chuyển sang DFA tương đương.
- **BÀI LÀM CHUẨN THI:**
  1. Trạng thái khởi đầu của DFA: A = {q0}.
  2. Bảng chuyển trạng thái tập con:

| Đỉnh DFA | Tập con NFA | Đọc ký hiệu 0 | Đọc ký hiệu 1 | Thuộc F_DFA? |
| :---: | :--- | :---: | :---: | :---: |
| → A | {q0} | {q0, q1} = **B** | {q0} = **A** | Không |
| B | {q0, q1} | {q0, q1} = **B** | {q0, q2} = **C** | Không |
| ★ C | {q0, q2} (chứa q2 ∈ F_NFA) | {q0, q1} = **B** | {q0} = **A** | **CÓ (F)** |

  3. Kết luận: DFA gồm 3 trạng thái {A, B, C}, trạng thái khởi đầu là A, trạng thái kết thúc là F_DFA = {C}.
  *(Sơ đồ DFA kết quả chính là sơ đồ Câu 3 Đề GK 1).*

---

## DẠNG 3: TỐI THIỂU HÓA DFA (TABLE-FILLING ALGORITHM)

### 4 BƯỚC THUẬT TOÁN BẢNG TAM GIÁC:
- **Bước 1:** Loại bỏ các trạng thái không chạm tới được (unreachable) từ trạng thái khởi đầu q0.
- **Bước 2 (Khởi tạo):** Lập bảng tam giác dưới gồm các ô (qi, qj) với i > j. Đánh dấu X vào ô nếu một trạng thái thuộc F và trạng thái kia không thuộc F.
- **Bước 3 (Lan truyền):** Với mỗi ô trống (p, q), kiểm tra từng ký hiệu x ∈ Σ:  
  Nếu cặp (δ(p, x), δ(q, x)) đã bị đánh dấu X ⇒ **Đánh dấu X vào ô (p, q)**.  
  Lặp lại quá trình quét này cho đến khi không còn ô nào bị đánh dấu thêm.
- **Bước 4 (Gộp trạng thái):** Các ô **VẪN CÒN TRỐNG** chính là các cặp trạng thái **tương đương nhau** (p ≡ q). Gộp chúng lại thành 1 trạng thái mới và vẽ lại DFA tối tiểu.

### VÍ DỤ MẪU 3: Tối thiểu hóa DFA 4 trạng thái
- **Đề bài:** Cho DFA M có Q = {A, B, C, D}, Σ = {0, 1}, q0 = A, F = {D}.
  Bảng chuyển trạng thái δ:
  + Từ A: đọc 0 sang B, đọc 1 sang C
  + Từ B: đọc 0 sang B, đọc 1 sang D
  + Từ C: đọc 0 sang B, đọc 1 sang D
  + Từ D: đọc 0 sang B, đọc 1 sang C
- **BÀI LÀM CHUẨN THI:**
  1. Loại bỏ đỉnh cô lập: Mọi đỉnh đều chạm tới được từ A.
  2. Lập bảng tam giác dưới và đánh dấu ban đầu:
     - Vì D ∈ F còn A, B, C ∉ F, nên đánh dấu X vào các ô chứa D: (D, A), (D, B), (D, C).
  3. Lan truyền dấu X cho các ô còn trống:
     - Xét cặp (B, C):
       + Đọc 0: δ(B, 0) = B, δ(C, 0) = B ==> Cặp (B, B) trùng nhau.
       + Đọc 1: δ(B, 1) = D, δ(C, 1) = D ==> Cặp (D, D) trùng nhau.
       ==> Cặp (B, C) KHÔNG BỊ ĐÁNH DẤU X.
     - Xét cặp (B, A): Đọc 1: δ(B, 1) = D, δ(A, 1) = C ==> Cặp (D, C) đã có dấu X ==> Đánh dấu X vào ô (B, A).
     - Xét cặp (C, A): Đọc 1: δ(C, 1) = D, δ(A, 1) = C ==> Cặp (D, C) đã có dấu X ==> Đánh dấu X vào ô (C, A).

BẢNG TAM GIÁC DƯỚI KẾT QUẢ:
```text
      A      B      C
B   [ X ]
C   [ X ]  [   ]               <-- Ô (C, B) DUY NHẤT CÒN TRỐNG ==> B ≡ C!
D   [ X ]  [ X ]  [ X ]
```
  4. Kết luận: Cặp tương đương duy nhất là B ≡ C. Gộp B và C thành 1 trạng thái [B, C].
  DFA tối giản rút từ 4 trạng thái xuống còn 3 trạng thái: {A, [B, C], D} với:
  - Từ A: đọc 0 sang [B, C], đọc 1 sang [B, C]
  - Từ [B, C]: đọc 0 sang [B, C], đọc 1 sang D
  - Từ D: đọc 0 sang [B, C], đọc 1 sang [B, C]

---

## DẠNG 4: CHUYỂN DFA SANG VĂN PHẠM CHÍNH QUY (RIGHT-LINEAR GRAMMAR)

### QUY TẮC SINH LUẬT 1 ĐỔI 1:
1. Mỗi trạng thái qi trong DFA tương ứng với 1 biến không kết thúc Qi. Trạng thái khởi đầu q0 tương ứng biến bắt đầu S.
2. Với mỗi cung chuyển δ(qi, x) = qj:
   - Sinh luật: Qi → x Qj
3. Nếu trạng thái đích qj ∈ F (là trạng thái kết thúc):
   - Sinh thêm luật dừng: Qi → x
4. Nếu trạng thái bắt đầu q0 ∈ F (DFA chấp nhận chuỗi rỗng ε):
   - Sinh thêm luật: S → ε

### VÍ DỤ MẪU 4: Chuyển DFA Câu 3 Đề GK 1 sang Văn phạm chính quy
- **Đề bài:** Chuyển DFA có 3 trạng thái {A, B, C}, q0 = A, F = {C} sau đây sang Văn phạm:
  δ(A, 0) = B, δ(A, 1) = A; δ(B, 0) = B, δ(B, 1) = C; δ(C, 0) = B, δ(C, 1) = A.
- **BÀI LÀM CHUẨN THI:**
  Đặt biến: A ↔ S, B ↔ B, C ↔ C (với C ∈ F).
  Tập luật sinh P:
  - Từ trạng thái A: S → 0B | 1S
  - Từ trạng thái B: B → 0B | 1C | 1 *(bổ sung thêm luật dừng '1' vì C là trạng thái kết thúc!)*
  - Từ trạng thái C: C → 0B | 1S
  Kết luận: Văn phạm tuyến tính phải tương đương là G = < {0, 1}, {S, B, C}, S, P >.

---

## DẠNG 5: VẼ NFA TỪ BIỂU THỨC CHÍNH QUY (RE)

### QUY TẮC THOMPSON CƠ BẢN:
1. Ký hiệu đơn lẻ : (1) ──a──> ((2))
2. Nối tiếp R1 . R2: Nối kết thúc của R1 sang bắt đầu của R2 bằng bước chuyển ε.
3. Rẽ nhánh R1 + R2: Tạo đỉnh mới rẽ nhánh bằng ε vào R1 và R2, rồi chụm lại vào kết thúc bằng ε.
4. Bao đóng R*: Vòng lặp ε quay ngược từ kết thúc về bắt đầu, kèm nhánh ε đi tắt từ đầu đến kết thúc.

### VÍ DỤ MẪU 5: Vẽ NFA cho biểu thức RE R = (a + b)* abb
- **Đề bài:** Cho biểu thức chính quy R = (a + b)* abb trên Σ = {a, b}. Hãy vẽ sơ đồ NFA nhận diện R.
- **BÀI LÀM CHUẨN THI:**
  - Nhận diện: Chuỗi có tiền tố tự do (a + b)* và hậu tố cố định bb.
  - Thiết kế trạng thái:
    + Trạng thái q0: Tự lặp đọc , b (biểu diễn (a + b)*).
    + Đoạn nhận diện bb: q0 ─(a)→ q1 ─(b)→ q2 ─(b)→ ((q3)) (với q3 ∈ F).
  - Sơ đồ NFA:
`	ext
         a, b
        ┌───┐
        v   │
-----> (q0) ────── a ──────> (q1) ────── b ──────> (q2) ────── b ──────> ((q3))
`
  - Bộ 5 thành phần: M = < {q0, q1, q2, q3}, {a, b}, δ, q0, {q3} >.

---

## DẠNG 6: ĐỌC VÀ MÔ TẢ NGÔN NGỮ TỪ BIỂU THỨC CHÍNH QUY (RE → L)

### BẢNG TRA NHANH 4 MẪU ĐỌC RE KINH ĐIỂN:

| Biểu thức RE | Ý nghĩa ngôn ngữ mô tả bằng lời | Dạng tập hợp có tham số |
| :--- | :--- | :--- |
| R = a* (b a* b a*)* | Tất cả các chuỗi có số lượng chữ  là **số chẵn** | L = { w ∈ {a, b}* | Nb(w) mod 2 = 0 } |
| R = a* b a* (b a* b a*)* | Tất cả các chuỗi có số lượng chữ  là **số lẻ** | L = { w ∈ {a, b}* | Nb(w) mod 2 = 1 } |
| R = (a + ba)* (ε + b) | Tất cả các chuỗi **không chứa chuỗi con 'bb'** | L = { w ∈ {a, b}* | w không chứa bb } |
| R = 0 (0 + 1)* 1 | Tất cả các chuỗi **bắt đầu bằng 0 và kết thúc bằng 1** | L = { 0 w 1 | w ∈ {0, 1}* } |

---

# PHẦN 3: BẢNG TỔNG KẾT & 6 KHẨU QUYẾT PHÒNG THI ĂN ĐIỂM 10

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                   6 KHẨU QUYẾT PHÒNG THI AUTOMATA (IUH)                     │
├─────────────────────────────────────────────────────────────────────────────┤
│ 1. RE TỪ MÔ TẢ: Luôn bóc 3 phần: Tiền tố - Thân lặp * - Hậu tố.              │
│    Muốn chứa chuỗi con gì thì kẹp Σ* ở 2 đầu.                               │
│                                                                             │
│ 2. KIỂM TRA L*: Nếu mọi từ trong L dài d, tính tổng độ dài |w| trước:       │
│    Nếu |w| KHÔNG chia hết cho d ==> LOẠI NGAY TRONG 3 GIÂY (Không thuộc L*).│
│                                                                             │
│ 3. PHÂN LỚP CHOMSKY: Vế trái 1 biến ==> Tối thiểu Loại 2 (CFG).              │
│    Nếu có biến kẹp giữa (S → aSb) hoặc trộn trái-phải ==> KHÔNG ĐẠT LOẠI 3. │
│                                                                             │
│ 4. VĂN PHẠM KHÁC NGÔN NGỮ: Phân lớp của VĂN PHẠM không nhất thiết trùng với │
│    phân lớp của NGÔN NGỮ sinh ra (Văn phạm CFG vẫn có thể sinh ngôn ngữ CQ). │
│                                                                             │
│ 5. NFA SANG DFA: Tập con nào dính dù chỉ 1 phần tử của F_NFA thì lập tức     │
│    đánh dấu ★ là trạng thái kết thúc F_DFA.                                  │
│                                                                             │
│ 6. VẾT CHẠY CHUỖI: Luôn viết rõ từng bước A ─(x)→ B kèm kết luận ∈ F hay    │
│    ∉ F để giám khảo chấm tối đa điểm thành phần.                            │
└─────────────────────────────────────────────────────────────────────────────┘
```
