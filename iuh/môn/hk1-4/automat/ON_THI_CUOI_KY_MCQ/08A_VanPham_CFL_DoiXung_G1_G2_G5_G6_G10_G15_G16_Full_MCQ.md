# BỘ ĐỀ ÔN TẬP VĂN PHẠM PHẦN 1 (CHÙM CFG ĐỐI XỨNG): $G_1, G_2, G_5, G_6, G_{10}, G_{15}, G_{16}$
## MỖI VĂN PHẠM FULL 24 CÂU CHUẨN ĐỀ MẪU SAMPLE 1 + 2 CÂU CHOMSKY/PDA TỪ WORD

> **QUY TẮC GỘP BÀI TỰA NHAU (KHÔNG BỎ SÓT KIẾN THỨC):**
> Trong 19 văn phạm của [OnTapAutomata.docx](file:///d:/folder/rac/iuh/môn/hk1-4/automat/ON_THI_CUOI_KY_MCQ/OnTapAutomata.docx):
> - **$G_1$** ($\{0^n 1^n \mid n \ge 0\}$) đại diện luôn cho **$G_9$ và $G_{12}$** ($\{a^n b^n \mid n \ge 1\}$ — chỉ đổi ký tự và bỏ $\varepsilon$).
> - **$G_{10}$** ($\{a^n c b^{2n} \mid n \ge 0\}$) đại diện luôn cho **$G_{11}$** ($\{a^{2n} c b^n \mid n \ge 0\}$ — chỉ đảo vai trò $a \leftrightarrow b$).
> - File này gồm **7 văn phạm CFG độc đáo**, mỗi văn phạm có **đầy đủ 26 câu hỏi trắc nghiệm** (24 câu chuẩn Sample 1 + 2 câu lý thuyết Chomsky/PDA từ Word) = **182 câu có lời giải chi tiết 100%**.

---

## VĂN PHẠM 1 ($G_1$): NGÔN NGỮ ĐỐI XỨNG CƠ BẢN $\{0^n 1^n \mid n \ge 0\}$

> **LƯU Ý GỘP DẠNG TỰA NHAU:** Bộ câu hỏi này đại diện luôn cho **$G_9 = \{S \to aSb \mid ab\}$** và **$G_{12} = \{S \to aSb \mid ab\}$** (2 văn phạm này giống hệt nhau 100%, chỉ đổi ký tự `0` $\to$ `a`, `1` $\to$ `b` và **không** chứa chuỗi rỗng $\varepsilon$ do $n \ge 1$).

> **ĐỀ BÀI GỐC ($G_1$):**
> $$
> G_1 = \langle \{0, 1\},\ \{S\},\ S,\ \{S \to 0S1 \mid \varepsilon\} \rangle
> $$
> Với các quy tắc sinh: $S \to 0S1$ và $S \to \varepsilon$

### Bản chất cốt lõi & Quy tắc vàng nhận diện trong 3 giây
1. **Dẫn xuất tổng quát:** Lặp luật $S \to 0S1$ đúng $n$ lần ($n \ge 0$) rồi dừng bằng $S \to \varepsilon$:
   $$S \Rightarrow 0S1 \Rightarrow 00S11 \Rightarrow \dots \Rightarrow 0^n S 1^n \Rightarrow 0^n 1^n$$
2. **Ba quy tắc vàng 3 giây:**
   - **Thứ tự:** Toàn bộ số `0` đứng trước, toàn bộ số `1` đứng sau (tuyệt đối không có `1` đứng trước `0`).
   - **Số lượng:** Số lượng chữ `0` BẰNG CHÍNH XÁC số lượng chữ `1` ($\#0 = \#1$).
   - **Chuỗi rỗng $\varepsilon$:** Có thuộc ngôn ngữ (ứng với $n=0$, khi dùng ngay $S \to \varepsilon$). *(Khác với $G_9, G_{12}$ không có $\varepsilon$)*.

### Bộ 24 câu trắc nghiệm chuẩn Đề Mẫu Sample 1 (+ 2 câu lý thuyết Word)

**Câu 1.** Xét ngôn ngữ $L$ sinh bởi $G_1$. Chuỗi nào sau đây **thuộc** $L$?
- A. `01`
- B. `001`
- C. `011`
- D. `10`
👉 **Đáp án đúng: A**
- **Giải thích:** `01` có 1 số `0` đứng trước 1 số `1` ($n=1$). `001` và `011` lệch số lượng, `10` sai thứ tự.

**Câu 2.** Xét ngôn ngữ $L$ sinh bởi $G_1$. Chuỗi nào sau đây **thuộc** $L$?
- A. `001`
- B. `0011`
- C. `1010`
- D. `0101`
👉 **Đáp án đúng: B**
- **Giải thích:** `0011` = $0^2 1^2$ ($n=2$). `0101` và `1010` có `1` đứng trước `0` nên sai.

**Câu 3.** Xét ngôn ngữ $L$ sinh bởi $G_1$. Chuỗi nào sau đây **thuộc** $L$?
- A. `00011`
- B. `00111`
- C. `000111`
- D. `111000`
👉 **Đáp án đúng: C**
- **Giải thích:** `000111` = $0^3 1^3$ ($n=3$).

**Câu 4.** Xét ngôn ngữ $L$ sinh bởi $G_1$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. $\varepsilon$
- B. `01`
- C. `0011`
- D. `001`
👉 **Đáp án đúng: D**
- **Giải thích:** `001` có 2 số `0` nhưng chỉ 1 số `1` ($2 \ne 1$) nên KHÔNG thuộc $L$.

**Câu 5.** Xét ngôn ngữ $L$ sinh bởi $G_1$. Chuỗi nào sau đây **thuộc** $L$?
- A. `0001111`
- B. `00001111`
- C. `00110011`
- D. `0000111`
👉 **Đáp án đúng: B**
- **Giải thích:** `00001111` = $0^4 1^4$ ($n=4$).

**Câu 6.** Xét ngôn ngữ $L$ sinh bởi $G_1$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `01`
- B. `0011`
- C. `000111`
- D. `0101`
👉 **Đáp án đúng: D**
- **Giải thích:** `0101` có chữ `1` đứng xen trước chữ `0` nên KHÔNG thuộc $L$.

**Câu 7.** Xét ngôn ngữ $L$ sinh bởi $G_1$. Chuỗi nào sau đây **thuộc** $L$?
- A. $\varepsilon$
- B. `000`
- C. `111`
- D. `0110`
👉 **Đáp án đúng: A**
- **Giải thích:** Khi $n=0$, áp dụng ngay $S \to \varepsilon$ thu được chuỗi rỗng $\varepsilon$.

**Câu 8.** Xét ngôn ngữ $L$ sinh bởi $G_1$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. $\varepsilon$
- B. `01`
- C. `0011`
- D. `10`
👉 **Đáp án đúng: D**
- **Giải thích:** `10` sai thứ tự `1` đứng trước `0`.

**Câu 9.** Xét ngôn ngữ $L$ sinh bởi $G_1$. Chuỗi nào sau đây **thuộc** $L$?
- A. `000001111`
- B. `0000011111`
- C. `000011111`
- D. `010101`
👉 **Đáp án đúng: B**
- **Giải thích:** `0000011111` = $0^5 1^5$ ($n=5$).

**Câu 12.** Xét ngôn ngữ $L$ sinh bởi $G_1$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. $\varepsilon$
- B. `0011`
- C. `000111`
- D. `0000`
👉 **Đáp án đúng: D**
- **Giải thích:** `0000` có 4 số `0` mà 0 số `1` ($4 \ne 0$).

**Câu 10.** Chuỗi nào có thể sinh từ ký hiệu bắt đầu $S$ của $G_1$?
- A. `0011`
- B. `010`
- C. `1100`
- D. `011`
👉 **Đáp án đúng: A**
- **Giải thích:** $S \Rightarrow 0S1 \Rightarrow 00S11 \Rightarrow 0011$.

**Câu 11.** Chuỗi nào được sinh với **ÍT NHẤT 1 LẦN** dùng luật $S \to 0S1$?
- A. $\varepsilon$
- B. `01`
- C. `0`
- D. `1`
👉 **Đáp án đúng: B**
- **Giải thích:** Dùng ít nhất 1 lần luật $S \to 0S1$ thì chuỗi sinh ra phải có ít nhất 1 cặp `0`...`1`, nên ngắn nhất là `01`. Chuỗi rỗng $\varepsilon$ chỉ dùng $S \to \varepsilon$ (0 lần $S \to 0S1$).

**Câu 13.** Chuỗi **NGẮN NHẤT** thuộc $L($G_1$)$ là:
- A. $\varepsilon$
- B. ``01``
- C. ``0``
- D. ``1``
👉 **Đáp án đúng: A**
- **Giải thích:** Do có luật $S \to \varepsilon$, chuỗi ngắn nhất là $\varepsilon$ (độ dài 0).

**Câu 14.** Chuỗi **NGẮN NHÌ** thuộc $L($G_1$)$ (nếu cùng độ dài thì ưu tiên thứ tự từ điển tăng dần) là:
- A. ``0``
- B. ``01``
- C. ``1``
- D. ``0011``
👉 **Đáp án đúng: B**
- **Giải thích:** Sau $\varepsilon$ (dài 0), chuỗi ngắn nhì là `01` (dài 2, ứng với $n=1$).

**Câu 15.** Ba chuỗi ngắn nhất thuộc $L($G_1$)$ (xếp theo độ dài và thứ tự từ điển tăng dần) là:
- A. $\varepsilon$, 0, 01
- B. $\varepsilon$, 01, 0011
- C. 01, 0011, 000111
- D. $\varepsilon$, 01, 10
👉 **Đáp án đúng: B**
- **Giải thích:** Ứng với $n=0, 1, 2$ ta lần lượt có: $\varepsilon$, `01`, `0011`.

**Câu 16.** Chuỗi **thứ 4** theo độ dài tăng dần của $L($G_1$)$ (nếu cùng độ dài ưu tiên thứ tự từ điển từ trái sang phải) là:
- A. ``000111``
- B. ``0011``
- C. ``0101``
- D. ``00011``
👉 **Đáp án đúng: A**
- **Giải thích:** Các chuỗi theo độ dài tăng dần: (1) $\varepsilon$, (2) `01`, (3) `0011`, (4) `000111` ($n=3$).

**Câu 17.** Chuỗi ngắn nhất thuộc $L($G_1$)$ thỏa điều kiện **có chứa ít nhất 1 ký tự `1`** là:
- A. ``1``
- B. ``01``
- C. ``0011``
- D. ``10``
👉 **Đáp án đúng: B**
- **Giải thích:** Chuỗi ngắn nhất có chứa `1` là `01` (ứng với $n=1$, độ dài 2).

**Câu 18.** Độ dài của mọi chuỗi hợp lệ trong $L(G_1)$ luôn có tính chất nào?
- A. Luôn là số chẵn ($0, 2, 4, 6, \dots$)
- B. Luôn là số lẻ
- C. Luôn $\ge 2$
- D. Chia hết cho 3
👉 **Đáp án đúng: A**
- **Giải thích:** Chuỗi $0^n 1^n$ có độ dài $2n$, luôn là số chẵn (kể cả 0).

**Câu 19.** Quan hệ giữa số lượng ký tự `0` và `1` trong chuỗi thuộc $L(G_1)$ là:
- A. $\#0 = \#1 + 1$
- B. $\#0 = 2 \times \#1$
- C. $\#0 = \#1$
- D. $\#0 \ge \#1$
👉 **Đáp án đúng: C**
- **Giải thích:** Mỗi lần mở rộng thêm 1 chữ `0` ở đầu luôn đi kèm 1 chữ `1` ở cuối nên $\#0 = \#1$.

**Câu 20.** Dạng tổng quát của ngôn ngữ $L(G_1)$ là:
- A. $\{0^n 1^n \mid n \ge 1\}$
- B. $\{0^n 1^n \mid n \ge 0\}$
- C. $\{0^n 1^m \mid n, m \ge 0\}$
- D. $(01)^*$
👉 **Đáp án đúng: B**
- **Giải thích:** Vì có luật $S \to \varepsilon$ nên $n$ bắt đầu từ $0$: $\{0^n 1^n \mid n \ge 0\}$.

**Câu 21.** Chuỗi `000111` có thuộc $L($G_1$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: A**
- **Giải thích:** Đúng, ứng với $n=3$ ($S \Rightarrow^3 000S111 \Rightarrow 000111$).

**Câu 22.** Chuỗi `00111` có thuộc $L($G_1$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: B**
- **Giải thích:** Sai, có 2 số `0` nhưng 3 số `1`.

**Câu 23.** Chuỗi $\varepsilon$ có thuộc $L($G_1$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: A**
- **Giải thích:** Đúng, ứng với $n=0$ ($S \Rightarrow \varepsilon$).

**Câu 24.** Chuỗi `0110` có thuộc $L($G_1$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: B**
- **Giải thích:** Sai, `1` đứng trước `0` và không theo mẫu $0^n 1^n$.

**Câu 25.** (Câu hỏi Word) Ngôn ngữ sinh bởi $G_1$ thuộc loại mấy theo phân loại Chomsky?
- A. Loại 3 (Chính quy)
- B. Loại 2 (Phi ngữ cảnh - CFG)
- C. Loại 1 (Cảm ngữ cảnh)
- D. Loại 0
👉 **Đáp án đúng: B**
- **Giải thích:** $G_1$ là văn phạm phi ngữ cảnh kinh điển (Loại 2), không phải chính quy vì DFA hữu hạn không đếm được $n$ tùy ý.

**Câu 26.** (Câu hỏi Word) Loại máy tối thiểu cần dùng để đoán nhận $L(G_1)$ là:
- A. `DFA`
- B. `NFA`
- C. Otomat đẩy xuống (PDA)
- D. Chỉ Máy Turing mới giải được
👉 **Đáp án đúng: C**
- **Giải thích:** Ngôn ngữ phi ngữ cảnh (Loại 2) được đoán nhận bởi Otomat đẩy xuống (PDA).

---

## VĂN PHẠM 2 ($G_2$): DẠNG LỆCH ĐUÔI $\{a^n b^{n+1} \mid n \ge 0\}$

> **ĐỀ BÀI GỐC ($G_2$):**
> $$
> G_2 = \langle \{a, b\},\ \{S, A\},\ S,\ \{S \to Ab,\ A \to aAb \mid \varepsilon\} \rangle
> $$
> Với các quy tắc sinh: $S \to Ab$, $A \to aAb \mid \varepsilon$

### Bản chất cốt lõi & Quy tắc vàng nhận diện trong 3 giây
1. **Dẫn xuất tổng quát:**
   - Từ $S$ luôn rẽ qua $S \to Ab$ (cộng sẵn **1 chữ `b`** ở cuối).
   - Biến $A$ lặp $n$ lần ($n \ge 0$) luật $A \to aAb$ rồi dừng bằng $A \to \varepsilon$: $A \Rightarrow a^n b^n$.
   - Ghép lại: $\mathbf{w = a^n b^{n+1}\ (n \ge 0)}$.
2. **Ba quy tắc vàng 3 giây:**
   - **Thứ tự:** Toàn bộ `a` đứng đầu, toàn bộ `b` đứng sau.
   - **Quan hệ số lượng:** **Số chữ `b` luôn NHIỀU HƠN số chữ `a` đúng 1 ký tự** ($\#b = \#a + 1$).
   - **Bẫy kinh điển:** Chuỗi `ab` (bằng nhau) KHÔNG thuộc $L$; chuỗi ngắn nhất là `b` (ứng với $n=0$).

### Bộ 24 câu trắc nghiệm chuẩn Đề Mẫu Sample 1 (+ 2 câu lý thuyết Word)

**Câu 1.** Xét ngôn ngữ $L$ sinh bởi $G_2$. Chuỗi nào sau đây **thuộc** $L$?
- A. `b`
- B. `ab`
- C. `a`
- D. $\varepsilon$
👉 **Đáp án đúng: A**
- **Giải thích:** Với $n=0$: $S \Rightarrow Ab \Rightarrow \varepsilon b = b$. `ab` sai vì $\#a=\#b$.

**Câu 2.** Xét ngôn ngữ $L$ sinh bởi $G_2$. Chuỗi nào sau đây **thuộc** $L$?
- A. `ab`
- B. `aab`
- C. `abb`
- D. `ba`
👉 **Đáp án đúng: C**
- **Giải thích:** `abb` có 1 `a`, 2 `b` ($\#b = 2 = 1 + 1$, ứng với $n=1$).

**Câu 3.** Xét ngôn ngữ $L$ sinh bởi $G_2$. Chuỗi nào sau đây **thuộc** $L$?
- A. `aabb`
- B. `aabbb`
- C. `aaabb`
- D. `abbb`
👉 **Đáp án đúng: B**
- **Giải thích:** `aabbb` có 2 `a`, 3 `b` ($n=2$).

**Câu 4.** Xét ngôn ngữ $L$ sinh bởi $G_2$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `b`
- B. `abb`
- C. `aabbb`
- D. `ab`
👉 **Đáp án đúng: D**
- **Giải thích:** `ab` có 1 `a` và 1 `b` (bằng nhau, vi phạm $\#b = \#a + 1$).

**Câu 5.** Xét ngôn ngữ $L$ sinh bởi $G_2$. Chuỗi nào sau đây **thuộc** $L$?
- A. `aaabbb`
- B. `aaabbbb`
- C. `aaaabbb`
- D. `abbbb`
👉 **Đáp án đúng: B**
- **Giải thích:** `aaabbbb` có 3 `a`, 4 `b` ($n=3$).

**Câu 6.** Xét ngôn ngữ $L$ sinh bởi $G_2$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `b`
- B. `abb`
- C. `aaabbbb`
- D. `aabb`
👉 **Đáp án đúng: D**
- **Giải thích:** `aabb` có số `a` bằng số `b` ($2=2$) nên KHÔNG thuộc $L$.

**Câu 7.** Xét ngôn ngữ $L$ sinh bởi $G_2$. Chuỗi nào sau đây **thuộc** $L$?
- A. `aaaabbbb`
- B. `aaaabbbbb`
- C. `aaabbbbb`
- D. `baaaabbbb`
👉 **Đáp án đúng: B**
- **Giải thích:** `aaaabbbbb` = $a^4 b^5$ ($n=4$).

**Câu 8.** Xét ngôn ngữ $L$ sinh bởi $G_2$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `b`
- B. `abb`
- C. `aabbb`
- D. `bb`
👉 **Đáp án đúng: D**
- **Giải thích:** `bb` có 0 `a`, 2 `b` ($2 \ne 0 + 1$) nên KHÔNG thuộc $L$.

**Câu 9.** Xét ngôn ngữ $L$ sinh bởi $G_2$. Chuỗi nào sau đây **thuộc** $L$?
- A. `aabb`
- B. `bab`
- C. `aaaabbbbb`
- D. `bbbb`
👉 **Đáp án đúng: C**
- **Giải thích:** `aaaabbbbb` thỏa $n=4$ ($a^4 b^5$).

**Câu 12.** Xét ngôn ngữ $L$ sinh bởi $G_2$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `b`
- B. `abb`
- C. `aaabbbb`
- D. `bab`
👉 **Đáp án đúng: D**
- **Giải thích:** `bab` có chữ `b` đứng trước `a` (sai thứ tự).

**Câu 10.** Chuỗi nào có thể sinh từ ký hiệu bắt đầu $S$ của $G_2$?
- A. `ab`
- B. `aabb`
- C. `aaabbbb`
- D. `ba`
👉 **Đáp án đúng: C**
- **Giải thích:** $S \Rightarrow Ab \Rightarrow^3 aaaAbbbb \Rightarrow aaabbbb$.

**Câu 11.** Chuỗi nào được sinh với **ÍT NHẤT 1 LẦN** dùng luật $A \to aAb$?
- A. `b`
- B. `abb`
- C. `ab`
- D. `aabb`
👉 **Đáp án đúng: B**
- **Giải thích:** Muốn dùng ít nhất 1 lần $A \to aAb$ thì phải sinh ra ít nhất 1 chữ `a`, nên chuỗi ngắn nhất là `abb` ($n=1$).

**Câu 13.** Chuỗi **NGẮN NHẤT** thuộc $L($G_2$)$ là:
- A. $\varepsilon$
- B. ``a``
- C. ``b``
- D. ``ab``
👉 **Đáp án đúng: C**
- **Giải thích:** $n=0 \implies S \Rightarrow Ab \Rightarrow b$ (độ dài 1).

**Câu 14.** Chuỗi **NGẮN NHÌ** thuộc $L($G_2$)$ (nếu cùng độ dài thì ưu tiên thứ tự từ điển tăng dần) là:
- A. ``ab``
- B. ``bb``
- C. ``abb``
- D. ``aab``
👉 **Đáp án đúng: C**
- **Giải thích:** Sau `b` ($n=0$, dài 1), chuỗi tiếp theo ứng với $n=1$ là `abb` (dài 3).

**Câu 15.** Ba chuỗi ngắn nhất thuộc $L($G_2$)$ (xếp theo độ dài và thứ tự từ điển tăng dần) là:
- A. b, ab, abb
- B. b, abb, aabbb
- C. b, bb, bbb
- D. ab, aabb, aaabbb
👉 **Đáp án đúng: B**
- **Giải thích:** Lần lượt ứng với $n=0, 1, 2$ là `b`, `abb`, `aabbb`.

**Câu 16.** Chuỗi **thứ 4** theo độ dài tăng dần của $L($G_2$)$ (nếu cùng độ dài ưu tiên thứ tự từ điển từ trái sang phải) là:
- A. ``aabbb``
- B. ``aaabbbb``
- C. ``aabb``
- D. ``abbb``
👉 **Đáp án đúng: B**
- **Giải thích:** Thứ tự độ dài: (1) `b`, (2) `abb`, (3) `aabbb`, (4) `aaabbbb` ($n=3$).

**Câu 17.** Chuỗi ngắn nhất thuộc $L($G_2$)$ thỏa điều kiện **có chứa ít nhất 1 ký tự `a`** là:
- A. ``ab``
- B. ``aab``
- C. ``abb``
- D. ``ba``
👉 **Đáp án đúng: C**
- **Giải thích:** Chuỗi hợp lệ ngắn nhất có chứa `a` ($n \ge 1$) là `abb` ($n=1$).

**Câu 18.** Số lượng ký tự `b` trong mọi chuỗi hợp lệ thuộc $L(G_2)$ là:
- A. $\ge 0$
- B. $\ge 1$
- C. Bằng số chữ `a`
- D. Nhỏ hơn số chữ `a`
👉 **Đáp án đúng: B**
- **Giải thích:** Do luật $S \to Ab$ luôn gắn ít nhất 1 chữ `b` ở cuối nên $\#b = n + 1 \ge 1$.

**Câu 19.** Quan hệ giữa số lượng chữ `a` và `b` trong $L(G_2)$ là:
- A. $b = a$
- B. $b = a + 1$
- C. $a = b + 1$
- D. $b = 2a$
👉 **Đáp án đúng: B**
- **Giải thích:** Dạng tổng quát là $a^n b^{n+1}$ nên số chữ `b` nhiều hơn số chữ `a` đúng 1 ký tự: $b = a + 1$.

**Câu 20.** Dạng tổng quát của chuỗi thuộc $L(G_2)$ là:
- A. $\{a^n b^n \mid n \ge 0\}$
- B. $\{a^n b^{n+1} \mid n \ge 0\}$
- C. $\{a^{n+1} b^n \mid n \ge 0\}$
- D. $\{a^n b^{n+1} \mid n \ge 1\}$
👉 **Đáp án đúng: B**
- **Giải thích:** Vì $A \to \varepsilon$ nên $n \ge 0$, ghép với $S \to Ab$ cho $\{a^n b^{n+1} \mid n \ge 0\}$.

**Câu 21.** Chuỗi `aabbb` có thuộc $L($G_2$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: A**
- **Giải thích:** Đúng, có 2 `a` và 3 `b` ($n=2$).

**Câu 22.** Chuỗi `ab` có thuộc $L($G_2$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: B**
- **Giải thích:** Sai, số `a` bằng số `b` ($1=1$).

**Câu 23.** Chuỗi `b` có thuộc $L($G_2$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: A**
- **Giải thích:** Đúng, ứng với $n=0$ ($S \Rightarrow Ab \Rightarrow b$).

**Câu 24.** Chuỗi `aaabb` có thuộc $L($G_2$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: B**
- **Giải thích:** Sai, 3 `a` nhưng chỉ 2 `b`.

**Câu 25.** (Câu hỏi Word) Văn phạm $G_2$ thuộc loại mấy theo phân loại Chomsky?
- A. Loại 3
- B. Loại 2 (Phi ngữ cảnh - CFG)
- C. Loại 1
- D. Loại 0
👉 **Đáp án đúng: B**
- **Giải thích:** $G_2$ là CFG chuẩn có bước kẹp $A \to aAb$, ngôn ngữ không chính quy nên thuộc Loại 2.

**Câu 26.** (Câu hỏi Word) Mô hình máy đoán nhận phù hợp cho $L(G_2)$ là:
- A. `DFA`
- B. `NFA`
- C. PDA (Otomat đẩy xuống)
- D. `LBA`
👉 **Đáp án đúng: C**
- **Giải thích:** Dùng PDA đẩy các chữ `a` vào Stack, đẩy thêm 1 đáy hoặc pop trước 1 chữ `b`, rồi đối chiếu `a` với `b`.

---

## VĂN PHẠM 5 ($G_5$): ĐỐI XỨNG KÈM ĐUÔI TỰ DO $\{a^n b^n a^m \mid n, m \ge 1\}$

> **ĐỀ BÀI GỐC ($G_5$):**
> $$
> G_5 = \langle \{a, b\},\ \{S, A\},\ S,\ \{S \to Sa \mid Aa,\ A \to aAb \mid ab\} \rangle
> $$
> Với các quy tắc sinh: $S \to Sa \mid Aa$, $A \to aAb \mid ab$

### Bản chất cốt lõi & Quy tắc vàng nhận diện trong 3 giây
1. **Dẫn xuất tổng quát:**
   - Biến $A$ ($A \to aAb \mid ab$) sinh ra $a^n b^n$ với **$n \ge 1$** (không có $\varepsilon$).
   - Biến $S$ ($S \to Sa \mid Aa$) sinh ra chuỗi $A a^m$ với **$m \ge 1$**.
   - Ghép lại: $\mathbf{w = a^n b^n a^m\ (n \ge 1,\ m \ge 1)}$.
2. **Ba quy tắc vàng 3 giây:**
   - **Cấu trúc 3 đoạn bắt buộc:** `a` đầu $\to$ `b` giữa $\to$ `a` cuối (cả 3 đoạn đều KHÔNG được rỗng!).
   - **Khớp mũ:** Số chữ `a` ở **đoạn đầu** PHẢI BẰNG số chữ `b` ở **đoạn giữa** ($n = \#b$).
   - **Đoạn `a` cuối:** Số lượng $m \ge 1$ hoàn toàn tự do, không phụ thuộc $n$!

### Bộ 24 câu trắc nghiệm chuẩn Đề Mẫu Sample 1 (+ 2 câu lý thuyết Word)

**Câu 1.** Xét ngôn ngữ $L$ sinh bởi $G_5$. Chuỗi nào sau đây **thuộc** $L$?
- A. `ab`
- B. `aba`
- C. `aab`
- D. `bba`
👉 **Đáp án đúng: B**
- **Giải thích:** `aba` = $a^1 b^1 a^1$ ($n=1, m=1$). `ab` thiếu đuôi `a` cuối.

**Câu 2.** Xét ngôn ngữ $L$ sinh bởi $G_5$. Chuỗi nào sau đây **thuộc** $L$?
- A. `abaa`
- B. `aaba`
- C. `abba`
- D. `baa`
👉 **Đáp án đúng: A**
- **Giải thích:** `abaa` = $a^1 b^1 a^2$ ($n=1, m=2$). `aaba` có 2 `a` đầu mà chỉ 1 `b` giữa.

**Câu 3.** Xét ngôn ngữ $L$ sinh bởi $G_5$. Chuỗi nào sau đây **thuộc** $L$?
- A. `aaba`
- B. `aaabba`
- C. `aabbaa`
- D. `abbaa`
👉 **Đáp án đúng: C**
- **Giải thích:** `aabbaa` = $a^2 b^2 a^2$ ($n=2, m=2$).

**Câu 4.** Xét ngôn ngữ $L$ sinh bởi $G_5$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `aba`
- B. `abaa`
- C. `aabba`
- D. `aabb`
👉 **Đáp án đúng: D**
- **Giải thích:** `aabb` không có đoạn `a` ở cuối (vi phạm $m \ge 1$).

**Câu 5.** Xét ngôn ngữ $L$ sinh bởi $G_5$. Chuỗi nào sau đây **thuộc** $L$?
- A. `aaabbba`
- B. `aaabba`
- C. `aabbb`
- D. `ababa`
👉 **Đáp án đúng: A**
- **Giải thích:** `aaabbba` = $a^3 b^3 a^1$ ($n=3, m=1$). `ababa` sai vì có 2 đoạn `b`.

**Câu 6.** Xét ngôn ngữ $L$ sinh bởi $G_5$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `aba`
- B. `abaaa`
- C. `aabbaaa`
- D. `aabbaabb`
👉 **Đáp án đúng: D**
- **Giải thích:** `aabbaabb` kết thúc bằng `b` nên KHÔNG thuộc $L$.

**Câu 7.** Xét ngôn ngữ $L$ sinh bởi $G_5$. Chuỗi nào sau đây **thuộc** $L$?
- A. `aabbba`
- B. `aabbaaa`
- C. `aaabbaa`
- D. `ba`
👉 **Đáp án đúng: B**
- **Giải thích:** `aabbaaa` = $a^2 b^2 a^3$ ($n=2, m=3$).

**Câu 8.** Xét ngôn ngữ $L$ sinh bởi $G_5$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `aba`
- B. `abaa`
- C. `aabba`
- D. `aaabbb`
👉 **Đáp án đúng: D**
- **Giải thích:** `aaabbb` thiếu đoạn `a` cuối ($m \ge 1$).

**Câu 9.** Xét ngôn ngữ $L$ sinh bởi $G_5$. Chuỗi nào sau đây **thuộc** $L$?
- A. `abbbba`
- B. `aaabbbaaa`
- C. `abaaab`
- D. `baab`
👉 **Đáp án đúng: B**
- **Giải thích:** `aaabbbaaa` = $a^3 b^3 a^3$ ($n=3, m=3$).

**Câu 12.** Xét ngôn ngữ $L$ sinh bởi $G_5$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `aba`
- B. `aabba`
- C. `abaaaa`
- D. `ababa`
👉 **Đáp án đúng: D**
- **Giải thích:** `ababa` xen kẽ 2 khối `b` nên không đúng khuôn $a^n b^n a^m$.

**Câu 10.** Chuỗi nào có thể sinh từ ký hiệu bắt đầu $S$ của $G_5$?
- A. `ab`
- B. `aabb`
- C. `aabba`
- D. `bab`
👉 **Đáp án đúng: C**
- **Giải thích:** $S \Rightarrow Aa \Rightarrow aAba \Rightarrow aabba$.

**Câu 11.** Chuỗi nào được sinh với **ÍT NHẤT 1 LẦN** dùng luật $S \to Sa$?
- A. `aba`
- B. `aabba`
- C. `abaa`
- D. `aaabbba`
👉 **Đáp án đúng: C**
- **Giải thích:** Dùng ít nhất 1 lần $S \to Sa$ tạo ít nhất 2 chữ `a` ở cuối (đuôi `aa`), nên chuỗi ngắn nhất thỏa điều này là `abaa` ($n=1, m=2$).

**Câu 13.** Chuỗi **NGẮN NHẤT** thuộc $L($G_5$)$ là:
- A. ``ab``
- B. ``ba``
- C. ``aba``
- D. ``aabb``
👉 **Đáp án đúng: C**
- **Giải thích:** Với $n=1, m=1$, ta có `aba` (độ dài 3).

**Câu 14.** Chuỗi **NGẮN NHÌ** thuộc $L($G_5$)$ (nếu cùng độ dài thì ưu tiên thứ tự từ điển tăng dần) là:
- A. ``aaba``
- B. ``abaa``
- C. ``abba``
- D. ``aabb``
👉 **Đáp án đúng: B**
- **Giải thích:** Chuỗi độ dài 4 duy nhất trong $L$ là `abaa` ($n=1, m=2$).

**Câu 15.** Ba chuỗi ngắn nhất thuộc $L($G_5$)$ (xếp theo độ dài và thứ tự từ điển tăng dần) là:
- A. ab, aba, aaba
- B. aba, abaa, aabba
- C. aba, aaba, abaa
- D. aba, abaa, abaaa
👉 **Đáp án đúng: B**
- **Giải thích:** Dài 3: `aba`. Dài 4: `abaa`. Dài 5 có `aabba` ($n=2,m=1$) và `abaaa` ($n=1,m=3$); theo từ điển `a < b` nên `aabba` đứng trước `abaaa`!

**Câu 16.** Chuỗi **thứ 4** theo độ dài tăng dần của $L($G_5$)$ (nếu cùng độ dài ưu tiên thứ tự từ điển từ trái sang phải) là:
- A. ``abaaa``
- B. ``aabba``
- C. ``aaabbba``
- D. ``abaaaa``
👉 **Đáp án đúng: A**
- **Giải thích:** Thứ tự tăng dần: (1) `aba` (dài 3), (2) `abaa` (dài 4), (3) `aabba` (dài 5), (4) `abaaa` (dài 5).

**Câu 17.** Chuỗi ngắn nhất thuộc $L($G_5$)$ thỏa điều kiện **có độ dài $\ge 4$** là:
- A. ``aabb``
- B. ``abaa``
- C. ``aaba``
- D. ``abba``
👉 **Đáp án đúng: B**
- **Giải thích:** Chuỗi hợp lệ ngắn nhất có độ dài $\ge 4$ là `abaa` (độ dài 4).

**Câu 18.** Tổng số chữ `a` trong mọi chuỗi hợp lệ của $L(G_5)$ thỏa mãn:
- A. Bằng số chữ `b`
- B. Lớn hơn số chữ `b` ít nhất 1 ký tự ($\#a = \#b + m \ge \#b + 1$)
- C. Luôn nhỏ hơn số chữ `b`
- D. Luôn bằng 2
👉 **Đáp án đúng: B**
- **Giải thích:** Số `a` gồm $n$ chữ đầu + $m$ chữ cuối ($m \ge 1$), còn số `b` là $n$, nên $\#a = \#b + m > \#b$.

**Câu 19.** Mối quan hệ chính xác giữa các đoạn trong chuỗi $w = a^n b^k a^m \in L(G_5)$ là:
- A. $n = k = m$
- B. $n = k$ và $m \ge 1$ tự do
- C. $k = m$ và $n \ge 1$
- D. $n + m = k$
👉 **Đáp án đúng: B**
- **Giải thích:** Khối $a^n b^n$ do $A$ sinh ra có $n=k \ge 1$, còn đuôi $a^m$ ($m \ge 1$) hoàn toàn độc lập.

**Câu 20.** Dạng tổng quát của chuỗi thuộc $L(G_5)$ là:
- A. $\{a^n b^n a^m \mid n \ge 1, m \ge 1\}$
- B. $\{a^n b^n a^m \mid n \ge 0, m \ge 0\}$
- C. $\{a^n b^m a^n \mid n, m \ge 1\}$
- D. $\{a^n b^n a^n \mid n \ge 1\}$
👉 **Đáp án đúng: A**
- **Giải thích:** $A$ bắt buộc có $ab$ ($n \ge 1$) và $S$ luôn kết thúc qua $Aa$ ($m \ge 1$).

**Câu 21.** Chuỗi `aabbaa` có thuộc $L($G_5$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: A**
- **Giải thích:** Đúng, $a^2 b^2 a^2$ ($n=2, m=2$).

**Câu 22.** Chuỗi `aabb` có thuộc $L($G_5$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: B**
- **Giải thích:** Sai, thiếu đoạn `a` ở cuối ($m \ge 1$).

**Câu 23.** Chuỗi `abaaa` có thuộc $L($G_5$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: A**
- **Giải thích:** Đúng, $a^1 b^1 a^3$ ($n=1, m=3$).

**Câu 24.** Chuỗi `aaabba` có thuộc $L($G_5$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: B**
- **Giải thích:** Sai, 3 `a` đầu nhưng chỉ 2 `b` ở giữa.

**Câu 25.** (Câu hỏi Word) $G_5$ thuộc loại văn phạm nào theo Chomsky?
- A. Loại 3
- B. Loại 2 (Phi ngữ cảnh - CFG)
- C. Loại 1
- D. Loại 0
👉 **Đáp án đúng: B**
- **Giải thích:** Mọi vế trái chỉ gồm 1 biến ($S$ hoặc $A$) và có đối xứng $a^n b^n$ nên là Loại 2 (CFG).

**Câu 26.** (Câu hỏi Word) Sau khi PDA đối chiếu xong khối $a^n b^n$ bằng Stack, phần đuôi $a^m$ được xử lý thế nào?
- A. Tiếp tục đẩy vào Stack để đếm bằng $n$
- B. Không dùng Stack nữa, chuyển sang trạng thái đọc tự do ít nhất 1 chữ `a` rồi kết thúc
- C. Không cần PDA, DFA làm được cả bài
- D. Phải dùng LBA mới đếm được $a^m$
👉 **Đáp án đúng: B**
- **Giải thích:** Đoạn $a^m$ là phần chính quy tự do ở đuôi nên PDA chỉ cần dùng 1 trạng thái tự lặp để đọc nốt `a`.

---

## VĂN PHẠM 6 ($G_6$): CÂN BẰNG SỐ CHỮ `0` VÀ `1` ($\#0 = \#1$)

> **ĐỀ BÀI GỐC ($G_6$):**
> $$
> G_6 = \langle \{0, 1\},\ \{S\},\ S,\ \{S \to SS \mid 0S1 \mid 1S0 \mid \varepsilon\} \rangle
> $$
> Với các quy tắc sinh: $S \to SS \mid 0S1 \mid 1S0 \mid \varepsilon$

### Bản chất cốt lõi & Quy tắc vàng nhận diện trong 3 giây
1. **Ý nghĩa các luật:**
   - $S \to 0S1$ và $S \to 1S0$: mỗi bước bọc thêm **1 chữ `0` và 1 chữ `1`**, luôn giữ cân bằng số lượng!
   - $S \to SS$: ghép hai chuỗi cân bằng lại với nhau (nên chuỗi `01` + `10` = `0110` hợp lệ, bất kể thứ tự!).
2. **Ba quy tắc vàng 3 giây:**
   - **KHÔNG BẮT BUỘC THỨ TỰ:** `0` và `1` có thể trộn lẫn bất kỳ (`0101`, `1001`, `1100`, `0110` đều đúng!).
   - **ĐIỀU KIỆN DUY NHẤT:** **Tổng số chữ `0` BẰNG CHÍNH XÁC tổng số chữ `1`** ($\#0(w) = \#1(w)$).
   - Độ dài chuỗi luôn chẵn (kể cả $\varepsilon$).

### Bộ 24 câu trắc nghiệm chuẩn Đề Mẫu Sample 1 (+ 2 câu lý thuyết Word)

**Câu 1.** Xét ngôn ngữ $L$ sinh bởi $G_6$. Chuỗi nào sau đây **thuộc** $L$?
- A. `0`
- B. `1`
- C. `01`
- D. `001`
👉 **Đáp án đúng: C**
- **Giải thích:** `01` có 1 số `0` và 1 số `1` ($1=1$).

**Câu 2.** Xét ngôn ngữ $L$ sinh bởi $G_6$. Chuỗi nào sau đây **thuộc** $L$?
- A. `100`
- B. `011`
- C. `10`
- D. `111`
👉 **Đáp án đúng: C**
- **Giải thích:** `10` có 1 số `1` và 1 số `0` ($S \Rightarrow 1S0 \Rightarrow 10$).

**Câu 3.** Xét ngôn ngữ $L$ sinh bởi $G_6$. Chuỗi nào sau đây **thuộc** $L$?
- A. `0110`
- B. `0010`
- C. `1101`
- D. `0001`
👉 **Đáp án đúng: A**
- **Giải thích:** `0110` có 2 số `0`, 2 số `1` ($S \Rightarrow SS \Rightarrow 0S1\,1S0 \Rightarrow 0110$).

**Câu 4.** Xét ngôn ngữ $L$ sinh bởi $G_6$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. $\varepsilon$
- B. `01`
- C. `10`
- D. `001`
👉 **Đáp án đúng: D**
- **Giải thích:** `001` có 2 số `0` nhưng chỉ 1 số `1` ($2 \ne 1$).

**Câu 5.** Xét ngôn ngữ $L$ sinh bởi $G_6$. Chuỗi nào sau đây **thuộc** $L$?
- A. `00101`
- B. `1010`
- C. `1110`
- D. `010`
👉 **Đáp án đúng: B**
- **Giải thích:** `1010` có 2 số `0`, 2 số `1`.

**Câu 6.** Xét ngôn ngữ $L$ sinh bởi $G_6$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `0110`
- B. `1001`
- C. `0101`
- D. `01101`
👉 **Đáp án đúng: D**
- **Giải thích:** `01101` dài 5 (số lẻ!) $\implies$ không thể cân bằng `0` và `1`.

**Câu 7.** Xét ngôn ngữ $L$ sinh bởi $G_6$. Chuỗi nào sau đây **thuộc** $L$?
- A. `11001`
- B. `00011`
- C. `101100`
- D. `1110`
👉 **Đáp án đúng: C**
- **Giải thích:** `101100` có 3 số `0`, 3 số `1`.

**Câu 8.** Xét ngôn ngữ $L$ sinh bởi $G_6$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. $\varepsilon$
- B. `0101`
- C. `1100`
- D. `1101`
👉 **Đáp án đúng: D**
- **Giải thích:** `1101` có 3 số `1`, 1 số `0` ($3 \ne 1$).

**Câu 9.** Xét ngôn ngữ $L$ sinh bởi $G_6$. Chuỗi nào sau đây **thuộc** $L$?
- A. `00011100`
- B. `101010`
- C. `00111`
- D. `11100`
👉 **Đáp án đúng: B**
- **Giải thích:** `101010` có 3 số `0`, 3 số `1`.

**Câu 12.** Xét ngôn ngữ $L$ sinh bởi $G_6$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `0011`
- B. `1100`
- C. `1010`
- D. `00110`
👉 **Đáp án đúng: D**
- **Giải thích:** `00110` có 3 số `0`, 2 số `1`.

**Câu 10.** Chuỗi nào có thể sinh từ ký hiệu bắt đầu $S$ của $G_6$?
- A. `001`
- B. `110`
- C. `1001`
- D. `010`
👉 **Đáp án đúng: C**
- **Giải thích:** `1001` cân bằng (`#0 = #1 = 2`): $S \Rightarrow 1S0 \Rightarrow 1(0S1)0 \Rightarrow 1001$ (hoặc $S \Rightarrow SS \Rightarrow 10\,01$).

**Câu 11.** Chuỗi nào được sinh với **ÍT NHẤT 1 LẦN** dùng luật $S \to SS$ với hai nhánh con khác rỗng (ví dụ có chữ đầu và chữ cuối GIỐNG NHAU)?
- A. `01`
- B. `10`
- C. `0110`
- D. `0011`
👉 **Đáp án đúng: C**
- **Giải thích:** Chữ đầu và cuối của `01`, `10`, `0011` đều khác nhau (`0..1` hoặc `1..0`) nên có thể chỉ dùng $0S1$ hoặc $1S0$. Riêng `0110` bắt đầu và kết thúc đều là `0`, bắt buộc phải tách bằng $S \to SS \Rightarrow (0S1)(1S0) \Rightarrow 0110$!

**Câu 13.** Chuỗi **NGẮN NHẤT** thuộc $L($G_6$)$ là:
- A. $\varepsilon$
- B. ``01``
- C. ``10``
- D. ``0``
👉 **Đáp án đúng: A**
- **Giải thích:** Nhờ luật $S \to \varepsilon$, chuỗi ngắn nhất là $\varepsilon$.

**Câu 14.** Chuỗi **NGẮN NHÌ** thuộc $L($G_6$)$ (nếu cùng độ dài thì ưu tiên thứ tự từ điển tăng dần) là:
- A. ``10``
- B. ``01``
- C. ``0011``
- D. ``0``
👉 **Đáp án đúng: B**
- **Giải thích:** Có 2 chuỗi dài 2 là `01` và `10`. Theo thứ tự từ điển (`0 < 1`), `01` đứng đầu nên `01` là chuỗi ngắn nhì!

**Câu 15.** Ba chuỗi ngắn nhất thuộc $L($G_6$)$ (xếp theo độ dài và thứ tự từ điển tăng dần) là:
- A. $\varepsilon$, 01, 0011
- B. $\varepsilon$, 01, 10
- C. 01, 10, 0011
- D. $\varepsilon$, 10, 01
👉 **Đáp án đúng: B**
- **Giải thích:** Ngắn nhất là $\varepsilon$ (dài 0), kế đến 2 chuỗi dài 2 là `01` rồi `10`.

**Câu 16.** Chuỗi **thứ 4** theo độ dài tăng dần của $L($G_6$)$ (nếu cùng độ dài ưu tiên thứ tự từ điển từ trái sang phải) là:
- A. ``10``
- B. ``0011``
- C. ``0101``
- D. ``1100``
👉 **Đáp án đúng: B**
- **Giải thích:** Thứ tự (độ dài, từ điển): (1) $\varepsilon$, (2) `01`, (3) `10`, (4) `0011` (chuỗi đầu tiên trong nhóm độ dài 4)!

**Câu 17.** Chuỗi ngắn nhất thuộc $L($G_6$)$ thỏa điều kiện **khác rỗng ($\ne \varepsilon$)** là:
- A. ``0``
- B. ``1``
- C. ``01``
- D. ``10``
👉 **Đáp án đúng: C**
- **Giải thích:** Chuỗi khác rỗng ngắn nhất theo thứ tự từ điển là `01` (dài 2).

**Câu 18.** Tổng độ dài mọi chuỗi thuộc $L(G_6)$ luôn là:
- A. Số lẻ
- B. Số chẵn ($2k$ với $k \ge 0$)
- C. Bằng 2
- D. Bội của 4
👉 **Đáp án đúng: B**
- **Giải thích:** Vì $\#0 = \#1 = k$ nên tổng độ dài là $k + k = 2k$ (luôn chẵn).

**Câu 19.** Điều kiện CẦN VÀ ĐỦ để một chuỗi nhị phân $w$ thuộc $L(G_6)$ là:
- A. Toàn bộ chữ `0` đứng trước chữ `1`
- B. Số lượng chữ `0` bằng số lượng chữ `1` ($\#0(w) = \#1(w)$)
- C. Bắt đầu bằng `0` và kết thúc bằng `1`
- D. Là chuỗi đối xứng (Palindrome)
👉 **Đáp án đúng: B**
- **Giải thích:** Nhờ $S \to SS \mid 0S1 \mid 1S0 \mid \varepsilon$, mọi hoán vị có $\#0 = \#1$ đều sinh được.

**Câu 20.** Biểu diễn tập hợp đúng nhất của $L(G_6)$ là:
- A. $\{0^n 1^n \mid n \ge 0\}$
- B. $\{w \in \{0,1\}^* \mid \#0(w) = \#1(w)\}$
- C. $(01 + 10)^*$
- D. $\{w \in \{0,1\}^+ \mid \#0(w) = \#1(w)\}$
👉 **Đáp án đúng: B**
- **Giải thích:** Chú ý `(01 + 10)*` KHÔNG sinh được `0011`! Đáp án đúng phải là tập mọi chuỗi có $\#0(w) = \#1(w)$ (kể cả $\varepsilon$).

**Câu 21.** Chuỗi `1001` có thuộc $L($G_6$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: A**
- **Giải thích:** Đúng, có 2 `0` và 2 `1`.

**Câu 22.** Chuỗi `00110` có thuộc $L($G_6$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: B**
- **Giải thích:** Sai, 3 `0` và 2 `1`.

**Câu 23.** Chuỗi `011010` có thuộc $L($G_6$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: A**
- **Giải thích:** Đúng, 3 `0` và 3 `1`.

**Câu 24.** Chuỗi `011` có thuộc $L($G_6$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: B**
- **Giải thích:** Sai, 1 `0` và 2 `1`.

**Câu 25.** (Câu hỏi Word) Văn phạm $G_6$ có bị nhập nhằng (mơ hồ - ambiguous) không?
- A. Không, vì mỗi chuỗi chỉ có 1 cây dẫn xuất
- B. Có, rất mơ hồ (ví dụ $\varepsilon$ hay `0101` có nhiều cây dẫn xuất khác nhau)
- C. Là văn phạm chính quy Loại 3
- D. Chỉ sinh chuỗi không rỗng
👉 **Đáp án đúng: B**
- **Giải thích:** Luật $S \to SS$ và $S \to \varepsilon$ làm $S \Rightarrow SS \Rightarrow \varepsilon$ và $S \Rightarrow \varepsilon$ tạo vô số cây cho cùng chuỗi $\varepsilon$ hay `0101`.

**Câu 26.** (Câu hỏi Word) $G_6$ thuộc loại mấy trong phân loại Chomsky?
- A. Loại 3
- B. Loại 2 (Phi ngữ cảnh - CFG)
- C. Loại 1
- D. Loại 0
👉 **Đáp án đúng: B**
- **Giải thích:** Mọi vế trái chỉ là biến $S$, nhưng ngôn ngữ không chính quy nên thuộc Loại 2.

---

## VĂN PHẠM 10 ($G_{10}$): TỶ LỆ GẤP ĐÔI $\{a^n c b^{2n} \mid n \ge 0\}$

> **LƯU Ý GỘP DẠNG TỰA NHAU:** Bộ câu hỏi này đại diện luôn cho **$G_{11} = \{S \to CSD \mid c, C \to aa, D \to b\}$** (tựa hệt nhau, chỉ đảo vai trò $a \leftrightarrow b$: $G_{11}$ sinh $a^{2n} c b^n$ với $\#a = 2\#b$).

> **ĐỀ BÀI GỐC ($G_{10}$):**
> $$
> G_{10} = \langle \{a, b, c\},\ \{S, A, B\},\ S,\ \{S \to ASB \mid c,\ A \to a,\ B \to bb\} \rangle
> $$
> Với các quy tắc sinh: $S \to ASB \mid c$, $A \to a$, $B \to bb$

### Bản chất cốt lõi & Quy tắc vàng nhận diện trong 3 giây
1. **Dẫn xuất tổng quát:**
   - Lặp $S \to ASB$ đúng $n$ lần ($n \ge 0$): $S \Rightarrow A^n S B^n \Rightarrow A^n c B^n$.
   - Thế $A \to a$ ($1$ chữ $a$) và $B \to bb$ ($2$ chữ $b$): $\mathbf{w = a^n c b^{2n}\ (n \ge 0)}$.
2. **Ba quy tắc vàng 3 giây:**
   - Ở giữa luôn có **đúng 1 chữ `c`** (không nhiều hơn, không thiếu).
   - Bên trái `c` toàn chữ `a`, bên phải `c` toàn chữ `b`.
   - **Số chữ `b` luôn GẤP ĐÔI số chữ `a`**: $\#b = 2 \times \#a$.

### Bộ 24 câu trắc nghiệm chuẩn Đề Mẫu Sample 1 (+ 2 câu lý thuyết Word)

**Câu 1.** Xét ngôn ngữ $L$ sinh bởi $G_{10}$. Chuỗi nào sau đây **thuộc** $L$?
- A. `c`
- B. `ac`
- C. `cb`
- D. `acb`
👉 **Đáp án đúng: A**
- **Giải thích:** Với $n=0$: $S \Rightarrow c$ (0 chữ `a`, 1 chữ `c`, 0 chữ `b`).

**Câu 2.** Xét ngôn ngữ $L$ sinh bởi $G_{10}$. Chuỗi nào sau đây **thuộc** $L$?
- A. `acb`
- B. `acbb`
- C. `aacbb`
- D. `abbc`
👉 **Đáp án đúng: B**
- **Giải thích:** Với $n=1$: $a^1 c b^2 =$ `acbb` (1 `a`, 2 `b`).

**Câu 3.** Xét ngôn ngữ $L$ sinh bởi $G_{10}$. Chuỗi nào sau đây **thuộc** $L$?
- A. `aacbb`
- B. `aacbbb`
- C. `aacbbbb`
- D. `aaacbbbb`
👉 **Đáp án đúng: C**
- **Giải thích:** Với $n=2$: $a^2 c b^4 =$ `aacbbbb`.

**Câu 4.** Xét ngôn ngữ $L$ sinh bởi $G_{10}$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `c`
- B. `acbb`
- C. `aacbbbb`
- D. `aacbb`
👉 **Đáp án đúng: D**
- **Giải thích:** `aacbb` có 2 `a` nhưng chỉ 2 `b` (phải là 4 `b`).

**Câu 5.** Xét ngôn ngữ $L$ sinh bởi $G_{10}$. Chuỗi nào sau đây **thuộc** $L$?
- A. `aaacbbbbbb`
- B. `aaacbbbb`
- C. `aacbbbbbb`
- D. `aaaccbbbbbb`
👉 **Đáp án đúng: A**
- **Giải thích:** Với $n=3$: $a^3 c b^6 =$ `aaacbbbbbb`.

**Câu 6.** Xét ngôn ngữ $L$ sinh bởi $G_{10}$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `c`
- B. `acbb`
- C. `aaacbbbbbb`
- D. `acb`
👉 **Đáp án đúng: D**
- **Giải thích:** `acb` có 1 `a` và 1 `b` ($1 \ne 2 \times 1$).

**Câu 7.** Xét ngôn ngữ $L$ sinh bởi $G_{10}$. Chuỗi nào sau đây **thuộc** $L$?
- A. `aaacbbbbbbbb`
- B. `aaaacbbbbbbbb`
- C. `aaaacbbbbbb`
- D. `acbbbbb`
👉 **Đáp án đúng: B**
- **Giải thích:** Với $n=4$: $a^4 c b^8 =$ `aaaacbbbbbbbb`.

**Câu 8.** Xét ngôn ngữ $L$ sinh bởi $G_{10}$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `c`
- B. `acbb`
- C. `aacbbbb`
- D. `acccbb`
👉 **Đáp án đúng: D**
- **Giải thích:** `acccbb` có tới 3 chữ `c` (chỉ được có đúng 1 chữ `c`).

**Câu 9.** Xét ngôn ngữ $L$ sinh bởi $G_{10}$. Chuỗi nào sau đây **thuộc** $L$?
- A. `accbb`
- B. `aacbbb`
- C. `aacbbbb`
- D. `aaacbbb`
👉 **Đáp án đúng: C**
- **Giải thích:** `aacbbbb` ($n=2$).

**Câu 12.** Xét ngôn ngữ $L$ sinh bởi $G_{10}$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `c`
- B. `acbb`
- C. `aacbbbb`
- D. `bbca`
👉 **Đáp án đúng: D**
- **Giải thích:** `bbca` đảo `b` lên trước `a` (sai thứ tự).

**Câu 10.** Chuỗi nào có thể sinh từ ký hiệu bắt đầu $S$ của $G_{10}$?
- A. `acb`
- B. `aaccbb`
- C. `aacbbbb`
- D. $\varepsilon$
👉 **Đáp án đúng: C**
- **Giải thích:** `aacbbbb` = $a^2 c b^4$ ($S \Rightarrow^2 AASBB \Rightarrow aacbbbb$).

**Câu 11.** Chuỗi nào được sinh với **ÍT NHẤT 1 LẦN** dùng luật $S \to ASB$?
- A. `c`
- B. `acb`
- C. `acbb`
- D. `ab`
👉 **Đáp án đúng: C**
- **Giải thích:** Dùng ít nhất 1 lần $S \to ASB$ tạo $1$ cặp `a`...`bb` kẹp quanh `c`, sinh `acbb`.

**Câu 13.** Chuỗi **NGẮN NHẤT** thuộc $L($G_{10}$)$ là:
- A. $\varepsilon$
- B. ``c``
- C. ``acb``
- D. ``acbb``
👉 **Đáp án đúng: B**
- **Giải thích:** $n=0 \implies S \Rightarrow c$ (độ dài 1).

**Câu 14.** Chuỗi **NGẮN NHÌ** thuộc $L($G_{10}$)$ (nếu cùng độ dài thì ưu tiên thứ tự từ điển tăng dần) là:
- A. ``acb``
- B. ``acbb``
- C. ``cc``
- D. ``aacb``
👉 **Đáp án đúng: B**
- **Giải thích:** Sau `c` ($n=0$, dài 1), chuỗi hợp lệ ngắn nhì là `acbb` ($n=1$, dài 4).

**Câu 15.** Ba chuỗi ngắn nhất thuộc $L($G_{10}$)$ (xếp theo độ dài và thứ tự từ điển tăng dần) là:
- A. c, acb, aacbb
- B. c, acbb, aacbbbb
- C. c, cc, ccc
- D. acbb, aacbbbb, aaacbbbbbb
👉 **Đáp án đúng: B**
- **Giải thích:** Lần lượt ứng với $n=0, 1, 2$ là `c` (dài 1), `acbb` (dài 4), `aacbbbb` (dài 7).

**Câu 16.** Chuỗi **thứ 4** theo độ dài tăng dần của $L($G_{10}$)$ (nếu cùng độ dài ưu tiên thứ tự từ điển từ trái sang phải) là:
- A. ``aacbbbb``
- B. ``aaacbbbbbb``
- C. ``aaacbbbb``
- D. ``acbbbb``
👉 **Đáp án đúng: B**
- **Giải thích:** Chuỗi thứ 4 ứng với $n=3$: `aaacbbbbbb` (độ dài $3+1+6 = 10$).

**Câu 17.** Chuỗi ngắn nhất thuộc $L($G_{10}$)$ thỏa điều kiện **có chứa ít nhất 1 chữ `a`** là:
- A. ``ac``
- B. ``acb``
- C. ``acbb``
- D. ``aacbb``
👉 **Đáp án đúng: C**
- **Giải thích:** Chuỗi ngắn nhất có chứa chữ `a` ($n=1$) là `acbb`.

**Câu 18.** Số lượng ký tự `c` trong mọi chuỗi hợp lệ thuộc $L(G_{10})$ là:
- A. $\ge 1$
- B. Đúng bằng 1
- C. Bằng số chữ `a`
- D. `Chẵn`
👉 **Đáp án đúng: B**
- **Giải thích:** Luật $S \to ASB$ không sinh `c`, chỉ khi dừng $S \to c$ mới sinh ra **đúng 1 chữ `c`**.

**Câu 19.** Quan hệ giữa số lượng chữ `a` và `b` trong $L(G_{10})$ là:
- A. $b = a$
- B. $a = 2b$
- C. $b = 2a$
- D. $b = 2a + 1$
👉 **Đáp án đúng: C**
- **Giải thích:** Mỗi lần lặp sinh 1 $A \to a$ và 1 $B \to bb$ nên $\#b = 2 \times \#a$.

**Câu 20.** Dạng tổng quát của ngôn ngữ $L(G_{10})$ là:
- A. $\{a^n c b^n \mid n \ge 0\}$
- B. $\{a^n c b^{2n} \mid n \ge 0\}$
- C. $\{a^{2n} c b^n \mid n \ge 0\}$
- D. $\{a^n c b^{2n} \mid n \ge 1\}$
👉 **Đáp án đúng: B**
- **Giải thích:** Khi $n=0$ sinh `c`, tổng quát là $\{a^n c b^{2n} \mid n \ge 0\}$.

**Câu 21.** Chuỗi `aacbbbb` có thuộc $L($G_{10}$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: A**
- **Giải thích:** Đúng, $a^2 c b^4$ ($n=2$).

**Câu 22.** Chuỗi `acbbbbb` có thuộc $L($G_{10}$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: B**
- **Giải thích:** Sai, 1 `a` nhưng 5 `b`.

**Câu 23.** Chuỗi `c` có thuộc $L($G_{10}$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: A**
- **Giải thích:** Đúng, $n=0$.

**Câu 24.** Chuỗi `aacbb` có thuộc $L($G_{10}$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: B**
- **Giải thích:** Sai, 2 `a` mà chỉ có 2 `b`.

**Câu 25.** (Câu hỏi Word) Ngôn ngữ của $G_{10}$ thuộc loại mấy theo Chomsky?
- A. Loại 3
- B. Loại 2 (Phi ngữ cảnh - CFG)
- C. Loại 1
- D. Loại 0
👉 **Đáp án đúng: B**
- **Giải thích:** Văn phạm kẹp đối xứng 2 đầu với tỷ lệ 1:2 thuộc Loại 2 (CFG).

**Câu 26.** (Câu hỏi Word) Trong tập 19 văn phạm, $G_{10}$ liên hệ đối xứng với văn phạm nào?
- A. $G_1$
- B. $G_{11}$ ($a^{2n} c b^n$)
- C. $G_7$
- D. $G_{14}$
👉 **Đáp án đúng: B**
- **Giải thích:** $G_{11}$ đảo vai trò $C \to aa, D \to b$ nên sinh $a^{2n} c b^n$ (đối xứng ngược lại với $G_{10}$).

---

## VĂN PHẠM 15 ($G_{15}$): BIẾN THỂ SAMPLE 1 DỒN KÝ TỰ $\{0^k 1^p \mid k \ge 1,\ p \ge k + 1\}$

> **ĐỀ BÀI GỐC ($G_{15}$):**
> $$
> G_{15} = \langle \{0, 1\},\ \{S, A\},\ S,\ \{S \to 0S1 \mid 0A1,\ A \to 1A \mid 1\} \rangle
> $$
> Với các quy tắc sinh: $S \to 0S1 \mid 0A1$, $A \to 1A \mid 1$

### Bản chất cốt lõi & Quy tắc vàng nhận diện trong 3 giây
1. **Dẫn xuất tổng quát:**
   - Lặp $S \to 0S1$ đúng $n$ lần ($n \ge 0$): $0^n S 1^n$.
   - Dừng $S$ qua $S \to 0A1$: $0^{n+1} A 1^{n+1}$.
   - Biến $A \to 1A \mid 1$ sinh $1^m$ ($m \ge 1$).
   - Ghép lại: $\mathbf{w = 0^{n+1} 1^{m+n+1} = 0^k 1^p}$ với **$k = n+1 \ge 1$** và **$p = k + m \ge k + 1$**!
2. **Mẹo 3 giây (khác Sample 1 ở đâu?):**
   - Trong Sample 1, phần giữa là chữ `c` tách biệt với chữ `b` cuối. Ở đây phần giữa và phần cuối **ĐỀU LÀ CHỮ `1`** nên gộp thành một dãy toàn `1`!
   - **Thứ tự:** Toàn bộ `0` đứng đầu $\to$ toàn bộ `1` đứng sau.
   - **Điều kiện đếm:** **Số chữ `1` LUÔN NHIỀU HƠN số chữ `0` ít nhất 1 ký tự** ($\#1 \ge \#0 + 1$, và $\#0 \ge 1$).
   - **Bẫy chết người:** `01` và `0011` KHÔNG thuộc $L$ (vì bằng nhau!). Chuỗi ngắn nhất là `011` ($k=1, p=2$).

### Bộ 24 câu trắc nghiệm chuẩn Đề Mẫu Sample 1 (+ 2 câu lý thuyết Word)

**Câu 1.** Xét ngôn ngữ $L$ sinh bởi $G_{15}$. Chuỗi nào sau đây **thuộc** $L$?
- A. `01`
- B. `011`
- C. `11`
- D. `0`
👉 **Đáp án đúng: B**
- **Giải thích:** `011` có 1 số `0` và 2 số `1` ($2 \ge 1+1$, ứng với $n=0, m=1$).

**Câu 2.** Xét ngôn ngữ $L$ sinh bởi $G_{15}$. Chuỗi nào sau đây **thuộc** $L$?
- A. `0011`
- B. `0101`
- C. `00111`
- D. `1001`
👉 **Đáp án đúng: C**
- **Giải thích:** `00111` có 2 số `0`, 3 số `1` ($n=1, m=1$). `0011` sai vì bằng nhau.

**Câu 3.** Xét ngôn ngữ $L$ sinh bởi $G_{15}$. Chuỗi nào sau đây **thuộc** $L$?
- A. `0011`
- B. `000111`
- C. `0001111`
- D. `0110`
👉 **Đáp án đúng: C**
- **Giải thích:** `0001111` có 3 `0`, 4 `1` ($n=2, m=1$).

**Câu 4.** Xét ngôn ngữ $L$ sinh bởi $G_{15}$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `011`
- B. `0111`
- C. `00111`
- D. `01`
👉 **Đáp án đúng: D**
- **Giải thích:** `01` có $\#0 = \#1 = 1$, vi phạm $\#1 \ge \#0 + 1$.

**Câu 5.** Xét ngôn ngữ $L$ sinh bởi $G_{15}$. Chuỗi nào sau đây **thuộc** $L$?
- A. `001111`
- B. `00011`
- C. `00001111`
- D. `01011`
👉 **Đáp án đúng: A**
- **Giải thích:** `001111` có 2 `0`, 4 `1` ($4 \ge 2+1$, ứng với $n=1, m=2$).

**Câu 6.** Xét ngôn ngữ $L$ sinh bởi $G_{15}$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `011`
- B. `00111`
- C. `001111`
- D. `0011`
👉 **Đáp án đúng: D**
- **Giải thích:** `0011` có 2 `0`, 2 `1` (không đủ ít nhất $2+1=3$ chữ `1`).

**Câu 7.** Xét ngôn ngữ $L$ sinh bởi $G_{15}$. Chuỗi nào sau đây **thuộc** $L$?
- A. `000111`
- B. `00011111`
- C. `00001111`
- D. `1111`
👉 **Đáp án đúng: B**
- **Giải thích:** `00011111` có 3 `0`, 5 `1` ($n=2, m=2$).

**Câu 8.** Xét ngôn ngữ $L$ sinh bởi $G_{15}$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `011`
- B. `01111`
- C. `00111`
- D. `111`
👉 **Đáp án đúng: D**
- **Giải thích:** `111` không có chữ `0` nào (vi phạm $\#0 \ge 1$).

**Câu 9.** Xét ngôn ngữ $L$ sinh bởi $G_{15}$. Chuỗi nào sau đây **thuộc** $L$?
- A. `001`
- B. `000111`
- C. `01111`
- D. `1011`
👉 **Đáp án đúng: C**
- **Giải thích:** `01111` có 1 `0`, 4 `1` ($n=0, m=3$).

**Câu 12.** Xét ngôn ngữ $L$ sinh bởi $G_{15}$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `011`
- B. `00111`
- C. `0001111`
- D. `0110`
👉 **Đáp án đúng: D**
- **Giải thích:** `0110` sai thứ tự vì có `0` đứng sau `1`.

**Câu 10.** Chuỗi nào có thể sinh từ ký hiệu bắt đầu $S$ của $G_{15}$?
- A. `01`
- B. `0011`
- C. `0111`
- D. `101`
👉 **Đáp án đúng: C**
- **Giải thích:** $S \Rightarrow 0A1 \Rightarrow 0(1A)1 \Rightarrow 0111$.

**Câu 11.** Chuỗi nào được sinh với **ÍT NHẤT 1 LẦN** dùng luật $S \to 0S1$?
- A. `011`
- B. `0111`
- C. `01111`
- D. `00111`
👉 **Đáp án đúng: D**
- **Giải thích:** Dùng ít nhất 1 lần $S \to 0S1$ sẽ sinh thêm một `0` nữa thành ít nhất **2 chữ `0`**, nên ngắn nhất là `00111`.

**Câu 13.** Chuỗi **NGẮN NHẤT** thuộc $L($G_{15}$)$ là:
- A. ``01``
- B. ``011``
- C. ``11``
- D. ``0``
👉 **Đáp án đúng: B**
- **Giải thích:** $n=0, m=1 \implies S \Rightarrow 0A1 \Rightarrow 011$ (độ dài 3).

**Câu 14.** Chuỗi **NGẮN NHÌ** thuộc $L($G_{15}$)$ (nếu cùng độ dài thì ưu tiên thứ tự từ điển tăng dần) là:
- A. ``0011``
- B. ``0111``
- C. ``00111``
- D. ``111``
👉 **Đáp án đúng: B**
- **Giải thích:** Chuỗi dài 4 duy nhất trong $L$ là `0111` ($n=0, m=2$).

**Câu 15.** Ba chuỗi ngắn nhất thuộc $L($G_{15}$)$ (xếp theo độ dài và thứ tự từ điển tăng dần) là:
- A. 01, 011, 0111
- B. 011, 0111, 00111
- C. 011, 0011, 00011
- D. 011, 00111, 0111
👉 **Đáp án đúng: B**
- **Giải thích:** Dài 3: `011`. Dài 4: `0111`. Dài 5 có `00111` ($n=1, m=1$) và `01111` ($n=0, m=3$); theo từ điển `0 < 1` nên `00111` đứng trước `01111`!

**Câu 16.** Chuỗi **thứ 4** theo độ dài tăng dần của $L($G_{15}$)$ (nếu cùng độ dài ưu tiên thứ tự từ điển từ trái sang phải) là:
- A. ``01111``
- B. ``00111``
- C. ``0001111``
- D. ``0111``
👉 **Đáp án đúng: A**
- **Giải thích:** Xếp hạng: (1) `011` (dài 3), (2) `0111` (dài 4), (3) `00111` (dài 5, chữ thứ 2 là `0`), (4) `01111` (dài 5, chữ thứ 2 là `1`).

**Câu 17.** Chuỗi ngắn nhất thuộc $L($G_{15}$)$ thỏa điều kiện **có ít nhất 2 chữ `0`** là:
- A. ``001``
- B. ``0011``
- C. ``00111``
- D. ``011``
👉 **Đáp án đúng: C**
- **Giải thích:** Có ít nhất 2 chữ `0` ($k=2$) thì số `1` phải $\ge 3 \implies$ ngắn nhất là `00111`.

**Câu 18.** Số lượng ký tự `1` trong mọi chuỗi hợp lệ thuộc $L(G_{15})$ thỏa mãn:
- A. Luôn bằng 1
- B. Luôn $\ge 2$
- C. Luôn bằng số chữ `0`
- D. Có thể bằng 0
👉 **Đáp án đúng: B**
- **Giải thích:** Vì $p = m + n + 1$ với $n \ge 0, m \ge 1$, nên nhỏ nhất là $p = 1 + 0 + 1 = 2$ (tức $\#1 \ge 2$).

**Câu 19.** Quan hệ giữa số lượng chữ `0` và `1` trong $L(G_{15})$ là:
- A. $\#1 = \#0$
- B. $\#1 = \#0 + 1$
- C. $\#1 \ge \#0 + 1$ (với $\#0 \ge 1$)
- D. $\#0 > \#1$
👉 **Đáp án đúng: C**
- **Giải thích:** Với $k$ chữ `0`, số chữ `1` là $k + m$ ($m \ge 1$) nên luôn lớn hơn số chữ `0` ít nhất 1.

**Câu 20.** Dạng tổng quát của ngôn ngữ $L(G_{15})$ là:
- A. $\{0^k 1^k \mid k \ge 1\}$
- B. $\{0^{n+1} 1^m 1^{n+1} \mid n \ge 0, m \ge 1\}$
- C. $\{0^n 1^m \mid n, m \ge 1\}$
- D. $\{0^n 1^{n+1} \mid n \ge 0\}$
👉 **Đáp án đúng: B**
- **Giải thích:** Thay $S \to 0S1$ lặp $n$ lần, rồi $S \to 0A1$, rồi $A \to 1^m$ ta thu đúng $0^{n+1} 1^m 1^{n+1}$.

**Câu 21.** Chuỗi `001111` có thuộc $L($G_{15}$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: A**
- **Giải thích:** Đúng, 2 `0` và 4 `1` ($4 \ge 2+1$).

**Câu 22.** Chuỗi `0011` có thuộc $L($G_{15}$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: B**
- **Giải thích:** Sai, 2 `0` và 2 `1` (không vượt quá số `0`).

**Câu 23.** Chuỗi `011` có thuộc $L($G_{15}$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: A**
- **Giải thích:** Đúng, $n=0, m=1$.

**Câu 24.** Chuỗi `000111` có thuộc $L($G_{15}$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: B**
- **Giải thích:** Sai, 3 `0` và 3 `1`.

**Câu 25.** (Câu hỏi Word) Phân loại Chomsky của $G_{15}$ là:
- A. Loại 3
- B. Loại 2 (Phi ngữ cảnh - CFG)
- C. Loại 1
- D. Loại 0
👉 **Đáp án đúng: B**
- **Giải thích:** Ràng buộc $\#1 > \#0$ cần bộ nhớ vô hạn của Stack (PDA) nên là Loại 2.

**Câu 26.** (Câu hỏi Word) Vì sao $G_{15}$ không phải ngôn ngữ chính quy?
- A. Vì có ký tự 0 và 1
- B. Vì DFA không kiểm tra được điều kiện $\#1 > \#0$ với số `0` lớn tùy ý
- C. Vì không có chuỗi rỗng
- D. Vì $A$ đệ quy phải
👉 **Đáp án đúng: B**
- **Giải thích:** Theo Bổ đề bơm cho ngôn ngữ chính quy, không thể so sánh số lượng `1` và `0` khi $n$ tăng vô hạn.

---

## VĂN PHẠM 16 ($G_{16}$): SỐ CHỮ `0` KHÁC SỐ CHỮ `1` ($\{0^i 1^j \mid i \ne j\}$)

> **ĐỀ BÀI GỐC ($G_{16}$):**
> $$
> G_{16} = \langle \{0, 1\},\ \{S, A, B\},\ S,\ \{S \to 0S1 \mid 0A \mid 1B \mid 0 \mid 1,\ A \to 0A \mid 0,\ B \to 1B \mid 1\} \rangle
> $$
> Với các quy tắc sinh: $S \to 0S1 \mid 0A \mid 1B \mid 0 \mid 1$, $A \to 0A \mid 0$, $B \to 1B \mid 1$

### Bản chất cốt lõi & Quy tắc vàng nhận diện trong 3 giây
1. **Dẫn xuất tổng quát:**
   - Lặp $S \to 0S1$ đúng $n$ lần ($n \ge 0$): $0^n S 1^n$ (lấy cặp cân bằng `0` và `1` làm vỏ bọc).
   - Sau đó thoát $S$ bằng 1 trong 4 nhánh phá cân bằng:
     + $S \to 0A \mid 0$: nhồi thêm **ít nhất 1 chữ `0`** ($0^+$) vào giữa $\implies 0^{n+k} 1^n$ ($\#0 > \#1$).
     + $S \to 1B \mid 1$: nhồi thêm **ít nhất 1 chữ `1`** ($1^+$) vào giữa $\implies 0^n 1^{n+k}$ ($\#1 > \#0$).
2. **Ba quy tắc vàng 3 giây:**
   - **Thứ tự:** Toàn bộ `0` đứng trước toàn bộ `1` (`1` không bao giờ đứng trước `0`).
   - **QUY TẮC SỐNG CÒN:** **Số chữ `0` BẮT BUỘC PHẢI KHÁC số chữ `1` ($\#0 \ne \#1$)!**
   - Mọi chuỗi có `#0 == #1` (như $\varepsilon$, `01`, `0011`, `000111`) ĐỀU BỊ LOẠI!

### Bộ 24 câu trắc nghiệm chuẩn Đề Mẫu Sample 1 (+ 2 câu lý thuyết Word)

**Câu 1.** Xét ngôn ngữ $L$ sinh bởi $G_{16}$. Chuỗi nào sau đây **thuộc** $L$?
- A. `01`
- B. `0`
- C. `0011`
- D. `10`
👉 **Đáp án đúng: B**
- **Giải thích:** `0` có $1$ chữ `0` và $0$ chữ `1` ($1 \ne 0$). `01`, `0011` có $\#0 = \#1$ nên bị loại!

**Câu 2.** Xét ngôn ngữ $L$ sinh bởi $G_{16}$. Chuỗi nào sau đây **thuộc** $L$?
- A. `01`
- B. `001`
- C. `10`
- D. `0011`
👉 **Đáp án đúng: B**
- **Giải thích:** `001` có 2 `0` và 1 `1` ($S \Rightarrow 0S1 \Rightarrow 001$).

**Câu 3.** Xét ngôn ngữ $L$ sinh bởi $G_{16}$. Chuỗi nào sau đây **thuộc** $L$?
- A. `0111`
- B. `0011`
- C. `110`
- D. `000111`
👉 **Đáp án đúng: A**
- **Giải thích:** `0111` có 1 `0` và 3 `1` ($S \Rightarrow 0S1 \Rightarrow 01B1 \Rightarrow 0111$).

**Câu 4.** Xét ngôn ngữ $L$ sinh bởi $G_{16}$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `0`
- B. `1`
- C. `001`
- D. `01`
👉 **Đáp án đúng: D**
- **Giải thích:** `01` có 1 `0` và 1 `1` ($\#0 = \#1$) nên KHÔNG thuộc $L$!

**Câu 5.** Xét ngôn ngữ $L$ sinh bởi $G_{16}$. Chuỗi nào sau đây **thuộc** $L$?
- A. `000111`
- B. `001111`
- C. `1100`
- D. `0101`
👉 **Đáp án đúng: B**
- **Giải thích:** `001111` ($2$ số `0`, $4$ số `1`, đúng thứ tự $0^*1^*$).

**Câu 6.** Xét ngôn ngữ $L$ sinh bởi $G_{16}$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `00`
- B. `11`
- C. `011`
- D. `0011`
👉 **Đáp án đúng: D**
- **Giải thích:** `0011` bị loại vì $\#0 = \#1 = 2$.

**Câu 7.** Xét ngôn ngữ $L$ sinh bởi $G_{16}$. Chuỗi nào sau đây **thuộc** $L$?
- A. `100`
- B. `000011`
- C. `000111`
- D. `010`
👉 **Đáp án đúng: B**
- **Giải thích:** `000011` ($4$ số `0`, $2$ số `1`, $S \Rightarrow^2 00S11 \Rightarrow 00(0A)11 \Rightarrow 000011$).

**Câu 8.** Xét ngôn ngữ $L$ sinh bởi $G_{16}$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `0`
- B. `1`
- C. `00011`
- D. `100`
👉 **Đáp án đúng: D**
- **Giải thích:** `100` có chữ `1` đứng trước chữ `0` (sai thứ tự $0^i 1^j$).

**Câu 9.** Xét ngôn ngữ $L$ sinh bởi $G_{16}$. Chuỗi nào sau đây **thuộc** $L$?
- A. $\varepsilon$
- B. `01`
- C. `00111`
- D. `110`
👉 **Đáp án đúng: C**
- **Giải thích:** `00111` có 2 `0`, 3 `1` ($2 \ne 3$).

**Câu 12.** Xét ngôn ngữ $L$ sinh bởi $G_{16}$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `00`
- B. `111`
- C. `0001`
- D. `000111`
👉 **Đáp án đúng: D**
- **Giải thích:** `000111` có 3 `0`, 3 `1` ($3=3$) nên KHÔNG thuộc $L$.

**Câu 10.** Chuỗi nào có thể sinh từ ký hiệu bắt đầu $S$ của $G_{16}$?
- A. `01`
- B. `0011`
- C. `10`
- D. Các lựa chọn khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** `01` và `0011` có `#0 = #1`; `10` sai thứ tự. Cả 3 đều không sinh được từ $S$.

**Câu 11.** Chuỗi nào được sinh với **ÍT NHẤT 1 LẦN** dùng luật $S \to 0S1$?
- A. `0`
- B. `00`
- C. `11`
- D. `001`
👉 **Đáp án đúng: D**
- **Giải thích:** Dùng $S \to 0S1$ ít nhất 1 lần thì chuỗi phải có cả `0` ở đầu và `1` ở cuối; chuỗi ngắn nhất là `001` (hoặc `011`).

**Câu 13.** Chuỗi **NGẮN NHẤT** thuộc $L($G_{16}$)$ là:
- A. $\varepsilon$
- B. ``0``
- C. ``01``
- D. ``00``
👉 **Đáp án đúng: B**
- **Giải thích:** Có 2 chuỗi dài 1 là `0` và `1`. Theo thứ tự từ điển (`0 < 1`), chuỗi đầu tiên là `0`.

**Câu 14.** Chuỗi **NGẮN NHÌ** thuộc $L($G_{16}$)$ (nếu cùng độ dài thì ưu tiên thứ tự từ điển tăng dần) là:
- A. ``0``
- B. ``1``
- C. ``00``
- D. ``01``
👉 **Đáp án đúng: B**
- **Giải thích:** Hai chuỗi ngắn nhất là `0` (dài 1, đầu) và `1` (dài 1, nhì).

**Câu 15.** Ba chuỗi ngắn nhất thuộc $L($G_{16}$)$ (xếp theo độ dài và thứ tự từ điển tăng dần) là:
- A. 0, 1, 01
- B. 0, 1, 00
- C. 0, 00, 000
- D. 01, 001, 011
👉 **Đáp án đúng: B**
- **Giải thích:** Dài 1: `0`, `1`. Dài 2 có `00`, `11` (`01` và `10` loại!), theo từ điển chọn `00` đứng trước `11`.

**Câu 16.** Chuỗi **thứ 4** theo độ dài tăng dần của $L($G_{16}$)$ (nếu cùng độ dài ưu tiên thứ tự từ điển từ trái sang phải) là:
- A. ``01``
- B. ``10``
- C. ``11``
- D. ``001``
👉 **Đáp án đúng: C**
- **Giải thích:** Thứ tự: (1) `0`, (2) `1`, (3) `00`, (4) `11`.

**Câu 17.** Chuỗi ngắn nhất thuộc $L($G_{16}$)$ thỏa điều kiện **có chứa CẢ chữ `0` lẫn chữ `1`** là:
- A. ``01``
- B. ``001``
- C. ``011``
- D. ``00``
👉 **Đáp án đúng: B**
- **Giải thích:** `01` không thuộc $L$. Với độ dài 3 chứa cả `0` và `1` có `001` và `011`; theo thứ tự từ điển `001` đứng trước `011`!

**Câu 18.** Chuỗi rỗng $\varepsilon$ có thuộc $L(G_{16})$ không?
- A. Có, khi $i=j=0$
- B. Không, vì mọi nhánh thoát của $S$ đều bắt buộc sinh ít nhất 1 ký tự `0` hoặc `1` (và $0=0$ không thỏa $i \ne j$)
- C. Có, vì có $S \to \varepsilon$
- D. Tùy trường hợp
👉 **Đáp án đúng: B**
- **Giải thích:** $G_{16}$ không có $S \to \varepsilon$, và với $\varepsilon$ thì $\#0 = \#1 = 0$.

**Câu 19.** Quan hệ giữa số lượng chữ `0` ($i$) và số lượng chữ `1` ($j$) trong $0^i 1^j \in L(G_{16})$ là:
- A. $i = j$
- B. $i \ne j$ (số `0` và số `1` khác nhau)
- C. $i > j$ luôn đúng
- D. $i < j$ luôn đúng
👉 **Đáp án đúng: B**
- **Giải thích:** Nhánh $0A/0$ làm $i > j$, nhánh $1B/1$ làm $i < j$, hợp lại thành $i \ne j$.

**Câu 20.** Dạng tổng quát của ngôn ngữ $L(G_{16})$ là:
- A. $\{0^i 1^j \mid i, j \ge 0\}$
- B. $\{0^i 1^j \mid i \ne j,\ i,j \ge 0\}$
- C. $\{0^i 1^i \mid i \ge 1\}$
- D. $\{0^i 1^j \mid i > j\}$
👉 **Đáp án đúng: B**
- **Giải thích:** Vì $i \ne j$ tự động loại trường hợp $i=j=0$ ($\varepsilon$), nên $\{0^i 1^j \mid i \ne j\}$ là biểu diễn chuẩn xác nhất.

**Câu 21.** Chuỗi `0011` có thuộc $L($G_{16}$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: B**
- **Giải thích:** Sai, vì $\#0 = \#1 = 2$.

**Câu 22.** Chuỗi `0111` có thuộc $L($G_{16}$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: A**
- **Giải thích:** Đúng, $1$ chữ `0` và $3$ chữ `1` ($1 \ne 3$).

**Câu 23.** Chuỗi `0000` có thuộc $L($G_{16}$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: A**
- **Giải thích:** Đúng, $4$ chữ `0` và $0$ chữ `1` ($4 \ne 0$, qua nhánh $S \to 0A$).

**Câu 24.** Chuỗi `10` có thuộc $L($G_{16}$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: B**
- **Giải thích:** Sai, `1` đứng trước `0`.

**Câu 25.** (Câu hỏi Word) Văn phạm $G_{16}$ thuộc loại mấy theo phân loại Chomsky?
- A. Loại 3
- B. Loại 2 (Phi ngữ cảnh - CFG)
- C. Loại 1
- D. Loại 0
👉 **Đáp án đúng: B**
- **Giải thích:** Ngôn ngữ $\{0^i 1^j \mid i \ne j\}$ là phi ngữ cảnh (CFG - Loại 2), cần PDA kiểm tra $i \ne j$.

**Câu 26.** (Câu hỏi Word) $G_{16}$ sinh phần bù của $0^n 1^n$ trong $0^*1^*$. Đúng hay sai?
- A. Đúng hoàn toàn
- B. Sai hoàn toàn
👉 **Đáp án đúng: A**
- **Giải thích:** Tập $0^*1^*$ trừ đi tập $0^n 1^n$ chính xác bằng $\{0^i 1^j \mid i \ne j\}$.

---
