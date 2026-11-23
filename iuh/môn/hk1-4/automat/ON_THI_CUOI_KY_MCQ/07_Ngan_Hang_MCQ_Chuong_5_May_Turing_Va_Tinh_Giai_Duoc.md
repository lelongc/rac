# NGÂN HÀNG TRẮC NGHIỆM CHƯƠNG 5: MÁY TURING & TÍNH GIẢI ĐƯỢC
## BÀI TOÁN DỪNG, BÀI TOÁN POST (PCP), PHÂN CẤP CHOMSKY VÀ LỜI GIẢI CHI TIẾT

---

# TÓM TẮT LÝ THUYẾT & BÍ KÍP "ĂN TRỌN ĐIỂM" CHƯƠNG 5

### 1. Máy Turing đơn định (DTM) - Bộ 7 thành phần:
$$M = \langle Q, \Sigma, \Gamma, \delta, s_0, B, F \rangle$$
- $Q$: Tập hữu hạn các trạng thái.
- $\Sigma$: Bảng chữ cái đầu vào (chuỗi nạp vào băng ban đầu).
- $\Gamma$: Bảng chữ cái trên băng (Tape alphabet), bao gồm cả $\Sigma$ và ký hiệu ô trống $B$ ($\Sigma \subset \Gamma \setminus \{B\}$).
- $s_0 \in Q$: Trạng thái bắt đầu.
- $B \in \Gamma$: Ký hiệu ô trống (Blank symbol, $B \notin \Sigma$).
- $F \subseteq Q$: Tập trạng thái dừng / chấp nhận (Halting / Accepting states).
- $\delta$: Hàm chuyển:
  $$\mathbf{\delta: Q \times \Gamma \to Q \times \Gamma \times \{L, R\}}$$
  - **Ý nghĩa:** Khi đang ở trạng thái $q$, đầu đọc đang trỏ vào ký hiệu $X$ trên băng, máy sẽ:
    1. Chuyển sang trạng thái mới $p$.
    2. Ghi đè ký hiệu mới $Y$ lên ô hiện tại.
    3. Di chuyển đầu đọc sang Trái ($L$ - Left) hoặc sang Phải ($R$ - Right) một ô.

### 2. Hình trạng (Instantaneous Description - ID) của Máy Turing:
- Ký hiệu: $\alpha = \langle \phi, s, a\psi \rangle$ hoặc viết gọn là $\phi s a \psi$:
  - $\phi$: Nội dung băng ở bên trái đầu đọc.
  - $s$: Trạng thái hiện tại của máy.
  - $a$: Ký hiệu tại ô mà đầu đọc đang trỏ tới.
  - $\psi$: Nội dung băng ở bên phải đầu đọc.
- Quy ước bước chuyển: $\alpha \vdash_M \beta$.
  - Nếu $\delta(s, a) = (p, Y, R) \implies \phi s a \psi \vdash \phi Y p \psi$ (đầu đọc sang phải).
  - Nếu $\delta(s, a) = (p, Y, L)$ và $\phi = \phi' X \implies \phi' X s a \psi \vdash \phi' p X Y \psi$ (đầu đọc sang trái).

### 3. Phân biệt Ngôn ngữ Đệ quy (Recursive) và Đệ quy liệt kê (Recursively Enumerable):

| Khái niệm | Tên gọi khác | Hành vi của máy Turing khi chạy chuỗi $w$ | Phân lớp Chomsky |
| :--- | :--- | :--- | :--- |
| **Ngôn ngữ Đệ quy liệt kê** (Recursively Enumerable - RE) | Turing-recognizable / Semi-decidable | - Nếu $w \in L$: Máy **dừng và chấp nhận**.<br>- Nếu $w \notin L$: Máy có thể **dừng từ chối HOẶC chạy lặp vô tận (Loop forever)**. | **Loại 0** (Văn phạm cấu trúc ngữ) |
| **Ngôn ngữ Đệ quy** (Recursive - R) | Turing-decidable / Decidable (Giải được) | - Nếu $w \in L$: Máy **dừng và chấp nhận**.<br>- Nếu $w \notin L$: Máy **dừng và từ chối**.<br>👉 **LUÔN LUÔN DỪNG trên mọi đầu vào!** | Nằm giữa Loại 1 và Loại 0 |

> [!IMPORTANT]
> **ĐỊNH LÝ BÙ QUAN TRỌNG:**
> Một ngôn ngữ $L$ là **Đệ quy (Recursive)** khi và chỉ khi **CẢ $L$ VÀ $\overline{L}$ ĐỀU LÀ ĐỆ QUY LIỆT KÊ (Recursively Enumerable)**!

### 4. Bài toán dừng (Halting Problem) & Tính không giải được (Undecidability):
- **Phát biểu Bài toán dừng:** *"Cho một máy Turing $M$ và một chuỗi đầu vào $w$, hãy xác định xem máy $M$ có dừng khi chạy với đầu vào $w$ hay không?"*
- **KẾT LUẬN LỊCH SỬ CỦA ALAN TURING (1936):** **Bài toán dừng là KHÔNG THỂ GIẢI ĐƯỢC (Undecidable)!** Không thể viết một chương trình máy tính nào có thể kiểm tra một chương trình tùy ý có bị treo vô tận hay không.

### 5. Bài toán tương ứng Post (Post Correspondence Problem - PCP):
- Cho hai danh sách các từ: $A = (x_1, x_2, \dots, x_k)$ và $B = (y_1, y_2, \dots, y_k)$.
- Tìm một dãy chỉ số $i_1, i_2, \dots, i_m$ ($m \ge 1$) sao cho:
  $$x_{i_1} x_{i_2} \dots x_{i_m} = y_{i_1} y_{i_2} \dots y_{i_m}$$
- **KẾT LUẬN:** Bài toán PCP trong trường hợp tổng quát là **KHÔNG THỂ GIẢI ĐƯỢC (Undecidable)**.

---

# PHẦN 1: CÁC DẠNG BÀI TẬP VÀ NGÂN HÀNG CÂU HỎI TRẮC NGHIỆM

---

## DẠNG 1: KHÁI NIỆM & ĐỊNH NGHĨA MÁY TURING (BỘ 7)

#### Câu 1: Máy Turing đơn định (DTM) là một bộ 7 $M = \langle Q, \Sigma, \Gamma, \delta, s_0, B, F \rangle$. Ký hiệu $B$ đại diện cho:
- A. Bảng chữ cái vào
- B. Ký hiệu ô trống (Blank symbol)
- C. Trạng thái bắt đầu
- D. Tập trạng thái kết thúc
👉 **Đáp án: B**
- **Giải thích:** $B$ là Blank symbol, đại diện cho các ô chưa được ghi trên băng (vô hạn về 2 phía hoặc về phía phải).

#### Câu 2: Trong định nghĩa máy Turing, mối quan hệ giữa bảng chữ cái vào $\Sigma$ và bảng chữ cái trên băng $\Gamma$ là:
- A. $\Gamma \subseteq \Sigma$
- B. $\Sigma \subset \Gamma$ và $B \in \Gamma \setminus \Sigma$
- C. $\Sigma = \Gamma$
- D. $\Sigma \cap \Gamma = \emptyset$
👉 **Đáp án: B**
- **Giải thích:** Bảng chữ cái trên băng $\Gamma$ luôn rộng hơn $\Sigma$, chứa toàn bộ $\Sigma$ cộng thêm ký hiệu ô trống $B$ và các ký hiệu phụ khác (ví dụ $X, Y$). Chuỗi đầu vào không bao giờ chứa $B$.

#### Câu 3: Hàm chuyển $\delta$ của máy Turing đơn định là ánh xạ:
- A. $\delta: Q \times \Gamma \to Q \times \Gamma \times \{L, R\}$
- B. $\delta: Q \times \Sigma \to Q$
- C. $\delta: Q \times \Gamma \to 2^Q$
- D. $\delta: Q \times \Sigma \to Q \times \{L, R\}$
👉 **Đáp án: A**
- **Giải thích:** Máy đọc ký hiệu trên băng ($\Gamma$), chuyển trạng thái mới ($Q$), ghi đè ký hiệu mới ($\Gamma$) và di chuyển đầu đọc sang trái $L$ hoặc sang phải $R$.

#### Câu 4: Khác biệt cốt lõi giữa Máy Turing và Ô-tô-mát đẩy xuống (PDA) là:
- A. Băng nhớ của máy Turing có thể vừa đọc vừa ghi và đầu đọc có thể di chuyển hai chiều (trái/phải)
- B. Máy Turing không có trạng thái kết thúc
- C. Máy Turing chỉ đọc được chuỗi nhị phân
- D. Máy Turing có bộ nhớ hữu hạn
👉 **Đáp án: A**
- **Giải thích:** PDA chỉ thao tác ở đỉnh ngăn xếp (LIFO), còn máy Turing có thể di chuyển tự do sang trái và phải trên băng nhớ vô hạn, ghi đè ký tự tùy ý.

#### Câu 5: Băng nhớ (Tape) của máy Turing chuẩn có đặc điểm:
- A. Có độ dài cố định 1024 ô
- B. Bị chặn ở đầu bên trái và vô hạn về phía bên phải (hoặc vô hạn về cả hai phía)
- C. Chỉ cho phép đọc, không cho phép ghi
- D. Tự động xóa sau mỗi bước
👉 **Đáp án: B**
- **Giải thích:** Băng nhớ của máy Turing được chia thành các ô (cells) và kéo dài vô hạn.

#### Câu 6: Khi máy Turing rơi vào một trạng thái và ký hiệu đọc vào mà hàm $\delta$ không định nghĩa bước chuyển tiếp theo:
- A. Máy bị lỗi cú pháp
- B. Máy dừng lại (Halt)
- C. Máy tự động quay về trạng thái ban đầu $s_0$
- D. Máy bị treo vô tận
👉 **Đáp án: B**
- **Giải thích:** Không có bước chuyển tiếp theo đồng nghĩa với việc máy kết thúc quá trình tính toán và dừng lại (Halt).

#### Câu 7: Một chuỗi $w$ được máy Turing đoán nhận nếu:
- A. Máy dừng lại ở một trạng thái thuộc tập $F$
- B. Máy xóa sạch băng nhớ
- C. Máy chạy mãi không dừng
- D. Đầu đọc quay về ô đầu tiên
👉 **Đáp án: A**
- **Giải thích:** Máy dừng ở trạng thái kết thúc $F \implies$ Chấp nhận chuỗi.

#### Câu 8: Khẳng định nào sau đây là ĐÚNG về máy Turing không đơn định (NTM) so với máy Turing đơn định (DTM)?
- A. NTM nhận diện được nhiều ngôn ngữ hơn DTM
- B. NTM và DTM hoàn toàn tương đương nhau về khả năng tính toán
- C. DTM mạnh hơn NTM
- D. NTM không thể mô phỏng được bằng DTM
👉 **Đáp án: B**
- **Giải thích:** Bất kỳ máy Turing không đơn định nào cũng có thể được mô phỏng bởi một máy Turing đơn định (dùng thuật toán duyệt theo chiều rộng BFS). Do đó khả năng nhận diện ngôn ngữ của chúng là như nhau.

#### Câu 9: Máy Turing có nhiều băng (Multi-tape Turing Machine) có khả năng tính toán:
- A. Mạnh hơn máy Turing 1 băng chuẩn
- B. Hoàn toàn tương đương máy Turing 1 băng chuẩn
- C. Yếu hơn máy Turing 1 băng
- D. Nhận diện được ngôn ngữ không đệ quy liệt kê
👉 **Đáp án: B**
- **Giải thích:** Định lý: Máy Turing nhiều băng có thể được mô phỏng hoàn toàn bởi máy Turing 1 băng (với thời gian tính toán tăng bậc hai).

#### Câu 10: Luận đề Church-Turing (Church-Turing Thesis) khẳng định rằng:
- A. Máy Turing là mô hình mạnh nhất, mọi thứ có thể tính toán được bằng thuật toán trong trực giác đều có thể tính toán được bằng Máy Turing
- B. Mọi bài toán toán học đều giải được
- C. Máy tính lượng tử vượt qua giới hạn của máy Turing về tính giải được
- D. C++ mạnh hơn máy Turing
👉 **Đáp án: A**
- **Giải thích:** Luận đề Church-Turing định nghĩa khái niệm "thuật toán" một cách hình thức thông qua máy Turing.

---

## DẠNG 2: HÌNH TRẠNG VÀ QUÁ TRÌNH TÍNH TOÁN CỦA MÁY TURING

#### Câu 11: Cho hình trạng $\alpha = \langle X, s_1, 01 \rangle$. Điều này có nghĩa là:
- A. Máy đang ở trạng thái $s_1$, nội dung băng bên trái là $X$, đầu đọc đang trỏ vào ô chứa ký tự `0`, và bên phải là `1`
- B. Máy đã đọc xong từ $X01$
- C. Máy dừng lại ở $s_1$
- D. Chuỗi trên băng là $s_1 X 01$
👉 **Đáp án: A**
- **Giải thích:** Cú pháp chuẩn của hình trạng ID: nội dung trước biến trạng thái là bên trái, ngay sau biến trạng thái là ký hiệu đầu đọc đang quét.

#### Câu 12: Cho máy Turing có bước chuyển $\delta(s_0, 0) = (s_1, X, R)$. Giả sử máy đang ở hình trạng $\langle \varepsilon, s_0, 001 \rangle$. Hình trạng tiếp theo là:
- A. $\langle X, s_1, 01 \rangle$
- B. $\langle \varepsilon, s_1, X01 \rangle$
- C. $\langle X0, s_1, 1 \rangle$
- D. $\langle 0, s_1, 01 \rangle$
👉 **Đáp án: A**
- **Giải thích:** Đang ở $s_0$ đọc số `0`. Máy chuyển sang $s_1$, ghi đè `0` thành $X$, và di chuyển sang Phải ($R$). Đầu đọc bây giờ trỏ vào số `0` thứ hai $\implies \langle X, s_1, 01 \rangle$.

#### Câu 13: Cho bước chuyển $\delta(s_1, 1) = (s_2, Y, L)$. Hình trạng hiện tại là $\langle X0, s_1, 1B \rangle$. Hình trạng tiếp theo là:
- A. $\langle X, s_2, 0YB \rangle$
- B. $\langle X0Y, s_2, B \rangle$
- C. $\langle X, s_2, YB \rangle$
- D. $\langle X0, s_2, Y \rangle$
👉 **Đáp án: A**
- **Giải thích:**
  - Ký tự `1` bị thay bởi $Y$.
  - Đầu đọc dịch sang Trái ($L$), do đó nó lùi về ô chứa ký tự `0` ở bên trái.
  - Hình trạng mới là $\langle X, s_2, 0YB \rangle$.

#### Câu 14: Hình trạng ban đầu (Initial ID) của máy Turing khi nạp chuỗi vào $w = a_1 a_2 \dots a_n$ là:
- A. $\langle \varepsilon, s_0, w \rangle$
- B. $\langle w, s_0, \varepsilon \rangle$
- C. $\langle B, s_0, w \rangle$
- D. $\langle s_0, w, B \rangle$
👉 **Đáp án: A**
- **Giải thích:** Máy bắt đầu ở trạng thái $s_0$, đầu đọc trỏ vào ký tự đầu tiên $a_1$, bên trái đầu đọc không có gì ($\varepsilon$).

#### Câu 15: Nếu từ hình trạng $\alpha$, máy không có bước chuyển nào tiếp theo, dãy hình trạng dừng lại. Ta nói quá trình tính toán:
- A. Bị lỗi
- B. Đã dừng (Halted)
- C. Lặp vô hạn
- D. Bị tràn bộ nhớ
👉 **Đáp án: B**

---

## DẠNG 3: NGÔN NGỮ ĐỆ QUY VÀ ĐỆ QUY LIỆT KÊ (RECURSIVE VS RE)

#### Câu 16: Ngôn ngữ được đoán nhận bởi một máy Turing (ngôn ngữ Loại 0 theo Chomsky) được gọi là:
- A. Ngôn ngữ chính quy
- B. Ngôn ngữ phi ngữ cảnh
- C. Ngôn ngữ đệ quy liệt kê (Recursively Enumerable)
- D. Ngôn ngữ hữu hạn
👉 **Đáp án: C**
- **Giải thích:** Lớp ngôn ngữ đoán nhận bởi máy Turing chính là ngôn ngữ đệ quy liệt kê (RE).

#### Câu 17: Điểm khác biệt DUY NHẤT giữa Ngôn ngữ Đệ quy (Recursive) và Ngôn ngữ Đệ quy liệt kê (RE) là:
- A. Với ngôn ngữ đệ quy, máy Turing LUÔN LUÔN DỪNG trên mọi chuỗi đầu vào (dù thuộc hay không thuộc ngôn ngữ)
- B. Ngôn ngữ đệ quy không thể mô phỏng bằng máy tính
- C. Ngôn ngữ đệ quy liệt kê có tính chất đóng kín ít hơn
- D. Ngôn ngữ đệ quy là tập con của ngôn ngữ chính quy
👉 **Đáp án: A**
- **Giải thích:** Ngôn ngữ đệ quy đảm bảo máy luôn dừng (Halts on all inputs) $\implies$ Giải được. Ngôn ngữ đệ quy liệt kê chỉ đảm bảo dừng khi chuỗi thuộc $L$, còn chuỗi không thuộc $L$ thì máy có thể lặp vô tận.

#### Câu 18: Cho $L$ là một ngôn ngữ. Khẳng định nào sau đây là ĐÚNG?
- A. Nếu $L$ là đệ quy thì $\overline{L}$ cũng là đệ quy
- B. Nếu $L$ là đệ quy liệt kê thì $\overline{L}$ cũng luôn là đệ quy liệt kê
- C. Mọi ngôn ngữ đệ quy liệt kê đều là đệ quy
- D. Không có ngôn ngữ nào là không đệ quy liệt kê
👉 **Đáp án: A**
- **Giải thích:** Lớp ngôn ngữ đệ quy ĐÓNG KÍN với phép lấy phần bù (chỉ cần đảo ngược trạng thái chấp nhận và từ chối của máy Turing luôn dừng).

#### Câu 19: Nếu ngôn ngữ $L$ là Đệ quy liệt kê (RE) và phần bù $\overline{L}$ CŨNG LÀ Đệ quy liệt kê (RE), thì $L$ chắc chắn là:
- A. Ngôn ngữ chính quy
- B. Ngôn ngữ Đệ quy (Recursive / Decidable)
- C. Ngôn ngữ phi ngữ cảnh
- D. Ngôn ngữ hữu hạn
👉 **Đáp án: B**
- **Giải thích:** Định lý cốt lõi: Cho hai máy $M_1$ nhận diện $L$ và $M_2$ nhận diện $\overline{L}$ chạy song song. Với mọi chuỗi $w$, chắc chắn đúng 1 trong 2 máy sẽ dừng $\implies$ Ghép lại thành một máy luôn dừng $\implies L$ là Đệ quy.

#### Câu 20: Ngôn ngữ nào sau đây là ví dụ kinh điển về ngôn ngữ ĐỆ QUY LIỆT KÊ nhưng KHÔNG ĐỆ QUY?
- A. Ngôn ngữ bài toán dừng $L_{halt} = \{ \langle M, w \rangle \mid M \text{ dừng trên } w \}$
- B. $L = \{ a^n b^n \mid n \ge 0 \}$
- C. $L = \{ a^n b^n c^n \mid n \ge 0 \}$
- D. $L = \Sigma^*$
👉 **Đáp án: A**
- **Giải thích:** Ngôn ngữ của bài toán dừng $L_{halt}$ là đệ quy liệt kê (chỉ cần mô phỏng $M$ chạy trên $w$, nếu $M$ dừng thì máy mô phỏng dừng chấp nhận). Nhưng nó KHÔNG đệ quy (vì bài toán dừng không giải được).

---

## DẠNG 4: BÀI TOÁN DỪNG VÀ TÍNH KHÔNG GIẢI ĐƯỢC (UNDECIDABILITY)

#### Câu 21: Một bài toán quyết định (Decision Problem) được gọi là "Giải được" (Decidable) nếu:
- A. Tồn tại một máy Turing luôn luôn dừng và trả lời đúng Có/Không (Yes/No) cho mọi đầu vào
- B. Máy Turing dừng cho ít nhất một đầu vào
- C. Có thể giải được trong thời gian 1 giây
- D. Nó có nghiệm duy nhất
👉 **Đáp án: A**
- **Giải thích:** Decidable đồng nghĩa với việc tồn tại thuật toán luôn kết thúc sau một số hữu hạn bước và đưa ra câu trả lời chính xác.

#### Câu 22: Bài toán dừng (Halting Problem) đã được chứng minh là không giải được bằng phương pháp nào?
- A. Quy nạp toán học
- B. Phương pháp đường chéo Cantor và phản chứng (Diagonalization & Contradiction)
- C. Bổ đề bơm
- D. Thuật toán phân hoạch
👉 **Đáp án: B**
- **Giải thích:** Alan Turing đã dùng kỹ thuật đường chéo giống như Cantor để tạo ra một máy phản ví dụ dẫn tới mâu thuẫn giả định (nếu nó dừng thì nó lặp, nếu nó lặp thì nó dừng).

#### Câu 23: Định lý Rice phát biểu rằng: Mọi tính chất ngữ nghĩa không tầm thường (Non-trivial semantic property) của ngôn ngữ được nhận diện bởi máy Turing đều:
- A. Giải được
- B. Không giải được (Undecidable)
- C. Chính quy
- D. Đa thức
👉 **Đáp án: B**
- **Giải thích:** Định lý Rice là định lý khái quát cực mạnh: Bất kỳ câu hỏi nào về hành vi của ngôn ngữ do máy Turing nhận diện (ví dụ: $L(M)$ có rỗng không? $L(M)$ có hữu hạn không? $L(M)$ có chính quy không?) đều là **KHÔNG THỂ GIẢI ĐƯỢC**!

#### Câu 24: Bài toán kiểm tra xem một máy Turing $M$ có đoán nhận chuỗi rỗng $\varepsilon$ hay không ($L(M) \ni \varepsilon$) là:
- A. Giải được
- B. Không giải được (Undecidable)
- C. Luôn đúng
- D. Giải được bằng DFA
👉 **Đáp án: B**
- **Giải thích:** Theo định lý Rice, đây là tính chất ngữ nghĩa không tầm thường của $L(M)$, do đó không giải được.

#### Câu 25: Bài toán nào sau đây là GIẢI ĐƯỢC (Decidable)?
- A. Kiểm tra xem một DFA có đoán nhận chuỗi rỗng không
- B. Kiểm tra xem một máy Turing có dừng trên chuỗi rỗng không
- C. Kiểm tra xem hai máy Turing có tương đương nhau không
- D. Kiểm tra xem ngôn ngữ của máy Turing có là chính quy không
👉 **Đáp án: A**
- **Giải thích:** Các bài toán kiểm tra trên DFA (tính rỗng, tính thuộc, tương đương) đều **GIẢI ĐƯỢC**. Chỉ các bài toán trên Máy Turing (và một số bài toán trên CFG) mới không giải được.

---

## DẠNG 5: BÀI TOÁN TƯƠNG ỨNG POST (PCP) & PHÂN CẤP CHOMSKY TOÀN DIỆN

#### Câu 26: Bài toán tương ứng Post (PCP) là bài toán tìm chuỗi các chỉ số ghép từ sao cho chuỗi ghép từ danh sách $A$ bằng chuỗi ghép từ danh sách $B$. Bài toán này:
- A. Luôn luôn giải được
- B. Không giải được trong trường hợp tổng quát (Undecidable)
- C. Chỉ giải được khi số từ $k \le 2$
- D. Cả B và C đều đúng
👉 **Đáp án: D**
- **Giải thích:** Khi $k=1$ hoặc $k=2$, PCP là giải được. Nhưng với $k \ge 7$ (hoặc tổng quát), PCP là bài toán không giải được.

#### Câu 27: Cho danh sách $A = (b, bab^3, ba)$ và $B = (b^3, ba, a)$. Dãy chỉ số $(2, 1, 1, 3)$ có phải là nghiệm của bài toán PCP không?
- Ta tính:
  - $A: bab^3 \cdot b \cdot b \cdot ba = bab^5 a$
  - $B: ba \cdot b^3 \cdot b^3 \cdot a = bab^6 a$
- Hai chuỗi $bab^5 a \ne bab^6 a$. Vậy:
- A. Là nghiệm
- B. Không phải là nghiệm
👉 **Đáp án: B** (vì chuỗi ghép lại không bằng nhau).

#### Câu 28: Ứng dụng quan trọng nhất của bài toán PCP là:
- A. Dùng để chứng minh nhiều bài toán khác trong văn phạm phi ngữ cảnh là không giải được (thông qua quy dẫn - Reduction)
- B. Tối thiểu hóa máy Turing
- C. Nén dữ liệu
- D. Mã hóa RSA
👉 **Đáp án: A**
- **Giải thích:** Nhà toán học Emil Post tạo ra PCP như một công cụ trung gian hoàn hảo để quy dẫn và chứng minh tính không giải được của các bài toán về CFG (như kiểm tra tính nhập nhằng, kiểm tra tương đương của 2 CFG).

#### Câu 29: Thứ tự bao hàm đúng nhất của các mô hình tính toán là:
- A. DFA $\equiv$ NFA $\subset$ DPDA $\subset$ NPDA $\subset$ LBA (Ô-tô-mát chặn tuyến tính) $\subset$ TM (Máy Turing)
- B. TM $\subset$ NPDA $\subset$ DFA
- C. DPDA $\equiv$ NPDA
- D. NFA $\subset$ DFA
👉 **Đáp án: A**
- **Giải thích:** Phân cấp sức mạnh tính toán kinh điển trong khoa học máy tính:
  - Hữu hạn: DFA $\equiv$ NFA (Loại 3)
  - Đẩy xuống đơn định: DPDA (DCFL)
  - Đẩy xuống không đơn định: NPDA (Loại 2)
  - Chặn tuyến tính: LBA (Loại 1)
  - Máy Turing: TM (Loại 0).

#### Câu 30: Văn phạm Loại 0 (Unrestricted Grammar) sinh ra đúng lớp ngôn ngữ nào?
- A. Ngôn ngữ chính quy
- B. Ngôn ngữ phi ngữ cảnh
- C. Ngôn ngữ cảm ngữ cảnh
- D. Ngôn ngữ đệ quy liệt kê (Recursively Enumerable)
👉 **Đáp án: D**
- **Giải thích:** Định lý Chomsky: Lớp ngôn ngữ sinh bởi văn phạm Loại 0 tương đương chính xác với lớp ngôn ngữ đoán nhận bởi Máy Turing (Đệ quy liệt kê).

---

## DẠNG 6: MỆNH ĐỀ LÝ THUYẾT ĐÚNG / SAI TỔNG HỢP TOÀN BỘ CHƯƠNG TRÌNH

#### Câu 31: Khẳng định nào sau đây là ĐÚNG?
- A. Mọi ngôn ngữ chính quy đều là ngôn ngữ phi ngữ cảnh
- B. Mọi ngôn ngữ phi ngữ cảnh đều là ngôn ngữ đệ quy
- C. Mọi ngôn ngữ đệ quy đều là ngôn ngữ đệ quy liệt kê
- D. Tất cả các khẳng định trên đều ĐÚNG
👉 **Đáp án: D**
- **Giải thích:** Chuỗi bao hàm hoàn chỉnh: $\text{Regular} \subset \text{CFL} \subset \text{Recursive} \subset \text{RE}$.

#### Câu 32: Bổ đề bơm tồn tại cho:
- A. Chỉ ngôn ngữ chính quy
- B. Chỉ ngôn ngữ phi ngữ cảnh
- C. Cả ngôn ngữ chính quy và ngôn ngữ phi ngữ cảnh (mỗi loại có bổ đề bơm riêng)
- D. Mọi ngôn ngữ loại 0
👉 **Đáp án: C**
- **Giải thích:** Bổ đề bơm $xyz$ cho ngôn ngữ chính quy, và bổ đề bơm $uvxyz$ cho ngôn ngữ phi ngữ cảnh.

#### Câu 33: Phép toán nào sau đây làm cho lớp ngôn ngữ phi ngữ cảnh KHÔNG ĐÓNG KÍN?
- A. Phép hợp ($\cup$)
- B. Phép giao ($\cap$)
- C. Phép ghép ($\cdot$)
- D. Phép sao Kleene ($*$)
👉 **Đáp án: B**

#### Câu 34: Một ngôn ngữ $L$ mà cả $L$ và phần bù $\overline{L}$ đều không phải là Đệ quy liệt kê:
- A. Tồn tại rất nhiều ngôn ngữ như vậy (theo định lý đếm Cantor)
- B. Không tồn tại ngôn ngữ nào như vậy
- C. Chỉ có ngôn ngữ rỗng
- D. Mọi ngôn ngữ đều đệ quy liệt kê
👉 **Đáp án: A**
- **Giải thích:** Tập tất cả các ngôn ngữ trên $\Sigma$ là không đếm được ($2^{\aleph_0}$), trong khi tập các máy Turing chỉ là đếm được ($\aleph_0$). Do đó có vô số ngôn ngữ vượt ra ngoài tầm với của máy Turing.

#### Câu 35: Khi giải bài thi trắc nghiệm cuối kỳ, nếu đề bài hỏi "Bài toán nào sau đây KHÔNG GIẢI ĐƯỢC?", dấu hiệu nhận biết nhanh nhất là:
- A. Bài toán hỏi về tính chất của DFA
- B. Bài toán dừng của máy Turing hoặc bài toán tính tương đương của hai CFG ($L(G_1) = L(G_2)$)
- C. Bài toán kiểm tra một chuỗi có thuộc ngôn ngữ chính quy không
- D. Bài toán tối thiểu hóa DFA
👉 **Đáp án: B**
- **Giải thích:** Mọi bài toán trên DFA đều giải được; bài toán kiểm tra chuỗi trên CFG giải được (thuật toán CYK). Nhưng bài toán tương đương 2 CFG, nhập nhằng của CFG, và các bài toán tổng quát trên Máy Turing là **KHÔNG GIẢI ĐƯỢC**.
