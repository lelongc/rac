# NGÂN HÀNG TRẮC NGHIỆM CHƯƠNG 1: KHÁI NIỆM CƠ BẢN VỀ NGÔN NGỮ VÀ VĂN PHẠM
## ÔN THI CUỐI KỲ - ĐẦY ĐỦ DẠNG BÀI, BIẾN THỂ VÀ LỜI GIẢI DỄ HIỂU NHẤT CHO NGƯỜI MỚI HỌC

---

# TÓM TẮT LÝ THUYẾT VÀ BÍ KÍP "ĂN TRỌN ĐIỂM" CHƯƠNG 1

### 1. Phép toán trên từ (chuỗi / xâu):
- **Bảng chữ cái $\Sigma$:** Tập hợp hữu hạn, khác rỗng các ký hiệu (ví dụ $\Sigma = \{a, b\}$ hoặc $\{0, 1\}$).
- **Từ rỗng $\varepsilon$ (hoặc $\Lambda$):** Từ không chứa ký hiệu nào, có độ dài $|\varepsilon| = 0$.
- **Độ dài của từ $|w|$:** Số lượng ký hiệu trong từ. Ví dụ: $|aba| = 3$, $|\varepsilon| = 0$.
- **Số lần xuất hiện của ký hiệu $a$ trong $w$:** Ký hiệu $|w|_a$. Ví dụ: $|abaca|_a = 3$.
- **Phép ghép từ (Nối từ):** Nếu $u = ab, v = ba \implies uv = abba$. Tính chất: $u\varepsilon = \varepsilon u = u$, $|uv| = |u| + |v|$.
- **Lũy thừa của từ $w^k$:** Ghép $k$ lần từ $w$. Quy ước $w^0 = \varepsilon, w^1 = w, w^2 = ww$.
- **Đảo ngược của từ $w^R$:** Viết ngược các ký hiệu. Ví dụ: $(abc)^R = cba$. Tính chất: $(uv)^R = v^R u^R$, $(w^R)^R = w$.
- **Tiền tố (Prefix), Hậu tố (Suffix), Từ con (Substring):**
  - Tiền tố: Các ký tự ở đầu. Từ rỗng $\varepsilon$ và chính $w$ luôn là tiền tố của $w$.
  - Hậu tố: Các ký tự ở cuối. $\varepsilon$ và chính $w$ luôn là hậu tố của $w$.
  - Từ con: Một đoạn liên tiếp trong $w$.

### 2. Phép toán trên ngôn ngữ:
- Ngôn ngữ $L$ trên $\Sigma$ là một tập con bất kỳ của $\Sigma^*$ ($L \subseteq \Sigma^*$).
- **Ngôn ngữ rỗng $\emptyset$:** Khác với $\{\varepsilon\}$! (Tập $\emptyset$ có 0 phần tử, tập $\{\varepsilon\}$ có 1 phần tử là từ rỗng).
- **Phép ghép ngôn ngữ:** $L_1 L_2 = \{ uv \mid u \in L_1, v \in L_2 \}$.
- **Bao đóng Kleene $L^*$:** $L^* = L^0 \cup L^1 \cup L^2 \cup \dots = \bigcup_{k=0}^\infty L^k$. **LUÔN LUÔN chứa $\varepsilon$!**
- **Bao đóng dương $L^+$:** $L^+ = L^1 \cup L^2 \cup \dots = \bigcup_{k=1}^\infty L^k$. Chỉ chứa $\varepsilon$ khi bản thân $L$ có chứa $\varepsilon$.
  - Mối quan hệ: $L^* = L^+ \cup \{\varepsilon\}$.

### 3. Phân cấp văn phạm theo Chomsky (CỰC KỲ QUAN TRỌNG TRONG ĐỀ THI):
Văn phạm $G = \langle \Sigma, \Delta, S, P \rangle$ với $\Sigma$ là ký hiệu kết thúc (chữ thường), $\Delta$ là biến/ký hiệu chưa kết thúc (chữ hoa), $S \in \Delta$ là biến bắt đầu, $P$ là tập luật $\alpha \to \beta$.

```text
┌────────────────────────────────────────────────────────────────────────┐
│ PHÂN CẤP CHOMSKY: LOẠI 3 ⊂ LOẠI 2 ⊂ LOẠI 1 ⊂ LOẠI 0                   │
├─────────┬───────────────────────────────┬──────────────────────────────┤
│ Loại    │ Tên gọi văn phạm              │ Đặc điểm nhận diện luật sinh │
├─────────┼───────────────────────────────┼──────────────────────────────┤
│ LOẠI 0  │ Cấu trúc ngữ (Unrestricted)   │ Mọi luật α → β (vế trái α    │
│         │                               │ chứa ít nhất 1 biến).        │
├─────────┼───────────────────────────────┼──────────────────────────────┤
│ LOẠI 1  │ Cảm ngữ cảnh (Context-        │ |α| ≤ |β| (vế phải luôn dài  │
│         │ sensitive - CSG)              │ hơn hoặc bằng vế trái).      │
├─────────┼───────────────────────────────┼──────────────────────────────┤
│ LOẠI 2  │ Phi ngữ cảnh (Context-        │ Vế trái chỉ gồm ĐÚNG 1 BIẾN  │
│         │ free - CFG)                   │ HOA: A → β (β tùy ý).        │
├─────────┼───────────────────────────────┼──────────────────────────────┤
│ LOẠI 3  │ Chính quy (Regular - RG)      │ A → wB | w (Tuyến tính phải) │
│         │                               │ HOẶC A → Bw | w (Tuyến tính  │
│         │                               │ trái).                       │
└─────────┴───────────────────────────────┴──────────────────────────────┘
```

> [!TIP]
> **BÍ KÍP XÁC ĐỊNH PHÂN LỚP THẤP NHẤT TRONG 5 GIÂY:**
> 1. Nhìn vế trái của TẤT CẢ các luật: Nếu có luật nào vế trái có từ 2 ký hiệu trở lên (ví dụ $aA \to ba$, $AB \to CD$) $\implies$ Không thể là Loại 2 hoặc 3. So độ dài $|\alpha| \le |\beta|$: nếu thỏa mãn là **Loại 1**, nếu vi phạm (vế phải ngắn hơn) là **Loại 0**.
> 2. Nếu mọi vế trái đều là 1 biến hoa ($S \to \dots, A \to \dots$): Chắc chắn ít nhất là **Loại 2 (CFG)**.
> 3. Kiểm tra xem có phải **Loại 3** không:
>    - Nếu vế phải chỉ có dạng: chữ thường đứng trước biến hoa ($A \to aB$ hoặc $A \to a$) $\implies$ Tuyến tính phải $\implies$ **Loại 3**.
>    - Nếu vế phải biến hoa đứng trước chữ thường ($A \to Ba$ hoặc $A \to a$) $\implies$ Tuyến tính trái $\implies$ **Loại 3**.
>    - Nếu biến hoa bị kẹp ở giữa (ví dụ $S \to aSb$) hoặc vừa có tuyến tính trái vừa có tuyến tính phải $\implies$ **Dừng lại ở Loại 2 (CFG)**!

---

# PHẦN 1: CÁC DẠNG BÀI TẬP VÀ NGÂN HÀNG CÂU HỎI TRẮC NGHIỆM

---

## DẠNG 1: PHÉP TOÁN TRÊN TỪ VÀ CHUỖI

#### Câu 1: Cho bảng chữ cái $\Sigma = \{a, b\}$. Số lượng từ có độ dài bằng 3 trên $\Sigma$ là:
- A. 6
- B. 8
- C. 9
- D. 7
👉 **Đáp án: B**
- **Giải thích:** Mỗi vị trí có 2 khả năng chọn ($a$ hoặc $b$). Chuỗi độ dài 3 có $2^3 = 8$ chuỗi: $\{aaa, aab, aba, abb, baa, bab, bba, bbb\}$.

#### Câu 2: Cho từ $u = ab$ và $v = baa$. Từ $w = u^2 v^R$ là:
- A. `abaabaa`
- B. `abab aab`
- C. `abab aab`
- D. `ababa`
👉 **Đáp án: B**
- **Giải thích:** $u^2 = uu = abab$. $v = baa \implies v^R = aab$. Ghép lại: $u^2 v^R = ababaab$.

#### Câu 3: Độ dài của chuỗi $w = (ab)^3 \varepsilon (ba)^2$ là:
- A. 10
- B. 11
- C. 9
- D. 12
👉 **Đáp án: A**
- **Giải thích:** $|(ab)^3| = 2 \times 3 = 6$. $|\varepsilon| = 0$. $|(ba)^2| = 2 \times 2 = 4$. Tổng độ dài $= 6 + 0 + 4 = 10$.

#### Câu 4: Cho từ $w = abcba$. Khẳng định nào sau đây là ĐÚNG?
- A. $w = w^R$ (chuỗi đối xứng / Palindrome)
- B. $|w| = 6$
- C. $ab$ là hậu tố của $w$
- D. $cb$ là tiền tố của $w$
👉 **Đáp án: A**
- **Giải thích:** $w^R = (abcba)^R = abcba = w$. Chuỗi bằng chính nó khi đảo ngược gọi là Palindrome (chuỗi đối xứng).

#### Câu 5: Số lượng tiền tố (prefix) phân biệt của từ $w = aab$ là:
- A. 3
- B. 4
- C. 5
- D. 2
👉 **Đáp án: B**
- **Giải thích:** Các tiền tố của $w = aab$ gồm: $\varepsilon$, $a$, $aa$, $aab$. Tổng cộng có 4 tiền tố phân biệt.

#### Câu 6: Cho $u, v$ là hai từ bất kỳ. Đẳng thức nào sau đây LUÔN ĐÚNG?
- A. $(uv)^R = u^R v^R$
- B. $(uv)^R = v^R u^R$
- C. $uv = vu$
- D. $|uv| = |u| \cdot |v|$
👉 **Đáp án: B**
- **Giải thích:** Đảo ngược của tích hai từ bằng tích đảo ngược theo thứ tự ngược lại: $(uv)^R = v^R u^R$.

#### Câu 7: Cho $w = 01001$. Số chuỗi con (substring) có độ dài bằng 2 của $w$ là:
- A. 4
- B. 3
- C. 5
- D. 2
👉 **Đáp án: B**
- **Giải thích:** Các đoạn con liên tiếp độ dài 2: `01`, `10`, `00`, `01`. Các chuỗi con **phân biệt** là $\{01, 10, 00\}$ (3 chuỗi phân biệt).

#### Câu 8: Chuỗi rỗng $\varepsilon$ có tính chất nào sau đây?
- A. $|\varepsilon| = 1$
- B. $\varepsilon^R = \varepsilon$ và $\varepsilon w = w \varepsilon = w$
- C. $\varepsilon = \emptyset$
- D. Không thể ghép $\varepsilon$ với từ khác
👉 **Đáp án: B**
- **Giải thích:** $\varepsilon$ là phần tử trung hòa của phép ghép từ.

#### Câu 9: Cho $w = a^n b^m$. Đảo ngược $w^R$ là:
- A. $a^n b^m$
- B. $b^n a^m$
- C. $b^m a^n$
- D. $a^m b^n$
👉 **Đáp án: C**
- **Giải thích:** $(a^n b^m)^R = (b^m)^R (a^n)^R = b^m a^n$.

#### Câu 10: Cho từ $w = abac$. Tập tất cả các hậu tố (suffixes) của $w$ là:
- A. $\{\varepsilon, c, ac, bac, abac\}$
- B. $\{c, ac, bac, abac\}$
- C. $\{\varepsilon, a, ab, aba, abac\}$
- D. $\{a, b, c\}$
👉 **Đáp án: A**
- **Giải thích:** Hậu tố là các phần đuôi, luôn tính cả chuỗi rỗng $\varepsilon$.

---

## DẠNG 2: PHÉP TOÁN TRÊN TẬP NGÔN NGỮ

#### Câu 11: Cho $L_1 = \{a, ab\}$ và $L_2 = \{\varepsilon, b\}$. Phép ghép ngôn ngữ $L_1 L_2$ là:
- A. $\{a, ab, abb\}$
- B. $\{ab, abb\}$
- C. $\{a, ab, ba, abb\}$
- D. $\{a, b, ab\}$
👉 **Đáp án: A**
- **Giải thích:** Ghép từng phần tử của $L_1$ với $L_2$:
  - $a \cdot \varepsilon = a$
  - $a \cdot b = ab$
  - $ab \cdot \varepsilon = ab$
  - $ab \cdot b = abb$
  Tập hợp kết quả: $\{a, ab, abb\}$.

#### Câu 12: Khẳng định nào sau đây là SAI về ngôn ngữ rỗng $\emptyset$ và $\{\varepsilon\}$?
- A. $|\emptyset| = 0$ và $|\{\varepsilon\}| = 1$
- B. $L \cdot \emptyset = \emptyset \cdot L = \emptyset$
- C. $L \cdot \{\varepsilon\} = \{\varepsilon\} \cdot L = L$
- D. $\emptyset^* = \emptyset$
👉 **Đáp án: D**
- **Giải thích:** $\emptyset^* = \{\varepsilon\}$ (bao đóng Kleene của bất kỳ tập nào cũng luôn chứa từ rỗng $\varepsilon$, do $\emptyset^0 = \{\varepsilon\}$). Do đó D là SAI.

#### Câu 13: Cho ngôn ngữ $L = \{a, b\}$. Ngôn ngữ $L^2$ là:
- A. $\{a^2, b^2\}$
- B. $\{aa, ab, ba, bb\}$
- C. $\{a, b, aa, bb\}$
- D. $\{aaa, bbb\}$
👉 **Đáp án: B**
- **Giải thích:** $L^2 = L \cdot L = \{aa, ab, ba, bb\}$.

#### Câu 14: Cho $L$ là một ngôn ngữ bất kỳ. Khẳng định nào sau đây LUÔN ĐÚNG?
- A. $\varepsilon \in L^+$
- B. $\varepsilon \in L^*$
- C. $L^* = L^+$
- D. $L \subseteq L^2$
👉 **Đáp án: B**
- **Giải thích:** Theo định nghĩa bao đóng Kleene, $L^* = L^0 \cup L^1 \cup \dots$, mà $L^0 = \{\varepsilon\}$, nên $\varepsilon$ luôn luôn thuộc $L^*$.

#### Câu 15: Cho ngôn ngữ $L = \{ab\}$. Ngôn ngữ $L^*$ là:
- A. $\{(ab)^n \mid n \ge 0\}$
- B. $\{a^n b^n \mid n \ge 0\}$
- C. $\{(ab)^n \mid n \ge 1\}$
- D. $\{a^* b^*\}$
👉 **Đáp án: A**
- **Giải thích:** $L^* = \{\varepsilon, ab, abab, ababab, \dots\} = \{(ab)^n \mid n \ge 0\}$.

#### Câu 16: Điều kiện để $L^+ = L^*$ là:
- A. $L = \emptyset$
- B. $\varepsilon \in L$
- C. $L$ là vô hạn
- D. Không bao giờ xảy ra
👉 **Đáp án: B**
- **Giải thích:** Vì $L^* = L^+ \cup \{\varepsilon\}$. Nếu bản thân $L$ đã có chứa $\varepsilon$ thì $L^+$ cũng đã chứa $\varepsilon$, do đó $L^+ = L^*$.

#### Câu 17: Cho $\Sigma = \{0, 1\}$. Ngôn ngữ $\Sigma^*$ là:
- A. Tập tất cả các chuỗi nhị phân (kể cả chuỗi rỗng $\varepsilon$)
- B. Tập tất cả các chuỗi nhị phân có độ dài $\ge 1$
- C. Tập các chuỗi chỉ chứa số 0 hoặc số 1
- D. Tập rỗng
👉 **Đáp án: A**
- **Giải thích:** $\Sigma^*$ là tập vũ trụ của tất cả các chuỗi tạo từ $\Sigma$.

#### Câu 18: Cho $L = \{a^n b^n \mid n \ge 1\}$. Ngôn ngữ bù $\overline{L} = \Sigma^* \setminus L$ (với $\Sigma = \{a, b\}$) có chứa chuỗi nào sau đây?
- A. `ab`
- B. `aabb`
- C. $\varepsilon$
- D. `aaabbb`
👉 **Đáp án: C**
- **Giải thích:** Vì $n \ge 1$ nên chuỗi rỗng $\varepsilon$ không thuộc $L$. Do đó $\varepsilon \in \overline{L}$. Còn `ab`, `aabb`, `aaabbb` đều thuộc $L$.

#### Câu 19: Cho hai ngôn ngữ $L_1$ và $L_2$. Đẳng thức nào sau đây KHÔNG ĐÚNG?
- A. $(L_1^*)^* = L_1^*$
- B. $(L_1 \cup L_2)^* = (L_1^* L_2^*)^*$
- C. $(L_1 L_2)^* = L_1^* L_2^*$
- D. $\emptyset^* = \{\varepsilon\}$
👉 **Đáp án: C**
- **Giải thích:** $(L_1 L_2)^*$ KHÔNG bằng $L_1^* L_2^*$. Ví dụ: $L_1 = \{a\}, L_2 = \{b\} \implies L_1^* L_2^* = a^* b^*$ (các chữ $a$ đứng trước các chữ $b$). Trong khi $(L_1 L_2)^* = (ab)^*$ (xen kẽ `ab`).

#### Câu 20: Cho $L = \{a, aa\}$. Ngôn ngữ $L^3$ chứa bao nhiêu phần tử?
- A. 8
- B. 4
- C. 6
- D. 5
👉 **Đáp án: B**
- **Giải thích:** Ghép 3 lần: $a^{1+1+1} = a^3$, $a^{1+1+2} = a^4$, $a^{1+2+2} = a^5$, $a^{2+2+2} = a^6$. Các phần tử phân biệt là $\{a^3, a^4, a^5, a^6\}$ (4 phần tử).

---

## DẠNG 3: PHÂN LOẠI VĂN PHẠM THEO CHOMSKY (LOẠI 0, 1, 2, 3)

#### Câu 21: Cho văn phạm $G$ có tập quy tắc: $S \to aSb \mid ab$. Phân lớp Chomsky thấp nhất của $G$ là:
- A. Loại 3 (Chính quy)
- B. Loại 2 (Phi ngữ cảnh)
- C. Loại 1 (Cảm ngữ cảnh)
- D. Loại 0
👉 **Đáp án: B**
- **Giải thích:**
  - Vế trái chỉ có 1 biến $S$ $\implies$ Ít nhất là Loại 2.
  - Vế phải có $aSb$ biến $S$ bị kẹp giữa $a$ và $b$ $\implies$ Không tuyến tính trái cũng không tuyến tính phải $\implies$ Không phải Loại 3.
  - Vậy phân lớp thấp nhất là **Loại 2 (CFG)**.

#### Câu 22: Cho văn phạm $G$ có tập quy tắc: $S \to aS \mid bA,\ A \to bA \mid b$. Văn phạm $G$ thuộc loại nào?
- A. Loại 3 (Tuyến tính phải)
- B. Loại 2 nhưng không chính quy
- C. Loại 1
- D. Loại 0
👉 **Đáp án: A**
- **Giải thích:** Mọi luật đều có dạng $X \to aY$ hoặc $X \to a$ (biến luôn đứng bên phải sau ký tự kết thúc) $\implies$ Văn phạm tuyến tính phải $\implies$ **Loại 3**.

#### Câu 23: Cho văn phạm $G$ có tập quy tắc: $S \to Sa \mid Ab,\ A \to Aa \mid a$. Văn phạm $G$ thuộc loại nào?
- A. Tuyến tính phải
- B. Tuyến tính trái (Loại 3)
- C. Loại 2 không chính quy
- D. Loại 1
👉 **Đáp án: B**
- **Giải thích:** Biến hoa luôn đứng ở đầu bên trái ($X \to Ya$ hoặc $X \to a$) $\implies$ Tuyến tính trái $\implies$ **Loại 3**.

#### Câu 24: Cho văn phạm $G$ có các luật: $S \to aS \mid Ba,\ B \to b$. Văn phạm này thuộc loại nào?
- A. Loại 3
- B. Loại 2 (Phi ngữ cảnh)
- C. Loại 1
- D. Loại 0
👉 **Đáp án: B**
- **Giải thích:** Luật $S \to aS$ là tuyến tính phải, nhưng luật $S \to Ba$ là tuyến tính trái. **Một văn phạm vừa chứa luật tuyến tính phải vừa chứa luật tuyến tính trái thì KHÔNG ĐƯỢC COI LÀ LOẠI 3!** Nó chỉ là **Loại 2 (CFG)**.

#### Câu 25: Cho văn phạm $G$ có luật: $aA \to ba,\ S \to aA$. Phân lớp Chomsky thấp nhất của $G$ là:
- A. Loại 3
- B. Loại 2
- C. Loại 1 (Cảm ngữ cảnh)
- D. Loại 0
👉 **Đáp án: C**
- **Giải thích:**
  - Luật $aA \to ba$ có vế trái gồm 2 ký hiệu ($|aA| = 2$) $\implies$ Không thể là Loại 2 hay Loại 3.
  - Độ dài vế trái $|aA| = 2$, độ dài vế phải $|ba| = 2 \implies |\alpha| \le |\beta|$ thỏa mãn.
  - Luật $S \to aA$ có $|S| = 1 \le |aA| = 2$ thỏa mãn.
  - Vậy phân lớp thấp nhất là **Loại 1 (Cảm ngữ cảnh)**.

#### Câu 26: Cho văn phạm $G$ có luật: $AB \to a,\ S \to AB$. Phân lớp Chomsky thấp nhất của $G$ là:
- A. Loại 1
- B. Loại 0 (Cấu trúc ngữ)
- C. Loại 2
- D. Loại 3
👉 **Đáp án: B**
- **Giải thích:** Luật $AB \to a$ có vế trái độ dài 2 ($|AB|=2$), nhưng vế phải độ dài chỉ bằng 1 ($|a|=1$). Vi phạm điều kiện $|\alpha| \le |\beta|$ của Loại 1 $\implies$ Rơi xuống **Loại 0**.

#### Câu 27: Mối quan hệ bao hàm giữa các lớp ngôn ngữ theo Chomsky là:
- A. $L_{\text{Loại 3}} \subset L_{\text{Loại 2}} \subset L_{\text{Loại 1}} \subset L_{\text{Loại 0}}$
- B. $L_{\text{Loại 0}} \subset L_{\text{Loại 1}} \subset L_{\text{Loại 2}} \subset L_{\text{Loại 3}}$
- C. $L_{\text{Loại 3}} = L_{\text{Loại 2}}$
- D. $L_{\text{Loại 1}} \subset L_{\text{Loại 2}}$
👉 **Đáp án: A**
- **Giải thích:** Chính quy (Loại 3) hẹp nhất, nằm trong Phi ngữ cảnh (Loại 2), nằm trong Cảm ngữ cảnh (Loại 1), nằm trong Cấu trúc ngữ (Loại 0).

#### Câu 28: Văn phạm nào sau đây là văn phạm chính quy (Loại 3)?
- A. $S \to aSb \mid \varepsilon$
- B. $S \to 0S \mid 1A,\ A \to 0A \mid \varepsilon$
- C. $S \to aS \mid Sa \mid a$
- D. $S \to SS \mid a$
👉 **Đáp án: B**
- **Giải thích:** B gồm toàn các luật tuyến tính phải chuẩn.

#### Câu 29: Cho văn phạm $G$ có $P = \{ S \to aB,\ B \to bC,\ C \to c \}$. Ngôn ngữ sinh bởi $G$ chỉ gồm đúng 1 từ là:
- A. `abc`
- B. `a`
- C. `cba`
- D. $\varepsilon$
👉 **Đáp án: A**
- **Giải thích:** $S \Rightarrow aB \Rightarrow abC \Rightarrow abc$.

#### Câu 30: Trong văn phạm phi ngữ cảnh (CFG - Loại 2), vế trái của mọi quy tắc sinh bắt buộc phải là:
- A. Một chuỗi ký tự kết thúc
- B. Đúng một biến chưa kết thúc (Non-terminal)
- C. Một chuỗi có độ dài nhỏ hơn vế phải
- D. Biến bắt đầu $S$
👉 **Đáp án: B**
- **Giải thích:** Định nghĩa CFG: mọi luật có dạng $A \to \alpha$ với $A \in \Delta$.

---

## DẠNG 4: NGÔN NGỮ SINH BỞI VĂN PHẠM & KIỂM TRA CHUỖI

#### Câu 31: Cho văn phạm $G$ có $P = \{ S \to 0S1 \mid \varepsilon \}$. Ngôn ngữ $L(G)$ là:
- A. $\{ 0^n 1^n \mid n \ge 1 \}$
- B. $\{ 0^n 1^n \mid n \ge 0 \}$
- C. $\{ (01)^n \mid n \ge 0 \}$
- D. $\{ 0^n 1^m \mid n, m \ge 0 \}$
👉 **Đáp án: B**
- **Giải thích:** Vì có luật $S \to \varepsilon$ nên chuỗi rỗng ($n=0$) được chấp nhận $\implies n \ge 0$.

#### Câu 32: Cho văn phạm $G$ có $P = \{ S \to aS \mid a \}$. Ngôn ngữ $L(G)$ là:
- A. $a^*$
- B. $a^+$ (tức $\{a^n \mid n \ge 1\}$)
- C. $\{a\}$
- D. $\{a^2\}$
👉 **Đáp án: B**
- **Giải thích:** Không có luật $S \to \varepsilon$, nên chuỗi ngắn nhất là $a$, sinh được mọi chuỗi $a, aa, aaa,\dots \implies a^+$.

#### Câu 33: Cho văn phạm $G$ có $P = \{ S \to aA,\ A \to bS \mid c \}$. Chuỗi nào sau đây thuộc $L(G)$?
- A. `abc`
- B. `abac`
- C. `ababc`
- D. Cả B và C đều thuộc $L(G)$
👉 **Đáp án: D**
- **Giải thích:**
  - $S \Rightarrow aA \Rightarrow a(bS) = abS \Rightarrow ab(aA) \Rightarrow aba(c) = abac$.
  - Lặp thêm 1 lần $ab$ nữa ta được `ababc`. Cả 2 đều thuộc $L(G)$.

#### Câu 34: Cho văn phạm $G$ có $P = \{ S \to aSb \mid aAb,\ A \to c \}$. Chuỗi ngắn nhất thuộc $L(G)$ là:
- A. `ab`
- B. `acb`
- C. `c`
- D. `aacbb`
👉 **Đáp án: B**
- **Giải thích:** $S \Rightarrow aAb \Rightarrow acb$ (độ dài 3).

#### Câu 35: Cho văn phạm $G$ có $P = \{ S \to aS \mid bS \mid a \}$. Ngôn ngữ $L(G)$ là tập hợp các chuỗi:
- A. Bắt đầu bằng chữ $a$
- B. Kết thúc bằng chữ $a$
- C. Chứa ít nhất một chữ $a$
- D. Có độ dài lẻ
👉 **Đáp án: B**
- **Giải thích:** $S \to aS$ hay $bS$ cứ thêm ký tự vào đầu, nhưng luật kết thúc duy nhất là $S \to a$ đặt ở vị trí cuối cùng $\implies$ Mọi chuỗi sinh ra đều **kết thúc bằng chữ $a$**.

#### Câu 36: Dẫn xuất trái nhất (Leftmost derivation) là dẫn xuất mà tại mỗi bước:
- A. Luôn thay thế biến chưa kết thúc ở vị trí ngoài cùng bên trái
- B. Luôn thay thế biến chưa kết thúc ở vị trí ngoài cùng bên phải
- C. Luôn thay thế biến $S$
- D. Luôn sinh ra ký tự ở bên trái
👉 **Đáp án: A**
- **Giải thích:** Định nghĩa: Leftmost derivation ưu tiên thay thế Non-terminal nằm xa nhất về bên trái.

#### Câu 37: Cho văn phạm $G$ có $P = \{ S \to aB \mid bA,\ A \to a \mid aS \mid bAA,\ B \to b \mid bS \mid aBB \}$. Ngôn ngữ do $G$ sinh ra là:
- A. Tập các chuỗi có số chữ $a$ bằng số chữ $b$ và độ dài $\ge 2$
- B. Tập các chuỗi có số chữ $a$ bằng số chữ $b$ ($|w|_a = |w|_b \ge 1$)
- C. Tập các chuỗi bắt đầu bằng $a$
- D. Tập các chuỗi Palindrome
👉 **Đáp án: B**
- **Giải thích:** Đây là văn phạm kinh điển sinh ra ngôn ngữ tất cả các chuỗi có số lượng chữ $a$ bằng số lượng chữ $b$ khác rỗng.

#### Câu 38: Cho văn phạm $G$ có $P = \{ S \to 1S00 \mid 100 \}$. Chuỗi nào sau đây thuộc $L(G)$?
- A. `110000`
- B. `111000000`
- C. `100`
- D. Tất cả các chuỗi trên
👉 **Đáp án: D**
- **Giải thích:** Dạng tổng quát là $1^n 0^{2n}$ với $n \ge 1$.
  - $n=1 \implies 100$
  - $n=2 \implies 110000$
  - $n=3 \implies 111000000$.

#### Câu 39: Cho văn phạm $G$ có $P = \{ S \to aA,\ A \to b \}$. Có bao nhiêu dẫn xuất khác nhau để sinh ra chuỗi `ab`?
- A. 1
- B. 2
- C. 0
- D. Vô số
👉 **Đáp án: A**
- **Giải thích:** Chỉ có duy nhất 1 đường: $S \Rightarrow aA \Rightarrow ab$.

#### Câu 40: Hai văn phạm $G_1$ và $G_2$ được gọi là tương đương nhau khi và chỉ khi:
- A. Chúng có cùng tập luật sinh $P$
- B. Chúng có cùng tập biến $\Delta$
- C. Ngôn ngữ sinh ra bởi chúng bằng nhau ($L(G_1) = L(G_2)$)
- D. Chúng thuộc cùng một phân lớp Chomsky
👉 **Đáp án: C**
- **Giải thích:** Định nghĩa tương đương của văn phạm là tạo ra cùng một tập ngôn ngữ.

---

## DẠNG 5: XÂY DỰNG VĂN PHẠM CHO NGÔN NGỮ

#### Câu 41: Văn phạm nào sau đây sinh ra ngôn ngữ $L = \{ a^n b^n \mid n \ge 1 \}$?
- A. $S \to aSb \mid ab$
- B. $S \to aSb \mid \varepsilon$
- C. $S \to ab$
- D. $S \to aS \mid b$
👉 **Đáp án: A**
- **Giải thích:** Luật dừng là $S \to ab$ đảm bảo $n \ge 1$ (không có từ rỗng).

#### Câu 42: Văn phạm nào sau đây sinh ra ngôn ngữ các chuỗi Palindrome chẵn trên $\{a, b\}$: $L = \{ w w^R \mid w \in \{a, b\}^* \}$?
- A. $S \to aSa \mid bSb \mid \varepsilon$
- B. $S \to aSa \mid bSb \mid a \mid b \mid \varepsilon$
- C. $S \to aSb \mid bSa \mid \varepsilon$
- D. $S \to abS \mid baS \mid \varepsilon$
👉 **Đáp án: A**
- **Giải thích:** Mỗi bước thêm cùng 1 ký tự ở 2 đầu ($aSa$ hoặc $bSb$), dừng bằng $\varepsilon$ nên độ dài luôn chẵn.

#### Câu 43: Văn phạm nào sau đây sinh ra ngôn ngữ các chuỗi Palindrome tùy ý (cả chẵn và lẻ) trên $\{a, b\}$?
- A. $S \to aSa \mid bSb \mid \varepsilon$
- B. $S \to aSa \mid bSb \mid a \mid b \mid \varepsilon$
- C. $S \to aSb \mid \varepsilon$
- D. $S \to aS \mid bS \mid \varepsilon$
👉 **Đáp án: B**
- **Giải thích:** Có thêm luật $S \to a \mid b$ để tạo ra tâm đối xứng có độ dài lẻ.

#### Câu 44: Văn phạm tuyến tính phải sinh ra ngôn ngữ $L = \{ a^n b \mid n \ge 0 \}$ là:
- A. $S \to aS \mid b$
- B. $S \to Sa \mid b$
- C. $S \to aSb \mid \varepsilon$
- D. $S \to aB,\ B \to b$
👉 **Đáp án: A**
- **Giải thích:** $S \Rightarrow aS \Rightarrow aaS \dots \Rightarrow a^n S \Rightarrow a^n b$.

#### Câu 45: Văn phạm sinh ra ngôn ngữ $L = \{ a^n b^{2n} \mid n \ge 1 \}$ là:
- A. $S \to aSbb \mid abb$
- B. $S \to aaSb \mid aab$
- C. $S \to aSbb \mid \varepsilon$
- D. $S \to aSb \mid ab$
👉 **Đáp án: A**
- **Giải thích:** Mỗi lần sinh 1 chữ $a$ ở đầu thì sinh 2 chữ $b$ ở đuôi. Dừng bằng $abb$ để $n \ge 1$.

---

## DẠNG 6: MỆNH ĐỀ LÝ THUYẾT ĐÚNG / SAI TỔNG HỢP

#### Câu 46: Khẳng định nào sau đây là ĐÚNG?
- A. Mọi văn phạm chính quy đều là văn phạm phi ngữ cảnh
- B. Mọi văn phạm phi ngữ cảnh đều là văn phạm chính quy
- C. Ngôn ngữ phi ngữ cảnh không thể được sinh bởi văn phạm loại 1
- D. Văn phạm loại 0 có tập luật sinh rỗng
👉 **Đáp án: A**
- **Giải thích:** Vì Loại 3 $\subset$ Loại 2, nên mọi văn phạm chính quy đều thỏa mãn điều kiện của văn phạm phi ngữ cảnh.

#### Câu 47: Khẳng định nào sau đây là SAI?
- A. Ngôn ngữ $L = \{ a^n b^n \mid n \ge 0 \}$ là ngôn ngữ chính quy
- B. Ngôn ngữ $L = \{ a^n b^n \mid n \ge 0 \}$ là ngôn ngữ phi ngữ cảnh
- C. Ngôn ngữ $L = \{ a^n \mid n \ge 0 \}$ là ngôn ngữ chính quy
- D. Ngôn ngữ $\{ab, ba\}$ là ngôn ngữ hữu hạn và chính quy
👉 **Đáp án: A**
- **Giải thích:** $a^n b^n$ đòi hỏi bộ nhớ vô hạn để đếm số lượng $a$ bằng số lượng $b$, ô-tô-mát hữu hạn không nhận diện được, nên nó **KHÔNG PHẢI là ngôn ngữ chính quy** mà là ngôn ngữ phi ngữ cảnh.

#### Câu 48: Văn phạm có luật $S \to \varepsilon$ thì ngôn ngữ sinh ra $L(G)$ chắc chắn:
- A. Chứa từ rỗng $\varepsilon$
- B. Là tập rỗng
- C. Là ngôn ngữ vô hạn
- D. Không thể là văn phạm loại 2
👉 **Đáp án: A**
- **Giải thích:** $S \Rightarrow \varepsilon \implies \varepsilon \in L(G)$.

#### Câu 49: Nếu $L$ là một ngôn ngữ hữu hạn (chỉ chứa một số hữu hạn các từ), thì $L$ chắc chắn là:
- A. Ngôn ngữ chính quy (Loại 3)
- B. Ngôn ngữ phi ngữ cảnh nhưng không chính quy
- C. Ngôn ngữ loại 1
- D. Không xác định được
👉 **Đáp án: A**
- **Giải thích:** Mọi ngôn ngữ hữu hạn đều là ngôn ngữ chính quy (vì luôn viết được biểu thức chính quy bằng phép hội các từ đó).

#### Câu 50: Trong định nghĩa văn phạm $G = \langle \Sigma, \Delta, S, P \rangle$, điều kiện bắt buộc giữa $\Sigma$ và $\Delta$ là:
- A. $\Sigma \cap \Delta = \emptyset$ (tập ký hiệu kết thúc và tập biến phải rời nhau)
- B. $\Sigma \subseteq \Delta$
- C. $\Delta \subseteq \Sigma$
- D. $\Sigma \cup \Delta = \emptyset$
👉 **Đáp án: A**
- **Giải thích:** Chữ thường (terminal) và chữ hoa (non-terminal) phải hoàn toàn phân biệt, không được trùng nhau.
