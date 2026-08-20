# CẨM NANG ÔN THI & MẸO GIẢI NHANH NFA ĐIỂM TỐI ĐA
*(Dành cho sinh viên thi môn Lý thuyết Ôtômát & Ngôn ngữ hình thức)*

---

## 1. TỔNG HỢP 4 DẠNG BÀI THI KINH ĐIỂN & CÁCH GIẢI

### DẠNG 1: Tính hàm chuyển dịch mở rộng $\delta^*(q, w)$ và kiểm tra chuỗi có được chấp nhận hay không

#### 🎯 Quy trình giải 3 bước chuẩn điểm tối đa:
1. **Bước 1 (Tìm tập ban đầu):** Xuất phát từ trạng thái $q$. Nếu tại $q$ có cung $\lambda$ đi sang trạng thái khác, phải lấy ngay bao đóng $\lambda$ (gọi là $\lambda\text{-closure}$).  
   *Ví dụ:* Tại $q_1$ có $q_1 \xrightarrow{\lambda} q_2 \Rightarrow$ Tập bắt đầu là $\{q_1, q_2\}$.
2. **Bước 2 (Duyệt từng ký tự từ trái sang phải):**
   - Với mỗi ký tự $x \in w$, xét tất cả các trạng thái trong tập hiện tại xem khi đọc $x$ sẽ đi tới những trạng thái nào.
   - Lấy hợp tất cả các trạng thái đích lại.
   - Nếu bất kỳ trạng thái đích nào có cung $\lambda$, nạp thêm các trạng thái đích của cung $\lambda$ vào tập.
   - Nếu gặp trạng thái không có cung đi cho ký tự $x$, coi như nhánh đó rơi vào $\emptyset$ (chết).
3. **Bước 3 (Kết luận):**
   - Sau khi đọc xong ký tự cuối cùng của chuỗi $w$, ta được tập trạng thái cuối cùng $Q_{\text{cuối}} = \delta^*(q, w)$.
   - **Quy tắc chấp nhận:**
     $$\text{Nếu } Q_{\text{cuối}} \cap F \neq \emptyset \Rightarrow \textbf{Chuỗi } w \textbf{ ĐƯỢC CHẤP NHẬN}$$
     $$\text{Nếu } Q_{\text{cuối}} \cap F = \emptyset \Rightarrow \textbf{Chuỗi } w \textbf{ KHÔNG ĐƯỢC CHẤP NHẬN}$$

---

### DẠNG 2: Vẽ đồ thị chuyển dịch từ Bảng chuyển dịch $\delta$

#### 🎯 Mẹo vẽ nhanh không bao giờ thiếu sót:
- Mỗi hàng trong bảng là 1 trạng thái (vẽ 1 hình tròn).
- Đọc từng cột:
  - Cột $0$: Vẽ mũi tên nhãn $0$ từ trạng thái hàng đến các trạng thái trong ô.
  - Cột $1$: Vẽ mũi tên nhãn $1$ từ trạng thái hàng đến các trạng thái trong ô.
  - Cột $\lambda$: Vẽ mũi tên nhãn $\lambda$ từ trạng thái hàng đến các trạng thái trong ô.
  - Ô có $\emptyset$: Tuyệt đối **không vẽ mũi tên nào**.
- Đừng quên: Vẽ mũi tên chỉ vào trạng thái ban đầu $q_0$, và vẽ vòng tròn đôi cho các trạng thái kết thúc $F$.

---

### DẠNG 3: Thiết kế NFA nhận dạng mẫu (Pattern Matching)

| Yêu cầu đề bài | Công thức thiết kế đồ thị NFA |
| :--- | :--- |
| **Chứa chuỗi con $w$ (Substring)** | Vòng lặp $\{0, 1\}$ tại $q_0 \xrightarrow{w}$ Trạng thái kết thúc $q_F$ (có vòng lặp $\{0, 1\}$ tại $q_F$). |
| **Bắt đầu bằng $w$ (Prefix)** | Từ $q_0 \xrightarrow{w} q_F$ (tại $q_F$ có vòng lặp $\{0, 1\}$). Tại $q_0$ **không có** vòng lặp. |
| **Kết thúc bằng $w$ (Suffix)** | Tại $q_0$ có vòng lặp $\{0, 1\} \xrightarrow{w} q_F$. Tại $q_F$ **không có** vòng lặp. |
| **Ký tự thứ $k$ từ cuối là '1'** | Tại $q_0$ loop $\{0, 1\} \xrightarrow{1} q_1 \xrightarrow{\text{ký tự bất kỳ}} q_2 \dots \xrightarrow{\text{ký tự bất kỳ}} q_k \in F$ (đúng $k-1$ bước sau số 1). |

---

### DẠNG 4: Thiết kế NFA cho phép HỢP (Ngôn ngữ $L_1$ HOẶC $L_2$)

#### 🎯 Bí quyết "Ghép máy bằng $\lambda$":
1. Thiết kế riêng máy tự động $M_1$ cho ngôn ngữ $L_1$ (trạng thái bắt đầu $s_1$, kết thúc $F_1$).
2. Thiết kế riêng máy tự động $M_2$ cho ngôn ngữ $L_2$ (trạng thái bắt đầu $s_2$, kết thúc $F_2$).
3. Tạo 1 trạng thái bắt đầu chung $q_0$, vẽ 2 cung $\lambda$:
   $$q_0 \xrightarrow{\lambda} s_1 \quad \text{và} \quad q_0 \xrightarrow{\lambda} s_2$$
4. Tập trạng thái kết thúc chung là $F = F_1 \cup F_2$.

---

## 2. NHỮNG LỖI SAI KINH ĐIỂN CẦN TRÁNH TRONG PHÒNG THI

1. ⚠️ **Quên bao đóng $\lambda$ khi tính $\delta^*$:**  
   Khi máy đến trạng thái $q_1$, nếu có cung $q_1 \xrightarrow{\lambda} q_2$, bạn **bắt buộc** phải ghi tập trạng thái là $\{q_1, q_2\}$. Nếu chỉ ghi $\{q_1\}$ là mất sạch điểm bài toán.
2. ⚠️ **Nhầm lẫn giữa NFA và DFA:**  
   Trong NFA, khi không có đường đi tiếp cho một ký tự, ta **để trống** (nhánh tự chết), **tuyệt đối KHÔNG vẽ thêm trạng thái bẫy (trap state)** làm rối hình và mất thời gian.
3. ⚠️ **Quên vẽ vòng tròn đôi cho trạng thái kết thúc:**  
   Mọi trạng thái $\in F$ bắt buộc phải vẽ **2 vòng tròn lồng nhau**. Thiếu vòng tròn đôi giám thị sẽ chấm 0 điểm đồ thị.
4. ⚠️ **Quên mũi tên bắt đầu:**  
   Trạng thái khởi đầu $q_0$ phải có một mũi tên từ ngoài không gian chỉ vào.

---

## 3. CHECKLIST TRƯỚC KHI NỘP BÀI THI

- [ ] Đã chỉ rõ bộ 5 $M = (Q, \Sigma, \delta, q_0, F)$ chưa?
- [ ] Đồ thị đã có mũi tên vào $q_0$ và vòng tròn đôi cho $F$ chưa?
- [ ] Các nhánh rẽ đã gắn đúng nhãn ký tự ($0, 1, a, b, \lambda$) chưa?
- [ ] Phần kiểm tra chuỗi có ghi rõ lý do $\delta^*(q_0, w) \cap F \neq \emptyset$ chưa?
