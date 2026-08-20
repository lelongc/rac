# BÀI GIẢI CHI TIẾT BÀI TẬP CHƯƠNG 1

### BÀI 1

**Hãy đưa ra 5 chuỗi có độ dài ngắn nhất (theo thứ tự từ điển với quy ước chuỗi rỗng đứng trước, tiếp đến là chuỗi có chiều dài tăng dần) của các ngôn ngữ $L_i$ trên $\Sigma = \{a, b\}$ sau:**
*(Quy ước: ký hiệu $u^{-1}$ trong đề tương đương với phép đảo ngược chuỗi $u^R$)*

#### a) $L_1 = \{ uuu^{-1} \mid u \in \Sigma^* \}$

- Xét các chuỗi $u \in \Sigma^*$ theo thứ tự độ dài tăng dần:
  - $|u| = 0: u = \lambda \Rightarrow uuu^{-1} = \lambda$ (độ dài 0)
  - $|u| = 1:$
    - $u = a \Rightarrow uuu^{-1} = aaa$ (độ dài 3)
    - $u = b \Rightarrow uuu^{-1} = bbb$ (độ dài 3)
  - $|u| = 2:$
    - $u = aa \Rightarrow uuu^{-1} = aaaaaa$ (độ dài 6)
    - $u = ab \Rightarrow uuu^{-1} = (ab)(ab)(ba) = ababba$ (độ dài 6)
    - $u = ba \Rightarrow uuu^{-1} = (ba)(ba)(ab) = babaab$ (độ dài 6)
    - $u = bb \Rightarrow uuu^{-1} = (bb)(bb)(bb) = bbbbbb$ (độ dài 6)

Sắp xếp 5 chuỗi theo thứ tự độ dài tăng dần và thứ tự từ điển:

$$
\lambda; \ aaa; \ bbb; \ aaaaaa; \ ababba
$$

---

#### b) $L_2 = \{ u^{-1}uu \mid u \in \Sigma^* \}$

- Xét các chuỗi $u \in \Sigma^*$ theo thứ tự độ dài tăng dần:
  - $|u| = 0: u = \lambda \Rightarrow u^{-1}uu = \lambda$ (độ dài 0)
  - $|u| = 1:$
    - $u = a \Rightarrow u^{-1}uu = aaa$ (độ dài 3)
    - $u = b \Rightarrow u^{-1}uu = bbb$ (độ dài 3)
  - $|u| = 2:$
    - $u = aa \Rightarrow u^{-1}uu = aaaaaa$ (độ dài 6)
    - $u = ba \Rightarrow u^{-1} = ab \Rightarrow u^{-1}uu = (ab)(ba)(ba) = abbaba$ (độ dài 6)
    - $u = ab \Rightarrow u^{-1} = ba \Rightarrow u^{-1}uu = (ba)(ab)(ab) = baabab$ (độ dài 6)
    - $u = bb \Rightarrow u^{-1}uu = (bb)(bb)(bb) = bbbbbb$ (độ dài 6)

5 chuỗi ngắn nhất của ngôn ngữ $L_2$ sắp xếp theo đúng yêu cầu là:

$$
\lambda; \ aaa; \ bbb; \ aaaaaa; \ abbaba
$$

---

#### c) $L_3 = \{ uau^{-1} \mid u \in \Sigma^* \}$

- Xét các chuỗi $u \in \Sigma^*$ theo thứ tự độ dài tăng dần:
  - $|u| = 0: u = \lambda \Rightarrow uau^{-1} = \lambda a \lambda = a$ (độ dài 1)
  - $|u| = 1:$
    - $u = a \Rightarrow uau^{-1} = a \cdot a \cdot a = aaa$ (độ dài 3)
    - $u = b \Rightarrow uau^{-1} = b \cdot a \cdot b = bab$ (độ dài 3)
  - $|u| = 2:$
    - $u = aa \Rightarrow uau^{-1} = aa \cdot a \cdot aa = aaaaa$ (độ dài 5)
    - $u = ab \Rightarrow uau^{-1} = ab \cdot a \cdot ba = ababa$ (độ dài 5)
    - $u = ba \Rightarrow uau^{-1} = ba \cdot a \cdot ab = baaab$ (độ dài 5)
    - $u = bb \Rightarrow uau^{-1} = bb \cdot a \cdot bb = bbabb$ (độ dài 5)

5 chuỗi ngắn nhất của ngôn ngữ $L_3$ sắp xếp theo đúng yêu cầu là:

$$
a; \ aaa; \ bab; \ aaaaa; \ ababa
$$

---

### BÀI 2

**Hãy đưa ra 5 chuỗi có độ dài ngắn nhất (theo thứ tự từ điển với quy ước chuỗi rỗng đứng trước, chiều dài tăng dần) và xác định tính chất (mô tả ngôn ngữ) của những văn phạm sau:**

---

#### a) Cho văn phạm $G_1 = (V, T, S, P)$ với: $V = \{S\}$, $T = \{a, b\}$, $P = \{S \to Sa \mid Sb \mid \lambda\}$

**1. Các bước dẫn xuất sinh ra 5 chuỗi có độ dài ngắn nhất (theo thứ tự từ điển):**

- **Chuỗi 1 (độ dài 0):** $S \Rightarrow \lambda$
- **Chuỗi 2 (độ dài 1):** $S \Rightarrow Sa \Rightarrow \lambda a = a$
- **Chuỗi 3 (độ dài 1):** $S \Rightarrow Sb \Rightarrow \lambda b = b$
- **Chuỗi 4 (độ dài 2):** $S \Rightarrow Sa \Rightarrow Saa \Rightarrow \lambda aa = aa$
- **Chuỗi 5 (độ dài 2):** $S \Rightarrow Sb \Rightarrow Sab \Rightarrow \lambda ab = ab$

**2. Danh sách 5 chuỗi ngắn nhất sắp xếp theo yêu cầu:**

$$
\lambda \text{ (độ dài 0)}; \quad a \text{ (độ dài 1)}; \quad b \text{ (độ dài 1)}; \quad aa \text{ (độ dài 2)}; \quad ab \text{ (độ dài 2)}
$$

**3. Xác định tính chất (mô tả ngôn ngữ):**

- **Phân tích cơ chế sinh:**
  - Quy tắc $S \to Sa$ cho phép nối thêm ký tự '$a$' vào phía sau của chuỗi hiện tại.
  - Quy tắc $S \to Sb$ cho phép nối thêm ký tự '$b$' vào phía sau của chuỗi hiện tại.
  - Quy tắc $S \to \lambda$ dùng để khử biến $S$ và kết thúc quá trình dẫn xuất.
- **Mô tả bằng lời:** Ngôn ngữ được sinh ra bởi văn phạm $G_1$ là tập hợp tất cả các chuỗi có thể được tạo thành từ bảng chữ cái $\{a, b\}$, bao gồm cả chuỗi rỗng.
- **Biểu diễn tập hợp:**
  $$
  L(G_1) = \Sigma^* = \{a, b\}^*
  $$

---

#### b) Cho văn phạm $G_2 = (V, T, S, P)$ với: $V = \{S\}$, $T = \{a, b\}$, $P = \{S \to aSa \mid bSb \mid a \mid b \mid \lambda\}$

**1. Các bước dẫn xuất sinh ra 5 chuỗi có độ dài ngắn nhất (theo thứ tự từ điển):**

- **Chuỗi 1 (độ dài 0):** $S \Rightarrow \lambda$
- **Chuỗi 2 (độ dài 1):** $S \Rightarrow a$
- **Chuỗi 3 (độ dài 1):** $S \Rightarrow b$
- **Chuỗi 4 (độ dài 2):** $S \Rightarrow aSa \Rightarrow a\lambda a = aa$
- **Chuỗi 5 (độ dài 2):** $S \Rightarrow bSb \Rightarrow b\lambda b = bb$

**2. Danh sách 5 chuỗi ngắn nhất sắp xếp theo yêu cầu:**

$$
\lambda \text{ (độ dài 0)}; \quad a \text{ (độ dài 1)}; \quad b \text{ (độ dài 1)}; \quad aa \text{ (độ dài 2)}; \quad bb \text{ (độ dài 2)}
$$

**3. Xác định tính chất (mô tả ngôn ngữ):**

- **Phân tích cơ chế sinh:**
  - Quy tắc $S \to aSa$ kẹp đồng thời hai ký tự '$a$' ở hai đầu chuỗi.
  - Quy tắc $S \to bSb$ kẹp đồng thời hai ký tự '$b$' ở hai đầu chuỗi.
  - Các quy tắc dừng: $S \to \lambda$ (kết thúc sinh chuỗi đối xứng độ dài chẵn), $S \to a$ hoặc $S \to b$ (kết thúc sinh chuỗi đối xứng độ dài lẻ có tâm là '$a$' hoặc '$b$').
- **Mô tả bằng lời:** Ngôn ngữ được sinh ra bởi văn phạm $G_2$ là tập hợp tất cả các chuỗi đối xứng (chuỗi Palindrome) trên bảng chữ cái $\{a, b\}$, nghĩa là chuỗi đọc xuôi hay đọc ngược đều hoàn toàn giống nhau.
- **Biểu diễn tập hợp:**
  $$
  L(G_2) = \{w \in \{a, b\}^* \mid w = w^R\}
  $$

---

#### c) Cho văn phạm $G_3 = (V, T, S, P)$ với: $V = \{S\}$, $T = \{a, b\}$, $P = \{S \to aSb \mid \lambda\}$

**1. Các bước dẫn xuất sinh ra 5 chuỗi có độ dài ngắn nhất (theo thứ tự từ điển):**

- **Chuỗi 1 (độ dài 0):** $S \Rightarrow \lambda$
- **Chuỗi 2 (độ dài 2):** $S \Rightarrow aSb \Rightarrow a\lambda b = ab$
- **Chuỗi 3 (độ dài 4):** $S \Rightarrow aSb \Rightarrow aaSbb \Rightarrow aa\lambda bb = aabb$
- **Chuỗi 4 (độ dài 6):** $S \Rightarrow aSb \Rightarrow aaSbb \Rightarrow aaaSbbb \Rightarrow aaa\lambda bbb = aaabbb$
- **Chuỗi 5 (độ dài 8):** $S \Rightarrow aSb \Rightarrow aaSbb \Rightarrow aaaSbbb \Rightarrow aaaaSbbbb \Rightarrow aaaa\lambda bbbb = aaaabbbb$

**2. Danh sách 5 chuỗi ngắn nhất sắp xếp theo yêu cầu:**

$$
\lambda \text{ (độ dài 0)}; \quad ab \text{ (độ dài 2)}; \quad aabb \text{ (độ dài 4)}; \quad aaabbb \text{ (độ dài 6)}; \quad aaaabbbb \text{ (độ dài 8)}
$$

**3. Xác định tính chất (mô tả ngôn ngữ):**

- **Phân tích cơ chế sinh:** Mỗi lần áp dụng quy tắc $S \to aSb$ sẽ sinh ra đúng 1 ký tự '$a$' ở phía bên trái và đúng 1 ký tự '$b$' ở phía bên phải. Do đó, số lượng ký tự '$a$' và '$b$' luôn bằng nhau và các ký tự '$a$' luôn đứng trước toàn bộ ký tự '$b$'. Dừng lại bằng $S \to \lambda$.
- **Mô tả bằng lời:** Ngôn ngữ sinh bởi văn phạm $G_3$ là tập hợp tất cả các chuỗi có $n$ ký tự '$a$' liên tiếp đứng trước, tiếp theo sau là đúng $n$ ký tự '$b$' liên tiếp, với $n \ge 0$.
- **Biểu diễn tập hợp:**
  $$
  L(G_3) = \{a^n b^n \mid n \ge 0\}
  $$

---

### BÀI 3

**Coi văn phạm $G = (V, T, S, P)$ với $V = \{S, B\}; \ T = \{a, b\}$; biến khởi đầu: $S$**
**Tập luật sinh $P: \{S \to aB; \ B \to bS; \ S \to \lambda\}$**
**Tìm 3 cặp chuỗi (mỗi cặp gồm 1 chuỗi được văn phạm chấp nhận và 1 chuỗi không được văn phạm chấp nhận) có chiều dài lần lượt là 2, 4 và 6.**

Ngôn ngữ sinh bởi văn phạm là tập hợp các chuỗi có dạng $(ab)^n$ với $n \ge 0$.

1. **Chiều dài 2:**

   - **Được chấp nhận:** $ab$ (vì $S \Rightarrow aB \Rightarrow abS \Rightarrow ab\lambda = ab$)
   - **Không được chấp nhận:** $aa$ (hoặc $ba, bb$)
2. **Chiều dài 4:**

   - **Được chấp nhận:** $abab$ (vì $S \Rightarrow aB \Rightarrow abS \Rightarrow abaB \Rightarrow ababS \Rightarrow abab$)
   - **Không được chấp nhận:** $aabb$ (hoặc $baab, aaaa$)
3. **Chiều dài 6:**

   - **Được chấp nhận:** $ababab$ (vì $S \Rightarrow^* (ab)^3 S \Rightarrow ababab$)
   - **Không được chấp nhận:** $baabab$ (hoặc $aaaaaa, aaabbb$)

---

### BÀI 4

**Coi văn phạm $G = (V, T, S, P)$ với $V = \{S, B\}; \ T = \{0, 1\}$; biến khởi đầu: $S$**
**Tập luật sinh $P: \{S \to 0A; \ A \to 1S; \ S \to \lambda\}$** 
**Tìm 3 cặp chuỗi (mỗi cặp gồm 1 chuỗi được văn phạm chấp nhận và 1 chuỗi không được văn phạm chấp nhận) có chiều dài lần lượt là 3, 5 và 7.**

> **Nhận xét lý thuyết về cấu trúc văn phạm:**
> Dãy dẫn xuất của văn phạm có dạng: $S \Rightarrow 0A \Rightarrow 01S \Rightarrow 010A \Rightarrow 0101S \Rightarrow \dots$
> Chuỗi kết thúc bắt buộc phải khử biến tại $S \to \lambda$, do đó số ký tự sinh ra luôn là số chẵn ($2k$ với $k \ge 0$).
> Vậy $L(G) = \{(01)^k \mid k \ge 0\} = \{\lambda, 01, 0101, 010101, \dots\}$.

Do văn phạm $G$ **chỉ sinh ra các chuỗi có chiều dài chẵn**, nên **không tồn tại chuỗi nào có chiều dài lẻ (3, 5, 7) được văn phạm chấp nhận**.


1. **Chiều dài 3:**
   - **Được chấp nhận:** Không có (do văn phạm chỉ sinh ra chuỗi có độ dài chẵn).
   - **Không được chấp nhận:** $010$ (hoặc $000, 111$).
2. **Chiều dài 5:**
   - **Được chấp nhận:** Không có.
   - **Không được chấp nhận:** $01010$ (hoặc $00000, 10101$).
3. **Chiều dài 7:**
   - **Được chấp nhận:** Không có.
   - **Không được chấp nhận:** $0101010$ (hoặc $0000000$).

---
