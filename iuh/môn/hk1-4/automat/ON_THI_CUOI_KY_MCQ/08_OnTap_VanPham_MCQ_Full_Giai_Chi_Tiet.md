# TỔNG HỢP 19 VĂN PHẠM & GIẢI FULL PHẦN 2 BIỂU THỨC CHÍNH QUY (ONTAPAUTOMATA.DOCX)
## BẢNG TRA CỨU TOÀN DIỆN + LỜI GIẢI 10 BIỂU THỨC CHÍNH QUY + 24 CÂU MCQ CHUẨN THI

> **HỆ THỐNG FILE ÔN VĂN PHẠM TRỌN BỘ (ĐÃ SỬA SẠCH LỖI & KIỂM CHỨNG TOÁN HỌC 100%):**
> 1. **File này (`08_OnTap...`):** Bảng tra cứu 19 Văn phạm ($G_1$–$G_{19}$), giải đáp 8 câu hỏi Word, và làm trọn vẹn **Phần 2 (10 Biểu thức chính quy + 24 câu MCQ)**.
> 2. **[08A_VanPham_CFL_DoiXung_G1_G2_G5_G6_G10_G15_G16_Full_MCQ.md](file:///d:/folder/rac/iuh/môn/hk1-4/automat/ON_THI_CUOI_KY_MCQ/08A_VanPham_CFL_DoiXung_G1_G2_G5_G6_G10_G15_G16_Full_MCQ.md):** **182 câu** (mỗi văn phạm đủ 24 câu Sample 1 + 2 câu Word) cho 7 văn phạm CFG độc đáo.
> 3. **[08B_VanPham_ChinhQuy_Va_DacBiet_G3_G4_G7_G8_G14_G17_G18_Full_MCQ.md](file:///d:/folder/rac/iuh/môn/hk1-4/automat/ON_THI_CUOI_KY_MCQ/08B_VanPham_ChinhQuy_Va_DacBiet_G3_G4_G7_G8_G14_G17_G18_Full_MCQ.md):** **182 câu** (mỗi văn phạm đủ 24 câu Sample 1 + 2 câu Word) cho 7 văn phạm chính quy & đặc biệt + phân tích $G_{19}$.

---

# PHẦN 1: BẢNG TỔNG HỢP SIÊU TỐC TOÀN BỘ 19 VĂN PHẠM ($G_1$ ĐẾN $G_{19}$)

| Văn phạm | Dạng chuỗi tổng quát $L(G)$ | Chomsky | Máy đoán nhận | Trạng thái trong bộ đề MCQ |
| :--- | :--- | :---: | :---: | :--- |
| **$G_1$** | $\{0^n 1^n \mid n \ge 0\}$ | Loại 2 | PDA | **Có bộ riêng 26 câu ở File 08A** |
| **$G_2$** | $\{a^n b^{n+1} \mid n \ge 0\}$ | Loại 2 | PDA | **Có bộ riêng 26 câu ở File 08A** |
| **$G_3$** | $\{a^i b^j c^k \mid i,j,k \ge 1\} = a^+ b^+ c^+$ | **Loại 3** | DFA/NFA | **Có bộ riêng 26 câu ở File 08B** *(Bẫy: luật CFG nhưng ngôn ngữ Regular!)* |
| **$G_4$** | $\{a^n b^n c^n \mid n \ge 1\}$ | **Loại 1** | LBA | **Có bộ riêng 26 câu ở File 08B** |
| **$G_5$** | $\{a^n b^n a^m \mid n, m \ge 1\}$ | Loại 2 | PDA | **Có bộ riêng 26 câu ở File 08A** |
| **$G_6$** | $\{w \in \{0,1\}^* \mid \#0(w) = \#1(w)\}$ | Loại 2 | PDA | **Có bộ riêng 26 câu ở File 08A** *(Văn phạm mơ hồ)* |
| **$G_7$** | $\{1^{2k} \mid k \ge 0\}$ | Loại 3 | DFA (2 states) | **Có bộ riêng 26 câu ở File 08B** |
| **$G_8$** | $0(0+1)^* 0$ | Loại 3 | DFA (4 states) | **Có bộ riêng 26 câu ở File 08B** |
| **$G_9$** | $\{a^n b^n \mid n \ge 1\}$ | Loại 2 | PDA | *Tựa $G_1$ (đổi 0,1 $\to$ a,b và bỏ $\varepsilon$)* — gộp chung $G_1$ |
| **$G_{10}$** | $\{a^n c b^{2n} \mid n \ge 0\}$ | Loại 2 | PDA | **Có bộ riêng 26 câu ở File 08A** |
| **$G_{11}$** | $\{a^{2n} c b^n \mid n \ge 0\}$ | Loại 2 | PDA | *Tựa $G_{10}$ (đảo vai trò $a \leftrightarrow b$)* — gộp chung $G_{10}$ |
| **$G_{12}$** | $\{a^n b^n \mid n \ge 1\}$ | Loại 2 | PDA | **Giống hệt $G_9$ ($G_{12} \equiv G_9$)** — gộp chung $G_1$ |
| **$G_{13}$** | $\{c^n \mid n \ge 1\} = c^+$ | Loại 3 | DFA (2 states) | *Đơn giản & cùng nhóm 1 ký tự với $G_7$* — ghi chú ở $G_7$ |
| **$G_{14}$** | $\{0, 01, 011, 0111\}$ (hữu hạn 4 từ) | Loại 3 | DFA | **Có bộ riêng 26 câu ở File 08B** |
| **$G_{15}$** | $\{0^{n+1} 1^m 1^{n+1} \mid n \ge 0, m \ge 1\}$ | Loại 2 | PDA | **Có bộ riêng 26 câu ở File 08A** |
| **$G_{16}$** | $\{0^i 1^j \mid i \ne j,\ i,j \ge 0\}$ | Loại 2 | PDA | **Có bộ riêng 26 câu ở File 08A** |
| **$G_{17}$** | $\{w \in \{0,1\}^+ \mid w\text{ không chứa }00\}$ | Loại 3 | DFA | **Có bộ riêng 26 câu ở File 08B** |
| **$G_{18}$** | $\{w\}$ mở rộng $G_{17}$ bằng cặp $A \to 1A0$ | Loại 2 | PDA | **Có bộ riêng 26 câu ở File 08B** *(Chứa thêm `01100`, `011100`...)* |
| **$G_{19}$** | $\emptyset$ (Bất biến $\#S + \#A$ luôn lẻ) | Loại 1/0 | Turing/LBA | **Phân tích riêng cuối File 08B** |

> *(Chỉnh nhẹ ghi chú: $G_{15}$ đặt trong **File 08A**).*

---

# PHẦN 2: GIẢI TRỌN GÓI 10 BIỂU THỨC TRONG FILE WORD (`OnTapAutomata.docx`)

Trên bảng chữ cái $\Sigma = \{a, b, c\}$, file Word cho 10 biểu thức sau:

| STT | Biểu thức trong Word | Có phải RE hợp lệ? | Ngôn ngữ mô tả $L(E)$ & Văn phạm chính quy tương đương |
| :---: | :--- | :---: | :--- |
| **1** | `(ab)c` | **CÓ** | Tập hữu hạn chỉ gồm **đúng 1 từ** `{abc}`. Văn phạm: $S \to abc$. |
| **2** | `(c* (a* + b*) c*)* ((ab)+c+)*  c* (a* + b*) c*)*)*` | **KHÔNG!** | **LỖI CÚ PHÁP NGHIÊM TRỌNG:** Dư dấu đóng ngoặc `)*)*` ở cuối (3 dấu `(` nhưng tới 5 dấu `)` không khớp!), nên **KHÔNG PHẢI** biểu thức chính quy! |
| **3** | `abc*` | **CÓ** | Bắt đầu bằng `ab`, theo sau bởi $\ge 0$ chữ `c`: $\{ab c^n \mid n \ge 0\}$. Văn phạm: $S \to abC,\ C \to cC \mid \varepsilon$. |
| **4** | `(a + b)* c*` | **CÓ** | Chuỗi gồm tùy ý `a, b` ở đầu rồi đến tùy ý `c` ở cuối (không có `c` đứng trước `a` hay `b`). Văn phạm: $S \to aS \mid bS \mid C \mid \varepsilon,\ C \to cC \mid \varepsilon$. |
| **5** | `(a + b)* (c (a + b)* c)* (a + b)*` | **CÓ** | **TRỌNG TÂM THI:** Tập mọi chuỗi trên $\{a, b, c\}$ có **số lượng chữ `c` là SỐ CHẴN** ($0, 2, 4, \dots$). Văn phạm: $S \to aS \mid bS \mid cA \mid \varepsilon,\ A \to aA \mid bA \mid cS$. |
| **6** | `(a + b + c)*` | **CÓ** | Mọi chuỗi bất kỳ (kể cả $\varepsilon$) trên $\{a, b, c\}$: $\Sigma^*$. Văn phạm: $S \to aS \mid bS \mid cS \mid \varepsilon$. |
| **7** | `cc*` | **CÓ** | Tương đương $c^+$: dãy các chữ `c` có độ dài $\ge 1$. Văn phạm: $S \to cS \mid c$. |
| **8** | `a* c*` | **CÓ** | Dãy chữ `a` rồi đến dãy chữ `c`: $\{a^i c^j \mid i, j \ge 0\}$. Văn phạm: $S \to aS \mid C,\ C \to cC \mid \varepsilon$. |
| **9** | `(a + b)* (cc)* (a + b)*` | **CÓ** | Các chữ `a, b` ở hai đầu, kẹp ở giữa **một khối duy nhất** gồm số chẵn chữ `c` đứng liền nhau (`cc`, `cccc`...). *(Lưu ý: `cac` KHÔNG thuộc biểu thức 9, nhưng LẠI thuộc biểu thức 5!)*. |
| **10**| `(a + b + c)*` | **CÓ** | Giống hệt biểu thức số 6 ($\Sigma^*$). |

---

# PHẦN 3: 24 CÂU TRẮC NGHIỆM CHUYÊN SÂU CHO BIỂU THỨC CHÍNH QUY (TRỌNG TÂM ĐỀ WORD)

**Câu 1.** Biểu thức nào sau đây trong Phần 2 file Word **KHÔNG PHẢI** biểu thức chính quy hợp lệ?
- A. `(ab)c`
- B. `(c* (a* + b*) c*)* ((ab)+c+)*  c* (a* + b*) c*)*)*`
- C. `(a + b)* (c (a + b)* c)* (a + b)*`
- D. `cc*`
👉 **Đáp án đúng: B**
- **Giải thích:** Biểu thức B có số dấu đóng ngoặc nhiều hơn số dấu mở ngoặc (thừa `)*)*` ở cuối).

**Câu 2.** Chuỗi nào sau đây thuộc $L(E_5)$ với $E_5 = (a+b)^*(c(a+b)^*c)^*(a+b)^*$?
- A. `c`
- B. `abc`
- C. `acbc`
- D. `ccac`
👉 **Đáp án đúng: C**
- **Giải thích:** `acbc` có 2 chữ `c` (chẵn). `c` (1), `abc` (1), `ccac` (3) đều lẻ.

**Câu 3.** Chuỗi nào sau đây **KHÔNG** thuộc $L(E_5)$?
- A. $\varepsilon$
- B. `abab`
- C. `cabcb`
- D. `cacac`
👉 **Đáp án đúng: D**
- **Giải thích:** $\varepsilon$ (0 `c`), `abab` (0 `c`), `cabcb` (2 `c`) đều chẵn. `cacac` có 3 chữ `c` (lẻ) $\implies$ KHÔNG thuộc.

**Câu 4.** Chuỗi nào sau đây thuộc $L(E_5)$ nhưng **KHÔNG** thuộc $L(E_9)$ với $E_9 = (a+b)^*(cc)^*(a+b)^*$?
- A. abccba
- B. cacc
- C. cac
- D. ccc
👉 **Đáp án đúng: C**
- **Giải thích:** `cac` có 2 chữ `c` không đứng cạnh nhau (chen `a` ở giữa), nên thuộc $E_5$ (chẵn `c`) nhưng không thuộc $E_9$ (đòi hỏi `c` đứng sát thành từng cặp `cc` tập trung 1 chỗ!).

**Câu 5.** Chuỗi nào sau đây **KHÔNG** thuộc $L(E_9) = L((a+b)^*(cc)^*(a+b)^*)$?
- A. `a`
- B. `cc`
- C. `accb`
- D. `ccaabcc`
👉 **Đáp án đúng: D**
- **Giải thích:** `ccaabcc` tách các cặp `cc` ra hai nơi khác nhau (bị chặn bởi `aab` ở giữa), mà `(cc)*` chỉ nằm một cụm ở giữa trong $E_9$!

**Câu 6.** Chuỗi nào sau đây thuộc $L(E_9)$?
- A. `cac`
- B. `c`
- C. `abccccba`
- D. `ccbcc`
👉 **Đáp án đúng: C**
- **Giải thích:** `abccccba` gồm `ab` + `(cc)^2` + `ba` (4 chữ `c` đứng liền kề một chỗ).

**Câu 7.** Biểu thức nào sau đây sinh ra ngôn ngữ chỉ gồm **DUY NHẤT 1 TỪ**?
- A. `(ab)c`
- B. `abc*`
- C. `cc*`
- D. `a* c*`
👉 **Đáp án đúng: A**
- **Giải thích:** `(ab)c` không có bất kỳ phép lặp `*` hay cộng `+` nào nên chỉ sinh đúng chuỗi `abc`.

**Câu 8.** Hai biểu thức nào trong danh sách Phần 2 của file Word là **TƯƠNG ĐƯƠNG NHAU HOÀN TOÀN**?
- A. `abc*` và `(a+b)*c*`
- B. Biểu thức số 6 `(a+b+c)*` và số 10 `(a+b+c)*`
- C. `cc*` và `a*c*`
- D. `E_5` và `E_9`
👉 **Đáp án đúng: B**
- **Giải thích:** Cả biểu thức 6 và 10 đều viết y hệt là `(a + b + c)*`.

**Câu 9.** Chuỗi nào sau đây thuộc $L(`abc*`)$?
- A. ac
- B. abab
- C. ab
- D. abbc
👉 **Đáp án đúng: C**
- **Giải thích:** Với $n=0$ lần lặp ở `c*`, `abc*` sinh ra `ab`.

**Câu 10.** Chuỗi nào sau đây **KHÔNG** thuộc $L(`(a+b)*c*`)$?
- A. 
- B. cc
- C. abbc
- D. acb
👉 **Đáp án đúng: D**
- **Giải thích:** `(a+b)*c*` không bao giờ cho phép `a` hoặc `b` xuất hiện sau `c`, nên `acb` bị loại.

**Câu 11.** Biểu thức `cc*` tương đương với cách viết nào sau đây?
- A. $c^*$
- B. $c^+$
- C. $(cc)^*$
- D. $\varepsilon + c$
👉 **Đáp án đúng: B**
- **Giải thích:** `cc*` là nối 1 chữ `c` với $\ge 0$ chữ `c` $\implies$ $\ge 1$ chữ `c` $= c^+$.

**Câu 12.** Chuỗi nào sau đây thuộc $L(`a*c*`)$?
- A. ca
- B. abc
- C. aaac
- D. aca
👉 **Đáp án đúng: C**
- **Giải thích:** `aaac` = $a^3 c^1$, không chứa `b` và toàn bộ `a` đứng trước `c`.

**Câu 13.** Chuỗi ngắn nhất thuộc $L(E_5)$ là:
- A. `c`
- B. `a`
- C. $\varepsilon$
- D. `cc`
👉 **Đáp án đúng: C**
- **Giải thích:** Khi chọn 0 lần cho mọi phép lặp `*` trong $E_5$, ta thu được chuỗi rỗng $\varepsilon$ (độ dài 0; trong khi `a` dài 1, `cc` dài 2, `c` không thuộc $L(E_5)$).

**Câu 14.** Chuỗi có độ dài 1 nào thuộc $L(E_5)$?
- A. Chỉ có `c`
- B. Chỉ có `a` và `b`
- C. Cả `a`, `b`, `c`
- D. Không có chuỗi nào
👉 **Đáp án đúng: B**
- **Giải thích:** Chuỗi dài 1 phải có 0 chữ `c` (vì 1 chữ `c` là số lẻ!), nên chỉ có `a` và `b`.

**Câu 15.** Đếm số chuỗi có độ dài đúng bằng 2 thuộc $L(E_5)$ trên $\{a, b, c\}$:
- A. 4 chuỗi
- B. 5 chuỗi (`aa, ab, ba, bb, cc`)
- C. 6 chuỗi
- D. 9 chuỗi
👉 **Đáp án đúng: B**
- **Giải thích:** Có 0 chữ `c`: $2 \times 2 = 4$ chuỗi (`aa, ab, ba, bb`). Có 2 chữ `c`: 1 chuỗi (`cc`). Tổng cộng = **5 chuỗi**.

**Câu 16.** DFA tối thiểu đoán nhận $L(E_5)$ (số lượng chữ `c` chẵn trên $\{a, b, c\}$) cần bao nhiêu trạng thái?
- A. 1 trạng thái
- B. 2 trạng thái (Chẵn chữ `c` và Lẻ chữ `c`)
- C. 3 trạng thái
- D. 4 trạng thái
👉 **Đáp án đúng: B**
- **Giải thích:** Đọc `a` hoặc `b` thì đứng yên tại chỗ; chỉ khi đọc `c` mới nhảy qua lại giữa 2 trạng thái: `Chẵn` (đầu & kết thúc) và `Lẻ`.

**Câu 17.** Văn phạm chính quy sinh ra ngôn ngữ của `abc*` là:
- A. $S \to abcS \mid \varepsilon$
- B. $S \to abA,\ A \to cA \mid \varepsilon$
- C. $S \to aSb \mid c$
- D. $S \to abc$
👉 **Đáp án đúng: B**
- **Giải thích:** `ab` cố định ở đầu dẫn sang `A`, còn `A` sinh $c^*$.

**Câu 18.** Quan hệ bao hàm giữa $L(E_9)$ và $L(E_5)$ là:
- A. $L(E_5) \subsetneq L(E_9)$
- B. $L(E_9) \subsetneq L(E_5)$
- C. $L(E_5) = L(E_9)$
- D. Không giao nhau
👉 **Đáp án đúng: B**
- **Giải thích:** Mọi chuỗi thuộc $E_9$ có $(cc)^*$ luôn có số chữ `c` chẵn ($2k$) nên đương nhiên thuộc $E_5$, nhưng `cac` thuộc $E_5$ lại không thuộc $E_9$.

**Câu 19.** Chuỗi nào thuộc $L(`a*c*`)$ nhưng **KHÔNG** thuộc $L(`abc*`)$?
- A. ab
- B. abc
- C. aaac
- D. abcc
👉 **Đáp án đúng: C**
- **Giải thích:** `aaac` chỉ có `a` và `c` (thuộc `a*c*`), không bắt đầu bằng `ab` nên không thuộc `abc*`.

**Câu 20.** Phát biểu nào sau đây **SAI** về ngôn ngữ của `(a + b)* c*`?
- A. Có chứa chuỗi rỗng $\varepsilon$
- B. Có chứa chuỗi `bbb`
- C. Có chứa chuỗi `ccc`
- D. Có chứa chuỗi `cba`
👉 **Đáp án đúng: D**
- **Giải thích:** `cba` sai vì `c` đứng trước `b, a`.

**Câu 21.** Chuỗi `cbacba` có thuộc $L(E_5)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: A**
- **Giải thích:** Có 2 chữ `c` (chẵn) và toàn bộ ký tự đều nằm trong $\{a,b,c\}$ $\implies$ Có!

**Câu 22.** Chuỗi `abccba` có thuộc $L(E_9)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: A**
- **Giải thích:** `ab` thuộc $(a+b)^*$, `cc` thuộc $(cc)^*$, `ba` thuộc $(a+b)^*$ $\implies$ Có!

**Câu 23.** Chuỗi `ccacc` có thuộc $L(E_9)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: B**
- **Giải thích:** Giữa 2 cụm `cc` có chữ `a` xen vào, mà `(cc)*` trong $E_9$ chỉ đứng thành 1 khối duy nhất ở giữa $\implies$ Không!

**Câu 24.** Chuỗi `abccc` có thuộc $L(`abc*`)$ không?
- A. Có
- B. Không
👉 **Đáp án đúng: A**
- **Giải thích:** `ab` + $c^3$ $\implies$ Có!
