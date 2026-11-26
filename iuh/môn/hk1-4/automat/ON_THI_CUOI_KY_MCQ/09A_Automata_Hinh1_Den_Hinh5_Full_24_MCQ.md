# BỘ ĐỀ AUTOMATA PHẦN 1: HÌNH 1 ĐẾN HÌNH 5 (120 CÂU CHUẨN ĐỀ MẪU SAMPLE 2)
## ĐÚNG THỨ TỰ TRONG ONTAPAUTOMATA.DOCX - MỖI HÌNH FULL 24 CÂU + BẢNG SUBSET & TỐI GIẢN

> Bao gồm: **Hình 1** (`image_7.png`), **Hình 2** (`image_3.png`), **Hình 3** (`image_0.png`), **Hình 4** (`image_12.jpg`), **Hình 5** (`image_10.png`).

---

## HÌNH 1 (`image_7.png`): NFA CHỨA CHUỖI CON `00` HOẶC `11`

> **THÔNG TIN ĐỀ BÀI GỐC (Hình 1 trong OnTapAutomata.docx - ảnh `image_7.png`):**
> - Tập trạng thái: $Q = \{q0, q1, q2, q3, q4\}$
> - Bảng chữ cái: $\Sigma = \{0, 1\}$
> - Trạng thái bắt đầu: $q0$
> - Trạng thái kết thúc: $F = \{q2, q4\}$
> - Tính chất ban đầu: **Không đơn định (NFA)**
> - Biểu thức chính quy tương đương: **$(0+1)^* (00 + 11) (0+1)^*$**
> - Ngôn ngữ đoán nhận: Tập hợp mọi chuỗi nhị phân chứa ít nhất một cặp ký tự giống nhau đứng cạnh nhau (`00` hoặc `11`).

```text
      0, 1
     ┌────┐
     │    ▼          1              1          0, 1 (vòng)
───► ( q0 ) ───────────► ( q1 ) ────────► ((( q2 ))) ──┐◄─┘
       │
       │ 0               0          0, 1 (vòng)
       ▼
     ( q3 ) ───────────► ((( q4 ))) ──┐◄─┘
```

### Quy tắc vàng nhận diện trong 3 giây
1. **QUY TẮC 1:** Chuỗi hợp lệ BẮT BUỘC phải chứa ít nhất một cụm **`00`** hoặc **`11`**.
2. **QUY TẮC 2:** Mọi chuỗi chỉ gồm `0` và `1` xen kẽ hoàn toàn (`0101...`, `1010...`) hoặc độ dài $< 2$ đều **BỊ TỪ CHỐI**!

### Bộ 24 câu trắc nghiệm chuẩn Đề Mẫu Sample 2

**Câu 1.** Xét các chuỗi: $s_1 = \text{"00"}$, $s_2 = \text{"0"}$, $s_3 = \text{"1"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Tất cả các chuỗi được nêu.
👉 **Đáp án đúng: A**
- **Giải thích:** `00` hợp lệ ($S_0$ $\xrightarrow{0}$ $S_1$ $\xrightarrow{0}$ $S_3$ (NHẬN)). Còn `0` và `1` không về được trạng thái kết thúc.

**Câu 2.** Xét các chuỗi: $s_1 = \text{"01"}$, $s_2 = \text{"10"}$, $s_3 = \text{"11"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Các chọn lựa khác đều ĐÚNG.
👉 **Đáp án đúng: C**
- **Giải thích:** Chỉ có $s_3 =$ `11` hợp lệ ($S_0$ $\xrightarrow{1}$ $S_2$ $\xrightarrow{1}$ $S_4$ (NHẬN)). Hai chuỗi $s_1, s_2$ bị từ chối.

**Câu 3.** Xét các chuỗi: $s_1 = \text{"000"}$, $s_2 = \text{"001"}$, $s_3 = \text{"011"}$, $s_4 = \text{"010"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1, s_2$ và $s_3$
- B. $s_2, s_3$ và $s_4$
- C. $s_3$ và $s_4$
- D. $s_4$
👉 **Đáp án đúng: A**
- **Giải thích:** $s_4 =$ `010` bị từ chối ($S_0$ $\xrightarrow{0}$ $S_1$ $\xrightarrow{1}$ $S_2$ $\xrightarrow{0}$ $S_1$ (TỪ CHỐI)). Ba chuỗi còn lại đều hợp lệ.

**Câu 4.** Xét các chuỗi: $s_1 = \text{"100"}$, $s_2 = \text{"101"}$, $s_3 = \text{"110"}$, $s_4 = \text{"0101"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_4$
- C. $s_1$ và $s_3$
- D. $s_1$ và $s_4$
👉 **Đáp án đúng: C**
- **Giải thích:** $s_1 =$ `100` và $s_3 =$ `110` hợp lệ; còn $s_2 =$ `101` và $s_4 =$ `0101` không hợp lệ.

**Câu 5.** Xét các chuỗi: $s_1 = \text{"10101"}$, $s_2 = \text{"11111"}$, $s_3 = \text{"01010"}$, $s_4 = \text{"11110"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_4$
- C. $s_2$ và $s_3$
- D. $s_1$ và $s_4$
👉 **Đáp án đúng: B**
- **Giải thích:** $s_2 =$ `11111` và $s_4 =$ `11110` đạt trạng thái kết thúc; $s_1, s_3$ bị từ chối.

**Câu 6.** Xét các chuỗi: $s_1 = \text{"000"}$, $s_2 = \text{"001"}$, $s_3 = \text{"011"}$, $s_4 = \text{"010"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Chỉ duy nhất $s_4 =$ `010` bị từ chối ($S_0$ $\xrightarrow{0}$ $S_1$ $\xrightarrow{1}$ $S_2$ $\xrightarrow{0}$ $S_1$ (TỪ CHỐI)).

**Câu 7.** Xét các chuỗi: $s_1 = \text{"00"}$, $s_2 = \text{"0"}$, $s_3 = \text{"11"}$, $s_4 = \text{"1"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_2$
- B. $s_1$
- C. $s_3$
- D. Tất cả các chuỗi đều không hợp lệ.
👉 **Đáp án đúng: A**
- **Giải thích:** $s_1, s_3$ đều hợp lệ nên loại B, C, D. Chuỗi $s_2 =$ `0` không hợp lệ ($S_0$ $\xrightarrow{0}$ $S_1$ (TỪ CHỐI)). *(Lưu ý tương tự Câu 7 Sample 2: $s_4$ cũng không hợp lệ nhưng chỉ có $s_2$ xuất hiện trong 4 lựa chọn nên A là đáp án duy nhất)*.

**Câu 8.** Xét các chuỗi: $s_1 = \text{"100"}$, $s_2 = \text{"110"}$, $s_3 = \text{"11111"}$, $s_4 = \text{"101"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_3$
- C. $s_3$ và $s_4$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Duy nhất $s_4 =$ `101` bị từ chối ($S_0$ $\xrightarrow{1}$ $S_2$ $\xrightarrow{0}$ $S_1$ $\xrightarrow{1}$ $S_2$ (TỪ CHỐI)).

**Câu 9.** Xét các chuỗi: $s_1 = \text{"100"}$, $s_2 = \text{"110"}$, $s_3 = \text{"11111"}$, $s_4 = \text{"101"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cả $s_1, s_2, s_3$ đều là chuỗi hợp lệ; chuỗi duy nhất không hợp lệ là $s_4 =$ `101` không nằm trong A, B, C $\implies$ Chọn D.

**Câu 10.** Xét các chuỗi: $s_1 = \text{"100"}$, $s_2 = \text{"101"}$, $s_3 = \text{"110"}$, $s_4 = \text{"0101"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$ và $s_4$
- B. $s_2$ và $s_3$
- C. $s_3$ và $s_4$
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cặp không hợp lệ đúng phải là $s_2$ và $s_4$ (`101` và `0101`), không có trong A, B, C $\implies$ Chọn D.

**Câu 11.** Xét các chuỗi: $s_1 = \text{"10101"}$, $s_2 = \text{"11111"}$, $s_3 = \text{"01010"}$, $s_4 = \text{"11110"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1, s_2$ và $s_3$
- B. $s_1$ và $s_3$
- C. $s_4$
- D. $s_3$ và $s_4$
👉 **Đáp án đúng: B**
- **Giải thích:** $s_1 =$ `10101` và $s_3 =$ `01010` đều không đạt trạng thái kết thúc.

**Câu 12.** Xét các chuỗi: $s_1 = \text{"000"}$, $s_2 = \text{"001"}$, $s_3 = \text{"011"}$, $s_4 = \text{"ε"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Chuỗi rỗng $s_4 = \varepsilon$ KHÔNG được nhận vì tập trạng thái khởi đầu (sau bao đóng $\varepsilon$) không chứa trạng thái kết thúc.

**Câu 13.** Xét biểu thức chính quy $E_1 = (0+1)^+ (0+1)^+$ (chuỗi độ dài $\ge 2$ trên $\{0, 1\}$). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc ngôn ngữ mô tả bởi $E_1$**?
- A. `00`
- B. `11`
- C. `01`
- D. `000`
👉 **Đáp án đúng: C**
- **Giải thích:** `01` thỏa $E_1$ nhưng bị Automaton từ chối ($S_0$ $\xrightarrow{0}$ $S_1$ $\xrightarrow{1}$ $S_2$ (TỪ CHỐI)). Ba chuỗi còn lại đều thuộc $L$.

**Câu 14.** Xét biểu thức $E_1 = (0+1)^+ (0+1)^+$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc ngôn ngữ mô tả bởi $E_1$**?
- A. Không có chuỗi nào
- B. `000`
- C. `010`
- D. `01`
👉 **Đáp án đúng: A**
- **Giải thích:** Mọi chuỗi hợp lệ của Automaton đều thỏa $E_1$ ($L \subseteq L(E_1)$), nên **không có chuỗi nào** thuộc $L$ mà lại ngoài $L(E_1)$!

**Câu 15.** Xét biểu thức $E_2 = (0+1)^* 00 (0+1)^*$ (chuỗi chứa cụm `00`). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_2)$**?
- A. `00`
- B. `000`
- C. `001`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Do $L(E_2) \subseteq L$ (và cả 3 chuỗi A, B, C đều thuộc $L$), nên không có chuỗi nào trong A, B, C thỏa điều kiện $\implies$ Chọn D.

**Câu 16.** Xét biểu thức $E_2 = (0+1)^* 00 (0+1)^*$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_2)$**?
- A. `00`
- B. `11`
- C. `000`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `11` thuộc $L$ ($S_0$ $\xrightarrow{1}$ $S_2$ $\xrightarrow{1}$ $S_4$ (NHẬN)) nhưng không khớp khuôn mẫu của $E_2$. Còn `00` và `000` đều thuộc cả $L$ lẫn $E_2$.

**Câu 17.** Xét biểu thức $E_2 = (0+1)^* 00 (0+1)^*$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_2)$**?
- A. `00`
- B. `000`
- C. `001`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cả 3 chuỗi `00`, `000`, `001` đều đồng thời thuộc cả $L$ lẫn $E_2$ $\implies$ Chọn D (y hệt bẫy Câu 17 Sample 2!).

**Câu 18.** Xét biểu thức $E_3 = (0+1)^* 11$ (chuỗi kết thúc bằng `11`). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_3)$**?
- A. `11`
- B. `011`
- C. `111`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Do $L(E_3) \subseteq L$, không có chuỗi nào trong A, B, C nằm ngoài $L$ $\implies$ Chọn D.

**Câu 19.** Xét biểu thức $E_3 = (0+1)^* 11$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_3)$**?
- A. `11`
- B. `00`
- C. `011`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `00` thuộc $L$ ($S_0$ $\xrightarrow{0}$ $S_1$ $\xrightarrow{0}$ $S_3$ (NHẬN)) nhưng nằm ngoài $E_3$. Hai chuỗi còn lại thuộc cả $L$ và $E_3$.

**Câu 20.** Xét biểu thức $E_3 = (0+1)^* 11$. Chuỗi nào **ĐỒNG THỜI KHÔNG** thuộc $L$ và **KHÔNG** thuộc $L(E_3)$?
- A. `00`
- B. `0`
- C. `111`
- D. `11`
👉 **Đáp án đúng: B**
- **Giải thích:** `0` vừa không được Automaton chấp nhận vừa không thuộc $E_3$. Các chuỗi kia đều thuộc $L$ hoặc $E_3$ (hoặc cả hai).

**Câu 21.** Xét biểu thức $E_4 = (0+1)^* 00 (0+1)^* + 1^*$ (chuỗi chứa `00` hoặc chỉ gồm toàn số `1`). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_4)$**?
- A. `00`
- B. `11`
- C. $\varepsilon$
- D. `000`
👉 **Đáp án đúng: C**
- **Giải thích:** $\varepsilon$ thuộc $L(E_4)$ nhưng bị Automaton từ chối ($S_0$ (TỪ CHỐI)). Ba chuỗi còn lại đều thuộc $L$.

**Câu 22.** Xét biểu thức $E_4 = (0+1)^* 00 (0+1)^* + 1^*$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_4)$**?
- A. `00`
- B. `011`
- C. `11`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `011` thuộc $L$ ($S_0$ $\xrightarrow{0}$ $S_1$ $\xrightarrow{1}$ $S_2$ $\xrightarrow{1}$ $S_4$ (NHẬN)) nhưng không khớp khuôn mẫu $E_4$.

**Câu 23.** Nếu áp dụng đơn định hóa Automaton đang quan tâm thì DFA đầy đủ thu được có bao nhiêu trạng thái?
- A. 8
- B. 9
- C. 10
- D. 11
👉 **Đáp án đúng: B**
- **Giải thích:** Áp dụng thuật toán xây dựng tập con (Subset Construction) thu được **9 trạng thái** (xem bảng bên dưới): *(Không xuất hiện trạng thái rỗng $\emptyset$, tất cả **9 trạng thái** đều đang hoạt động).*

| Trạng thái DFA | Tập con NFA | Đọc `0` | Đọc `1` | Kết thúc? |
| :---: | :---: | :---: | :---: | :---: |
| $S_0$ (Đầu) | $\{q0\}$ | $S_1$ | $S_2$ | Không |
| $S_1$ | $\{q0, q3\}$ | $S_3$ | $S_2$ | Không |
| $S_2$ | $\{q0, q1\}$ | $S_1$ | $S_4$ | Không |
| $S_3$ | $\{q0, q3, q4\}$ | $S_3$ | $S_5$ | **CÓ** |
| $S_4$ | $\{q0, q1, q2\}$ | $S_6$ | $S_4$ | **CÓ** |
| $S_5$ | $\{q0, q1, q4\}$ | $S_3$ | $S_7$ | **CÓ** |
| $S_6$ | $\{q0, q2, q3\}$ | $S_8$ | $S_4$ | **CÓ** |
| $S_7$ | $\{q0, q1, q2, q4\}$ | $S_8$ | $S_7$ | **CÓ** |
| $S_8$ | $\{q0, q2, q3, q4\}$ | $S_8$ | $S_7$ | **CÓ** |

**Câu 24.** DFA tối giản tương đương có bao nhiêu trạng thái?
- A. 3
- B. 4
- C. 5
- D. 6
👉 **Đáp án đúng: B**
- **Giải thích:** Có thể gộp từ **9** trạng thái xuống còn **4** trạng thái tương đương. Phân hoạch các nhóm trạng thái tương đương cuối cùng gồm **4 nhóm**: `{$S_3$, $S_4$, $S_5$, $S_6$, $S_7$, $S_8$}`, `{$S_1$}`, `{$S_0$}`, `{$S_2$}`.

---

## HÌNH 2 (`image_3.png`): $\varepsilon$-NFA CHỨA CHUỖI CON `11` HOẶC `101`

> **THÔNG TIN ĐỀ BÀI GỐC (Hình 2 trong OnTapAutomata.docx - ảnh `image_3.png`):**
> - Tập trạng thái: $Q = \{q0, q1, q2, q3\}$
> - Bảng chữ cái: $\Sigma = \{0, 1\}$
> - Trạng thái bắt đầu: $q0$
> - Trạng thái kết thúc: $F = \{q3\}$
> - Tính chất ban đầu: **Không đơn định có chuyển rỗng ($\varepsilon$-NFA)**
> - Biểu thức chính quy tương đương: **$(0+1)^* 1(0+\varepsilon)1 (0+1)^*$**
> - Ngôn ngữ đoán nhận: Tập hợp mọi chuỗi nhị phân có chứa chuỗi con **`11`** hoặc **`101`**.

```text
      0, 1                                        0, 1
     ┌────┐                                      ┌────┐
     │    ▼                                      │    ▼
───► ( q0 ) ──── 1 ────► ( q1 ) ── 0, ε ──► ( q2 ) ──── 1 ────► ((( q3 )))
```

### Quy tắc vàng nhận diện trong 3 giây
1. **QUY TẮC 1:** Nhánh giữa đọc `1` $\to$ (`0` hoặc $\varepsilon$) $\to$ `1`, tạo đúng mẫu **`101`** hoặc **`11`**.
2. **QUY TẮC 2:** Hễ không có `11` lẫn `101` (ví dụ chỉ toàn `0`, có đúng một chữ `1`, hoặc các chữ `1` cách nhau $\ge 2$ chữ `0` như `1001`) thì **BỊ TỪ CHỐI**!

### Bộ 24 câu trắc nghiệm chuẩn Đề Mẫu Sample 2

**Câu 1.** Xét các chuỗi: $s_1 = \text{"11"}$, $s_2 = \text{"0"}$, $s_3 = \text{"1"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Tất cả các chuỗi được nêu.
👉 **Đáp án đúng: A**
- **Giải thích:** `11` hợp lệ ($S_0$ $\xrightarrow{1}$ $S_1$ $\xrightarrow{1}$ $S_3$ (NHẬN)). Còn `0` và `1` không về được trạng thái kết thúc.

**Câu 2.** Xét các chuỗi: $s_1 = \text{"00"}$, $s_2 = \text{"01"}$, $s_3 = \text{"011"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Các chọn lựa khác đều ĐÚNG.
👉 **Đáp án đúng: C**
- **Giải thích:** Chỉ có $s_3 =$ `011` hợp lệ ($S_0$ $\xrightarrow{0}$ $S_0$ $\xrightarrow{1}$ $S_1$ $\xrightarrow{1}$ $S_3$ (NHẬN)). Hai chuỗi $s_1, s_2$ bị từ chối.

**Câu 3.** Xét các chuỗi: $s_1 = \text{"101"}$, $s_2 = \text{"110"}$, $s_3 = \text{"111"}$, $s_4 = \text{"10"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1, s_2$ và $s_3$
- B. $s_2, s_3$ và $s_4$
- C. $s_3$ và $s_4$
- D. $s_4$
👉 **Đáp án đúng: A**
- **Giải thích:** $s_4 =$ `10` bị từ chối ($S_0$ $\xrightarrow{1}$ $S_1$ $\xrightarrow{0}$ $S_2$ (TỪ CHỐI)). Ba chuỗi còn lại đều hợp lệ.

**Câu 4.** Xét các chuỗi: $s_1 = \text{"0011"}$, $s_2 = \text{"000"}$, $s_3 = \text{"0101"}$, $s_4 = \text{"001"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_4$
- C. $s_1$ và $s_3$
- D. $s_1$ và $s_4$
👉 **Đáp án đúng: C**
- **Giải thích:** $s_1 =$ `0011` và $s_3 =$ `0101` hợp lệ; còn $s_2 =$ `000` và $s_4 =$ `001` không hợp lệ.

**Câu 5.** Xét các chuỗi: $s_1 = \text{"10010"}$, $s_2 = \text{"11111"}$, $s_3 = \text{"10001"}$, $s_4 = \text{"11110"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_4$
- C. $s_2$ và $s_3$
- D. $s_1$ và $s_4$
👉 **Đáp án đúng: B**
- **Giải thích:** $s_2 =$ `11111` và $s_4 =$ `11110` đạt trạng thái kết thúc; $s_1, s_3$ bị từ chối.

**Câu 6.** Xét các chuỗi: $s_1 = \text{"101"}$, $s_2 = \text{"110"}$, $s_3 = \text{"111"}$, $s_4 = \text{"10"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Chỉ duy nhất $s_4 =$ `10` bị từ chối ($S_0$ $\xrightarrow{1}$ $S_1$ $\xrightarrow{0}$ $S_2$ (TỪ CHỐI)).

**Câu 7.** Xét các chuỗi: $s_1 = \text{"11"}$, $s_2 = \text{"0"}$, $s_3 = \text{"011"}$, $s_4 = \text{"1"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_2$
- B. $s_1$
- C. $s_3$
- D. Tất cả các chuỗi đều không hợp lệ.
👉 **Đáp án đúng: A**
- **Giải thích:** $s_1, s_3$ đều hợp lệ nên loại B, C, D. Chuỗi $s_2 =$ `0` không hợp lệ ($S_0$ $\xrightarrow{0}$ $S_0$ (TỪ CHỐI)). *(Lưu ý tương tự Câu 7 Sample 2: $s_4$ cũng không hợp lệ nhưng chỉ có $s_2$ xuất hiện trong 4 lựa chọn nên A là đáp án duy nhất)*.

**Câu 8.** Xét các chuỗi: $s_1 = \text{"0011"}$, $s_2 = \text{"0101"}$, $s_3 = \text{"11111"}$, $s_4 = \text{"000"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_3$
- C. $s_3$ và $s_4$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Duy nhất $s_4 =$ `000` bị từ chối ($S_0$ $\xrightarrow{0}$ $S_0$ $\xrightarrow{0}$ $S_0$ $\xrightarrow{0}$ $S_0$ (TỪ CHỐI)).

**Câu 9.** Xét các chuỗi: $s_1 = \text{"0011"}$, $s_2 = \text{"0101"}$, $s_3 = \text{"11111"}$, $s_4 = \text{"000"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cả $s_1, s_2, s_3$ đều là chuỗi hợp lệ; chuỗi duy nhất không hợp lệ là $s_4 =$ `000` không nằm trong A, B, C $\implies$ Chọn D.

**Câu 10.** Xét các chuỗi: $s_1 = \text{"0011"}$, $s_2 = \text{"000"}$, $s_3 = \text{"0101"}$, $s_4 = \text{"001"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$ và $s_4$
- B. $s_2$ và $s_3$
- C. $s_3$ và $s_4$
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cặp không hợp lệ đúng phải là $s_2$ và $s_4$ (`000` và `001`), không có trong A, B, C $\implies$ Chọn D.

**Câu 11.** Xét các chuỗi: $s_1 = \text{"10010"}$, $s_2 = \text{"11111"}$, $s_3 = \text{"10001"}$, $s_4 = \text{"11110"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1, s_2$ và $s_3$
- B. $s_1$ và $s_3$
- C. $s_4$
- D. $s_3$ và $s_4$
👉 **Đáp án đúng: B**
- **Giải thích:** $s_1 =$ `10010` và $s_3 =$ `10001` đều không đạt trạng thái kết thúc.

**Câu 12.** Xét các chuỗi: $s_1 = \text{"101"}$, $s_2 = \text{"110"}$, $s_3 = \text{"111"}$, $s_4 = \text{"ε"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Chuỗi rỗng $s_4 = \varepsilon$ KHÔNG được nhận vì tập trạng thái khởi đầu (sau bao đóng $\varepsilon$) không chứa trạng thái kết thúc.

**Câu 13.** Xét biểu thức chính quy $E_1 = (0+1)^* 1 (0+1)^*$ (chuỗi có ít nhất một chữ `1`). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc ngôn ngữ mô tả bởi $E_1$**?
- A. `11`
- B. `011`
- C. `1`
- D. `101`
👉 **Đáp án đúng: C**
- **Giải thích:** `1` thỏa $E_1$ nhưng bị Automaton từ chối ($S_0$ $\xrightarrow{1}$ $S_1$ (TỪ CHỐI)). Ba chuỗi còn lại đều thuộc $L$.

**Câu 14.** Xét biểu thức $E_1 = (0+1)^* 1 (0+1)^*$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc ngôn ngữ mô tả bởi $E_1$**?
- A. Không có chuỗi nào
- B. `101`
- C. `10`
- D. `1`
👉 **Đáp án đúng: A**
- **Giải thích:** Mọi chuỗi hợp lệ của Automaton đều thỏa $E_1$ ($L \subseteq L(E_1)$), nên **không có chuỗi nào** thuộc $L$ mà lại ngoài $L(E_1)$!

**Câu 15.** Xét biểu thức $E_2 = (0+1)^* 11 (0+1)^*$ (chuỗi chứa cụm `11`). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_2)$**?
- A. `11`
- B. `011`
- C. `110`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Do $L(E_2) \subseteq L$ (và cả 3 chuỗi A, B, C đều thuộc $L$), nên không có chuỗi nào trong A, B, C thỏa điều kiện $\implies$ Chọn D.

**Câu 16.** Xét biểu thức $E_2 = (0+1)^* 11 (0+1)^*$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_2)$**?
- A. `11`
- B. `101`
- C. `011`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `101` thuộc $L$ ($S_0$ $\xrightarrow{1}$ $S_1$ $\xrightarrow{0}$ $S_2$ $\xrightarrow{1}$ $S_3$ (NHẬN)) nhưng không khớp khuôn mẫu của $E_2$. Còn `11` và `011` đều thuộc cả $L$ lẫn $E_2$.

**Câu 17.** Xét biểu thức $E_2 = (0+1)^* 11 (0+1)^*$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_2)$**?
- A. `11`
- B. `011`
- C. `110`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cả 3 chuỗi `11`, `011`, `110` đều đồng thời thuộc cả $L$ lẫn $E_2$ $\implies$ Chọn D (y hệt bẫy Câu 17 Sample 2!).

**Câu 18.** Xét biểu thức $E_3 = 0^* 101 0^*$ (chuỗi chứa đúng một cụm `101` và các chữ `0` xung quanh). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_3)$**?
- A. `101`
- B. `0101`
- C. `1010`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Do $L(E_3) \subseteq L$, không có chuỗi nào trong A, B, C nằm ngoài $L$ $\implies$ Chọn D.

**Câu 19.** Xét biểu thức $E_3 = 0^* 101 0^*$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_3)$**?
- A. `101`
- B. `11`
- C. `0101`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `11` thuộc $L$ ($S_0$ $\xrightarrow{1}$ $S_1$ $\xrightarrow{1}$ $S_3$ (NHẬN)) nhưng nằm ngoài $E_3$. Hai chuỗi còn lại thuộc cả $L$ và $E_3$.

**Câu 20.** Xét biểu thức $E_3 = 0^* 101 0^*$. Chuỗi nào **ĐỒNG THỜI KHÔNG** thuộc $L$ và **KHÔNG** thuộc $L(E_3)$?
- A. `11`
- B. `0`
- C. `1010`
- D. `101`
👉 **Đáp án đúng: B**
- **Giải thích:** `0` vừa không được Automaton chấp nhận vừa không thuộc $E_3$. Các chuỗi kia đều thuộc $L$ hoặc $E_3$ (hoặc cả hai).

**Câu 21.** Xét biểu thức $E_4 = (0+1)^* 10 (0+1)^*$ (chuỗi chứa cụm `10`). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_4)$**?
- A. `11`
- B. `011`
- C. `10`
- D. `101`
👉 **Đáp án đúng: C**
- **Giải thích:** `10` thuộc $L(E_4)$ nhưng bị Automaton từ chối ($S_0$ $\xrightarrow{1}$ $S_1$ $\xrightarrow{0}$ $S_2$ (TỪ CHỐI)). Ba chuỗi còn lại đều thuộc $L$.

**Câu 22.** Xét biểu thức $E_4 = (0+1)^* 10 (0+1)^*$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_4)$**?
- A. `101`
- B. `11`
- C. `110`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `11` thuộc $L$ ($S_0$ $\xrightarrow{1}$ $S_1$ $\xrightarrow{1}$ $S_3$ (NHẬN)) nhưng không khớp khuôn mẫu $E_4$.

**Câu 23.** Nếu áp dụng đơn định hóa Automaton đang quan tâm thì DFA đầy đủ thu được có bao nhiêu trạng thái?
- A. 5
- B. 6
- C. 7
- D. 8
👉 **Đáp án đúng: B**
- **Giải thích:** Áp dụng thuật toán xây dựng tập con (Subset Construction) thu được **6 trạng thái** (xem bảng bên dưới): *(Không xuất hiện trạng thái rỗng $\emptyset$, tất cả **6 trạng thái** đều đang hoạt động).*

| Trạng thái DFA | Tập con NFA | Đọc `0` | Đọc `1` | Kết thúc? |
| :---: | :---: | :---: | :---: | :---: |
| $S_0$ (Đầu) | $\{q0\}$ | $S_0$ | $S_1$ | Không |
| $S_1$ | $\{q0, q1, q2\}$ | $S_2$ | $S_3$ | Không |
| $S_2$ | $\{q0, q2\}$ | $S_0$ | $S_3$ | Không |
| $S_3$ | $\{q0, q1, q2, q3\}$ | $S_4$ | $S_3$ | **CÓ** |
| $S_4$ | $\{q0, q2, q3\}$ | $S_5$ | $S_3$ | **CÓ** |
| $S_5$ | $\{q0, q3\}$ | $S_5$ | $S_3$ | **CÓ** |

**Câu 24.** DFA tối giản tương đương có bao nhiêu trạng thái?
- A. 3
- B. 4
- C. 5
- D. 6
👉 **Đáp án đúng: B**
- **Giải thích:** Có thể gộp từ **6** trạng thái xuống còn **4** trạng thái tương đương. Phân hoạch các nhóm trạng thái tương đương cuối cùng gồm **4 nhóm**: `{$S_3$, $S_4$, $S_5$}`, `{$S_1$}`, `{$S_2$}`, `{$S_0$}`.

---

## HÌNH 3 (`image_0.png`): NFA TÁCH NHÁNH $\{a^3\} \cup \{a^{2k} \mid k \ge 1\}$

> **THÔNG TIN ĐỀ BÀI GỐC (Hình 3 trong OnTapAutomata.docx - ảnh `image_0.png`):**
> - Tập trạng thái: $Q = \{q0, q1, q2, q3, q4, q5\}$
> - Bảng chữ cái: $\Sigma = \{a\}$
> - Trạng thái bắt đầu: $q0$
> - Trạng thái kết thúc: $F = \{q3, q5\}$
> - Tính chất ban đầu: **Không đơn định (NFA)**
> - Biểu thức chính quy tương đương: **$a^3 + a^2(aa)^*$**
> - Ngôn ngữ đoán nhận: Tập hợp gồm chuỗi `aaa` và tất cả các chuỗi chữ `a` có độ dài chẵn $\ge 2$ ($a^2, a^3, a^4, a^6, a^8, \dots$).

```text
          a          a          a
───► ( q0 ) ───► ( q1 ) ───► ( q2 ) ───► ((( q3 )))
       │
       │ a
       ▼
     ( q4 ) ◄─── a ───► ((( q5 )))
```

### Quy tắc vàng nhận diện trong 3 giây
1. **QUY TẮC 1:** Nhánh trên CHỈ chấp nhận duy nhất **`aaa`** (độ dài 3).
2. **QUY TẮC 2:** Nhánh dưới chấp nhận mọi độ dài **chẵn $\ge 2$** (`aa`, `aaaa`, `aaaaaa`,...).
3. **QUY TẮC 3:** Chuỗi rỗng $\varepsilon$, chuỗi `a` (dài 1) và mọi độ dài lẻ $\ge 5$ (`aaaaa`, `aaaaaaa`,...) đều **BỊ TỪ CHỐI**!

### Bộ 24 câu trắc nghiệm chuẩn Đề Mẫu Sample 2

**Câu 1.** Xét các chuỗi: $s_1 = \text{"aa"}$, $s_2 = \text{"a"}$, $s_3 = \text{"aaaaa"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Tất cả các chuỗi được nêu.
👉 **Đáp án đúng: A**
- **Giải thích:** `aa` hợp lệ ($S_0$ $\xrightarrow{a}$ $S_1$ $\xrightarrow{a}$ $S_2$ (NHẬN)). Còn `a` và `aaaaa` không về được trạng thái kết thúc.

**Câu 2.** Xét các chuỗi: $s_1 = \text{"aaaaaaa"}$, $s_2 = \text{"aaaaaaaaa"}$, $s_3 = \text{"aaa"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Các chọn lựa khác đều ĐÚNG.
👉 **Đáp án đúng: C**
- **Giải thích:** Chỉ có $s_3 =$ `aaa` hợp lệ ($S_0$ $\xrightarrow{a}$ $S_1$ $\xrightarrow{a}$ $S_2$ $\xrightarrow{a}$ $S_3$ (NHẬN)). Hai chuỗi $s_1, s_2$ bị từ chối.

**Câu 3.** Xét các chuỗi: $s_1 = \text{"aaaa"}$, $s_2 = \text{"aaaaaa"}$, $s_3 = \text{"aaaaaaaa"}$, $s_4 = \text{"aaaaaaaaaaa"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1, s_2$ và $s_3$
- B. $s_2, s_3$ và $s_4$
- C. $s_3$ và $s_4$
- D. $s_4$
👉 **Đáp án đúng: A**
- **Giải thích:** $s_4 =$ `aaaaaaaaaaa` bị từ chối ($S_0$ $\xrightarrow{a}$ $S_1$ $\xrightarrow{a}$ $S_2$ $\xrightarrow{a}$ $S_3$ $\xrightarrow{a}$ $S_4$ $\xrightarrow{a}$ $S_5$ $\xrightarrow{a}$ $S_4$ $\xrightarrow{a}$ $S_5$ $\xrightarrow{a}$ $S_4$ $\xrightarrow{a}$ $S_5$ $\xrightarrow{a}$ $S_4$ $\xrightarrow{a}$ $S_5$ (TỪ CHỐI)). Ba chuỗi còn lại đều hợp lệ.

**Câu 4.** Xét các chuỗi: $s_1 = \text{"aaaaaaaaaa"}$, $s_2 = \text{"aaaaa"}$, $s_3 = \text{"aaaaaaaaaaaa"}$, $s_4 = \text{"aaaaaaa"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_4$
- C. $s_1$ và $s_3$
- D. $s_1$ và $s_4$
👉 **Đáp án đúng: C**
- **Giải thích:** $s_1 =$ `aaaaaaaaaa` và $s_3 =$ `aaaaaaaaaaaa` hợp lệ; còn $s_2 =$ `aaaaa` và $s_4 =$ `aaaaaaa` không hợp lệ.

**Câu 5.** Xét các chuỗi: $s_1 = \text{"aaaaa"}$, $s_2 = \text{"aa"}$, $s_3 = \text{"aaaaaaa"}$, $s_4 = \text{"aaa"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_4$
- C. $s_2$ và $s_3$
- D. $s_1$ và $s_4$
👉 **Đáp án đúng: B**
- **Giải thích:** $s_2 =$ `aa` và $s_4 =$ `aaa` đạt trạng thái kết thúc; $s_1, s_3$ bị từ chối.

**Câu 6.** Xét các chuỗi: $s_1 = \text{"aaaa"}$, $s_2 = \text{"aaaaaa"}$, $s_3 = \text{"aaaaaaaa"}$, $s_4 = \text{"aaaaaaaaaaa"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Chỉ duy nhất $s_4 =$ `aaaaaaaaaaa` bị từ chối ($S_0$ $\xrightarrow{a}$ $S_1$ $\xrightarrow{a}$ $S_2$ $\xrightarrow{a}$ $S_3$ $\xrightarrow{a}$ $S_4$ $\xrightarrow{a}$ $S_5$ $\xrightarrow{a}$ $S_4$ $\xrightarrow{a}$ $S_5$ $\xrightarrow{a}$ $S_4$ $\xrightarrow{a}$ $S_5$ $\xrightarrow{a}$ $S_4$ $\xrightarrow{a}$ $S_5$ (TỪ CHỐI)).

**Câu 7.** Xét các chuỗi: $s_1 = \text{"aa"}$, $s_2 = \text{"a"}$, $s_3 = \text{"aaa"}$, $s_4 = \text{"aaaaa"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_2$
- B. $s_1$
- C. $s_3$
- D. Tất cả các chuỗi đều không hợp lệ.
👉 **Đáp án đúng: A**
- **Giải thích:** $s_1, s_3$ đều hợp lệ nên loại B, C, D. Chuỗi $s_2 =$ `a` không hợp lệ ($S_0$ $\xrightarrow{a}$ $S_1$ (TỪ CHỐI)). *(Lưu ý tương tự Câu 7 Sample 2: $s_4$ cũng không hợp lệ nhưng chỉ có $s_2$ xuất hiện trong 4 lựa chọn nên A là đáp án duy nhất)*.

**Câu 8.** Xét các chuỗi: $s_1 = \text{"aaaaaaaaaa"}$, $s_2 = \text{"aaaaaaaaaaaa"}$, $s_3 = \text{"aa"}$, $s_4 = \text{"aaaaa"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_3$
- C. $s_3$ và $s_4$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Duy nhất $s_4 =$ `aaaaa` bị từ chối ($S_0$ $\xrightarrow{a}$ $S_1$ $\xrightarrow{a}$ $S_2$ $\xrightarrow{a}$ $S_3$ $\xrightarrow{a}$ $S_4$ $\xrightarrow{a}$ $S_5$ (TỪ CHỐI)).

**Câu 9.** Xét các chuỗi: $s_1 = \text{"aaaaaaaaaa"}$, $s_2 = \text{"aaaaaaaaaaaa"}$, $s_3 = \text{"aa"}$, $s_4 = \text{"aaaaa"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cả $s_1, s_2, s_3$ đều là chuỗi hợp lệ; chuỗi duy nhất không hợp lệ là $s_4 =$ `aaaaa` không nằm trong A, B, C $\implies$ Chọn D.

**Câu 10.** Xét các chuỗi: $s_1 = \text{"aaaaaaaaaa"}$, $s_2 = \text{"aaaaa"}$, $s_3 = \text{"aaaaaaaaaaaa"}$, $s_4 = \text{"aaaaaaa"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$ và $s_4$
- B. $s_2$ và $s_3$
- C. $s_3$ và $s_4$
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cặp không hợp lệ đúng phải là $s_2$ và $s_4$ (`aaaaa` và `aaaaaaa`), không có trong A, B, C $\implies$ Chọn D.

**Câu 11.** Xét các chuỗi: $s_1 = \text{"aaaaa"}$, $s_2 = \text{"aa"}$, $s_3 = \text{"aaaaaaa"}$, $s_4 = \text{"aaa"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1, s_2$ và $s_3$
- B. $s_1$ và $s_3$
- C. $s_4$
- D. $s_3$ và $s_4$
👉 **Đáp án đúng: B**
- **Giải thích:** $s_1 =$ `aaaaa` và $s_3 =$ `aaaaaaa` đều không đạt trạng thái kết thúc.

**Câu 12.** Xét các chuỗi: $s_1 = \text{"aaaa"}$, $s_2 = \text{"aaaaaa"}$, $s_3 = \text{"aaaaaaaa"}$, $s_4 = \text{"ε"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Chuỗi rỗng $s_4 = \varepsilon$ KHÔNG được nhận vì tập trạng thái khởi đầu (sau bao đóng $\varepsilon$) không chứa trạng thái kết thúc.

**Câu 13.** Xét biểu thức chính quy $E_1 = a a^+$ (chuỗi chữ `a` có độ dài $\ge 2$). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc ngôn ngữ mô tả bởi $E_1$**?
- A. `aa`
- B. `aaa`
- C. `aaaaa`
- D. `aaaa`
👉 **Đáp án đúng: C**
- **Giải thích:** `aaaaa` thỏa $E_1$ nhưng bị Automaton từ chối ($S_0$ $\xrightarrow{a}$ $S_1$ $\xrightarrow{a}$ $S_2$ $\xrightarrow{a}$ $S_3$ $\xrightarrow{a}$ $S_4$ $\xrightarrow{a}$ $S_5$ (TỪ CHỐI)). Ba chuỗi còn lại đều thuộc $L$.

**Câu 14.** Xét biểu thức $E_1 = a a^+$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc ngôn ngữ mô tả bởi $E_1$**?
- A. Không có chuỗi nào
- B. `aaaa`
- C. `aaaaaaaaaaa`
- D. `aaaaa`
👉 **Đáp án đúng: A**
- **Giải thích:** Mọi chuỗi hợp lệ của Automaton đều thỏa $E_1$ ($L \subseteq L(E_1)$), nên **không có chuỗi nào** thuộc $L$ mà lại ngoài $L(E_1)$!

**Câu 15.** Xét biểu thức $E_2 = a (aa)^*$ (chuỗi chữ `a` có độ dài lẻ). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_2)$**?
- A. `aa`
- B. `a`
- C. `aaa`
- D. `aaaa`
👉 **Đáp án đúng: B**
- **Giải thích:** `a` sinh được từ $E_2$ nhưng không thuộc $L$ ($S_0$ $\xrightarrow{a}$ $S_1$ (TỪ CHỐI)). Ba chuỗi kia đều thuộc $L$.

**Câu 16.** Xét biểu thức $E_2 = a (aa)^*$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_2)$**?
- A. `aaa`
- B. `aa`
- C. `a`
- D. aaaaa
👉 **Đáp án đúng: B**
- **Giải thích:** `aa` thuộc $L$ nhưng ngoài $E_2$; `aaa` thuộc cả $L$ lẫn $E_2$; `a`, `aaaaa` không thuộc $L$.

**Câu 17.** Xét biểu thức $E_2 = a (aa)^*$. Chuỗi nào sau đây **thuộc $L$** nhưng **KHÔNG thuộc $L(E_2)$**?
- A. `aaaa`
- B. `aaa`
- C. `a`
- D. `aaaaa`
👉 **Đáp án đúng: A**
- **Giải thích:** `aaaa` thuộc $L$ nhưng không sinh được từ $E_2$; `a`, `aaaaa` không thuộc $L$.

**Câu 18.** Xét biểu thức $E_3 = (aa)^*$ (chuỗi chữ `a` có độ dài chẵn (kể cả rỗng $\varepsilon$)). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_3)$**?
- A. `aa`
- B. $\varepsilon$
- C. `aaa`
- D. `aaaa`
👉 **Đáp án đúng: B**
- **Giải thích:** $\varepsilon$ thuộc $E_3$ nhưng không được Automaton chấp nhận ($S_0$ (TỪ CHỐI)). Các chuỗi kia đều thuộc $L$.

**Câu 19.** Xét biểu thức $E_3 = (aa)^*$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_3)$**?
- A. `aa`
- B. `aaa`
- C. `aaaa`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `aaa` thuộc $L$ ($S_0$ $\xrightarrow{a}$ $S_1$ $\xrightarrow{a}$ $S_2$ $\xrightarrow{a}$ $S_3$ (NHẬN)) nhưng nằm ngoài $E_3$. Hai chuỗi còn lại thuộc cả $L$ và $E_3$.

**Câu 20.** Xét biểu thức $E_3 = (aa)^*$. Chuỗi nào **ĐỒNG THỜI KHÔNG** thuộc $L$ và **KHÔNG** thuộc $L(E_3)$?
- A. `aaa`
- B. `a`
- C. $\varepsilon$
- D. `aa`
👉 **Đáp án đúng: B**
- **Giải thích:** `a` vừa không được Automaton chấp nhận vừa không thuộc $E_3$. Các chuỗi kia đều thuộc $L$ hoặc $E_3$ (hoặc cả hai).

**Câu 21.** Xét biểu thức $E_4 = aaa a^*$ (chuỗi chữ `a` có độ dài $\ge 3$). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_4)$**?
- A. `aa`
- B. `aaa`
- C. `aaaaa`
- D. `aaaa`
👉 **Đáp án đúng: C**
- **Giải thích:** `aaaaa` thuộc $L(E_4)$ nhưng bị Automaton từ chối ($S_0$ $\xrightarrow{a}$ $S_1$ $\xrightarrow{a}$ $S_2$ $\xrightarrow{a}$ $S_3$ $\xrightarrow{a}$ $S_4$ $\xrightarrow{a}$ $S_5$ (TỪ CHỐI)). Ba chuỗi còn lại đều thuộc $L$.

**Câu 22.** Xét biểu thức $E_4 = aaa a^*$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_4)$**?
- A. `aaa`
- B. `aa`
- C. `aaaa`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `aa` thuộc $L$ ($S_0$ $\xrightarrow{a}$ $S_1$ $\xrightarrow{a}$ $S_2$ (NHẬN)) nhưng không khớp khuôn mẫu $E_4$.

**Câu 23.** Nếu áp dụng đơn định hóa Automaton đang quan tâm thì DFA đầy đủ thu được có bao nhiêu trạng thái?
- A. 5
- B. 6
- C. 7
- D. 8
👉 **Đáp án đúng: B**
- **Giải thích:** Áp dụng thuật toán xây dựng tập con (Subset Construction) thu được **6 trạng thái** (xem bảng bên dưới): *(Không xuất hiện trạng thái rỗng $\emptyset$, tất cả **6 trạng thái** đều đang hoạt động).*

| Trạng thái DFA | Tập con NFA | Đọc `a` | Kết thúc? |
| :---: | :---: | :---: | :---: |
| $S_0$ (Đầu) | $\{q0\}$ | $S_1$ | Không |
| $S_1$ | $\{q1, q4\}$ | $S_2$ | Không |
| $S_2$ | $\{q2, q5\}$ | $S_3$ | **CÓ** |
| $S_3$ | $\{q3, q4\}$ | $S_4$ | **CÓ** |
| $S_4$ | $\{q5\}$ | $S_5$ | **CÓ** |
| $S_5$ | $\{q4\}$ | $S_4$ | Không |

**Câu 24.** DFA tối giản tương đương có bao nhiêu trạng thái?
- A. 5
- B. 6
- C. 7
- D. 8
👉 **Đáp án đúng: B**
- **Giải thích:** DFA thu được **đã tối giản** (**6 trạng thái**). Phân hoạch các nhóm trạng thái tương đương cuối cùng gồm **6 nhóm**: `{$S_2$}`, `{$S_3$}`, `{$S_4$}`, `{$S_5$}`, `{$S_1$}`, `{$S_0$}`.

---

## HÌNH 4 (`image_12.jpg`): NFA CHỨA ÍT NHẤT HAI CHỮ `b`

> **THÔNG TIN ĐỀ BÀI GỐC (Hình 4 trong OnTapAutomata.docx - ảnh `image_12.jpg`):**
> - Tập trạng thái: $Q = \{q0, q1, q2\}$
> - Bảng chữ cái: $\Sigma = \{a, b\}$
> - Trạng thái bắt đầu: $q0$
> - Trạng thái kết thúc: $F = \{q2\}$
> - Tính chất ban đầu: **Không đơn định (NFA)**
> - Biểu thức chính quy tương đương: **$(a+b)^* b (a+b)^* b (a+b)^*$**
> - Ngôn ngữ đoán nhận: Tập hợp mọi chuỗi trên $\{a, b\}$ có chứa **ít nhất 2 ký tự `b`** (vị trí tùy ý).

```text
      a, b               a, b               a, b
     ┌────┐             ┌────┐             ┌────┐
     │    ▼             │    ▼             │    ▼
───► ( q0 ) ──── b ────► ( q1 ) ──── b ────► ((( q2 )))
```

### Quy tắc vàng nhận diện trong 3 giây
1. **QUY TẮC 1:** Vì tại $q_0, q_1, q_2$ đều có vòng tự lặp `a, b`, chỉ cần có **tổng cộng từ 2 chữ `b` trở lên** ($\#b \ge 2$) là chắc chắn về được $q_2$.
2. **QUY TẮC 2:** Mọi chuỗi có 0 hoặc đúng 1 chữ `b` đều **BỊ TỪ CHỐI**!

### Bộ 24 câu trắc nghiệm chuẩn Đề Mẫu Sample 2

**Câu 1.** Xét các chuỗi: $s_1 = \text{"bb"}$, $s_2 = \text{"a"}$, $s_3 = \text{"b"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Tất cả các chuỗi được nêu.
👉 **Đáp án đúng: A**
- **Giải thích:** `bb` hợp lệ ($S_0$ $\xrightarrow{b}$ $S_1$ $\xrightarrow{b}$ $S_2$ (NHẬN)). Còn `a` và `b` không về được trạng thái kết thúc.

**Câu 2.** Xét các chuỗi: $s_1 = \text{"aa"}$, $s_2 = \text{"ab"}$, $s_3 = \text{"abb"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Các chọn lựa khác đều ĐÚNG.
👉 **Đáp án đúng: C**
- **Giải thích:** Chỉ có $s_3 =$ `abb` hợp lệ ($S_0$ $\xrightarrow{a}$ $S_0$ $\xrightarrow{b}$ $S_1$ $\xrightarrow{b}$ $S_2$ (NHẬN)). Hai chuỗi $s_1, s_2$ bị từ chối.

**Câu 3.** Xét các chuỗi: $s_1 = \text{"bab"}$, $s_2 = \text{"bba"}$, $s_3 = \text{"bbb"}$, $s_4 = \text{"ba"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1, s_2$ và $s_3$
- B. $s_2, s_3$ và $s_4$
- C. $s_3$ và $s_4$
- D. $s_4$
👉 **Đáp án đúng: A**
- **Giải thích:** $s_4 =$ `ba` bị từ chối ($S_0$ $\xrightarrow{b}$ $S_1$ $\xrightarrow{a}$ $S_1$ (TỪ CHỐI)). Ba chuỗi còn lại đều hợp lệ.

**Câu 4.** Xét các chuỗi: $s_1 = \text{"aabb"}$, $s_2 = \text{"aaa"}$, $s_3 = \text{"abab"}$, $s_4 = \text{"aab"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_4$
- C. $s_1$ và $s_3$
- D. $s_1$ và $s_4$
👉 **Đáp án đúng: C**
- **Giải thích:** $s_1 =$ `aabb` và $s_3 =$ `abab` hợp lệ; còn $s_2 =$ `aaa` và $s_4 =$ `aab` không hợp lệ.

**Câu 5.** Xét các chuỗi: $s_1 = \text{"baaaa"}$, $s_2 = \text{"bbbbb"}$, $s_3 = \text{"abaaa"}$, $s_4 = \text{"bbbba"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_4$
- C. $s_2$ và $s_3$
- D. $s_1$ và $s_4$
👉 **Đáp án đúng: B**
- **Giải thích:** $s_2 =$ `bbbbb` và $s_4 =$ `bbbba` đạt trạng thái kết thúc; $s_1, s_3$ bị từ chối.

**Câu 6.** Xét các chuỗi: $s_1 = \text{"bab"}$, $s_2 = \text{"bba"}$, $s_3 = \text{"bbb"}$, $s_4 = \text{"ba"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Chỉ duy nhất $s_4 =$ `ba` bị từ chối ($S_0$ $\xrightarrow{b}$ $S_1$ $\xrightarrow{a}$ $S_1$ (TỪ CHỐI)).

**Câu 7.** Xét các chuỗi: $s_1 = \text{"bb"}$, $s_2 = \text{"a"}$, $s_3 = \text{"abb"}$, $s_4 = \text{"b"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_2$
- B. $s_1$
- C. $s_3$
- D. Tất cả các chuỗi đều không hợp lệ.
👉 **Đáp án đúng: A**
- **Giải thích:** $s_1, s_3$ đều hợp lệ nên loại B, C, D. Chuỗi $s_2 =$ `a` không hợp lệ ($S_0$ $\xrightarrow{a}$ $S_0$ (TỪ CHỐI)). *(Lưu ý tương tự Câu 7 Sample 2: $s_4$ cũng không hợp lệ nhưng chỉ có $s_2$ xuất hiện trong 4 lựa chọn nên A là đáp án duy nhất)*.

**Câu 8.** Xét các chuỗi: $s_1 = \text{"aabb"}$, $s_2 = \text{"abab"}$, $s_3 = \text{"bbbbb"}$, $s_4 = \text{"aaa"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_3$
- C. $s_3$ và $s_4$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Duy nhất $s_4 =$ `aaa` bị từ chối ($S_0$ $\xrightarrow{a}$ $S_0$ $\xrightarrow{a}$ $S_0$ $\xrightarrow{a}$ $S_0$ (TỪ CHỐI)).

**Câu 9.** Xét các chuỗi: $s_1 = \text{"aabb"}$, $s_2 = \text{"abab"}$, $s_3 = \text{"bbbbb"}$, $s_4 = \text{"aaa"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cả $s_1, s_2, s_3$ đều là chuỗi hợp lệ; chuỗi duy nhất không hợp lệ là $s_4 =$ `aaa` không nằm trong A, B, C $\implies$ Chọn D.

**Câu 10.** Xét các chuỗi: $s_1 = \text{"aabb"}$, $s_2 = \text{"aaa"}$, $s_3 = \text{"abab"}$, $s_4 = \text{"aab"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$ và $s_4$
- B. $s_2$ và $s_3$
- C. $s_3$ và $s_4$
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cặp không hợp lệ đúng phải là $s_2$ và $s_4$ (`aaa` và `aab`), không có trong A, B, C $\implies$ Chọn D.

**Câu 11.** Xét các chuỗi: $s_1 = \text{"baaaa"}$, $s_2 = \text{"bbbbb"}$, $s_3 = \text{"abaaa"}$, $s_4 = \text{"bbbba"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1, s_2$ và $s_3$
- B. $s_1$ và $s_3$
- C. $s_4$
- D. $s_3$ và $s_4$
👉 **Đáp án đúng: B**
- **Giải thích:** $s_1 =$ `baaaa` và $s_3 =$ `abaaa` đều không đạt trạng thái kết thúc.

**Câu 12.** Xét các chuỗi: $s_1 = \text{"bab"}$, $s_2 = \text{"bba"}$, $s_3 = \text{"bbb"}$, $s_4 = \text{"ε"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Chuỗi rỗng $s_4 = \varepsilon$ KHÔNG được nhận vì tập trạng thái khởi đầu (sau bao đóng $\varepsilon$) không chứa trạng thái kết thúc.

**Câu 13.** Xét biểu thức chính quy $E_1 = (a+b)^* b (a+b)^*$ (chuỗi chứa ít nhất 1 chữ `b`). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc ngôn ngữ mô tả bởi $E_1$**?
- A. `bb`
- B. `abb`
- C. `b`
- D. `bab`
👉 **Đáp án đúng: C**
- **Giải thích:** `b` thỏa $E_1$ nhưng bị Automaton từ chối ($S_0$ $\xrightarrow{b}$ $S_1$ (TỪ CHỐI)). Ba chuỗi còn lại đều thuộc $L$.

**Câu 14.** Xét biểu thức $E_1 = (a+b)^* b (a+b)^*$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc ngôn ngữ mô tả bởi $E_1$**?
- A. Không có chuỗi nào
- B. `bab`
- C. `ba`
- D. `b`
👉 **Đáp án đúng: A**
- **Giải thích:** Mọi chuỗi hợp lệ của Automaton đều thỏa $E_1$ ($L \subseteq L(E_1)$), nên **không có chuỗi nào** thuộc $L$ mà lại ngoài $L(E_1)$!

**Câu 15.** Xét biểu thức $E_2 = a^* b a^* b a^*$ (chuỗi chứa đúng 2 chữ `b`). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_2)$**?
- A. `bb`
- B. `abb`
- C. `bab`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Do $L(E_2) \subseteq L$ (và cả 3 chuỗi A, B, C đều thuộc $L$), nên không có chuỗi nào trong A, B, C thỏa điều kiện $\implies$ Chọn D.

**Câu 16.** Xét biểu thức $E_2 = a^* b a^* b a^*$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_2)$**?
- A. `bb`
- B. `bbb`
- C. `abb`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `bbb` thuộc $L$ ($S_0$ $\xrightarrow{b}$ $S_1$ $\xrightarrow{b}$ $S_2$ $\xrightarrow{b}$ $S_2$ (NHẬN)) nhưng không khớp khuôn mẫu của $E_2$. Còn `bb` và `abb` đều thuộc cả $L$ lẫn $E_2$.

**Câu 17.** Xét biểu thức $E_2 = a^* b a^* b a^*$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_2)$**?
- A. `bb`
- B. `abb`
- C. `bab`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cả 3 chuỗi `bb`, `abb`, `bab` đều đồng thời thuộc cả $L$ lẫn $E_2$ $\implies$ Chọn D (y hệt bẫy Câu 17 Sample 2!).

**Câu 18.** Xét biểu thức $E_3 = (a+b)^* bb (a+b)^*$ (chuỗi chứa hai chữ `b` đứng liền nhau). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_3)$**?
- A. `bb`
- B. `abb`
- C. `bba`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Do $L(E_3) \subseteq L$, không có chuỗi nào trong A, B, C nằm ngoài $L$ $\implies$ Chọn D.

**Câu 19.** Xét biểu thức $E_3 = (a+b)^* bb (a+b)^*$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_3)$**?
- A. `bb`
- B. `bab`
- C. `abb`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `bab` thuộc $L$ ($S_0$ $\xrightarrow{b}$ $S_1$ $\xrightarrow{a}$ $S_1$ $\xrightarrow{b}$ $S_2$ (NHẬN)) nhưng nằm ngoài $E_3$. Hai chuỗi còn lại thuộc cả $L$ và $E_3$.

**Câu 20.** Xét biểu thức $E_3 = (a+b)^* bb (a+b)^*$. Chuỗi nào **ĐỒNG THỜI KHÔNG** thuộc $L$ và **KHÔNG** thuộc $L(E_3)$?
- A. `bab`
- B. `a`
- C. `bba`
- D. `bb`
👉 **Đáp án đúng: B**
- **Giải thích:** `a` vừa không được Automaton chấp nhận vừa không thuộc $E_3$. Các chuỗi kia đều thuộc $L$ hoặc $E_3$ (hoặc cả hai).

**Câu 21.** Xét biểu thức $E_4 = b^* a^* b^*$ (chuỗi có toàn bộ chữ `a` đứng kẹp giữa (hoặc không có `a`)). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_4)$**?
- A. `bb`
- B. `abb`
- C. $\varepsilon$
- D. `bab`
👉 **Đáp án đúng: C**
- **Giải thích:** $\varepsilon$ thuộc $L(E_4)$ nhưng bị Automaton từ chối ($S_0$ (TỪ CHỐI)). Ba chuỗi còn lại đều thuộc $L$.

**Câu 22.** Xét biểu thức $E_4 = b^* a^* b^*$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_4)$**?
- A. `bb`
- B. `abab`
- C. `abb`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `abab` thuộc $L$ ($S_0$ $\xrightarrow{a}$ $S_0$ $\xrightarrow{b}$ $S_1$ $\xrightarrow{a}$ $S_1$ $\xrightarrow{b}$ $S_2$ (NHẬN)) nhưng không khớp khuôn mẫu $E_4$.

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
| $S_1$ | $\{q0, q1\}$ | $S_1$ | $S_2$ | Không |
| $S_2$ | $\{q0, q1, q2\}$ | $S_2$ | $S_2$ | **CÓ** |

**Câu 24.** DFA tối giản tương đương có bao nhiêu trạng thái?
- A. 2
- B. 3
- C. 4
- D. 5
👉 **Đáp án đúng: B**
- **Giải thích:** DFA thu được **đã tối giản** (**3 trạng thái**). Phân hoạch các nhóm trạng thái tương đương cuối cùng gồm **3 nhóm**: `{$S_2$}`, `{$S_0$}`, `{$S_1$}`.

---

## HÌNH 5 (`image_10.png`): $\varepsilon$-NFA LẶP CỤM `10` ($(10)^*$)

> **THÔNG TIN ĐỀ BÀI GỐC (Hình 5 trong OnTapAutomata.docx - ảnh `image_10.png`):**
> - Tập trạng thái: $Q = \{q0, q1, q2\}$
> - Bảng chữ cái: $\Sigma = \{0, 1\}$
> - Trạng thái bắt đầu: $q0$
> - Trạng thái kết thúc: $F = \{q0\}$
> - Tính chất ban đầu: **Không đơn định có chuyển rỗng ($\varepsilon$-NFA)**
> - Biểu thức chính quy tương đương: **$(10)^*$**
> - Ngôn ngữ đoán nhận: Tập hợp gồm chuỗi rỗng $\varepsilon$ và các chuỗi lặp lại cụm `10`: $\{\varepsilon, 10, 1010, 101010, \dots\}$. *(Cẩn thận bẫy: $q_2$ là trạng thái ngõ cụt không kết thúc, mũi tên $\varepsilon$ sang $q_2$ không làm chuỗi dài thêm hay kết thúc được!)*

```text
            0
        ┌───────┐
        ▼       │      0, 1
───► ((( q0 ))) ── 1 ──► ( q1 ) ──────► ( q2 )
        │                                 ▲
        └────────────── ε ────────────────┘
```

### Quy tắc vàng nhận diện trong 3 giây
1. **QUY TẮC 1:** $q_0$ vừa là đầu vừa là kết thúc $\implies$ **chuỗi rỗng $\varepsilon$ ĐƯỢC NHẬN**.
2. **QUY TẮC 2:** Chu trình sống duy nhất là $q_0 \xrightarrow{1} q_1 \xrightarrow{0} q_0$. Mọi mũi tên dẫn vào $q_2$ đều rơi vào ngõ cụt không lối thoát! Do đó chỉ nhận đúng **`ε, 10, 1010, ...`**!

### Bộ 24 câu trắc nghiệm chuẩn Đề Mẫu Sample 2

**Câu 1.** Xét các chuỗi: $s_1 = \text{"10"}$, $s_2 = \text{"0"}$, $s_3 = \text{"1"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Tất cả các chuỗi được nêu.
👉 **Đáp án đúng: A**
- **Giải thích:** `10` hợp lệ ($S_0$ $\xrightarrow{1}$ $S_2$ $\xrightarrow{0}$ $S_0$ (NHẬN)). Còn `0` và `1` không về được trạng thái kết thúc.

**Câu 2.** Xét các chuỗi: $s_1 = \text{"00"}$, $s_2 = \text{"01"}$, $s_3 = \text{"1010"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Các chọn lựa khác đều ĐÚNG.
👉 **Đáp án đúng: C**
- **Giải thích:** Chỉ có $s_3 =$ `1010` hợp lệ ($S_0$ $\xrightarrow{1}$ $S_2$ $\xrightarrow{0}$ $S_0$ $\xrightarrow{1}$ $S_2$ $\xrightarrow{0}$ $S_0$ (NHẬN)). Hai chuỗi $s_1, s_2$ bị từ chối.

**Câu 3.** Xét các chuỗi: $s_1 = \text{"101010"}$, $s_2 = \text{"10101010"}$, $s_3 = \text{"10"}$, $s_4 = \text{"11"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1, s_2$ và $s_3$
- B. $s_2, s_3$ và $s_4$
- C. $s_3$ và $s_4$
- D. $s_4$
👉 **Đáp án đúng: A**
- **Giải thích:** $s_4 =$ `11` bị từ chối ($S_0$ $\xrightarrow{1}$ $S_2$ $\xrightarrow{1}$ $S_3$ (TỪ CHỐI)). Ba chuỗi còn lại đều hợp lệ.

**Câu 4.** Xét các chuỗi: $s_1 = \text{"10"}$, $s_2 = \text{"000"}$, $s_3 = \text{"1010"}$, $s_4 = \text{"001"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_4$
- C. $s_1$ và $s_3$
- D. $s_1$ và $s_4$
👉 **Đáp án đúng: C**
- **Giải thích:** $s_1 =$ `10` và $s_3 =$ `1010` hợp lệ; còn $s_2 =$ `000` và $s_4 =$ `001` không hợp lệ.

**Câu 5.** Xét các chuỗi: $s_1 = \text{"11111111"}$, $s_2 = \text{"10"}$, $s_3 = \text{"11111110"}$, $s_4 = \text{"1010"}$. Chuỗi nào hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_4$
- C. $s_2$ và $s_3$
- D. $s_1$ và $s_4$
👉 **Đáp án đúng: B**
- **Giải thích:** $s_2 =$ `10` và $s_4 =$ `1010` đạt trạng thái kết thúc; $s_1, s_3$ bị từ chối.

**Câu 6.** Xét các chuỗi: $s_1 = \text{"101010"}$, $s_2 = \text{"10101010"}$, $s_3 = \text{"10"}$, $s_4 = \text{"11"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Chỉ duy nhất $s_4 =$ `11` bị từ chối ($S_0$ $\xrightarrow{1}$ $S_2$ $\xrightarrow{1}$ $S_3$ (TỪ CHỐI)).

**Câu 7.** Xét các chuỗi: $s_1 = \text{"10"}$, $s_2 = \text{"0"}$, $s_3 = \text{"1010"}$, $s_4 = \text{"1"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_2$
- B. $s_1$
- C. $s_3$
- D. Tất cả các chuỗi đều không hợp lệ.
👉 **Đáp án đúng: A**
- **Giải thích:** $s_1, s_3$ đều hợp lệ nên loại B, C, D. Chuỗi $s_2 =$ `0` không hợp lệ ($S_0$ $\xrightarrow{0}$ $S_1$ (TỪ CHỐI)). *(Lưu ý tương tự Câu 7 Sample 2: $s_4$ cũng không hợp lệ nhưng chỉ có $s_2$ xuất hiện trong 4 lựa chọn nên A là đáp án duy nhất)*.

**Câu 8.** Xét các chuỗi: $s_1 = \text{"10"}$, $s_2 = \text{"1010"}$, $s_3 = \text{"101010"}$, $s_4 = \text{"000"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$ và $s_2$
- B. $s_2$ và $s_3$
- C. $s_3$ và $s_4$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Duy nhất $s_4 =$ `000` bị từ chối ($S_0$ $\xrightarrow{0}$ $S_1$ $\xrightarrow{0}$ $S_1$ $\xrightarrow{0}$ $S_1$ (TỪ CHỐI)).

**Câu 9.** Xét các chuỗi: $s_1 = \text{"10"}$, $s_2 = \text{"1010"}$, $s_3 = \text{"101010"}$, $s_4 = \text{"000"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cả $s_1, s_2, s_3$ đều là chuỗi hợp lệ; chuỗi duy nhất không hợp lệ là $s_4 =$ `000` không nằm trong A, B, C $\implies$ Chọn D.

**Câu 10.** Xét các chuỗi: $s_1 = \text{"10"}$, $s_2 = \text{"000"}$, $s_3 = \text{"1010"}$, $s_4 = \text{"001"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$ và $s_4$
- B. $s_2$ và $s_3$
- C. $s_3$ và $s_4$
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cặp không hợp lệ đúng phải là $s_2$ và $s_4$ (`000` và `001`), không có trong A, B, C $\implies$ Chọn D.

**Câu 11.** Xét các chuỗi: $s_1 = \text{"11111111"}$, $s_2 = \text{"10"}$, $s_3 = \text{"11111110"}$, $s_4 = \text{"1010"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1, s_2$ và $s_3$
- B. $s_1$ và $s_3$
- C. $s_4$
- D. $s_3$ và $s_4$
👉 **Đáp án đúng: B**
- **Giải thích:** $s_1 =$ `11111111` và $s_3 =$ `11111110` đều không đạt trạng thái kết thúc.

**Câu 12.** Xét các chuỗi: $s_1 = \text{"101010"}$, $s_2 = \text{"10101010"}$, $s_3 = \text{"ε"}$, $s_4 = \text{"11111111"}$. Chuỗi nào **KHÔNG** hợp lệ với $L$?
- A. $s_1$
- B. $s_2$
- C. $s_3$
- D. $s_4$
👉 **Đáp án đúng: D**
- **Giải thích:** Chuỗi rỗng $s_3 = \varepsilon$ ĐƯỢC NHẬN (vì trạng thái bắt đầu nằm trong $F$); chỉ có $s_4 =$ `11111111` không hợp lệ.

**Câu 13.** Xét biểu thức chính quy $E_1 = (0 + 10)^*$ (chuỗi ghép từ `0` và `10`). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc ngôn ngữ mô tả bởi $E_1$**?
- A. `10`
- B. `1010`
- C. `0`
- D. `101010`
👉 **Đáp án đúng: C**
- **Giải thích:** `0` thỏa $E_1$ nhưng bị Automaton từ chối ($S_0$ $\xrightarrow{0}$ $S_1$ (TỪ CHỐI)). Ba chuỗi còn lại đều thuộc $L$.

**Câu 14.** Xét biểu thức $E_1 = (0 + 10)^*$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc ngôn ngữ mô tả bởi $E_1$**?
- A. Không có chuỗi nào
- B. `101010`
- C. `11`
- D. `0`
👉 **Đáp án đúng: A**
- **Giải thích:** Mọi chuỗi hợp lệ của Automaton đều thỏa $E_1$ ($L \subseteq L(E_1)$), nên **không có chuỗi nào** thuộc $L$ mà lại ngoài $L(E_1)$!

**Câu 15.** Xét biểu thức $E_2 = (10)^+$ (chuỗi lặp `10` ít nhất 1 lần (KHÔNG chứa $\varepsilon$)). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_2)$**?
- A. `10`
- B. `1010`
- C. `101010`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Do $L(E_2) \subseteq L$ (và cả 3 chuỗi A, B, C đều thuộc $L$), nên không có chuỗi nào trong A, B, C thỏa điều kiện $\implies$ Chọn D.

**Câu 16.** Xét biểu thức $E_2 = (10)^+$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_2)$**?
- A. `10`
- B. $\varepsilon$
- C. `1010`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** $\varepsilon$ thuộc $L$ ($S_0$ (NHẬN)) nhưng không khớp khuôn mẫu của $E_2$. Còn `10` và `1010` đều thuộc cả $L$ lẫn $E_2$.

**Câu 17.** Xét biểu thức $E_2 = (10)^+$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_2)$**?
- A. `10`
- B. `1010`
- C. `101010`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: D**
- **Giải thích:** Cả 3 chuỗi `10`, `1010`, `101010` đều đồng thời thuộc cả $L$ lẫn $E_2$ $\implies$ Chọn D (y hệt bẫy Câu 17 Sample 2!).

**Câu 18.** Xét biểu thức $E_3 = (01)^* + 10$ (chuỗi lặp `01` hoặc đúng chuỗi `10`). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_3)$**?
- A. `10`
- B. `01`
- C. `1010`
- D. `101010`
👉 **Đáp án đúng: B**
- **Giải thích:** `01` thuộc $E_3$ nhưng không được Automaton chấp nhận ($S_0$ $\xrightarrow{0}$ $S_1$ $\xrightarrow{1}$ $S_1$ (TỪ CHỐI)). Các chuỗi kia đều thuộc $L$.

**Câu 19.** Xét biểu thức $E_3 = (01)^* + 10$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_3)$**?
- A. $\varepsilon$
- B. `1010`
- C. `10`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** `1010` thuộc $L$ ($S_0$ $\xrightarrow{1}$ $S_2$ $\xrightarrow{0}$ $S_0$ $\xrightarrow{1}$ $S_2$ $\xrightarrow{0}$ $S_0$ (NHẬN)) nhưng nằm ngoài $E_3$. Hai chuỗi còn lại thuộc cả $L$ và $E_3$.

**Câu 20.** Xét biểu thức $E_3 = (01)^* + 10$. Chuỗi nào **ĐỒNG THỜI KHÔNG** thuộc $L$ và **KHÔNG** thuộc $L(E_3)$?
- A. `1010`
- B. `0`
- C. `01`
- D. $\varepsilon$
👉 **Đáp án đúng: B**
- **Giải thích:** `0` vừa không được Automaton chấp nhận vừa không thuộc $E_3$. Các chuỗi kia đều thuộc $L$ hoặc $E_3$ (hoặc cả hai).

**Câu 21.** Xét biểu thức $E_4 = (0+1)^* 10$ (chuỗi kết thúc bằng cụm `10`). Chuỗi nào **KHÔNG thuộc $L$** nhưng **thuộc $L(E_4)$**?
- A. `10`
- B. `1010`
- C. `010`
- D. `101010`
👉 **Đáp án đúng: C**
- **Giải thích:** `010` thuộc $L(E_4)$ nhưng bị Automaton từ chối ($S_0$ $\xrightarrow{0}$ $S_1$ $\xrightarrow{1}$ $S_1$ $\xrightarrow{0}$ $S_1$ (TỪ CHỐI)). Ba chuỗi còn lại đều thuộc $L$.

**Câu 22.** Xét biểu thức $E_4 = (0+1)^* 10$. Chuỗi nào **thuộc $L$** nhưng **KHÔNG thuộc $L(E_4)$**?
- A. `10`
- B. $\varepsilon$
- C. `1010`
- D. Các chọn lựa khác đều SAI.
👉 **Đáp án đúng: B**
- **Giải thích:** $\varepsilon$ thuộc $L$ ($S_0$ (NHẬN)) nhưng không khớp khuôn mẫu $E_4$.

**Câu 23.** Nếu áp dụng đơn định hóa Automaton đang quan tâm thì DFA đầy đủ thu được có bao nhiêu trạng thái?
- A. 3
- B. 4
- C. 5
- D. 6
👉 **Đáp án đúng: B**
- **Giải thích:** Áp dụng thuật toán xây dựng tập con (Subset Construction) thu được **4 trạng thái** (xem bảng bên dưới): *(Lưu ý: Sơ đồ có xuất hiện tập con rỗng $\emptyset$ làm trạng thái bẫy chết. Nếu một số đề không vẽ trạng thái bẫy này thì còn **3 trạng thái**; theo chuẩn hàm chuyển toàn phần trong Sample 2 của IUH thì tính đủ **4 trạng thái**).*

| Trạng thái DFA | Tập con NFA | Đọc `0` | Đọc `1` | Kết thúc? |
| :---: | :---: | :---: | :---: | :---: |
| $S_0$ (Đầu) | $\{q0, q2\}$ | $S_1$ | $S_2$ | **CÓ** |
| $S_1$ (Bẫy) | $\emptyset$ | $S_1$ | $S_1$ | Không |
| $S_2$ | $\{q1\}$ | $S_0$ | $S_3$ | Không |
| $S_3$ | $\{q2\}$ | $S_1$ | $S_1$ | Không |

**Câu 24.** DFA tối giản tương đương có bao nhiêu trạng thái?
- A. 2
- B. 3
- C. 4
- D. 5
👉 **Đáp án đúng: B**
- **Giải thích:** Có thể gộp từ **4** trạng thái xuống còn **3** trạng thái tương đương. Phân hoạch các nhóm trạng thái tương đương cuối cùng gồm **3 nhóm**: `{$S_0$}`, `{$S_1$, $S_3$}`, `{$S_2$}`. *(Nếu bỏ trạng thái bẫy chết khỏi đồ thị thì còn **2 trạng thái**; tính đủ hàm toàn phần như Sample 2 là **3 trạng thái**).*

---
