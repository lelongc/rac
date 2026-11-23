# NGÂN HÀNG TRẮC NGHIỆM CHƯƠNG 4: VĂN PHẠM PHI NGỮ CẢNH (CFG) & Ô-TÔ-MÁT ĐẨY XUỐNG (PDA)
## RÚT GỌN VĂN PHẠM, DẠNG CHUẨN CHOMSKY, NHẬP NHẰNG VÀ PDA KÈM LỜI GIẢI CHI TIẾT

---

# TÓM TẮT LÝ THUYẾT & BÍ KÍP "ĂN TRỌN ĐIỂM" CHƯƠNG 4

### 1. Cây cú pháp và Dẫn xuất:
- **Dẫn xuất trái nhất (Leftmost):** Luôn thay thế biến chưa kết thúc nằm ở ngoài cùng bên trái.
- **Dẫn xuất phải nhất (Rightmost):** Luôn thay thế biến chưa kết thúc nằm ở ngoài cùng bên phải.
- **Cây phân tích cú pháp (Parse Tree):**
  - Gốc là biến bắt đầu $S$.
  - Các nút trong là các biến (Non-terminals).
  - Các lá (Leaves) từ trái sang phải ghép lại tạo thành chuỗi kết thúc (chuỗi dẫn xuất).

### 2. Văn phạm nhập nhằng (Ambiguous Grammar):
- Một văn phạm phi ngữ cảnh $G$ là **nhập nhằng** nếu tồn tại ít nhất một chuỗi $w \in L(G)$ có **từ 2 cây cú pháp khác nhau** (hoặc 2 dẫn xuất trái nhất khác nhau).
- **Mẹo nhận biết 3 giây:**
  + Thấy cùng một biến đệ quy ở cả hai đầu: $S \to SbS \mid a$, $S \to S+S \mid S*S$, $S \to SS \implies$ **Chắc chắn 100% nhập nhằng!**

### 3. Rút gọn văn phạm phi ngữ cảnh (Thứ tự bắt buộc: Rỗng $\to$ Đơn vị $\to$ Vô ích):
1. **Khử luật $\varepsilon$ ($A \to \varepsilon$):** Tìm các biến có thể "bốc hơi" (nullable). Viết thêm các phiên bản luật bỏ biến đó đi, rồi xóa $A \to \varepsilon$.
2. **Khử luật đơn vị ($A \to B$):** Thừa kế gia tài: sao chép tất cả các luật vế phải của $B$ sang cho $A$, rồi xóa $A \to B$.
3. **Khử ký hiệu vô ích:**
   - Khử vô sinh: Biến không sinh ra được chuỗi ký tự kết thúc.
   - Khử không đến được: Biến từ $S$ không thể đi tới.

### 4. Dạng chuẩn Chomsky (CNF - Chomsky Normal Form):
- Mọi luật chỉ có **đúng 2 dạng**:
  $$\mathbf{A \to BC} \quad (\text{2 biến hoa}) \qquad \text{hoặc} \qquad \mathbf{A \to a} \quad (\text{1 chữ thường})$$
- **CÔNG THỨC VÀNG VỀ ĐỘ DÀI DẪN XUẤT TRONG CNF:**
  > Để sinh ra một chuỗi có độ dài $n$ ($|w| = n$) trong văn phạm ở dạng chuẩn Chomsky, cây cú pháp luôn cần **đúng $2n - 1$ bước dẫn xuất**!
  > *(Ví dụ chuỗi dài 5 thì cần $2(5) - 1 = 9$ bước dẫn xuất)*.

### 5. Ô-tô-mát đẩy xuống (Pushdown Automata - PDA):
- Là bộ 7: $M = \langle Q, \Sigma, \Gamma, \delta, q_0, Z_0, F \rangle$ ($\Gamma$ là bảng chữ cái ngăn xếp, $Z_0$ là ký hiệu đáy ngăn xếp).
- **Cơ chế:** Có thêm một bộ nhớ ngăn xếp (Stack) hoạt động theo nguyên tắc LIFO (vào sau ra trước).
- **Hai cách đoán nhận:**
  1. $T(M)$: Bằng trạng thái kết thúc ($q \in F$).
  2. $N(M)$: Bằng ngăn xếp rỗng (ngăn xếp sạch bóng không còn ký hiệu nào).
- **Tính chất quan trọng:**
  - PDA không đơn định (NPDA) nhận diện đúng lớp **Ngôn ngữ phi ngữ cảnh (CFL)**.
  - PDA đơn định (DPDA) **yếu hơn** NPDA! (DPDA chỉ nhận diện được DCFL, ví dụ không nhận diện được Palindrome chẵn $ww^R$).

---

# PHẦN 1: CÁC DẠNG BÀI TẬP VÀ NGÂN HÀNG CÂU HỎI TRẮC NGHIỆM

---

## DẠNG 1: CÂY CÚ PHÁP, DẪN XUẤT VÀ ĐỘ DÀI TRONG CNF

#### Câu 1: Cho văn phạm $G$ ở dạng chuẩn Chomsky (CNF). Để sinh ra một từ có độ dài bằng 4 ($|w| = 4$), số bước dẫn xuất cần thiết là:
- A. 4 bước
- B. 7 bước
- C. 8 bước
- D. 5 bước
👉 **Đáp án: B**
- **Giải thích:** Áp dụng công thức vàng cho CNF: Số bước $= 2n - 1 = 2(4) - 1 = 7$ bước.

#### Câu 2: Cho văn phạm ở dạng chuẩn Chomsky. Nếu một cây cú pháp có 9 bước dẫn xuất thì chuỗi ở các nút lá có độ dài bằng:
- A. 4
- B. 5
- C. 6
- D. 9
👉 **Đáp án: B**
- **Giải thích:** Ta có $2n - 1 = 9 \implies 2n = 10 \implies n = 5$.

#### Câu 3: Trong cây phân tích cú pháp của một văn phạm phi ngữ cảnh, các nút lá (Leaves) từ trái sang phải biểu diễn:
- A. Biến bắt đầu $S$
- B. Các biến chưa kết thúc (Non-terminals)
- C. Chuỗi ký tự kết thúc được sinh ra
- D. Tập các quy tắc sinh
👉 **Đáp án: C**
- **Giải thích:** Đọc tất cả các nút lá từ trái qua phải thu được chuỗi kết thúc (chuỗi suy dẫn / yield of the tree).

#### Câu 4: Dẫn xuất $S \Rightarrow aB \Rightarrow abC \Rightarrow abc$ là dẫn xuất:
- A. Trái nhất (Leftmost)
- B. Phải nhất (Rightmost)
- C. Cả trái nhất và phải nhất
- D. Không phải dẫn xuất hợp lệ
👉 **Đáp án: C**
- **Giải thích:** Tại mỗi bước trung gian, chuỗi chỉ chứa duy nhất một biến ($S$, sau đó là $B$, sau đó là $C$). Vì chỉ có 1 biến nên nó vừa là biến ngoài cùng bên trái, vừa là ngoài cùng bên phải $\implies$ Vừa là Leftmost vừa là Rightmost!

#### Câu 5: Cho văn phạm $G$ có $P = \{ S \to AB,\ A \to a,\ B \to b \}$. Dẫn xuất phải nhất để sinh ra chuỗi `ab` là:
- A. $S \Rightarrow AB \Rightarrow Ab \Rightarrow ab$
- B. $S \Rightarrow AB \Rightarrow aB \Rightarrow ab$
- C. $S \Rightarrow aB \Rightarrow ab$
- D. $S \Rightarrow Ab \Rightarrow ab$
👉 **Đáp án: A**
- **Giải thích:** Rightmost derivation bắt buộc phải thay thế biến bên phải trước: $S \Rightarrow AB \Rightarrow Ab$ (thay $B$ thành $b$ trước), sau đó $Ab \Rightarrow ab$ (thay $A$ thành $a$).

---

## DẠNG 2: VĂN PHẠM NHẬP NHẰNG (AMBIGUITY)

#### Câu 6: Một văn phạm phi ngữ cảnh $G$ được gọi là nhập nhằng (đa nghĩa) nếu:
- A. Tồn tại ít nhất một chuỗi có từ 2 cây phân tích cú pháp khác nhau
- B. Tồn tại một chuỗi có từ 2 dẫn xuất trái nhất khác nhau
- C. Tồn tại một chuỗi có từ 2 dẫn xuất phải nhất khác nhau
- D. Tất cả các phát biểu trên đều ĐÚNG
👉 **Đáp án: D**
- **Giải thích:** Ba định nghĩa trên là hoàn toàn tương đương nhau.

#### Câu 7: Văn phạm nào sau đây là văn phạm NHẬP NHẰNG?
- A. $S \to aSb \mid ab$
- B. $S \to SbS \mid a$
- C. $S \to aA,\ A \to b$
- D. $S \to 0S1 \mid \varepsilon$
👉 **Đáp án: B**
- **Giải thích:** $S \to SbS \mid a$ có đệ quy 2 đầu. Chuỗi `ababa` có 2 cây cú pháp: $(SbS)bS$ và $Sb(SbS)$.

#### Câu 8: Chuỗi nào sau đây chứng minh văn phạm $S \to S+S \mid S*S \mid a$ là nhập nhằng?
- A. `a`
- B. `a+a`
- C. `a+a*a`
- D. `*+a`
👉 **Đáp án: C**
- **Giải thích:** Chuỗi `a+a*a` có 2 cây: một cây thực hiện phép cộng trước $(a+a)*a$, một cây thực hiện phép nhân trước $a+(a*a)$.

#### Câu 9: Cho văn phạm $S \to a \mid abS \mid aAb,\ A \to bS \mid aAAb$. Chuỗi ngắn nhất chứng minh văn phạm là nhập nhằng là:
- A. `ab`
- B. `aba`
- C. `ababab`
- D. `aab`
👉 **Đáp án: C**
- **Giải thích:** Chuỗi `ababab` có thể sinh theo 2 nhánh: $S \to abS \to ab(aAb) \dots$ và $S \to aAb \to a(bS)b \dots$

#### Câu 10: Khẳng định nào sau đây là ĐÚNG về ngôn ngữ nhập nhằng cố hữu (Inherently Ambiguous Language)?
- A. Mọi văn phạm sinh ra ngôn ngữ đó đều bị nhập nhằng
- B. Có thể tìm được một văn phạm đơn nghĩa tương đương
- C. Là ngôn ngữ chính quy
- D. Ô-tô-mát hữu hạn nhận diện được nó
👉 **Đáp án: A**
- **Giải thích:** Ngôn ngữ nhập nhằng cố hữu là ngôn ngữ mà KHÔNG TỒN TẠI bất kỳ văn phạm phi ngữ cảnh đơn nghĩa nào sinh ra nó (ví dụ $L = \{ a^n b^n c^m d^m \} \cup \{ a^n b^m c^m d^n \}$).

---

## DẠNG 3: RÚT GỌN VĂN PHẠM PHI NGỮ CẢNH (CFG)

#### Câu 11: Thứ tự chuẩn khi thực hiện rút gọn văn phạm phi ngữ cảnh là:
- A. Khử vô ích $\to$ Khử $\varepsilon$ $\to$ Khử đơn vị
- B. Khử $\varepsilon$ $\to$ Khử đơn vị $\to$ Khử vô ích
- C. Khử đơn vị $\to$ Khử vô ích $\to$ Khử $\varepsilon$
- D. Thứ tự nào cũng được
👉 **Đáp án: B**
- **Giải thích:** Thần chú: "Rỗng $\to$ Đơn vị $\to$ Vô ích". Làm sai thứ tự có thể làm phát sinh lại các ký hiệu thừa.

#### Câu 12: Trong văn phạm có quy tắc $A \to \varepsilon$, biến $A$ được gọi là:
- A. Biến vô sinh
- B. Biến triệt tiêu (Nullable variable)
- C. Biến không đến được
- D. Biến kết thúc
👉 **Đáp án: B**
- **Giải thích:** Biến có thể dẫn ra chuỗi rỗng $\varepsilon$ sau một hoặc nhiều bước được gọi là biến triệt tiêu.

#### Câu 13: Cho văn phạm $P = \{ S \to AB,\ A \to aA \mid \varepsilon,\ B \to b \}$. Sau khi khử luật $\varepsilon$, tập luật sinh của $S$ trở thành:
- A. $S \to AB \mid B$
- B. $S \to AB \mid A$
- C. $S \to B$
- D. $S \to AB$
👉 **Đáp án: A**
- **Giải thích:** Biến $A$ là triệt tiêu ($A \to \varepsilon$). Tại $S \to AB$, nếu $A$ biến mất thì còn lại $B$. Do đó $S \to AB \mid B$.

#### Câu 14: Quy tắc nào sau đây là một quy tắc đơn vị (Unit production)?
- A. $A \to a$
- B. $A \to B$ ($A, B \in \Delta$)
- C. $A \to AB$
- D. $A \to \varepsilon$
👉 **Đáp án: B**
- **Giải thích:** Quy tắc đơn vị có dạng $A \to B$ với cả $A$ và $B$ đều là biến (Non-terminals).

#### Câu 15: Cho văn phạm có các luật: $S \to A,\ A \to B,\ B \to a \mid b$. Sau khi khử các quy tắc đơn vị, các luật từ $S$ là:
- A. $S \to a \mid b$
- B. $S \to A \mid a \mid b$
- C. $S \to B$
- D. $S \to a$
👉 **Đáp án: A**
- **Giải thích:** $S \to A \to B \to a \mid b$. Biến $S$ thừa kế toàn bộ giá trị kết thúc của chuỗi: $S \to a \mid b$.

#### Câu 16: Biến $X$ trong văn phạm phi ngữ cảnh được gọi là "vô sinh" (Non-generating) nếu:
- A. Từ $S$ không thể dẫn ra chuỗi chứa $X$
- B. Từ $X$ không thể dẫn ra bất kỳ chuỗi ký tự kết thúc nào ($X \not\Rightarrow^* w \in \Sigma^*$)
- C. $X$ chỉ có đúng một luật sinh
- D. $X$ sinh ra chuỗi rỗng
👉 **Đáp án: B**

#### Câu 17: Cho văn phạm có $P = \{ S \to AB,\ A \to a,\ B \to bB \}$. Biến nào là biến vô ích?
- A. Biến $A$
- B. Biến $B$ (và kéo theo $S$)
- C. Biến $S$
- D. Không có biến nào
👉 **Đáp án: B**
- **Giải thích:** Biến $B$ chỉ có luật $B \to bB$, cứ lặp mãi không bao giờ sinh ra chữ thường để kết thúc $\implies B$ vô sinh. Vì $B$ vô sinh nên $S \to AB$ cũng không bao giờ kết thúc $\implies S$ cũng vô sinh. Ngôn ngữ của văn phạm là rỗng $L(G) = \emptyset$.

#### Câu 18: Cho văn phạm $P = \{ S \to aA,\ A \to a,\ B \to b \}$. Biến $B$ là ký hiệu thừa vì:
- A. $B$ là biến vô sinh
- B. $B$ là biến không đến được từ biến bắt đầu $S$
- C. $B$ sinh ra từ rỗng
- D. $B$ là quy tắc đơn vị
👉 **Đáp án: B**
- **Giải thích:** Từ $S$ chỉ dẫn ra $aA$, không có đường nào dẫn tới biến $B$.

---

## DẠNG 4: DẠNG CHUẨN CHOMSKY (CNF)

#### Câu 19: Dạng chuẩn Chomsky (CNF) quy định mọi quy tắc sinh chỉ có dạng:
- A. $A \to BC$ hoặc $A \to a$
- B. $A \to aB$ hoặc $A \to a$
- C. $A \to \alpha$ với $|\alpha| \le 2$
- D. $A \to aBC$
👉 **Đáp án: A**
- **Giải thích:** Định nghĩa CNF: Vế phải chỉ có thể là 2 biến hoa hoặc đúng 1 chữ thường.

#### Câu 20: Quy tắc nào sau đây ĐÃ Ở DẠNG CHUẨN CHOMSKY?
- A. $S \to aB$
- B. $S \to AB$
- C. $S \to ABC$
- D. $S \to a$
👉 **Đáp án: Cả B và D đều ở dạng chuẩn Chomsky** (nếu câu hỏi chọn 1 thì $S \to AB$ là dạng 2 biến hoa điển hình).

#### Câu 21: Để đưa quy tắc $S \to aA$ về dạng chuẩn Chomsky, ta thay bằng:
- A. $S \to A_a A$ và thêm $A_a \to a$
- B. $S \to a$ và $S \to A$
- C. $S \to AA$
- D. Giữ nguyên vì đã chuẩn
👉 **Đáp án: A**
- **Giải thích:** Thay ký tự thường $a$ bằng biến mới $A_a$, kèm luật $A_a \to a$.

#### Câu 22: Để đưa quy tắc $S \to ABCD$ về dạng chuẩn Chomsky, ta cần thêm ít nhất bao nhiêu biến phụ mới?
- A. 1 biến
- B. 2 biến
- C. 3 biến
- D. 4 biến
👉 **Đáp án: B**
- **Giải thích:** $S \to A C_1$, $C_1 \to B C_2$, $C_2 \to C D$. Cần thêm 2 biến phụ là $C_1$ và $C_2$.

#### Câu 23: Văn phạm ở dạng chuẩn Chomsky có thể sinh ra từ rỗng $\varepsilon$ không?
- A. Có
- B. Không (chỉ sinh được ngôn ngữ $L \setminus \{\varepsilon\}$)
- C. Luôn luôn sinh ra $\varepsilon$
- D. Tùy thuộc vào số lượng biến
👉 **Đáp án: B**
- **Giải thích:** Theo định nghĩa chuẩn Chomsky không chứa luật $A \to \varepsilon$. Nếu muốn chứa $\varepsilon$ thì phải thêm luật đặc biệt $S \to \varepsilon$ với điều kiện $S$ không xuất hiện ở vế phải.

---

## DẠNG 5: Ô-TÔ-MÁT ĐẨY XUỐNG (PDA)

#### Câu 24: Ô-tô-mát đẩy xuống (PDA) là một bộ 7 $M = \langle Q, \Sigma, \Gamma, \delta, q_0, Z_0, F \rangle$. Ký hiệu $\Gamma$ đại diện cho:
- A. Bảng chữ cái đầu vào
- B. Bảng chữ cái ký hiệu ngăn xếp (Stack alphabet)
- C. Tập trạng thái
- D. Hàm chuyển
👉 **Đáp án: B**
- **Giải thích:** $\Gamma$ là tập các ký hiệu có thể được lưu trữ trong ngăn xếp.

#### Câu 25: Ngăn xếp của PDA hoạt động theo cơ chế nào?
- A. FIFO (Vào trước ra trước)
- B. LIFO (Vào sau ra trước - Last In First Out)
- C. Truy cập ngẫu nhiên
- D. Hàng đợi hai đầu
👉 **Đáp án: B**
- **Giải thích:** Ngăn xếp (Stack) chỉ cho phép PUSH (thêm) và POP (lấy) tại một đầu duy nhất là đỉnh ngăn xếp (LIFO).

#### Câu 26: Bước chuyển $\delta(q, a, Z) = \{(p, \varepsilon)\}$ có nghĩa là:
- A. Đọc chữ $a$, chuyển sang trạng thái $p$, và PUSH thêm $Z$
- B. Đọc chữ $a$, chuyển sang trạng thái $p$, và POP (xóa) ký hiệu $Z$ khỏi đỉnh ngăn xếp
- C. Đọc chữ $a$, thay $Z$ bằng $\varepsilon Z$
- D. Đọc chữ rỗng
👉 **Đáp án: B**
- **Giải thích:** Đỉnh $Z$ bị thay thế bởi chuỗi rỗng $\varepsilon$, tức là $Z$ bị lấy ra khỏi ngăn xếp (POP).

#### Câu 27: Bước chuyển $\delta(q, a, Z) = \{(p, YZ)\}$ có nghĩa là:
- A. Lấy $Z$ ra và đẩy $Y$ vào
- B. Giữ nguyên $Z$ ở dưới và PUSH thêm ký hiệu $Y$ lên đỉnh ngăn xếp
- C. Xóa cả $Y$ và $Z$
- D. Chuyển trạng thái mà không tác động ngăn xếp
👉 **Đáp án: B**
- **Giải thích:** Chuỗi $YZ$ thay cho $Z$, nghĩa là $Y$ nằm ở trên đỉnh, $Z$ nằm ở dưới.

#### Câu 28: Hai cách đoán nhận của PDA là đoán nhận bằng trạng thái kết thúc $T(M)$ và đoán nhận bằng ngăn xếp rỗng $N(M)$:
- A. Nhận diện hai lớp ngôn ngữ hoàn toàn khác nhau
- B. Hoàn toàn tương đương nhau (đều nhận diện lớp ngôn ngữ phi ngữ cảnh)
- C. $T(M)$ mạnh hơn $N(M)$
- D. $N(M)$ mạnh hơn $T(M)$
👉 **Đáp án: B**
- **Giải thích:** Định lý: Với mọi PDA $A$, luôn tồn tại PDA $B$ sao cho $T(A) = N(B)$ và ngược lại.

#### Câu 29: Ô-tô-mát đẩy xuống ĐƠN ĐỊNH (DPDA):
- A. Có sức mạnh tương đương NPDA
- B. Yếu hơn NPDA (chỉ nhận diện được một tập con thực sự của CFL, gọi là DCFL)
- C. Nhận diện được mọi ngôn ngữ phi ngữ cảnh
- D. Nhận diện được ngôn ngữ $a^n b^n c^n$
👉 **Đáp án: B**
- **Giải thích:** Ví dụ ngôn ngữ Palindrome $L = \{ w w^R \mid w \in \{0, 1\}^* \}$ cần đoán điểm giữa của chuỗi để đổi chiều ngăn xếp, DPDA không làm được mà bắt buộc phải dùng NPDA.

#### Câu 30: Ngôn ngữ nào sau đây đoán nhận được bởi PDA nhưng KHÔNG THỂ đoán nhận bởi DFA?
- A. $\{ a^n b^n \mid n \ge 1 \}$
- B. $\{ a^* b^* \}$
- C. $\{ a^n b^m \mid n, m \ge 1 \}$
- D. $\{ w \mid |w| \text{ chẵn} \}$
👉 **Đáp án: A**
- **Giải thích:** $\{a^n b^n\}$ cần ngăn xếp của PDA để đếm số lượng $a$ và so khớp với $b$.

#### Câu 31: Khi chuyển từ PDA sang CFG (như trong Ví dụ 3.8), biến của CFG có dạng:
- A. $[q, Z, p]$
- B. $[q, a, p]$
- C. $[Z, q, a]$
- D. $[q, Z]$
👉 **Đáp án: A**
- **Giải thích:** Biến $[q, Z, p]$ biểu diễn chuyến đi từ trạng thái $q$, xóa sạch ký hiệu ngăn xếp $Z$, và dừng ở trạng thái $p$.

#### Câu 32: Cho PDA có $|Q| = 2$ trạng thái và $|\Gamma| = 2$ ký hiệu ngăn xếp. Tổng số biến dạng $[q, Z, p]$ trong CFG tương đương là:
- A. 4
- B. 8
- C. 16
- D. 9
👉 **Đáp án: B**
- **Giải thích:** Số lượng biến $= |Q| \times |\Gamma| \times |Q| = 2 \times 2 \times 2 = 8$ biến. (Nếu tính cả biến bắt đầu $S$ là 9 biến).

#### Câu 33: Bước chuyển $\delta(q_1, b, Z) = \{(q_1, \varepsilon)\}$ (ngăn xếp bị xóa rỗng về $\varepsilon$) sinh ra luật nào trong CFG?
- A. $[q_1, Z, q_1] \to b$
- B. $[q_1, Z, q_1] \to \varepsilon$
- C. $[q_1, Z, q_1] \to b [q_1, Z, q_1]$
- D. $S \to b$
👉 **Đáp án: A**
- **Giải thích:** Công thức xóa rỗng: $(p, \varepsilon) \in \delta(q, a, Z) \implies [q, Z, p] \to a$. Ở đây $q=q_1, a=b, Z=Z, p=q_1 \implies [q_1, Z, q_1] \to b$.

#### Câu 34: Bước chuyển $\delta(q_0, a, Z) = \{(q_1, Z)\}$ (ngăn xếp thay bằng 1 ký hiệu) trong máy có 2 trạng thái $\{q_0, q_1\}$ sẽ sinh ra bao nhiêu quy tắc trong CFG?
- A. 1 quy tắc
- B. 2 quy tắc
- C. 4 quy tắc
- D. 8 quy tắc
👉 **Đáp án: B**
- **Giải thích:** Thay 1 ký hiệu thì đuôi chạy qua các trạng thái $r_1 \in \{q_0, q_1\} \implies$ sinh đúng 2 quy tắc.

#### Câu 35: Bước chuyển $\delta(q_0, b, Z_0) = \{(q_0, ZZ_0)\}$ (ngăn xếp thay bằng 2 ký hiệu) trong máy có 2 trạng thái $\{q_0, q_1\}$ sẽ sinh ra bao nhiêu quy tắc trong CFG?
- A. 2 quy tắc
- B. 4 quy tắc
- C. 8 quy tắc
- D. 16 quy tắc
👉 **Đáp án: B**
- **Giải thích:** Thay 2 ký hiệu có 2 biến $r_1, r_2$, số quy tắc là $|Q|^2 = 2^2 = 4$ quy tắc (chính là $P_3, P_4, P_5, P_6$).

---

## DẠNG 6: TÍNH CHẤT ĐÓNG KÍN VÀ BỔ ĐỀ BƠM CHO CFL

#### Câu 36: Lớp các ngôn ngữ phi ngữ cảnh (CFL) KHÔNG ĐÓNG KÍN đối với phép toán nào sau đây?
- A. Phép hợp ($\cup$)
- B. Phép giao ($\cap$)
- C. Phép ghép ($L_1 L_2$)
- D. Phép sao Kleene ($L^*$)
👉 **Đáp án: B**
- **Giải thích:** Giao của hai ngôn ngữ phi ngữ cảnh có thể KHÔNG PHẢI là ngôn ngữ phi ngữ cảnh! Ví dụ: $L_1 = \{ a^n b^n c^m \}$ (CFL) và $L_2 = \{ a^m b^n c^n \}$ (CFL), nhưng $L_1 \cap L_2 = \{ a^n b^n c^n \}$ KHÔNG PHẢI là CFL!

#### Câu 37: Lớp ngôn ngữ phi ngữ cảnh (CFL) có đóng kín với phép lấy phần bù ($\overline{L}$) không?
- A. Có
- B. Không
- C. Chỉ đóng kín khi $\Sigma$ có 1 ký tự
- D. Luôn đóng kín
👉 **Đáp án: B**
- **Giải thích:** Nếu CFL đóng kín với phần bù thì theo luật De Morgan: $L_1 \cap L_2 = \overline{\overline{L_1} \cup \overline{L_2}}$, CFL cũng sẽ đóng kín với phép giao (mâu thuẫn). Do đó CFL **KHÔNG đóng kín với phần bù**.

#### Câu 38: Giao của một Ngôn ngữ phi ngữ cảnh ($L_1$) và một Ngôn ngữ chính quy ($R$) là:
- A. Luôn luôn là một Ngôn ngữ phi ngữ cảnh ($L_1 \cap R \in \text{CFL}$)
- B. Luôn là ngôn ngữ chính quy
- C. Luôn là ngôn ngữ loại 0
- D. Luôn bằng $\emptyset$
👉 **Đáp án: A**
- **Giải thích:** Định lý rất quan trọng: Giao của CFL với Regular Language luôn luôn là CFL (chứng minh bằng cách nhân tích giữa PDA và DFA).

#### Câu 39: Bổ đề bơm cho Ngôn ngữ phi ngữ cảnh (Pumping Lemma for CFL) phân tích chuỗi $w$ thành mấy phần?
- A. 3 phần ($xyz$)
- B. 5 phần ($uvxyz$)
- C. 2 phần ($uv$)
- D. 4 phần ($wxyz$)
👉 **Đáp án: B**
- **Giải thích:** Bổ đề bơm cho CFL (Bar-Hillel lemma) phân tích $w = uvxyz$ với điều kiện $|vy| \ge 1$, $|vxy| \le p$, và $\forall i \ge 0: u v^i x y^i z \in L$.

#### Câu 40: Ngôn ngữ nào sau đây KHÔNG PHẢI là ngôn ngữ phi ngữ cảnh?
- A. $\{ a^n b^n \mid n \ge 0 \}$
- B. $\{ a^n b^n c^n \mid n \ge 0 \}$
- C. $\{ a^n b^{2n} \mid n \ge 0 \}$
- D. $\{ w w^R \mid w \in \{a, b\}^* \}$
👉 **Đáp án: B**
- **Giải thích:** $\{a^n b^n c^n\}$ đòi hỏi phải nhớ đồng thời 3 đại lượng bằng nhau, ngăn xếp của PDA chỉ nhớ được 2 đại lượng nên không nhận diện được. Nó thuộc **Loại 1 (Cảm ngữ cảnh)**.

#### Câu 41: Ngôn ngữ nào sau đây là ngôn ngữ phi ngữ cảnh?
- A. $\{ a^n b^n c^n \mid n \ge 1 \}$
- B. $\{ a^n b^m c^n d^m \mid n, m \ge 1 \}$
- C. $\{ a^n b^m c^m d^n \mid n, m \ge 1 \}$
- D. $\{ a^p \mid p \text{ là số nguyên tố} \}$
👉 **Đáp án: C**
- **Giải thích:** Ở câu C, các cặp lồng nhau đối xứng: $a^n (\dots) d^n$ bọc bên ngoài $b^m c^m$ bên trong (cơ chế ngăn xếp LIFO giải quyết hoàn hảo). Còn câu B có tính chất bắt chéo xen kẽ nên không phải CFL.

#### Câu 42: Bài toán quyết định: "Cho một CFG $G$, kiểm tra xem $L(G) = \emptyset$ (ngôn ngữ có rỗng không)" có giải được không?
- A. Có, giải được bằng thuật toán tìm các biến sinh
- B. Không giải được (Undecidable)
- C. Chỉ giải được khi văn phạm ở dạng CNF
- D. Không xác định
👉 **Đáp án: A**
- **Giải thích:** Tính rỗng của CFG là giải được (Decidable): Nếu biến bắt đầu $S$ không phải là biến sinh thì $L(G) = \emptyset$.

#### Câu 43: Bài toán quyết định: "Cho hai CFG $G_1$ và $G_2$, kiểm tra xem $L(G_1) = L(G_2)$ không" là bài toán:
- A. Giải được (Decidable)
- B. Không giải được (Undecidable)
- C. Luôn đúng
- D. Giải được trong thời gian đa thức
👉 **Đáp án: B**
- **Giải thích:** Bài toán kiểm tra tính tương đương của hai văn phạm phi ngữ cảnh là **KHÔNG GIẢI ĐƯỢC** (Undecidable).

#### Câu 44: Bài toán kiểm tra một CFG có nhập nhằng hay không là bài toán:
- A. Giải được
- B. Không giải được (Undecidable)
- C. Giải được bằng DFA
- D. Tuyến tính
👉 **Đáp án: B**
- **Giải thích:** Không tồn tại bất kỳ thuật toán tổng quát nào có thể kiểm tra một CFG bất kỳ có nhập nhằng hay không.

#### Câu 45: Cho $L$ là ngôn ngữ phi ngữ cảnh. Ngôn ngữ $L^R = \{ w^R \mid w \in L \}$ là:
- A. Ngôn ngữ phi ngữ cảnh
- B. Ngôn ngữ chính quy
- C. Ngôn ngữ loại 0
- D. Không thể xác định
👉 **Đáp án: A**
- **Giải thích:** CFL đóng kín đối với phép đảo ngược: đảo ngược vế phải của tất cả các luật sinh trong CFG ($A \to \alpha^R$).

#### Câu 46: Trong PDA, từ "đẩy xuống" (Pushdown) có nguồn gốc từ:
- A. Bộ điều khiển trạng thái
- B. Cơ chế ngăn xếp: phần tử mới được đẩy xuống đỉnh ngăn xếp
- C. Đầu đọc băng vào
- D. Tên nhà toán học
👉 **Đáp án: B**

#### Câu 47: Một văn phạm phi ngữ cảnh $G$ không có $\varepsilon$-quy tắc và không có quy tắc đơn vị. Để đưa về CNF, ta chỉ cần:
- A. Thay các ký tự kết thúc trong vế phải có độ dài $\ge 2$ bằng biến, và bẻ các luật có vế phải $\ge 3$ thành các luật có vế phải bằng 2
- B. Khử lại luật $\varepsilon$
- C. Thêm bước chuyển $\varepsilon$
- D. Đảo ngược các luật sinh
👉 **Đáp án: A**

#### Câu 48: Số lượng ký hiệu tối đa được phép xuất hiện ở vế phải của một luật trong dạng chuẩn Chomsky là:
- A. 1
- B. 2
- C. 3
- D. Tùy ý
👉 **Đáp án: B**
- **Giải thích:** Chỉ tối đa 2 biến ($A \to BC$).

#### Câu 49: PDA khác Ô-tô-mát hữu hạn (FA) ở điểm mấu chốt nào?
- A. PDA có thêm bộ nhớ ngăn xếp với dung lượng không giới hạn
- B. PDA có nhiều trạng thái hơn
- C. PDA đọc băng theo 2 chiều
- D. PDA không có trạng thái kết thúc
👉 **Đáp án: A**
- **Giải thích:** Ngăn xếp của PDA có thể lưu trữ số lượng ký hiệu tùy ý lớn (không giới hạn độ sâu).

#### Câu 50: Ngôn ngữ nào sau đây được đoán nhận bởi PDA với ngăn xếp rỗng $N(M)$?
- A. Mọi ngôn ngữ phi ngữ cảnh không chứa từ rỗng
- B. Mọi ngôn ngữ phi ngữ cảnh (kể cả chứa từ rỗng nếu ngăn xếp ban đầu rỗng)
- C. Chỉ các ngôn ngữ chính quy
- D. Chỉ các ngôn ngữ hữu hạn
👉 **Đáp án: B**
- **Giải thích:** Đoán nhận theo ngăn xếp rỗng và theo trạng thái kết thúc hoàn toàn tương đương nhau về lớp ngôn ngữ.
