# BỘ ĐỀ ÔN TẬP VĂN PHẠM PHẦN 2 (CHÍNH QUY & ĐẶC BIỆT): $G_3, G_4, G_7, G_8, G_{14}, G_{17}, G_{18}$ & $G_{19}$
## MỖI VĂN PHẠM FULL 24 CÂU CHUẨN ĐỀ MẪU SAMPLE 1 + CÂU CHOMSKY/RE/DFA TỪ WORD

> **QUY TẮC GỘP BÀI TỰA NHAU:**
> - **$G_7$** ($\{1^{2k} \mid k \ge 0\}$) đại diện luôn cho trường hợp đơn giản hơn là **$G_{13}$** ($\{c^n \mid n \ge 1\} = c^+$).
> - **$G_{19}$** ($P = \{S \to 0AB, A0 \to S0B, A1 \to SB1, B \to SA \mid 01\}$) được phân tích riêng ở cuối file vì chứng minh được bất biến $(\#S + \#A)$ luôn lẻ $\implies L(G_{19}) = \emptyset$.
> - File này gồm **7 văn phạm độc đáo**, mỗi văn phạm có **đầy đủ 26 câu hỏi trắc nghiệm** = **182 câu giải chi tiết 100%**.

---

## VĂN PHẠM 3 ($G_3$): BẪY CFG SINH NGÔN NGỮ CHÍNH QUY $a^+ b^+ c^+$

> **ĐỀ BÀI GỐC ($G_3$):**
> $$
> G_3 = \langle \{a, b, c\},\ \{S, A, B, C\},\ S,\ \{S \to ABC,\ A \to aA \mid a,\ B \to bB \mid b,\ C \to cC \mid c\} \rangle
> $$
> Với các quy tắc sinh: $S \to ABC$, $A \to aA \mid a$, $B \to bB \mid b$, $C \to cC \mid c$

### Bản chất cốt lõi & Quy tắc vàng nhận diện trong 3 giây
1. **Dẫn xuất tổng quát:**
   - $S \to ABC$ tách làm 3 khối độc lập nhau hoàn toàn: $A \Rightarrow a^+$, $B \Rightarrow b^+$, $C \Rightarrow c^+$.
   - Ghép lại: $\mathbf{L(G_3) = \{a^i b^j c^k \mid i, j, k \ge 1\} = a^+ b^+ c^+}$.
2. **Ba quy tắc vàng 3 giây & Bẫy thi cử:**
   - **Thứ tự:** Toàn bộ `a` $\to$ toàn bộ `b` $\to$ toàn bộ `c`. Mỗi loại có **ít nhất 1 chữ**!
   - **ĐỘC LẬP SỐ MŨ:** Số lượng `a`, `b`, `c` **KHÔNG CẦN BẰNG NHAU** (`aabccc`, `abbc` đều hợp lệ!).
   - **BẪY LÝ THUYẾT CHOMSKY:** Hình thức viết có $S \to ABC$ (dạng CFG), nhưng **ngôn ngữ sinh ra là Ngôn ngữ CHÍNH QUY (Loại 3)** vì biểu diễn được bằng RE $aa^* bb^* cc^* = a^+ b^+ c^+$!

### Bộ 24 câu trắc nghiệm chuẩn Đề Mẫu Sample 1 (+ 2 câu lý thuyết Word)

**Câu 1.** Xét ngôn ngữ $L$ sinh bởi $G_3$. Chuỗi nào sau đây **thuộc** $L$?
- A. `ab`
- B. `abc`
- C. `bc`
- D. `ac`
👉 **Đáp án đúng: B**
- **Giải thích:** `abc` = $a^1 b^1 c^1$. Các chuỗi kia thiếu mất `c`, `a`, hoặc `b`.

**Câu 2.** Xét ngôn ngữ $L$ sinh bởi $G_3$. Chuỗi nào sau đây **thuộc** $L$?
- A. `aabbc`
- B. `abbca`
- C. `cba`
- D. `aaabbb`
👉 **Đáp án đúng: A**
- **Giải thích:** `aabbc` = $a^2 b^2 c^1$. Trong $G_3$, số mũ $i, j, k$ hoàn toàn tự do từ 1 trở lên!

**Câu 3.** Xét ngôn ngữ $L$ sinh bởi $G_3$. Chuỗi nào sau đây **thuộc** $L$?
- A. `aabbcc`
- B. `acbb`
- C. `abccba`
- D. $\varepsilon$
👉 **Đáp án đúng: A**
- **Giải thích:** `aabbcc` = $a^2 b^2 c^2$.

**Câu 4.** Xét ngôn ngữ $L$ sinh bởi $G_3$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `abc`
- B. `aabc`
- C. `abbbc`
- D. `abccba`
👉 **Đáp án đúng: D**
- **Giải thích:** `abccba` có `b` và `a` đứng sau `c`, vi phạm thứ tự `a` $\to$ `b` $\to$ `c`.

**Câu 5.** Xét ngôn ngữ $L$ sinh bởi $G_3$. Chuỗi nào sau đây **thuộc** $L$?
- A. `abccc`
- B. `acccb`
- C. `bbbaac`
- D. `ccba`
👉 **Đáp án đúng: A**
- **Giải thích:** `abccc` = $a^1 b^1 c^3$.

**Câu 6.** Xét ngôn ngữ $L$ sinh bởi $G_3$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `abc`
- B. `aaabbc`
- C. `abccc`
- D. `aabba`
👉 **Đáp án đúng: D**
- **Giải thích:** `aabba` thiếu chữ `c` và có `a` nằm cuối.

**Câu 7.** Xét ngôn ngữ $L$ sinh bởi $G_3$. Chuỗi nào sau đây **thuộc** $L$?
- A. `aaabccc`
- B. `ababa`
- C. `cccaaabbb`
- D. `aabb`
👉 **Đáp án đúng: A**
- **Giải thích:** `aaabccc` = $a^3 b^1 c^3$.

**Câu 8.** Xét ngôn ngữ $L$ sinh bởi $G_3$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `abc`
- B. `aaab`
- C. `abbbccc`
- D. `aabccc`
👉 **Đáp án đúng: B**
- **Giải thích:** `aaab` thiếu hẳn khối $C$ (không có chữ `c`).

**Câu 9.** Xét ngôn ngữ $L$ sinh bởi $G_3$. Chuỗi nào sau đây **thuộc** $L$?
- A. `aaabbbccc`
- B. `acb`
- C. `bca`
- D. `aabccaa`
👉 **Đáp án đúng: A**
- **Giải thích:** `aaabbbccc` = $a^3 b^3 c^3$.

**Câu 12.** Xét ngôn ngữ $L$ sinh bởi $G_3$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `aabc`
- B. `abbc`
- C. `abcc`
- D. `bbcc`
👉 **Đáp án đúng: D**
- **Giải thích:** `bbcc` thiếu khối $A$ (không có chữ `a`).

**Câu 10.** Chuỗi nào có thể sinh từ ký hiệu bắt đầu $S$ của $G_3$?
- A. `ab`
- B. `ac`
- C. `aabcc`
- D. `bc`
👉 **Đáp án đúng: C**
- **Giải thích:** $S \Rightarrow ABC \Rightarrow aABC \Rightarrow aaBC \Rightarrow aabC \Rightarrow aabcC \Rightarrow aabcc$.

**Câu 11.** Chuỗi nào được sinh với **ÍT NHẤT 1 LẦN** dùng luật $A \to aA$, $B \to bB$, hoặc $C \to cC$ (lặp thêm ký tự)?
- A. `abc`
- B. `ab`
- C. `bc`
- D. `abbc`
👉 **Đáp án đúng: D**
- **Giải thích:** `abc` chỉ dùng đúng $A \to a, B \to b, C \to c$ (không lặp). Muốn dùng ít nhất 1 bước lặp, độ dài phải $\ge 4$, như `abbc`.

**Câu 13.** Chuỗi **NGẮN NHẤT** thuộc $L($G_3$)$ là:
- A. $\varepsilon$
- B. ``a``
- C. ``ab``
- D. ``abc``
👉 **Đáp án đúng: D**
- **Giải thích:** Mỗi biến $A, B, C$ sinh tối thiểu 1 ký tự nên chuỗi ngắn nhất là `abc` (độ dài 3).

**Câu 14.** Chuỗi **NGẮN NHÌ** thuộc $L($G_3$)$ (nếu cùng độ dài thì ưu tiên thứ tự từ điển tăng dần) là:
- A. ``aabc``
- B. ``abbc``
- C. ``abcc``
- D. ``aabb``
👉 **Đáp án đúng: A**
- **Giải thích:** Có 3 chuỗi dài 4 là `aabc`, `abbc`, `abcc`. Theo thứ tự từ điển (`a < b < c`), chuỗi đứng đầu là `aabc`!

**Câu 15.** Ba chuỗi ngắn nhất thuộc $L($G_3$)$ (xếp theo độ dài và thứ tự từ điển tăng dần) là:
- A. abc, aabc, abbc
- B. abc, abcc, aabc
- C. a, ab, abc
- D. abc, aabbcc, aaabbbccc
👉 **Đáp án đúng: A**
- **Giải thích:** Dài 3: `abc`. Dài 4 theo thứ tự từ điển: `aabc` rồi đến `abbc`.

**Câu 16.** Chuỗi **thứ 4** theo độ dài tăng dần của $L($G_3$)$ (nếu cùng độ dài ưu tiên thứ tự từ điển từ trái sang phải) là:
- A. ``abbc``
- B. ``abcc``
- C. ``aaabc``
- D. ``aabc``
👉 **Đáp án đúng: B**
- **Giải thích:** Xếp hạng (độ dài, từ điển): (1) `abc`, (2) `aabc`, (3) `abbc`, (4) `abcc`.

**Câu 17.** Chuỗi ngắn nhất thuộc $L($G_3$)$ thỏa điều kiện **có độ dài $\ge 4$** là:
- A. ``aabb``
- B. ``aabc``
- C. ``abc``
- D. ``abca``
👉 **Đáp án đúng: B**
- **Giải thích:** Chuỗi hợp lệ ngắn nhất dài $\ge 4$ theo thứ tự từ điển là `aabc` (dài 4).

**Câu 18.** Số lượng ký tự mỗi loại `a`, `b`, `c` trong chuỗi thuộc $L(G_3)$ là:
- A. Phải bằng nhau hết
- B. Đều $\ge 1$ và độc lập với nhau
- C. Luôn $\ge 2$
- D. Có thể bằng 0
👉 **Đáp án đúng: B**
- **Giải thích:** Các biến $A, B, C$ tách biệt hoàn toàn nên số lượng `a, b, c` tự do $\ge 1$.

**Câu 19.** Khẳng định nào ĐÚNG về quan hệ số lượng $i=\#a$, $j=\#b$, $k=\#c$ trong $L(G_3)$?
- A. $i = j = k$
- B. $i \ge 1, j \ge 1, k \ge 1$ (không ràng buộc bằng nhau)
- C. $i + j = k$
- D. $i < j < k$
👉 **Đáp án đúng: B**
- **Giải thích:** Khác với $G_4$ ($a^n b^n c^n$), $G_3$ chỉ yêu cầu mỗi chữ xuất hiện ít nhất 1 lần theo đúng thứ tự.

**Câu 20.** Biểu diễn chính xác ngôn ngữ $L(G_3)$ là:
- A. $\{a^n b^n c^n \mid n \ge 1\}$
- B. $a^+ b^+ c^+$ (tức $\{a^i b^j c^k \mid i, j, k \ge 1\}$)
- C. $(abc)^+$
- D. $a^* b^* c^*$
👉 **Đáp án đúng: B**
- **Giải thích:** $A \Rightarrow a^+$, $B \Rightarrow b^+$, $C \Rightarrow c^+$ ghép lại thành $a^+ b^+ c^+$.

**Câu 21.** Chuỗi `aabccc` có thuộc $L($G_3$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: A**
- **Giải thích:** Đúng, $a^2 b^1 c^3$ (đúng thứ tự, mỗi chữ $\ge 1$).

**Câu 22.** Chuỗi `aabbb` có thuộc $L($G_3$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: B**
- **Giải thích:** Sai, thiếu chữ `c`.

**Câu 23.** Chuỗi `abc` có thuộc $L($G_3$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: A**
- **Giải thích:** Đúng, $a^1 b^1 c^1$.

**Câu 24.** Chuỗi `aacbb` có thuộc $L($G_3$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: B**
- **Giải thích:** Sai, `c` đứng trước `b`.

**Câu 25.** (Câu hỏi Word - Bẫy cực hay) Ngôn ngữ $L(G_3)$ thuộc loại mấy theo phân loại Chomsky?
- A. Loại 2 (chỉ là CFG, không chính quy)
- B. Loại 3 (Ngôn ngữ chính quy - Regular)
- C. Loại 1
- D. Loại 0
👉 **Đáp án đúng: B**
- **Giải thích:** Tuy tập luật $G_3$ viết theo dạng CFG ($S \to ABC$), nhưng ngôn ngữ sinh ra là $a^+ b^+ c^+ = aa^*bb^*cc^*$ là một **Biểu thức chính quy**, nên $L(G_3)$ là Ngôn ngữ Chính quy (Loại 3)!

**Câu 26.** (Câu hỏi Word) Biểu thức chính quy (RE) tương đương với $L(G_3)$ là:
- A. $(a+b+c)^+$
- B. $aa^*bb^*cc^*$
- C. $a^*b^*c^*$
- D. $(abc)^*$
👉 **Đáp án đúng: B**
- **Giải thích:** $a^+ = aa^*$, $b^+ = bb^*$, $c^+ = cc^*$, ghép lại thành $aa^*bb^*cc^*$.

---

## VĂN PHẠM 4 ($G_4$): CẢM NGỮ CẢNH KINH ĐIỂN $\{a^n b^n c^n \mid n \ge 1\}$

> **ĐỀ BÀI GỐC ($G_4$):**
> $$
> G_4 = \langle \{a, b, c\},\ \{S, A, B, C\},\ S,\ P \rangle
> $$
> Với các quy tắc sinh: $S \to aSAC \mid abC$, $CA \to BA$, $BA \to BC$, $BC \to AC$, $bA \to bb$, $C \to c$

### Bản chất cốt lõi & Quy tắc vàng nhận diện trong 3 giây
1. **Cách hoạt động của bộ luật ngữ cảnh:**
   - $S \to aSAC$ lặp $n-1$ lần rồi dừng bằng $S \to abC$ tạo: $a^n b C (AC)^{n-1}$.
   - Ba luật $CA \to BA$, $BA \to BC$, $BC \to AC$ dùng để **đổi chỗ** $CA \Rightarrow BA \Rightarrow BC \Rightarrow AC$ (đẩy tất cả biến $A$ sang bên trái gặp $b$ để thành $bb$, dồn $C$ sang phải thành $cc...c$!).
   - Kết quả thu được: $\mathbf{L(G_4) = \{a^n b^n c^n \mid n \ge 1\}}$.
2. **Ba quy tắc vàng 3 giây:**
   - Thứ tự: toàn `a` $\to$ toàn `b` $\to$ toàn `c`.
   - **Số lượng CẢ 3 CHỮ PHẢI BẰNG NHAU HẾT**: $\#a = \#b = \#c \ge 1$.
   - **Loại Chomsky:** Vì vế trái có 2 ký hiệu ($CA, BA, BC, bA$) và không co rút ($|\alpha| \le |\beta|$), đây là **Văn phạm Cảm ngữ cảnh (Loại 1 - CSG)**!

### Bộ 24 câu trắc nghiệm chuẩn Đề Mẫu Sample 1 (+ 2 câu lý thuyết Word)

**Câu 1.** Xét ngôn ngữ $L$ sinh bởi $G_4$. Chuỗi nào sau đây **thuộc** $L$?
- A. `abc`
- B. `ab`
- C. `aabc`
- D. $\varepsilon$
👉 **Đáp án đúng: A**
- **Giải thích:** Với $n=1$: $S \Rightarrow abC \Rightarrow abc$.

**Câu 2.** Xét ngôn ngữ $L$ sinh bởi $G_4$. Chuỗi nào sau đây **thuộc** $L$?
- A. `aabbc`
- B. `aabbcc`
- C. `abbcc`
- D. `aabcc`
👉 **Đáp án đúng: B**
- **Giải thích:** `aabbcc` = $a^2 b^2 c^2$ ($n=2$). Các chuỗi kia không bằng nhau cả 3.

**Câu 3.** Xét ngôn ngữ $L$ sinh bởi $G_4$. Chuỗi nào sau đây **thuộc** $L$?
- A. `aaabbbccc`
- B. `aaabbbcc`
- C. `aabbbccc`
- D. `aaaabbbccc`
👉 **Đáp án đúng: A**
- **Giải thích:** `aaabbbccc` = $a^3 b^3 c^3$ ($n=3$).

**Câu 4.** Xét ngôn ngữ $L$ sinh bởi $G_4$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `abc`
- B. `aabbcc`
- C. `aaabbbccc`
- D. `aabbc`
👉 **Đáp án đúng: D**
- **Giải thích:** `aabbc` chỉ có 1 chữ `c` ($2, 2, 1$ không bằng nhau).

**Câu 5.** Xét ngôn ngữ $L$ sinh bởi $G_4$. Chuỗi nào sau đây **thuộc** $L$?
- A. `aaaabbbbcccc`
- B. `aaabbbbcccc`
- C. `aaaabbbcccc`
- D. `aaaabbbbccc`
👉 **Đáp án đúng: A**
- **Giải thích:** `aaaabbbbcccc` = $a^4 b^4 c^4$ ($n=4$).

**Câu 6.** Xét ngôn ngữ $L$ sinh bởi $G_4$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `abc`
- B. `aabbcc`
- C. `aaaabbbbcccc`
- D. `abcc`
👉 **Đáp án đúng: D**
- **Giải thích:** `abcc` có 1 `a`, 1 `b`, 2 `c` (lệch số `c`).

**Câu 7.** Xét ngôn ngữ $L$ sinh bởi $G_4$. Chuỗi nào sau đây **thuộc** $L$?
- A. `aaaaabbbbbccccc`
- B. `aaabbbcccbbb`
- C. `abcabc`
- D. `aaccbb`
👉 **Đáp án đúng: A**
- **Giải thích:** `aaaaabbbbbccccc` = $a^5 b^5 c^5$ ($n=5$).

**Câu 8.** Xét ngôn ngữ $L$ sinh bởi $G_4$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `abc`
- B. `aabbcc`
- C. `aaabbbccc`
- D. $\varepsilon$
👉 **Đáp án đúng: D**
- **Giải thích:** Chuỗi rỗng $\varepsilon$ KHÔNG thuộc $L(G_4)$ vì $n \ge 1$.

**Câu 9.** Xét ngôn ngữ $L$ sinh bởi $G_4$. Chuỗi nào sau đây **thuộc** $L$?
- A. `aacbbc`
- B. `bbccaa`
- C. `aabbcc`
- D. `abcab`
👉 **Đáp án đúng: C**
- **Giải thích:** `aabbcc` ($n=2$).

**Câu 12.** Xét ngôn ngữ $L$ sinh bởi $G_4$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `abc`
- B. `aabbcc`
- C. `aaabbbccc`
- D. `aaccbb`
👉 **Đáp án đúng: D**
- **Giải thích:** `aaccbb` sai thứ tự (`c` đứng trước `b`).

**Câu 10.** Chuỗi nào có thể sinh từ ký hiệu bắt đầu $S$ của $G_4$?
- A. `aabb`
- B. `aabbcc`
- C. `abcabc`
- D. $\varepsilon$
👉 **Đáp án đúng: B**
- **Giải thích:** Với $n=2$: $S \Rightarrow aSAC \Rightarrow a(abC)AC \Rightarrow aab(CA)C \Rightarrow^* aabbcc$.

**Câu 11.** Chuỗi nào được sinh với **ÍT NHẤT 1 LẦN** dùng luật $S \to aSAC$?
- A. `abc`
- B. `aabbcc`
- C. `aabc`
- D. `abcc`
👉 **Đáp án đúng: B**
- **Giải thích:** Dùng ít nhất 1 lần $S \to aSAC$ thì $n \ge 2$, nên chuỗi ngắn nhất là `aabbcc` (dài 6).

**Câu 13.** Chuỗi **NGẮN NHẤT** thuộc $L($G_4$)$ là:
- A. $\varepsilon$
- B. ``ab``
- C. ``abc``
- D. ``aabbcc``
👉 **Đáp án đúng: C**
- **Giải thích:** Chuỗi ngắn nhất ứng với $n=1$ là `abc` (độ dài 3).

**Câu 14.** Chuỗi **NGẮN NHÌ** thuộc $L($G_4$)$ (nếu cùng độ dài thì ưu tiên thứ tự từ điển tăng dần) là:
- A. ``aabc``
- B. ``aabb``
- C. ``aabbcc``
- D. ``abcc``
👉 **Đáp án đúng: C**
- **Giải thích:** Không có chuỗi dài 4 hay 5 nào có 3 chữ bằng nhau! Chuỗi ngắn nhì là `aabbcc` ($n=2$, dài 6).

**Câu 15.** Ba chuỗi ngắn nhất thuộc $L($G_4$)$ (xếp theo độ dài và thứ tự từ điển tăng dần) là:
- A. abc, aabc, abcc
- B. abc, aabbcc, aaabbbccc
- C. abc, abcabc, abcabcabc
- D. aabbcc, aaabbbccc, aaaabbbbcccc
👉 **Đáp án đúng: B**
- **Giải thích:** Lần lượt ứng với $n=1, 2, 3$: `abc` (3), `aabbcc` (6), `aaabbbccc` (9).

**Câu 16.** Chuỗi **thứ 4** theo độ dài tăng dần của $L($G_4$)$ (nếu cùng độ dài ưu tiên thứ tự từ điển từ trái sang phải) là:
- A. ``aaabbbccc``
- B. ``aaaabbbbcccc``
- C. ``aabbcc``
- D. ``aaaabbbccc``
👉 **Đáp án đúng: B**
- **Giải thích:** Chuỗi thứ 4 ứng với $n=4$: `aaaabbbbcccc` (độ dài 12).

**Câu 17.** Chuỗi ngắn nhất thuộc $L($G_4$)$ thỏa điều kiện **có độ dài $\ge 6$** là:
- A. ``aabb``
- B. ``aabbc``
- C. ``aabbcc``
- D. ``abcc``
👉 **Đáp án đúng: C**
- **Giải thích:** Chuỗi hợp lệ đầu tiên có độ dài $\ge 6$ là `aabbcc` (độ dài 6).

**Câu 18.** Độ dài của mọi chuỗi thuộc $L(G_4)$ luôn chia hết cho số nào?
- A. `2`
- B. 3 (luôn bằng $3n$ với $n \ge 1$)
- C. `4`
- D. `5`
👉 **Đáp án đúng: B**
- **Giải thích:** Mỗi chuỗi $a^n b^n c^n$ có tổng độ dài $n + n + n = 3n$, luôn là bội số dương của 3.

**Câu 19.** Quan hệ giữa số lượng `a`, `b`, `c` trong $L(G_4)$ là:
- A. $\#a = \#b = \#c \ge 1$
- B. Độc lập hoàn toàn
- C. $\#a + \#b = \#c$
- D. $\#a = \#b + 1$
👉 **Đáp án đúng: A**
- **Giải thích:** Cả 3 ký tự phải có số lượng bằng hệt nhau và ít nhất bằng 1.

**Câu 20.** Dạng tổng quát của ngôn ngữ $L(G_4)$ là:
- A. $\{a^n b^n c^n \mid n \ge 0\}$
- B. $\{a^n b^n c^n \mid n \ge 1\}$
- C. $a^+ b^+ c^+$
- D. $(abc)^+$
👉 **Đáp án đúng: B**
- **Giải thích:** Nhánh dừng là $S \to abC$ nên không sinh $\varepsilon$, kết quả là $\{a^n b^n c^n \mid n \ge 1\}$.

**Câu 21.** Chuỗi `aabbcc` có thuộc $L($G_4$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: A**
- **Giải thích:** Đúng, $n=2$.

**Câu 22.** Chuỗi `aabbc` có thuộc $L($G_4$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: B**
- **Giải thích:** Sai, thiếu 1 chữ `c`.

**Câu 23.** Chuỗi `abc` có thuộc $L($G_4$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: A**
- **Giải thích:** Đúng, $n=1$.

**Câu 24.** Chuỗi `aabcc` có thuộc $L($G_4$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: B**
- **Giải thích:** Sai, thiếu 1 chữ `b`.

**Câu 25.** (Câu hỏi Word) Văn phạm $G_4$ thuộc loại mấy theo phân loại Chomsky?
- A. Loại 3 (Chính quy)
- B. Loại 2 (Phi ngữ cảnh)
- C. Loại 1 (Cảm ngữ cảnh - CSG)
- D. Không có lời giải
👉 **Đáp án đúng: C**
- **Giải thích:** Vì các luật $CA \to BA, BA \to BC, BC \to AC, bA \to bb$ có vế trái gồm 2 ký hiệu và $|\alpha| \le |\beta|$, nên $G_4$ là Văn phạm Cảm ngữ cảnh (Loại 1)!

**Câu 26.** (Câu hỏi Word) Cỗ máy tối thiểu đoán nhận được ngôn ngữ $\{a^n b^n c^n \mid n \ge 1\}$ là:
- A. `DFA`
- B. PDA (1 ngăn xếp)
- C. LBA (Otomat giới hạn tuyến tính)
- D. Chỉ NFA làm được
👉 **Đáp án đúng: C**
- **Giải thích:** Ngôn ngữ Loại 1 (Cảm ngữ cảnh) không thể đoán nhận bởi PDA 1 stack mà phải dùng LBA.

---

## VĂN PHẠM 7 ($G_7$): VĂN PHẠM CHÍNH QUY MỘT KÝ TỰ $\{1^{2k} \mid k \ge 0\}$

> **LƯU Ý GỘP DẠNG TỰA NHAU:** Kèm luôn trường hợp đơn giản hơn là **$G_{13} = \langle \{c\}, \{S\}, S, \{S \to cS \mid c\} \rangle$**: chỉ sinh $\{c^n \mid n \ge 1\} = c^+$ (độ dài bất kỳ $\ge 1$, không có $\varepsilon$).

> **ĐỀ BÀI GỐC ($G_7$):**
> $$
> G_7 = \langle \{1\},\ \{S, A, B\},\ S,\ \{S \to \varepsilon \mid 1A,\ A \to 1B \mid 1,\ B \to 1A\} \rangle
> $$
> Với các quy tắc sinh: $S \to \varepsilon \mid 1A$, $A \to 1B \mid 1$, $B \to 1A$

### Bản chất cốt lõi & Quy tắc vàng nhận diện trong 3 giây
1. **Dẫn xuất tổng quát:**
   - Nhánh 1: $S \to \varepsilon$ (0 chữ `1`).
   - Nhánh 2: $S \to 1A$:
     + Nếu dừng ngay $A \to 1$ $\implies$ `11` (2 chữ `1`).
     + Nếu lặp vòng $A \to 1B \to 1(1A)$ thêm đúng **2 chữ `1`**, lặp $k-1$ lần rồi đóng bằng $A \to 1$ $\implies 1^{2k}$.
   - Kết quả: $\mathbf{L(G_7) = \{1^{2k} \mid k \ge 0\} = \{\varepsilon, 11, 1111, 111111, \dots\}}$.
2. **Quy tắc vàng 3 giây:**
   - Chỉ toàn ký tự `1`.
   - **Độ dài (số lượng chữ `1`) BẮT BUỘC LÀ SỐ CHẴN** (0, 2, 4, 6, 8, ...). Mọi chuỗi có độ dài lẻ ĐỀU BỊ LOẠI!

### Bộ 24 câu trắc nghiệm chuẩn Đề Mẫu Sample 1 (+ 2 câu lý thuyết Word)

**Câu 1.** Xét ngôn ngữ $L$ sinh bởi $G_7$. Chuỗi nào sau đây **thuộc** $L$?
- A. `1`
- B. `11`
- C. `111`
- D. `00`
👉 **Đáp án đúng: B**
- **Giải thích:** `11` có 2 chữ `1` (chẵn). `00` sai bảng chữ cái.

**Câu 2.** Xét ngôn ngữ $L$ sinh bởi $G_7$. Chuỗi nào sau đây **thuộc** $L$?
- A. `111`
- B. `1111`
- C. `11111`
- D. `1010`
👉 **Đáp án đúng: B**
- **Giải thích:** `1111` có 4 chữ `1` (chẵn).

**Câu 3.** Xét ngôn ngữ $L$ sinh bởi $G_7$. Chuỗi nào sau đây **thuộc** $L$?
- A. `11111`
- B. `111111`
- C. `1111111`
- D. `111`
👉 **Đáp án đúng: B**
- **Giải thích:** `111111` có 6 chữ `1` (chẵn).

**Câu 4.** Xét ngôn ngữ $L$ sinh bởi $G_7$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. $\varepsilon$
- B. `11`
- C. `1111`
- D. `111`
👉 **Đáp án đúng: D**
- **Giải thích:** `111` có 3 chữ `1` (số lẻ!) nên KHÔNG thuộc $L$.

**Câu 5.** Xét ngôn ngữ $L$ sinh bởi $G_7$. Chuỗi nào sau đây **thuộc** $L$?
- A. `1111111`
- B. `11111111`
- C. `11111`
- D. `1`
👉 **Đáp án đúng: B**
- **Giải thích:** `11111111` có 8 chữ `1` (chẵn).

**Câu 6.** Xét ngôn ngữ $L$ sinh bởi $G_7$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. $\varepsilon$
- B. `11`
- C. `111111`
- D. `1`
👉 **Đáp án đúng: D**
- **Giải thích:** `1` có 1 chữ `1` (số lẻ!).

**Câu 7.** Xét ngôn ngữ $L$ sinh bởi $G_7$. Chuỗi nào sau đây **thuộc** $L$?
- A. $\varepsilon$
- B. `1`
- C. `111`
- D. `11111`
👉 **Đáp án đúng: A**
- **Giải thích:** Do $S \to \varepsilon$, chuỗi rỗng (0 chữ `1`) hợp lệ.

**Câu 8.** Xét ngôn ngữ $L$ sinh bởi $G_7$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `11`
- B. `1111`
- C. `111111`
- D. `11111`
👉 **Đáp án đúng: D**
- **Giải thích:** `11111` có 5 chữ `1` (số lẻ!).

**Câu 9.** Xét ngôn ngữ $L$ sinh bởi $G_7$. Chuỗi nào sau đây **thuộc** $L$?
- A. `1111111111`
- B. `111111111`
- C. `111`
- D. `10`
👉 **Đáp án đúng: A**
- **Giải thích:** `1111111111` có 10 chữ `1` (chẵn).

**Câu 12.** Xét ngôn ngữ $L$ sinh bởi $G_7$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. $\varepsilon$
- B. `11`
- C. `1111`
- D. `1111111`
👉 **Đáp án đúng: D**
- **Giải thích:** `1111111` có 7 chữ `1` (lẻ).

**Câu 10.** Chuỗi nào có thể sinh từ ký hiệu bắt đầu $S$ của $G_7$?
- A. `1`
- B. `111`
- C. `1111`
- D. `01`
👉 **Đáp án đúng: C**
- **Giải thích:** $S \Rightarrow 1A \Rightarrow 1(1B) \Rightarrow 11(1A) \Rightarrow 1111$.

**Câu 11.** Chuỗi nào được sinh với **ÍT NHẤT 1 LẦN** dùng luật $A \to 1B$ (quay vòng chẵn thêm 2 số `1`)?
- A. $\varepsilon$
- B. `11`
- C. `1111`
- D. `111`
👉 **Đáp án đúng: C**
- **Giải thích:** Không dùng $A \to 1B$ thì chỉ sinh $\varepsilon$ hoặc `11`. Dùng ít nhất 1 lần $A \to 1B$ sinh ít nhất 4 chữ `1` (`1111`).

**Câu 13.** Chuỗi **NGẮN NHẤT** thuộc $L($G_7$)$ là:
- A. $\varepsilon$
- B. ``1``
- C. ``11``
- D. ``111``
👉 **Đáp án đúng: A**
- **Giải thích:** Nhờ luật $S \to \varepsilon$, chuỗi ngắn nhất là $\varepsilon$.

**Câu 14.** Chuỗi **NGẮN NHÌ** thuộc $L($G_7$)$ (nếu cùng độ dài thì ưu tiên thứ tự từ điển tăng dần) là:
- A. ``1``
- B. ``11``
- C. ``111``
- D. ``1111``
👉 **Đáp án đúng: B**
- **Giải thích:** Sau $\varepsilon$ (dài 0), chuỗi ngắn nhì là `11` (dài 2).

**Câu 15.** Ba chuỗi ngắn nhất thuộc $L($G_7$)$ (xếp theo độ dài và thứ tự từ điển tăng dần) là:
- A. 1, 11, 111
- B. $\varepsilon$, 1, 11
- C. $\varepsilon$, 11, 1111
- D. 11, 1111, 111111
👉 **Đáp án đúng: C**
- **Giải thích:** Ba chuỗi ngắn nhất lần lượt dài $0, 2, 4$: $\varepsilon$, `11`, `1111`.

**Câu 16.** Chuỗi **thứ 4** theo độ dài tăng dần của $L($G_7$)$ (nếu cùng độ dài ưu tiên thứ tự từ điển từ trái sang phải) là:
- A. ``1111``
- B. ``11111``
- C. ``111111``
- D. ``11111111``
👉 **Đáp án đúng: C**
- **Giải thích:** Chuỗi 1: $\varepsilon$ (0), chuỗi 2: `11` (2), chuỗi 3: `1111` (4), chuỗi 4: `111111` (6).

**Câu 17.** Chuỗi ngắn nhất thuộc $L($G_7$)$ thỏa điều kiện **khác rỗng ($\ne \varepsilon$)** là:
- A. ``1``
- B. ``11``
- C. ``111``
- D. ``1111``
👉 **Đáp án đúng: B**
- **Giải thích:** Chuỗi khác rỗng ngắn nhất là `11` (dài 2).

**Câu 18.** Số lượng chữ `1` trong mọi chuỗi hợp lệ thuộc $L(G_7)$ là:
- A. Luôn lẻ
- B. Luôn chẵn ($0, 2, 4, \dots$)
- C. Luôn $\ge 2$
- D. Chia hết cho 3
👉 **Đáp án đúng: B**
- **Giải thích:** Mỗi lần đi qua vòng $A \to 1B \to 11A$ cộng thêm 2 chữ `1`, kết hợp `S -> ε` tạo số chẵn.

**Câu 19.** Điều kiện chia hết của độ dài chuỗi $w \in L(G_7)$ là:
- A. $|w| \equiv 1 \pmod 2$
- B. $|w| \equiv 0 \pmod 2$ (chia hết cho 2)
- C. $|w| \equiv 0 \pmod 3$
- D. $|w| \ge 1$
👉 **Đáp án đúng: B**
- **Giải thích:** Mọi chuỗi hợp lệ đều có độ dài chẵn $|w| = 2k$.

**Câu 20.** Dạng tổng quát của ngôn ngữ $L(G_7)$ là:
- A. $\{1^{2k} \mid k \ge 1\}$
- B. $\{1^{2k} \mid k \ge 0\}$
- C. $\{1^{2k+1} \mid k \ge 0\}$
- D. $\{1^k \mid k \ge 0\}$
👉 **Đáp án đúng: B**
- **Giải thích:** Vì có chuỗi rỗng $\varepsilon = 1^0$ nên $k \ge 0$.

**Câu 21.** Chuỗi `1111` có thuộc $L($G_7$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: A**
- **Giải thích:** Đúng, 4 chữ `1` (chẵn).

**Câu 22.** Chuỗi `111` có thuộc $L($G_7$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: B**
- **Giải thích:** Sai, 3 chữ `1` (lẻ).

**Câu 23.** Chuỗi $\varepsilon$ có thuộc $L($G_7$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: A**
- **Giải thích:** Đúng, 0 chữ `1` (chẵn).

**Câu 24.** Chuỗi `1` có thuộc $L($G_7$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: B**
- **Giải thích:** Sai, 1 chữ `1` (lẻ).

**Câu 25.** (Câu hỏi Word) Văn phạm $G_7$ thuộc loại mấy và biểu thức chính quy (RE) tương đương là gì?
- A. Loại 2; không có RE
- B. Loại 3 (Chính quy); RE = $(11)^*$
- C. Loại 3 (Chính quy); RE = $1^*$
- D. Loại 1; RE = $1(11)^*$
👉 **Đáp án đúng: B**
- **Giải thích:** Mọi luật đều có dạng tuyến tính phải ($X \to aY \mid a \mid \varepsilon$), thuộc Loại 3 (Chính quy), với RE là $(11)^*$.

**Câu 26.** (Câu hỏi Word) DFA tối thiểu đoán nhận $L(G_7)$ có bao nhiêu trạng thái?
- A. 1 trạng thái
- B. 2 trạng thái (Chẵn/Lẻ)
- C. 3 trạng thái
- D. 4 trạng thái
👉 **Đáp án đúng: B**
- **Giải thích:** Chỉ cần 2 trạng thái: $q_0$ (Chẵn - đầu & kết thúc) và $q_1$ (Lẻ), đọc `1` đảo qua lại giữa $q_0$ và $q_1$.

---

## VĂN PHẠM 8 ($G_8$): CHÍNH QUY ĐẦU `0` ĐUÔI `0` ($0(0+1)^* 0$)

> **ĐỀ BÀI GỐC ($G_8$):**
> $$
> G_8 = \langle \{0, 1\},\ \{S, A\},\ S,\ \{S \to 0A,\ A \to 0A \mid 1A \mid 0\} \rangle
> $$
> Với các quy tắc sinh: $S \to 0A$, $A \to 0A \mid 1A \mid 0$

### Bản chất cốt lõi & Quy tắc vàng nhận diện trong 3 giây
1. **Dẫn xuất tổng quát:**
   - $S \to 0A$: ép ký tự **đầu tiên bắt buộc là `0`**.
   - $A \to 0A \mid 1A$: lặp đoạn giữa bất kỳ chuỗi nhị phân $(0+1)^*$.
   - $A \to 0$: ép ký tự **cuối cùng bắt buộc là `0`**.
   - Ghép lại: $\mathbf{L(G_8) = 0(0+1)^* 0}$.
2. **Ba quy tắc vàng 3 giây:**
   - **Bắt đầu bằng `0`** và **kết thúc bằng `0`**.
   - **Độ dài tối thiểu phải $\ge 2$** (vì `0` đầu và `0` cuối là 2 vị trí riêng biệt!). Chuỗi `0` độ dài 1 bị LOẠI!
   - Ở giữa muốn chứa bao nhiêu `0`, `1` cũng được.

### Bộ 24 câu trắc nghiệm chuẩn Đề Mẫu Sample 1 (+ 2 câu lý thuyết Word)

**Câu 1.** Xét ngôn ngữ $L$ sinh bởi $G_8$. Chuỗi nào sau đây **thuộc** $L$?
- A. `0`
- B. `01`
- C. `00`
- D. `10`
👉 **Đáp án đúng: C**
- **Giải thích:** `00` dài 2, bắt đầu và kết thúc đều bằng `0` ($S \Rightarrow 0A \Rightarrow 00$).

**Câu 2.** Xét ngôn ngữ $L$ sinh bởi $G_8$. Chuỗi nào sau đây **thuộc** $L$?
- A. `010`
- B. `011`
- C. `100`
- D. `0`
👉 **Đáp án đúng: A**
- **Giải thích:** `010` bắt đầu `0`, kết thúc `0`, ở giữa là `1`.

**Câu 3.** Xét ngôn ngữ $L$ sinh bởi $G_8$. Chuỗi nào sau đây **thuộc** $L$?
- A. `0010`
- B. `1000`
- C. `0101`
- D. `0001`
👉 **Đáp án đúng: A**
- **Giải thích:** `0010` bắt đầu `0`, kết thúc `0`.

**Câu 4.** Xét ngôn ngữ $L$ sinh bởi $G_8$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `00`
- B. `010`
- C. `000`
- D. `0`
👉 **Đáp án đúng: D**
- **Giải thích:** `0` chỉ có độ dài 1 (không đủ cả đầu `0` và đuôi `0` do $S \to 0A$ bắt buộc đi tiếp sang $A \to \dots 0$).

**Câu 5.** Xét ngôn ngữ $L$ sinh bởi $G_8$. Chuỗi nào sau đây **thuộc** $L$?
- A. `01110`
- B. `11100`
- C. `01111`
- D. `10101`
👉 **Đáp án đúng: A**
- **Giải thích:** `01110` bắt đầu `0`, kết thúc `0`.

**Câu 6.** Xét ngôn ngữ $L$ sinh bởi $G_8$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `00`
- B. `000`
- C. `0110`
- D. `001`
👉 **Đáp án đúng: D**
- **Giải thích:** `001` kết thúc bằng `1` (loại).

**Câu 7.** Xét ngôn ngữ $L$ sinh bởi $G_8$. Chuỗi nào sau đây **thuộc** $L$?
- A. `1010`
- B. `01010`
- C. `00001`
- D. `1110`
👉 **Đáp án đúng: B**
- **Giải thích:** `01010` có đầu `0`, đuôi `0`.

**Câu 8.** Xét ngôn ngữ $L$ sinh bởi $G_8$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `00`
- B. `010`
- C. `01110`
- D. `100`
👉 **Đáp án đúng: D**
- **Giải thích:** `100` bắt đầu bằng `1` (loại).

**Câu 9.** Xét ngôn ngữ $L$ sinh bởi $G_8$. Chuỗi nào sau đây **thuộc** $L$?
- A. `0110110`
- B. `1001`
- C. `0011`
- D. `1100`
👉 **Đáp án đúng: A**
- **Giải thích:** `0110110` bắt đầu `0` và kết thúc `0`.

**Câu 12.** Xét ngôn ngữ $L$ sinh bởi $G_8$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `000`
- B. `010`
- C. `0110`
- D. $\varepsilon$
👉 **Đáp án đúng: D**
- **Giải thích:** $\varepsilon$ không có độ dài $\ge 2$ nên không thuộc $L$.

**Câu 10.** Chuỗi nào có thể sinh từ ký hiệu bắt đầu $S$ của $G_8$?
- A. `0`
- B. `01`
- C. `100`
- D. `0010`
👉 **Đáp án đúng: D**
- **Giải thích:** $S \Rightarrow 0A \Rightarrow 00A \Rightarrow 001A \Rightarrow 0010$.

**Câu 11.** Chuỗi nào được sinh với **ÍT NHẤT 1 LẦN** dùng luật $A \to 0A$ hoặc $A \to 1A$?
- A. `0`
- B. `00`
- C. `010`
- D. `100`
👉 **Đáp án đúng: C**
- **Giải thích:** Không lặp $A$ thì chỉ được `00` (dài 2). Dùng ít nhất 1 bước lặp tạo chuỗi dài $\ge 3$, ngắn nhất là `000` hoặc `010`.

**Câu 13.** Chuỗi **NGẮN NHẤT** thuộc $L($G_8$)$ là:
- A. $\varepsilon$
- B. ``0``
- C. ``00``
- D. ``010``
👉 **Đáp án đúng: C**
- **Giải thích:** Chuỗi ngắn nhất: $S \Rightarrow 0A \Rightarrow 00$ (độ dài 2).

**Câu 14.** Chuỗi **NGẮN NHÌ** thuộc $L($G_8$)$ (nếu cùng độ dài thì ưu tiên thứ tự từ điển tăng dần) là:
- A. ``00``
- B. ``000``
- C. ``010``
- D. ``001``
👉 **Đáp án đúng: B**
- **Giải thích:** Có 2 chuỗi dài 3 là `000` và `010`. Theo từ điển `0 < 1`, `000` đứng trước nên là chuỗi ngắn nhì.

**Câu 15.** Ba chuỗi ngắn nhất thuộc $L($G_8$)$ (xếp theo độ dài và thứ tự từ điển tăng dần) là:
- A. 0, 00, 000
- B. 00, 000, 010
- C. 00, 010, 000
- D. 00, 01, 000
👉 **Đáp án đúng: B**
- **Giải thích:** Dài 2: `00`. Dài 3 theo thứ tự từ điển: `000` rồi đến `010`.

**Câu 16.** Chuỗi **thứ 4** theo độ dài tăng dần của $L($G_8$)$ (nếu cùng độ dài ưu tiên thứ tự từ điển từ trái sang phải) là:
- A. ``010``
- B. ``0000``
- C. ``000``
- D. ``0010``
👉 **Đáp án đúng: B**
- **Giải thích:** Xếp hạng: (1) `00` (2), (2) `000` (3), (3) `010` (3), (4) `0000` (4 - nhỏ nhất nhóm độ dài 4!).

**Câu 17.** Chuỗi ngắn nhất thuộc $L($G_8$)$ thỏa điều kiện **có chứa ít nhất 1 chữ `1`** là:
- A. ``01``
- B. ``010``
- C. ``100``
- D. ``0010``
👉 **Đáp án đúng: B**
- **Giải thích:** Chuỗi ngắn nhất chứa `1` và có đầu `0`, đuôi `0` là `010` (dài 3).

**Câu 18.** Độ dài tối thiểu của một chuỗi hợp lệ thuộc $L(G_8)$ là:
- A. `0`
- B. `1`
- C. `2`
- D. `3`
👉 **Đáp án đúng: C**
- **Giải thích:** Phải có ít nhất 1 số `0` từ $S \to 0A$ và 1 số `0` kết thúc từ $A \to 0$, nên $|w| \ge 2$.

**Câu 19.** Điều kiện nhận biết ngay một chuỗi nhị phân $w$ thuộc $L(G_8)$ là:
- A. Số lượng `0` bằng số lượng `1`
- B. Bắt đầu bằng `0`, kết thúc bằng `0`, độ dài $\ge 2$
- C. Chứa `00` ở bất kỳ đâu
- D. Chỉ gồm toàn `0`
👉 **Đáp án đúng: B**
- **Giải thích:** Đầu cố định `0`, giữa tự do `(0+1)*`, đuôi cố định `0`.

**Câu 20.** Biểu thức chính quy (RE) tương đương với $L(G_8)$ là:
- A. $0^*(0+1)^*0^*$
- B. $0(0+1)^*0$
- C. $0 + 0(0+1)^*0$
- D. $(0+1)^*0$
👉 **Đáp án đúng: B**
- **Giải thích:** Bắt buộc có `0` đầu và `0` cuối nên là $0(0+1)^*0$ (lưu ý `0` đứng một mình KHÔNG thuộc $L$!).

**Câu 21.** Chuỗi `0110` có thuộc $L($G_8$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: A**
- **Giải thích:** Đúng, đầu `0`, đuôi `0`, dài $4 \ge 2$.

**Câu 22.** Chuỗi `0` có thuộc $L($G_8$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: B**
- **Giải thích:** Sai, độ dài chỉ là 1.

**Câu 23.** Chuỗi `0000` có thuộc $L($G_8$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: A**
- **Giải thích:** Đúng, đầu `0`, đuôi `0`.

**Câu 24.** Chuỗi `0111` có thuộc $L($G_8$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: B**
- **Giải thích:** Sai, kết thúc bằng `1`.

**Câu 25.** (Câu hỏi Word) Văn phạm $G_8$ thuộc loại mấy theo phân loại Chomsky?
- A. Loại 3 (Chính quy - Tuyến tính phải)
- B. Loại 2
- C. Loại 1
- D. Loại 0
👉 **Đáp án đúng: A**
- **Giải thích:** Mọi quy tắc sinh đều có vế phải dạng $aB$ hoặc $a$ ($S \to 0A, A \to 0A \mid 1A \mid 0$) nên chuẩn Loại 3!

**Câu 26.** (Câu hỏi Word) DFA hoàn chỉnh tối thiểu đoán nhận $L(G_8)$ (tính cả trạng thái bẫy chết nếu mở đầu bằng `1`) có bao nhiêu trạng thái?
- A. 2 trạng thái
- B. 3 trạng thái
- C. 4 trạng thái (Đầu, Đang đọc, Kết thúc, Bẫy)
- D. 5 trạng thái
👉 **Đáp án đúng: C**
- **Giải thích:** Gồm: $q_0$ (ban đầu), $q_1$ (đã đọc `0` đầu, đang đọc giữa), $q_2$ (vừa đọc `0` ở cuối - kết thúc), và $q_{\text{bẫy}}$ (khi đọc `1` ngay từ đầu). (Nếu bỏ trạng thái bẫy thì chỉ có 3 trạng thái).

---

## VĂN PHẠM 14 ($G_{14}$): NGÔN NGỮ HỮU HẠN 4 TỪ ($\{0, 01, 011, 0111\}$)

> **ĐỀ BÀI GỐC ($G_{14}$):**
> $$
> G_{14} = \langle \{0, 1\},\ \{S, A, B, C\},\ S,\ \{S \to 0 \mid 0A,\ A \to 1 \mid 1B,\ B \to 1 \mid 1C,\ C \to 1\} \rangle
> $$
> Với các quy tắc sinh: $S \to 0 \mid 0A$, $A \to 1 \mid 1B$, $B \to 1 \mid 1C$, $C \to 1$

### Bản chất cốt lõi & Quy tắc vàng nhận diện trong 3 giây
1. **Dẫn xuất toàn bộ (chỉ có đúng 4 đường, KHÔNG có vòng lặp!):**
   - Nhánh 1: $S \to 0 \implies$ **`0`**
   - Nhánh 2: $S \to 0A \to 0(1) \implies$ **`01`**
   - Nhánh 3: $S \to 0A \to 01B \to 01(1) \implies$ **`011`**
   - Nhánh 4: $S \to 0A \to 01B \to 011C \to 011(1) \implies$ **`0111`**
2. **Quy tắc vàng 3 giây:**
   - **Ngôn ngữ HỮU HẠN** chỉ gồm đúng **4 chuỗi duy nhất**: $\{0, 01, 011, 0111\}$.
   - Mở đầu bằng một chữ `0`, theo sau bởi $0, 1, 2$ hoặc tối đa **3 chữ `1`**! Từ 4 chữ `1` (`01111`) trở lên đều BỊ LOẠI!

### Bộ 24 câu trắc nghiệm chuẩn Đề Mẫu Sample 1 (+ 2 câu lý thuyết Word)

**Câu 1.** Xét ngôn ngữ $L$ sinh bởi $G_{14}$. Chuỗi nào sau đây **thuộc** $L$?
- A. `0`
- B. `1`
- C. `00`
- D. $\varepsilon$
👉 **Đáp án đúng: A**
- **Giải thích:** Nhánh $S \to 0$ sinh trực tiếp `0`.

**Câu 2.** Xét ngôn ngữ $L$ sinh bởi $G_{14}$. Chuỗi nào sau đây **thuộc** $L$?
- A. `00`
- B. `01`
- C. `10`
- D. `11`
👉 **Đáp án đúng: B**
- **Giải thích:** $S \Rightarrow 0A \Rightarrow 01$.

**Câu 3.** Xét ngôn ngữ $L$ sinh bởi $G_{14}$. Chuỗi nào sau đây **thuộc** $L$?
- A. `010`
- B. `001`
- C. `011`
- D. `01111`
👉 **Đáp án đúng: C**
- **Giải thích:** $S \Rightarrow 0A \Rightarrow 01B \Rightarrow 011$.

**Câu 4.** Xét ngôn ngữ $L$ sinh bởi $G_{14}$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `0`
- B. `01`
- C. `011`
- D. `01111`
👉 **Đáp án đúng: D**
- **Giải thích:** `01111` có tới 4 chữ `1` (quá giới hạn 3 chữ `1` tại $C \to 1$).

**Câu 5.** Xét ngôn ngữ $L$ sinh bởi $G_{14}$. Chuỗi nào sau đây **thuộc** $L$?
- A. `0111`
- B. `01111`
- C. `0011`
- D. `111`
👉 **Đáp án đúng: A**
- **Giải thích:** $S \Rightarrow 0A \Rightarrow 01B \Rightarrow 011C \Rightarrow 0111$.

**Câu 6.** Xét ngôn ngữ $L$ sinh bởi $G_{14}$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `0`
- B. `01`
- C. `0111`
- D. `001`
👉 **Đáp án đúng: D**
- **Giải thích:** `001` có 2 chữ `0` (trong khi chỉ sinh được đúng 1 chữ `0` ở đầu).

**Câu 7.** Xét ngôn ngữ $L$ sinh bởi $G_{14}$. Chuỗi nào sau đây **thuộc** $L$?
- A. $\varepsilon$
- B. `1`
- C. `01`
- D. `010`
👉 **Đáp án đúng: C**
- **Giải thích:** `01` thuộc $L(G_{14})$.

**Câu 8.** Xét ngôn ngữ $L$ sinh bởi $G_{14}$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `0`
- B. `01`
- C. `011`
- D. `1`
👉 **Đáp án đúng: D**
- **Giải thích:** `1` thiếu chữ `0` ở đầu.

**Câu 9.** Xét ngôn ngữ $L$ sinh bởi $G_{14}$. Chuỗi nào sau đây **thuộc** $L$?
- A. `0110`
- B. `011`
- C. `101`
- D. `01110`
👉 **Đáp án đúng: B**
- **Giải thích:** `011` thuộc tập 4 từ của $L(G_{14})$.

**Câu 12.** Xét ngôn ngữ $L$ sinh bởi $G_{14}$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `0`
- B. `011`
- C. `0111`
- D. `010`
👉 **Đáp án đúng: D**
- **Giải thích:** `010` có chữ `0` xuất hiện ở cuối (chỉ cho phép 1 chữ `0` duy nhất ở đầu).

**Câu 10.** Chuỗi nào có thể sinh từ ký hiệu bắt đầu $S$ của $G_{14}$?
- A. `00`
- B. `01111`
- C. `101`
- D. `0111`
👉 **Đáp án đúng: D**
- **Giải thích:** $S \Rightarrow 0A \Rightarrow 01B \Rightarrow 011C \Rightarrow 0111$.

**Câu 11.** Chuỗi nào được sinh với **ÍT NHẤT 1 LẦN** dùng luật đi qua biến $B$ ($A \to 1B$)?
- A. `0`
- B. `01`
- C. `011`
- D. `1`
👉 **Đáp án đúng: C**
- **Giải thích:** Đi qua $B$ ($A \to 1B$) cần sinh ít nhất 2 chữ `1` $\implies$ ngắn nhất là `011`.

**Câu 13.** Chuỗi **NGẮN NHẤT** thuộc $L($G_{14}$)$ là:
- A. $\varepsilon$
- B. ``0``
- C. ``01``
- D. ``1``
👉 **Đáp án đúng: B**
- **Giải thích:** Chuỗi ngắn nhất là `0` (độ dài 1).

**Câu 14.** Chuỗi **NGẮN NHÌ** thuộc $L($G_{14}$)$ (nếu cùng độ dài thì ưu tiên thứ tự từ điển tăng dần) là:
- A. ``0``
- B. ``01``
- C. ``1``
- D. ``00``
👉 **Đáp án đúng: B**
- **Giải thích:** Chuỗi ngắn nhì là `01` (độ dài 2).

**Câu 15.** Ba chuỗi ngắn nhất thuộc $L($G_{14}$)$ (xếp theo độ dài và thứ tự từ điển tăng dần) là:
- A. 0, 01, 001
- B. 0, 01, 011
- C. 01, 011, 0111
- D. $\varepsilon$, 0, 01
👉 **Đáp án đúng: B**
- **Giải thích:** Ba chuỗi ngắn nhất là `0`, `01`, `011`.

**Câu 16.** Chuỗi **thứ 4** theo độ dài tăng dần của $L($G_{14}$)$ (nếu cùng độ dài ưu tiên thứ tự từ điển từ trái sang phải) là:
- A. ``011``
- B. ``0111``
- C. ``01111``
- D. ``0011``
👉 **Đáp án đúng: B**
- **Giải thích:** Tất cả 4 chuỗi của ngôn ngữ theo thứ tự tăng dần: (1) `0`, (2) `01`, (3) `011`, (4) `0111`.

**Câu 17.** Chuỗi ngắn nhất thuộc $L($G_{14}$)$ thỏa điều kiện **có độ dài $\ge 3$** là:
- A. ``01``
- B. ``011``
- C. ``0111``
- D. ``01111``
👉 **Đáp án đúng: B**
- **Giải thích:** Chuỗi hợp lệ ngắn nhất có độ dài $\ge 3$ là `011` (dài 3).

**Câu 18.** Ngôn ngữ $L(G_{14})$ có tất cả bao nhiêu chuỗi?
- A. 3 chuỗi
- B. 4 chuỗi
- C. 5 chuỗi
- D. Vô hạn chuỗi
👉 **Đáp án đúng: B**
- **Giải thích:** Vì không có đệ quy vòng lặp nên chỉ sinh được hữu hạn 4 chuỗi: `0, 01, 011, 0111`.

**Câu 19.** Độ dài tối đa của một chuỗi thuộc $L(G_{14})$ là:
- A. `3`
- B. 4 (chuỗi `0111`)
- C. `5`
- D. Không có giới hạn
👉 **Đáp án đúng: B**
- **Giải thích:** Đường dẫn dài nhất dừng ở $C \to 1$ cho chuỗi `0111` (4 ký tự).

**Câu 20.** Tập hợp đầy đủ của ngôn ngữ $L(G_{14})$ là:
- A. $01^*$
- B. $\{0, 01, 011, 0111\}$
- C. $\{01, 011, 0111\}$
- D. $01^+ $
👉 **Đáp án đúng: B**
- **Giải thích:** Ngôn ngữ hữu hạn gồm đúng 4 từ `{0, 01, 011, 0111}`.

**Câu 21.** Chuỗi `0111` có thuộc $L($G_{14}$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: A**
- **Giải thích:** Đúng, từ thứ 4 của $L(G_{14})$.

**Câu 22.** Chuỗi `01111` có thuộc $L($G_{14}$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: B**
- **Giải thích:** Sai, tối đa chỉ 3 chữ `1`.

**Câu 23.** Chuỗi `0` có thuộc $L($G_{14}$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: A**
- **Giải thích:** Đúng, $S \to 0$.

**Câu 24.** Chuỗi $\varepsilon$ có thuộc $L($G_{14}$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: B**
- **Giải thích:** Sai, chuỗi rỗng không thuộc $L(G_{14})$.

**Câu 25.** (Câu hỏi Word) Ngôn ngữ hữu hạn $L(G_{14})$ thuộc loại mấy theo phân loại Chomsky?
- A. Loại 3 (Chính quy - Regular)
- B. Chỉ là Loại 2
- C. Chỉ là Loại 1
- D. Loại 0
👉 **Đáp án đúng: A**
- **Giải thích:** **Mọi ngôn ngữ hữu hạn ĐỀU LÀ NGÔN NGỮ CHÍNH QUY (Loại 3)!** Ngoài ra các luật của $G_{14}$ đều tuyến tính phải ($X \to aY \mid a$).

**Câu 26.** (Câu hỏi Word) Biểu thức chính quy (RE) biểu diễn $L(G_{14})$ là:
- A. $01^*$
- B. $0(\varepsilon + 1 + 11 + 111)$ (hay $0 + 01 + 011 + 0111$)
- C. $(0+1)^*$
- D. $01^+$
👉 **Đáp án đúng: B**
- **Giải thích:** Ngôn ngữ hữu hạn biểu diễn trực tiếp bằng phép cộng hữu hạn các từ của nó: $0 + 01 + 011 + 0111$.

---

## VĂN PHẠM 17 ($G_{17}$): CHÍNH QUY CẤM CỤM `00` ($\{w \in \{0,1\}^+ \mid w\text{ không chứa }00\}$)

> **ĐỀ BÀI GỐC ($G_{17}$):**
> $$
> G_{17} = \langle \{0, 1\},\ \{S, A\},\ S,\ \{S \to 0A \mid 1S \mid 0 \mid 1,\ A \to 1A \mid 1S \mid 1\} \rangle
> $$
> Với các quy tắc sinh: $S \to 0A \mid 1S \mid 0 \mid 1$, $A \to 1A \mid 1S \mid 1$

### Bản chất cốt lõi & Quy tắc vàng nhận diện trong 3 giây
1. **Phân tích các bước chuyển từ $S$ và $A$:**
   - Từ $S$: đọc `1` giữ nguyên ở $S$ ($1S$) hoặc dừng ($1$); đọc `0` nhảy sang $A$ ($0A$) hoặc dừng ($0$).
   - Tại $A$ (trạng thái **"vừa mới đọc một chữ `0`"**): các luật của $A$ chỉ cho phép sinh **`1`** ($1A \mid 1S \mid 1$), **TUYỆT ĐỐI KHÔNG CÓ `0` đứng sau `0`!**
   - Kết quả: $\mathbf{L(G_{17}) = \{w \in \{0,1\}^+ \mid w\text{ KHÔNG chứa chuỗi con }00\}}$.
2. **Ba quy tắc vàng 3 giây:**
   - Độ dài $\ge 1$ (không chứa $\varepsilon$).
   - Chữ `1` xuất hiện tự do bao nhiêu cũng được.
   - **CẤM TUYỆT ĐỐI hai chữ `0` đứng cạnh nhau (`00`)!** (`0101` hợp lệ, `001` hay `1001` bị loại ngay!).

### Bộ 24 câu trắc nghiệm chuẩn Đề Mẫu Sample 1 (+ 2 câu lý thuyết Word)

**Câu 1.** Xét ngôn ngữ $L$ sinh bởi $G_{17}$. Chuỗi nào sau đây **thuộc** $L$?
- A. `00`
- B. `01`
- C. `001`
- D. `100`
👉 **Đáp án đúng: B**
- **Giải thích:** `01` khác rỗng và không chứa cụm `00` ($S \Rightarrow 0A \Rightarrow 01$).

**Câu 2.** Xét ngôn ngữ $L$ sinh bởi $G_{17}$. Chuỗi nào sau đây **thuộc** $L$?
- A. `000`
- B. `100`
- C. `010`
- D. `001`
👉 **Đáp án đúng: C**
- **Giải thích:** `010` không có hai chữ `0` liền nhau ($S \Rightarrow 0A \Rightarrow 01S \Rightarrow 010$).

**Câu 3.** Xét ngôn ngữ $L$ sinh bởi $G_{17}$. Chuỗi nào sau đây **thuộc** $L$?
- A. `0011`
- B. `10101`
- C. `1100`
- D. `0000`
👉 **Đáp án đúng: B**
- **Giải thích:** `10101` không chứa cụm `00`.

**Câu 4.** Xét ngôn ngữ $L$ sinh bởi $G_{17}$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `0`
- B. `1`
- C. `010`
- D. `00`
👉 **Đáp án đúng: D**
- **Giải thích:** `00` vi phạm quy tắc cấm hai chữ `0` đứng liền nhau!

**Câu 5.** Xét ngôn ngữ $L$ sinh bởi $G_{17}$. Chuỗi nào sau đây **thuộc** $L$?
- A. `110110`
- B. `110011`
- C. `001100`
- D. `0100`
👉 **Đáp án đúng: A**
- **Giải thích:** `110110` không chứa `00` (các chữ `0` luôn được cách bởi chữ `1`).

**Câu 6.** Xét ngôn ngữ $L$ sinh bởi $G_{17}$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `111`
- B. `0110`
- C. `10110`
- D. `0100`
👉 **Đáp án đúng: D**
- **Giải thích:** `0100` có đuôi `00` nên KHÔNG thuộc $L$.

**Câu 7.** Xét ngôn ngữ $L$ sinh bởi $G_{17}$. Chuỗi nào sau đây **thuộc** $L$?
- A. $\varepsilon$
- B. `1010`
- C. `001`
- D. `1001`
👉 **Đáp án đúng: B**
- **Giải thích:** `1010` khác rỗng và không có `00`.

**Câu 8.** Xét ngôn ngữ $L$ sinh bởi $G_{17}$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `0`
- B. `10`
- C. `1101`
- D. `1001`
👉 **Đáp án đúng: D**
- **Giải thích:** `1001` chứa cụm `00` ở giữa nên bị loại.

**Câu 9.** Xét ngôn ngữ $L$ sinh bởi $G_{17}$. Chuỗi nào sau đây **thuộc** $L$?
- A. `0010`
- B. `1100`
- C. `011101`
- D. `000`
👉 **Đáp án đúng: C**
- **Giải thích:** `011101` không chứa `00`.

**Câu 12.** Xét ngôn ngữ $L$ sinh bởi $G_{17}$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `01`
- B. `10`
- C. `0110`
- D. $\varepsilon$
👉 **Đáp án đúng: D**
- **Giải thích:** Chuỗi rỗng $\varepsilon$ không thuộc $L(G_{17})$ vì $S$ không có $S \to \varepsilon$.

**Câu 10.** Chuỗi nào có thể sinh từ ký hiệu bắt đầu $S$ của $G_{17}$?
- A. `00`
- B. `100`
- C. `0100`
- D. `0110`
👉 **Đáp án đúng: D**
- **Giải thích:** `0110` được sinh qua: $S \Rightarrow 0A \Rightarrow 01A \Rightarrow 011S \Rightarrow 0110$.

**Câu 11.** Chuỗi nào được sinh với **ÍT NHẤT 1 LẦN** dùng luật $S \to 0A$ (chuyển sang trạng thái $A$ bắt buộc đọc `1` nếu muốn đi tiếp)?
- A. `0`
- B. `1`
- C. `11`
- D. `01`
👉 **Đáp án đúng: D**
- **Giải thích:** Muốn dùng $S \to 0A$ phải sinh ít nhất `0` rồi `1`, nên ngắn nhất là `01`.

**Câu 13.** Chuỗi **NGẮN NHẤT** thuộc $L($G_{17}$)$ là:
- A. $\varepsilon$
- B. ``0``
- C. ``01``
- D. ``10``
👉 **Đáp án đúng: B**
- **Giải thích:** Có 2 chuỗi dài 1 là `0` và `1`. Theo thứ tự từ điển (`0 < 1`), `0` đứng đầu.

**Câu 14.** Chuỗi **NGẮN NHÌ** thuộc $L($G_{17}$)$ (nếu cùng độ dài thì ưu tiên thứ tự từ điển tăng dần) là:
- A. ``0``
- B. ``1``
- C. ``01``
- D. ``10``
👉 **Đáp án đúng: B**
- **Giải thích:** Chuỗi ngắn nhì là `1` (cũng có độ dài 1, xếp sau `0`).

**Câu 15.** Ba chuỗi ngắn nhất thuộc $L($G_{17}$)$ (xếp theo độ dài và thứ tự từ điển tăng dần) là:
- A. 0, 1, 00
- B. 0, 1, 01
- C. 01, 10, 11
- D. $\varepsilon$, 0, 1
👉 **Đáp án đúng: B**
- **Giải thích:** Dài 1: `0`, `1`. Dài 2 có 3 chuỗi hợp lệ là `01`, `10`, `11` (`00` bị loại!); xếp đầu là `01`.

**Câu 16.** Chuỗi **thứ 4** theo độ dài tăng dần của $L($G_{17}$)$ (nếu cùng độ dài ưu tiên thứ tự từ điển từ trái sang phải) là:
- A. ``00``
- B. ``01``
- C. ``10``
- D. ``11``
👉 **Đáp án đúng: C**
- **Giải thích:** Thứ tự tăng dần: (1) `0`, (2) `1`, (3) `01`, (4) `10`.

**Câu 17.** Chuỗi ngắn nhất thuộc $L($G_{17}$)$ thỏa điều kiện **có chứa chữ `0` và độ dài $\ge 2$** là:
- A. ``00``
- B. ``01``
- C. ``10``
- D. ``11``
👉 **Đáp án đúng: B**
- **Giải thích:** Chuỗi dài $\ge 2$ có chứa `0` đứng đầu từ điển là `01`.

**Câu 18.** Mẫu chuỗi con nào TUYỆT ĐỐI KHÔNG BAO GIỜ xuất hiện trong $L(G_{17})$?
- A. ``11``
- B. ``01``
- C. ``00``
- D. ``10``
👉 **Đáp án đúng: C**
- **Giải thích:** Tại trạng thái $A$ (sau khi đọc `0`) không hề có luật nào bắt đầu bằng `0` nên `00` không bao giờ sinh được.

**Câu 19.** Số lượng chuỗi có độ dài $n$ thuộc $L(G_{17})$ (không chứa `00`) tuân theo quy luật gì?
- A. $2^n$
- B. Dãy Fibonacci ($2, 3, 5, 8, 13, \dots$)
- C. Luôn bằng 2
- D. Số chẵn
👉 **Đáp án đúng: B**
- **Giải thích:** Dài 1: 2 (`0,1`); dài 2: 3 (`01,10,11`); dài 3: 5; dài 4: 8; dài 5: 13.

**Câu 20.** Mô tả chính xác nhất ngôn ngữ $L(G_{17})$ là:
- A. $\{w \in \{0,1\}^* \mid w\text{ chứa }00\}$
- B. $\{w \in \{0,1\}^+ \mid w\text{ không chứa }00\}$
- C. $(01)^+$
- D. $\{w \in \{0,1\}^+ \mid w\text{ kết thúc bằng }1\}$
👉 **Đáp án đúng: B**
- **Giải thích:** Gồm mọi chuỗi nhị phân khác rỗng không chứa hai số `0` liên tiếp.

**Câu 21.** Chuỗi `0101` có thuộc $L($G_{17}$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: A**
- **Giải thích:** Đúng, không chứa `00`.

**Câu 22.** Chuỗi `01001` có thuộc $L($G_{17}$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: B**
- **Giải thích:** Sai, chứa `00`.

**Câu 23.** Chuỗi `1111` có thuộc $L($G_{17}$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: A**
- **Giải thích:** Đúng, toàn `1` không chứa `00`.

**Câu 24.** Chuỗi `00` có thuộc $L($G_{17}$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: B**
- **Giải thích:** Sai, chính là `00`.

**Câu 25.** (Câu hỏi Word) Văn phạm $G_{17}$ thuộc loại mấy theo phân loại Chomsky?
- A. Loại 3 (Chính quy - Tuyến tính phải)
- B. Loại 2
- C. Loại 1
- D. Loại 0
👉 **Đáp án đúng: A**
- **Giải thích:** Mọi quy tắc sinh ($S \to 0A \mid 1S \mid 0 \mid 1,\ A \to 1A \mid 1S \mid 1$) đều là tuyến tính phải chuẩn Loại 3.

**Câu 26.** (Câu hỏi Word) Biểu thức chính quy (RE) biểu diễn $L(G_{17})$ (tất cả chuỗi khác rỗng không chứa `00`) là:
- A. $(1 + 01)^* (0 + \varepsilon)$ trừ $\varepsilon$, tức $(1+01)^+ + (1+01)^*0$
- B. $(0+1)^*00(0+1)^*$
- C. $0^*1^*$
- D. $(01)^*$
👉 **Đáp án đúng: A**
- **Giải thích:** Mỗi chữ `0` (trừ chữ `0` đứng cuối cùng) bắt buộc phải có `1` theo sau thành khối `01`, nên mọi chuỗi không chứa `00` khác rỗng đều có dạng $(1+01)^+$ hoặc $(1+01)^*0$.

---

## VĂN PHẠM 18 ($G_{18}$): BIẾN THỂ CFG TUYẾN TÍNH TỪ $G_{17}$ ($A \to 1A0$)

> **ĐỀ BÀI GỐC ($G_{18}$):**
> $$
> G_{18} = \langle \{0, 1\},\ \{S, A\},\ S,\ \{S \to 0A \mid 1S \mid 0 \mid 1,\ A \to 1A0 \mid 1S \mid 1\} \rangle
> $$
> Với các quy tắc sinh: $S \to 0A \mid 1S \mid 0 \mid 1$, $A \to 1A0 \mid 1S \mid 1$

### Bản chất cốt lõi & Quy tắc vàng nhận diện trong 3 giây
1. **So sánh với $G_{17}$ (cùng đề bài nhưng thay $A \to 1A$ bằng $A \to 1A0$):**
   - Tất cả mọi chuỗi của $G_{17}$ (không chứa `00`) **VẪN ĐƯỢC SINH** trong $G_{18}$ (qua $S \to 0A \mid 1S \mid 0 \mid 1$ và $A \to 1S \mid 1$).
   - Ngoài ra, luật **$A \to 1A0$** cho phép lặp $k$ lần để kẹp: $A \Rightarrow 1^k (1S \mid 1) 0^k$.
   - Nhờ vậy, khi dừng ở $1S0 \to 100$ (cho chuỗi **`01100`**!) hoặc $1(1)0$, chữ `0` ở cuối của khối $A \to 1A0$ đứng cạnh chữ `0` khác sinh ra từ $S$, **tạo được cụm `00` nhưng PHẢI KÈM TƯƠNG ỨNG CHỮ `1` ĐỐI XỨNG Ở PHÍA TRƯỚC!**
2. **Mẹo 3 giây phân biệt $G_{17}$ và $G_{18}$:**
   - $G_{17}$: CẤM TIỆT cụm `00`.
   - $G_{18}$: Vẫn cấm `00`, `000`, `0100`, `001`, `100` (các chuỗi `00` đứng trơ trụi không có cụm `1^k ... 0^k` bao bọc), NHƯNG **CHẤP NHẬN `01100`** ($S \to 0A \to 0(1A0) \to 01(1S)0 \to 011(0)0$)!

### Bộ 24 câu trắc nghiệm chuẩn Đề Mẫu Sample 1 (+ 2 câu lý thuyết Word)

**Câu 1.** Xét ngôn ngữ $L$ sinh bởi $G_{18}$. Chuỗi nào sau đây **thuộc** $L$?
- A. `00`
- B. `01100`
- C. `0100`
- D. `100`
👉 **Đáp án đúng: B**
- **Giải thích:** `01100` hợp lệ qua: $S \Rightarrow 0A \Rightarrow 0(1A0) \Rightarrow 01(1S)0 \Rightarrow 01100$. Các chuỗi `00`, `0100`, `100` đều sai!

**Câu 2.** Xét ngôn ngữ $L$ sinh bởi $G_{18}$. Chuỗi nào sau đây **thuộc** $L$?
- A. `000`
- B. `1001`
- C. `01101`
- D. `001`
👉 **Đáp án đúng: C**
- **Giải thích:** `01101` không chứa `00` nên sinh được bình thường qua $S \to 0A \to 01S \dots$.

**Câu 3.** Xét ngôn ngữ $L$ sinh bởi $G_{18}$. Chuỗi nào sau đây **thuộc** $L$?
- A. `0011`
- B. `011100`
- C. `0100`
- D. `1100`
👉 **Đáp án đúng: B**
- **Giải thích:** `011100` = `0` + `1(1(1S)0)0`... kiểm tra: $S \Rightarrow 0A \Rightarrow 0(1A0) \Rightarrow 01(1S)0 \Rightarrow 011(1S)0$ không có `0`? Khoan: $S \Rightarrow 0A \Rightarrow 0(1A0) \Rightarrow 01(1A0)0$ thiếu, còn $011100$: $S \Rightarrow 0A \Rightarrow 01A0$ rồi $A \Rightarrow 1S$ ra $011S0 \Rightarrow 011(1S)0 \Rightarrow 0111(0)0$ = `011100`! ĐÚNG 100%!

**Câu 4.** Xét ngôn ngữ $L$ sinh bởi $G_{18}$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `01`
- B. `01100`
- C. `011100`
- D. `0100`
👉 **Đáp án đúng: D**
- **Giải thích:** `0100` KHÔNG sinh được vì để có đuôi `00` qua $A \to 1A0$, bên trái `00` cần ít nhất 2 chữ `1` (`01100`).

**Câu 5.** Xét ngôn ngữ $L$ sinh bởi $G_{18}$. Chuỗi nào sau đây **thuộc** $L$?
- A. `0100`
- B. `101100`
- C. `1100`
- D. `0010`
👉 **Đáp án đúng: B**
- **Giải thích:** `101100`: $S \Rightarrow 1S \Rightarrow 1(01100)$.

**Câu 6.** Xét ngôn ngữ $L$ sinh bởi $G_{18}$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `0`
- B. `010`
- C. `01100`
- D. `001`
👉 **Đáp án đúng: D**
- **Giải thích:** `001` bắt đầu ngay bằng `00` (không thể có $1A0$ trước chữ `0` đầu tiên).

**Câu 7.** Xét ngôn ngữ $L$ sinh bởi $G_{18}$. Chuỗi nào sau đây **thuộc** $L$?
- A. `00`
- B. `0111000`
- C. `1000`
- D. `0100`
👉 **Đáp án đúng: B**
- **Giải thích:** `0111000`: $S \Rightarrow 0A \Rightarrow 01A0 \Rightarrow 011A00 \Rightarrow 0111S00 \Rightarrow 0111000$!

**Câu 8.** Xét ngôn ngữ $L$ sinh bởi $G_{18}$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `1`
- B. `010`
- C. `01100`
- D. `100`
👉 **Đáp án đúng: D**
- **Giải thích:** `100` chỉ có một chữ `1` đứng trước `00`, trong khi dạng `00` ngắn nhất sau `0` phải cần `01100`.

**Câu 9.** Xét ngôn ngữ $L$ sinh bởi $G_{18}$. Chuỗi nào sau đây **thuộc** $L$?
- A. `000`
- B. `001100`
- C. `011011`
- D. `01001`
👉 **Đáp án đúng: C**
- **Giải thích:** `011011` không chứa `00` nên sinh dễ dàng qua $S \to 0A \to 01A \dots$.

**Câu 12.** Xét ngôn ngữ $L$ sinh bởi $G_{18}$. Chuỗi nào sau đây **KHÔNG thuộc** $L$?
- A. `01`
- B. `10`
- C. `01100`
- D. `0000`
👉 **Đáp án đúng: D**
- **Giải thích:** `0000` bắt đầu bằng `00`, không thể sinh được từ $S \to 0A$.

**Câu 10.** Chuỗi nào có thể sinh từ ký hiệu bắt đầu $S$ của $G_{18}$?
- A. `00`
- B. `0100`
- C. `01100`
- D. `100`
👉 **Đáp án đúng: C**
- **Giải thích:** $S \Rightarrow 0A \Rightarrow 01A0 \Rightarrow 011S0 \Rightarrow 01100$.

**Câu 11.** Chuỗi nào được sinh với **ÍT NHẤT 1 LẦN** dùng luật $A \to 1A0$ (tạo cụm `00` hợp lệ mà $G_{17}$ không sinh được)?
- A. `0`
- B. `01`
- C. `01100`
- D. `101`
👉 **Đáp án đúng: C**
- **Giải thích:** `0`, `01`, `101` đều sinh được trong $G_{17}$ (không cần $A \to 1A0$). Chuỗi `01100` là chuỗi ngắn nhất bắt buộc phải dùng luật $A \to 1A0$!

**Câu 13.** Chuỗi **NGẮN NHẤT** thuộc $L($G_{18}$)$ là:
- A. $\varepsilon$
- B. ``0``
- C. ``01``
- D. ``1``
👉 **Đáp án đúng: B**
- **Giải thích:** Hai chuỗi dài 1 là `0`, `1`; theo từ điển chọn `0`.

**Câu 14.** Chuỗi **NGẮN NHÌ** thuộc $L($G_{18}$)$ (nếu cùng độ dài thì ưu tiên thứ tự từ điển tăng dần) là:
- A. ``0``
- B. ``1``
- C. ``01``
- D. ``10``
👉 **Đáp án đúng: B**
- **Giải thích:** Chuỗi ngắn nhì là `1` (dài 1).

**Câu 15.** Ba chuỗi ngắn nhất thuộc $L($G_{18}$)$ (xếp theo độ dài và thứ tự từ điển tăng dần) là:
- A. 0, 1, 00
- B. 0, 1, 01
- C. 01, 10, 01100
- D. $\varepsilon$, 0, 1
👉 **Đáp án đúng: B**
- **Giải thích:** Dài 1: `0`, `1`. Dài 2 đầu tiên theo từ điển: `01` (`00` bị loại!).

**Câu 16.** Chuỗi **thứ 4** theo độ dài tăng dần của $L($G_{18}$)$ (nếu cùng độ dài ưu tiên thứ tự từ điển từ trái sang phải) là:
- A. ``00``
- B. ``01``
- C. ``10``
- D. ``11``
👉 **Đáp án đúng: C**
- **Giải thích:** Thứ tự: (1) `0`, (2) `1`, (3) `01`, (4) `10`.

**Câu 17.** Chuỗi ngắn nhất thuộc $L($G_{18}$)$ thỏa điều kiện **có chứa cụm `00`** là:
- A. ``00``
- B. ``001``
- C. ``0100``
- D. ``01100``
👉 **Đáp án đúng: D**
- **Giải thích:** Chuỗi hợp lệ NGẮN NHẤT có chứa `00` trong $L(G_{18})$ là **`01100`** (độ dài 5)! Mọi chuỗi chứa `00` dài 2, 3, 4 đều không sinh được!

**Câu 18.** So sánh với $L(G_{17})$, chuỗi nào sau đây thuộc $L(G_{18})$ nhưng KHÔNG thuộc $L(G_{17})$?
- A. ``01``
- B. ``1010``
- C. ``01100``
- D. ``111``
👉 **Đáp án đúng: C**
- **Giải thích:** `01100` chứa cụm `00` nên bị $G_{17}$ loại, nhưng lại sinh được từ $G_{18}$ nhờ luật $A \to 1A0$.

**Câu 19.** Luật nào trong $G_{18}$ khiến văn phạm này KHÔNG còn là văn phạm chính quy (Loại 3) như $G_{17}$?
- A. $S \to 0A$
- B. $S \to 1S$
- C. $A \to 1A0$
- D. $A \to 1$
👉 **Đáp án đúng: C**
- **Giải thích:** $A \to 1A0$ kẹp hai ký tự kết thúc `1` và `0` ở hai đầu biến $A$, phá vỡ dạng tuyến tính phải/trái của Loại 3.

**Câu 20.** Quan hệ bao hàm giữa $L(G_{17})$ và $L(G_{18})$ là:
- A. $L(G_{17}) = L(G_{18})$
- B. $L(G_{17}) \subsetneq L(G_{18})$ (mở rộng thêm các chuỗi chứa cặp $1^k \dots 0^k$)
- C. $L(G_{18}) \subsetneq L(G_{17})$
- D. Rời nhau hoàn toàn
👉 **Đáp án đúng: B**
- **Giải thích:** Mọi dẫn xuất dùng $A \to 1A$ ở $G_{17}$ đều làm được ở $G_{18}$ qua $A \to 1S \mid 1$? Khoan: chuỗi `0110` ở $G_{17}$ đi $S \to 0A \to 01A \to 011S \to 0110$; ở $G_{18}$ dùng $A \to 1S$? Đợi đã: `01110` ở $G_{17}$ đi $0A \to 01A \to 011A \to 0111S \to 01110$. Trong $G_{18}$, `A` không có `A -> 1A` (mất `1A`, chỉ còn `1A0 | 1S | 1`), mà `S` lại có `S -> 1S`! Nên $A \to 1S \to 11S \dots$ sinh được ĐÚNG mọi chuỗi sau `1` của $G_{17}$!! Do đó $L(G_{17}) \subsetneq L(G_{18})$ CHUẨN 100%!

**Câu 21.** Chuỗi `01100` có thuộc $L($G_{18}$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: A**
- **Giải thích:** Đúng, $S \Rightarrow 0A \Rightarrow 01A0 \Rightarrow 011S0 \Rightarrow 01100$.

**Câu 22.** Chuỗi `0100` có thuộc $L($G_{18}$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: B**
- **Giải thích:** Sai, không đủ chữ `1` tương ứng với `0` bọc ngoài.

**Câu 23.** Chuỗi `01110` có thuộc $L($G_{18}$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: A**
- **Giải thích:** Đúng, $S \Rightarrow 0A \Rightarrow 01S \Rightarrow 011S \Rightarrow 0111S \Rightarrow 01110$.

**Câu 24.** Chuỗi `00` có thuộc $L($G_{18}$)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: B**
- **Giải thích:** Sai, không bắt đầu bằng `00` được.

**Câu 25.** (Câu hỏi Word) Văn phạm $G_{18}$ thuộc loại mấy theo phân loại Chomsky?
- A. Loại 3 (Chính quy)
- B. Loại 2 (Phi ngữ cảnh tuyến tính - CFG)
- C. Loại 1 (không có trong Loại 2)
- D. Loại 0
👉 **Đáp án đúng: B**
- **Giải thích:** Vế trái chỉ là 1 biến ($S, A$), vế phải có luật $A \to 1A0$ kẹp 2 đầu tạo đối xứng `1^k...0^k` nên là Ngôn ngữ Phi ngữ cảnh (Loại 2).

**Câu 26.** (Câu hỏi Word) Loại máy cần thiết để đoán nhận $L(G_{18})$ là:
- A. `DFA`
- B. `NFA`
- C. Otomat đẩy xuống (PDA)
- D. Chỉ Máy Turing
👉 **Đáp án đúng: C**
- **Giải thích:** Vì ngôn ngữ thuộc Loại 2 (CFG) nên cần Otomat đẩy xuống (PDA) có ngăn xếp để đếm số lượng `1` khớp với số `0` từ luật $A \to 1A0$.

---

## CHUYÊN MỤC ĐẶC BIỆT: GIẢI MÃ BẪY VĂN PHẠM $G_{19}$ TRONG FILE WORD

> **Đề bài gốc:**
> $$G_{19} = \langle \{0, 1\},\ \{S, A, B\},\ S,\ \{S \to 0AB,\ A0 \to S0B,\ A1 \to SB1,\ B \to SA \mid 01\} \rangle$$

### Phân tích toán học bất ngờ (Tránh bị lừa khi thi!):
1. **Phân loại Chomsky theo cú pháp:** Vì có các luật $A0 \to S0B$ và $A1 \to SB1$ với vế trái gồm 2 ký hiệu ($|\alpha| = 2 \le |\beta| = 3$, không rút gọn), $G_{19}$ có dạng hình thức của **Văn phạm Cảm ngữ cảnh (Loại 1)** hoặc xếp vào **Loại 0** trong nhóm văn phạm tổng quát (vì vế trái không thuần 1 biến và có chữ số kết thúc đi kèm).
2. **Ngôn ngữ thực tế sinh ra $L(G_{19})$ là gì?**
   Hãy đếm tổng số chữ cái không kết thúc $(\#S + \#A)$ ở mỗi bước dẫn xuất:
   - Ban đầu tại $S$: $\#S + \#A = 1 + 0 = 1$ (**số lẻ!**).
   - Dùng $S \to 0AB$: mất 1 chữ $S$, thêm 1 chữ $A$ $\implies \#S + \#A$ **không đổi (vẫn lẻ)**.
   - Dùng $A0 \to S0B$ hoặc $A1 \to SB1$: mất 1 chữ $A$, thêm 1 chữ $S$ $\implies \#S + \#A$ **không đổi (vẫn lẻ)**.
   - Dùng $B \to SA$: thêm cả 1 $S$ và 1 $A$ ($+2$) $\implies$ tính chẵn lẻ của $(\#S + \#A)$ **không đổi (vẫn lẻ)**.
   - Dùng $B \to 01$: không đổi $S$ và $A$ $\implies$ vẫn **lẻ**.
   👉 **KẾT LUẬN CHẤN ĐỘNG:** Trong mọi chuỗi sinh từ $S$, số lượng biến $(S, A)$ còn lại **LUÔN LÀ SỐ LẺ ($\ge 1$)**, không bao giờ triệt tiêu hết để chỉ còn toàn chữ `0` và `1`!
   Do đó **$L(G_{19}) = \emptyset$ (Ngôn ngữ rỗng!)** — không có bất kỳ từ kết thúc nào được sinh ra từ $G_{19}$!
