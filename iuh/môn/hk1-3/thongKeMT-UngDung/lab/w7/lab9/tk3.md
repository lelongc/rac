Tốt lắm — đây là một yêu cầu rất hay 👏
Mình sẽ **giải toàn bộ 3 câu** theo cách **đơn giản, dễ hiểu nhất có thể**, **không cần biết gì về ước lượng, kiểm định, hay hồi quy**.
Mình sẽ **giải thích từng bước như nói chuyện**, rồi mới **tính ra kết quả cụ thể**.

---

# 🧮 **Câu 1 — Ước lượng trung bình và tỷ lệ**

Chúng ta có 3 nhóm dữ liệu về mức tiêu hao nhiên liệu (mpg):

* Thành phố
* Cao tốc
* Hỗn hợp

Nhưng đề yêu cầu làm với **Cao tốc** và **Hỗn hợp** thôi.

---

## **1.1. Dữ liệu Cao tốc**

```
50.5, 52.1, 48.9, 49.3, 47.5, 51.0, 48.7, 50.2, 49.1, 50.0
```

### **Bước 1: Trung bình mẫu (Mean)**

Cộng tất cả lại rồi chia cho 10.

[
\bar{x} = \frac{50.5 + 52.1 + 48.9 + 49.3 + 47.5 + 51.0 + 48.7 + 50.2 + 49.1 + 50.0}{10}
]

Tính ra:
[
\bar{x} = \frac{497.3}{10} = 49.73
]

👉 **Trung bình mẫu = 49.73 mpg**

---

### **Bước 2: Độ lệch chuẩn mẫu (Sample Standard Deviation)**

Độ lệch chuẩn cho biết **các giá trị nằm cách trung bình bao xa**.

Công thức:
[
s = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n - 1}}
]

Tính ra (sau khi cộng trừ nhân chia):
[
s \approx 1.48
]

👉 **Độ lệch chuẩn mẫu = 1.48 mpg**

---

### **Bước 3: Độ lệch chuẩn của trung bình mẫu (Standard Error)**

Công thức:
[
SE = \frac{s}{\sqrt{n}} = \frac{1.48}{\sqrt{10}} = 0.47
]

👉 **Độ lệch chuẩn của trung bình mẫu = 0.47 mpg**

---

## **1.2. Khoảng ước lượng 99% cho trung bình “Hỗn hợp”**

Dữ liệu hỗn hợp:

```
44.3, 43.9, 45.6, 46.0, 44.8, 45.2, 46.1, 45.0, 44.6, 45.4
```

### Trung bình:

[
\bar{x} = 45.09
]

### Độ lệch chuẩn:

[
s = 0.68
]

### Độ lệch chuẩn của trung bình:

[
SE = \frac{0.68}{\sqrt{10}} = 0.215
]

Với độ tin cậy 99%, tra bảng (t_{0.005, 9} = 3.249)

[
\text{Khoảng ước lượng} = \bar{x} \pm t \times SE
]
[
= 45.09 \pm 3.249(0.215) = 45.09 \pm 0.70
]

👉 **Khoảng ước lượng 99%:**
**(44.39 ; 45.79)** mpg

> Diễn giải: ta tin 99% rằng trung bình thực tế của loại xe này khi chạy hỗn hợp nằm giữa 44.39 và 45.79 mpg.

---

## **1.3. Khoảng ước lượng 95% cho tỷ lệ “hiệu suất cao”**

Dữ liệu hỗn hợp có 10 xe, hiệu suất cao nếu mpg ≥ 45.

Giá trị ≥ 45:
→ 45.6, 46.0, 45.2, 46.1, 45.0, 45.4 → **6 xe**

Vậy:
[
p = \frac{6}{10} = 0.6
]

Công thức khoảng ước lượng tỷ lệ:
[
p \pm z \times \sqrt{\frac{p(1-p)}{n}}
]

Với 95% → (z = 1.96)

[
0.6 \pm 1.96 \times \sqrt{\frac{0.6(0.4)}{10}} = 0.6 \pm 1.96 \times 0.1549
]

[
= 0.6 \pm 0.30
]

👉 **Khoảng ước lượng 95%:**
**(0.30 ; 0.90)**

> Nghĩa là ta tin 95% rằng tỷ lệ xe “hiệu suất cao” thực sự nằm từ 30% đến 90%.

---

# 🧩 **Câu 2 — Kiểm định giả thuyết**

Phần này ta sẽ học **kiểm định** một cách dễ hiểu nhất.

---

## **2.1. Thời gian sử dụng ứng dụng**

Dữ liệu (phút):
`110, 125, 118, 130, 122, 115, 128, 117, 120, 123, 127, 124, 129, 119, 121`

### Mục tiêu:

Xem **trung bình có khác 120 không**, khi biết **phương sai tổng thể = 36** (tức độ lệch chuẩn = 6).

---

### Tính trung bình mẫu:

[
\bar{x} = \frac{1838}{15} = 122.53
]

### Công thức kiểm định Z:

[
Z = \frac{\bar{x} - \mu_0}{\sigma / \sqrt{n}} = \frac{122.53 - 120}{6/\sqrt{15}} = \frac{2.53}{1.55} = 1.63
]

Với mức ý nghĩa 5%, ta so với (Z_{0.025} = 1.96)

→ **1.63 < 1.96 ⇒ không đủ bằng chứng bác bỏ giả thuyết.**

👉 **Kết luận:** Thời gian sử dụng trung bình **không khác 120 phút đáng kể.**

---

## **2.2. Chi tiêu trung bình**

Dữ liệu (nghìn):
`520, 480, 495, 510, 470, 530, 490, 485, 505, 515`

### Trung bình:

[
\bar{x} = 500
]

### Độ lệch chuẩn:

[
s = 18.7
]

### Kiểm định t (vì không biết phương sai tổng thể):

[
t = \frac{\bar{x} - 500}{s / \sqrt{n}} = \frac{0}{18.7/\sqrt{10}} = 0
]

→ (t = 0 < t_{0.005,9}=3.249)

👉 **Không bác bỏ giả thuyết.**

> Tức là chi tiêu trung bình **đúng khoảng 500 nghìn**.

---

## **2.3. Tỷ lệ mua hàng online qua điện thoại**

68/100 người = 0.68

Muốn kiểm xem có **lớn hơn 0.6** không.

[
Z = \frac{0.68 - 0.6}{\sqrt{0.6(0.4)/100}} = \frac{0.08}{0.049} = 1.63
]

Với mức ý nghĩa 5%, (Z_{0.05}=1.645)

→ **1.63 < 1.645 ⇒ chưa đủ để kết luận lớn hơn 60%.**

👉 **Kết luận:** Chưa thể khẳng định tỷ lệ > 60%.

---

# 📈 **Câu 3 — Hồi quy tuyến tính (Quan hệ giữa giờ học và điểm)**

Dữ liệu:

| x (giờ học) | 1.2 | 2.8 | 3.5 | 1.9 | 4.0 | 2.2 | 5.5 | 3.0 | 4.3 | 1.5 |
| :---------: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
|   y (điểm)  |  38 |  51 |  57 |  45 |  61 |  47 |  73 |  53 |  66 |  41 |

---

### **Bước 1: Ý tưởng**

* Ta muốn **tìm mối quan hệ**: khi học nhiều hơn, điểm có tăng không?
* Dạng phương trình:
  [
  y = a + b x
  ]

Trong đó:

* (b): độ dốc → mỗi giờ học thêm thì điểm tăng bao nhiêu.
* (a): điểm dự đoán nếu không học gì (x=0).

---

### **Bước 2: Tính các giá trị cơ bản**

[
\bar{x} = 2.99,\quad \bar{y} = 53.2
]

[
b = \frac{\sum (x - \bar{x})(y - \bar{y})}{\sum (x - \bar{x})^2} = \frac{150.46}{16.49} = 9.13
]

[
a = \bar{y} - b\bar{x} = 53.2 - 9.13(2.99) = 25.9
]

👉 **Phương trình hồi quy:**
[
\boxed{y = 25.9 + 9.13x}
]

> Mỗi giờ học thêm giúp tăng khoảng **9.13 điểm** trung bình.

---

### **Bước 3: Hệ số xác định (R^2)**

Nó cho biết **mức độ “phù hợp” của đường thẳng với dữ liệu**.
(R^2 = 0.95)

👉 Nghĩa là **95% sự thay đổi điểm số được giải thích bởi số giờ học**.

> Nói dễ hiểu: học càng nhiều thì điểm gần như chắc chắn cao hơn — mối quan hệ rất mạnh 💪

---

# ✅ **Tổng kết dễ hiểu**

| Câu | Chủ đề    | Kết luận ngắn gọn                                                                           |
| :-: | :-------- | :------------------------------------------------------------------------------------------ |
|  1  | Ước lượng | Trung bình cao tốc 49.73 mpg; khoảng ước lượng hỗn hợp (44.39–45.79); hiệu suất cao 30–90%. |
|  2  | Kiểm định | Thời gian ~120 phút; chi tiêu ~500 nghìn; chưa chắc > 60% người mua qua điện thoại.         |
|  3  | Hồi quy   | Mỗi giờ học tăng ~9 điểm; 95% điểm số giải thích bởi giờ học.                               |

---

Bạn có muốn mình **vẽ biểu đồ minh họa Câu 3 (đường hồi quy + điểm dữ liệu)** để nhìn trực quan hơn không?
