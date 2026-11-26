# BỘ ĐỀ AUTOMATA PHẦN 3: HÌNH 11 ĐẾN HÌNH 14 (96 CÂU CHUẨN ĐỀ MẪU SAMPLE 2)
## ĐÚNG THỨ TỰ TRONG ONTAPAUTOMATA.DOCX - MỖI HÌNH FULL 24 CÂU + BẢNG SUBSET & TỐI GIẢN

> Bao gồm: **Hình 11** (`image_6.png`), **Hình 12** (`image_5.png`), **Hình 13** (`image_2.png`), **Hình 14** (`image_11.png` — biến thể sinh đôi của Sample 2).

---

## HÌNH 11 (`image_6.png`): DFA KẾT THÚC BẰNG `101` KHÔNG CHỒNG LẤN

> **THÔNG TIN ĐỀ BÀI GỐC (Hình 11 trong OnTapAutomata.docx - ảnh `image_6.png`):**
> - Tập trạng thái: $Q = \{q1, q2, q3, q4\}$
> - Bảng chữ cái: $\Sigma = \{0, 1\}$
> - Trạng thái bắt đầu: $q1$
> - Trạng thái kết thúc: $F = \{q4\}$
> - Tính chất ban đầu: **Đơn định đầy đủ (Complete DFA)**
> - Biểu thức chính quy tương đương: **$(0^* 1^+ (00 + 010))^* 0^* 1^+ (011^+)^* 01$**
> - Ngôn ngữ đoán nhận: Kết thúc bằng `101`, **NHƯNG LƯU Ý BẪY CỰC ĐỘC**: tại $q_4$, cạnh `0` quay thẳng về đầu $q_1$ (reset toàn bộ) chứ không về $q_3$! Vì vậy hai cụm `101` không thể chồng nhau — ví dụ `10101` **BỊ TỪ CHỐI**, trong khi `101`, `1101`, `101101` được nhận!

```text
      0                  1
    ┌───┐              ┌───┐
    │   ▼      1       │   ▼
───► ( q1 ) ──────► ( q2 )
       ▲  ▲           │ ▲
       │  │ 0         │ │ 1 (từ q4)
     0 │  └─────── ( q3 )
       │             │ 1
       │             ▼
     ((( q4 ))) ◄────┘
```

### Quy tắc vàng nhận diện trong 3 giây
1. **QUY TẮC 1:** Đường vào $q_4$ duy nhất đi qua $q_1 \xrightarrow{1} q_2 \xrightarrow{0} q_3 \xrightarrow{1} q_4$, nên mọi chuỗi hợp lệ đều có 3 ký tự cuối là **`101`**.
2. **QUY TẮC 2 (CÁI BẪY `10101`):** Khi vừa đọc xong `101` (đứng tại $q_4$), nếu đọc tiếp **`0`** thì máy **RESET VỀ TẬN $q_1$** (quên mất chữ `1` đứng trước!). Do đó **`10101` bị từ chối** (rơi vào $q_2$)! Nếu đọc tiếp `1` thì về $q_2$ nên `101101` vẫn hợp lệ.

### Bộ 24 câu trắc nghiệm chuẩn Đề Mẫu Sample 2

**Câu 1.** Xét các chuỗi: $s_1 = \text{"101"}$, $s_2 = \text{"0"}$, $s_3 = \text{"1"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Tất cả các chuỗi được nêu.
👉 **Đáp án đúng: A**
- **Giải thích:** `101` hợp lệ ($S_0$ $\xrightarrow{1}$ $S_1$ $\xrightarrow{0}$ $S_2$ $\xrightarrow{1}$ $S_3$ (NHẬN)). Còn `0` và `1` không về được trạng thái kết thúc.

**Câu 2.** Xét các chuỗi: $s_1 = \text{"00"}$, $s_2 = \text{"01"}$, $s_3 = \text{"0101"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Các chọn lựa khác đều ĐÚNG.
👉 **Đáp án đúng: C**
- **Giải thích:** Chỉ có $s_3 =$ `0101` hợp lệ ($S_0$ $\xrightarrow{0}$ $S_0$ $\xrightarrow{1}$ $S_1$ $\xrightarrow{0}$ $S_2$ $\xrightarrow{1}$ $S_3$ (NHẬN)). Hai chuỗi $s_1, s_2$ bị từ chối.

**Câu 3.** Xét các chuỗi: $s_1 = \text{"1101"}$, $s_2 = \text{"00101"}$, $s_3 = \text{"01101"}$, $s_4 = \text{"10"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1, s_2$ và $s_3$
- B. $s_2, s_3$ và $s_4$
- C. $s_3$ và $s_4$
- D. $s_4$
👉 **Đáp án đúng: A**
- **Giải thích:** $s_4 =$ `10` bị từ chối ($S_0$ $\xrightarrow{1}$ $S_1$ $\xrightarrow{0}$ $S_2$ (TỪ CHỐI)). Ba chuỗi còn lại đều hợp lệ.

**Câu 4.** Xét các chuỗi: $s_1 = \text{"11101"}$, $s_2 = \text{"11"}$, $s_3 = \text{"101"}$, $s_4 = \text{"000"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_4$
- C. $s_1$ và $s_3$
- D. $s_1$ và $s_4$
👉 **Đáp án đúng: C**
- **Giải thích:** $s_1 =$ `11101` và $s_3 =$ `101` hợp lệ; còn $s_2 =$ `11` và $s_4 =$ `000` không hợp lệ.

**Câu 5.** Xét các chuỗi: $s_1 = \text{"11111"}$, $s_2 = \text{"101"}$, $s_3 = \text{"11110"}$, $s_4 = \text{"0101"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_4$
- C. $s_2$ và $s_3$
- D. $s_1$ và $s_4$
👉 **Đáp án đúng: B**
- **Giải thích:** $s_2 =$ `101` và $s_4 =$ `0101` đạt trạng thái kết thúc; $s_1, s_3$ bị từ chối.

**Câu 6.** Xét các chuỗi: $s_1 = \text{"1101"}$, $s_2 = \text{"00101"}$, $s_3 = \text{"01101"}$, $s_4 = \text{"10"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Chỉ duy nhất $s_4 =$ `10` bị từ chối ($S_0$ $\xrightarrow{1}$ $S_1$ $\xrightarrow{0}$ $S_2$ (TỪ CHỐI)).

**Câu 7.** Xét các chuỗi: $s_1 = \text{"101"}$, $s_2 = \text{"0"}$, $s_3 = \text{"0101"}$, $s_4 = \text{"1"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_2$
- B. $s_1$
- C. $s_3$
- D. Tất cả các chuỗi đều không hợp lệ.
👉 **Đáp án đúng: A**
- **Giải thích:** $s_1, s_3$ đều hợp lệ nên loại B, C, D. Chuỗi $s_2 =$ `0` không hợp lệ ($S_0$ $\xrightarrow{0}$ $S_0$ (TỪ CHỐI)). *(Lưu ý tương tự Câu 7 Sample 2: $s_4$ cũng không hợp lệ nhưng chỉ có $s_2$ xuất hiện trong 4 lựa chọn nên A là đáp án duy nhất)*.

**Câu 8.** Xét các chuỗi: $s_1 = \text{"11101"}$, $s_2 = \text{"101"}$, $s_3 = \text{"0101"}$, $s_4 = \text{"11"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_3$
- C. $s_3$ và $s_4$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Duy nhất $s_4 =$ `11` bị từ chối ($S_0$ $\xrightarrow{1}$ $S_1$ $\xrightarrow{1}$ $S_1$ (TỪ CHỐI)).

**Câu 9.** Xét các chuỗi: $s_1 = \text{"11101"}$, $s_2 = \text{"101"}$, $s_3 = \text{"0101"}$, $s_4 = \text{"11"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cả $s_1, s_2, s_3$ đều là chuỗi hợp lệ; chuỗi duy nhất không hợp lệ là $s_4 =$ `11` không nằm trong A, B, C $\implies$ Chọn D.

**Câu 10.** Xét các chuỗi: $s_1 = \text{"11101"}$, $s_2 = \text{"11"}$, $s_3 = \text{"101"}$, $s_4 = \text{"000"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$ và $s_4$
- B. $s_2$ và $s_3$
- C. $s_3$ và $s_4$
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cặp không hợp lệ đúng phải là $s_2$ và $s_4$ (`11` và `000`), không có trong A, B, C $\implies$ Chọn D.

**Câu 11.** Xét các chuỗi: $s_1 = \text{"11111"}$, $s_2 = \text{"101"}$, $s_3 = \text{"11110"}$, $s_4 = \text{"0101"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1, s_2$ và $s_3$
- B. $s_1$ và $s_3$
- C. $s_4$
- D. $s_3$ và $s_4$
👉 **Đáp án đúng: B**
- **Giải thích:** $s_1 =$ `11111` và $s_3 =$ `11110` đều không đạt trạng thái kết thúc.

**Câu 12.** Xét các chuỗi: $s_1 = \text{"1101"}$, $s_2 = \text{"00101"}$, $s_3 = \text{"01101"}$, $s_4 = \text{"ε"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Chuỗi rỗng $s_4 = \varepsilon$ KHÔNG được nhận vì tập trạng thái khởi đầu (sau bao đóng $\varepsilon$) không chứa trạng thái kết thúc.

**Câu 13.** Xét biểu thức chính quy $E_1 = (0+1)^* 101$ (mọi chuỗi kết thúc bằng `101` (kể cả `10101`)). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc ngôn ngữ mô tả bởi $E_1$**?
- A. `101`
- B. `0101`
- C. `10101`
- D. `1101`
👉 **Đáp án đúng: C**
- **Giải thích:** `10101` thỏa $E_1$ nhưng bị Automaton từ chối ($S_0$ $\xrightarrow{1}$ $S_1$ $\xrightarrow{0}$ $S_2$ $\xrightarrow{1}$ $S_3$ $\xrightarrow{0}$ $S_0$ $\xrightarrow{1}$ $S_1$ (TỪ CHỐI)). Ba chuỗi còn lại đều thuộc $L$.

**Câu 14.** Xét biểu thức $E_1 = (0+1)^* 101$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc ngôn ngữ mô tả bởi $E_1$**?
- A. Không có chuỗi nào
- B. `1101`
- C. `10`
- D. `10101`
👉 **Đáp án đúng: A**
- **Giải thích:** Mọi chuỗi hợp lệ của Automaton đều thỏa $E_1$ ($L \subseteq L(E_1)$), nên **không có chuỗi nào** thuộc $L$ mà lại ngoài $L(E_1)$!

**Câu 15.** Xét biểu thức $E_2 = 0^* 101$ (toàn `0` ở đầu rồi đến `101`). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_2)$**?
- A. `101`
- B. `0101`
- C. `00101`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Do $L(E_2) \subseteq L$ (và cả 3 chuỗi A, B, C đều thuộc $L$), nên không có chuỗi nào trong A, B, C thỏa điều kiện $\implies$ Chọn D.

**Câu 16.** Xét biểu thức $E_2 = 0^* 101$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_2)$**?
- A. `101`
- B. `1101`
- C. `0101`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `1101` thuộc $L$ ($S_0$ $\xrightarrow{1}$ $S_1$ $\xrightarrow{1}$ $S_1$ $\xrightarrow{0}$ $S_2$ $\xrightarrow{1}$ $S_3$ (NHẬN)) nhưng không khớp khuôn mẫu của $E_2$. Còn `101` và `0101` đều thuộc cả $L$ lẫn $E_2$.

**Câu 17.** Xét biểu thức $E_2 = 0^* 101$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_2)$**?
- A. `101`
- B. `0101`
- C. `00101`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cả 3 chuỗi `101`, `0101`, `00101` đều đồng thời thuộc cả $L$ lẫn $E_2$ $\implies$ Chọn D (y hệt bẫy Câu 17 Sample 2!).

**Câu 18.** Xét biểu thức $E_3 = 1(01)^*$ (bắt đầu bằng `1` theo sau bởi số lần lặp `01`). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_3)$**?
- A. `101`
- B. `1`
- C. `0101`
- D. `1101`
👉 **Đáp án đúng: B**
- **Giải thích:** `1` thuộc $E_3$ nhưng không được Automaton chấp nhận ($S_0$ $\xrightarrow{1}$ $S_1$ (TỪ CHỐI)). Các chuỗi kia đều thuộc $L$.

**Câu 19.** Xét biểu thức $E_3 = 1(01)^*$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_3)$**?
- A. `0101`
- B. `1`
- C. `0`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: A**
- **Giải thích:** `0101` thuộc $L$ nhưng không thuộc $E_3$; hai chuỗi sau không thuộc $L$.

**Câu 20.** Xét biểu thức $E_3 = 1(01)^*$. Chuỗi nào **ĐỒNG THỜI KHÔNG** thuộc $L$ và **KHÔNG** thuộc $L(E_3)$?
- A. `0101`
- B. `0`
- C. `1`
- D. `101`
👉 **Đáp án đúng: B**
- **Giải thích:** `0` vừa không được Automaton chấp nhận vừa không thuộc $E_3$. Các chuỗi kia đều thuộc $L$ hoặc $E_3$ (hoặc cả hai).

**Câu 21.** Xét biểu thức $E_4 = 1(0+1)^* 1$ (chuỗi bắt đầu bằng `1` và kết thúc bằng `1`). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_4)$**?
- A. `101`
- B. `0101`
- C. `11`
- D. `1101`
👉 **Đáp án đúng: C**
- **Giải thích:** `11` thuộc $L(E_4)$ nhưng bị Automaton từ chối ($S_0$ $\xrightarrow{1}$ $S_1$ $\xrightarrow{1}$ $S_1$ (TỪ CHỐI)). Ba chuỗi còn lại đều thuộc $L$.

**Câu 22.** Xét biểu thức $E_4 = 1(0+1)^* 1$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_4)$**?
- A. `101`
- B. `0101`
- C. `1101`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `0101` thuộc $L$ ($S_0$ $\xrightarrow{0}$ $S_0$ $\xrightarrow{1}$ $S_1$ $\xrightarrow{0}$ $S_2$ $\xrightarrow{1}$ $S_3$ (NHẬN)) nhưng không khớp khuôn mẫu $E_4$.

**Câu 23.** Nếu áp dụng đơn định hóa Automaton đang quan tâm thì DFA đầy đủ thu được có bao nhiêu trạng thái?
- A. 3
- B. 4
- C. 5
- D. 6
👉 **Đáp án đúng: B**
- **Giải thích:** Áp dụng thuật toán xây dựng tập con (Subset Construction) thu được **4 trạng thái** (xem bảng bên dưới): *(Không xuất hiện trạng thái rỗng $\emptyset$, tất cả **4 trạng thái** đều đang hoạt động).*

| Trạng thái DFA | Tập con NFA | Đọc `0` | Đọc `1` | Kết thúc? |
| :---: | :---: | :---: | :---: | :---: |
| $S_0$ (Đầu) | $\{q1\}$ | $S_0$ | $S_1$ | Không |
| $S_1$ | $\{q2\}$ | $S_2$ | $S_1$ | Không |
| $S_2$ | $\{q3\}$ | $S_0$ | $S_3$ | Không |
| $S_3$ | $\{q4\}$ | $S_0$ | $S_1$ | **CÓ** |

**Câu 24.** DFA tối giản tương đương có bao nhiêu trạng thái?
- A. 3
- B. 4
- C. 5
- D. 6
👉 **Đáp án đúng: B**
- **Giải thích:** DFA thu được **đã tối giản** (**4 trạng thái**). Phân hoạch các nhóm trạng thái tương đương cuối cùng gồm **4 nhóm**: `{$S_3$}`, `{$S_1$}`, `{$S_0$}`, `{$S_2$}`.

---

## HÌNH 12 (`image_5.png`): NFA 3 TRẠNG THÁI CHỨA `aba` HOẶC ĐUÔI `a(bb)*`

> **THÔNG TIN ĐỀ BÀI GỐC (Hình 12 trong OnTapAutomata.docx - ảnh `image_5.png`):**
> - Tập trạng thái: $Q = \{q0, q1, q2\}$
> - Bảng chữ cái: $\Sigma = \{a, b\}$
> - Trạng thái bắt đầu: $q0$
> - Trạng thái kết thúc: $F = \{q1\}$
> - Tính chất ban đầu: **Không đơn định (NFA)**
> - Biểu thức chính quy tương đương: **$b^* a (a + bb)^* (\varepsilon + ba(a+b)^*)$**
> - Ngôn ngữ đoán nhận: Chấp nhận chuỗi kết thúc bằng `a` (hoặc `abb`, `abbbb`...), HOẶC bất kỳ chuỗi nào có đi qua chu trình tạo `aba` (từ đó đạt tập trạng thái kết thúc vĩnh viễn).

```text
      a, b                            a
     ┌────┐                         ┌───┐
     │    ▼          a              │   ▼
───► ( q0 ) ───────────► ((( q1 ))) ◄──── ( q2 )
       ▲                   │  ▲            ▲
       └─────── b ─────────┘  └─── a, b ───┘
                           └────── b ──────┘
```

### Quy tắc vàng nhận diện trong 3 giây
1. **QUY TẮC 1:** Hễ chuỗi **kết thúc bằng `a`** (như `a`, `ba`, `bba`, `aa`), đi $q_0 \xrightarrow{a} q_1$ $\implies$ **CHẮC CHẮN NHẬN**!
2. **QUY TẮC 2:** Chuỗi không có bất kỳ chữ `a` nào ($\varepsilon$, `b`, `bb`, `bbb`...) chắc chắn BỊ TỪ CHỐI. Ngoài ra `ab` bị từ chối nhưng `abb` được nhận ($q_0 \xrightarrow{a} q_1 \xrightarrow{b} q_2 \xrightarrow{b} q_1$).

### Bộ 24 câu trắc nghiệm chuẩn Đề Mẫu Sample 2

**Câu 1.** Xét các chuỗi: $s_1 = \text{"a"}$, $s_2 = \text{"b"}$, $s_3 = \text{"ab"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Tất cả các chuỗi được nêu.
👉 **Đáp án đúng: A**
- **Giải thích:** `a` hợp lệ ($S_0$ $\xrightarrow{a}$ $S_1$ (NHẬN)). Còn `b` và `ab` không về được trạng thái kết thúc.

**Câu 2.** Xét các chuỗi: $s_1 = \text{"bb"}$, $s_2 = \text{"aab"}$, $s_3 = \text{"aa"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Các chọn lựa khác đều ĐÚNG.
👉 **Đáp án đúng: C**
- **Giải thích:** Chỉ có $s_3 =$ `aa` hợp lệ ($S_0$ $\xrightarrow{a}$ $S_1$ $\xrightarrow{a}$ $S_1$ (NHẬN)). Hai chuỗi $s_1, s_2$ bị từ chối.

**Câu 3.** Xét các chuỗi: $s_1 = \text{"ba"}$, $s_2 = \text{"aaa"}$, $s_3 = \text{"aba"}$, $s_4 = \text{"bab"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1, s_2$ và $s_3$
- B. $s_2, s_3$ và $s_4$
- C. $s_3$ và $s_4$
- D. $s_4$
👉 **Đáp án đúng: A**
- **Giải thích:** $s_4 =$ `bab` bị từ chối ($S_0$ $\xrightarrow{b}$ $S_0$ $\xrightarrow{a}$ $S_1$ $\xrightarrow{b}$ $S_2$ (TỪ CHỐI)). Ba chuỗi còn lại đều hợp lệ.

**Câu 4.** Xét các chuỗi: $s_1 = \text{"abb"}$, $s_2 = \text{"bbb"}$, $s_3 = \text{"baa"}$, $s_4 = \text{"aaab"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_4$
- C. $s_1$ và $s_3$
- D. $s_1$ và $s_4$
👉 **Đáp án đúng: C**
- **Giải thích:** $s_1 =$ `abb` và $s_3 =$ `baa` hợp lệ; còn $s_2 =$ `bbb` và $s_4 =$ `aaab` không hợp lệ.

**Câu 5.** Xét các chuỗi: $s_1 = \text{"bbbbb"}$, $s_2 = \text{"bbbba"}$, $s_3 = \text{"bbbab"}$, $s_4 = \text{"bbbaa"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_4$
- C. $s_2$ và $s_3$
- D. $s_1$ và $s_4$
👉 **Đáp án đúng: B**
- **Giải thích:** $s_2 =$ `bbbba` và $s_4 =$ `bbbaa` đạt trạng thái kết thúc; $s_1, s_3$ bị từ chối.

**Câu 6.** Xét các chuỗi: $s_1 = \text{"ba"}$, $s_2 = \text{"aaa"}$, $s_3 = \text{"aba"}$, $s_4 = \text{"bab"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Chỉ duy nhất $s_4 =$ `bab` bị từ chối ($S_0$ $\xrightarrow{b}$ $S_0$ $\xrightarrow{a}$ $S_1$ $\xrightarrow{b}$ $S_2$ (TỪ CHỐI)).

**Câu 7.** Xét các chuỗi: $s_1 = \text{"a"}$, $s_2 = \text{"b"}$, $s_3 = \text{"aa"}$, $s_4 = \text{"ab"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_2$
- B. $s_1$
- C. $s_3$
- D. Tất cả các chuỗi đều không hợp lệ.
👉 **Đáp án đúng: A**
- **Giải thích:** $s_1, s_3$ đều hợp lệ nên loại B, C, D. Chuỗi $s_2 =$ `b` không hợp lệ ($S_0$ $\xrightarrow{b}$ $S_0$ (TỪ CHỐI)). *(Lưu ý tương tự Câu 7 Sample 2: $s_4$ cũng không hợp lệ nhưng chỉ có $s_2$ xuất hiện trong 4 lựa chọn nên A là đáp án duy nhất)*.

**Câu 8.** Xét các chuỗi: $s_1 = \text{"abb"}$, $s_2 = \text{"baa"}$, $s_3 = \text{"bbbba"}$, $s_4 = \text{"bbb"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_3$
- C. $s_3$ và $s_4$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Duy nhất $s_4 =$ `bbb` bị từ chối ($S_0$ $\xrightarrow{b}$ $S_0$ $\xrightarrow{b}$ $S_0$ $\xrightarrow{b}$ $S_0$ (TỪ CHỐI)).

**Câu 9.** Xét các chuỗi: $s_1 = \text{"abb"}$, $s_2 = \text{"baa"}$, $s_3 = \text{"bbbba"}$, $s_4 = \text{"bbb"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cả $s_1, s_2, s_3$ đều là chuỗi hợp lệ; chuỗi duy nhất không hợp lệ là $s_4 =$ `bbb` không nằm trong A, B, C $\implies$ Chọn D.

**Câu 10.** Xét các chuỗi: $s_1 = \text{"abb"}$, $s_2 = \text{"bbb"}$, $s_3 = \text{"baa"}$, $s_4 = \text{"aaab"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$ và $s_4$
- B. $s_2$ và $s_3$
- C. $s_3$ và $s_4$
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cặp không hợp lệ đúng phải là $s_2$ và $s_4$ (`bbb` và `aaab`), không có trong A, B, C $\implies$ Chọn D.

**Câu 11.** Xét các chuỗi: $s_1 = \text{"bbbbb"}$, $s_2 = \text{"bbbba"}$, $s_3 = \text{"bbbab"}$, $s_4 = \text{"bbbaa"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1, s_2$ và $s_3$
- B. $s_1$ và $s_3$
- C. $s_4$
- D. $s_3$ và $s_4$
👉 **Đáp án đúng: B**
- **Giải thích:** $s_1 =$ `bbbbb` và $s_3 =$ `bbbab` đều không đạt trạng thái kết thúc.

**Câu 12.** Xét các chuỗi: $s_1 = \text{"ba"}$, $s_2 = \text{"aaa"}$, $s_3 = \text{"aba"}$, $s_4 = \text{"ε"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Chuỗi rỗng $s_4 = \varepsilon$ KHÔNG được nhận vì tập trạng thái khởi đầu (sau bao đóng $\varepsilon$) không chứa trạng thái kết thúc.

**Câu 13.** Xét biểu thức chính quy $E_1 = (a+b)^* a (a+b)^*$ (chuỗi chứa ít nhất 1 chữ `a`). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc ngôn ngữ mô tả bởi $E_1$**?
- A. `a`
- B. `aa`
- C. `ab`
- D. `ba`
👉 **Đáp án đúng: C**
- **Giải thích:** `ab` thỏa $E_1$ nhưng bị Automaton từ chối ($S_0$ $\xrightarrow{a}$ $S_1$ $\xrightarrow{b}$ $S_2$ (TỪ CHỐI)). Ba chuỗi còn lại đều thuộc $L$.

**Câu 14.** Xét biểu thức $E_1 = (a+b)^* a (a+b)^*$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc ngôn ngữ mô tả bởi $E_1$**?
- A. Không có chuỗi nào
- B. `ba`
- C. `bab`
- D. `ab`
👉 **Đáp án đúng: A**
- **Giải thích:** Mọi chuỗi hợp lệ của Automaton đều thỏa $E_1$ ($L \subseteq L(E_1)$), nên **không có chuỗi nào** thuộc $L$ mà lại ngoài $L(E_1)$!

**Câu 15.** Xét biểu thức $E_2 = (a+b)^* a$ (chuỗi kết thúc bằng `a`). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_2)$**?
- A. `a`
- B. `aa`
- C. `ba`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Do $L(E_2) \subseteq L$ (và cả 3 chuỗi A, B, C đều thuộc $L$), nên không có chuỗi nào trong A, B, C thỏa điều kiện $\implies$ Chọn D.

**Câu 16.** Xét biểu thức $E_2 = (a+b)^* a$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_2)$**?
- A. `a`
- B. `abb`
- C. `aa`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `abb` thuộc $L$ ($S_0$ $\xrightarrow{a}$ $S_1$ $\xrightarrow{b}$ $S_2$ $\xrightarrow{b}$ $S_1$ (NHẬN)) nhưng không khớp khuôn mẫu của $E_2$. Còn `a` và `aa` đều thuộc cả $L$ lẫn $E_2$.

**Câu 17.** Xét biểu thức $E_2 = (a+b)^* a$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_2)$**?
- A. `a`
- B. `aa`
- C. `ba`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cả 3 chuỗi `a`, `aa`, `ba` đều đồng thời thuộc cả $L$ lẫn $E_2$ $\implies$ Chọn D (y hệt bẫy Câu 17 Sample 2!).

**Câu 18.** Xét biểu thức $E_3 = (a+b)^* aba (a+b)^*$ (chuỗi chứa cụm `aba`). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_3)$**?
- A. `aba`
- B. `aaba`
- C. `abaa`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Do $L(E_3) \subseteq L$, không có chuỗi nào trong A, B, C nằm ngoài $L$ $\implies$ Chọn D.

**Câu 19.** Xét biểu thức $E_3 = (a+b)^* aba (a+b)^*$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_3)$**?
- A. `aba`
- B. `a`
- C. `aaba`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `a` thuộc $L$ ($S_0$ $\xrightarrow{a}$ $S_1$ (NHẬN)) nhưng nằm ngoài $E_3$. Hai chuỗi còn lại thuộc cả $L$ và $E_3$.

**Câu 20.** Xét biểu thức $E_3 = (a+b)^* aba (a+b)^*$. Chuỗi nào **ĐỒNG THỜI KHÔNG** thuộc $L$ và **KHÔNG** thuộc $L(E_3)$?
- A. `a`
- B. `b`
- C. `abaa`
- D. `aba`
👉 **Đáp án đúng: B**
- **Giải thích:** `b` vừa không được Automaton chấp nhận vừa không thuộc $E_3$. Các chuỗi kia đều thuộc $L$ hoặc $E_3$ (hoặc cả hai).

**Câu 21.** Xét biểu thức $E_4 = a (a+b)^*$ (chuỗi bắt đầu bằng ký tự `a`). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_4)$**?
- A. `a`
- B. `aa`
- C. `ab`
- D. `ba`
👉 **Đáp án đúng: C**
- **Giải thích:** `ab` thuộc $L(E_4)$ nhưng bị Automaton từ chối ($S_0$ $\xrightarrow{a}$ $S_1$ $\xrightarrow{b}$ $S_2$ (TỪ CHỐI)). Ba chuỗi còn lại đều thuộc $L$.

**Câu 22.** Xét biểu thức $E_4 = a (a+b)^*$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_4)$**?
- A. `a`
- B. `ba`
- C. `aa`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `ba` thuộc $L$ ($S_0$ $\xrightarrow{b}$ $S_0$ $\xrightarrow{a}$ $S_1$ (NHẬN)) nhưng không khớp khuôn mẫu $E_4$.

**Câu 23.** Nếu áp dụng đơn định hóa Automaton đang quan tâm thì DFA đầy đủ thu được có bao nhiêu trạng thái?
- A. 3
- B. 4
- C. 5
- D. 6
👉 **Đáp án đúng: B**
- **Giải thích:** Áp dụng thuật toán xây dựng tập con (Subset Construction) thu được **4 trạng thái** (xem bảng bên dưới): *(Không xuất hiện trạng thái rỗng $\emptyset$, tất cả **4 trạng thái** đều đang hoạt động).*

| Trạng thái DFA | Tập con NFA | Đọc `a` | Đọc `b` | Kết thúc? |
| :---: | :---: | :---: | :---: | :---: |
| $S_0$ (Đầu) | $\{q0\}$ | $S_1$ | $S_0$ | Không |
| $S_1$ | $\{q0, q1\}$ | $S_1$ | $S_2$ | **CÓ** |
| $S_2$ | $\{q0, q2\}$ | $S_3$ | $S_1$ | Không |
| $S_3$ | $\{q0, q1, q2\}$ | $S_3$ | $S_3$ | **CÓ** |

**Câu 24.** DFA tối giản tương đương có bao nhiêu trạng thái?
- A. 3
- B. 4
- C. 5
- D. 6
👉 **Đáp án đúng: B**
- **Giải thích:** DFA thu được **đã tối giản** (**4 trạng thái**). Phân hoạch các nhóm trạng thái tương đương cuối cùng gồm **4 nhóm**: `{$S_3$}`, `{$S_1$}`, `{$S_2$}`, `{$S_0$}`.

---

## HÌNH 13 (`image_2.png`): DFA CHU TRÌNH `b` MODULO 3 ($(a + bbb)^*(b + bb)$)

> **THÔNG TIN ĐỀ BÀI GỐC (Hình 13 trong OnTapAutomata.docx - ảnh `image_2.png`):**
> - Tập trạng thái: $Q = \{q0, q1, q2\}$
> - Bảng chữ cái: $\Sigma = \{a, b\}$
> - Trạng thái bắt đầu: $q0$
> - Trạng thái kết thúc: $F = \{q1, q2\}$
> - Tính chất ban đầu: **Đơn định thiếu cung (Partial DFA - cần thêm trạng thái bẫy $\emptyset$ để thành DFA đầy đủ)**
> - Biểu thức chính quy tương đương: **$(a + bbb)^* (b + bb)$**
> - Ngôn ngữ đoán nhận: Các khối lặp lại từ $q_0$ gồm `a` hoặc `bbb`, cuối cùng kết thúc ở $q_1$ (đọc thêm `b`) hoặc $q_2$ (đọc thêm `bb`). *(Lưu ý cực kỳ quan trọng: tại $q_1$ và $q_2$ KHÔNG có cạnh đọc `a`, nên `bab` hay `bba` đều bị từ chối, còn `bbbab` hợp lệ!)*

```text
          a
        ┌───┐
        │   ▼
───► ( q0 ) ───── b ─────► ((( q1 )))
       ▲                      │
       │                      │ b
       │ b                    ▼
       └───────────────── ((( q2 )))
```

### Quy tắc vàng nhận diện trong 3 giây
1. **QUY TẮC 1:** Mọi chuỗi hợp lệ BẮT BUỘC phải **kết thúc bằng `b`**. Nếu kết thúc bằng `a` hoặc là $\varepsilon$ thì **LOẠI NGAY**!
2. **QUY TẮC 2:** Tại $q_1, q_2$ không có đường đọc `a`, nên mỗi khi rời $q_0$ bằng `b`, phải đi đủ 3 chữ `bbb` mới được quay về $q_0$ đọc `a` tiếp (nghĩa là không bao giờ có 1 chữ `b` hay 2 chữ `b` đứng kẹp trước `a`, như `bab`, `bba` đều bị loại!).
3. **QUY TẮC 3:** Số chữ `b` ở đoạn cuối (sau chữ `a` cuối cùng) chia 3 dư 1 hoặc 2 (không được chia hết cho 3 như `bbb`, `abbb`).

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
- **Giải thích:** $s_4 =$ `aba` bị từ chối ($S_0$ $\xrightarrow{a}$ $S_0$ $\xrightarrow{b}$ $S_1$ $\xrightarrow{a}$ $S_2$ (TỪ CHỐI)). Ba chuỗi còn lại đều hợp lệ.

**Câu 4.** Xét các chuỗi: $s_1 = \text{"aaab"}$, $s_2 = \text{"baa"}$, $s_3 = \text{"aabb"}$, $s_4 = \text{"bab"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_4$
- C. $s_1$ và $s_3$
- D. $s_1$ và $s_4$
👉 **Đáp án đúng: C**
- **Giải thích:** $s_1 =$ `aaab` và $s_3 =$ `aabb` hợp lệ; còn $s_2 =$ `baa` và $s_4 =$ `bab` không hợp lệ.

**Câu 5.** Xét các chuỗi: $s_1 = \text{"bbbba"}$, $s_2 = \text{"bbbbb"}$, $s_3 = \text{"bbbaa"}$, $s_4 = \text{"bbbab"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_4$
- C. $s_2$ và $s_3$
- D. $s_1$ và $s_4$
👉 **Đáp án đúng: B**
- **Giải thích:** $s_2 =$ `bbbbb` và $s_4 =$ `bbbab` đạt trạng thái kết thúc; $s_1, s_3$ bị từ chối.

**Câu 6.** Xét các chuỗi: $s_1 = \text{"bb"}$, $s_2 = \text{"aab"}$, $s_3 = \text{"abb"}$, $s_4 = \text{"aba"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Chỉ duy nhất $s_4 =$ `aba` bị từ chối ($S_0$ $\xrightarrow{a}$ $S_0$ $\xrightarrow{b}$ $S_1$ $\xrightarrow{a}$ $S_2$ (TỪ CHỐI)).

**Câu 7.** Xét các chuỗi: $s_1 = \text{"b"}$, $s_2 = \text{"a"}$, $s_3 = \text{"ab"}$, $s_4 = \text{"aa"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_2$
- B. $s_1$
- C. $s_3$
- D. Tất cả các chuỗi đều không hợp lệ.
👉 **Đáp án đúng: A**
- **Giải thích:** $s_1, s_3$ đều hợp lệ nên loại B, C, D. Chuỗi $s_2 =$ `a` không hợp lệ ($S_0$ $\xrightarrow{a}$ $S_0$ (TỪ CHỐI)). *(Lưu ý tương tự Câu 7 Sample 2: $s_4$ cũng không hợp lệ nhưng chỉ có $s_2$ xuất hiện trong 4 lựa chọn nên A là đáp án duy nhất)*.

**Câu 8.** Xét các chuỗi: $s_1 = \text{"aaab"}$, $s_2 = \text{"aabb"}$, $s_3 = \text{"bbbbb"}$, $s_4 = \text{"baa"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_3$
- C. $s_3$ và $s_4$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Duy nhất $s_4 =$ `baa` bị từ chối ($S_0$ $\xrightarrow{b}$ $S_1$ $\xrightarrow{a}$ $S_2$ $\xrightarrow{a}$ $S_2$ (TỪ CHỐI)).

**Câu 9.** Xét các chuỗi: $s_1 = \text{"aaab"}$, $s_2 = \text{"aabb"}$, $s_3 = \text{"bbbbb"}$, $s_4 = \text{"baa"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cả $s_1, s_2, s_3$ đều là chuỗi hợp lệ; chuỗi duy nhất không hợp lệ là $s_4 =$ `baa` không nằm trong A, B, C $\implies$ Chọn D.

**Câu 10.** Xét các chuỗi: $s_1 = \text{"aaab"}$, $s_2 = \text{"baa"}$, $s_3 = \text{"aabb"}$, $s_4 = \text{"bab"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$ và $s_4$
- B. $s_2$ và $s_3$
- C. $s_3$ và $s_4$
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cặp không hợp lệ đúng phải là $s_2$ và $s_4$ (`baa` và `bab`), không có trong A, B, C $\implies$ Chọn D.

**Câu 11.** Xét các chuỗi: $s_1 = \text{"bbbba"}$, $s_2 = \text{"bbbbb"}$, $s_3 = \text{"bbbaa"}$, $s_4 = \text{"bbbab"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1, s_2$ và $s_3$
- B. $s_1$ và $s_3$
- C. $s_4$
- D. $s_3$ và $s_4$
👉 **Đáp án đúng: B**
- **Giải thích:** $s_1 =$ `bbbba` và $s_3 =$ `bbbaa` đều không đạt trạng thái kết thúc.

**Câu 12.** Xét các chuỗi: $s_1 = \text{"bb"}$, $s_2 = \text{"aab"}$, $s_3 = \text{"abb"}$, $s_4 = \text{"ε"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Chuỗi rỗng $s_4 = \varepsilon$ KHÔNG được nhận vì tập trạng thái khởi đầu (sau bao đóng $\varepsilon$) không chứa trạng thái kết thúc.

**Câu 13.** Xét biểu thức chính quy $E_1 = (a+b)^* b$ (mọi chuỗi kết thúc bằng `b`). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc ngôn ngữ mô tả bởi $E_1$**?
- A. `b`
- B. `ab`
- C. `bab`
- D. `bb`
👉 **Đáp án đúng: C**
- **Giải thích:** `bab` thỏa $E_1$ nhưng bị Automaton từ chối ($S_0$ $\xrightarrow{b}$ $S_1$ $\xrightarrow{a}$ $S_2$ $\xrightarrow{b}$ $S_2$ (TỪ CHỐI)). Ba chuỗi còn lại đều thuộc $L$.

**Câu 14.** Xét biểu thức $E_1 = (a+b)^* b$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc ngôn ngữ mô tả bởi $E_1$**?
- A. Không có chuỗi nào
- B. `bb`
- C. `aba`
- D. `bab`
👉 **Đáp án đúng: A**
- **Giải thích:** Mọi chuỗi hợp lệ của Automaton đều thỏa $E_1$ ($L \subseteq L(E_1)$), nên **không có chuỗi nào** thuộc $L$ mà lại ngoài $L(E_1)$!

**Câu 15.** Xét biểu thức $E_2 = a^* (b + bb)$ (dãy `a` ở đầu kèm đuôi `b` hoặc `bb`). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_2)$**?
- A. `b`
- B. `ab`
- C. `bb`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Do $L(E_2) \subseteq L$ (và cả 3 chuỗi A, B, C đều thuộc $L$), nên không có chuỗi nào trong A, B, C thỏa điều kiện $\implies$ Chọn D.

**Câu 16.** Xét biểu thức $E_2 = a^* (b + bb)$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_2)$**?
- A. `b`
- B. `bbbb`
- C. `ab`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `bbbb` thuộc $L$ ($S_0$ $\xrightarrow{b}$ $S_1$ $\xrightarrow{b}$ $S_3$ $\xrightarrow{b}$ $S_0$ $\xrightarrow{b}$ $S_1$ (NHẬN)) nhưng không khớp khuôn mẫu của $E_2$. Còn `b` và `ab` đều thuộc cả $L$ lẫn $E_2$.

**Câu 17.** Xét biểu thức $E_2 = a^* (b + bb)$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_2)$**?
- A. `b`
- B. `ab`
- C. `bb`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cả 3 chuỗi `b`, `ab`, `bb` đều đồng thời thuộc cả $L$ lẫn $E_2$ $\implies$ Chọn D (y hệt bẫy Câu 17 Sample 2!).

**Câu 18.** Xét biểu thức $E_3 = a^* b^+$ (dãy `a` ở đầu theo sau bởi ít nhất 1 `b`). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_3)$**?
- A. `b`
- B. `bbb`
- C. `ab`
- D. `bb`
👉 **Đáp án đúng: B**
- **Giải thích:** `bbb` thuộc $E_3$ nhưng không được Automaton chấp nhận ($S_0$ $\xrightarrow{b}$ $S_1$ $\xrightarrow{b}$ $S_3$ $\xrightarrow{b}$ $S_0$ (TỪ CHỐI)). Các chuỗi kia đều thuộc $L$.

**Câu 19.** Xét biểu thức $E_3 = a^* b^+$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_3)$**?
- A. `b`
- B. `bbbab`
- C. `ab`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `bbbab` thuộc $L$ ($S_0$ $\xrightarrow{b}$ $S_1$ $\xrightarrow{b}$ $S_3$ $\xrightarrow{b}$ $S_0$ $\xrightarrow{a}$ $S_0$ $\xrightarrow{b}$ $S_1$ (NHẬN)) nhưng nằm ngoài $E_3$. Hai chuỗi còn lại thuộc cả $L$ và $E_3$.

**Câu 20.** Xét biểu thức $E_3 = a^* b^+$. Chuỗi nào **ĐỒNG THỜI KHÔNG** thuộc $L$ và **KHÔNG** thuộc $L(E_3)$?
- A. `bbbab`
- B. `a`
- C. `bbb`
- D. `b`
👉 **Đáp án đúng: B**
- **Giải thích:** `a` vừa không được Automaton chấp nhận vừa không thuộc $E_3$. Các chuỗi kia đều thuộc $L$ hoặc $E_3$ (hoặc cả hai).

**Câu 21.** Xét biểu thức $E_4 = (a+b)^* bb$ (kết thúc bằng `bb`). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_4)$**?
- A. `b`
- B. `ab`
- C. `bbb`
- D. `bb`
👉 **Đáp án đúng: C**
- **Giải thích:** `bbb` thuộc $L(E_4)$ nhưng bị Automaton từ chối ($S_0$ $\xrightarrow{b}$ $S_1$ $\xrightarrow{b}$ $S_3$ $\xrightarrow{b}$ $S_0$ (TỪ CHỐI)). Ba chuỗi còn lại đều thuộc $L$.

**Câu 22.** Xét biểu thức $E_4 = (a+b)^* bb$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_4)$**?
- A. `bb`
- B. `b`
- C. `abb`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `b` thuộc $L$ ($S_0$ $\xrightarrow{b}$ $S_1$ (NHẬN)) nhưng không khớp khuôn mẫu $E_4$.

**Câu 23.** Nếu áp dụng đơn định hóa Automaton đang quan tâm thì DFA đầy đủ thu được có bao nhiêu trạng thái?
- A. 3
- B. 4
- C. 5
- D. 6
👉 **Đáp án đúng: B**
- **Giải thích:** Áp dụng thuật toán xây dựng tập con (Subset Construction) thu được **4 trạng thái** (xem bảng bên dưới): *(Lưu ý: Sơ đồ có xuất hiện tập con rỗng $\emptyset$ làm trạng thái bẫy chết. Nếu một số đề không vẽ trạng thái bẫy này thì còn **3 trạng thái**; theo chuẩn hàm chuyển toàn phần trong Sample 2 của IUH thì tính đủ **4 trạng thái**).*

| Trạng thái DFA | Tập con NFA | Đọc `a` | Đọc `b` | Kết thúc? |
| :---: | :---: | :---: | :---: | :---: |
| $S_0$ (Đầu) | $\{q0\}$ | $S_0$ | $S_1$ | Không |
| $S_1$ | $\{q1\}$ | $S_2$ | $S_3$ | **CÓ** |
| $S_2$ (Bẫy) | $\emptyset$ | $S_2$ | $S_2$ | Không |
| $S_3$ | $\{q2\}$ | $S_2$ | $S_0$ | **CÓ** |

**Câu 24.** DFA tối giản tương đương có bao nhiêu trạng thái?
- A. 3
- B. 4
- C. 5
- D. 6
👉 **Đáp án đúng: B**
- **Giải thích:** DFA thu được **đã tối giản** (**4 trạng thái**). Phân hoạch các nhóm trạng thái tương đương cuối cùng gồm **4 nhóm**: `{$S_3$}`, `{$S_1$}`, `{$S_2$}`, `{$S_0$}`. *(Nếu bỏ trạng thái bẫy chết khỏi đồ thị thì còn **3 trạng thái**; tính đủ hàm toàn phần như Sample 2 là **4 trạng thái**).*

---

## HÌNH 14 (`image_11.png`): $\varepsilon$-NFA BIẾN THỂ SINH ĐÔI CỦA SAMPLE 2

> **THÔNG TIN ĐỀ BÀI GỐC (Hình 14 trong OnTapAutomata.docx - ảnh `image_11.png`):**
> - Tập trạng thái: $Q = \{q0, q1, q2\}$
> - Bảng chữ cái: $\Sigma = \{a, b\}$
> - Trạng thái bắt đầu: $q0$
> - Trạng thái kết thúc: $F = \{q2\}$
> - Tính chất ban đầu: **Không đơn định có chuyển rỗng ($\varepsilon$-NFA)**
> - Biểu thức chính quy tương đương: **$a^* b (bb)^* (a a^* b (bb)^*)^*$**
> - Ngôn ngữ đoán nhận: Chuỗi kết thúc bằng số lẻ chữ `b` ($b, bbb, \dots$), sau các đoạn toàn `a`, và không bao giờ có chữ `a` đứng ngay sau số chẵn chữ `b` (như `bba` bị loại!).

```text
                  a
                ┌───┐
                │   ▼
  Bắt đầu ───► ( q0 ) ───── a, ε ─────► ( q1 )
                 ▲                      ▲    │
                 │ a                    │    │ b
                 │                 b    │    ▼
               ((( q2 ))) ──────────────┘    │
                    ▲                        │
                    └────────────────────────┘
```

### Quy tắc vàng nhận diện trong 3 giây
1. **QUY TẮC 1:** Mũi tên duy nhất vào đích $q_2$ là nhãn `b` $\implies$ **Mọi chuỗi hợp lệ PHẢI KẾT THÚC BẰNG `b`!** (Kết thúc bằng `a` hoặc $\varepsilon$ là LOẠI!).
2. **QUY TẮC 2:** Đếm số chữ `b` ở đoạn cuối (từ sau chữ `a` cuối cùng) PHẢI LÀ **SỐ LẺ** (`b`, `bbb`, `ab`, `abbb` nhận; còn `bb`, `aabb` ở $q_1$ bị loại!).
3. **QUY TẮC 3:** Khi đang ở $q_1$ (vừa đọc chẵn chữ `b`), không có đường cho `a` $\implies$ **CẤM cụm `bba` hay `bbbba`**! (Ví dụ `bbab` bị loại!).

### Bộ 24 câu trắc nghiệm chuẩn Đề Mẫu Sample 2

**Câu 1.** Xét các chuỗi: $s_1 = \text{"b"}$, $s_2 = \text{"a"}$, $s_3 = \text{"aa"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Tất cả các chuỗi được nêu.
👉 **Đáp án đúng: A**
- **Giải thích:** `b` hợp lệ ($S_0$ $\xrightarrow{b}$ $S_1$ (NHẬN)). Còn `a` và `aa` không về được trạng thái kết thúc.

**Câu 2.** Xét các chuỗi: $s_1 = \text{"ba"}$, $s_2 = \text{"bb"}$, $s_3 = \text{"ab"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Các chọn lựa khác đều ĐÚNG.
👉 **Đáp án đúng: C**
- **Giải thích:** Chỉ có $s_3 =$ `ab` hợp lệ ($S_0$ $\xrightarrow{a}$ $S_0$ $\xrightarrow{b}$ $S_1$ (NHẬN)). Hai chuỗi $s_1, s_2$ bị từ chối.

**Câu 3.** Xét các chuỗi: $s_1 = \text{"aab"}$, $s_2 = \text{"bab"}$, $s_3 = \text{"bbb"}$, $s_4 = \text{"aaa"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1, s_2$ và $s_3$
- B. $s_2, s_3$ và $s_4$
- C. $s_3$ và $s_4$
- D. $s_4$
👉 **Đáp án đúng: A**
- **Giải thích:** $s_4 =$ `aaa` bị từ chối ($S_0$ $\xrightarrow{a}$ $S_0$ $\xrightarrow{a}$ $S_0$ $\xrightarrow{a}$ $S_0$ (TỪ CHỐI)). Ba chuỗi còn lại đều hợp lệ.

**Câu 4.** Xét các chuỗi: $s_1 = \text{"aaab"}$, $s_2 = \text{"aba"}$, $s_3 = \text{"abab"}$, $s_4 = \text{"abb"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_4$
- C. $s_1$ và $s_3$
- D. $s_1$ và $s_4$
👉 **Đáp án đúng: C**
- **Giải thích:** $s_1 =$ `aaab` và $s_3 =$ `abab` hợp lệ; còn $s_2 =$ `aba` và $s_4 =$ `abb` không hợp lệ.

**Câu 5.** Xét các chuỗi: $s_1 = \text{"bbbba"}$, $s_2 = \text{"bbbbb"}$, $s_3 = \text{"bbbaa"}$, $s_4 = \text{"bbbab"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_4$
- C. $s_2$ và $s_3$
- D. $s_1$ và $s_4$
👉 **Đáp án đúng: B**
- **Giải thích:** $s_2 =$ `bbbbb` và $s_4 =$ `bbbab` đạt trạng thái kết thúc; $s_1, s_3$ bị từ chối.

**Câu 6.** Xét các chuỗi: $s_1 = \text{"aab"}$, $s_2 = \text{"bab"}$, $s_3 = \text{"bbb"}$, $s_4 = \text{"aaa"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Chỉ duy nhất $s_4 =$ `aaa` bị từ chối ($S_0$ $\xrightarrow{a}$ $S_0$ $\xrightarrow{a}$ $S_0$ $\xrightarrow{a}$ $S_0$ (TỪ CHỐI)).

**Câu 7.** Xét các chuỗi: $s_1 = \text{"b"}$, $s_2 = \text{"a"}$, $s_3 = \text{"ab"}$, $s_4 = \text{"aa"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_2$
- B. $s_1$
- C. $s_3$
- D. Tất cả các chuỗi đều không hợp lệ.
👉 **Đáp án đúng: A**
- **Giải thích:** $s_1, s_3$ đều hợp lệ nên loại B, C, D. Chuỗi $s_2 =$ `a` không hợp lệ ($S_0$ $\xrightarrow{a}$ $S_0$ (TỪ CHỐI)). *(Lưu ý tương tự Câu 7 Sample 2: $s_4$ cũng không hợp lệ nhưng chỉ có $s_2$ xuất hiện trong 4 lựa chọn nên A là đáp án duy nhất)*.

**Câu 8.** Xét các chuỗi: $s_1 = \text{"aaab"}$, $s_2 = \text{"abab"}$, $s_3 = \text{"bbbbb"}$, $s_4 = \text{"aba"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_3$
- C. $s_3$ và $s_4$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Duy nhất $s_4 =$ `aba` bị từ chối ($S_0$ $\xrightarrow{a}$ $S_0$ $\xrightarrow{b}$ $S_1$ $\xrightarrow{a}$ $S_0$ (TỪ CHỐI)).

**Câu 9.** Xét các chuỗi: $s_1 = \text{"aaab"}$, $s_2 = \text{"abab"}$, $s_3 = \text{"bbbbb"}$, $s_4 = \text{"aba"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cả $s_1, s_2, s_3$ đều là chuỗi hợp lệ; chuỗi duy nhất không hợp lệ là $s_4 =$ `aba` không nằm trong A, B, C $\implies$ Chọn D.

**Câu 10.** Xét các chuỗi: $s_1 = \text{"aaab"}$, $s_2 = \text{"aba"}$, $s_3 = \text{"abab"}$, $s_4 = \text{"abb"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$ và $s_4$
- B. $s_2$ và $s_3$
- C. $s_3$ và $s_4$
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cặp không hợp lệ đúng phải là $s_2$ và $s_4$ (`aba` và `abb`), không có trong A, B, C $\implies$ Chọn D.

**Câu 11.** Xét các chuỗi: $s_1 = \text{"bbbba"}$, $s_2 = \text{"bbbbb"}$, $s_3 = \text{"bbbaa"}$, $s_4 = \text{"bbbab"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1, s_2$ và $s_3$
- B. $s_1$ và $s_3$
- C. $s_4$
- D. $s_3$ và $s_4$
👉 **Đáp án đúng: B**
- **Giải thích:** $s_1 =$ `bbbba` và $s_3 =$ `bbbaa` đều không đạt trạng thái kết thúc.

**Câu 12.** Xét các chuỗi: $s_1 = \text{"aab"}$, $s_2 = \text{"bab"}$, $s_3 = \text{"bbb"}$, $s_4 = \text{"ε"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Chuỗi rỗng $s_4 = \varepsilon$ KHÔNG được nhận vì tập trạng thái khởi đầu (sau bao đóng $\varepsilon$) không chứa trạng thái kết thúc.

**Câu 13.** Xét biểu thức chính quy $E_1 = (a+b)^* b$ (mọi chuỗi kết thúc bằng `b`). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc ngôn ngữ mô tả bởi $E_1$**?
- A. `b`
- B. `ab`
- C. `bb`
- D. `aab`
👉 **Đáp án đúng: C**
- **Giải thích:** `bb` thỏa $E_1$ nhưng bị Automaton từ chối ($S_0$ $\xrightarrow{b}$ $S_1$ $\xrightarrow{b}$ $S_2$ (TỪ CHỐI)). Ba chuỗi còn lại đều thuộc $L$.

**Câu 14.** Xét biểu thức $E_1 = (a+b)^* b$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc ngôn ngữ mô tả bởi $E_1$**?
- A. Không có chuỗi nào
- B. `aab`
- C. `aaa`
- D. `bb`
👉 **Đáp án đúng: A**
- **Giải thích:** Mọi chuỗi hợp lệ của Automaton đều thỏa $E_1$ ($L \subseteq L(E_1)$), nên **không có chuỗi nào** thuộc $L$ mà lại ngoài $L(E_1)$!

**Câu 15.** Xét biểu thức $E_2 = a^* b (bb)^*$ (dãy `a*` theo sau bởi số lẻ chữ `b`). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_2)$**?
- A. `b`
- B. `ab`
- C. `aab`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Do $L(E_2) \subseteq L$ (và cả 3 chuỗi A, B, C đều thuộc $L$), nên không có chuỗi nào trong A, B, C thỏa điều kiện $\implies$ Chọn D.

**Câu 16.** Xét biểu thức $E_2 = a^* b (bb)^*$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_2)$**?
- A. `b`
- B. `bab`
- C. `ab`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `bab` thuộc $L$ ($S_0$ $\xrightarrow{b}$ $S_1$ $\xrightarrow{a}$ $S_0$ $\xrightarrow{b}$ $S_1$ (NHẬN)) nhưng không khớp khuôn mẫu của $E_2$. Còn `b` và `ab` đều thuộc cả $L$ lẫn $E_2$.

**Câu 17.** Xét biểu thức $E_2 = a^* b (bb)^*$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_2)$**?
- A. `b`
- B. `ab`
- C. `aab`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cả 3 chuỗi `b`, `ab`, `aab` đều đồng thời thuộc cả $L$ lẫn $E_2$ $\implies$ Chọn D (y hệt bẫy Câu 17 Sample 2!).

**Câu 18.** Xét biểu thức $E_3 = (a+b)^* ab$ (mọi chuỗi kết thúc bằng `ab`). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_3)$**?
- A. `b`
- B. `bbab`
- C. `ab`
- D. `aab`
👉 **Đáp án đúng: B**
- **Giải thích:** `bbab` thuộc $E_3$ nhưng không được Automaton chấp nhận ($S_0$ $\xrightarrow{b}$ $S_1$ $\xrightarrow{b}$ $S_2$ $\xrightarrow{a}$ $S_3$ $\xrightarrow{b}$ $S_3$ (TỪ CHỐI)). Các chuỗi kia đều thuộc $L$.

**Câu 19.** Xét biểu thức $E_3 = (a+b)^* ab$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_3)$**?
- A. `ab`
- B. `b`
- C. `aab`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `b` thuộc $L$ ($S_0$ $\xrightarrow{b}$ $S_1$ (NHẬN)) nhưng nằm ngoài $E_3$. Hai chuỗi còn lại thuộc cả $L$ và $E_3$.

**Câu 20.** Xét biểu thức $E_3 = (a+b)^* ab$. Chuỗi nào **ĐỒNG THỜI KHÔNG** thuộc $L$ và **KHÔNG** thuộc $L(E_3)$?
- A. `b`
- B. `a`
- C. `bbab`
- D. `ab`
👉 **Đáp án đúng: B**
- **Giải thích:** `a` vừa không được Automaton chấp nhận vừa không thuộc $E_3$. Các chuỗi kia đều thuộc $L$ hoặc $E_3$ (hoặc cả hai).

**Câu 21.** Xét biểu thức $E_4 = (a+b)^* bb$ (chuỗi kết thúc bằng hai chữ `b` liên tiếp (`bb`)). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_4)$**?
- A. `b`
- B. `ab`
- C. `bb`
- D. `aab`
👉 **Đáp án đúng: C**
- **Giải thích:** `bb` thuộc $L(E_4)$ nhưng bị Automaton từ chối ($S_0$ $\xrightarrow{b}$ $S_1$ $\xrightarrow{b}$ $S_2$ (TỪ CHỐI)). Ba chuỗi còn lại đều thuộc $L$.

**Câu 22.** Xét biểu thức $E_4 = (a+b)^* bb$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_4)$**?
- A. `bbb`
- B. `b`
- C. `abbb`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `b` thuộc $L$ ($S_0$ $\xrightarrow{b}$ $S_1$ (NHẬN)) nhưng không khớp khuôn mẫu $E_4$.

**Câu 23.** Nếu áp dụng đơn định hóa Automaton đang quan tâm thì DFA đầy đủ thu được có bao nhiêu trạng thái?
- A. 3
- B. 4
- C. 5
- D. 6
👉 **Đáp án đúng: B**
- **Giải thích:** Áp dụng thuật toán xây dựng tập con (Subset Construction) thu được **4 trạng thái** (xem bảng bên dưới): *(Lưu ý: Sơ đồ có xuất hiện tập con rỗng $\emptyset$ làm trạng thái bẫy chết. Nếu một số đề không vẽ trạng thái bẫy này thì còn **3 trạng thái**; theo chuẩn hàm chuyển toàn phần trong Sample 2 của IUH thì tính đủ **4 trạng thái**).*

| Trạng thái DFA | Tập con NFA | Đọc `a` | Đọc `b` | Kết thúc? |
| :---: | :---: | :---: | :---: | :---: |
| $S_0$ (Đầu) | $\{q0, q1\}$ | $S_0$ | $S_1$ | Không |
| $S_1$ | $\{q2\}$ | $S_0$ | $S_2$ | **CÓ** |
| $S_2$ | $\{q1\}$ | $S_3$ | $S_1$ | Không |
| $S_3$ (Bẫy) | $\emptyset$ | $S_3$ | $S_3$ | Không |

**Câu 24.** DFA tối giản tương đương có bao nhiêu trạng thái?
- A. 3
- B. 4
- C. 5
- D. 6
👉 **Đáp án đúng: B**
- **Giải thích:** DFA thu được **đã tối giản** (**4 trạng thái**). Phân hoạch các nhóm trạng thái tương đương cuối cùng gồm **4 nhóm**: `{$S_1$}`, `{$S_3$}`, `{$S_2$}`, `{$S_0$}`. *(Nếu bỏ trạng thái bẫy chết khỏi đồ thị thì còn **3 trạng thái**; tính đủ hàm toàn phần như Sample 2 là **4 trạng thái**).*

---
