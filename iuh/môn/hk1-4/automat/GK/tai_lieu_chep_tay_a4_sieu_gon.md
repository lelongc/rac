# BẢNG TRA CHÉP TAY A4 SIÊU GỌN - AUTOMATA (IUH)
## (BẢN TỐI GIẢN CÔNG THỨC & MẸO PHÒNG THI - VỪA KHÍT 1 TỜ A4)

> **QUY ƯỚC:** Chuỗi rỗng là `ε`, bước chuyển là `→`, dẫn xuất là `⇒`.

---

## 1. PHÉP TOÁN TỪ, CHUỖI & TẬP HỢP (CHƯƠNG 1)
- `|ε| = 0`, `w.ε = ε.w = w`, `(uv)^R = v^R u^R`, Palindrome: `w = w^R`.
- Tập hợp: `L1 ∪ L2`, `L1 ∩ L2`, `L1 - L2`, bù `L_bù = Σ* - L`, ghép `L1.L2 = {uv | u∈L1, v∈L2}`.
- Lũy thừa: `L^0 = {ε}`, `L^1 = L`, `L^2 = L.L`.
- **Định nghĩa Kleene Star:** `L* = ∪(k=0..∞) L^k = {w1...wk | k≥0, wi ∈ L}` (luôn có `ε ∈ L*`).
- **Mẹo 3s kiểm tra w ∈ L*:** Mọi từ trong L dài d.
  + Nếu `|w|` KHÔNG chia hết cho d ⇒ **LOẠI NGAY** (`w ∉ L*`).
  + Nếu `|w|` chia hết cho d ⇒ Tách từng khối d ký tự, mọi khối ∈ L ⇒ `w ∈ L*`.

---

## 2. BẢNG TRA 10 CÔNG THỨC RE KINH ĐIỂN (CHƯƠNG 3)

| Yêu cầu ngôn ngữ | Biểu thức RE chuẩn | Mẹo nhớ |
| :--- | :--- | :--- |
| Chứa chuỗi con `u` | `Σ* u Σ*` | Kẹp giữa 2 đầu tùy ý |
| Chứa chuỗi con `u` HOẶC `v` | `Σ* (u + v) Σ*` | Rẽ nhánh dấu cộng |
| Bắt đầu `u`, kết thúc `v` | `u Σ* v` | Khóa 2 đầu, thân tự do |
| Mọi `b` đi thành cặp `bb` | `(a + bb)*` | Khối cơ sở: `a` hoặc `bb` |
| Số lượng `b` là số chẵn | `a* (b a* b a*)*` | Mỗi vòng lặp thêm 2 `b` |
| Số lượng `b` là số lẻ | `a* b a* (b a* b a*)*` | 1 chữ `b` lẻ + các cặp `bb` |
| KHÔNG chứa chuỗi con `bb` | `(a + ba)* (ε + b)` | Sau `b` phải có `a`, đuôi tối đa 1 `b` |
| Độ dài ít nhất `k` | `Σ^k Σ*` | Cố định k ký tự đầu |
| Bắt đầu `u1` hoặc `u2`, hết `v` | `(u1 + u2) Σ* v` | Nhóm tiền tố trong ngoặc |
| Bẫy đếm `Na(w) = 2.Nb(w)` | **Phi chính quy** (Pumping Lemma) | Xấp xỉ: `(c*(aab+aba+baa)c*)* + c*` |

---

## 3. PHÂN LOẠI CHOMSKY 10 GIÂY & MẪU ĂN ĐIỂM (CHƯƠNG 1)
- **Loại 2 (CFG):** Vế trái đúng 1 biến. Vế phải có biến kẹp giữa (`S → aSb`) HOẶC trộn lẫn trái-phải (`S → aA | Sb`).
- **Loại 3 (Regular):** Vế trái đúng 1 biến. Vế phải THUẦN TUÝ phải (`A → wB | w`) HOẶC THUẦN TUÝ trái (`A → Bw | w`).
- **Mẫu câu chuẩn đi thi:**
  > 1. Vế trái mọi luật sinh có đúng 1 biến (|α|=1) ⇒ G tối thiểu đạt **Loại 2 (CFG)**.  
  > 2. Vế phải có luật `S → aSb` biến kẹp giữa (không thuần tuyến tính) ⇒ G không đạt Loại 3.  
  > ⇒ **Kết luận:** Phân lớp thấp nhất của G là **LOẠI 2 (CFG)**.

---

## 4. BẢNG TẠO VĂN PHẠM CHO NGÔN NGỮ (L → G)

| Ngôn ngữ L | Tập luật sinh P | Loại Chomsky |
| :--- | :--- | :---: |
| `a^n b^n (n ≥ 1)` | `S → aSb | ab` | Loại 2 (CFG) |
| `a^n b^n (n ≥ 0)` | `S → aSb | ε` | Loại 2 (CFG) |
| `a^n b^(2n) (n ≥ 0)` | `S → aSbb | ε` | Loại 2 (CFG) |
| `a^n b^m (n ≥ m ≥ 0)` | `S → aS | A;  A → aAb | ε` | Loại 2 (CFG) |
| Palindrome `w = w^R` | `S → aSa | bSb | a | b | ε` | Loại 2 (CFG) |
| `a* b*` (độc lập số mũ) | `S → aS | B;  B → bB | ε` | Loại 3 (Regular) |

---

## 5. AUTOMATA HỮU HẠN & VẾT CHẠY (CHƯƠNG 2)
- **Bộ 5:** `M = (Q, Σ, δ, q0, F)`. `q0`: đỉnh vào (mũi tên trỏ vào); `F`: đỉnh kết thúc (vòng tròn đôi / ★).
- **Trình bày vết chạy:**
  + Chấp nhận: `w = 110: q0 ─(1)→ q1 ─(1)→ q1 ─(0)→ q2 ∈ F ⇒ CHẤP NHẬN.`
  + Từ chối: `w = 101: q0 ─(1)→ q1 ─(0)→ q2 ─(1)→ q1 ∉ F ⇒ TỪ CHỐI.`
- **DFA → Văn phạm tuyến tính phải:**
  + `δ(qi, x) = qj` ⇒ Viết luật: `Qi → x Qj`.
  + Nếu `qj ∈ F` (đích là kết thúc) ⇒ Bổ sung thêm luật dừng: `Qi → x`.

---

## 6. CHUYỂN NFA SANG DFA (SUBSET CONSTRUCTION)
- **B1:** Đỉnh đầu DFA: `A = ε-closure(q0)` (không có ε thì `A = {q0}`).
- **B2:** Với mỗi tập đỉnh `U` và ký tự `x`: `δ*(U, x) = ε-closure( ∪(q∈U) δ_NFA(q, x) )`. Đặt tên mới `B, C...` (nếu rỗng ghi `∅`).
- **B3:** Tập nào của DFA chứa ít nhất 1 trạng thái thuộc `F_NFA` ⇒ Đánh dấu `★ F_DFA`.

---

## 7. TỐI THIỂU HÓA DFA (BẢNG TAM GIÁC MYHILL-NERODE)
- **B1:** Xóa đỉnh cô lập (không có đường đi từ `q0`).
- **B2:** Lập bảng tam giác dưới `(qi, qj) (i > j)`. Đánh `X` vào ô có 1 đỉnh ∈ F và 1 đỉnh ∉ F.
- **B3 (Lan truyền):** Xét ô trống `(p, q)`. Nếu có ký tự `x` mà `(δ(p,x), δ(q,x))` đã có `X` ⇒ Đánh `X` vào `(p, q)`. Lặp lại đến khi hết.
- **B4:** Các ô **CÒN TRỐNG** là tương đương (`p ≡ q`) ⇒ Gộp thành 1 đỉnh mới `[p, q]`.

---

## 8. 5 KHẨU QUYẾT NÉ BẪY ĂN TRỌN ĐIỂM
1. **So sánh đếm vô hạn** (`a^n b^n`, `Na = 2Nb`) ⇒ Bổ đề Bơm khẳng định **Phi chính quy** (không vẽ DFA / không có RE chuẩn).
2. **Phân lớp VĂN PHẠM ≠ NGÔN NGỮ:** Văn phạm CFG vẫn sinh ra ngôn ngữ Regular bình thường.
3. **Kiểm tra L*:** Tính tổng độ dài `|w|` trước, lẻ loại luôn trong 3 giây.
4. **NFA → DFA:** Cứ dính 1 phần tử của `F_NFA` là cả tập thành `F_DFA` (vòng tròn kép).
5. **DFA → Văn phạm:** Trạng thái đích thuộc F thì BẮT BUỘC sinh thêm luật dừng `Qi → x`.
