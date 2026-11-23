# NGÂN HÀNG TRẮC NGHIỆM CHƯƠNG 2: Ô-TÔ-MÁT HỮU HẠN (DFA, NFA, $\varepsilon$-NFA)
## TỐI THIỂU HÓA, CHUYỂN ĐỔI TẬP CON VÀ PHÂN DẠNG BÀI TẬP KÈM LỜI GIẢI CHI TIẾT

---

# TÓM TẮT LÝ THUYẾT & BÍ KÍP "ĂN TRỌN ĐIỂM" CHƯƠNG 2

### 1. Định nghĩa Ô-tô-mát hữu hạn (Bộ 5 thành phần):
Mọi ô-tô-mát hữu hạn (FA) đều là bộ 5:
$$M = \langle Q, \Sigma, \delta, q_0, F \rangle$$
- $Q$: Tập hữu hạn các trạng thái.
- $\Sigma$: Bảng chữ cái vào (ký hiệu đọc).
- $\delta$: Hàm chuyển (hoặc ánh xạ chuyển).
- $q_0 \in Q$: Trạng thái bắt đầu duy nhất.
- $F \subseteq Q$: Tập các trạng thái kết thúc / chấp nhận (vòng tròn kép). Có thể rỗng ($F = \emptyset$), có thể có 1 hoặc nhiều trạng thái.

### 2. Phân biệt DFA, NFA và $\varepsilon$-NFA:

| Tiêu chí | DFA (Đơn định) | NFA (Không đơn định) | $\varepsilon$-NFA (Có bước chuyển rỗng) |
| :--- | :--- | :--- | :--- |
| **Miền xác định hàm $\delta$** | $\delta: Q \times \Sigma \to Q$ | $\delta: Q \times \Sigma \to 2^Q$ | $\delta: Q \times (\Sigma \cup \{\varepsilon\}) \to 2^Q$ |
| **Số nhánh rẽ từ 1 trạng thái** | Đúng **1 nhánh duy nhất** cho mỗi ký tự trong $\Sigma$ | Có thể **0, 1 hoặc nhiều nhánh** | Có thể đi tiếp mà **không cần đọc ký tự** ($\varepsilon$) |
| **Khả năng nhận diện ngôn ngữ** | **NGANG NHAU!** Cả 3 mô hình đều nhận diện chính xác lớp **Ngôn ngữ chính quy (Loại 3)** |
| **Số trạng thái khi đổi sang DFA** | Chuẩn | NFA có $n$ trạng thái $\implies$ DFA tương đương có tối đa **$2^n$ trạng thái** |

### 3. Thuật toán Bao đóng $\varepsilon$ ($\varepsilon$-closure):
- $\varepsilon\text{-closure}(q)$: Là tập gồm chính $q$ và tất cả các trạng thái có thể đi tới từ $q$ chỉ bằng các cung mang nhãn $\varepsilon$.
- Trạng thái bắt đầu của DFA tương đương luôn là: $S_0 = \varepsilon\text{-closure}(q_0)$.

### 4. Thuật toán Tối thiểu hóa DFA (Minimization):
- **Bước 1:** Loại bỏ các trạng thái **không đến được** (unreachable states) từ trạng thái bắt đầu.
- **Bước 2:** Phân hoạch ban đầu thành 2 nhóm: Nhóm chấp nhận $F$ và nhóm không chấp nhận $Q \setminus F$.
- **Bước 3:** Chia nhỏ từng nhóm nếu tồn tại 2 trạng thái khi đọc cùng một ký tự mà nhảy sang 2 nhóm khác nhau.
- **Bước 4:** Lặp lại cho đến khi không chia được nữa. Mỗi nhóm còn lại gộp thành 1 trạng thái của DFA tối giản.

> [!TIP]
> **MẸO NHẨM NHANH SỐ TRẠNG THÁI TỐI THIỂU CỦA DFA:**
> - Nhận diện chuỗi **kết thúc bằng một từ con độ dài $k$** (ví dụ kết thúc bằng `01`, $k=2$) $\implies$ Cần tối thiểu **$k + 1$ trạng thái** (ví dụ $2+1 = 3$ trạng thái).
> - Nhận diện chuỗi có **độ dài chia hết cho $m$** (hoặc số lượng chữ $a$ chia hết cho $m$) $\implies$ Cần đúng **$m$ trạng thái** (tương ứng số dư $0, 1, \dots, m-1$).
> - Nhận diện chuỗi có **số chữ $a$ chẵn và số chữ $b$ lẻ** $\implies$ Cần $2 \times 2 = \mathbf{4}$ **trạng thái**.

---

# PHẦN 1: CÁC DẠNG BÀI TẬP VÀ NGÂN HÀNG CÂU HỎI TRẮC NGHIỆM

---

## DẠNG 1: KHÁI NIỆM & ĐỊNH NGHĨA DFA, NFA, $\varepsilon$-NFA

#### Câu 1: Một ô-tô-mát hữu hạn đơn định (DFA) là một bộ 5 $M = \langle Q, \Sigma, \delta, q_0, F \rangle$, trong đó hàm chuyển $\delta$ là ánh xạ:
- A. $\delta: Q \times \Sigma \to 2^Q$
- B. $\delta: Q \times \Sigma \to Q$
- C. $\delta: Q \times (\Sigma \cup \{\varepsilon\}) \to Q$
- D. $\delta: Q \to \Sigma$
👉 **Đáp án: B**
- **Giải thích:** DFA là đơn định, nên từ một trạng thái đọc một ký hiệu chỉ đi đến đúng một trạng thái duy nhất thuộc $Q$.

#### Câu 2: Trong NFA, giá trị của $\delta(q, a)$ là:
- A. Một trạng thái duy nhất
- B. Một tập hợp con của $Q$ (thuộc $2^Q$)
- C. Một ký tự thuộc $\Sigma$
- D. Luôn luôn khác rỗng
👉 **Đáp án: B**
- **Giải thích:** NFA cho phép đi tới nhiều trạng thái hoặc không đi tới đâu ($\emptyset$), nên kết quả là một phần tử của tập lũy thừa $2^Q$.

#### Câu 3: Khẳng định nào sau đây là ĐÚNG về khả năng nhận diện ngôn ngữ giữa DFA và NFA?
- A. NFA nhận diện được nhiều ngôn ngữ hơn DFA
- B. DFA nhận diện được nhiều ngôn ngữ hơn NFA
- C. DFA và NFA có khả năng nhận diện ngôn ngữ hoàn toàn tương đương nhau
- D. $\varepsilon$-NFA mạnh hơn NFA
👉 **Đáp án: C**
- **Giải thích:** Cả DFA, NFA và $\varepsilon$-NFA đều chỉ nhận diện đúng lớp **Ngôn ngữ chính quy**. Bất kỳ NFA nào cũng có thể chuyển đổi thành DFA tương đương.

#### Câu 4: Một từ $w \in \Sigma^*$ được DFA $M = \langle Q, \Sigma, \delta, q_0, F \rangle$ đoán nhận khi và chỉ khi:
- A. Sau khi đọc hết từ $w$, máy dừng lại ở một trạng thái thuộc $F$
- B. Trong quá trình đọc từ $w$, máy đi qua ít nhất một trạng thái thuộc $F$
- C. Máy dừng lại ở trạng thái bắt đầu $q_0$
- D. Máy không rơi vào ngõ cụt
👉 **Đáp án: A**
- **Giải thích:** Chuỗi được chấp nhận nếu trạng thái kết thúc của toàn bộ quá trình đọc chuỗi thuộc tập trạng thái kết thúc $F$: $\hat{\delta}(q_0, w) \in F$.

#### Câu 5: Từ rỗng $\varepsilon$ được DFA đoán nhận khi và chỉ khi:
- A. $F = Q$
- B. Trạng thái bắt đầu $q_0 \in F$
- C. $F = \emptyset$
- D. Có bước chuyển $\varepsilon$
👉 **Đáp án: B**
- **Giải thích:** Khi đọc chuỗi rỗng $\varepsilon$, máy không đổi trạng thái mà đứng yên tại $q_0$. Để $\varepsilon$ được chấp nhận thì $q_0$ bắt buộc phải là trạng thái kết thúc ($q_0 \in F$).

#### Câu 6: Cho NFA có $n$ trạng thái. DFA tương đương được xây dựng bằng phương pháp tập con có tối đa bao nhiêu trạng thái?
- A. $n$
- B. $n^2$
- C. $2^n$
- D. $2n$
👉 **Đáp án: C**
- **Giải thích:** Vì mỗi trạng thái của DFA là một tập con của tập trạng thái NFA, và tập hợp có $n$ phần tử thì có đúng $2^n$ tập con.

#### Câu 7: Điểm khác biệt DUY NHẤT giữa $\varepsilon$-NFA và NFA thông thường là:
- A. $\varepsilon$-NFA có nhiều trạng thái bắt đầu
- B. $\varepsilon$-NFA cho phép bước chuyển trạng thái mà không cần tiêu thụ ký tự vào (nhãn $\varepsilon$)
- C. $\varepsilon$-NFA nhận diện được ngôn ngữ phi ngữ cảnh
- D. $\varepsilon$-NFA không có trạng thái kết thúc
👉 **Đáp án: B**
- **Giải thích:** $\varepsilon$-NFA mở rộng miền xác định của hàm chuyển thêm ký hiệu rỗng $\varepsilon$.

#### Câu 8: Một DFA có tập trạng thái kết thúc $F = \emptyset$ thì ngôn ngữ được đoán nhận $L(M)$ là:
- A. $\{\varepsilon\}$
- B. $\emptyset$ (Tập rỗng)
- C. $\Sigma^*$
- D. Không xác định được
👉 **Đáp án: B**
- **Giải thích:** Vì không có bất kỳ trạng thái kết thúc nào, nên không có chuỗi nào có thể kết thúc tại $F \implies L(M) = \emptyset$.

#### Câu 9: Trạng thái "bẫy" (Dead state / Trap state) trong DFA là trạng thái:
- A. Không thuộc $F$, và với mọi ký tự vào đều tự quay về chính nó
- B. Thuộc $F$, và không thể đi ra khỏi nó
- C. Không thể đến được từ trạng thái bắt đầu
- D. Luôn luôn xuất hiện trong mọi DFA
👉 **Đáp án: A**
- **Giải thích:** Trạng thái bẫy là trạng thái không chấp nhận, khi đã rơi vào đó thì không thể nào thoát ra để đến được trạng thái kết thúc nữa.

#### Câu 10: Cho DFA $M$. Nếu ta đổi tất cả các trạng thái không kết thúc thành kết thúc ($Q \setminus F$) và ngược lại, DFA mới sẽ đoán nhận ngôn ngữ:
- A. $L(M)^R$ (Đảo ngược)
- B. $\overline{L(M)} = \Sigma^* \setminus L(M)$ (Phần bù)
- C. $L(M)^*$ (Bao đóng Kleene)
- D. Ngôn ngữ rỗng
👉 **Đáp án: B**
- **Giải thích:** Đây là thuật toán tìm phần bù của ngôn ngữ chính quy: đảo vai trò của tập $F$ và $Q \setminus F$.

---

## DẠNG 2: TRUY VẾT & ĐOÁN NHẬN CHUỖI TRÊN AUTOMATA

#### Câu 11: Cho DFA có các trạng thái $\{q_0, q_1\}$, trạng thái đầu $q_0$, kết thúc $F = \{q_1\}$. Hàm chuyển: $\delta(q_0, 0) = q_0, \delta(q_0, 1) = q_1, \delta(q_1, 0) = q_1, \delta(q_1, 1) = q_0$. Chuỗi nào sau đây được đoán nhận?
- A. `0010`
- B. `0101`
- C. `1011`
- D. `000`
👉 **Đáp án: A**
- **Giải thích:**
  - Để ý: mỗi khi đọc số 1 thì trạng thái đổi giữa $q_0$ và $q_1$. Máy bắt đầu ở $q_0$ (chẵn số 1), kết thúc ở $q_1$ (lẻ số 1).
  - Chuỗi `0010` có đúng 1 chữ số 1 (lẻ) $\implies$ Dừng ở $q_1 \in F$ (Đoán nhận!).
  - `0101` có hai số 1 (chẵn) $\implies$ dừng ở $q_0 \notin F$.

#### Câu 12: Với DFA ở Câu 11, ngôn ngữ được đoán nhận $L(M)$ là:
- A. Tập các chuỗi nhị phân có chứa ít nhất một số 1
- B. Tập các chuỗi nhị phân có số lượng số 1 là số LẺ
- C. Tập các chuỗi nhị phân có số lượng số 1 là số CHẴN
- D. Tập các chuỗi nhị phân kết thúc bằng 1
👉 **Đáp án: B**

#### Câu 13: Cho DFA có $Q = \{A, B, C\}$, trạng thái đầu $A$, $F = \{C\}$. Bước chuyển:
- $\delta(A, a) = B, \delta(A, b) = A$
- $\delta(B, a) = B, \delta(B, b) = C$
- $\delta(C, a) = B, \delta(C, b) = A$
Chuỗi nào sau đây KHÔNG được đoán nhận?
- A. `ab`
- B. `aab`
- C. `bab`
- D. `aba`
👉 **Đáp án: D**
- **Giải thích:**
  - Chạy `aba`: $A \xrightarrow{a} B \xrightarrow{b} C \xrightarrow{a} B \notin F$ (Không được đoán nhận!).
  - Chạy `ab`: $A \xrightarrow{a} B \xrightarrow{b} C \in F$ (Đoán nhận).

#### Câu 14: Với DFA ở Câu 13, đặc điểm của chuỗi được đoán nhận là:
- A. Bắt đầu bằng $a$
- B. Kết thúc bằng cụm `ab`
- C. Chứa số lượng chữ $b$ chẵn
- D. Có độ dài chia hết cho 3
👉 **Đáp án: B**
- **Giải thích:** Nhìn vào trạng thái kết thúc $C$: cung duy nhất đi vào $C$ là cung có nhãn $b$ xuất phát từ $B$, mà muốn đến $B$ thì phải vừa đọc ký tự $a$. Do đó mọi chuỗi kết thúc ở $C$ bắt buộc phải có tận cùng là `ab`.

#### Câu 15: Cho NFA có $Q = \{q_0, q_1\}$, trạng thái đầu $q_0$, $F = \{q_1\}$. Bước chuyển:
- $\delta(q_0, 0) = \{q_0, q_1\}, \delta(q_0, 1) = \{q_0\}$
- $\delta(q_1, 0) = \emptyset, \delta(q_1, 1) = \emptyset$
Chuỗi nào sau đây được đoán nhận?
- A. `111`
- B. `101`
- C. `110`
- D. $\varepsilon$
👉 **Đáp án: C**
- **Giải thích:** Trạng thái kết thúc $q_1$ chỉ có thể đạt được khi ký tự cuối cùng đọc vào là số `0`. Do đó chuỗi phải kết thúc bằng `0`. `110` chạy: $q_0 \xrightarrow{1} q_0 \xrightarrow{1} q_0 \xrightarrow{0} q_1 \in F$ (Đoán nhận!).

---

## DẠNG 3: BAO ĐÓNG $\varepsilon$ VÀ CHUYỂN NFA SANG DFA

#### Câu 16: Cho $\varepsilon$-NFA có các bước chuyển rỗng: $\delta(q_0, \varepsilon) = \{q_1\}, \delta(q_1, \varepsilon) = \{q_2\}$. Bao đóng $\varepsilon\text{-closure}(q_0)$ bằng:
- A. $\{q_0\}$
- B. $\{q_0, q_1\}$
- C. $\{q_0, q_1, q_2\}$
- D. $\{q_1, q_2\}$
👉 **Đáp án: C**
- **Giải thích:** $\varepsilon\text{-closure}(q_0)$ bao gồm chính $q_0$, đi qua $\varepsilon$ đến $q_1$, đi tiếp qua $\varepsilon$ đến $q_2 \implies \{q_0, q_1, q_2\}$.

#### Câu 17: Cho $\varepsilon$-NFA có $Q = \{A, B, C\}$, không có bước chuyển $\varepsilon$ nào xuất phát từ $B$. Khi đó $\varepsilon\text{-closure}(B)$ bằng:
- A. $\emptyset$
- B. $\{B\}$
- C. $\{A, B, C\}$
- D. Không xác định được
👉 **Đáp án: B**
- **Giải thích:** Theo định nghĩa, bao đóng $\varepsilon$ của một trạng thái LUÔN LUÔN chứa chính nó, dù không có bước chuyển $\varepsilon$ nào đi ra.

#### Câu 18: Khi chuyển đổi NFA $M = \langle Q, \Sigma, \delta, q_0, F \rangle$ sang DFA $M' = \langle Q', \Sigma, \delta', q_0', F' \rangle$, một trạng thái $S \in Q'$ của DFA là trạng thái kết thúc khi và chỉ khi:
- A. $S \subseteq F$
- B. $S \cap F \ne \emptyset$ (chứa ít nhất một trạng thái kết thúc của NFA)
- C. $S = F$
- D. $q_0 \in S$
👉 **Đáp án: B**
- **Giải thích:** Chỉ cần tập hợp con $S$ có chứa ít nhất một trạng thái thuộc $F$ thì toàn bộ tập $S$ được coi là trạng thái kết thúc của DFA.

#### Câu 19: Cho NFA có bảng chuyển trạng thái sau ($\Sigma = \{a, b\}$):
- $\delta(q_0, a) = \{q_0, q_1\}, \delta(q_0, b) = \{q_0\}$
- $\delta(q_1, a) = \emptyset, \delta(q_1, b) = \{q_2\}$
- $\delta(q_2, a) = \emptyset, \delta(q_2, b) = \emptyset$
Trạng thái ban đầu của DFA tương đương là $S_0 = \{q_0\}$. Khi đọc ký tự $a$, DFA chuyển đến trạng thái nào?
- A. $\{q_0\}$
- B. $\{q_1\}$
- C. $\{q_0, q_1\}$
- D. $\{q_2\}$
👉 **Đáp án: C**
- **Giải thích:** $\delta'(\{q_0\}, a) = \delta(q_0, a) = \{q_0, q_1\}$.

#### Câu 20: Tiếp tục Câu 19, từ trạng thái $\{q_0, q_1\}$, khi đọc ký tự $b$, DFA chuyển đến trạng thái nào?
- A. $\{q_0\}$
- B. $\{q_2\}$
- C. $\{q_0, q_2\}$
- D. $\{q_0, q_1, q_2\}$
👉 **Đáp án: C**
- **Giải thích:** $\delta'(\{q_0, q_1\}, b) = \delta(q_0, b) \cup \delta(q_1, b) = \{q_0\} \cup \{q_2\} = \{q_0, q_2\}$.

---

## DẠNG 4: TỐI THIỂU HÓA TRẠNG THÁI DFA

#### Câu 21: Mục đích của thuật toán tối thiểu hóa DFA là:
- A. Chuyển DFA thành NFA
- B. Tìm một DFA tương đương có số lượng trạng thái là ít nhất
- C. Loại bỏ các ký tự kết thúc
- D. Làm cho ô-tô-mát đoán nhận được từ rỗng
👉 **Đáp án: B**

#### Câu 22: Hai trạng thái $p$ và $q$ của DFA được gọi là tương đương nhau (không phân biệt được) khi và chỉ khi:
- A. $\delta(p, a) = \delta(q, a)$ với mọi $a \in \Sigma$
- B. Với mọi chuỗi $w \in \Sigma^*$, $\hat{\delta}(p, w) \in F \iff \hat{\delta}(q, w) \in F$
- C. Cả hai trạng thái đều thuộc $F$
- D. Cả hai trạng thái đều không thuộc $F$
👉 **Đáp án: B**
- **Giải thích:** Định nghĩa Myhill-Nerode: Với mọi chuỗi thử $w$, đi từ $p$ hay đi từ $q$ đều cùng cho ra kết quả (cùng được chấp nhận hoặc cùng bị từ chối).

#### Câu 23: Trong thuật toán phân hoạch tối thiểu hóa DFA, bước phân hoạch đầu tiên chia tập trạng thái $Q$ thành 2 nhóm là:
- A. Nhóm có chỉ số chẵn và nhóm có chỉ số lẻ
- B. Nhóm các trạng thái kết thúc $F$ và nhóm các trạng thái không kết thúc $Q \setminus F$
- C. Nhóm trạng thái bắt đầu và nhóm các trạng thái còn lại
- D. Nhóm các trạng thái đến được và nhóm không đến được
👉 **Đáp án: B**
- **Giải thích:** Một trạng thái thuộc $F$ và một trạng thái không thuộc $F$ luôn luôn bị phân biệt bởi chuỗi rỗng $\varepsilon$, do đó không bao giờ có thể gộp chung với nhau.

#### Câu 24: Cho DFA có các trạng thái $\{A, B, C\}$, $F = \{B, C\}$. Bước chuyển:
- $\delta(A, 0) = B, \delta(A, 1) = C$
- $\delta(B, 0) = B, \delta(B, 1) = C$
- $\delta(C, 0) = B, \delta(C, 1) = C$
DFA tối giản tương đương có bao nhiêu trạng thái?
- A. 1
- B. 2
- C. 3
- D. 0
👉 **Đáp án: B**
- **Giải thích:**
  - Nhìn vào $B$ và $C$: Cả hai đều thuộc $F$. Đọc 0 đều về $B$, đọc 1 đều về $C$.
  - Do đó $B$ và $C$ hành xử giống hệt nhau với mọi đầu vào $\implies B$ và $C$ tương đương nhau, gộp thành một trạng thái $\{B, C\}$.
  - DFA tối giản chỉ còn 2 trạng thái: $A$ và $\{B, C\}$.

#### Câu 25: Trước khi tiến hành phân hoạch tối thiểu hóa DFA, bước bắt buộc phải làm đầu tiên là:
- A. Đổi tên các trạng thái
- B. Loại bỏ các trạng thái không đến được (unreachable states) từ trạng thái bắt đầu
- C. Thêm trạng thái bẫy
- D. Chuyển DFA sang NFA
👉 **Đáp án: B**
- **Giải thích:** Trạng thái không đến được không ảnh hưởng gì đến ngôn ngữ của ô-tô-mát nhưng nếu không loại bỏ sẽ làm sai số trạng thái tối thiểu.

---

## DẠNG 5: NHẬN DIỆN NGÔN NGỮ & SỐ TRẠNG THÁI TỐI THIỂU CẦN THIẾT

#### Câu 26: Số trạng thái tối thiểu của một DFA nhận diện ngôn ngữ các chuỗi trên $\{0, 1\}$ kết thúc bằng `01` là:
- A. 2
- B. 3
- C. 4
- D. 5
👉 **Đáp án: B**
- **Giải thích:** Quy tắc: Cần tối thiểu $k+1$ trạng thái với $k$ là độ dài chuỗi đuôi. Chuỗi `01` dài 2 $\implies$ cần $2 + 1 = 3$ trạng thái ($q_0$: chưa có gì, $q_1$: vừa thấy `0`, $q_2$: vừa thấy `01` - kết thúc).

#### Câu 27: Số trạng thái tối thiểu của một DFA nhận diện ngôn ngữ các chuỗi trên $\{0, 1\}$ có chứa chuỗi con `101` là:
- A. 3
- B. 4
- C. 5
- D. 6
👉 **Đáp án: B**
- **Giải thích:** Nhận diện chuỗi con độ dài 3 cần $3 + 1 = 4$ trạng thái (Trạng thái 4 là trạng thái kết thúc bẫy, hễ đã thấy `101` thì ở lại đó mãi mãi).

#### Câu 28: Số trạng thái tối thiểu của một DFA nhận diện ngôn ngữ các chuỗi nhị phân có độ dài chia hết cho 3 là:
- A. 2
- B. 3
- C. 4
- D. 1
👉 **Đáp án: B**
- **Giải thích:** Các số dư khi chia cho 3 là $\{0, 1, 2\}$, tương ứng với đúng 3 trạng thái. Trạng thái số dư 0 là trạng thái kết thúc.

#### Câu 29: Số trạng thái tối thiểu của một DFA nhận diện ngôn ngữ các chuỗi trên $\{a, b\}$ có số lượng ký tự $a$ là số CHẴN và số lượng ký tự $b$ là số CHẴN là:
- A. 2
- B. 4
- C. 3
- D. 8
👉 **Đáp án: B**
- **Giải thích:** Có 4 tổ hợp tính chẵn lẻ: (chẵn a, chẵn b), (chẵn a, lẻ b), (lẻ a, chẵn b), (lẻ a, lẻ b) $\implies$ Cần đúng $2 \times 2 = 4$ trạng thái.

#### Câu 30: Số trạng thái tối thiểu của một DFA nhận diện ngôn ngữ các chuỗi nhị phân biểu diễn số nguyên chia hết cho 5 (ở hệ thập phân) là:
- A. 4
- B. 5
- C. 6
- D. 10
👉 **Đáp án: B**
- **Giải thích:** Cần 5 trạng thái tương ứng với 5 số dư khi chia cho 5: $\{0, 1, 2, 3, 4\}$.

#### Câu 31: DFA nhận diện ngôn ngữ $L = \{ w \in \{a, b\}^* \mid |w| \ge 2 \}$ cần tối thiểu bao nhiêu trạng thái?
- A. 2
- B. 3
- C. 4
- D. 5
👉 **Đáp án: B**
- **Giải thích:** $q_0$ (dài 0), $q_1$ (dài 1), $q_2$ (dài $\ge 2$, kết thúc) $\implies 3$ trạng thái.

#### Câu 32: DFA nhận diện ngôn ngữ $L = \{ w \in \{a, b\}^* \mid |w| \le 2 \}$ cần tối thiểu bao nhiêu trạng thái?
- A. 3
- B. 4
- C. 2
- D. 5
👉 **Đáp án: B**
- **Giải thích:** $q_0$ (dài 0, kết thúc), $q_1$ (dài 1, kết thúc), $q_2$ (dài 2, kết thúc), $q_3$ (dài $\ge 3$, bẫy không kết thúc) $\implies 4$ trạng thái.

#### Câu 33: DFA nhận diện ngôn ngữ bắt đầu bằng chữ $a$ trên bảng chữ cái $\{a, b\}$ cần tối thiểu bao nhiêu trạng thái?
- A. 2
- B. 3
- C. 4
- D. 1
👉 **Đáp án: B**
- **Giải thích:** $q_0$ (bắt đầu), $q_1$ (đã đọc $a$, kết thúc), $q_2$ (đã đọc $b$, bẫy chết) $\implies 3$ trạng thái.

#### Câu 34: DFA nhận diện ngôn ngữ các chuỗi có số chữ $a$ chia hết cho 2 HOẶC số chữ $b$ chia hết cho 2 cần tối đa bao nhiêu trạng thái?
- A. 2
- B. 4
- C. 8
- D. 6
👉 **Đáp án: B**
- **Giải thích:** Dùng tích Descartes giữa máy đếm $a$ (2 trạng thái) và máy đếm $b$ (2 trạng thái) $\implies 2 \times 2 = 4$ trạng thái.

#### Câu 35: DFA nhận diện ngôn ngữ các chuỗi có chứa ít nhất một ký tự $a$ trên $\{a, b\}$ cần tối thiểu bao nhiêu trạng thái?
- A. 1
- B. 2
- C. 3
- D. 4
👉 **Đáp án: B**
- **Giải thích:** $q_0$ (chưa có $a$, lặp $b$), gặp $a$ nhảy sang $q_1$ (kết thúc, lặp $a, b$) $\implies 2$ trạng thái.

---

## DẠNG 6: MỆNH ĐỀ LÝ THUYẾT ĐÚNG / SAI TỔNG HỢP

#### Câu 36: Khẳng định nào sau đây là SAI?
- A. Một DFA có thể có nhiều trạng thái bắt đầu
- B. Một DFA có thể có nhiều trạng thái kết thúc
- C. Một DFA có thể không có trạng thái kết thúc nào
- D. Trạng thái bắt đầu của DFA có thể đồng thời là trạng thái kết thúc
👉 **Đáp án: A**
- **Giải thích:** Theo định nghĩa, DFA chỉ có DUY NHẤT một trạng thái bắt đầu $q_0$.

#### Câu 37: Khẳng định nào sau đây là ĐÚNG về đồ thị chuyển trạng thái của DFA?
- A. Từ mỗi đỉnh, với mỗi ký tự trong bảng chữ cái, có đúng một cung đi ra
- B. Từ mỗi đỉnh có thể có cung mang nhãn $\varepsilon$
- C. Tổng số cung đi ra từ một đỉnh luôn bằng số trạng thái
- D. Không được phép có khuyên (cung tự quay về chính nó)
👉 **Đáp án: A**
- **Giải thích:** Định nghĩa tính đơn định và toàn phần của DFA.

#### Câu 38: Nếu một ngôn ngữ $L$ được nhận diện bởi NFA có 3 trạng thái, thì DFA tối giản nhận diện $L$ có thể có số trạng thái là:
- A. 1 trạng thái
- B. 4 trạng thái
- C. 8 trạng thái
- D. Tất cả các khả năng trên đều có thể xảy ra
👉 **Đáp án: D**
- **Giải thích:** Số trạng thái của DFA tối giản nằm trong khoảng từ $1$ đến $2^3 = 8$ trạng thái.

#### Câu 39: Trong bảng phân biệt trạng thái Myhill-Nerode, ô $(p, q)$ được đánh dấu 'X' (phân biệt được) ngay ở bước cơ sở nếu:
- A. $p$ và $q$ cùng thuộc $F$
- B. $p \in F$ và $q \notin F$ (hoặc ngược lại)
- C. $p = q_0$
- D. $p = q$
👉 **Đáp án: B**
- **Giải thích:** Một trạng thái chấp nhận và một trạng thái từ chối luôn phân biệt được bởi chuỗi rỗng $\varepsilon$.

#### Câu 40: Ngôn ngữ nào sau đây KHÔNG THỂ nhận diện được bởi bất kỳ ô-tô-mát hữu hạn nào?
- A. $\{ a^n b^m \mid n, m \ge 0 \}$
- B. $\{ a^n b^n \mid n \ge 0 \}$
- C. $\{ a^n \mid n \text{ chia hết cho 5} \}$
- D. $\{ w \in \{0, 1\}^* \mid w \text{ kết thúc bằng 00} \}$
👉 **Đáp án: B**
- **Giải thích:** $\{a^n b^n \mid n \ge 0\}$ là ngôn ngữ phi ngữ cảnh phi chính quy, đòi hỏi bộ nhớ vô hạn để đếm số $a$ bằng số $b$, ô-tô-mát hữu hạn chỉ có bộ nhớ hữu hạn nên bất lực.

#### Câu 41: Bổ đề bơm (Pumping Lemma) cho ngôn ngữ chính quy được sử dụng để:
- A. Chứng minh một ngôn ngữ là chính quy
- B. Chứng minh một ngôn ngữ KHÔNG PHẢI là chính quy
- C. Tối thiểu hóa DFA
- D. Chuyển NFA sang DFA
👉 **Đáp án: B**
- **Giải thích:** Bổ đề bơm là điều kiện cần của ngôn ngữ chính quy, dùng phương pháp phản chứng để chứng minh một ngôn ngữ phi chính quy.

#### Câu 42: Cho NFA $M$. Nếu từ trạng thái bắt đầu $q_0$ không có đường đi nào tới được bất kỳ trạng thái kết thúc nào trong $F$, thì:
- A. $L(M) = \emptyset$
- B. $L(M) = \{\varepsilon\}$
- C. $L(M) = \Sigma^*$
- D. Máy bị lỗi cú pháp
👉 **Đáp án: A**

#### Câu 43: Khi thực hiện phép giao giữa 2 ngôn ngữ chính quy $L_1$ và $L_2$ nhận diện bởi 2 DFA có số trạng thái lần lượt là $m$ và $n$, DFA tích nhận diện $L_1 \cap L_2$ có số trạng thái là:
- A. $m + n$
- B. $m \times n$
- C. $m^n$
- D. $2^{m+n}$
👉 **Đáp án: B**
- **Giải thích:** Thuật toán nhân tích Descartes (Product Automaton) ghép cặp các trạng thái $(q_i, p_j) \implies m \times n$ trạng thái.

#### Câu 44: Trong DFA tích cho $L_1 \cap L_2$ ở Câu 43, trạng thái $(q_i, p_j)$ là trạng thái kết thúc khi:
- A. $q_i \in F_1$ HOẶC $p_j \in F_2$
- B. $q_i \in F_1$ VÀ $p_j \in F_2$
- C. $q_i = p_j$
- D. $q_i \notin F_1$
👉 **Đáp án: B**
- **Giải thích:** Phép giao ($\cap$) đòi hỏi chuỗi phải được chấp nhận bởi CẢ HAI máy.

#### Câu 45: Trong DFA tích cho $L_1 \cup L_2$, trạng thái $(q_i, p_j)$ là trạng thái kết thúc khi:
- A. $q_i \in F_1$ HOẶC $p_j \in F_2$
- B. $q_i \in F_1$ VÀ $p_j \in F_2$
- C. $q_i \notin F_1$
- D. $p_j \notin F_2$
👉 **Đáp án: A**
- **Giải thích:** Phép hội ($\cup$) chỉ cần ít nhất một trong hai máy chấp nhận.

#### Câu 46: Một ngôn ngữ hữu hạn (chỉ chứa một số hữu hạn các từ) thì:
- A. Luôn luôn đoán nhận được bởi DFA
- B. Không thể đoán nhận bởi DFA
- C. Đòi hỏi DFA vô hạn trạng thái
- D. Là ngôn ngữ phi ngữ cảnh
👉 **Đáp án: A**

#### Câu 47: Cho DFA có $\Sigma = \{0, 1\}$. Nếu tại trạng thái $q$, ta không vẽ mũi tên cho ký hiệu `0`, điều này ngầm hiểu là:
- A. DFA này bị sai định nghĩa
- B. Tồn tại một trạng thái bẫy ngầm và mũi tên cho `0` đi tới trạng thái bẫy đó
- C. Chuỗi có số 0 không được phép nhập vào
- D. Máy sẽ dừng và chấp nhận
👉 **Đáp án: B**

#### Câu 48: Số lượng cung đi ra từ một trạng thái trong $\varepsilon$-NFA có bảng chữ cái $\Sigma = \{a, b\}$ là:
- A. Đúng 2 cung
- B. Tối đa 3 cung
- C. Tùy ý (có thể 0 cung, hoặc nhiều cung mang nhãn $a, b, \varepsilon$)
- D. Luôn luôn có cung $\varepsilon$
👉 **Đáp án: C**

#### Câu 49: Nếu một DFA có $n$ trạng thái và đoán nhận một chuỗi có độ dài $|w| \ge n$, thì theo nguyên lý Dirichlet (Pigeonhole Principle):
- A. Chuỗi $w$ chứa từ rỗng
- B. Trong quá trình đọc $w$, máy bắt buộc phải lặp lại ít nhất một trạng thái (tạo thành chu trình / loop)
- C. Máy bị treo vô tận
- D. Ngôn ngữ của máy là hữu hạn
👉 **Đáp án: B**
- **Giải thích:** Đọc chuỗi độ dài $\ge n$ thì máy đi qua ít nhất $n+1$ lượt trạng thái. Vì máy chỉ có $n$ trạng thái khác nhau nên chắc chắn có ít nhất 1 trạng thái bị lặp lại. Đây chính là nền tảng của **Bổ đề bơm**.

#### Câu 50: Ô-tô-mát hữu hạn được ứng dụng phổ biến nhất trong giai đoạn nào của trình biên dịch (Compiler)?
- A. Phân tích cú pháp (Syntax Analysis)
- B. Phân tích từ vựng (Lexical Analysis / Scanner)
- C. Tối ưu hóa mã nguồn
- D. Sinh mã đích
👉 **Đáp án: B**
- **Giải thích:** Giai đoạn phân tích từ vựng (nhận diện các Token, từ khóa, định danh, số thực) sử dụng biểu thức chính quy và DFA.
