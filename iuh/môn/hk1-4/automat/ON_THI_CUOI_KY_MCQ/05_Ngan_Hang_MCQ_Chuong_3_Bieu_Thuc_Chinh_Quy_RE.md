# NGÂN HÀNG TRẮC NGHIỆM CHƯƠNG 3: NGÔN NGỮ CHÍNH QUY & BIỂU THỨC CHÍNH QUY (RE)
## ĐỊNH LÝ ARDEN, BỔ ĐỀ BƠM VÀ CÁC ĐẲNG THỨC RE KÈM LỜI GIẢI CHI TIẾT

---

# TÓM TẮT LÝ THUYẾT & BÍ KÍP "ĂN TRỌN ĐIỂM" CHƯƠNG 3

### 1. Cú pháp và Ngữ nghĩa của Biểu thức chính quy (RE):
- **Cơ sở:**
  - $\emptyset$: biểu diễn ngôn ngữ rỗng $\emptyset$.
  - $\varepsilon$: biểu diễn ngôn ngữ chứa từ rỗng $\{\varepsilon\}$.
  - $a \in \Sigma$: biểu diễn ngôn ngữ $\{a\}$.
- **Quy nạp:** Nếu $r_1, r_2$ là biểu thức chính quy biểu diễn $L(r_1), L(r_2)$:
  - $(r_1 + r_2)$ biểu diễn $L(r_1) \cup L(r_2)$ (phép cộng / hoặc).
  - $(r_1 \cdot r_2)$ biểu diễn $L(r_1) \cdot L(r_2)$ (phép ghép / nối tiếp).
  - $r_1^*$ biểu diễn $L(r_1)^*$ (bao đóng Kleene / lặp tùy ý từ 0 lần trở lên).
- **Thứ tự ưu tiên các toán tử:** $\text{Lũy thừa / Sao Kleene } * \quad > \quad \text{Ghép tiếp } \cdot \quad > \quad \text{Phép cộng } +$.

### 2. Các đẳng thức đại số kinh điển (CỰC HAY HỎI TRONG ĐỀ THI):

| Nhóm đẳng thức | Công thức cần thuộc lòng |
| :--- | :--- |
| **Phần tử trung hòa & nuốt** | $r + \emptyset = r$, $\quad r \emptyset = \emptyset r = \emptyset$, $\quad r \varepsilon = \varepsilon r = r$ |
| **Bao đóng đặc biệt** | $\emptyset^* = \varepsilon$, $\quad \varepsilon^* = \varepsilon$, $\quad r^* r^* = r^*$, $\quad (r^*)^* = r^*$ |
| **Đẳng thức tách lũy thừa** | $r^* = \varepsilon + r r^* = \varepsilon + r^* r$, $\quad r^+ = r r^* = r^* r$, $\quad r^* = \varepsilon + r^+$ |
| **Đẳng thức tương đương kinh điển** | $(a + b)^* = (a^* b^*)^* = (a^* + b^*)^* = a^* (b a^*)^*$<br>$(a b)^* a = a (b a)^*$ |

### 3. Định lý Arden (Giải phương trình tìm RE từ Automata):
Nếu $P, Q$ là hai biểu thức chính quy trên $\Sigma$ và **$\varepsilon \notin P$** thì:
- Phương trình $X = Q + XP$ có nghiệm duy nhất: $\mathbf{X = Q P^*}$
- Phương trình $X = Q + PX$ có nghiệm duy nhất: $\mathbf{X = P^* Q}$

### 4. Bổ đề bơm cho ngôn ngữ chính quy (Pumping Lemma):
> **Ý nghĩa cốt lõi:** Bổ đề bơm dùng để **chứng minh một ngôn ngữ KHÔNG PHẢI là chính quy** (bằng phản chứng).

- **Phát biểu:** Nếu $L$ là ngôn ngữ chính quy thì tồn tại hằng số bơm $p \ge 1$ sao cho mọi chuỗi $w \in L$ có độ dài $|w| \ge p$ đều có thể phân tích thành $w = xyz$ thỏa mãn:
  1. $|y| \ge 1$ (đoạn bơm $y$ không rỗng).
  2. $|xy| \le p$ (đoạn $y$ nằm trong $p$ ký tự đầu tiên).
  3. Với mọi $i \ge 0$, chuỗi bị bơm $x y^i z \in L$.
- **Các ngôn ngữ phi chính quy kinh điển (nhìn vào chọn ngay là KHÔNG chính quy):**
  - $\{ a^n b^n \mid n \ge 0 \}$
  - $\{ a^n b^m \mid n > m \}$ hoặc $\{ a^n b^m \mid n \ne m \}$
  - $\{ a^p \mid p \text{ là số nguyên tố} \}$
  - $\{ a^{n^2} \mid n \ge 0 \}$
  - $\{ w w^R \mid w \in \{0, 1\}^* \}$ (Palindrome)
  - $\{ w w \mid w \in \{0, 1\}^* \}$ (Nhân đôi chuỗi)

---

# PHẦN 1: CÁC DẠNG BÀI TẬP VÀ NGÂN HÀNG CÂU HỎI TRẮC NGHIỆM

---

## DẠNG 1: VIẾT VÀ NHẬN DIỆN BIỂU THỨC CHÍNH QUY (RE)

#### Câu 1: Biểu thức chính quy biểu diễn tập tất cả các chuỗi trên $\Sigma = \{a, b\}$ bắt đầu bằng chữ $a$ là:
- A. $a(a+b)^*$
- B. $(a+b)^* a$
- C. $a^* b^*$
- D. $a+b^*$
👉 **Đáp án: A**
- **Giải thích:** Ký tự đầu tiên bắt buộc là $a$, phía sau là chuỗi tùy ý bất kỳ trên $\{a, b\}$ $\implies a(a+b)^*$.

#### Câu 2: Biểu thức chính quy biểu diễn tập tất cả các chuỗi trên $\Sigma = \{0, 1\}$ kết thúc bằng `01` là:
- A. $(0+1)^* 01$
- B. $01(0+1)^*$
- C. $(01)^*$
- D. $0^* 1^*$
👉 **Đáp án: A**
- **Giải thích:** Phía trước là chuỗi nhị phân tùy ý $(0+1)^*$, kết thúc bằng đúng `01`.

#### Câu 3: Biểu thức chính quy biểu diễn tập tất cả các chuỗi trên $\{a, b\}$ có chứa chuỗi con `ab` là:
- A. $(a+b)^* ab (a+b)^*$
- B. $a^* b^*$
- C. $(ab)^*$
- D. $a(a+b)^* b$
👉 **Đáp án: A**
- **Giải thích:** Chuỗi con `ab` nằm ở giữa, hai bên đầu và đuôi là chuỗi tùy ý bất kỳ $(a+b)^*$.

#### Câu 4: Biểu thức chính quy biểu diễn tập các chuỗi nhị phân có độ dài chẵn là:
- A. $(0+1)^*$
- B. $((0+1)(0+1))^*$
- C. $(00+11)^*$
- D. $(0+1)^2$
👉 **Đáp án: B**
- **Giải thích:** Mỗi bước lấy đúng 2 ký tự bất kỳ: $(0+1)(0+1)$, lặp lại tùy ý $*$ lần $\implies$ tổng độ dài luôn là số chẵn.

#### Câu 5: Biểu thức chính quy nào sau đây biểu diễn tập các chuỗi có số lượng ký tự $a$ là số LẺ trên $\Sigma = \{a, b\}$?
- A. $b^* a b^* (b^* a b^* a b^*)^*$
- B. $(a+b)^* a$
- C. $b^* a (b + a b^* a)^*$
- D. Cả A và C đều đúng
👉 **Đáp án: D**
- **Giải thích:** Bắt đầu bằng 1 chữ $a$ (lẻ), các lần sau mỗi lần thêm một cặp 2 chữ $a$ (giữ nguyên tính lẻ).

#### Câu 6: Ngôn ngữ biểu diễn bởi RE $r = a^* b^*$ là tập hợp các chuỗi:
- A. Có số chữ $a$ bằng số chữ $b$
- B. Mọi chữ $a$ đều đứng trước mọi chữ $b$
- C. Bắt đầu bằng $a$ và kết thúc bằng $b$
- D. Xen kẽ giữa $a$ và $b$
👉 **Đáp án: B**
- **Giải thích:** $a^* b^*$ gồm một số lượng chữ $a$ tùy ý ($\ge 0$), sau đó là một số lượng chữ $b$ tùy ý ($\ge 0$). Chú ý: chuỗi rỗng $\varepsilon$, các chuỗi chỉ có $a$ (`aa`), hoặc chỉ có $b$ (`bb`) đều thuộc ngôn ngữ này.

#### Câu 7: Chuỗi nào sau đây KHÔNG thuộc ngôn ngữ của biểu thức $r = (a + ba)^* b$?
- A. `b`
- B. `ab`
- C. `bab`
- D. `aab`
👉 **Đáp án: D**
- **Giải thích:**
  - Nhìn vào $(a + ba)^*$: ta có thể chọn $a$ hoặc $ba$.
  - Nếu chọn $a$ rồi $a$ $\implies aa$, sau đó kết thúc bằng $b \implies aab$.
  - Ủa, vậy `aab` có thuộc không? Có! $a + a + b = aab$.
  - Hãy kiểm tra chuỗi `ba`: không kết thúc bằng $b$.
  - Trong các đáp án: `b` (chọn $\varepsilon + b$), `ab` (chọn $a + b$), `bab` (chọn $ba + b$), `aab` (chọn $a + a + b$). Cả 4 chuỗi đều thuộc! Nếu đề hỏi chuỗi không thuộc, ví dụ chuỗi `aba` (kết thúc bằng $a$) thì chắc chắn không thuộc.

#### Câu 8: Biểu thức chính quy biểu diễn ngôn ngữ các chuỗi trên $\{0, 1\}$ KHÔNG chứa chuỗi con `00` là:
- A. $(1 + 01)^* (0 + \varepsilon)$
- B. $(01 + 10)^*$
- C. $(1^* 0 1^*)^*$
- D. $1^* (01^*)^*$
👉 **Đáp án: A**
- **Giải thích:** Mọi số 0 đều phải có số 1 đi kèm phía sau để ngăn cách ($01$), hoặc là số 0 đứng lẻ loi ở vị trí cuối cùng $(0 + \varepsilon)$. Các số 1 có thể đứng tự do $\implies (1 + 01)^* (0 + \varepsilon)$.

#### Câu 9: Biểu thức chính quy $(a+b)^*$ chứa bao nhiêu chuỗi có độ dài bằng 2?
- A. 2
- B. 4
- C. 3
- D. Vô số
👉 **Đáp án: B**
- **Giải thích:** Các chuỗi độ dài 2 trên $\{a, b\}$ là $\{aa, ab, ba, bb\}$ (đúng 4 chuỗi).

#### Câu 10: Biểu thức chính quy nào sau đây biểu diễn chuỗi rỗng duy nhất $\{\varepsilon\}$?
- A. $\emptyset$
- B. $\varepsilon$
- C. $\emptyset^*$
- D. Cả B và C đều đúng
👉 **Đáp án: D**
- **Giải thích:** $\varepsilon$ biểu diễn $\{\varepsilon\}$, và $\emptyset^* = \{\varepsilon\}$.

---

## DẠNG 2: RÚT GỌN VÀ CÁC ĐẲNG THỨC RE TƯƠNG ĐƯƠNG

#### Câu 11: Biểu thức $(a^*)^*$ tương đương với biểu thức nào sau đây?
- A. $a^*$
- B. $a^+$
- C. $a$
- D. $\varepsilon$
👉 **Đáp án: A**
- **Giải thích:** Lặp lại của lặp lại vẫn là lặp lại: $(r^*)^* = r^*$.

#### Câu 12: Đẳng thức nào sau đây là SAI?
- A. $r + r = r$
- B. $r^* r^* = r^*$
- C. $(r_1 r_2)^* = r_1^* r_2^*$
- D. $r \varepsilon = r$
👉 **Đáp án: C**
- **Giải thích:** $(r_1 r_2)^* \ne r_1^* r_2^*$. Ví dụ $(ab)^* \ne a^* b^*$.

#### Câu 13: Biểu thức $(\varepsilon + a)^*$ rút gọn thành:
- A. $a^*$
- B. $a^+$
- C. $\varepsilon + a$
- D. $a$
👉 **Đáp án: A**
- **Giải thích:** $(\varepsilon + a)^* = a^*$ vì bản thân $a^*$ đã chứa sẵn $\varepsilon$.

#### Câu 14: Biểu thức nào sau đây KHÔNG tương đương với $(a+b)^*$?
- A. $(a^* b^*)^*$
- B. $(a^* + b^*)^*$
- C. $a^* (b a^*)^*$
- D. $a^* b^*$
👉 **Đáp án: D**
- **Giải thích:** $a^* b^*$ chỉ sinh các chuỗi $a$ trước $b$ sau (không sinh được `ba`, `aba`), trong khi $(a+b)^*$ sinh mọi chuỗi.

#### Câu 15: Rút gọn biểu thức $R = a + a b^*$:
- A. $a b^*$
- B. $a$
- C. $b^*$
- D. $(ab)^*$
👉 **Đáp án: A**
- **Giải thích:** $a + a b^* = a(\varepsilon + b^*) = a b^*$ (do $\varepsilon + b^* = b^*$).

#### Câu 16: Cho $R = (a+b)^* a (a+b)^* + (a+b)^* b (a+b)^*$. Biểu thức $R$ biểu diễn ngôn ngữ:
- A. $\Sigma^*$
- B. $\Sigma^+$ (mọi chuỗi có độ dài $\ge 1$)
- C. $\emptyset$
- D. $\{\varepsilon\}$
👉 **Đáp án: B**
- **Giải thích:** Nhánh 1 là mọi chuỗi chứa ít nhất một chữ $a$. Nhánh 2 là mọi chuỗi chứa ít nhất một chữ $b$. Hợp của hai nhánh là mọi chuỗi có chứa ít nhất một ký tự $\implies$ độ dài $\ge 1 \implies \Sigma^+$.

#### Câu 17: Đẳng thức $(ab)^* a = a (ba)^*$ thể hiện tính chất:
- A. Giao hoán của phép nhân
- B. Chuyển dịch chu kỳ của sao Kleene
- C. Phân phối
- D. Kết hợp
👉 **Đáp án: B**
- **Giải thích:** $(ab)^* a = (ab)(ab)\dots(ab)a = a(ba)(ba)\dots(ba) = a(ba)^*$.

#### Câu 18: Biểu thức $(a + \emptyset)^*$:
- A. $a^*$
- B. $\emptyset$
- C. $\varepsilon$
- D. $a^+$
👉 **Đáp án: A**
- **Giải thích:** $a + \emptyset = a \implies (a + \emptyset)^* = a^*$.

#### Câu 19: Biểu thức $(\emptyset \cdot a)^*$:
- A. $\emptyset$
- B. $\varepsilon$
- C. $a^*$
- D. $a$
👉 **Đáp án: B**
- **Giải thích:** $\emptyset \cdot a = \emptyset \implies \emptyset^* = \varepsilon$.

#### Câu 20: Cho $L(r) = \{a\}$. Biểu thức $r^*$ biểu diễn:
- A. $\{a^n \mid n \ge 0\}$
- B. $\{a^n \mid n \ge 1\}$
- C. $\{a\}$
- D. $\{\varepsilon, a\}$
👉 **Đáp án: A**

---

## DẠNG 3: ĐỊNH LÝ ARDEN VÀ TÌM RE TỪ AUTOMATA

#### Câu 21: Định lý Arden phát biểu rằng: Nếu $\varepsilon \notin P$ thì phương trình $X = Q + XP$ có nghiệm duy nhất là:
- A. $X = P^* Q$
- B. $X = Q P^*$
- C. $X = (Q+P)^*$
- D. $X = Q^* P$
👉 **Đáp án: B**
- **Giải thích:** Định lý Arden: Biến $X$ nằm ở bên TRÁI của $P$ trong số hạng $XP$ $\implies$ nghiệm là $X = Q P^*$.

#### Câu 22: Nếu phương trình có dạng $X = Q + PX$ (biến $X$ nằm bên PHẢI của $P$) và $\varepsilon \notin P$, nghiệm duy nhất là:
- A. $X = P^* Q$
- B. $X = Q P^*$
- C. $X = P Q^*$
- D. $X = (PQ)^*$
👉 **Đáp án: A**
- **Giải thích:** Khi $X$ ở bên phải thì lũy thừa $P^*$ nhân ở bên trái: $X = P^* Q$.

#### Câu 23: Nghiệm của phương trình ngôn ngữ $X = b + Xa$ là:
- A. $X = a^* b$
- B. $X = b a^*$
- C. $X = (ba)^*$
- D. $X = (b+a)^*$
👉 **Đáp án: B**
- **Giải thích:** Ở đây $Q = b, P = a$. Theo Arden: $X = Q P^* = b a^*$.

#### Câu 24: Cho hệ phương trình tương ứng với DFA có 2 trạng thái $X_0, X_1$:
- $X_0 = \varepsilon + X_1 b$
- $X_1 = X_0 a$
Biểu thức chính quy cho $X_0$ là:
- A. $(ab)^*$
- B. $a^* b^*$
- C. $(ba)^*$
- D. $(a+b)^*$
👉 **Đáp án: A**
- **Giải thích:**
  - Thay $X_1 = X_0 a$ vào phương trình $X_0$:
    $$X_0 = \varepsilon + (X_0 a) b = \varepsilon + X_0 (ab)$$
  - Áp dụng định lý Arden với $Q = \varepsilon, P = ab$:
    $$X_0 = \varepsilon (ab)^* = (ab)^*$$

#### Câu 25: Điều kiện bắt buộc để nghiệm $X = Q P^*$ trong định lý Arden là duy nhất:
- A. $P$ là ngôn ngữ hữu hạn
- B. Từ rỗng $\varepsilon$ KHÔNG thuộc $P$ ($\varepsilon \notin P$)
- C. $Q \ne \emptyset$
- D. $P \ne Q$
👉 **Đáp án: B**
- **Giải thích:** Nếu $\varepsilon \in P$ thì phương trình $X = Q + XP$ sẽ có vô số nghiệm.

---

## DẠNG 4: BỔ ĐỀ BƠM & CHỨNG MINH NGÔN NGỮ PHI CHÍNH QUY

#### Câu 26: Bổ đề bơm (Pumping Lemma) cho ngôn ngữ chính quy phát biểu rằng: nếu $L$ là chính quy thì tồn tại số $p$ sao cho mọi $w \in L$ với $|w| \ge p$ đều phân tích được thành $w = xyz$ thỏa mãn:
- A. $|y| \ge 1$, $|xy| \le p$, và $\forall i \ge 0: xy^i z \in L$
- B. $|y| \ge 0$, $|xy| \le p$, và $xyz \in L$
- C. $|y| \ge 1$, $|yz| \le p$, và $xy^2 z \in L$
- D. $|x| \ge 1$, $|y| \ge 1$, $|z| \ge 1$
👉 **Đáp án: A**
- **Giải thích:** Ba điều kiện chuẩn của Bổ đề bơm: đoạn bơm $y$ khác rỗng ($|y| \ge 1$), đoạn $xy$ nằm trong phạm vi $p$ ký tự đầu ($|xy| \le p$), và mọi số lần lặp $i \ge 0$ thì $xy^i z$ vẫn phải thuộc $L$.

#### Câu 27: Khi dùng bổ đề bơm chứng minh $L = \{ a^n b^n \mid n \ge 0 \}$ không chính quy, ta thường chọn chuỗi $w$ là:
- A. $w = a^p b^p$
- B. $w = ab$
- C. $w = a^{2p} b^p$
- D. $w = a^p$
👉 **Đáp án: A**
- **Giải thích:** Chuỗi $w = a^p b^p$ có độ dài $2p \ge p$. Vì $|xy| \le p$ nên đoạn $y$ hoàn toàn chỉ chứa toàn các ký tự $a$ ($y = a^k$ với $k \ge 1$). Khi bơm $i=2$, số lượng chữ $a$ tăng lên trong khi số chữ $b$ giữ nguyên $\implies x y^2 z = a^{p+k} b^p \notin L$ (mâu thuẫn!).

#### Câu 28: Ngôn ngữ nào sau đây là ngôn ngữ CHÍNH QUY?
- A. $L = \{ a^n b^n \mid n \ge 0 \}$
- B. $L = \{ a^n b^{2n} \mid n \ge 0 \}$
- C. $L = \{ a^n b^m \mid n, m \ge 0 \}$
- D. $L = \{ w w^R \mid w \in \{0, 1\}^* \}$
👉 **Đáp án: C**
- **Giải thích:** $L = \{ a^n b^m \mid n, m \ge 0 \}$ chính là $a^* b^*$, hai biến $n$ và $m$ hoàn toàn độc lập với nhau, không cần đếm hay so sánh số lượng $\implies$ Chính quy!

#### Câu 29: Ngôn ngữ nào sau đây là ngôn ngữ PHI CHÍNH QUY?
- A. $L = \{ w \in \{0, 1\}^* \mid |w| \le 1000 \}$
- B. $L = \{ 0^n 1^m \mid n \ge 1, m \ge 1 \}$
- C. $L = \{ a^n b^n \mid n \ge 1 \}$
- D. $L = \{ w \in \{a, b\}^* \mid w \text{ chứa chuỗi con } ab \}$
👉 **Đáp án: C**
- **Giải thích:** $a^n b^n$ có mối ràng buộc bằng nhau giữa $a$ và $b$ nên không chính quy.

#### Câu 30: Cho ngôn ngữ $L = \{ a^p \mid p \text{ là số nguyên tố} \}$. Ngôn ngữ $L$ là:
- A. Ngôn ngữ chính quy
- B. Ngôn ngữ phi chính quy
- C. Ngôn ngữ hữu hạn
- D. Ngôn ngữ rỗng
👉 **Đáp án: B**
- **Giải thích:** Khoảng cách giữa các số nguyên tố tăng dần không theo chu kỳ hữu hạn, ô-tô-mát hữu hạn không thể nhận diện được.

#### Câu 31: Cho ngôn ngữ $L = \{ a^{n^2} \mid n \ge 0 \}$. Ngôn ngữ $L$ là:
- A. Chính quy
- B. Phi chính quy
- C. Hữu hạn
- D. Chứa mọi chuỗi trên $\{a\}$
👉 **Đáp án: B**
- **Giải thích:** Các số chính phương $0, 1, 4, 9, 16, 25,\dots$ có bước nhảy $(n+1)^2 - n^2 = 2n+1$ tăng vô hạn, vi phạm bổ đề bơm.

#### Câu 32: Khẳng định nào sau đây là ĐÚNG về Bổ đề bơm?
- A. Nếu một ngôn ngữ thỏa mãn bổ đề bơm thì ngôn ngữ đó chắc chắn là chính quy
- B. Bổ đề bơm là điều kiện cần nhưng không phải điều kiện đủ của ngôn ngữ chính quy
- C. Bổ đề bơm dùng để tìm biểu thức chính quy ngắn nhất
- D. Mọi ngôn ngữ phi ngữ cảnh đều thỏa mãn bổ đề bơm của ngôn ngữ chính quy
👉 **Đáp án: B**
- **Giải thích:** Bổ đề bơm là điều kiện CẦN. Có những ngôn ngữ phi chính quy vẫn thỏa mãn bổ đề bơm.

#### Câu 33: Trong phép phân tích $w = xyz$ của bổ đề bơm, khi chọn giá trị bơm $i = 0$, chuỗi thu được là:
- A. $xz$
- B. $yz$
- C. $xy$
- D. $\varepsilon$
👉 **Đáp án: A**
- **Giải thích:** $y^0 = \varepsilon \implies x y^0 z = x \varepsilon z = xz$ (phép "rút bớt" / pumping down).

---

## DẠNG 5: TÍNH CHẤT ĐÓNG KÍN CỦA NGÔN NGỮ CHÍNH QUY

#### Câu 34: Lớp các ngôn ngữ chính quy ĐÓNG KÍN đối với phép toán nào sau đây?
- A. Phép hợp (Union) và phép giao (Intersection)
- B. Phép ghép (Concatenation) và sao Kleene (Kleene star)
- C. Phép lấy phần bù (Complement) và hiệu (Difference)
- D. Tất cả các phép toán trên
👉 **Đáp án: D**
- **Giải thích:** Lớp ngôn ngữ chính quy có tính chất đóng kín rất mạnh: đóng kín với hợp, giao, phần bù, hiệu, ghép, sao Kleene, đảo ngược.

#### Câu 35: Nếu $L_1$ là ngôn ngữ chính quy và $L_2$ là ngôn ngữ chính quy, thì $L_1 \cap L_2$ là:
- A. Luôn luôn là ngôn ngữ chính quy
- B. Có thể không chính quy
- C. Luôn là ngôn ngữ phi ngữ cảnh không chính quy
- D. Luôn là tập rỗng
👉 **Đáp án: A**
- **Giải thích:** Tính chất đóng kín đối với phép giao của lớp ngôn ngữ chính quy.

#### Câu 36: Nếu $L_1$ là ngôn ngữ chính quy và $L_2$ KHÔNG PHẢI là ngôn ngữ chính quy, thì $L_1 \cup L_2$:
- A. Chắc chắn là chính quy
- B. Có thể chính quy hoặc không chính quy
- C. Chắc chắn không chính quy
- D. Luôn là ngôn ngữ rỗng
👉 **Đáp án: B**
- **Giải thích:**
  - Ví dụ 1: $L_1 = \Sigma^*$ (chính quy), $L_2 = \{a^n b^n\}$ (không chính quy) $\implies L_1 \cup L_2 = \Sigma^*$ (chính quy!).
  - Ví dụ 2: $L_1 = \emptyset$ (chính quy) $\implies L_1 \cup L_2 = L_2$ (không chính quy).

#### Câu 37: Cho $L$ là ngôn ngữ chính quy trên $\Sigma$. Ngôn ngữ đảo ngược $L^R = \{ w^R \mid w \in L \}$ là:
- A. Ngôn ngữ chính quy
- B. Ngôn ngữ phi ngữ cảnh không chính quy
- C. Ngôn ngữ loại 0
- D. Không xác định được
👉 **Đáp án: A**
- **Giải thích:** Tính chất đóng kín đối với phép đảo ngược: Đảo chiều tất cả các mũi tên của DFA và đổi trạng thái bắt đầu thành kết thúc ta thu được NFA nhận diện $L^R$.

#### Câu 38: Nếu $L$ là ngôn ngữ chính quy thì hiệu $L_1 \setminus L_2$:
- A. Bằng $L_1 \cap \overline{L_2}$ và là ngôn ngữ chính quy
- B. Luôn là ngôn ngữ phi chính quy
- C. Không xác định được
- D. Luôn bằng $\emptyset$
👉 **Đáp án: A**
- **Giải thích:** Vì $L_1 \setminus L_2 = L_1 \cap \overline{L_2}$, mà phần bù và giao đều đóng kín nên hiệu cũng đóng kín.

#### Câu 39: Ngôn ngữ hữu hạn $L = \{w_1, w_2, \dots, w_k\}$ có phải là ngôn ngữ chính quy không?
- A. Luôn luôn là ngôn ngữ chính quy
- B. Chỉ chính quy khi $k \le 10$
- C. Không bao giờ chính quy
- D. Tùy thuộc vào độ dài các từ
👉 **Đáp án: A**
- **Giải thích:** Mọi ngôn ngữ hữu hạn đều viết được dưới dạng biểu thức chính quy: $w_1 + w_2 + \dots + w_k$.

#### Câu 40: Cho $L$ là ngôn ngữ bất kỳ (có thể không chính quy). Ngôn ngữ $L \cap \emptyset$ là:
- A. $\emptyset$ (và là ngôn ngữ chính quy)
- B. Không chính quy
- C. $L$
- D. Phụ thuộc vào $L$
👉 **Đáp án: A**
- **Giải thích:** Giao với tập rỗng luôn bằng tập rỗng $\emptyset$, mà $\emptyset$ là ngôn ngữ chính quy.

---

## DẠNG 6: MỆNH ĐỀ LÝ THUYẾT ĐÚNG / SAI TỔNG HỢP CHƯƠNG 3

#### Câu 41: Khẳng định nào sau đây là ĐÚNG?
- A. Ngôn ngữ chính quy là ngôn ngữ được đoán nhận bởi Ô-tô-mát hữu hạn
- B. Ngôn ngữ chính quy là ngôn ngữ được biểu diễn bởi Biểu thức chính quy
- C. Ngôn ngữ chính quy là ngôn ngữ được sinh ra bởi Văn phạm chính quy (Loại 3)
- D. Tất cả các khẳng định trên đều ĐÚNG
👉 **Đáp án: D**
- **Giải thích:** Định lý tương đương giữa DFA/NFA, Biểu thức chính quy (Định lý Kleene) và Văn phạm Loại 3.

#### Câu 42: Cho $r = a^*$. Giá trị nào sau đây KHÔNG THUỘC $L(r)$?
- A. $\varepsilon$
- B. `a`
- C. `b`
- D. `aaa`
👉 **Đáp án: C**
- **Giải thích:** $a^*$ chỉ sinh các chuỗi gồm toàn chữ $a$ hoặc rỗng, không chứa ký tự $b$.

#### Câu 43: Thuật toán chuyển từ Biểu thức chính quy sang $\varepsilon$-NFA được gọi là:
- A. Thuật toán Thompson
- B. Thuật toán Myhill-Nerode
- C. Thuật toán Dijkstra
- D. Thuật toán Chomsky
👉 **Đáp án: A**
- **Giải thích:** Thompson's Construction là thuật toán quy nạp xây dựng từng khối $\varepsilon$-NFA cho các phép toán $+$, $\cdot$, $*$.

#### Câu 44: Biểu thức $(a+b)^* ab(a+b)^*$ nhận diện các chuỗi:
- A. Bắt đầu bằng $ab$
- B. Kết thúc bằng $ab$
- C. Chứa chuỗi con $ab$
- D. Không chứa chuỗi con $ba$
👉 **Đáp án: C**

#### Câu 45: Cho ngôn ngữ $L$ gồm các chuỗi nhị phân có số chữ số 0 bằng số chữ số 1. Ngôn ngữ $L$ là:
- A. Ngôn ngữ chính quy
- B. Ngôn ngữ phi ngữ cảnh nhưng không chính quy
- C. Ngôn ngữ hữu hạn
- D. Ngôn ngữ loại 1
👉 **Đáp án: B**
- **Giải thích:** Nếu $L$ chính quy thì $L \cap 0^* 1^* = \{0^n 1^n\}$ cũng phải chính quy (vô lý). Do đó $L$ không chính quy.

#### Câu 46: Trong các biểu thức sau, biểu thức nào biểu diễn tập tất cả các chuỗi có độ dài ít nhất là 1 trên $\{a, b\}$?
- A. $(a+b)^*$
- B. $(a+b)^+$
- C. $(a+b)(a+b)^*$
- D. Cả B và C đều đúng
👉 **Đáp án: D**
- **Giải thích:** $(a+b)^+ = (a+b)(a+b)^*$ đều biểu diễn độ dài $\ge 1$.

#### Câu 47: Khẳng định nào sau đây là SAI về phép toán sao Kleene $*$?
- A. $L^*$ luôn chứa chuỗi rỗng $\varepsilon$
- B. Nếu $L = \emptyset$ thì $L^* = \emptyset$
- C. $L^* L^* = L^*$
- D. $(L^*)^* = L^*$
👉 **Đáp án: B**
- **Giải thích:** $\emptyset^* = \{\varepsilon\} \ne \emptyset$.

#### Câu 48: Phương trình $X = aX$ (không có số hạng tự do $Q$) có nghiệm là:
- A. $X = \emptyset$
- B. $X = a^*$
- C. $X = a^+$
- D. $X = \{\varepsilon\}$
👉 **Đáp án: A**
- **Giải thích:** $X = \emptyset + aX \implies X = a^* \cdot \emptyset = \emptyset$.

#### Câu 49: Nếu $L_1 \subseteq L_2$ và $L_1$ là ngôn ngữ phi chính quy thì:
- A. $L_2$ chắc chắn phi chính quy
- B. $L_2$ chắc chắn chính quy
- C. Chưa thể kết luận tính chính quy của $L_2$
- D. $L_2$ là tập rỗng
👉 **Đáp án: C**
- **Giải thích:** Ví dụ $L_1 = \{a^n b^n\}$ (phi chính quy), tập mẹ $L_2 = \Sigma^*$ (chính quy) hoặc $L_2 = \{a^n b^n c^m\}$ (phi chính quy).

#### Câu 50: Bài toán quyết định: "Cho một DFA $M$, kiểm tra xem $L(M)$ có rỗng hay không ($L(M) = \emptyset$)" có giải được không?
- A. Có, giải được bằng cách duyệt đồ thị xem từ $q_0$ có đường đi đến $F$ không
- B. Không giải được (Undecidable)
- C. Chỉ giải được khi $\Sigma$ có 1 ký tự
- D. Phụ thuộc vào số trạng thái của DFA
👉 **Đáp án: A**
- **Giải thích:** Bài toán kiểm tra tính rỗng của DFA tương đương với bài toán tìm đường đi trong đồ thị từ đỉnh $q_0$ đến các đỉnh thuộc $F$ (dùng BFS hoặc DFS là giải được ngay).
