# TỔNG HỢP TOÀN BỘ 14 AUTOMATA (ONTAPAUTOMATA.DOCX) & LỜI GIẢI 7 CÂU HỎI TỰ LUẬN WORD
## ĐÚNG THỨ TỰ HÌNH 1 ĐẾN HÌNH 14 TRONG WORD + BẢNG ĐƠN ĐỊNH HÓA & TỐI GIẢN HÓA 100%

> **HỆ THỐNG FILE TRẮC NGHIỆM AUTOMATA CHUẨN MẪU SAMPLE 2 (336 CÂU - MỖI HÌNH ĐỦ 24 CÂU):**
> - **File này (`09_OnTap_Automata...`):** Bảng tra cứu chuẩn xác theo đúng thứ tự **Hình 1 đến Hình 14** trong [OnTapAutomata.docx](file:///d:/folder/rac/iuh/môn/hk1-4/automat/ON_THI_CUOI_KY_MCQ/OnTapAutomata.docx) và lời giải chi tiết 7 câu hỏi tự luận Phần 3 (5 từ nhận, 5 từ loại, hữu hạn/đơn định, RE, văn phạm, đơn định hóa & tối giản hóa).
> - **[09A_Automata_Hinh1_Den_Hinh5_Full_24_MCQ.md](file:///d:/folder/rac/iuh/môn/hk1-4/automat/ON_THI_CUOI_KY_MCQ/09A_Automata_Hinh1_Den_Hinh5_Full_24_MCQ.md):** Hình 1 đến Hình 5 (**120 câu** chuẩn Sample 2).
> - **[09B_Automata_Hinh6_Den_Hinh10_Full_24_MCQ.md](file:///d:/folder/rac/iuh/môn/hk1-4/automat/ON_THI_CUOI_KY_MCQ/09B_Automata_Hinh6_Den_Hinh10_Full_24_MCQ.md):** Hình 6 đến Hình 10 (**120 câu** chuẩn Sample 2).
> - **[09C_Automata_Hinh11_Den_Hinh14_Full_24_MCQ.md](file:///d:/folder/rac/iuh/môn/hk1-4/automat/ON_THI_CUOI_KY_MCQ/09C_Automata_Hinh11_Den_Hinh14_Full_24_MCQ.md):** Hình 11 đến Hình 14 (**96 câu** chuẩn Sample 2, gồm Hình 14 sinh đôi với Đề Sample 2).

---

# PHẦN 1: BẢNG TRA CỨU ĐÚNG THỨ TỰ HÌNH 1 – HÌNH 14 TRONG FILE WORD

| Hình | File ảnh gốc | Phân loại ban đầu | Biểu thức chính quy (RE) | Số trạng thái DFA (Subset) | Số trạng thái tối giản | Bộ đề 24 câu |
| :---: | :--- | :--- | :--- | :---: | :---: | :--- |
| **Hình 01** | [`image_7.png`](file:///d:/folder/rac/iuh/môn/hk1-4/automat/ON_THI_CUOI_KY_MCQ/ontap_images/image_7.png) | Không đơn định (NFA) | $(0+1)^* (00 + 11) (0+1)^*$ | 9 | 4 | File **09A** (24 câu) |
| **Hình 02** | [`image_3.png`](file:///d:/folder/rac/iuh/môn/hk1-4/automat/ON_THI_CUOI_KY_MCQ/ontap_images/image_3.png) | Không đơn định có chuyển rỗng ($\varepsilon$-NFA) | $(0+1)^* 1(0+\varepsilon)1 (0+1)^*$ | 6 | 4 | File **09A** (24 câu) |
| **Hình 03** | [`image_0.png`](file:///d:/folder/rac/iuh/môn/hk1-4/automat/ON_THI_CUOI_KY_MCQ/ontap_images/image_0.png) | Không đơn định (NFA) | $a^3 + a^2(aa)^*$ | 6 | 6 | File **09A** (24 câu) |
| **Hình 04** | [`image_12.jpg`](file:///d:/folder/rac/iuh/môn/hk1-4/automat/ON_THI_CUOI_KY_MCQ/ontap_images/image_12.jpg) | Không đơn định (NFA) | $(a+b)^* b (a+b)^* b (a+b)^*$ | 3 | 3 | File **09A** (24 câu) |
| **Hình 05** | [`image_10.png`](file:///d:/folder/rac/iuh/môn/hk1-4/automat/ON_THI_CUOI_KY_MCQ/ontap_images/image_10.png) | Không đơn định có chuyển rỗng ($\varepsilon$-NFA) | $(10)^*$ | 4 (bỏ bẫy: 3) | 3 (bỏ bẫy: 2) | File **09A** (24 câu) |
| **Hình 06** | [`image_8.png`](file:///d:/folder/rac/iuh/môn/hk1-4/automat/ON_THI_CUOI_KY_MCQ/ontap_images/image_8.png) | Không đơn định (NFA có nhiều trạng thái bắt đầu) | $1 + 1^* 0 (1^* 0 + 1^+)$ | 7 (bỏ bẫy: 6) | 7 (bỏ bẫy: 6) | File **09B** (24 câu) |
| **Hình 07** | [`image_4.jpg`](file:///d:/folder/rac/iuh/môn/hk1-4/automat/ON_THI_CUOI_KY_MCQ/ontap_images/image_4.jpg) | Đơn định thiếu cung (Partial DFA - cần thêm trạng thái bẫy $\emptyset$ để thành DFA đầy đủ) | $(01 + 001)^* 00$ | 4 (bỏ bẫy: 3) | 4 (bỏ bẫy: 3) | File **09B** (24 câu) |
| **Hình 08** | [`image_1.jpg`](file:///d:/folder/rac/iuh/môn/hk1-4/automat/ON_THI_CUOI_KY_MCQ/ontap_images/image_1.jpg) | Không đơn định (NFA) | $0(1^+ + 21)$ | 6 (bỏ bẫy: 5) | 6 (bỏ bẫy: 5) | File **09B** (24 câu) |
| **Hình 09** | [`image_13.png`](file:///d:/folder/rac/iuh/môn/hk1-4/automat/ON_THI_CUOI_KY_MCQ/ontap_images/image_13.png) | Đơn định đầy đủ (Complete DFA) | $a^* b (a+b)^*$ | 2 | 2 | File **09B** (24 câu) |
| **Hình 10** | [`image_9.png`](file:///d:/folder/rac/iuh/môn/hk1-4/automat/ON_THI_CUOI_KY_MCQ/ontap_images/image_9.png) | Không đơn định (NFA) | $(a+b)^* b (b^+ a)^* b^*$ | 3 | 3 | File **09B** (24 câu) |
| **Hình 11** | [`image_6.png`](file:///d:/folder/rac/iuh/môn/hk1-4/automat/ON_THI_CUOI_KY_MCQ/ontap_images/image_6.png) | Đơn định đầy đủ (Complete DFA) | $(0^* 1^+ (00 + 010))^* 0^* 1^+ (011^+)^* 01$ | 4 | 4 | File **09C** (24 câu) |
| **Hình 12** | [`image_5.png`](file:///d:/folder/rac/iuh/môn/hk1-4/automat/ON_THI_CUOI_KY_MCQ/ontap_images/image_5.png) | Không đơn định (NFA) | $b^* a (a + bb)^* (\varepsilon + ba(a+b)^*)$ | 4 | 4 | File **09C** (24 câu) |
| **Hình 13** | [`image_2.png`](file:///d:/folder/rac/iuh/môn/hk1-4/automat/ON_THI_CUOI_KY_MCQ/ontap_images/image_2.png) | Đơn định thiếu cung (Partial DFA - cần thêm trạng thái bẫy $\emptyset$ để thành DFA đầy đủ) | $(a + bbb)^* (b + bb)$ | 4 (bỏ bẫy: 3) | 4 (bỏ bẫy: 3) | File **09C** (24 câu) |
| **Hình 14** | [`image_11.png`](file:///d:/folder/rac/iuh/môn/hk1-4/automat/ON_THI_CUOI_KY_MCQ/ontap_images/image_11.png) | Không đơn định có chuyển rỗng ($\varepsilon$-NFA) | $a^* b (bb)^* (a a^* b (bb)^*)^*$ | 4 (bỏ bẫy: 3) | 4 (bỏ bẫy: 3) | File **09C** (24 câu) |

---

# PHẦN 2: GIẢI TRỌN GÓI 7 CÂU HỎI TỰ LUẬN WORD + BẢNG ĐƠN ĐỊNH HÓA CHO CẢ 14 HÌNH

### Hình 01 (`ontap_images/image_7.png`)
1. **5 từ được đoán nhận:** `00`, `11`, `000`, `001`, `011`
2. **5 từ KHÔNG được đoán nhận:** $\varepsilon$, `0`, `1`, `01`, `10`
3. **Có hữu hạn không? Có đơn định không?** Có (tập trạng thái hữu hạn). Tính chất ban đầu: **Không đơn định (NFA)**.
4. **Mô tả ngôn ngữ & RE:** Tập hợp mọi chuỗi nhị phân chứa ít nhất một cặp ký tự giống nhau đứng cạnh nhau (`00` hoặc `11`). $\implies$ RE: $(0+1)^* (00 + 11) (0+1)^*$.
5. **Văn phạm chính quy tương đương:** $S \to 0S \mid 1S \mid 0A \mid 1B,\ A \to 0C,\ B \to 1C,\ C \to 0C \mid 1C \mid \varepsilon$
6. **Tối giản chưa? DFA sau đơn định hóa & tối giản:** DFA đầy đủ có **9** trạng thái; DFA tối giản có **4** trạng thái.

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

### Hình 02 (`ontap_images/image_3.png`)
1. **5 từ được đoán nhận:** `11`, `011`, `101`, `110`, `111`
2. **5 từ KHÔNG được đoán nhận:** $\varepsilon$, `0`, `1`, `00`, `01`
3. **Có hữu hạn không? Có đơn định không?** Có (tập trạng thái hữu hạn). Tính chất ban đầu: **Không đơn định có chuyển rỗng ($\varepsilon$-NFA)**.
4. **Mô tả ngôn ngữ & RE:** Tập hợp mọi chuỗi nhị phân có chứa chuỗi con **`11`** hoặc **`101`**. $\implies$ RE: $(0+1)^* 1(0+\varepsilon)1 (0+1)^*$.
5. **Văn phạm chính quy tương đương:** $S \to 0S \mid 1S \mid 1A,\ A \to 0B \mid B,\ B \to 1C,\ C \to 0C \mid 1C \mid \varepsilon$
6. **Tối giản chưa? DFA sau đơn định hóa & tối giản:** DFA đầy đủ có **6** trạng thái; DFA tối giản có **4** trạng thái.

| Trạng thái DFA | Tập con NFA | Đọc `0` | Đọc `1` | Kết thúc? |
| :---: | :---: | :---: | :---: | :---: |
| $S_0$ (Đầu) | $\{q0\}$ | $S_0$ | $S_1$ | Không |
| $S_1$ | $\{q0, q1, q2\}$ | $S_2$ | $S_3$ | Không |
| $S_2$ | $\{q0, q2\}$ | $S_0$ | $S_3$ | Không |
| $S_3$ | $\{q0, q1, q2, q3\}$ | $S_4$ | $S_3$ | **CÓ** |
| $S_4$ | $\{q0, q2, q3\}$ | $S_5$ | $S_3$ | **CÓ** |
| $S_5$ | $\{q0, q3\}$ | $S_5$ | $S_3$ | **CÓ** |

### Hình 03 (`ontap_images/image_0.png`)
1. **5 từ được đoán nhận:** `aa`, `aaa`, `aaaa`, `aaaaaa`, `aaaaaaaa`
2. **5 từ KHÔNG được đoán nhận:** $\varepsilon$, `a`, `aaaaa`, `aaaaaaa`, `aaaaaaaaa`
3. **Có hữu hạn không? Có đơn định không?** Có (tập trạng thái hữu hạn). Tính chất ban đầu: **Không đơn định (NFA)**.
4. **Mô tả ngôn ngữ & RE:** Tập hợp gồm chuỗi `aaa` và tất cả các chuỗi chữ `a` có độ dài chẵn $\ge 2$ ($a^2, a^3, a^4, a^6, a^8, \dots$). $\implies$ RE: $a^3 + a^2(aa)^*$.
5. **Văn phạm chính quy tương đương:** $S \to aaa \mid aaA,\ A \to aaA \mid \varepsilon$
6. **Tối giản chưa? DFA sau đơn định hóa & tối giản:** DFA đầy đủ có **6** trạng thái; DFA tối giản có **6** trạng thái.

| Trạng thái DFA | Tập con NFA | Đọc `a` | Kết thúc? |
| :---: | :---: | :---: | :---: |
| $S_0$ (Đầu) | $\{q0\}$ | $S_1$ | Không |
| $S_1$ | $\{q1, q4\}$ | $S_2$ | Không |
| $S_2$ | $\{q2, q5\}$ | $S_3$ | **CÓ** |
| $S_3$ | $\{q3, q4\}$ | $S_4$ | **CÓ** |
| $S_4$ | $\{q5\}$ | $S_5$ | **CÓ** |
| $S_5$ | $\{q4\}$ | $S_4$ | Không |

### Hình 04 (`ontap_images/image_12.jpg`)
1. **5 từ được đoán nhận:** `bb`, `abb`, `bab`, `bba`, `bbb`
2. **5 từ KHÔNG được đoán nhận:** $\varepsilon$, `a`, `b`, `aa`, `ab`
3. **Có hữu hạn không? Có đơn định không?** Có (tập trạng thái hữu hạn). Tính chất ban đầu: **Không đơn định (NFA)**.
4. **Mô tả ngôn ngữ & RE:** Tập hợp mọi chuỗi trên $\{a, b\}$ có chứa **ít nhất 2 ký tự `b`** (vị trí tùy ý). $\implies$ RE: $(a+b)^* b (a+b)^* b (a+b)^*$.
5. **Văn phạm chính quy tương đương:** $S \to aS \mid bS \mid bA,\ A \to aA \mid bA \mid bB,\ B \to aB \mid bB \mid \varepsilon$
6. **Tối giản chưa? DFA sau đơn định hóa & tối giản:** DFA đầy đủ có **3** trạng thái; DFA tối giản có **3** trạng thái.

| Trạng thái DFA | Tập con NFA | Đọc `a` | Đọc `b` | Kết thúc? |
| :---: | :---: | :---: | :---: | :---: |
| $S_0$ (Đầu) | $\{q0\}$ | $S_0$ | $S_1$ | Không |
| $S_1$ | $\{q0, q1\}$ | $S_1$ | $S_2$ | Không |
| $S_2$ | $\{q0, q1, q2\}$ | $S_2$ | $S_2$ | **CÓ** |

### Hình 05 (`ontap_images/image_10.png`)
1. **5 từ được đoán nhận:** $\varepsilon$, `10`, `1010`, `101010`, `10101010`
2. **5 từ KHÔNG được đoán nhận:** `0`, `1`, `00`, `01`, `11`
3. **Có hữu hạn không? Có đơn định không?** Có (tập trạng thái hữu hạn). Tính chất ban đầu: **Không đơn định có chuyển rỗng ($\varepsilon$-NFA)**.
4. **Mô tả ngôn ngữ & RE:** Tập hợp gồm chuỗi rỗng $\varepsilon$ và các chuỗi lặp lại cụm `10`: $\{\varepsilon, 10, 1010, 101010, \dots\}$. *(Cẩn thận bẫy: $q_2$ là trạng thái ngõ cụt không kết thúc, mũi tên $\varepsilon$ sang $q_2$ không làm chuỗi dài thêm hay kết thúc được!)* $\implies$ RE: $(10)^*$.
5. **Văn phạm chính quy tương đương:** $S \to 10S \mid \varepsilon$ (hoặc $S \to 1A \mid \varepsilon,\ A \to 0S$)
6. **Tối giản chưa? DFA sau đơn định hóa & tối giản:** DFA đầy đủ có **4 (bỏ bẫy: 3)** trạng thái; DFA tối giản có **3 (bỏ bẫy: 2)** trạng thái.

| Trạng thái DFA | Tập con NFA | Đọc `0` | Đọc `1` | Kết thúc? |
| :---: | :---: | :---: | :---: | :---: |
| $S_0$ (Đầu) | $\{q0, q2\}$ | $S_1$ | $S_2$ | **CÓ** |
| $S_1$ (Bẫy) | $\emptyset$ | $S_1$ | $S_1$ | Không |
| $S_2$ | $\{q1\}$ | $S_0$ | $S_3$ | Không |
| $S_3$ | $\{q2\}$ | $S_1$ | $S_1$ | Không |

### Hình 06 (`ontap_images/image_8.png`)
1. **5 từ được đoán nhận:** `1`, `00`, `01`, `010`, `011`
2. **5 từ KHÔNG được đoán nhận:** $\varepsilon$, `0`, `10`, `11`, `000`
3. **Có hữu hạn không? Có đơn định không?** Có (tập trạng thái hữu hạn). Tính chất ban đầu: **Không đơn định (NFA có nhiều trạng thái bắt đầu)**.
4. **Mô tả ngôn ngữ & RE:** Hoặc chuỗi `1` (từ điểm đầu $q_1 \xrightarrow{1} q_3$), hoặc sau cụm $1^* 0$ đầu tiên là $1^* 0$ hay $1^+$ (ví dụ `00`, `01`, `100`, `0110`, `1011`). $\implies$ RE: $1 + 1^* 0 (1^* 0 + 1^+)$.
5. **Văn phạm chính quy tương đương:** $S \to 1 \mid 1S \mid 0A,\ A \to 0 \mid 1 \mid 1A$
6. **Tối giản chưa? DFA sau đơn định hóa & tối giản:** DFA đầy đủ có **7 (bỏ bẫy: 6)** trạng thái; DFA tối giản có **7 (bỏ bẫy: 6)** trạng thái.

| Trạng thái DFA | Tập con NFA | Đọc `0` | Đọc `1` | Kết thúc? |
| :---: | :---: | :---: | :---: | :---: |
| $S_0$ (Đầu) | $\{q0, q1\}$ | $S_1$ | $S_2$ | Không |
| $S_1$ | $\{q1, q2\}$ | $S_3$ | $S_4$ | Không |
| $S_2$ | $\{q0, q3\}$ | $S_1$ | $S_5$ | **CÓ** |
| $S_3$ | $\{q3\}$ | $S_6$ | $S_6$ | **CÓ** |
| $S_4$ | $\{q1, q2, q3\}$ | $S_3$ | $S_4$ | **CÓ** |
| $S_5$ | $\{q0\}$ | $S_1$ | $S_5$ | Không |
| $S_6$ (Bẫy) | $\emptyset$ | $S_6$ | $S_6$ | Không |

### Hình 07 (`ontap_images/image_4.jpg`)
1. **5 từ được đoán nhận:** `00`, `0100`, `00100`, `010100`, `0010100`
2. **5 từ KHÔNG được đoán nhận:** $\varepsilon$, `0`, `1`, `01`, `10`
3. **Có hữu hạn không? Có đơn định không?** Có (tập trạng thái hữu hạn). Tính chất ban đầu: **Đơn định thiếu cung (Partial DFA - cần thêm trạng thái bẫy $\emptyset$ để thành DFA đầy đủ)**.
4. **Mô tả ngôn ngữ & RE:** Chuỗi ghép bởi các khối `01` hoặc `001`, kết thúc bắt buộc bằng **`00`**. *(Bẫy: Không có đường đọc `1` tại $q_0$ và không có đường đọc `0` tại $q_2$ nên không chứa `000` và không chứa `11`!)* $\implies$ RE: $(01 + 001)^* 00$.
5. **Văn phạm chính quy tương đương:** $S \to 0A,\ A \to 1S \mid 0B,\ B \to 1S \mid \varepsilon$
6. **Tối giản chưa? DFA sau đơn định hóa & tối giản:** DFA đầy đủ có **4 (bỏ bẫy: 3)** trạng thái; DFA tối giản có **4 (bỏ bẫy: 3)** trạng thái.

| Trạng thái DFA | Tập con NFA | Đọc `0` | Đọc `1` | Kết thúc? |
| :---: | :---: | :---: | :---: | :---: |
| $S_0$ (Đầu) | $\{q0\}$ | $S_1$ | $S_2$ | Không |
| $S_1$ | $\{q1\}$ | $S_3$ | $S_0$ | Không |
| $S_2$ (Bẫy) | $\emptyset$ | $S_2$ | $S_2$ | Không |
| $S_3$ | $\{q2\}$ | $S_2$ | $S_0$ | **CÓ** |

### Hình 08 (`ontap_images/image_1.jpg`)
1. **5 từ được đoán nhận:** `01`, `011`, `021`, `0111`, `01111`
2. **5 từ KHÔNG được đoán nhận:** $\varepsilon$, `0`, `1`, `2`, `00`
3. **Có hữu hạn không? Có đơn định không?** Có (tập trạng thái hữu hạn). Tính chất ban đầu: **Không đơn định (NFA)**.
4. **Mô tả ngôn ngữ & RE:** Bắt đầu bằng đúng một chữ `0`, tiếp theo là một hay nhiều chữ `1` (`01, 011, 0111, ...`), HOẶC chuỗi duy nhất `021`. $\implies$ RE: $0(1^+ + 21)$.
5. **Văn phạm chính quy tương đương:** $S \to 0A \mid 021,\ A \to 1A \mid 1$
6. **Tối giản chưa? DFA sau đơn định hóa & tối giản:** DFA đầy đủ có **6 (bỏ bẫy: 5)** trạng thái; DFA tối giản có **6 (bỏ bẫy: 5)** trạng thái.

| Trạng thái DFA | Tập con NFA | Đọc `0` | Đọc `1` | Đọc `2` | Kết thúc? |
| :---: | :---: | :---: | :---: | :---: | :---: |
| $S_0$ (Đầu) | $\{q0\}$ | $S_1$ | $S_2$ | $S_2$ | Không |
| $S_1$ | $\{q1, q3\}$ | $S_2$ | $S_3$ | $S_4$ | Không |
| $S_2$ (Bẫy) | $\emptyset$ | $S_2$ | $S_2$ | $S_2$ | Không |
| $S_3$ | $\{q1, q2\}$ | $S_2$ | $S_3$ | $S_2$ | **CÓ** |
| $S_4$ | $\{q4\}$ | $S_2$ | $S_5$ | $S_2$ | Không |
| $S_5$ | $\{q2\}$ | $S_2$ | $S_2$ | $S_2$ | **CÓ** |

### Hình 09 (`ontap_images/image_13.png`)
1. **5 từ được đoán nhận:** `b`, `ab`, `ba`, `bb`, `aab`
2. **5 từ KHÔNG được đoán nhận:** $\varepsilon$, `a`, `aa`, `aaa`, `aaaa`
3. **Có hữu hạn không? Có đơn định không?** Có (tập trạng thái hữu hạn). Tính chất ban đầu: **Đơn định đầy đủ (Complete DFA)**.
4. **Mô tả ngôn ngữ & RE:** Tập hợp các chuỗi chứa **ít nhất 1 chữ `b`**. *(Cực kỳ tinh vi: $t_1$ và $T_3$ không có mũi tên đi tới từ trạng thái khởi đầu $t_0$ nên là trạng thái chết không tới được — unreachable states — phải loại bỏ khi đơn định hóa/tối giản hóa!)* $\implies$ RE: $a^* b (a+b)^*$.
5. **Văn phạm chính quy tương đương:** $S \to aS \mid bA,\ A \to aA \mid bA \mid \varepsilon$
6. **Tối giản chưa? DFA sau đơn định hóa & tối giản:** DFA đầy đủ có **2** trạng thái; DFA tối giản có **2** trạng thái.

| Trạng thái DFA | Tập con NFA | Đọc `a` | Đọc `b` | Kết thúc? |
| :---: | :---: | :---: | :---: | :---: |
| $S_0$ (Đầu) | $\{t0\}$ | $S_0$ | $S_1$ | Không |
| $S_1$ | $\{t2\}$ | $S_1$ | $S_1$ | **CÓ** |

### Hình 10 (`ontap_images/image_9.png`)
1. **5 từ được đoán nhận:** `b`, `ab`, `bb`, `aab`, `abb`
2. **5 từ KHÔNG được đoán nhận:** $\varepsilon$, `a`, `aa`, `ba`, `aaa`
3. **Có hữu hạn không? Có đơn định không?** Có (tập trạng thái hữu hạn). Tính chất ban đầu: **Không đơn định (NFA)**.
4. **Mô tả ngôn ngữ & RE:** Nhận mọi chuỗi kết thúc bằng **`b`**, HOẶC kết thúc bằng cụm `bba`, `bbba`, `bbaba` (cụ thể: sau chữ `b` đưa vào $q_1$ có các chu trình $b^+ a$ rồi kết thúc bằng $b^*$). Đuôi `ba` đơn lẻ hoặc chuỗi toàn `a` bị từ chối! $\implies$ RE: $(a+b)^* b (b^+ a)^* b^*$.
5. **Văn phạm chính quy tương đương:** $S_0 \to aS_0 \mid bS_1,\ S_1 \to aS_0 \mid bS_2 \mid \varepsilon,\ S_2 \to aS_1 \mid bS_2 \mid \varepsilon$
6. **Tối giản chưa? DFA sau đơn định hóa & tối giản:** DFA đầy đủ có **3** trạng thái; DFA tối giản có **3** trạng thái.

| Trạng thái DFA | Tập con NFA | Đọc `a` | Đọc `b` | Kết thúc? |
| :---: | :---: | :---: | :---: | :---: |
| $S_0$ (Đầu) | $\{q0\}$ | $S_0$ | $S_1$ | Không |
| $S_1$ | $\{q0, q1\}$ | $S_0$ | $S_2$ | **CÓ** |
| $S_2$ | $\{q0, q1, q2\}$ | $S_1$ | $S_2$ | **CÓ** |

### Hình 11 (`ontap_images/image_6.png`)
1. **5 từ được đoán nhận:** `101`, `0101`, `1101`, `00101`, `01101`
2. **5 từ KHÔNG được đoán nhận:** $\varepsilon$, `0`, `1`, `00`, `01`
3. **Có hữu hạn không? Có đơn định không?** Có (tập trạng thái hữu hạn). Tính chất ban đầu: **Đơn định đầy đủ (Complete DFA)**.
4. **Mô tả ngôn ngữ & RE:** Kết thúc bằng `101`, **NHƯNG LƯU Ý BẪY CỰC ĐỘC**: tại $q_4$, cạnh `0` quay thẳng về đầu $q_1$ (reset toàn bộ) chứ không về $q_3$! Vì vậy hai cụm `101` không thể chồng nhau — ví dụ `10101` **BỊ TỪ CHỐI**, trong khi `101`, `1101`, `101101` được nhận! $\implies$ RE: $(0^* 1^+ (00 + 010))^* 0^* 1^+ (011^+)^* 01$.
5. **Văn phạm chính quy tương đương:** $S_1 \to 0S_1 \mid 1S_2,\ S_2 \to 1S_2 \mid 0S_3,\ S_3 \to 0S_1 \mid 1S_4,\ S_4 \to 0S_1 \mid 1S_2 \mid \varepsilon$
6. **Tối giản chưa? DFA sau đơn định hóa & tối giản:** DFA đầy đủ có **4** trạng thái; DFA tối giản có **4** trạng thái.

| Trạng thái DFA | Tập con NFA | Đọc `0` | Đọc `1` | Kết thúc? |
| :---: | :---: | :---: | :---: | :---: |
| $S_0$ (Đầu) | $\{q1\}$ | $S_0$ | $S_1$ | Không |
| $S_1$ | $\{q2\}$ | $S_2$ | $S_1$ | Không |
| $S_2$ | $\{q3\}$ | $S_0$ | $S_3$ | Không |
| $S_3$ | $\{q4\}$ | $S_0$ | $S_1$ | **CÓ** |

### Hình 12 (`ontap_images/image_5.png`)
1. **5 từ được đoán nhận:** `a`, `aa`, `ba`, `aaa`, `aba`
2. **5 từ KHÔNG được đoán nhận:** $\varepsilon$, `b`, `ab`, `bb`, `aab`
3. **Có hữu hạn không? Có đơn định không?** Có (tập trạng thái hữu hạn). Tính chất ban đầu: **Không đơn định (NFA)**.
4. **Mô tả ngôn ngữ & RE:** Chấp nhận chuỗi kết thúc bằng `a` (hoặc `abb`, `abbbb`...), HOẶC bất kỳ chuỗi nào có đi qua chu trình tạo `aba` (từ đó đạt tập trạng thái kết thúc vĩnh viễn). $\implies$ RE: $b^* a (a + bb)^* (\varepsilon + ba(a+b)^*)$.
5. **Văn phạm chính quy tương đương:** $S_0 \to bS_0 \mid aS_1,\ S_1 \to aS_1 \mid bS_2 \mid \varepsilon,\ S_2 \to bS_1 \mid aS_3,\ S_3 \to aS_3 \mid bS_3 \mid \varepsilon$
6. **Tối giản chưa? DFA sau đơn định hóa & tối giản:** DFA đầy đủ có **4** trạng thái; DFA tối giản có **4** trạng thái.

| Trạng thái DFA | Tập con NFA | Đọc `a` | Đọc `b` | Kết thúc? |
| :---: | :---: | :---: | :---: | :---: |
| $S_0$ (Đầu) | $\{q0\}$ | $S_1$ | $S_0$ | Không |
| $S_1$ | $\{q0, q1\}$ | $S_1$ | $S_2$ | **CÓ** |
| $S_2$ | $\{q0, q2\}$ | $S_3$ | $S_1$ | Không |
| $S_3$ | $\{q0, q1, q2\}$ | $S_3$ | $S_3$ | **CÓ** |

### Hình 13 (`ontap_images/image_2.png`)
1. **5 từ được đoán nhận:** `b`, `ab`, `bb`, `aab`, `abb`
2. **5 từ KHÔNG được đoán nhận:** $\varepsilon$, `a`, `aa`, `ba`, `aaa`
3. **Có hữu hạn không? Có đơn định không?** Có (tập trạng thái hữu hạn). Tính chất ban đầu: **Đơn định thiếu cung (Partial DFA - cần thêm trạng thái bẫy $\emptyset$ để thành DFA đầy đủ)**.
4. **Mô tả ngôn ngữ & RE:** Các khối lặp lại từ $q_0$ gồm `a` hoặc `bbb`, cuối cùng kết thúc ở $q_1$ (đọc thêm `b`) hoặc $q_2$ (đọc thêm `bb`). *(Lưu ý cực kỳ quan trọng: tại $q_1$ và $q_2$ KHÔNG có cạnh đọc `a`, nên `bab` hay `bba` đều bị từ chối, còn `bbbab` hợp lệ!)* $\implies$ RE: $(a + bbb)^* (b + bb)$.
5. **Văn phạm chính quy tương đương:** $S_0 \to aS_0 \mid bS_1,\ S_1 \to bS_2 \mid \varepsilon,\ S_2 \to bS_0 \mid \varepsilon$
6. **Tối giản chưa? DFA sau đơn định hóa & tối giản:** DFA đầy đủ có **4 (bỏ bẫy: 3)** trạng thái; DFA tối giản có **4 (bỏ bẫy: 3)** trạng thái.

| Trạng thái DFA | Tập con NFA | Đọc `a` | Đọc `b` | Kết thúc? |
| :---: | :---: | :---: | :---: | :---: |
| $S_0$ (Đầu) | $\{q0\}$ | $S_0$ | $S_1$ | Không |
| $S_1$ | $\{q1\}$ | $S_2$ | $S_3$ | **CÓ** |
| $S_2$ (Bẫy) | $\emptyset$ | $S_2$ | $S_2$ | Không |
| $S_3$ | $\{q2\}$ | $S_2$ | $S_0$ | **CÓ** |

### Hình 14 (`ontap_images/image_11.png`)
1. **5 từ được đoán nhận:** `b`, `ab`, `aab`, `bab`, `bbb`
2. **5 từ KHÔNG được đoán nhận:** $\varepsilon$, `a`, `aa`, `ba`, `bb`
3. **Có hữu hạn không? Có đơn định không?** Có (tập trạng thái hữu hạn). Tính chất ban đầu: **Không đơn định có chuyển rỗng ($\varepsilon$-NFA)**.
4. **Mô tả ngôn ngữ & RE:** Chuỗi kết thúc bằng số lẻ chữ `b` ($b, bbb, \dots$), sau các đoạn toàn `a`, và không bao giờ có chữ `a` đứng ngay sau số chẵn chữ `b` (như `bba` bị loại!). $\implies$ RE: $a^* b (bb)^* (a a^* b (bb)^*)^*$.
5. **Văn phạm chính quy tương đương:** $S_0 \to aS_0 \mid bS_2,\ S_2 \to aS_0 \mid bS_1 \mid \varepsilon,\ S_1 \to bS_2$
6. **Tối giản chưa? DFA sau đơn định hóa & tối giản:** DFA đầy đủ có **4 (bỏ bẫy: 3)** trạng thái; DFA tối giản có **4 (bỏ bẫy: 3)** trạng thái.

| Trạng thái DFA | Tập con NFA | Đọc `a` | Đọc `b` | Kết thúc? |
| :---: | :---: | :---: | :---: | :---: |
| $S_0$ (Đầu) | $\{q0, q1\}$ | $S_0$ | $S_1$ | Không |
| $S_1$ | $\{q2\}$ | $S_0$ | $S_2$ | **CÓ** |
| $S_2$ | $\{q1\}$ | $S_3$ | $S_1$ | Không |
| $S_3$ (Bẫy) | $\emptyset$ | $S_3$ | $S_3$ | Không |
