# BỘ ĐỀ MẪU CUỐI KỲ 2: GIẢI CHI TIẾT 100% ĐỀ MCQ SAMPLE 2 (AUTOMATA & RE)
## KÈM BẢNG ĐƠN ĐỊNH HÓA, TỐI THIỂU HÓA VÀ 10 CÂU BIẾN THỂ KINH ĐIỂN

> **THÔNG TIN ĐỀ BÀI GỐC (Trích Automata - mcq sample 2.pdf):**
> Xét ngôn ngữ $L$ trên bảng chữ cái $\Sigma = \{a, b\}$ được mô tả bởi $\varepsilon$-NFA có đồ thị chuyển trạng thái như sau:
> - Tập trạng thái: $Q = \{q_0, q_1, q_2\}$
> - Trạng thái bắt đầu: $q_0$
> - Trạng thái kết thúc: $F = \{q_2\}$ (vòng tròn kép)
> - Các bước chuyển:
>   + $\delta(q_0, b) = \{q_0\}$
>   + $\delta(q_0, a) = \{q_1\}$
>   + $\delta(q_0, \varepsilon) = \{q_1\}$ (bước chuyển rỗng!)
>   + $\delta(q_1, b) = \{q_2\}$
>   + $\delta(q_2, b) = \{q_0\}$
>   + $\delta(q_2, a) = \{q_1\}$

```text
                  b
                ┌───┐
                │   ▼
  Bắt đầu ───► ( q0 ) ───── a, ε ─────► ( q1 )
                 ▲                      ▲    │
                 │ b                    │    │ b
                 │                 a    │    ▼
               ((( q2 ))) ──────────────┘    │
                    ▲                        │
                    └────────────────────────┘
```

---

# PHẦN 1: BẢN CHẤT CỐT LÕI (2 QUY TẮC VÀNG ĐOÁN NHẬN CHUỖI TRONG 3 GIÂY)

Nhìn vào đồ thị ô-tô-mát trên, ta rút ra được **2 quy tắc vàng** để giải quyết từ Câu 1 đến Câu 12 trong chớp mắt:

### 1. QUY TẮC 1: MỌI CHUỖI HỢP LỆ BẮT BUỘC PHẢI KẾT THÚC BẰNG 'b'
- Nhìn vào đỉnh đích duy nhất là **$q_2$**: Mọi mũi tên đi vào $q_2$ đều chỉ có nhãn là **$b$** (từ $q_1$ đi vào $q_2$ bằng chữ $b$).
- Từ $q_2$ không có bước chuyển $\varepsilon$ nào khác.
👉 **KẾT LUẬN:** *Bất kỳ chuỗi nào kết thúc bằng chữ **`a`** đều KHÔNG HỢP LỆ (BỊ LOẠI NGAY LẬP TỨC)!*
  *(Ví dụ: `a`, `aa`, `ba`, `bba`, `aab`, `aaab`,... loại sạch!)*

### 2. QUY TẮC 2: KHÔNG BAO GIỜ ĐƯỢC CHỨA CỤM "aa"
- Từ bất kỳ trạng thái nào, hễ đọc chữ **$a$** thì máy đều nhảy về $q_1$.
- Nhưng tại $q_1$, **hoàn toàn KHÔNG CÓ đường đi cho chữ $a$**!
👉 **KẾT LUẬN:** *Hễ chuỗi nào xuất hiện 2 chữ $a$ đứng liền nhau (**`aa`**) thì máy rơi vào ngõ cụt (trạng thái bẫy chết $\emptyset$) $\implies$ KHÔNG HỢP LỆ!*

### 3. QUY TẮC 3 (CÁI BẪY ĐUÔI `abb`): SAU `ab` KHÔNG ĐƯỢC KẾT THÚC BẰNG ĐÚNG 1 CHỮ `b`
- Khi đọc xong `ab`, máy chỉ đứng ở duy nhất trạng thái $q_2$ (không còn ở $q_0$).
- Nếu đọc thêm **1 chữ $b$** nữa (thành đuôi `abb`), máy từ $q_2 \xrightarrow{b} q_0 \xrightarrow{\varepsilon} \{q_0, q_1\}$ — **không có $q_2$**, nên **bị loại**! (Phải đọc thêm chữ $b$ thứ ba thành `abbb` hoặc `ab` nữa thành `abbab` thì mới về lại được $q_2$).
👉 **KẾT LUẬN:** *Chuỗi kết thúc bằng **`abb`** (như `abb`, `babb`) đều KHÔNG HỢP LỆ!*

### 4. VẬY NHỮNG CHUỖI NÀO LÀ HỢP LỆ?
- Mọi chuỗi chỉ toàn chữ $b$ (như `b`, `bb`, `bbb`, `bbbb`,...).
- Chuỗi kết thúc bằng `ab` hoặc `abbb...` và không chứa cụm `aa` (như `ab`, `bab`, `abab`, `bbab`, `abbab`, `babab`,...).

---

# PHẦN 2: LỜI GIẢI CHI TIẾT TỪNG CÂU TỪ CÂU 1 ĐẾN CÂU 24

---

### Câu 1: Xét các chuỗi: $s_1 = \text{"b"}$, $s_2 = \text{"a"}$, $s_3 = \text{"aa"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Tất cả các chuỗi được nêu.

👉 **ĐÁP ÁN ĐÚNG: A**
- **Giải thích:**
  - $s_1 = \text{"b"}$: Xuất phát từ $q_0$, đi qua bước chuyển $\varepsilon$ sang $q_1$, đọc chữ $b$ nhảy sang $q_2$ (kết thúc hợp lệ!).
  - $s_2 = \text{"a"}$ và $s_3 = \text{"aa"}$ đều kết thúc bằng chữ $a$ (không về được $q_2$).

---

### Câu 2: Xét các chuỗi: $s_1 = \text{"aa"}$, $s_2 = \text{"a"}$, $s_3 = \text{"ab"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Các chọn lựa khác đều ĐÚNG.

👉 **ĐÁP ÁN ĐÚNG: C**
- **Giải thích:** $s_1, s_2$ kết thúc bằng $a$ (loại). $s_3 = \text{"ab"}$: $q_0 \xrightarrow{a} q_1 \xrightarrow{b} q_2$ (hợp lệ!).

---

### Câu 3: Xét các chuỗi: $s_1 = \text{"bb"}$, $s_2 = \text{"bbb"}$, $s_3 = \text{"bbab"}$, $s_4 = \text{"bba"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1, s_2$, và $s_3$
- B. $s_2, s_3$ và $s_4$
- C. $s_3$ và $s_4$
- D. $s_4$

👉 **ĐÁP ÁN ĐÚNG: A**
- **Giải thích:** $s_4 = \text{"bba"}$ kết thúc bằng chữ $a$ nên không hợp lệ. Còn $s_1, s_2, s_3$ đều kết thúc bằng $b$ và không chứa $aa$ nên đều hợp lệ.

---

### Câu 4: Xét các chuỗi: $s_1 = \text{"abab"}$, $s_2 = \text{"abba"}$, $s_3 = \text{"bab"}$, $s_4 = \text{"aab"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_4$
- C. $s_1$ và $s_3$
- D. $s_1$ và $s_4$

👉 **ĐÁP ÁN ĐÚNG: C**
- **Giải thích:**
  - $s_2 = \text{"abba"}$ kết thúc bằng $a$ (loại).
  - $s_4 = \text{"aab"}$ chứa cụm $aa$ (loại).
  - $s_1 = \text{"abab"}$ và $s_3 = \text{"bab"}$ đều hợp lệ.

---

### Câu 5: Xét các chuỗi: $s_1 = \text{"ba"}$, $s_2 = \text{"babab"}$, $s_3 = \text{"aaaa"}$, $s_4 = \text{"bbbab"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_4$
- C. $s_2$ và $s_3$
- D. $s_1$ và $s_4$

👉 **ĐÁP ÁN ĐÚNG: B**
- **Giải thích:** $s_1, s_3$ kết thúc bằng $a$ (loại). $s_2 = \text{"babab"}$ và $s_4 = \text{"bbbab"}$ đều hợp lệ.

---

### Câu 6: Xét các chuỗi: $s_1 = \text{"ababab"}$, $s_2 = \text{"bbbb"}$, $s_3 = \text{"abbab"}$, $s_4 = \text{"aaab"}$. Chuỗi nào KHÔNG hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. $s_4$

👉 **ĐÁP ÁN ĐÚNG: D**
- **Giải thích:** Đề hỏi chuỗi **KHÔNG** hợp lệ. Chuỗi $s_4 = \text{"aaab"}$ chứa $aa$ nên rơi vào trạng thái bẫy, không thể được đoán nhận.

---

### Câu 7: Xét các chuỗi: $s_1 = \text{"b"}$, $s_2 = \text{"a"}$, $s_3 = \text{"ab"}$, $s_4 = \text{"aa"}$. Chuỗi nào KHÔNG hợp lệ với $L$?
- A. $s_2$
- B. $s_1$
- C. $s_3$
- D. Tất cả các chuỗi đều không hợp lệ.

👉 **ĐÁP ÁN ĐÚNG: A**
- **Giải thích:**
  - $s_1 = \text{"b"}$ và $s_3 = \text{"ab"}$ đều **hợp lệ** $\implies$ Loại B, C và D ("Tất cả các chuỗi đều không hợp lệ").
  - Cả $s_2 = \text{"a"}$ và $s_4 = \text{"aa"}$ đều **không hợp lệ** (kết thúc bằng `a` / chứa `aa`). Tuy nhiên trong 4 phương án đề gốc của thầy chỉ liệt kê $s_2$ ở đáp án A (thiếu $s_4$), nên **A** là đáp án đúng duy nhất có thể chọn.

---

### Câu 8: Xét các chuỗi: $s_1 = \text{"bb"}$, $s_2 = \text{"bbb"}$, $s_3 = \text{"bbab"}$, $s_4 = \text{"bba"}$. Chuỗi nào KHÔNG hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_3$
- C. $s_3$ và $s_4$
- D. $s_4$

👉 **ĐÁP ÁN ĐÚNG: D**
- **Giải thích:** Duy nhất $s_4 = \text{"bba"}$ kết thúc bằng $a$ nên không hợp lệ.

---

### Câu 9: Xét các chuỗi: $s_1 = \text{"bb"}$, $s_2 = \text{"bbb"}$, $s_3 = \text{"bbab"}$, $s_4 = \text{"bba"}$. Chuỗi nào KHÔNG hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Các chọn lựa khác đều SAI.

👉 **ĐÁP ÁN ĐÚNG: D**
- **Giải thích:** Chuỗi không hợp lệ ở đây là $s_4$. Vì $s_1, s_2, s_3$ đều là chuỗi hợp lệ nên các phương án A, B, C đều sai $\implies$ Chọn D.

---

### Câu 10: Xét các chuỗi: $s_1 = \text{"abab"}$, $s_2 = \text{"abba"}$, $s_3 = \text{"bab"}$, $s_4 = \text{"aab"}$. Chuỗi nào KHÔNG hợp lệ với $L$?
- A. $s_1$ và $s_4$
- B. $s_2$ và $s_3$
- C. $s_3$ và $s_4$
- D. Các chọn lựa khác đều SAI. (hoặc nếu có phương án $s_2$ và $s_4$)

👉 **ĐÁP ÁN ĐÚNG: D** (vì cặp không hợp lệ đúng phải là $s_2$ và $s_4$).

---

### Câu 11: Xét các chuỗi: $s_1 = \text{"ba"}$, $s_2 = \text{"babab"}$, $s_3 = \text{"aaaa"}$, $s_4 = \text{"bbbab"}$. Chuỗi nào KHÔNG hợp lệ với $L$?
- A. $s_1, s_2$ và $s_3$
- B. $s_1$ và $s_3$
- C. $s_4$
- D. $s_3$ và $s_4$

👉 **ĐÁP ÁN ĐÚNG: B**
- **Giải thích:** $s_1 = \text{"ba"}$ và $s_3 = \text{"aaaa"}$ đều kết thúc bằng $a$ nên không hợp lệ.

---

### Câu 12: Xét các chuỗi: $s_1 = \text{"ababab"}$, $s_2 = \text{"bbbb"}$, $s_3 = \text{"abbab"}$, $s_4 = \text{"aaab"}$. Chuỗi nào KHÔNG hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. $s_4$

👉 **ĐÁP ÁN ĐÚNG: D** (Do $s_4$ chứa $aa$).

---

### Câu 13: Xét biểu thức chính quy $E_1 = (a+b)^* b$. Chuỗi nào KHÔNG thuộc $L$ nhưng thuộc ngôn ngữ được mô tả bởi $E_1$?
- A. "bbb"
- B. "ab"
- C. "bab"
- D. "bbab"

👉 **ĐÁP ÁN: Đề thi có lỗi kỹ thuật ở các phương án hoặc chọn D (Các lựa chọn khác đều SAI)**
- **Giải thích chuyên sâu:** Biểu thức $E_1 = (a+b)^* b$ mô tả **tất cả các chuỗi kết thúc bằng $b$**.
  Mọi chuỗi thuộc $L$ đều kết thúc bằng $b$, do đó $L \subseteq L(E_1)$.
  Một chuỗi thuộc $E_1$ mà không thuộc $L$ phải là chuỗi kết thúc bằng $b$ nhưng **có chứa $aa$** (ví dụ `aab`, `aaab`, `baab`). Vì cả 4 phương án A, B, C, D đưa ra (`bbb`, `ab`, `bab`, `bbab`) đều thuộc cả $L$ và $E_1$, nên nếu đề có đáp án "Các lựa chọn khác đều SAI" thì chọn đáp án đó, hoặc nếu là câu lỗi của đề gốc thì lưu ý nguyên lý trên.

---

### Câu 14: Xét biểu thức $E_1 = (a+b)^* b$. Chuỗi nào thuộc $L$ nhưng KHÔNG thuộc ngôn ngữ được mô tả bởi $E_1$?
- A. Không có chuỗi nào
- B. "ab"
- C. "abb"
- D. "bbab"

👉 **ĐÁP ÁN ĐÚNG: A**
- **Giải thích:** Vì mọi chuỗi trong $L$ bắt buộc phải kết thúc bằng chữ $b$, mà $E_1 = (a+b)^* b$ chính là tập hợp tất cả các chuỗi kết thúc bằng $b$, nên $L \subseteq L(E_1)$. Do đó **hoàn toàn không có chuỗi nào** thuộc $L$ mà lại không thuộc $E_1$.

---

### Câu 15: Xét biểu thức $E_2 = b^*(ab)^*$. Chuỗi nào KHÔNG thuộc $L$ nhưng thuộc ngôn ngữ được mô tả bởi $E_2$?
- A. "bb"
- B. "bbb"
- C. "abab"
- D. Các chọn lựa khác đều SAI.

👉 **ĐÁP ÁN ĐÚNG: D**
- **Giải thích:** Cả `bb`, `bbb`, `abab` đều thuộc $L$. Do đó không có chuỗi nào trong 3 chuỗi trên là "không thuộc $L$". Đáp án D là chính xác.

---

### Câu 16: Xét biểu thức $E_2 = b^*(ab)^*$. Chuỗi nào thuộc $L$ nhưng KHÔNG thuộc ngôn ngữ được mô tả bởi $E_2$?
- A. "bb"
- B. "bababbb"
- C. "bbabab"
- D. Các chọn lựa khác đều SAI.

👉 **ĐÁP ÁN ĐÚNG: B**
- **Giải thích:**
  - Ngôn ngữ của $E_2 = b^*(ab)^*$ chỉ chấp nhận dạng: một số chữ $b$ ở đầu, sau đó là các cặp $ab$ lặp lại (ví dụ `b`, `bb`, `bbab`, `bbabab`, `abab`).
  - Chuỗi `bababbb` thuộc $L$ (kết thúc bằng $b$, không chứa $aa$), nhưng sau cụm $ab$ nó lại có các chữ $b$ đứng cuối (`bbb`), điều mà $b^*(ab)^*$ không thể sinh ra được. Do đó `bababbb` không thuộc $E_2$.

---

### Câu 17: Xét biểu thức $E_2 = b^*(ab)^*$. Chuỗi nào thuộc $L$ nhưng KHÔNG thuộc ngôn ngữ được mô tả bởi $E_2$?
- A. "abab"
- B. "bab"
- C. "bb"
- D. Các chọn lựa khác đều SAI.

👉 **ĐÁP ÁN ĐÚNG: D**
- **Giải thích:**
  - `abab` = $b^0 (ab)^2 \in E_2$
  - `bab` = $b^1 (ab)^1 \in E_2$
  - `bb` = $b^2 (ab)^0 \in E_2$
  - Cả 3 chuỗi đều thuộc $E_2$. Do đó không có chuỗi nào "không thuộc $E_2$". Chọn D.

---

### Câu 18: Xét biểu thức $E_3 = (ab+b)^*$. Chuỗi nào KHÔNG thuộc $L$ nhưng thuộc ngôn ngữ được mô tả bởi $E_3$?
- A. "bbb"
- B. "abb"
- C. "bab"
- D. "bb"

👉 **ĐÁP ÁN ĐÚNG: B**
- **Giải thích:**
  - Chuỗi `abb` sinh được từ $E_3$ (bằng $ab + b$).
  - Nhưng trong ô-tô-mát: từ $\{q_0, q_1\}$ đọc $a \to \{q_1\}$, đọc $b \to \{q_2\}$, đọc tiếp $b \to \{q_0, q_1\}$ (không chứa trạng thái kết thúc $q_2$). Do đó `abb` **KHÔNG thuộc $L$**.

---

### Câu 19: Xét biểu thức $E_3 = (ab+b)^*$. Chuỗi nào thuộc $L$ nhưng KHÔNG thuộc ngôn ngữ được mô tả bởi $E_3$?
- A. "bbab"
- B. "ab"
- C. "b"
- D. Các chọn lựa khác đều SAI.

👉 **ĐÁP ÁN ĐÚNG: D**
- **Giải thích:**
  - `bbab` = $b + b + ab \in E_3$
  - `ab` = $ab \in E_3$
  - `b` = $b \in E_3$
  - Cả 3 đều thuộc $E_3$. Do đó chọn D.

---

### Câu 20: Xét biểu thức $E_3 = (ab+b)^*$. Chuỗi nào ĐỒNG THỜI KHÔNG thuộc $L$ và KHÔNG thuộc ngôn ngữ được mô tả bởi $E_3$?
- A. "bbab"
- B. "asb"
- C. "b"
- D. Các chọn lựa khác đều SAI.

👉 **ĐÁP ÁN ĐÚNG: B**
- **Giải thích:** Chuỗi `asb` chứa ký tự `s` lạ, không thuộc bảng chữ cái $\Sigma = \{a, b\}$, nên chắc chắn vừa không thuộc $L$ vừa không thuộc $E_3$.

---

### Câu 21: Xét biểu thức $E_4 = (a+b)^*(ab)$. Chuỗi nào KHÔNG thuộc $L$ nhưng thuộc ngôn ngữ được mô tả bởi $E_4$?
- A. "abb"
- B. "bbab"
- C. "abbaab"
- D. "abab"

👉 **ĐÁP ÁN ĐÚNG: C**
- **Giải thích:**
  - Chuỗi `abbaab` kết thúc bằng `ab` nên thuộc $E_4$.
  - Nhưng `abbaab` có chứa cụm **`aa`** $\implies$ chết ở trạng thái bẫy, không thuộc $L$.

---

### Câu 22: Xét biểu thức $E_4 = (a+b)^*(ab)$. Chuỗi nào thuộc $L$ nhưng KHÔNG thuộc ngôn ngữ được mô tả bởi $E_4$?
- A. "ab"
- B. "abab"
- C. "b"
- D. "bbab"

👉 **ĐÁP ÁN ĐÚNG: C**
- **Giải thích:** $E_4$ bắt buộc phải kết thúc bằng cụm `ab`. Chuỗi `b` thuộc $L$ nhưng kết thúc bằng `b` chứ không phải `ab`, nên không thuộc $E_4$.

---

### Câu 23: Nếu áp dụng đơn định hóa automata đang quan tâm thì DFA thu được có bao nhiêu trạng thái?
- A. 3
- B. 4
- C. 5
- D. 6

👉 **ĐÁP ÁN ĐÚNG: C (5 trạng thái)**
- **BẢNG ĐƠN ĐỊNH HÓA CHI TIẾT (SUBSET CONSTRUCTION):**
  - Trạng thái bắt đầu của DFA là $\varepsilon\text{-closure}(q_0) = \{q_0, q_1\}$ (đặt tên là **$S_0$**).

| Tên trạng thái DFA | Tập trạng thái NFA thành phần | Khi đọc ký tự $a$ | Khi đọc ký tự $b$ | Là trạng thái kết thúc? |
| :---: | :---: | :---: | :---: | :---: |
| **$S_0$** (Khởi đầu) | $\{q_0, q_1\}$ | $\{q_1\} = \mathbf{S_1}$ | $\{q_0, q_1, q_2\} = \mathbf{S_2}$ | Không |
| **$S_1$** | $\{q_1\}$ | $\emptyset = \mathbf{S_3}$ (Bẫy) | $\{q_2\} = \mathbf{S_4}$ | Không |
| **$S_2$** | $\{q_0, q_1, q_2\}$ | $\{q_1\} = \mathbf{S_1}$ | $\{q_0, q_1, q_2\} = \mathbf{S_2}$ | **CÓ** (chứa $q_2$) |
| **$S_3$** | $\emptyset$ (Trạng thái bẫy chết) | $\emptyset = \mathbf{S_3}$ | $\emptyset = \mathbf{S_3}$ | Không |
| **$S_4$** | $\{q_2\}$ | $\{q_1\} = \mathbf{S_1}$ | $\{q_0, q_1\} = \mathbf{S_0}$ | **CÓ** (chứa $q_2$) |

👉 Tổng cộng DFA gồm đúng **5 trạng thái**: $\{S_0, S_1, S_2, S_3, S_4\}$. Chọn **C**.
*(Lưu ý: Nếu một số tài liệu không vẽ trạng thái bẫy rỗng $S_3 = \emptyset$ thì có 4 trạng thái, nhưng theo chuẩn định nghĩa hàm chuyển toàn phần $\delta: Q \times \Sigma \to Q$ trong giáo trình IUH thì luôn tính cả trạng thái bẫy $\implies$ 5 trạng thái).*

---

### Câu 24: DFA tối giản tương đương có bao nhiêu trạng thái?
- A. 3
- B. 4
- C. 5
- D. 6

👉 **ĐÁP ÁN ĐÚNG: C (5 trạng thái)**
- **GIẢI THÍCH TỐI THIỂU HÓA:**
  - Ta chia làm 2 nhóm ban đầu:
    + Nhóm chấp nhận: $F = \{S_2, S_4\}$
    + Nhóm không chấp nhận: $NF = \{S_0, S_1, S_3\}$
  - Xét nhóm $F = \{S_2, S_4\}$:
    + Từ $S_2$, đọc $b \to S_2$ (thuộc $F$).
    + Từ $S_4$, đọc $b \to S_0$ (thuộc $NF$).
    $\implies$ $S_2$ và $S_4$ bị phân biệt bởi ký tự $b$, không thể gộp nhau!
  - Xét nhóm $NF = \{S_0, S_1, S_3\}$:
    + $S_3$ là bẫy chết (đọc gì cũng ở $S_3$).
    + Từ $S_0$ đọc $b \to S_2 \in F$.
    + Từ $S_1$ đọc $b \to S_4 \in F$, nhưng từ $S_1$ đọc $a \to S_3$, trong khi từ $S_0$ đọc $a \to S_1$.
    $\implies$ Cả 3 trạng thái $S_0, S_1, S_3$ đều phân biệt đôi một.
  👉 Cả 5 trạng thái đều không thể gộp được $\implies$ DFA tối giản vẫn có đúng **5 trạng thái**. Chọn **C**.

---

# PHẦN 3: 10 CÂU BIẾN THỂ KINH ĐIỂN CÙNG DẠNG

#### Câu B1: Nếu ô-tô-mát có thêm bước chuyển $\delta(q_1, a) = \{q_1\}$, chuỗi nào sau đây sẽ trở thành hợp lệ?
- A. `aa`
- B. `aab`
- C. `a`
- D. `ba`
👉 **Đáp án: B**
- **Giải thích:** Khi đó cho phép lặp chữ $a$ tại $q_1$, chuỗi `aab` đi từ $q_0 \xrightarrow{a} q_1 \xrightarrow{a} q_1 \xrightarrow{b} q_2$ (hợp lệ!).

#### Câu B2: Trong ô-tô-mát gốc của đề, $\varepsilon\text{-closure}(q_0)$ bằng:
- A. $\{q_0\}$
- B. $\{q_1\}$
- C. $\{q_0, q_1\}$
- D. $\{q_0, q_1, q_2\}$
👉 **Đáp án: C**
- **Giải thích:** Xuất phát từ $q_0$, đi theo các bước chuyển $\varepsilon$ ta đến được chính nó $q_0$ và $q_1$.

#### Câu B3: $\varepsilon\text{-closure}(q_1)$ và $\varepsilon\text{-closure}(q_2)$ lần lượt bằng:
- A. $\{q_1\}$ và $\{q_2\}$
- B. $\{q_1, q_2\}$ và $\{q_0\}$
- C. $\{q_1\}$ và $\{q_0, q_2\}$
- D. $\emptyset$ và $\emptyset$
👉 **Đáp án: A** (Từ $q_1$ và $q_2$ không có bước chuyển $\varepsilon$ nào).

#### Câu B4: Từ rỗng $\varepsilon$ có được ô-tô-mát gốc đoán nhận không?
- A. Có
- B. Không
👉 **Đáp án: B**
- **Giải thích:** $\varepsilon\text{-closure}(q_0) = \{q_0, q_1\}$ không chứa trạng thái kết thúc $q_2$, nên từ rỗng $\varepsilon$ không được đoán nhận.

#### Câu B5: Chuỗi ngắn nhất được ô-tô-mát gốc đoán nhận là:
- A. $\varepsilon$
- B. `a`
- C. `b`
- D. `ab`
👉 **Đáp án: C**
- **Giải thích:** $q_0 \xrightarrow{\varepsilon} q_1 \xrightarrow{b} q_2$, độ dài bằng 1.

#### Câu B6: Nếu trạng thái kết thúc đổi thành $F = \{q_1\}$, chuỗi nào sau đây được đoán nhận?
- A. $\varepsilon$
- B. `a`
- C. `ba`
- D. Tất cả các chuỗi trên
👉 **Đáp án: D**
- **Giải thích:** $q_0 \xrightarrow{\varepsilon} q_1$ (chấp nhận $\varepsilon$). $q_0 \xrightarrow{a} q_1$ (chấp nhận `a`). $q_0 \xrightarrow{b} q_0 \xrightarrow{a} q_1$ (chấp nhận `ba`).

#### Câu B7: Điều kiện cần để một NFA có thể tối thiểu hóa giảm số trạng thái là:
- A. Có ít nhất một trạng thái không đến được hoặc có 2 trạng thái tương đương
- B. Phải có bước chuyển $\varepsilon$
- C. Phải có nhiều hơn 1 trạng thái kết thúc
- D. Không bao giờ tối thiểu hóa được NFA
👉 **Đáp án: A**

#### Câu B8: Một NFA có $n$ trạng thái thì DFA tương đương theo thuật toán tập con có tối đa bao nhiêu trạng thái?
- A. $n$
- B. $n^2$
- C. $2^n$
- D. $n!$
👉 **Đáp án: C**
- **Giải thích:** Tập các trạng thái của DFA là tập lũy thừa $\mathcal{P}(Q)$, có tối đa $2^n$ trạng thái.

#### Câu B9: Ngôn ngữ được đoán nhận bởi ô-tô-mát trong bài tương đương với biểu thức chính quy nào dưới đây?
- A. $(b + ab(ab)^* b)^* (\varepsilon + a) b (ab)^*$
- B. $b^* (ab)^*$
- C. $(a+b)^* b$
- D. $(b + ab)^* b$
👉 **Đáp án: A**
- **Giải thích:** Theo định lý Arden trên đồ thị:
  + Nhánh quay về $q_0$ gồm: tự lặp $b$, hoặc đi $ab(ab)^* b$ (tức cụm `abb` ở giữa vẫn hợp lệ nếu phía sau còn đường về đích, như `abbb`, `abbab`).
  + Nhánh đi tới đích $q_2$ ở cuối là $(\varepsilon + a) b (ab)^*$ (chặn được chuỗi `abb` ở cuối vì sau `ab` không thể kết thúc bằng đúng 1 chữ `b`).
  + Lưu ý: **D (`(b + ab)* b`) là bẫy** vì nó sinh được chuỗi `abb`, trong khi `abb` không thuộc $L$!

#### Câu B10: Cho NFA không có $\varepsilon$-chuyển với $Q=\{A, B\}$, $\Sigma=\{0, 1\}$. Nếu $\delta(A, 0) = \{A, B\}$, đây là đặc điểm của:
- A. DFA
- B. NFA
- C. PDA
- D. Máy Turing
👉 **Đáp án: B** (Tại 1 trạng thái đọc 1 ký tự mà đi đến tập có nhiều hơn 1 trạng thái là đặc trưng của NFA).
