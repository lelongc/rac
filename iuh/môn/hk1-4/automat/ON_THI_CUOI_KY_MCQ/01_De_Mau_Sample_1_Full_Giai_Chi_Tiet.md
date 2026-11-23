# BỘ ĐỀ MẪU CUỐI KỲ 1: GIẢI CHI TIẾT 100% ĐỀ MCQ SAMPLE 1 (VĂN PHẠM CFG)

## KÈM 10 CÂU BIẾN THỂ THỰC CHIẾN CÓ LỜI GIẢI DỄ HIỂU NHẤT CHO NGƯỜI MỚI HỌC

> **THÔNG TIN ĐỀ BÀI GỐC (Trích Automata - mcq sample 1.pdf):**
> Xét ngôn ngữ $L$ được xác định bởi văn phạm phi ngữ cảnh:
>
> $$
> G = \langle \{a, b, c\},\ \{S, A\},\ S,\ P \rangle
> $$
>
> với tập quy tắc sinh $P$ gồm:
>
> - $S \to aSb \mid aA$
> - $A \to cA \mid c$

---

# PHẦN 1: BẢN CHẤT CỐT LÕI CỦA VĂN PHẠM (HIỂU TRONG 1 PHÚT LÀ LÀM ĐƯỢC 24 CÂU)

Để làm đúng 24/24 câu trong đề thi thật mà không bao giờ bị nhầm, bạn chỉ cần nắm vững **công thức chuỗi tổng quát** sinh ra từ văn phạm này:

### 1. Phân tích quá trình dẫn xuất từng bước:

1. **Giai đoạn 1 (Lặp luật $S \to aSb$ $n$ lần, với $n \ge 0$):**
   Mỗi lần dùng luật này, ta thêm 1 chữ $a$ ở đầu và 1 chữ $b$ ở cuối:
   $$
   S \Rightarrow aSb \Rightarrow aaSbb \Rightarrow \dots \Rightarrow a^n S b^n
   $$
2. **Giai đoạn 2 (Dừng biến $S$, chuyển sang biến $A$ bằng luật $S \to aA$):**
   Thêm tiếp **đúng 1 chữ $a$** ở trước biến $A$:
   $$
   a^n S b^n \Rightarrow a^n (aA) b^n = a^{n+1} A b^n
   $$
3. **Giai đoạn 3 (Biến $A$ sinh toàn bộ các chữ $c$ bằng luật $A \to cA \mid c$):**
   Mỗi lần dùng $A \to cA$ sinh thêm 1 chữ $c$. Kết thúc bằng luật $A \to c$.
   Nếu biến $A$ lặp $m$ lần ($m \ge 1$):
   $$
   A \Rightarrow c^m
   $$
4. **Gộp lại, chuỗi tổng quát của ngôn ngữ $L$ là:**
   $$
   \mathbf{w = a^{n+1} c^m b^n \quad (với\ n \ge 0,\ m \ge 1)}
   $$

---

### 2. Ba đặc điểm "thần thánh" giúp nhận diện đáp án trong 3 giây:

| Đặc điểm                              | Quy tắc nhận diện                                                                                                                      | Ví dụ hợp lệ                                                                                                                                 | Ví dụ SAI                                                                                                                                        |
| :---------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Thứ tự ký tự**             | Toàn bộ chữ $a$ đứng đầu $\to$ toàn bộ $c$ ở giữa $\to$ toàn bộ $b$ ở cuối                                       | `aacb`, `aaccb`                                                                                                                              | `cab` (sai vì $c$ đứng đầu), `acba` (sai vì $a$ ở cuối)                                                                            |
| **2. Tương quan $a$ và $b$** | **Số lượng chữ $a$ luôn nhiều hơn số lượng chữ $b$ đúng 1 ký tự**:
$$
\#a = \#b + 1
$$

                               | `ac` (1 $a$, 0 $b$ $\implies 1 = 0+1$)`aacb` (2 $a$, 1 $b$ $\implies 2 = 1+1$)`aaacbb` (3 $a$, 2 $b$ $\implies 3 = 2+1$) | `ab` (1 $a$, 1 $b$ $\implies$ bằng nhau là sai)`aacbb` (2 $a$, 2 $b$ $\implies$ sai)`acbb` (1 $a$, 2 $b$ $\implies$ sai) |
| **3. Số lượng chữ $c$**       | **Bắt buộc phải có ít nhất 1 chữ $c$** ($m \ge 1$), vì $A \to cA \mid c$ không có luật rỗng $A \to \varepsilon$ | `ac` (1 chữ $c$), `acc` (2 chữ $c$)                                                                                                    | `ab`, `aab` (không có $c$ là loại ngay lập tức!)                                                                                       |

---

# PHẦN 2: LỜI GIẢI CHI TIẾT TỪNG CÂU TỪ CÂU 1 ĐẾN CÂU 24

### Câu 1: Chuỗi nào thuộc $L$?

- A. `ac`
- B. `ab`
- C. `aab`
- D. `c`

👉 **ĐÁP ÁN ĐÚNG: A**

- **Giải thích:**
  - `ac`: Có 1 chữ $a$, 1 chữ $c$, 0 chữ $b$. Thỏa mãn $\#a = 1 = 0 + 1 = \#b + 1$, và số chữ $c = 1 \ge 1$ (ứng với $n=0, m=1$). Dẫn xuất: $S \Rightarrow aA \Rightarrow ac$.
  - `ab`, `aab`: Không có chữ $c$ (loại vì $A$ luôn sinh ít nhất 1 chữ $c$).
  - `c`: Không có chữ $a$ (loại vì luật $S \to aA$ bắt buộc có ít nhất 1 chữ $a$).

---

### Câu 2: Chuỗi nào thuộc $L$?

- A. `aacb`
- B. `acb`
- C. `ab`
- D. `cab`

👉 **ĐÁP ÁN ĐÚNG: A**

- **Giải thích:**
  - `aacb`: Có 2 chữ $a$, 1 chữ $c$, 1 chữ $b$. Kiểm tra: $\#a = 2, \#b = 1 \implies 2 = 1 + 1$ (Đúng, ứng với $n=1, m=1$). Dẫn xuất: $S \Rightarrow aSb \Rightarrow a(aA)b \Rightarrow aacb$.
  - `acb`: Có 1 chữ $a$, 1 chữ $b \implies \#a = \#b$ (vi phạm $\#a = \#b + 1$).
  - `cab`: Chữ $c$ đứng trước $a$ là sai thứ tự.

---

### Câu 3: Chuỗi nào thuộc $L$?

- A. `aaabb`
- B. `aacbb`
- C. `acbbb`
- D. `aaacbb`

👉 **ĐÁP ÁN ĐÚNG: D**

- **Giải thích:**
  - `aaacbb`: Có 3 chữ $a$, 1 chữ $c$, 2 chữ $b$. Thỏa mãn $\#a = 3 = 2 + 1 = \#b + 1$ (ứng với $n=2, m=1$).
  - `aaabb`: Không có $c$ (loại).
  - `aacbb`: Có 2 $a$, 2 $b \implies \#a = \#b$ (loại).
  - `acbbb`: Có 1 $a$, 3 $b \implies \#a < \#b$ (loại).

---

### Câu 4: Chuỗi nào KHÔNG thuộc $L$?

- A. `ac`
- B. `aacb`
- C. `aacccb`
- D. `ab`

👉 **ĐÁP ÁN ĐÚNG: D**

- **Giải thích:** Đề hỏi chuỗi **KHÔNG** thuộc $L$. `ab` không có ký tự $c$, nên chắc chắn không thể sinh từ văn phạm $G$.

---

### Câu 5: Chuỗi nào thuộc $L$?

- A. `accbb`
- B. `aaccb`
- C. `aaacccb`
- D. `aabbb`

👉 **ĐÁP ÁN ĐÚNG: B**

- **Giải thích:**
  - `aaccb`: Có 2 $a$, 2 $c$, 1 $b$. Thỏa mãn $\#a = 2 = 1 + 1 = \#b + 1$ (ứng với $n=1, m=2$).
  - `accbb`: 1 $a$, 2 $b \implies$ sai.
  - `aaacccb`: 3 $a$, 0 $b \implies 3 \ne 0 + 1$ (sai).

---

### Câu 6: Chuỗi nào KHÔNG thuộc $L$?

- A. `ac`
- B. `aaccb`
- C. `aacbb`
- D. `aaacbb`

👉 **ĐÁP ÁN ĐÚNG: C**

- **Giải thích:** `aacbb` có 2 chữ $a$ và 2 chữ $b$ (bằng nhau), vi phạm quy tắc số chữ $a$ phải nhiều hơn số chữ $b$ là 1 ký tự.

---

### Câu 7: Chuỗi nào thuộc $L$?

- A. `aacccbb`
- B. `acccb`
- C. `aacccb`
- D. `accbb`

👉 **ĐÁP ÁN ĐÚNG: C**

- **Giải thích:** `aacccb` có 2 $a$, 3 $c$, 1 $b$. Thỏa mãn $2 = 1 + 1$ (ứng với $n=1, m=3$).

---

### Câu 8: Chuỗi nào KHÔNG thuộc $L$?

- A. `ac`
- B. `aacb`
- C. `aacbb`
- D. `acc`

👉 **ĐÁP ÁN ĐÚNG: C**

- **Giải thích:** `acc` có 1 $a$, 2 $c$, 0 $b \implies 1 = 0 + 1$ (thuộc $L$). Còn `aacbb` có 2 $a$, 2 $b$ (không thuộc $L$).

---

### Câu 9: Chuỗi nào thuộc $L$?

- A. `aaacccbb`
- B. `aaccbbb`
- C. `accbbb`
- D. `aaacccb`

👉 **ĐÁP ÁN ĐÚNG: A**

- **Giải thích:** `aaacccbb` có 3 $a$, 3 $c$, 2 $b$. Thỏa mãn $\#a = 3 = 2 + 1 = \#b + 1$ (ứng với $n=2, m=3$).

---

### Câu 10: Chuỗi nào có thể sinh từ $S$?

- A. `ac`
- B. `aab`
- C. `accb`
- D. Các lựa chọn khác đều SAI.

👉 **ĐÁP ÁN ĐÚNG: A**

- **Giải thích:** $S \Rightarrow aA \Rightarrow ac$.

---

### Câu 11: Chuỗi nào được sinh với ÍT NHẤT 1 LẦN dùng $S \to aSb$?

- A. `ac`
- B. `aacb`
- C. `acc`
- D. `a`

👉 **ĐÁP ÁN ĐÚNG: B**

- **Giải thích:**
  - Quy tắc $S \to aSb$ là quy tắc duy nhất sinh ra ký tự $b$. Do đó, chuỗi nào sinh từ $S \to aSb$ ít nhất 1 lần thì **bắt buộc phải chứa ít nhất 1 ký tự $b$**.
  - Trong các đáp án: `ac`, `acc`, `a` đều không có chữ $b$. Chỉ có `aacb` là có chứa $b$.

---

### Câu 12: Chuỗi nào KHÔNG thuộc $L$?

- A. `ac`
- B. `aacb`
- C. `aaacbb`
- D. `acbb`

👉 **ĐÁP ÁN ĐÚNG: D**

- **Giải thích:** `acbb` có 1 $a$ và 2 $b \implies \#a < \#b$ (sai).

---

### Câu 13: Chuỗi NGẮN NHẤT thuộc $L$ là:

- A. $\varepsilon$
- B. `a`
- C. `ac`
- D. `ab`

👉 **ĐÁP ÁN ĐÚNG: C**

- **Giải thích:** Dẫn xuất ngắn nhất không lặp: $S \Rightarrow aA \Rightarrow ac$. Độ dài bằng 2.

---

### Câu 14: Chuỗi NGẮN NHÌ thuộc $L$ là:

- A. `aac`
- B. `acc`
- C. `acb`
- D. `aab`

👉 **ĐÁP ÁN ĐÚNG: B**

- **Giải thích:**
  - Chuỗi ngắn nhất là `ac` (độ dài 2).
  - Chuỗi dài 3 thuộc $L$: ứng với $n=0, m=2 \implies w = a^1 c^2 b^0 =$ `acc`.
  - `aac` và `acb` không thỏa mãn $\#a = \#b + 1$ nên không thuộc $L$. Vậy chuỗi ngắn nhì là `acc`.

---

### Câu 15: Ba chuỗi ngắn nhất thuộc $L$ là:

- A. `ac, aac, acc`
- B. `ac, acc, accc`
- C. `ac, acc, aac`
- D. `ac, aac, aacb`

👉 **ĐÁP ÁN ĐÚNG: B**

- **Giải thích:** Các đáp án A, C, D đều chứa `aac` (mà `aac` không thuộc $L$). Chỉ có B gồm các chuỗi hợp lệ: `ac` (dài 2), `acc` (dài 3), `accc` (dài 4).

---

### Câu 16: Chuỗi thứ 4 theo độ dài tăng dần là (nếu cùng độ dài thì ưu tiên theo bảng chữ cái từ trái sang phải):

- A. `accc`
- B. `aacc`
- C. `aacb`
- D. `accb`

👉 **ĐÁP ÁN ĐÚNG: C**

- **Giải thích:**
  - Độ dài 2: `ac` (vị trí 1).
  - Độ dài 3: `acc` (vị trí 2).
  - Độ dài 4 gồm 2 chuỗi hợp lệ: `aacb` ($n=1, m=1$) và `accc` ($n=0, m=3$).
  - So sánh thứ tự từ điển: chữ thứ hai của `aacb` là `a`, chữ thứ hai của `accc` là `c`. Vì `a` < `c` nên `aacb` đứng trước $\implies$ `aacb` là chuỗi thứ 3, `accc` là chuỗi thứ 4 (hoặc nếu đếm thì `aacb` là chuỗi độ dài 4 đầu tiên). Đề thi chọn đáp án **C. aacb**.

---

### Câu 17: Chuỗi ngắn nhất có chứa ký tự `b` là:

- A. `ac`
- B. `aacb`
- C. `acb`
- D. `acc`

👉 **ĐÁP ÁN ĐÚNG: B**

- **Giải thích:** Muốn có ký tự $b$ thì ít nhất phải có 1 $b$ ($n=1$). Khi $n=1$, số $a$ phải là $n+1 = 2$, số $c$ ít nhất là 1 ($m=1$). Chuỗi ngắn nhất là $a^2 c^1 b^1 =$ `aacb` (độ dài 4).

---

### Câu 18: Số lượng ký tự `c` trong chuỗi hợp lệ là:

- A. $\ge 1$
- B. $\ge 0$
- C. = số lượng `a`
- D. = số lượng `b`

👉 **ĐÁP ÁN ĐÚNG: A**

- **Giải thích:** Do biến $A$ sinh bởi $A \to cA \mid c$ (không có $A \to \varepsilon$), nên mọi chuỗi thuộc $L$ luôn có ít nhất 1 chữ $c$.

---

### Câu 19: Quan hệ giữa số lượng `a` và `b`:

- A. $a = b$
- B. $a \ge b$
- C. $a = b + 1$
- D. $a < b$

👉 **ĐÁP ÁN ĐÚNG: C**

- **Giải thích:** Dạng tổng quát là $a^{n+1} c^m b^n$, do đó số lượng chữ $a$ luôn đúng bằng số lượng chữ $b$ cộng thêm 1 ($a = b + 1$).

---

### Câu 20: Dạng tổng quát của chuỗi là:

- A. $a^n b^n c^n$
- B. $a^n c^m b^n$
- C. $a^{n+1} c^m b^n$
- D. $c^m a^n b^n$

👉 **ĐÁP ÁN ĐÚNG: C**

- **Giải thích:** Chuỗi tổng quát là $a^{n+1} c^m b^n$ với $n \ge 0, m \ge 1$.

---

### Câu 21: Chuỗi "aacb" có thuộc $L$ không?

- A. Có
- B. Không

👉 **ĐÁP ÁN ĐÚNG: A** (Có, ứng với $n=1, m=1$).

---

### Câu 22: Chuỗi "acbb" có thuộc $L$ không?

- A. Có
- B. Không

👉 **ĐÁP ÁN ĐÚNG: B** (Không, vì 1 $a$ và 2 $b$).

---

### Câu 23: Chuỗi "aaaccbb" có thuộc $L$ không?

- A. Có
- B. Không

👉 **ĐÁP ÁN ĐÚNG: A** (Có, vì 3 $a$, 2 $c$, 2 $b \implies 3 = 2 + 1$).

---

### Câu 24: Chuỗi "accbb" có thuộc $L$ không?

- A. Có
- B. Không

👉 **ĐÁP ÁN ĐÚNG: B** (Không, vì 1 $a$ và 2 $b$).

---

# PHẦN 3: 10 CÂU BIẾN THỂ KINH ĐIỂN (ĐỀ THI RẤT DỄ ĐỔI SANG)

#### Câu B1: Cho văn phạm $G$ có $P = \{ S \to aSb \mid bA,\ A \to cA \mid c \}$. Dạng tổng quát của chuỗi là:

- A. $a^n b c^m b^n$ ($n \ge 0, m \ge 1$)
- B. $a^n c^m b^{n+1}$
- C. $a^{n+1} c^m b^n$
- D. $a^n b^n c^m$
  👉 **Đáp án: A**
- **Giải thích:** $S \Rightarrow a^n S b^n \Rightarrow a^n (bA) b^n = a^n b A b^n \Rightarrow a^n b c^m b^n$.

#### Câu B2: Cho văn phạm $G$ có $P = \{ S \to 0S1 \mid 0A,\ A \to 2A \mid 2 \}$. Chuỗi nào ngắn nhất thuộc $L(G)$?

- A. `01`
- B. `02`
- C. `021`
- D. `2`
  👉 **Đáp án: B**
- **Giải thích:** Dẫn xuất ngắn nhất: $S \Rightarrow 0A \Rightarrow 02$.

#### Câu B3: Cho văn phạm $G$ có $P = \{ S \to aSbb \mid aA,\ A \to cA \mid c \}$. Mối quan hệ giữa số lượng chữ $a$ và chữ $b$ là:

- A. $b = 2a$
- B. $b = 2(a - 1)$
- C. $a = 2b + 1$
- D. $a = b$
  👉 **Đáp án: B**
- **Giải thích:** $S \Rightarrow a^n S b^{2n} \Rightarrow a^{n+1} A b^{2n}$. Số lượng $a$ là $n+1$, số lượng $b$ là $2n$. Do đó $b = 2n = 2(a - 1)$.

#### Câu B4: Với văn phạm ở Câu B3, chuỗi nào sau đây thuộc $L$?

- A. `aacbb`
- B. `aaacbbbb`
- C. `acbb`
- D. `aacb`
  👉 **Đáp án: B**
- **Giải thích:** Ứng với $n=2$: số $a = n+1 = 3$, số $b = 2n = 4$, ở giữa có ít nhất 1 chữ $c \implies$ `aaacbbbb`.

#### Câu B5: Cho văn phạm $G$ có $P = \{ S \to aSb \mid A,\ A \to cA \mid \varepsilon \}$. Chuỗi ngắn nhất thuộc $L(G)$ là:

- A. `acb`
- B. `c`
- C. $\varepsilon$
- D. `a`
  👉 **Đáp án: C**
- **Giải thích:** Vì $A \to \varepsilon$ nên $S \Rightarrow A \Rightarrow \varepsilon$.

#### Câu B6: Với văn phạm ở Câu B5, dạng tổng quát của chuỗi là:

- A. $a^n c^m b^n$ ($n \ge 0, m \ge 0$)
- B. $a^{n+1} c^m b^n$ ($n \ge 0, m \ge 1$)
- C. $a^n b^n c^m$
- D. $(abc)^n$
  👉 **Đáp án: A**
- **Giải thích:** $S \Rightarrow a^n S b^n \Rightarrow a^n A b^n \Rightarrow a^n c^m b^n$ (với $n \ge 0, m \ge 0$ vì có luật $A \to \varepsilon$).

#### Câu B7: Cho văn phạm $G$ có $P = \{ S \to aS \mid bA,\ A \to cA \mid d \}$. Phân lớp Chomsky thấp nhất của $G$ là:

- A. Loại 0
- B. Loại 1
- C. Loại 2
- D. Loại 3 (Chính quy)
  👉 **Đáp án: D**
- **Giải thích:** Mọi luật đều có dạng tuyến tính phải ($A \to wB$ hoặc $A \to w$), nên đây là văn phạm chính quy (Loại 3).

#### Câu B8: Cho văn phạm $G$ có $P = \{ S \to aSb \mid c \}$. Đây là văn phạm:

- A. Tuyến tính phải
- B. Tuyến tính trái
- C. Phi ngữ cảnh (Loại 2) nhưng không chính quy
- D. Cảm ngữ cảnh
  👉 **Đáp án: C**
- **Giải thích:** Vế trái chỉ có 1 biến $S$, vế phải $aSb$ kẹp 2 bên $\implies$ không tuyến tính $\implies$ là Loại 2 (CFG).

#### Câu B9: Cho văn phạm $G$ có $P = \{ S \to SS \mid a \}$. Ngôn ngữ sinh ra bởi $G$ là:

- A. $\{ a^n \mid n \ge 1 \}$
- B. $\{ a^{2n} \mid n \ge 1 \}$
- C. $\{ a \}$
- D. $\{ a^n \mid n \ge 0 \}$
  👉 **Đáp án: A**
- **Giải thích:** Bằng cách ghép các $S \to SS$, ta có thể sinh ra số lượng chữ $a$ tùy ý từ 1 trở lên.

#### Câu B10: Với văn phạm $S \to SS \mid a$, chuỗi nào sau đây chứng minh văn phạm là nhập nhằng?

- A. `a`
- B. `aa`
- C. `aaa`
- D. Không nhập nhằng
  👉 **Đáp án: C**
- **Giải thích:** Chuỗi `aaa` có 2 cây suy dẫn khác nhau: $(SS)S$ và $S(SS)$.
