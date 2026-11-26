# BỘ ĐỀ AUTOMATA PHẦN 2: HÌNH 6 ĐẾN HÌNH 10 (120 CÂU CHUẨN ĐỀ MẪU SAMPLE 2)
## ĐÚNG THỨ TỰ TRONG ONTAPAUTOMATA.DOCX - MỖI HÌNH FULL 24 CÂU + BẢNG SUBSET & TỐI GIẢN

> Bao gồm: **Hình 6** (`image_8.png`), **Hình 7** (`image_4.jpg`), **Hình 8** (`image_1.jpg`), **Hình 9** (`image_13.png`), **Hình 10** (`image_9.png`).

---

## HÌNH 6 (`image_8.png`): NFA CÓ HAI TRẠNG THÁI BẮT ĐẦU $\{q_0, q_1\}$

> **THÔNG TIN ĐỀ BÀI GỐC (Hình 6 trong OnTapAutomata.docx - ảnh `image_8.png`):**
> - Tập trạng thái: $Q = \{q0, q1, q2, q3\}$
> - Bảng chữ cái: $\Sigma = \{0, 1\}$
> - Trạng thái bắt đầu: $q0$, $q1$
> - Trạng thái kết thúc: $F = \{q3\}$
> - Tính chất ban đầu: **Không đơn định (NFA có nhiều trạng thái bắt đầu)**
> - Biểu thức chính quy tương đương: **$1 + 1^* 0 (1^* 0 + 1^+)$**
> - Ngôn ngữ đoán nhận: Hoặc chuỗi `1` (từ điểm đầu $q_1 \xrightarrow{1} q_3$), hoặc sau cụm $1^* 0$ đầu tiên là $1^* 0$ hay $1^+$ (ví dụ `00`, `01`, `100`, `0110`, `1011`).

```text
      1            (bắt đầu nữa!)
    ┌───┐               │
    │   ▼               ▼
───► ( q0 ) ─── 0 ──► ( q1 ) ───── 1 ─────► ((( q3 )))
       │                ▲                      ▲
       │ 0              │ 1                    │ 0
       ▼                │                      │
     ( q2 ) ────────────┴──────────────────────┘
      │ ▲
      └─┘ 1
```

### Quy tắc vàng nhận diện trong 3 giây
1. **QUY TẮC 1:** Có **2 điểm xuất phát là $q_0$ và $q_1$**, nên chuỗi **`1`** đi thẳng từ $q_1 \xrightarrow{1} q_3$ ĐƯỢC NHẬN ngay!
2. **QUY TẮC 2:** Không nhận $\varepsilon$, không nhận `0`, không nhận `10` hay `11` (vì sau chữ `0` đầu tiên cần thêm ít nhất 1 ký tự; sau chữ `0` thứ hai nếu đã tới $q_3$ thì không đi tiếp được nữa!).

### Bộ 24 câu trắc nghiệm chuẩn Đề Mẫu Sample 2

**Câu 1.** Xét các chuỗi: $s_1 = \text{"1"}$, $s_2 = \text{"0"}$, $s_3 = \text{"10"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Tất cả các chuỗi được nêu.
👉 **Đáp án đúng: A**
- **Giải thích:** `1` hợp lệ ($S_0$ $\xrightarrow{1}$ $S_2$ (NHẬN)). Còn `0` và `10` không về được trạng thái kết thúc.

**Câu 2.** Xét các chuỗi: $s_1 = \text{"11"}$, $s_2 = \text{"000"}$, $s_3 = \text{"00"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Các chọn lựa khác đều ĐÚNG.
👉 **Đáp án đúng: C**
- **Giải thích:** Chỉ có $s_3 =$ `00` hợp lệ ($S_0$ $\xrightarrow{0}$ $S_1$ $\xrightarrow{0}$ $S_3$ (NHẬN)). Hai chuỗi $s_1, s_2$ bị từ chối.

**Câu 3.** Xét các chuỗi: $s_1 = \text{"01"}$, $s_2 = \text{"010"}$, $s_3 = \text{"011"}$, $s_4 = \text{"001"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1, s_2$ và $s_3$
- B. $s_2, s_3$ và $s_4$
- C. $s_3$ và $s_4$
- D. $s_4$
👉 **Đáp án đúng: A**
- **Giải thích:** $s_4 =$ `001` bị từ chối ($S_0$ $\xrightarrow{0}$ $S_1$ $\xrightarrow{0}$ $S_3$ $\xrightarrow{1}$ $S_6$ (TỪ CHỐI)). Ba chuỗi còn lại đều hợp lệ.

**Câu 4.** Xét các chuỗi: $s_1 = \text{"100"}$, $s_2 = \text{"110"}$, $s_3 = \text{"101"}$, $s_4 = \text{"111"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_4$
- C. $s_1$ và $s_3$
- D. $s_1$ và $s_4$
👉 **Đáp án đúng: C**
- **Giải thích:** $s_1 =$ `100` và $s_3 =$ `101` hợp lệ; còn $s_2 =$ `110` và $s_4 =$ `111` không hợp lệ.

**Câu 5.** Xét các chuỗi: $s_1 = \text{"11111"}$, $s_2 = \text{"11101"}$, $s_3 = \text{"11110"}$, $s_4 = \text{"11100"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_4$
- C. $s_2$ và $s_3$
- D. $s_1$ và $s_4$
👉 **Đáp án đúng: B**
- **Giải thích:** $s_2 =$ `11101` và $s_4 =$ `11100` đạt trạng thái kết thúc; $s_1, s_3$ bị từ chối.

**Câu 6.** Xét các chuỗi: $s_1 = \text{"01"}$, $s_2 = \text{"010"}$, $s_3 = \text{"011"}$, $s_4 = \text{"001"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Chỉ duy nhất $s_4 =$ `001` bị từ chối ($S_0$ $\xrightarrow{0}$ $S_1$ $\xrightarrow{0}$ $S_3$ $\xrightarrow{1}$ $S_6$ (TỪ CHỐI)).

**Câu 7.** Xét các chuỗi: $s_1 = \text{"1"}$, $s_2 = \text{"0"}$, $s_3 = \text{"00"}$, $s_4 = \text{"10"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_2$
- B. $s_1$
- C. $s_3$
- D. Tất cả các chuỗi đều không hợp lệ.
👉 **Đáp án đúng: A**
- **Giải thích:** $s_1, s_3$ đều hợp lệ nên loại B, C, D. Chuỗi $s_2 =$ `0` không hợp lệ ($S_0$ $\xrightarrow{0}$ $S_1$ (TỪ CHỐI)). *(Lưu ý tương tự Câu 7 Sample 2: $s_4$ cũng không hợp lệ nhưng chỉ có $s_2$ xuất hiện trong 4 lựa chọn nên A là đáp án duy nhất)*.

**Câu 8.** Xét các chuỗi: $s_1 = \text{"100"}$, $s_2 = \text{"101"}$, $s_3 = \text{"11101"}$, $s_4 = \text{"110"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_3$
- C. $s_3$ và $s_4$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Duy nhất $s_4 =$ `110` bị từ chối ($S_0$ $\xrightarrow{1}$ $S_2$ $\xrightarrow{1}$ $S_5$ $\xrightarrow{0}$ $S_1$ (TỪ CHỐI)).

**Câu 9.** Xét các chuỗi: $s_1 = \text{"100"}$, $s_2 = \text{"101"}$, $s_3 = \text{"11101"}$, $s_4 = \text{"110"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cả $s_1, s_2, s_3$ đều là chuỗi hợp lệ; chuỗi duy nhất không hợp lệ là $s_4 =$ `110` không nằm trong A, B, C $\implies$ Chọn D.

**Câu 10.** Xét các chuỗi: $s_1 = \text{"100"}$, $s_2 = \text{"110"}$, $s_3 = \text{"101"}$, $s_4 = \text{"111"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$ và $s_4$
- B. $s_2$ và $s_3$
- C. $s_3$ và $s_4$
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cặp không hợp lệ đúng phải là $s_2$ và $s_4$ (`110` và `111`), không có trong A, B, C $\implies$ Chọn D.

**Câu 11.** Xét các chuỗi: $s_1 = \text{"11111"}$, $s_2 = \text{"11101"}$, $s_3 = \text{"11110"}$, $s_4 = \text{"11100"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1, s_2$ và $s_3$
- B. $s_1$ và $s_3$
- C. $s_4$
- D. $s_3$ và $s_4$
👉 **Đáp án đúng: B**
- **Giải thích:** $s_1 =$ `11111` và $s_3 =$ `11110` đều không đạt trạng thái kết thúc.

**Câu 12.** Xét các chuỗi: $s_1 = \text{"01"}$, $s_2 = \text{"010"}$, $s_3 = \text{"011"}$, $s_4 = \text{"ε"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Chuỗi rỗng $s_4 = \varepsilon$ KHÔNG được nhận vì tập trạng thái khởi đầu (sau bao đóng $\varepsilon$) không chứa trạng thái kết thúc.

**Câu 13.** Xét biểu thức chính quy $E_1 = (0+1)^+$ (mọi chuỗi nhị phân khác rỗng). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc ngôn ngữ mô tả bởi $E_1$**?
- A. `1`
- B. `00`
- C. `0`
- D. `01`
👉 **Đáp án đúng: C**
- **Giải thích:** `0` thỏa $E_1$ nhưng bị Automaton từ chối ($S_0$ $\xrightarrow{0}$ $S_1$ (TỪ CHỐI)). Ba chuỗi còn lại đều thuộc $L$.

**Câu 14.** Xét biểu thức $E_1 = (0+1)^+$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc ngôn ngữ mô tả bởi $E_1$**?
- A. Không có chuỗi nào
- B. `01`
- C. `001`
- D. `0`
👉 **Đáp án đúng: A**
- **Giải thích:** Mọi chuỗi hợp lệ của Automaton đều thỏa $E_1$ ($L \subseteq L(E_1)$), nên **không có chuỗi nào** thuộc $L$ mà lại ngoài $L(E_1)$!

**Câu 15.** Xét biểu thức $E_2 = 1^* 0 1^+$ (dạng $1^* 0 1^+$ (thiếu nhánh kết thúc bằng `0`)). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_2)$**?
- A. `01`
- B. `011`
- C. `101`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Do $L(E_2) \subseteq L$ (và cả 3 chuỗi A, B, C đều thuộc $L$), nên không có chuỗi nào trong A, B, C thỏa điều kiện $\implies$ Chọn D.

**Câu 16.** Xét biểu thức $E_2 = 1^* 0 1^+$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_2)$**?
- A. `01`
- B. `1`
- C. `011`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `1` thuộc $L$ ($S_0$ $\xrightarrow{1}$ $S_2$ (NHẬN)) nhưng không khớp khuôn mẫu của $E_2$. Còn `01` và `011` đều thuộc cả $L$ lẫn $E_2$.

**Câu 17.** Xét biểu thức $E_2 = 1^* 0 1^+$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_2)$**?
- A. `01`
- B. `011`
- C. `101`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cả 3 chuỗi `01`, `011`, `101` đều đồng thời thuộc cả $L$ lẫn $E_2$ $\implies$ Chọn D (y hệt bẫy Câu 17 Sample 2!).

**Câu 18.** Xét biểu thức $E_3 = (0+1)^* 0$ (chuỗi kết thúc bằng `0`). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_3)$**?
- A. `1`
- B. `0`
- C. `00`
- D. `01`
👉 **Đáp án đúng: B**
- **Giải thích:** `0` thuộc $E_3$ nhưng không được Automaton chấp nhận ($S_0$ $\xrightarrow{0}$ $S_1$ (TỪ CHỐI)). Các chuỗi kia đều thuộc $L$.

**Câu 19.** Xét biểu thức $E_3 = (0+1)^* 0$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_3)$**?
- A. `00`
- B. `1`
- C. `010`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `1` thuộc $L$ ($S_0$ $\xrightarrow{1}$ $S_2$ (NHẬN)) nhưng nằm ngoài $E_3$. Hai chuỗi còn lại thuộc cả $L$ và $E_3$.

**Câu 20.** Xét biểu thức $E_3 = (0+1)^* 0$. Chuỗi nào **ĐỒNG THỜI KHÔNG** thuộc $L$ và **KHÔNG** thuộc $L(E_3)$?
- A. `1`
- B. `11`
- C. `0`
- D. `00`
👉 **Đáp án đúng: B**
- **Giải thích:** `11` vừa không được Automaton chấp nhận vừa không thuộc $E_3$. Các chuỗi kia đều thuộc $L$ hoặc $E_3$ (hoặc cả hai).

**Câu 21.** Xét biểu thức $E_4 = (0+1)^* 00$ (chuỗi kết thúc bằng đuôi `00`). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_4)$**?
- A. `1`
- B. `00`
- C. `000`
- D. `01`
👉 **Đáp án đúng: C**
- **Giải thích:** `000` thuộc $L(E_4)$ nhưng bị Automaton từ chối ($S_0$ $\xrightarrow{0}$ $S_1$ $\xrightarrow{0}$ $S_3$ $\xrightarrow{0}$ $S_6$ (TỪ CHỐI)). Ba chuỗi còn lại đều thuộc $L$.

**Câu 22.** Xét biểu thức $E_4 = (0+1)^* 00$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_4)$**?
- A. `00`
- B. `1`
- C. `100`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `1` thuộc $L$ ($S_0$ $\xrightarrow{1}$ $S_2$ (NHẬN)) nhưng không khớp khuôn mẫu $E_4$.

**Câu 23.** Nếu áp dụng đơn định hóa Automaton đang quan tâm thì DFA đầy đủ thu được có bao nhiêu trạng thái?
- A. 6
- B. 7
- C. 8
- D. 9
👉 **Đáp án đúng: B**
- **Giải thích:** Áp dụng thuật toán xây dựng tập con (Subset Construction) thu được **7 trạng thái** (xem bảng bên dưới): *(Lưu ý: Sơ đồ có xuất hiện tập con rỗng $\emptyset$ làm trạng thái bẫy chết. Nếu một số đề không vẽ trạng thái bẫy này thì còn **6 trạng thái**; theo chuẩn hàm chuyển toàn phần trong Sample 2 của IUH thì tính đủ **7 trạng thái**).*

| Trạng thái DFA | Tập con NFA | Đọc `0` | Đọc `1` | Kết thúc? |
| :---: | :---: | :---: | :---: | :---: |
| $S_0$ (Đầu) | $\{q0, q1\}$ | $S_1$ | $S_2$ | Không |
| $S_1$ | $\{q1, q2\}$ | $S_3$ | $S_4$ | Không |
| $S_2$ | $\{q0, q3\}$ | $S_1$ | $S_5$ | **CÓ** |
| $S_3$ | $\{q3\}$ | $S_6$ | $S_6$ | **CÓ** |
| $S_4$ | $\{q1, q2, q3\}$ | $S_3$ | $S_4$ | **CÓ** |
| $S_5$ | $\{q0\}$ | $S_1$ | $S_5$ | Không |
| $S_6$ (Bẫy) | $\emptyset$ | $S_6$ | $S_6$ | Không |

**Câu 24.** DFA tối giản tương đương có bao nhiêu trạng thái?
- A. 6
- B. 7
- C. 8
- D. 9
👉 **Đáp án đúng: B**
- **Giải thích:** DFA thu được **đã tối giản** (**7 trạng thái**). Phân hoạch các nhóm trạng thái tương đương cuối cùng gồm **7 nhóm**: `{$S_2$}`, `{$S_3$}`, `{$S_4$}`, `{$S_6$}`, `{$S_5$}`, `{$S_0$}`, `{$S_1$}`. *(Nếu bỏ trạng thái bẫy chết khỏi đồ thị thì còn **6 trạng thái**; tính đủ hàm toàn phần như Sample 2 là **7 trạng thái**).*

---

## HÌNH 7 (`image_4.jpg`): PARTIAL DFA $(01 + 001)^* 00$

> **THÔNG TIN ĐỀ BÀI GỐC (Hình 7 trong OnTapAutomata.docx - ảnh `image_4.jpg`):**
> - Tập trạng thái: $Q = \{q0, q1, q2\}$
> - Bảng chữ cái: $\Sigma = \{0, 1\}$
> - Trạng thái bắt đầu: $q0$
> - Trạng thái kết thúc: $F = \{q2\}$
> - Tính chất ban đầu: **Đơn định thiếu cung (Partial DFA - cần thêm trạng thái bẫy $\emptyset$ để thành DFA đầy đủ)**
> - Biểu thức chính quy tương đương: **$(01 + 001)^* 00$**
> - Ngôn ngữ đoán nhận: Chuỗi ghép bởi các khối `01` hoặc `001`, kết thúc bắt buộc bằng **`00`**. *(Bẫy: Không có đường đọc `1` tại $q_0$ và không có đường đọc `0` tại $q_2$ nên không chứa `000` và không chứa `11`!)*

```text
              0             0
───► ( q0 ) ─────► ( q1 ) ─────► ((( q2 )))
       ▲  ▲          │               │
       │  └──── 1 ───┘               │
       └────────────── 1 ────────────┘
```

### Quy tắc vàng nhận diện trong 3 giây
1. **QUY TẮC 1:** Phải mở đầu bằng `0` (từ $q_0$ không đọc được `1`) và kết thúc bằng **`00`**.
2. **QUY TẮC 2:** Tuyệt đối KHÔNG chứa **`000`** (vì tại $q_2$ không có cạnh `0`) và KHÔNG chứa **`11`** (vì tại $q_0$ không có cạnh `1`)!

### Bộ 24 câu trắc nghiệm chuẩn Đề Mẫu Sample 2

**Câu 1.** Xét các chuỗi: $s_1 = \text{"00"}$, $s_2 = \text{"0"}$, $s_3 = \text{"1"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Tất cả các chuỗi được nêu.
👉 **Đáp án đúng: A**
- **Giải thích:** `00` hợp lệ ($S_0$ $\xrightarrow{0}$ $S_1$ $\xrightarrow{0}$ $S_3$ (NHẬN)). Còn `0` và `1` không về được trạng thái kết thúc.

**Câu 2.** Xét các chuỗi: $s_1 = \text{"01"}$, $s_2 = \text{"10"}$, $s_3 = \text{"0100"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Các chọn lựa khác đều ĐÚNG.
👉 **Đáp án đúng: C**
- **Giải thích:** Chỉ có $s_3 =$ `0100` hợp lệ ($S_0$ $\xrightarrow{0}$ $S_1$ $\xrightarrow{1}$ $S_0$ $\xrightarrow{0}$ $S_1$ $\xrightarrow{0}$ $S_3$ (NHẬN)). Hai chuỗi $s_1, s_2$ bị từ chối.

**Câu 3.** Xét các chuỗi: $s_1 = \text{"00100"}$, $s_2 = \text{"010100"}$, $s_3 = \text{"0010100"}$, $s_4 = \text{"11"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1, s_2$ và $s_3$
- B. $s_2, s_3$ và $s_4$
- C. $s_3$ và $s_4$
- D. $s_4$
👉 **Đáp án đúng: A**
- **Giải thích:** $s_4 =$ `11` bị từ chối ($S_0$ $\xrightarrow{1}$ $S_2$ $\xrightarrow{1}$ $S_2$ (TỪ CHỐI)). Ba chuỗi còn lại đều hợp lệ.

**Câu 4.** Xét các chuỗi: $s_1 = \text{"0100100"}$, $s_2 = \text{"000"}$, $s_3 = \text{"00100100"}$, $s_4 = \text{"001"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_4$
- C. $s_1$ và $s_3$
- D. $s_1$ và $s_4$
👉 **Đáp án đúng: C**
- **Giải thích:** $s_1 =$ `0100100` và $s_3 =$ `00100100` hợp lệ; còn $s_2 =$ `000` và $s_4 =$ `001` không hợp lệ.

**Câu 5.** Xét các chuỗi: $s_1 = \text{"11111111"}$, $s_2 = \text{"01010100"}$, $s_3 = \text{"11111110"}$, $s_4 = \text{"00"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_4$
- C. $s_2$ và $s_3$
- D. $s_1$ và $s_4$
👉 **Đáp án đúng: B**
- **Giải thích:** $s_2 =$ `01010100` và $s_4 =$ `00` đạt trạng thái kết thúc; $s_1, s_3$ bị từ chối.

**Câu 6.** Xét các chuỗi: $s_1 = \text{"00100"}$, $s_2 = \text{"010100"}$, $s_3 = \text{"0010100"}$, $s_4 = \text{"11"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Chỉ duy nhất $s_4 =$ `11` bị từ chối ($S_0$ $\xrightarrow{1}$ $S_2$ $\xrightarrow{1}$ $S_2$ (TỪ CHỐI)).

**Câu 7.** Xét các chuỗi: $s_1 = \text{"00"}$, $s_2 = \text{"0"}$, $s_3 = \text{"0100"}$, $s_4 = \text{"1"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_2$
- B. $s_1$
- C. $s_3$
- D. Tất cả các chuỗi đều không hợp lệ.
👉 **Đáp án đúng: A**
- **Giải thích:** $s_1, s_3$ đều hợp lệ nên loại B, C, D. Chuỗi $s_2 =$ `0` không hợp lệ ($S_0$ $\xrightarrow{0}$ $S_1$ (TỪ CHỐI)). *(Lưu ý tương tự Câu 7 Sample 2: $s_4$ cũng không hợp lệ nhưng chỉ có $s_2$ xuất hiện trong 4 lựa chọn nên A là đáp án duy nhất)*.

**Câu 8.** Xét các chuỗi: $s_1 = \text{"0100100"}$, $s_2 = \text{"00100100"}$, $s_3 = \text{"01010100"}$, $s_4 = \text{"000"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_3$
- C. $s_3$ và $s_4$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Duy nhất $s_4 =$ `000` bị từ chối ($S_0$ $\xrightarrow{0}$ $S_1$ $\xrightarrow{0}$ $S_3$ $\xrightarrow{0}$ $S_2$ (TỪ CHỐI)).

**Câu 9.** Xét các chuỗi: $s_1 = \text{"0100100"}$, $s_2 = \text{"00100100"}$, $s_3 = \text{"01010100"}$, $s_4 = \text{"000"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cả $s_1, s_2, s_3$ đều là chuỗi hợp lệ; chuỗi duy nhất không hợp lệ là $s_4 =$ `000` không nằm trong A, B, C $\implies$ Chọn D.

**Câu 10.** Xét các chuỗi: $s_1 = \text{"0100100"}$, $s_2 = \text{"000"}$, $s_3 = \text{"00100100"}$, $s_4 = \text{"001"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$ và $s_4$
- B. $s_2$ và $s_3$
- C. $s_3$ và $s_4$
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cặp không hợp lệ đúng phải là $s_2$ và $s_4$ (`000` và `001`), không có trong A, B, C $\implies$ Chọn D.

**Câu 11.** Xét các chuỗi: $s_1 = \text{"11111111"}$, $s_2 = \text{"01010100"}$, $s_3 = \text{"11111110"}$, $s_4 = \text{"00"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1, s_2$ và $s_3$
- B. $s_1$ và $s_3$
- C. $s_4$
- D. $s_3$ và $s_4$
👉 **Đáp án đúng: B**
- **Giải thích:** $s_1 =$ `11111111` và $s_3 =$ `11111110` đều không đạt trạng thái kết thúc.

**Câu 12.** Xét các chuỗi: $s_1 = \text{"00100"}$, $s_2 = \text{"010100"}$, $s_3 = \text{"0010100"}$, $s_4 = \text{"ε"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Chuỗi rỗng $s_4 = \varepsilon$ KHÔNG được nhận vì tập trạng thái khởi đầu (sau bao đóng $\varepsilon$) không chứa trạng thái kết thúc.

**Câu 13.** Xét biểu thức chính quy $E_1 = (0+1)^* 00$ (mọi chuỗi kết thúc bằng `00`). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc ngôn ngữ mô tả bởi $E_1$**?
- A. `00`
- B. `0100`
- C. `000`
- D. `00100`
👉 **Đáp án đúng: C**
- **Giải thích:** `000` thỏa $E_1$ nhưng bị Automaton từ chối ($S_0$ $\xrightarrow{0}$ $S_1$ $\xrightarrow{0}$ $S_3$ $\xrightarrow{0}$ $S_2$ (TỪ CHỐI)). Ba chuỗi còn lại đều thuộc $L$.

**Câu 14.** Xét biểu thức $E_1 = (0+1)^* 00$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc ngôn ngữ mô tả bởi $E_1$**?
- A. Không có chuỗi nào
- B. `00100`
- C. `11`
- D. `000`
👉 **Đáp án đúng: A**
- **Giải thích:** Mọi chuỗi hợp lệ của Automaton đều thỏa $E_1$ ($L \subseteq L(E_1)$), nên **không có chuỗi nào** thuộc $L$ mà lại ngoài $L(E_1)$!

**Câu 15.** Xét biểu thức $E_2 = (01)^* 00$ (lặp `01` rồi kết thúc bằng `00`). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_2)$**?
- A. `00`
- B. `0100`
- C. `010100`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Do $L(E_2) \subseteq L$ (và cả 3 chuỗi A, B, C đều thuộc $L$), nên không có chuỗi nào trong A, B, C thỏa điều kiện $\implies$ Chọn D.

**Câu 16.** Xét biểu thức $E_2 = (01)^* 00$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_2)$**?
- A. `00`
- B. `00100`
- C. `0100`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `00100` thuộc $L$ ($S_0$ $\xrightarrow{0}$ $S_1$ $\xrightarrow{0}$ $S_3$ $\xrightarrow{1}$ $S_0$ $\xrightarrow{0}$ $S_1$ $\xrightarrow{0}$ $S_3$ (NHẬN)) nhưng không khớp khuôn mẫu của $E_2$. Còn `00` và `0100` đều thuộc cả $L$ lẫn $E_2$.

**Câu 17.** Xét biểu thức $E_2 = (01)^* 00$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_2)$**?
- A. `00`
- B. `0100`
- C. `010100`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cả 3 chuỗi `00`, `0100`, `010100` đều đồng thời thuộc cả $L$ lẫn $E_2$ $\implies$ Chọn D (y hệt bẫy Câu 17 Sample 2!).

**Câu 18.** Xét biểu thức $E_3 = (01)^+ (0+1)^*$ (bắt đầu bằng `01` theo sau bất kỳ). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_3)$**?
- A. `00`
- B. `01`
- C. `0100`
- D. `00100`
👉 **Đáp án đúng: B**
- **Giải thích:** `01` thuộc $E_3$ nhưng không được Automaton chấp nhận ($S_0$ $\xrightarrow{0}$ $S_1$ $\xrightarrow{1}$ $S_0$ (TỪ CHỐI)). Các chuỗi kia đều thuộc $L$.

**Câu 19.** Xét biểu thức $E_3 = (01)^+ (0+1)^*$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_3)$**?
- A. `0100`
- B. `00`
- C. `010100`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `00` thuộc $L$ ($S_0$ $\xrightarrow{0}$ $S_1$ $\xrightarrow{0}$ $S_3$ (NHẬN)) nhưng nằm ngoài $E_3$. Hai chuỗi còn lại thuộc cả $L$ và $E_3$.

**Câu 20.** Xét biểu thức $E_3 = (01)^+ (0+1)^*$. Chuỗi nào **ĐỒNG THỜI KHÔNG** thuộc $L$ và **KHÔNG** thuộc $L(E_3)$?
- A. `00`
- B. `0`
- C. `01`
- D. `0100`
👉 **Đáp án đúng: B**
- **Giải thích:** `0` vừa không được Automaton chấp nhận vừa không thuộc $E_3$. Các chuỗi kia đều thuộc $L$ hoặc $E_3$ (hoặc cả hai).

**Câu 21.** Xét biểu thức $E_4 = 0^+ 0$ (chuỗi chỉ gồm toàn ký tự `0` có độ dài $\ge 2$). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_4)$**?
- A. `00`
- B. `0100`
- C. `000`
- D. `00100`
👉 **Đáp án đúng: C**
- **Giải thích:** `000` thuộc $L(E_4)$ nhưng bị Automaton từ chối ($S_0$ $\xrightarrow{0}$ $S_1$ $\xrightarrow{0}$ $S_3$ $\xrightarrow{0}$ $S_2$ (TỪ CHỐI)). Ba chuỗi còn lại đều thuộc $L$.

**Câu 22.** Xét biểu thức $E_4 = 0^+ 0$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_4)$**?
- A. `00`
- B. `0100`
- C. $\varepsilon$
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `0100` thuộc $L$ ($S_0$ $\xrightarrow{0}$ $S_1$ $\xrightarrow{1}$ $S_0$ $\xrightarrow{0}$ $S_1$ $\xrightarrow{0}$ $S_3$ (NHẬN)) nhưng không khớp khuôn mẫu $E_4$.

**Câu 23.** Nếu áp dụng đơn định hóa Automaton đang quan tâm thì DFA đầy đủ thu được có bao nhiêu trạng thái?
- A. 3
- B. 4
- C. 5
- D. 6
👉 **Đáp án đúng: B**
- **Giải thích:** Áp dụng thuật toán xây dựng tập con (Subset Construction) thu được **4 trạng thái** (xem bảng bên dưới): *(Lưu ý: Sơ đồ có xuất hiện tập con rỗng $\emptyset$ làm trạng thái bẫy chết. Nếu một số đề không vẽ trạng thái bẫy này thì còn **3 trạng thái**; theo chuẩn hàm chuyển toàn phần trong Sample 2 của IUH thì tính đủ **4 trạng thái**).*

| Trạng thái DFA | Tập con NFA | Đọc `0` | Đọc `1` | Kết thúc? |
| :---: | :---: | :---: | :---: | :---: |
| $S_0$ (Đầu) | $\{q0\}$ | $S_1$ | $S_2$ | Không |
| $S_1$ | $\{q1\}$ | $S_3$ | $S_0$ | Không |
| $S_2$ (Bẫy) | $\emptyset$ | $S_2$ | $S_2$ | Không |
| $S_3$ | $\{q2\}$ | $S_2$ | $S_0$ | **CÓ** |

**Câu 24.** DFA tối giản tương đương có bao nhiêu trạng thái?
- A. 3
- B. 4
- C. 5
- D. 6
👉 **Đáp án đúng: B**
- **Giải thích:** DFA thu được **đã tối giản** (**4 trạng thái**). Phân hoạch các nhóm trạng thái tương đương cuối cùng gồm **4 nhóm**: `{$S_3$}`, `{$S_2$}`, `{$S_0$}`, `{$S_1$}`. *(Nếu bỏ trạng thái bẫy chết khỏi đồ thị thì còn **3 trạng thái**; tính đủ hàm toàn phần như Sample 2 là **4 trạng thái**).*

---

## HÌNH 8 (`image_1.jpg`): NFA BA KÝ TỰ $\{0, 1, 2\}$ ($0(1^+ + 21)$)

> **THÔNG TIN ĐỀ BÀI GỐC (Hình 8 trong OnTapAutomata.docx - ảnh `image_1.jpg`):**
> - Tập trạng thái: $Q = \{q0, q1, q2, q3, q4\}$
> - Bảng chữ cái: $\Sigma = \{0, 1, 2\}$
> - Trạng thái bắt đầu: $q0$
> - Trạng thái kết thúc: $F = \{q2\}$
> - Tính chất ban đầu: **Không đơn định (NFA)**
> - Biểu thức chính quy tương đương: **$0(1^+ + 21)$**
> - Ngôn ngữ đoán nhận: Bắt đầu bằng đúng một chữ `0`, tiếp theo là một hay nhiều chữ `1` (`01, 011, 0111, ...`), HOẶC chuỗi duy nhất `021`.

```text
              1       1 (vòng)
    ((( q2 ))) ◄──── ( q1 ) ◄────┐ 0
        ▲                         ( q0 ) ◄───
        │ 1          2            │ 0
     ( q4 ) ◄──────────── ( q3 ) ◄┘
```

### Quy tắc vàng nhận diện trong 3 giây
1. **QUY TẮC 1:** Bắt buộc mở đầu bằng **đúng 1 chữ `0`** và kết thúc bằng **`1`**.
2. **QUY TẮC 2:** Chỉ có 2 dạng hợp lệ: **`01, 011, 0111, ...`** ($01^+$) hoặc đúng chuỗi **`021`**!

### Bộ 24 câu trắc nghiệm chuẩn Đề Mẫu Sample 2

**Câu 1.** Xét các chuỗi: $s_1 = \text{"01"}$, $s_2 = \text{"0"}$, $s_3 = \text{"1"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Tất cả các chuỗi được nêu.
👉 **Đáp án đúng: A**
- **Giải thích:** `01` hợp lệ ($S_0$ $\xrightarrow{0}$ $S_1$ $\xrightarrow{1}$ $S_3$ (NHẬN)). Còn `0` và `1` không về được trạng thái kết thúc.

**Câu 2.** Xét các chuỗi: $s_1 = \text{"2"}$, $s_2 = \text{"00"}$, $s_3 = \text{"011"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Các chọn lựa khác đều ĐÚNG.
👉 **Đáp án đúng: C**
- **Giải thích:** Chỉ có $s_3 =$ `011` hợp lệ ($S_0$ $\xrightarrow{0}$ $S_1$ $\xrightarrow{1}$ $S_3$ $\xrightarrow{1}$ $S_3$ (NHẬN)). Hai chuỗi $s_1, s_2$ bị từ chối.

**Câu 3.** Xét các chuỗi: $s_1 = \text{"021"}$, $s_2 = \text{"0111"}$, $s_3 = \text{"01111"}$, $s_4 = \text{"02"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1, s_2$ và $s_3$
- B. $s_2, s_3$ và $s_4$
- C. $s_3$ và $s_4$
- D. $s_4$
👉 **Đáp án đúng: A**
- **Giải thích:** $s_4 =$ `02` bị từ chối ($S_0$ $\xrightarrow{0}$ $S_1$ $\xrightarrow{2}$ $S_4$ (TỪ CHỐI)). Ba chuỗi còn lại đều hợp lệ.

**Câu 4.** Xét các chuỗi: $s_1 = \text{"01"}$, $s_2 = \text{"10"}$, $s_3 = \text{"011"}$, $s_4 = \text{"11"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_4$
- C. $s_1$ và $s_3$
- D. $s_1$ và $s_4$
👉 **Đáp án đúng: C**
- **Giải thích:** $s_1 =$ `01` và $s_3 =$ `011` hợp lệ; còn $s_2 =$ `10` và $s_4 =$ `11` không hợp lệ.

**Câu 5.** Xét các chuỗi: $s_1 = \text{"22222"}$, $s_2 = \text{"01"}$, $s_3 = \text{"22221"}$, $s_4 = \text{"011"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_4$
- C. $s_2$ và $s_3$
- D. $s_1$ và $s_4$
👉 **Đáp án đúng: B**
- **Giải thích:** $s_2 =$ `01` và $s_4 =$ `011` đạt trạng thái kết thúc; $s_1, s_3$ bị từ chối.

**Câu 6.** Xét các chuỗi: $s_1 = \text{"021"}$, $s_2 = \text{"0111"}$, $s_3 = \text{"01111"}$, $s_4 = \text{"02"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Chỉ duy nhất $s_4 =$ `02` bị từ chối ($S_0$ $\xrightarrow{0}$ $S_1$ $\xrightarrow{2}$ $S_4$ (TỪ CHỐI)).

**Câu 7.** Xét các chuỗi: $s_1 = \text{"01"}$, $s_2 = \text{"0"}$, $s_3 = \text{"011"}$, $s_4 = \text{"1"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_2$
- B. $s_1$
- C. $s_3$
- D. Tất cả các chuỗi đều không hợp lệ.
👉 **Đáp án đúng: A**
- **Giải thích:** $s_1, s_3$ đều hợp lệ nên loại B, C, D. Chuỗi $s_2 =$ `0` không hợp lệ ($S_0$ $\xrightarrow{0}$ $S_1$ (TỪ CHỐI)). *(Lưu ý tương tự Câu 7 Sample 2: $s_4$ cũng không hợp lệ nhưng chỉ có $s_2$ xuất hiện trong 4 lựa chọn nên A là đáp án duy nhất)*.

**Câu 8.** Xét các chuỗi: $s_1 = \text{"01"}$, $s_2 = \text{"011"}$, $s_3 = \text{"021"}$, $s_4 = \text{"10"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_3$
- C. $s_3$ và $s_4$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Duy nhất $s_4 =$ `10` bị từ chối ($S_0$ $\xrightarrow{1}$ $S_2$ $\xrightarrow{0}$ $S_2$ (TỪ CHỐI)).

**Câu 9.** Xét các chuỗi: $s_1 = \text{"01"}$, $s_2 = \text{"011"}$, $s_3 = \text{"021"}$, $s_4 = \text{"10"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cả $s_1, s_2, s_3$ đều là chuỗi hợp lệ; chuỗi duy nhất không hợp lệ là $s_4 =$ `10` không nằm trong A, B, C $\implies$ Chọn D.

**Câu 10.** Xét các chuỗi: $s_1 = \text{"01"}$, $s_2 = \text{"10"}$, $s_3 = \text{"011"}$, $s_4 = \text{"11"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$ và $s_4$
- B. $s_2$ và $s_3$
- C. $s_3$ và $s_4$
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cặp không hợp lệ đúng phải là $s_2$ và $s_4$ (`10` và `11`), không có trong A, B, C $\implies$ Chọn D.

**Câu 11.** Xét các chuỗi: $s_1 = \text{"22222"}$, $s_2 = \text{"01"}$, $s_3 = \text{"22221"}$, $s_4 = \text{"011"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1, s_2$ và $s_3$
- B. $s_1$ và $s_3$
- C. $s_4$
- D. $s_3$ và $s_4$
👉 **Đáp án đúng: B**
- **Giải thích:** $s_1 =$ `22222` và $s_3 =$ `22221` đều không đạt trạng thái kết thúc.

**Câu 12.** Xét các chuỗi: $s_1 = \text{"021"}$, $s_2 = \text{"0111"}$, $s_3 = \text{"01111"}$, $s_4 = \text{"ε"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Chuỗi rỗng $s_4 = \varepsilon$ KHÔNG được nhận vì tập trạng thái khởi đầu (sau bao đóng $\varepsilon$) không chứa trạng thái kết thúc.

**Câu 13.** Xét biểu thức chính quy $E_1 = 0(1+2)^* 1$ (mở đầu bằng `0`, kết thúc bằng `1`, giữa toàn `1, 2`). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc ngôn ngữ mô tả bởi $E_1$**?
- A. `01`
- B. `011`
- C. `0121`
- D. `021`
👉 **Đáp án đúng: C**
- **Giải thích:** `0121` thỏa $E_1$ nhưng bị Automaton từ chối ($S_0$ $\xrightarrow{0}$ $S_1$ $\xrightarrow{1}$ $S_3$ $\xrightarrow{2}$ $S_2$ $\xrightarrow{1}$ $S_2$ (TỪ CHỐI)). Ba chuỗi còn lại đều thuộc $L$.

**Câu 14.** Xét biểu thức $E_1 = 0(1+2)^* 1$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc ngôn ngữ mô tả bởi $E_1$**?
- A. Không có chuỗi nào
- B. `021`
- C. `02`
- D. `0121`
👉 **Đáp án đúng: A**
- **Giải thích:** Mọi chuỗi hợp lệ của Automaton đều thỏa $E_1$ ($L \subseteq L(E_1)$), nên **không có chuỗi nào** thuộc $L$ mà lại ngoài $L(E_1)$!

**Câu 15.** Xét biểu thức $E_2 = 0 1^+$ (dạng `0` rồi dãy `1` (không chứa chữ `2`)). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_2)$**?
- A. `01`
- B. `011`
- C. `0111`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Do $L(E_2) \subseteq L$ (và cả 3 chuỗi A, B, C đều thuộc $L$), nên không có chuỗi nào trong A, B, C thỏa điều kiện $\implies$ Chọn D.

**Câu 16.** Xét biểu thức $E_2 = 0 1^+$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_2)$**?
- A. `01`
- B. `021`
- C. `011`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `021` thuộc $L$ ($S_0$ $\xrightarrow{0}$ $S_1$ $\xrightarrow{2}$ $S_4$ $\xrightarrow{1}$ $S_5$ (NHẬN)) nhưng không khớp khuôn mẫu của $E_2$. Còn `01` và `011` đều thuộc cả $L$ lẫn $E_2$.

**Câu 17.** Xét biểu thức $E_2 = 0 1^+$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_2)$**?
- A. `01`
- B. `011`
- C. `0111`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cả 3 chuỗi `01`, `011`, `0111` đều đồng thời thuộc cả $L$ lẫn $E_2$ $\implies$ Chọn D (y hệt bẫy Câu 17 Sample 2!).

**Câu 18.** Xét biểu thức $E_3 = 0(1+2)1$ (chỉ gồm `011` và `021` (độ dài đúng bằng 3)). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_3)$**?
- A. `01`
- B. `011`
- C. `021`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Do $L(E_3) \subseteq L$, không có chuỗi nào trong A, B, C nằm ngoài $L$ $\implies$ Chọn D.

**Câu 19.** Xét biểu thức $E_3 = 0(1+2)1$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_3)$**?
- A. `011`
- B. `01`
- C. `021`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `01` thuộc $L$ ($S_0$ $\xrightarrow{0}$ $S_1$ $\xrightarrow{1}$ $S_3$ (NHẬN)) nhưng nằm ngoài $E_3$. Hai chuỗi còn lại thuộc cả $L$ và $E_3$.

**Câu 20.** Xét biểu thức $E_3 = 0(1+2)1$. Chuỗi nào **ĐỒNG THỜI KHÔNG** thuộc $L$ và **KHÔNG** thuộc $L(E_3)$?
- A. `01`
- B. `0`
- C. `021`
- D. `011`
👉 **Đáp án đúng: B**
- **Giải thích:** `0` vừa không được Automaton chấp nhận vừa không thuộc $E_3$. Các chuỗi kia đều thuộc $L$ hoặc $E_3$ (hoặc cả hai).

**Câu 21.** Xét biểu thức $E_4 = (0+1)^+ 1$ (chuỗi nhị phân trên `{0, 1}` có độ dài $\ge 2$ và kết thúc bằng `1`). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_4)$**?
- A. `01`
- B. `011`
- C. `11`
- D. `021`
👉 **Đáp án đúng: C**
- **Giải thích:** `11` thuộc $L(E_4)$ nhưng bị Automaton từ chối ($S_0$ $\xrightarrow{1}$ $S_2$ $\xrightarrow{1}$ $S_2$ (TỪ CHỐI)). Ba chuỗi còn lại đều thuộc $L$.

**Câu 22.** Xét biểu thức $E_4 = (0+1)^+ 1$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_4)$**?
- A. `01`
- B. `021`
- C. `011`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `021` thuộc $L$ ($S_0$ $\xrightarrow{0}$ $S_1$ $\xrightarrow{2}$ $S_4$ $\xrightarrow{1}$ $S_5$ (NHẬN)) nhưng không khớp khuôn mẫu $E_4$.

**Câu 23.** Nếu áp dụng đơn định hóa Automaton đang quan tâm thì DFA đầy đủ thu được có bao nhiêu trạng thái?
- A. 5
- B. 6
- C. 7
- D. 8
👉 **Đáp án đúng: B**
- **Giải thích:** Áp dụng thuật toán xây dựng tập con (Subset Construction) thu được **6 trạng thái** (xem bảng bên dưới): *(Lưu ý: Sơ đồ có xuất hiện tập con rỗng $\emptyset$ làm trạng thái bẫy chết. Nếu một số đề không vẽ trạng thái bẫy này thì còn **5 trạng thái**; theo chuẩn hàm chuyển toàn phần trong Sample 2 của IUH thì tính đủ **6 trạng thái**).*

| Trạng thái DFA | Tập con NFA | Đọc `0` | Đọc `1` | Đọc `2` | Kết thúc? |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $S_0$ (Đầu) | $\{q0\}$ | $S_1$ | $S_2$ | $S_2$ | Không |
| $S_1$ | $\{q1, q3\}$ | $S_2$ | $S_3$ | $S_4$ | Không |
| $S_2$ (Bẫy) | $\emptyset$ | $S_2$ | $S_2$ | $S_2$ | Không |
| $S_3$ | $\{q1, q2\}$ | $S_2$ | $S_3$ | $S_2$ | **CÓ** |
| $S_4$ | $\{q4\}$ | $S_2$ | $S_5$ | $S_2$ | Không |
| $S_5$ | $\{q2\}$ | $S_2$ | $S_2$ | $S_2$ | **CÓ** |

**Câu 24.** DFA tối giản tương đương có bao nhiêu trạng thái?
- A. 5
- B. 6
- C. 7
- D. 8
👉 **Đáp án đúng: B**
- **Giải thích:** DFA thu được **đã tối giản** (**6 trạng thái**). Phân hoạch các nhóm trạng thái tương đương cuối cùng gồm **6 nhóm**: `{$S_5$}`, `{$S_3$}`, `{$S_2$}`, `{$S_0$}`, `{$S_4$}`, `{$S_1$}`. *(Nếu bỏ trạng thái bẫy chết khỏi đồ thị thì còn **5 trạng thái**; tính đủ hàm toàn phần như Sample 2 là **6 trạng thái**).*

---

## HÌNH 9 (`image_13.png`): BẪY TRẠNG THÁI KHÔNG TỚI ĐƯỢC ($t_1, T_3$)

> **THÔNG TIN ĐỀ BÀI GỐC (Hình 9 trong OnTapAutomata.docx - ảnh `image_13.png`):**
> - Tập trạng thái: $Q = \{t0, t1, t2, T3\}$
> - Bảng chữ cái: $\Sigma = \{a, b\}$
> - Trạng thái bắt đầu: $t0$
> - Trạng thái kết thúc: $F = \{t1, t2\}$
> - Tính chất ban đầu: **Đơn định đầy đủ (Complete DFA)**
> - Biểu thức chính quy tương đương: **$a^* b (a+b)^*$**
> - Ngôn ngữ đoán nhận: Tập hợp các chuỗi chứa **ít nhất 1 chữ `b`**. *(Cực kỳ tinh vi: $t_1$ và $T_3$ không có mũi tên đi tới từ trạng thái khởi đầu $t_0$ nên là trạng thái chết không tới được — unreachable states — phải loại bỏ khi đơn định hóa/tối giản hóa!)*

```text
       a                       a, b
     ┌───┐                    ┌────┐
     │   ▼                    │    ▼
───► ( t0 ) ────── b ─────► ((( t2 )))
                                ▲
  ((( t1 ))) ───────── a ───────┘  (t1 và T3 KHÔNG tới được từ t0!)
       │
       └────── b ─────► ( T3 ) ──┐ a, b (vòng)
                          ▲──────┘
```

### Quy tắc vàng nhận diện trong 3 giây
1. **QUY TẮC 1:** Chỉ đi từ $t_0$: lặp `a` tại $t_0$, hễ gặp 1 chữ **`b`** thì nhảy sang $t_2$ và ở $t_2$ mãi mãi $\implies$ **cứ chứa ít nhất 1 chữ `b` là NHẬN!**
2. **QUY TẮC 2:** Hai đỉnh $t_1$ và $T_3$ đứng cô lập không có đường từ $t_0$ sang nên KHÔNG ảnh hưởng tới chuỗi được nhận! Khi tối giản hóa còn đúng **2 trạng thái $\{t_0, t_2\}$**!

### Bộ 24 câu trắc nghiệm chuẩn Đề Mẫu Sample 2

**Câu 1.** Xét các chuỗi: $s_1 = \text{"b"}$, $s_2 = \text{"a"}$, $s_3 = \text{"aa"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Tất cả các chuỗi được nêu.
👉 **Đáp án đúng: A**
- **Giải thích:** `b` hợp lệ ($S_0$ $\xrightarrow{b}$ $S_1$ (NHẬN)). Còn `a` và `aa` không về được trạng thái kết thúc.

**Câu 2.** Xét các chuỗi: $s_1 = \text{"aaa"}$, $s_2 = \text{"aaaa"}$, $s_3 = \text{"ab"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Các chọn lựa khác đều ĐÚNG.
👉 **Đáp án đúng: C**
- **Giải thích:** Chỉ có $s_3 =$ `ab` hợp lệ ($S_0$ $\xrightarrow{a}$ $S_0$ $\xrightarrow{b}$ $S_1$ (NHẬN)). Hai chuỗi $s_1, s_2$ bị từ chối.

**Câu 3.** Xét các chuỗi: $s_1 = \text{"ba"}$, $s_2 = \text{"bb"}$, $s_3 = \text{"aab"}$, $s_4 = \text{"aaaaa"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1, s_2$ và $s_3$
- B. $s_2, s_3$ và $s_4$
- C. $s_3$ và $s_4$
- D. $s_4$
👉 **Đáp án đúng: A**
- **Giải thích:** $s_4 =$ `aaaaa` bị từ chối ($S_0$ $\xrightarrow{a}$ $S_0$ $\xrightarrow{a}$ $S_0$ $\xrightarrow{a}$ $S_0$ $\xrightarrow{a}$ $S_0$ $\xrightarrow{a}$ $S_0$ (TỪ CHỐI)). Ba chuỗi còn lại đều hợp lệ.

**Câu 4.** Xét các chuỗi: $s_1 = \text{"aba"}$, $s_2 = \text{"aa"}$, $s_3 = \text{"abb"}$, $s_4 = \text{"aaa"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_4$
- C. $s_1$ và $s_3$
- D. $s_1$ và $s_4$
👉 **Đáp án đúng: C**
- **Giải thích:** $s_1 =$ `aba` và $s_3 =$ `abb` hợp lệ; còn $s_2 =$ `aa` và $s_4 =$ `aaa` không hợp lệ.

**Câu 5.** Xét các chuỗi: $s_1 = \text{"aa"}$, $s_2 = \text{"bbbbb"}$, $s_3 = \text{"aaa"}$, $s_4 = \text{"bbbba"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_4$
- C. $s_2$ và $s_3$
- D. $s_1$ và $s_4$
👉 **Đáp án đúng: B**
- **Giải thích:** $s_2 =$ `bbbbb` và $s_4 =$ `bbbba` đạt trạng thái kết thúc; $s_1, s_3$ bị từ chối.

**Câu 6.** Xét các chuỗi: $s_1 = \text{"ba"}$, $s_2 = \text{"bb"}$, $s_3 = \text{"aab"}$, $s_4 = \text{"aaaaa"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Chỉ duy nhất $s_4 =$ `aaaaa` bị từ chối ($S_0$ $\xrightarrow{a}$ $S_0$ $\xrightarrow{a}$ $S_0$ $\xrightarrow{a}$ $S_0$ $\xrightarrow{a}$ $S_0$ $\xrightarrow{a}$ $S_0$ (TỪ CHỐI)).

**Câu 7.** Xét các chuỗi: $s_1 = \text{"b"}$, $s_2 = \text{"a"}$, $s_3 = \text{"ab"}$, $s_4 = \text{"aa"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_2$
- B. $s_1$
- C. $s_3$
- D. Tất cả các chuỗi đều không hợp lệ.
👉 **Đáp án đúng: A**
- **Giải thích:** $s_1, s_3$ đều hợp lệ nên loại B, C, D. Chuỗi $s_2 =$ `a` không hợp lệ ($S_0$ $\xrightarrow{a}$ $S_0$ (TỪ CHỐI)). *(Lưu ý tương tự Câu 7 Sample 2: $s_4$ cũng không hợp lệ nhưng chỉ có $s_2$ xuất hiện trong 4 lựa chọn nên A là đáp án duy nhất)*.

**Câu 8.** Xét các chuỗi: $s_1 = \text{"aba"}$, $s_2 = \text{"abb"}$, $s_3 = \text{"bbbbb"}$, $s_4 = \text{"aa"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_3$
- C. $s_3$ và $s_4$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Duy nhất $s_4 =$ `aa` bị từ chối ($S_0$ $\xrightarrow{a}$ $S_0$ $\xrightarrow{a}$ $S_0$ (TỪ CHỐI)).

**Câu 9.** Xét các chuỗi: $s_1 = \text{"aba"}$, $s_2 = \text{"abb"}$, $s_3 = \text{"bbbbb"}$, $s_4 = \text{"aa"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cả $s_1, s_2, s_3$ đều là chuỗi hợp lệ; chuỗi duy nhất không hợp lệ là $s_4 =$ `aa` không nằm trong A, B, C $\implies$ Chọn D.

**Câu 10.** Xét các chuỗi: $s_1 = \text{"aba"}$, $s_2 = \text{"aa"}$, $s_3 = \text{"abb"}$, $s_4 = \text{"aaa"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$ và $s_4$
- B. $s_2$ và $s_3$
- C. $s_3$ và $s_4$
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cặp không hợp lệ đúng phải là $s_2$ và $s_4$ (`aa` và `aaa`), không có trong A, B, C $\implies$ Chọn D.

**Câu 11.** Xét các chuỗi: $s_1 = \text{"aa"}$, $s_2 = \text{"bbbbb"}$, $s_3 = \text{"aaa"}$, $s_4 = \text{"bbbba"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1, s_2$ và $s_3$
- B. $s_1$ và $s_3$
- C. $s_4$
- D. $s_3$ và $s_4$
👉 **Đáp án đúng: B**
- **Giải thích:** $s_1 =$ `aa` và $s_3 =$ `aaa` đều không đạt trạng thái kết thúc.

**Câu 12.** Xét các chuỗi: $s_1 = \text{"ba"}$, $s_2 = \text{"bb"}$, $s_3 = \text{"aab"}$, $s_4 = \text{"ε"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Chuỗi rỗng $s_4 = \varepsilon$ KHÔNG được nhận vì tập trạng thái khởi đầu (sau bao đóng $\varepsilon$) không chứa trạng thái kết thúc.

**Câu 13.** Xét biểu thức chính quy $E_1 = (a+b)^+$ (mọi chuỗi khác rỗng trên $\{a, b\}$). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc ngôn ngữ mô tả bởi $E_1$**?
- A. `b`
- B. `ab`
- C. `a`
- D. `ba`
👉 **Đáp án đúng: C**
- **Giải thích:** `a` thỏa $E_1$ nhưng bị Automaton từ chối ($S_0$ $\xrightarrow{a}$ $S_0$ (TỪ CHỐI)). Ba chuỗi còn lại đều thuộc $L$.

**Câu 14.** Xét biểu thức $E_1 = (a+b)^+$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc ngôn ngữ mô tả bởi $E_1$**?
- A. Không có chuỗi nào
- B. `ba`
- C. `aaaaa`
- D. `a`
👉 **Đáp án đúng: A**
- **Giải thích:** Mọi chuỗi hợp lệ của Automaton đều thỏa $E_1$ ($L \subseteq L(E_1)$), nên **không có chuỗi nào** thuộc $L$ mà lại ngoài $L(E_1)$!

**Câu 15.** Xét biểu thức $E_2 = a^* b a^*$ (chuỗi chứa đúng 1 chữ `b`). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_2)$**?
- A. `b`
- B. `ab`
- C. `ba`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Do $L(E_2) \subseteq L$ (và cả 3 chuỗi A, B, C đều thuộc $L$), nên không có chuỗi nào trong A, B, C thỏa điều kiện $\implies$ Chọn D.

**Câu 16.** Xét biểu thức $E_2 = a^* b a^*$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_2)$**?
- A. `b`
- B. `bb`
- C. `ab`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `bb` thuộc $L$ ($S_0$ $\xrightarrow{b}$ $S_1$ $\xrightarrow{b}$ $S_1$ (NHẬN)) nhưng không khớp khuôn mẫu của $E_2$. Còn `b` và `ab` đều thuộc cả $L$ lẫn $E_2$.

**Câu 17.** Xét biểu thức $E_2 = a^* b a^*$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_2)$**?
- A. `b`
- B. `ab`
- C. `ba`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cả 3 chuỗi `b`, `ab`, `ba` đều đồng thời thuộc cả $L$ lẫn $E_2$ $\implies$ Chọn D (y hệt bẫy Câu 17 Sample 2!).

**Câu 18.** Xét biểu thức $E_3 = (a+b)^* b$ (chuỗi kết thúc bằng `b`). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_3)$**?
- A. `b`
- B. `ab`
- C. `bb`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Do $L(E_3) \subseteq L$, không có chuỗi nào trong A, B, C nằm ngoài $L$ $\implies$ Chọn D.

**Câu 19.** Xét biểu thức $E_3 = (a+b)^* b$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_3)$**?
- A. `b`
- B. `ba`
- C. `ab`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `ba` thuộc $L$ ($S_0$ $\xrightarrow{b}$ $S_1$ $\xrightarrow{a}$ $S_1$ (NHẬN)) nhưng nằm ngoài $E_3$. Hai chuỗi còn lại thuộc cả $L$ và $E_3$.

**Câu 20.** Xét biểu thức $E_3 = (a+b)^* b$. Chuỗi nào **ĐỒNG THỜI KHÔNG** thuộc $L$ và **KHÔNG** thuộc $L(E_3)$?
- A. `ba`
- B. `a`
- C. `bb`
- D. `b`
👉 **Đáp án đúng: B**
- **Giải thích:** `a` vừa không được Automaton chấp nhận vừa không thuộc $E_3$. Các chuỗi kia đều thuộc $L$ hoặc $E_3$ (hoặc cả hai).

**Câu 21.** Xét biểu thức $E_4 = (a+b)^* a$ (chuỗi kết thúc bằng `a`). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_4)$**?
- A. `b`
- B. `ab`
- C. `a`
- D. `ba`
👉 **Đáp án đúng: C**
- **Giải thích:** `a` thuộc $L(E_4)$ nhưng bị Automaton từ chối ($S_0$ $\xrightarrow{a}$ $S_0$ (TỪ CHỐI)). Ba chuỗi còn lại đều thuộc $L$.

**Câu 22.** Xét biểu thức $E_4 = (a+b)^* a$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_4)$**?
- A. `ba`
- B. `b`
- C. `aba`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `b` thuộc $L$ ($S_0$ $\xrightarrow{b}$ $S_1$ (NHẬN)) nhưng không khớp khuôn mẫu $E_4$.

**Câu 23.** Nếu áp dụng đơn định hóa Automaton đang quan tâm thì DFA đầy đủ thu được có bao nhiêu trạng thái?
- A. 1
- B. 2
- C. 3
- D. 4
👉 **Đáp án đúng: B**
- **Giải thích:** Áp dụng thuật toán xây dựng tập con (Subset Construction) thu được **2 trạng thái** (xem bảng bên dưới): *(Không xuất hiện trạng thái rỗng $\emptyset$, tất cả **2 trạng thái** đều đang hoạt động).*

| Trạng thái DFA | Tập con NFA | Đọc `a` | Đọc `b` | Kết thúc? |
| :---: | :---: | :---: | :---: | :---: |
| $S_0$ (Đầu) | $\{t0\}$ | $S_0$ | $S_1$ | Không |
| $S_1$ | $\{t2\}$ | $S_1$ | $S_1$ | **CÓ** |

**Câu 24.** DFA tối giản tương đương có bao nhiêu trạng thái?
- A. 1
- B. 2
- C. 3
- D. 4
👉 **Đáp án đúng: B**
- **Giải thích:** DFA thu được **đã tối giản** (**2 trạng thái**). Phân hoạch các nhóm trạng thái tương đương cuối cùng gồm **2 nhóm**: `{$S_1$}`, `{$S_0$}`.

---

## HÌNH 10 (`image_9.png`): NFA 3 TRẠNG THÁI ($(a+b)^* b (b^+ a)^* b^*$)

> **THÔNG TIN ĐỀ BÀI GỐC (Hình 10 trong OnTapAutomata.docx - ảnh `image_9.png`):**
> - Tập trạng thái: $Q = \{q0, q1, q2\}$
> - Bảng chữ cái: $\Sigma = \{a, b\}$
> - Trạng thái bắt đầu: $q0$
> - Trạng thái kết thúc: $F = \{q1\}$
> - Tính chất ban đầu: **Không đơn định (NFA)**
> - Biểu thức chính quy tương đương: **$(a+b)^* b (b^+ a)^* b^*$**
> - Ngôn ngữ đoán nhận: Nhận mọi chuỗi kết thúc bằng **`b`**, HOẶC kết thúc bằng cụm `bba`, `bbba`, `bbaba` (cụ thể: sau chữ `b` đưa vào $q_1$ có các chu trình $b^+ a$ rồi kết thúc bằng $b^*$). Đuôi `ba` đơn lẻ hoặc chuỗi toàn `a` bị từ chối!

```text
      a, b                            b
     ┌────┐                         ┌───┐
     │    ▼          b              │   ▼
───► ( q0 ) ───────────► ((( q1 ))) ◄──── ( q2 )
       ▲                   │  ▲            ▲
       └─────── a, b ──────┘  └──── a ─────┘
                           └──── b ────────┘
```

### Quy tắc vàng nhận diện trong 3 giây
1. **QUY TẮC 1:** Mọi chuỗi **kết thúc bằng `b`** đều ĐƯỢC NHẬN (vì từ $q_0$ luôn chạy vòng đến cuối rồi đọc $b$ sang $q_1$).
2. **QUY TẮC 2:** Chuỗi kết thúc bằng **`a`** muốn hợp lệ phải đi theo đường $q_2 \xrightarrow{a} q_1$, nghĩa là trước chữ `a` cuối phải có ít nhất 2 chữ `b` (như `bba`, `bbba`, `bbaba`) — còn chuỗi **`ba`** hay toàn **`a`** bị loại!

### Bộ 24 câu trắc nghiệm chuẩn Đề Mẫu Sample 2

**Câu 1.** Xét các chuỗi: $s_1 = \text{"b"}$, $s_2 = \text{"a"}$, $s_3 = \text{"aa"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Tất cả các chuỗi được nêu.
👉 **Đáp án đúng: A**
- **Giải thích:** `b` hợp lệ ($S_0$ $\xrightarrow{b}$ $S_1$ (NHẬN)). Còn `a` và `aa` không về được trạng thái kết thúc.

**Câu 2.** Xét các chuỗi: $s_1 = \text{"ba"}$, $s_2 = \text{"aaa"}$, $s_3 = \text{"ab"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Các chọn lựa khác đều ĐÚNG.
👉 **Đáp án đúng: C**
- **Giải thích:** Chỉ có $s_3 =$ `ab` hợp lệ ($S_0$ $\xrightarrow{a}$ $S_0$ $\xrightarrow{b}$ $S_1$ (NHẬN)). Hai chuỗi $s_1, s_2$ bị từ chối.

**Câu 3.** Xét các chuỗi: $s_1 = \text{"bb"}$, $s_2 = \text{"aab"}$, $s_3 = \text{"abb"}$, $s_4 = \text{"aba"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1, s_2$ và $s_3$
- B. $s_2, s_3$ và $s_4$
- C. $s_3$ và $s_4$
- D. $s_4$
👉 **Đáp án đúng: A**
- **Giải thích:** $s_4 =$ `aba` bị từ chối ($S_0$ $\xrightarrow{a}$ $S_0$ $\xrightarrow{b}$ $S_1$ $\xrightarrow{a}$ $S_0$ (TỪ CHỐI)). Ba chuỗi còn lại đều hợp lệ.

**Câu 4.** Xét các chuỗi: $s_1 = \text{"bab"}$, $s_2 = \text{"baa"}$, $s_3 = \text{"bba"}$, $s_4 = \text{"aaaa"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_4$
- C. $s_1$ và $s_3$
- D. $s_1$ và $s_4$
👉 **Đáp án đúng: C**
- **Giải thích:** $s_1 =$ `bab` và $s_3 =$ `bba` hợp lệ; còn $s_2 =$ `baa` và $s_4 =$ `aaaa` không hợp lệ.

**Câu 5.** Xét các chuỗi: $s_1 = \text{"bbbaa"}$, $s_2 = \text{"bbbbb"}$, $s_3 = \text{"bbaaa"}$, $s_4 = \text{"bbbba"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_4$
- C. $s_2$ và $s_3$
- D. $s_1$ và $s_4$
👉 **Đáp án đúng: B**
- **Giải thích:** $s_2 =$ `bbbbb` và $s_4 =$ `bbbba` đạt trạng thái kết thúc; $s_1, s_3$ bị từ chối.

**Câu 6.** Xét các chuỗi: $s_1 = \text{"bb"}$, $s_2 = \text{"aab"}$, $s_3 = \text{"abb"}$, $s_4 = \text{"aba"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Chỉ duy nhất $s_4 =$ `aba` bị từ chối ($S_0$ $\xrightarrow{a}$ $S_0$ $\xrightarrow{b}$ $S_1$ $\xrightarrow{a}$ $S_0$ (TỪ CHỐI)).

**Câu 7.** Xét các chuỗi: $s_1 = \text{"b"}$, $s_2 = \text{"a"}$, $s_3 = \text{"ab"}$, $s_4 = \text{"aa"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_2$
- B. $s_1$
- C. $s_3$
- D. Tất cả các chuỗi đều không hợp lệ.
👉 **Đáp án đúng: A**
- **Giải thích:** $s_1, s_3$ đều hợp lệ nên loại B, C, D. Chuỗi $s_2 =$ `a` không hợp lệ ($S_0$ $\xrightarrow{a}$ $S_0$ (TỪ CHỐI)). *(Lưu ý tương tự Câu 7 Sample 2: $s_4$ cũng không hợp lệ nhưng chỉ có $s_2$ xuất hiện trong 4 lựa chọn nên A là đáp án duy nhất)*.

**Câu 8.** Xét các chuỗi: $s_1 = \text{"bab"}$, $s_2 = \text{"bba"}$, $s_3 = \text{"bbbbb"}$, $s_4 = \text{"baa"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_3$
- C. $s_3$ và $s_4$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Duy nhất $s_4 =$ `baa` bị từ chối ($S_0$ $\xrightarrow{b}$ $S_1$ $\xrightarrow{a}$ $S_0$ $\xrightarrow{a}$ $S_0$ (TỪ CHỐI)).

**Câu 9.** Xét các chuỗi: $s_1 = \text{"bab"}$, $s_2 = \text{"bba"}$, $s_3 = \text{"bbbbb"}$, $s_4 = \text{"baa"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cả $s_1, s_2, s_3$ đều là chuỗi hợp lệ; chuỗi duy nhất không hợp lệ là $s_4 =$ `baa` không nằm trong A, B, C $\implies$ Chọn D.

**Câu 10.** Xét các chuỗi: $s_1 = \text{"bab"}$, $s_2 = \text{"baa"}$, $s_3 = \text{"bba"}$, $s_4 = \text{"aaaa"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$ và $s_4$
- B. $s_2$ và $s_3$
- C. $s_3$ và $s_4$
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cặp không hợp lệ đúng phải là $s_2$ và $s_4$ (`baa` và `aaaa`), không có trong A, B, C $\implies$ Chọn D.

**Câu 11.** Xét các chuỗi: $s_1 = \text{"bbbaa"}$, $s_2 = \text{"bbbbb"}$, $s_3 = \text{"bbaaa"}$, $s_4 = \text{"bbbba"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1, s_2$ và $s_3$
- B. $s_1$ và $s_3$
- C. $s_4$
- D. $s_3$ và $s_4$
👉 **Đáp án đúng: B**
- **Giải thích:** $s_1 =$ `bbbaa` và $s_3 =$ `bbaaa` đều không đạt trạng thái kết thúc.

**Câu 12.** Xét các chuỗi: $s_1 = \text{"bb"}$, $s_2 = \text{"aab"}$, $s_3 = \text{"abb"}$, $s_4 = \text{"ε"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Chuỗi rỗng $s_4 = \varepsilon$ KHÔNG được nhận vì tập trạng thái khởi đầu (sau bao đóng $\varepsilon$) không chứa trạng thái kết thúc.

**Câu 13.** Xét biểu thức chính quy $E_1 = (a+b)^+$ (mọi chuỗi khác rỗng trên $\{a, b\}$). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc ngôn ngữ mô tả bởi $E_1$**?
- A. `b`
- B. `ab`
- C. `a`
- D. `bb`
👉 **Đáp án đúng: C**
- **Giải thích:** `a` thỏa $E_1$ nhưng bị Automaton từ chối ($S_0$ $\xrightarrow{a}$ $S_0$ (TỪ CHỐI)). Ba chuỗi còn lại đều thuộc $L$.

**Câu 14.** Xét biểu thức $E_1 = (a+b)^+$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc ngôn ngữ mô tả bởi $E_1$**?
- A. Không có chuỗi nào
- B. `bb`
- C. `aba`
- D. `a`
👉 **Đáp án đúng: A**
- **Giải thích:** Mọi chuỗi hợp lệ của Automaton đều thỏa $E_1$ ($L \subseteq L(E_1)$), nên **không có chuỗi nào** thuộc $L$ mà lại ngoài $L(E_1)$!

**Câu 15.** Xét biểu thức $E_2 = (a+b)^* b$ (mọi chuỗi kết thúc bằng `b`). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_2)$**?
- A. `b`
- B. `ab`
- C. `bb`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Do $L(E_2) \subseteq L$ (và cả 3 chuỗi A, B, C đều thuộc $L$), nên không có chuỗi nào trong A, B, C thỏa điều kiện $\implies$ Chọn D.

**Câu 16.** Xét biểu thức $E_2 = (a+b)^* b$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_2)$**?
- A. `b`
- B. `bba`
- C. `ab`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `bba` thuộc $L$ ($S_0$ $\xrightarrow{b}$ $S_1$ $\xrightarrow{b}$ $S_2$ $\xrightarrow{a}$ $S_1$ (NHẬN)) nhưng không khớp khuôn mẫu của $E_2$. Còn `b` và `ab` đều thuộc cả $L$ lẫn $E_2$.

**Câu 17.** Xét biểu thức $E_2 = (a+b)^* b$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_2)$**?
- A. `b`
- B. `ab`
- C. `bb`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cả 3 chuỗi `b`, `ab`, `bb` đều đồng thời thuộc cả $L$ lẫn $E_2$ $\implies$ Chọn D (y hệt bẫy Câu 17 Sample 2!).

**Câu 18.** Xét biểu thức $E_3 = (a+b)^* (b + bba)$ (kết thúc bằng `b` hoặc `bba`). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_3)$**?
- A. `b`
- B. `ab`
- C. `bb`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Do $L(E_3) \subseteq L$, không có chuỗi nào trong A, B, C nằm ngoài $L$ $\implies$ Chọn D.

**Câu 19.** Xét biểu thức $E_3 = (a+b)^* (b + bba)$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_3)$**?
- A. `b`
- B. `bbaba`
- C. `ab`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `bbaba` thuộc $L$ ($S_0$ $\xrightarrow{b}$ $S_1$ $\xrightarrow{b}$ $S_2$ $\xrightarrow{a}$ $S_1$ $\xrightarrow{b}$ $S_2$ $\xrightarrow{a}$ $S_1$ (NHẬN)) nhưng nằm ngoài $E_3$. Hai chuỗi còn lại thuộc cả $L$ và $E_3$.

**Câu 20.** Xét biểu thức $E_3 = (a+b)^* (b + bba)$. Chuỗi nào **ĐỒNG THỜI KHÔNG** thuộc $L$ và **KHÔNG** thuộc $L(E_3)$?
- A. `bbaba`
- B. `a`
- C. `bb`
- D. `b`
👉 **Đáp án đúng: B**
- **Giải thích:** `a` vừa không được Automaton chấp nhận vừa không thuộc $E_3$. Các chuỗi kia đều thuộc $L$ hoặc $E_3$ (hoặc cả hai).

**Câu 21.** Xét biểu thức $E_4 = a^* b^+ a^*$ (chứa một khối `b` kẹp bởi các chữ `a`). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_4)$**?
- A. `b`
- B. `ab`
- C. `ba`
- D. `bb`
👉 **Đáp án đúng: C**
- **Giải thích:** `ba` thuộc $L(E_4)$ nhưng bị Automaton từ chối ($S_0$ $\xrightarrow{b}$ $S_1$ $\xrightarrow{a}$ $S_0$ (TỪ CHỐI)). Ba chuỗi còn lại đều thuộc $L$.

**Câu 22.** Xét biểu thức $E_4 = a^* b^+ a^*$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_4)$**?
- A. `b`
- B. `bab`
- C. `ab`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `bab` thuộc $L$ ($S_0$ $\xrightarrow{b}$ $S_1$ $\xrightarrow{a}$ $S_0$ $\xrightarrow{b}$ $S_1$ (NHẬN)) nhưng không khớp khuôn mẫu $E_4$.

**Câu 23.** Nếu áp dụng đơn định hóa Automaton đang quan tâm thì DFA đầy đủ thu được có bao nhiêu trạng thái?
- A. 2
- B. 3
- C. 4
- D. 5
👉 **Đáp án đúng: B**
- **Giải thích:** Áp dụng thuật toán xây dựng tập con (Subset Construction) thu được **3 trạng thái** (xem bảng bên dưới): *(Không xuất hiện trạng thái rỗng $\emptyset$, tất cả **3 trạng thái** đều đang hoạt động).*

| Trạng thái DFA | Tập con NFA | Đọc `a` | Đọc `b` | Kết thúc? |
| :---: | :---: | :---: | :---: | :---: |
| $S_0$ (Đầu) | $\{q0\}$ | $S_0$ | $S_1$ | Không |
| $S_1$ | $\{q0, q1\}$ | $S_0$ | $S_2$ | **CÓ** |
| $S_2$ | $\{q0, q1, q2\}$ | $S_1$ | $S_2$ | **CÓ** |

**Câu 24.** DFA tối giản tương đương có bao nhiêu trạng thái?
- A. 2
- B. 3
- C. 4
- D. 5
👉 **Đáp án đúng: B**
- **Giải thích:** DFA thu được **đã tối giản** (**3 trạng thái**). Phân hoạch các nhóm trạng thái tương đương cuối cùng gồm **3 nhóm**: `{$S_2$}`, `{$S_1$}`, `{$S_0$}`.

---
