# 🔥 CHEAT SHEET THI THỐNG KÊ MÔ TẢ - COPY & PASTE

## 🎯 QUY TẮC VÀNG: NHÌN ĐỀ → TÌM MÃ → COPY → THAY TÊN → CHẠY!

---

## 📋 MENU TÌM KIẾM SIÊU TỐC

### 🔍 THẤY TỪ KHÓA GÌ TRONG ĐỀ → CTRL+F TÌM MÃ ĐÓ

| **THẤY TRONG ĐỀ**                | **TÌM MÃ** | **THAY GÌ**    |
| -------------------------------- | ---------- | -------------- |
| đọc dữ liệu, hiển thị            | `A01`      | tên file       |
| bao nhiêu dòng, bao nhiêu cột    | `A02`      | không thay     |
| thiếu dữ liệu, missing, null     | `A03`      | không thay     |
| định tính, định lượng, phân loại | `A04`      | không thay     |
| có bao nhiêu, value_counts       | `B01`      | tên cột        |
| nhiều nhất, ít nhất, top         | `B02`      | tên cột        |
| tỷ lệ, %, phần trăm              | `B03`      | tên cột        |
| theo nhóm, groupby, so sánh      | `B04`      | 2 tên cột      |
| trung bình, mean, median         | `C01`      | tên cột        |
| độ lệch chuẩn, std, var          | `C02`      | tên cột        |
| phân vị, quantile, Q1, Q3        | `C03`      | tên cột        |
| biểu đồ cột, bar chart           | `D01`      | tên cột        |
| biểu đồ tròn, pie chart          | `D02`      | tên cột        |
| histogram, phân bố               | `D03`      | tên cột        |
| boxplot, hộp râu                 | `D04`      | tên cột        |
| so sánh boxplot, theo hãng       | `D05`      | 2 tên cột      |
| ma trận tương quan, heatmap      | `D06`      | không thay     |
| xác suất, P(, nhị thức           | `E01`      | n, p, k        |
| Poisson, λ, lambda               | `E02`      | λ, k           |
| chuẩn, normal, mm, đường kính    | `E03`      | μ, σ, x        |
| lấy mẫu, sample                  | `F01`      | số mẫu         |
| mô phỏng, simulation, 100 lần    | `F02`      | số lần         |
| đổi đơn vị, inches, pounds       | `G01`      | công thức      |
| BMI, kg/m², béo phì              | `G02`      | height, weight |
| datetime, thời gian, tháng       | `G03`      | cột time       |

---

## 🎯 KHU VỰC COPY CODE

### A01 - ĐỌC FILE + HIỂN THỊ

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# ⭐ THAY TÊN FILE
df = pd.read_csv('TÊN_FILE.csv')
print("5/7/10 dòng đầu:")
print(df.head(5))  # Thay 5→7→10 tùy đề
print("5/7/10 dòng cuối:")
print(df.tail(5))
```

**🔧 Dùng khi:** Đề yêu cầu đọc file và hiển thị dữ liệu
**💡 Ví dụ đề:** "Đọc dữ liệu acs12.csv và hiển thị 7 dòng cuối"

### A02 - SỐ DÒNG CỘT

```python
print(f"Dữ liệu có {df.shape[0]} dòng và {df.shape[1]} cột")
print(f"Kích thước: {df.shape}")
```

**🔧 Dùng khi:** Đề hỏi kích thước dữ liệu
**💡 Ví dụ đề:** "Cho biết kích thước bộ dữ liệu"

### A03 - THIẾU DỮ LIỆU

```python
print("Số giá trị thiếu:")
print(df.isnull().sum())
print(f"Tổng thiếu: {df.isnull().sum().sum()}")

# Bỏ dòng thiếu dữ liệu
df_clean = df.dropna()
print(f"Sau khi bỏ thiếu: {df_clean.shape[0]} dòng")
```

**🔧 Dùng khi:** Đề yêu cầu xử lý dữ liệu thiếu
**💡 Ví dụ đề:** "Bỏ qua các dòng bị thiếu dữ liệu năm"

### A04 - PHÂN LOẠI THUỘC TÍNH

```python
print("Thuộc tính định lượng (số):", df.select_dtypes(include=[np.number]).columns.tolist())
print("Thuộc tính định tính (chữ):", df.select_dtypes(include=['object']).columns.tolist())

# Hiển thị giá trị phân biệt cho thuộc tính định tính
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    print(f"\n{col}: {df[col].unique()}")
```

**🔧 Dùng khi:** Đề hỏi phân loại thuộc tính hoặc giá trị phân biệt
**💡 Ví dụ đề:** "Với mỗi thuộc tính định tính cho biết các giá trị phân biệt"

---

### B01 - ĐẾM SỐ LƯỢNG

```python
# ⭐ THAY TÊN CỘT
counts = df['TÊN_CỘT'].value_counts()
print("Số lượng từng loại:")
print(counts)
print(f"Tổng có {df['TÊN_CỘT'].nunique()} loại khác nhau")

# VÍ DỤ: Số lượng sinh viên mỗi năm
year_counts = df['Year'].value_counts().sort_index()
print("Số lượng sinh viên mỗi năm:")
print(year_counts)
```

**🔧 Dùng khi:** Đề hỏi số lượng, phân phối tần số
**💡 Ví dụ đề:** "Xây dựng bảng phân phối tần số số lượng sinh viên mỗi năm"

### B02 - TÌM NHIỀU NHẤT/ÍT NHẤT

```python
# ⭐ THAY TÊN CỘT
top = df['TÊN_CỘT'].value_counts().head(1)
print(f"Nhiều nhất: {top.index[0]} ({top.iloc[0]} lần)")

least = df['TÊN_CỘT'].value_counts().tail(1)
print(f"Ít nhất: {least.index[0]} ({least.iloc[0]} lần)")

# Mode (giá trị xuất hiện nhiều nhất)
mode_value = df['TÊN_CỘT'].mode().iloc[0]
print(f"Mode: {mode_value}")
```

**🔧 Dùng khi:** Đề hỏi giá trị phổ biến nhất, ít nhất
**💡 Ví dụ đề:** "Trình độ học vấn nào phổ biến nhất?"

### B03 - TỶ LỆ PHẦN TRĂM

```python
# ⭐ THAY TÊN CỘT
counts = df['TÊN_CỘT'].value_counts()
percentages = (counts / len(df) * 100).round(1)
print("Tỷ lệ %:")
for i, value in enumerate(counts.index):
    print(f"{value}: {counts.iloc[i]} ({percentages.iloc[i]}%)")

# VÍ DỤ: Tỷ lệ trình độ học vấn
edu_counts = df['edu'].value_counts()
edu_percent = (edu_counts / len(df) * 100).round(1)
print("Tỷ lệ trình độ học vấn:")
for edu in edu_counts.index:
    print(f"{edu}: {edu_counts[edu]} ({edu_percent[edu]}%)")
```

**🔧 Dùng khi:** Đề hỏi tỷ lệ phần trăm
**💡 Ví dụ đề:** "Tính tỷ lệ mỗi trình độ học vấn"

### B04 - SO SÁNH THEO NHÓM

```python
# ⭐ THAY 2 TÊN CỘT
# Bảng chéo 2 biến
crosstab = pd.crosstab(df['CỘT_NHÓM_1'], df['CỘT_NHÓM_2'])
print("Bảng chéo:")
print(crosstab)

# Tỷ lệ theo nhóm
crosstab_percent = pd.crosstab(df['CỘT_NHÓM_1'], df['CỘT_NHÓM_2'], normalize='index') * 100
print("Tỷ lệ % theo hàng:")
print(crosstab_percent.round(1))

# VÍ DỤ: So sánh trình độ sau ĐH theo chủng tộc
grad_by_race = df[df['edu'] == 'grad'].groupby('race').size()
total_by_race = df.groupby('race').size()
grad_percent = (grad_by_race / total_by_race * 100).round(1)
print("Tỷ lệ % có bằng sau ĐH theo chủng tộc:")
print(grad_percent)

# Tỷ lệ grad theo race
grad_by_race = df[df['edu'] == 'grad'].groupby('race').size()
total_by_race = df.groupby('race').size()
grad_percent = (grad_by_race / total_by_race * 100).round(1)
print("Tỷ lệ % có bằng sau ĐH theo chủng tộc:")
print(grad_percent)
```

**🔧 Dùng khi:** Đề yêu cầu so sánh theo nhóm
**💡 Ví dụ đề:** "So sánh trình độ sau ĐH giữa các chủng tộc"

---

### C01 - TRUNG BÌNH, TRUNG VỊ

```python
# ⭐ THAY TÊN CỘT
print(f"Trung bình: {df['TÊN_CỘT'].mean():.3f}")
print(f"Trung vị: {df['TÊN_CỘT'].median():.3f}")
print(f"Mode: {df['TÊN_CỘT'].mode().iloc[0] if len(df['TÊN_CỘT'].mode()) > 0 else 'N/A'}")

# Thống kê tổng hợp
print(df['TÊN_CỘT'].describe())

# Theo nhóm
group_stats = df.groupby('CỘT_NHÓM')['CỘT_GIÁ_TRỊ'].agg(['mean', 'median', 'std']).round(2)
print("Thống kê theo nhóm:")
print(group_stats)
```

**🔧 Dùng khi:** Đề hỏi thống kê mô tả
**💡 Ví dụ đề:** "Tuổi trung bình, trung vị là bao nhiêu?"

### C02 - ĐỘ LỆCH CHUẨN, PHƯƠNG SAI

```python
# ⭐ THAY TÊN CỘT
print(f"Độ lệch chuẩn: {df['TÊN_CỘT'].std():.3f}")
print(f"Phương sai: {df['TÊN_CỘT'].var():.3f}")
print(f"Min: {df['TÊN_CỘT'].min():.3f}")
print(f"Max: {df['TÊN_CỘT'].max():.3f}")
print(f"Khoảng (Range): {df['TÊN_CỘT'].max() - df['TÊN_CỘT'].min():.3f}")
```

**🔧 Dùng khi:** Đề hỏi độ biến thiên
**💡 Ví dụ đề:** "Độ lệch chuẩn của tuổi"

### C03 - PHÂN VỊ

```python
# ⭐ THAY TÊN CỘT
q1 = df['TÊN_CỘT'].quantile(0.25)
q2 = df['TÊN_CỘT'].quantile(0.50)  # Trung vị
q3 = df['TÊN_CỘT'].quantile(0.75)

print(f"Q1 (25%): {q1:.3f}")
print(f"Q2 (50%): {q2:.3f}")
print(f"Q3 (75%): {q3:.3f}")
print(f"IQR: {q3-q1:.3f}")

# Các phân vị khác
print(f"P10: {df['TÊN_CỘT'].quantile(0.10):.3f}")
print(f"P90: {df['TÊN_CỘT'].quantile(0.90):.3f}")
```

**🔧 Dùng khi:** Đề hỏi phân vị
**💡 Ví dụ đề:** "Các phân vị 25%, 50%, 75% của tuổi"

---

### D01 - BIỂU ĐỒ CỘT

```python
# ⭐ THAY TÊN CỘT
plt.figure(figsize=(10, 6))
counts = df['TÊN_CỘT'].value_counts()
counts.plot(kind='bar', color='skyblue')
plt.title('Biểu đồ cột - TÊN_CỘT')
plt.xlabel('Danh mục')
plt.ylabel('Số lượng')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# So sánh theo nhóm
plt.figure(figsize=(12, 6))
df.groupby('CỘT_NHÓM')['CỘT_GIÁ_TRỊ'].mean().plot(kind='bar', color='lightcoral')
plt.title('So sánh trung bình theo nhóm')
plt.ylabel('Giá trị trung bình')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

**🔧 Dùng khi:** Đề yêu cầu vẽ biểu đồ cột
**💡 Ví dụ đề:** "Vẽ biểu đồ số lượng mỗi loại BDS"

### D02 - BIỂU ĐỒ TRÒN

```python
# ⭐ THAY TÊN CỘT
plt.figure(figsize=(10, 8))
counts = df['TÊN_CỘT'].value_counts()
plt.pie(counts.values, labels=counts.index, autopct='%1.1f%%')
plt.title('Biểu đồ tròn - TÊN_CỘT')
plt.axis('equal')
plt.tight_layout()
plt.show()

# VÍ DỤ: Tỷ lệ các chủng tộc
plt.figure(figsize=(10, 10))
race_counts = df['race'].value_counts()
plt.pie(race_counts.values, labels=race_counts.index, autopct='%1.1f%%')
plt.title('Tỷ lệ % các chủng tộc trong khảo sát')
plt.axis('equal')
plt.show()
```

**🔧 Dùng khi:** Đề yêu cầu vẽ pie chart
**💡 Ví dụ đề:** "Vẽ pie chart thể hiện tỷ lệ % các chủng tộc"

### D03 - HISTOGRAM

```python
# ⭐ THAY TÊN CỘT
plt.figure(figsize=(10, 6))
plt.hist(df['TÊN_CỘT'].dropna(), bins=30, color='lightgreen', alpha=0.7, edgecolor='black')
plt.title('Histogram - TÊN_CỘT')
plt.xlabel('Giá trị')
plt.ylabel('Tần suất')
plt.grid(axis='y', alpha=0.3)
plt.show()

# VÍ DỤ: Vẽ 3 histogram cùng lúc
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Pulse
axes[0].hist(df['Pulse'].dropna(), bins=20, color='lightblue', alpha=0.7)
axes[0].set_title('Phân bố Nhịp tim')
axes[0].set_xlabel('Nhịp tim (beats/min)')

# Exercise
axes[1].hist(df['Exercise'].dropna(), bins=20, color='lightcoral', alpha=0.7)
axes[1].set_title('Phân bố Số giờ tập')
axes[1].set_xlabel('Giờ tập/tuần')

# Piercings
axes[2].hist(df['Piercings'].dropna(), bins=20, color='lightgreen', alpha=0.7)
axes[2].set_title('Phân bố Số khuyên')
axes[2].set_xlabel('Số khuyên')

plt.tight_layout()
plt.show()

# Nhận xét phân phối
print("Nhận xét phân phối:")
print("- Pulse: Phân phối gần đối xứng/lệch phải")
print("- Exercise: Phân phối lệch phải (nhiều người tập ít)")
print("- Piercings: Phân phối lệch phải (nhiều người không đeo)")
```

**🔧 Dùng khi:** Đề yêu cầu vẽ histogram
**💡 Ví dụ đề:** "Vẽ histogram 3 thuộc tính và nhận xét phân phối"

### D04 - BOXPLOT ĐƠN GIẢN

```python
# ⭐ THAY TÊN CỘT
plt.figure(figsize=(8, 6))
plt.boxplot(df['TÊN_CỘT'].dropna())
plt.title('Boxplot - TÊN_CỘT')
plt.ylabel('Giá trị')
plt.show()

# Nhiều cột cùng lúc
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
cols = ['Pulse', 'Exercise', 'Piercings']
for i, col in enumerate(cols):
    axes[i].boxplot(df[col].dropna())
    axes[i].set_title(f'Boxplot {col}')
    axes[i].set_ylabel(col)
plt.tight_layout()
plt.show()
```

**🔧 Dùng khi:** Đề yêu cầu boxplot đơn giản
**💡 Ví dụ đề:** "Vẽ boxplot của thu nhập"

### D05 - BOXPLOT SO SÁNH NHÓM

```python
# ⭐ THAY 2 TÊN CỘT
plt.figure(figsize=(12, 8))

# Cách 1: Pandas
df.boxplot(column='CỘT_GIÁ_TRỊ', by='CỘT_NHÓM', figsize=(12, 8))
plt.title('Boxplot so sánh theo nhóm')
plt.suptitle('')  # Xóa title mặc định
plt.show()

# Cách 2: Seaborn (đẹp hơn)
plt.figure(figsize=(12, 8))
sns.boxplot(data=df, x='CỘT_NHÓM', y='CỘT_GIÁ_TRỊ')
plt.title('Boxplot so sánh theo nhóm')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# VÍ DỤ: So sánh cân nặng người có/không tập thể dục
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='exerany', y='weight')
plt.title('So sánh cân nặng theo việc tập thể dục')
plt.xlabel('Có tập thể dục (1=Có, 0=Không)')
plt.ylabel('Cân nặng (pounds)')
plt.show()
```

**🔧 Dùng khi:** Đề yêu cầu so sánh boxplot theo nhóm
**💡 Ví dụ đề:** "Vẽ boxplot so sánh cân nặng của những người có/không tập thể dục"

### D06 - MA TRẬN TƯƠNG QUAN

```python
# Ma trận tương quan cho các cột số
numeric_cols = df.select_dtypes(include=[np.number]).columns
correlation_matrix = df[numeric_cols].corr()

plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0,
            square=True, linewidths=0.5, fmt='.2f')
plt.title('Ma trận tương quan')
plt.tight_layout()
plt.show()

# Scatter plot để kiểm tra tương quan
plt.figure(figsize=(10, 6))
plt.scatter(df['CỘT_X'], df['CỘT_Y'], alpha=0.6)
plt.title('Tương quan giữa X và Y')
plt.xlabel('CỘT_X')
plt.ylabel('CỘT_Y')
plt.show()

# VÍ DỤ: Tương quan hrs_work và income
plt.figure(figsize=(10, 6))
plt.scatter(df['hrs_work'], df['income'], alpha=0.6)
plt.title('Tương quan giữa giờ làm việc và thu nhập')
plt.xlabel('Số giờ làm việc/tuần')
plt.ylabel('Thu nhập hàng năm')
plt.show()
```

**🔧 Dùng khi:** Đề hỏi tương quan hoặc ảnh hưởng
**💡 Ví dụ đề:** "Khảo sát ảnh hưởng số giờ làm việc đến thu nhập"

---

### E01 - XÁC SUẤT NHỊ THỨC

```python
from scipy.stats import binom

# ⭐ THAY SỐ
n = 10     # Số lần thử (10 bóng)
p_red = 0.4    # Xác suất thành công (bóng đỏ)
p_blue = 0.6   # Xác suất thất bại (bóng xanh)

# a. P(đúng 4 bóng đỏ)
prob_4_red = binom.pmf(4, n, p_red)
print(f"a. P(4 bóng đỏ) = {prob_4_red:.6f}")

# b. P(đúng 2 bóng xanh)
prob_2_blue = binom.pmf(2, n, p_blue)
print(f"b. P(2 bóng xanh) = {prob_2_blue:.6f}")

# c. Đồ thị PMF số bóng xanh
x_values = range(0, n+1)
probs = [binom.pmf(x, n, p_blue) for x in x_values]
plt.figure(figsize=(10, 6))
plt.bar(x_values, probs, alpha=0.7, color='lightblue')
plt.title('Phân phối xác suất số bóng xanh')
plt.xlabel('Số bóng xanh')
plt.ylabel('P(X = k)')
plt.show()

# d. Đồ thị CDF
cdf_values = [binom.cdf(x, n, p_blue) for x in x_values]
plt.figure(figsize=(10, 6))
plt.plot(x_values, cdf_values, 'bo-', markersize=8)
plt.title('Hàm phân phối tích lũy số bóng xanh')
plt.xlabel('Số bóng xanh')
plt.ylabel('P(X ≤ k)')
plt.grid(True)
plt.show()
```

**🔧 Dùng khi:** Đề về lấy bóng, xác suất nhị thức
**💡 Ví dụ đề:** "Túi có 40% bóng đỏ, 60% bóng xanh, lấy 10 bóng"

### E02 - XÁC SUẤT POISSON

```python
from scipy.stats import poisson

# ⭐ THAY SỐ
lam = 3    # Lambda (trung bình)
k = 2      # Số sự kiện

# Xác suất
prob_k = poisson.pmf(k, lam)
print(f"P(X = {k}) = {prob_k:.6f}")

prob_less_equal = poisson.cdf(k, lam)
print(f"P(X ≤ {k}) = {prob_less_equal:.6f}")

prob_greater = 1 - poisson.cdf(k, lam)
print(f"P(X > {k}) = {prob_greater:.6f}")

# VÍ DỤ: Số cuộc gọi điện thoại
lam_calls = 10  # 10 cuộc gọi/giờ
print(f"P(5 cuộc gọi trong 1h) = {poisson.pmf(5, lam_calls):.6f}")
print(f"P(≤3 cuộc gọi trong 1h) = {poisson.cdf(3, lam_calls):.6f}")
print(f"P(15 cuộc gọi trong 2h) = {poisson.pmf(15, lam_calls*2):.6f}")
print(f"P(5 cuộc gọi trong 30p) = {poisson.pmf(5, lam_calls*0.5):.6f}")
```

**🔧 Dùng khi:** Đề về sự kiện hiếm, cuộc gọi, tai nạn
**💡 Ví dụ đề:** "Trung bình 10 cuộc gọi/giờ, tính xác suất..."

### E03 - XÁC SUẤT CHUẨN

```python
from scipy.stats import norm

# ⭐ THAY SỐ (theo đề về đường kính chi tiết máy)
mu = 20      # Kỳ vọng (mm)
sigma = 0.2  # Độ lệch chuẩn (mm)

# a. P(X < 20.3)
prob_a = norm.cdf(20.3, mu, sigma)
print(f"a. P(X < 20.3) = {prob_a:.6f}")

# b. P(19.9 < X < 20.3)
prob_b = norm.cdf(20.3, mu, sigma) - norm.cdf(19.9, mu, sigma)
print(f"b. P(19.9 < X < 20.3) = {prob_b:.6f}")

# c. P(|X - μ| ≤ 0.3) = P(19.7 < X < 20.3)
prob_c = norm.cdf(20.3, mu, sigma) - norm.cdf(19.7, mu, sigma)
print(f"c. P(|X - 20| ≤ 0.3) = {prob_c:.6f}")

# VÍ DỤ: Chiều cao người Mỹ
mu_height = 170  # cm
sigma_height = 10  # cm
print(f"P(cao > 180cm) = {1 - norm.cdf(180, mu_height, sigma_height):.6f}")
print(f"P(160 < cao < 180) = {norm.cdf(180, mu_height, sigma_height) - norm.cdf(160, mu_height, sigma_height):.6f}")
```

**🔧 Dùng khi:** Đề về đường kính, chiều cao, cân nặng, điểm số
**💡 Ví dụ đề:** "Chi tiết máy có đường kính trung bình 20mm, σ=0.2mm"

---

### F01 - LẤY MẪU

```python
# ⭐ THAY SỐ MẪU
sample_size = 50
sample_df = df.sample(n=sample_size, random_state=42)

print(f"Mẫu gốc: {len(df)} dòng")
print(f"Mẫu lấy: {len(sample_df)} dòng")

# VÍ DỤ: Tỷ lệ nữ trong mẫu
original_female_ratio = (df['Gender'] == 'F').mean()
sample_female_ratio = (sample_df['Gender'] == 'F').mean()
error = abs(sample_female_ratio - original_female_ratio)

print(f"Tỷ lệ nữ gốc: {original_female_ratio:.3f}")
print(f"Tỷ lệ nữ mẫu: {sample_female_ratio:.3f}")
print(f"Sai số: {error:.3f}")
```

**🔧 Dùng khi:** Đề yêu cầu lấy mẫu ngẫu nhiên
**💡 Ví dụ đề:** "Lấy mẫu 50 sinh viên, tính tỷ lệ nữ và sai số"

### F02 - MÔ PHỎNG

```python
# ⭐ THAY SỐ LẦN VÀ SỐ MẪU
n_simulations = 100
sample_size = 50
results = []

np.random.seed(42)  # Để kết quả ổn định
for i in range(n_simulations):
    sample = df.sample(n=sample_size)
    # Tính tỷ lệ hoặc trung bình tùy đề
    result = (sample['Gender'] == 'F').mean()  # ⭐ THAY
    results.append(result)

# Thống kê kết quả mô phỏng
print(f"Trung bình {n_simulations} lần mô phỏng: {np.mean(results):.3f}")
print(f"Độ lệch chuẩn: {np.std(results):.3f}")

# Vẽ histogram
plt.figure(figsize=(10, 6))
plt.hist(results, bins=20, alpha=0.7, edgecolor='black', color='lightblue')
plt.title(f'Histogram {n_simulations} lần mô phỏng (n={sample_size})')
plt.xlabel('Tỷ lệ nữ trong mẫu')
plt.ylabel('Tần suất')
plt.axvline(np.mean(results), color='red', linestyle='--',
           label=f'TB: {np.mean(results):.3f}')
plt.legend()
plt.grid(axis='y', alpha=0.3)
plt.show()

# So sánh các cỡ mẫu khác nhau
sample_sizes = [10, 30, 50, 100]
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()

for i, size in enumerate(sample_sizes):
    results_size = []
    for j in range(100):
        sample = df.sample(n=size)
        result = (sample['Gender'] == 'F').mean()
        results_size.append(result)

    axes[i].hist(results_size, bins=15, alpha=0.7)
    axes[i].set_title(f'n={size}, SD={np.std(results_size):.3f}')
    axes[i].axvline(np.mean(results_size), color='red', linestyle='--')

plt.tight_layout()
plt.show()

print("Nhận xét: Cỡ mẫu càng lớn, phân bố càng tập trung, độ lệch chuẩn giảm")
```

---

### G01 - ĐỔI ĐƠN VỊ

```python
# ⭐ THAY CÔNG THỨC ĐỔI ĐƠN VỊ
# Inches sang cm
df['height_cm'] = df['height'] * 2.54
print(f"Chiều cao TB: {df['height_cm'].mean():.1f} cm")

# Pounds sang kg
df['weight_kg'] = df['weight'] * 0.453592
print(f"Cân nặng TB: {df['weight_kg'].mean():.1f} kg")

# Cân nặng mong muốn
df['wtdesire_kg'] = df['wtdesire'] * 0.453592

# VÍ DỤ: Tỷ lệ muốn giảm cân
want_lose_weight = (df['wtdesire_kg'] < df['weight_kg']).sum()
total_people = len(df.dropna(subset=['weight_kg', 'wtdesire_kg']))
lose_weight_ratio = want_lose_weight / total_people
print(f"Tỷ lệ muốn giảm cân: {lose_weight_ratio:.3f} ({lose_weight_ratio*100:.1f}%)")
```

**🔧 Dùng khi:** Đề yêu cầu đổi đơn vị inches/pounds sang cm/kg
**💡 Ví dụ đề:** "Đổi chiều cao từ inches sang cm, cân nặng từ pounds sang kg"

### G02 - TÍNH BMI VÀ PHÂN LOẠI

```python
# Tính BMI (cần có height_cm và weight_kg)
df['BMI'] = df['weight_kg'] / (df['height_cm'] / 100) ** 2

# Phân loại BMI theo CDC
def classify_bmi(bmi):
    if bmi < 18.5:
        return 'Thiếu cân'
    elif bmi < 25:
        return 'Bình thường'
    elif bmi < 30:
        return 'Thừa cân'
    else:
        return 'Béo phì'

df['BMI_category'] = df['BMI'].apply(classify_bmi)

# Thống kê BMI
print("BMI trung bình theo giới tính:")
bmi_by_gender = df.groupby('gender')['BMI'].agg(['mean', 'std']).round(2)
print(bmi_by_gender)

# Tỷ lệ béo phì
obesity_stats = df['BMI_category'].value_counts()
obesity_percent = (obesity_stats / len(df) * 100).round(1)
print("\nTỷ lệ phân loại BMI:")
for category in obesity_stats.index:
    print(f"{category}: {obesity_stats[category]} ({obesity_percent[category]}%)")

# Tỷ lệ béo phì theo giới tính
obesity_by_gender = pd.crosstab(df['gender'], df['BMI_category'], normalize='index') * 100
print("\nTỷ lệ % phân loại BMI theo giới tính:")
print(obesity_by_gender.round(1))

# Tỷ lệ béo phì theo nhóm tuổi
df['age_group'] = pd.cut(df['age'], bins=[0, 30, 45, 60, 100],
                        labels=['<30', '30-44', '45-59', '60+'])
obesity_by_age = pd.crosstab(df['age_group'], df['BMI_category'], normalize='index') * 100
print("\nTỷ lệ % phân loại BMI theo nhóm tuổi:")
print(obesity_by_age.round(1))
```

**🔧 Dùng khi:** Đề hỏi về BMI, béo phì
**💡 Ví dụ đề:** "Tính BMI, phân tích tỷ lệ béo phì theo giới tính và tuổi"

### G03 - XỬ LÝ DATETIME VÀ THỜI GIAN

```python
# ⭐ THAY TÊN CỘT THỜI GIAN
# Chuyển cột thời gian thành datetime
df['time'] = pd.to_datetime(df['time'])

# Trích xuất tháng, năm
df['month'] = df['time'].dt.month
df['year'] = df['time'].dt.year

# Thống kê theo tháng
monthly_stats = df.groupby('month').size()
print("Số lượng BDS bán theo tháng:")
print(monthly_stats)

# Vẽ biểu đồ theo tháng
plt.figure(figsize=(12, 6))
monthly_stats.plot(kind='bar', color='lightblue')
plt.title('Số lượng BDS được bán theo tháng năm 2020')
plt.xlabel('Tháng')
plt.ylabel('Số lượng')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.3)
plt.show()

# VÍ DỤ: Xác suất bán trong mùa hè (tháng 6-8)
summer_sales = df[df['month'].isin([6, 7, 8])]
total_sales = len(df)
summer_prob = len(summer_sales) / total_sales
print(f"\nXác suất BDS bán trong mùa hè: {summer_prob:.6f}")

# Nhận xét theo tháng
peak_month = monthly_stats.idxmax()
min_month = monthly_stats.idxmin()
print(f"Tháng bán nhiều nhất: {peak_month} ({monthly_stats.max()} BDS)")
print(f"Tháng bán ít nhất: {min_month} ({monthly_stats.min()} BDS)")
```

**🔧 Dùng khi:** Đề có cột thời gian, yêu cầu phân tích theo tháng
**💡 Ví dụ đề:** "Vẽ biểu đồ số BDS bán theo tháng, tính xác suất bán trong mùa hè"

---

## 🎯 TEMPLATE ĐỀ HOÀN CHỈNH

### ĐỀ MẪU 1: DỮ LIỆU KHẢO SÁT NGƯỜI MỸ (ACS12.CSV)

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# a. Đọc dữ liệu
df = pd.read_csv('acs12.csv')
print(f"Kích thước: {df.shape}")
print("7 dòng cuối:")
print(df.tail(7))

# b. Giá trị phân biệt thuộc tính định tính
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    print(f"\n{col}: {df[col].unique()}")

# c. Tỷ lệ trình độ học vấn
edu_counts = df['edu'].value_counts()
edu_percent = (edu_counts / len(df) * 100).round(1)
print("\nTỷ lệ trình độ học vấn:")
for edu in edu_counts.index:
    print(f"{edu}: {edu_counts[edu]} ({edu_percent[edu]}%)")

# d. So sánh sau ĐH theo chủng tộc
grad_by_race = df[df['edu'] == 'grad'].groupby('race').size()
total_by_race = df.groupby('race').size()
grad_percent = (grad_by_race / total_by_race * 100).round(1)
print("\nTỷ lệ % có bằng sau ĐH theo chủng tộc:")
print(grad_percent)

# e. Pie chart chủng tộc
plt.figure(figsize=(10, 8))
race_counts = df['race'].value_counts()
plt.pie(race_counts.values, labels=race_counts.index, autopct='%1.1f%%')
plt.title('Tỷ lệ % các chủng tộc trong khảo sát')
plt.show()

# f. Tương quan hrs_work và income
plt.figure(figsize=(10, 6))
plt.scatter(df['hrs_work'], df['income'], alpha=0.6)
plt.title('Ảnh hưởng số giờ làm việc đến thu nhập')
plt.xlabel('Số giờ làm việc/tuần')
plt.ylabel('Thu nhập hàng năm')
plt.show()
```

### ĐỀ MẪU 2: LẤY BÓNG NGẪU NHIÊN

```python
from scipy.stats import binom
import matplotlib.pyplot as plt
import numpy as np

# Tham số
n = 10    # 10 bóng
p_red = 0.4    # P(đỏ)
p_blue = 0.6   # P(xanh)

# a. P(đúng 4 bóng đỏ)
prob_4_red = binom.pmf(4, n, p_red)
print(f"a. P(4 bóng đỏ) = {prob_4_red:.6f}")

# b. P(đúng 2 bóng xanh)
prob_2_blue = binom.pmf(2, n, p_blue)
print(f"b. P(2 bóng xanh) = {prob_2_blue:.6f}")

# c. Đồ thị PMF số bóng xanh
x_values = range(0, n+1)
probs = [binom.pmf(x, n, p_blue) for x in x_values]
plt.figure(figsize=(10, 6))
plt.bar(x_values, probs, alpha=0.7, color='lightblue')
plt.title('Phân phối xác suất số bóng xanh')
plt.xlabel('Số bóng xanh')
plt.ylabel('P(X = k)')
plt.show()

# d. Đồ thị CDF
cdf_values = [binom.cdf(x, n, p_blue) for x in x_values]
plt.figure(figsize=(10, 6))
plt.plot(x_values, cdf_values, 'bo-', markersize=8)
plt.title('Hàm phân phối tích lũy số bóng xanh')
plt.xlabel('Số bóng xanh')
plt.ylabel('P(X ≤ k)')
plt.grid(True)
plt.show()
```

### ĐỀ MẪU 3: SINH VIÊN (STUDENTSURVEY.CSV)

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Đọc và hiển thị
df = pd.read_csv('StudentSurvey.csv')
print("5 dòng đầu:")
print(df.head())

# Bảng phân phối tần số theo năm (bỏ thiếu dữ liệu)
year_counts = df['Year'].dropna().value_counts().sort_index()
print("\nSố lượng sinh viên mỗi năm:")
print(year_counts)

# 2a. Tỷ lệ đeo khuyên
piercing_ratio = (df['Piercings'] > 0).mean()
print(f"\n2a. Tỷ lệ đeo khuyên: {piercing_ratio:.3f} ({piercing_ratio*100:.1f}%)")

# 2b. So sánh nam nữ
piercing_by_gender = df.groupby('Gender').apply(lambda x: (x['Piercings'] > 0).mean())
print("\n2b. Tỷ lệ đeo khuyên theo giới:")
print(piercing_by_gender)

# 3. Histogram 3 thuộc tính
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
attrs = ['Pulse', 'Exercise', 'Piercings']
for i, attr in enumerate(attrs):
    axes[i].hist(df[attr].dropna(), bins=20, alpha=0.7)
    axes[i].set_title(f'Histogram {attr}')
    axes[i].set_xlabel(attr)
plt.tight_layout()
plt.show()

print("Nhận xét phân phối:")
print("- Pulse: Gần đối xứng")
print("- Exercise: Lệch phải")
print("- Piercings: Lệch phải")

# 4a. Lấy mẫu 50
sample_50 = df.sample(n=50, random_state=42)
original_female = (df['Gender'] == 'F').mean()
sample_female = (sample_50['Gender'] == 'F').mean()
error = abs(sample_female - original_female)
print(f"\n4a. Tỷ lệ nữ gốc: {original_female:.3f}")
print(f"     Tỷ lệ nữ mẫu: {sample_female:.3f}")
print(f"     Sai số: {error:.3f}")

# 4b. Mô phỏng 100 lần
results_100 = []
for i in range(100):
    sample = df.sample(n=50)
    female_ratio = (sample['Gender'] == 'F').mean()
    results_100.append(female_ratio)

plt.figure(figsize=(10, 6))
plt.hist(results_100, bins=20, alpha=0.7, edgecolor='black')
plt.title('Histogram 100 lần mô phỏng (n=50)')
plt.xlabel('Tỷ lệ nữ trong mẫu')
plt.ylabel('Tần suất')
plt.axvline(np.mean(results_100), color='red', linestyle='--')
plt.show()

# 4c. So sánh cỡ mẫu khác nhau
sample_sizes = [10, 30, 50, 100]
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()

for i, size in enumerate(sample_sizes):
    results = []
    for j in range(100):
        sample = df.sample(n=size)
        ratio = (sample['Gender'] == 'F').mean()
        results.append(ratio)

    axes[i].hist(results, bins=15, alpha=0.7)
    axes[i].set_title(f'n={size}, SD={np.std(results):.3f}')
    axes[i].axvline(np.mean(results), color='red', linestyle='--')

plt.tight_layout()
plt.show()

print("Nhận xét: Cỡ mẫu càng lớn, phân bố càng tập trung, độ lệch chuẩn giảm")
```

---

## 🚨 CHECKLIST THI QUAN TRỌNG

### ✅ TRƯỚC KHI BẮT ĐẦU:

1. **Đọc kỹ đề**: Gạch chân từ khóa quan trọng
2. **Kiểm tra file**: Tên file có đúng không?
3. **Import thư viện**: Copy đầy đủ import statements
4. **Đọc cột**: `print(df.columns)` để biết tên cột chính xác

### ✅ KHI LÀM BÀI:

1. **Thay tên đúng**: File name, column name, số liệu
2. **Chạy từng cell**: Đừng chạy tất cả cùng lúc
3. **Kiểm tra kết quả**: Có hợp lý không?
4. **Comment kết quả**: Viết nhận xét nếu đề yêu cầu

### ✅ TRƯỚC KHI NỘP:

1. **Kiểm tra lại tên file notebook**: `stt_hoten_GK.ipynb`
2. **Thông tin đầu file**: MSV, họ tên, số máy
3. **Tất cả cell đã chạy**: Không có lỗi
4. **Đủ câu trả lời**: Tất cả câu hỏi đã làm

### 🔧 SỬA LỖI NHANH:

- `KeyError`: Sai tên cột → `print(df.columns)`
- `FileNotFoundError`: Sai tên file → kiểm tra chính tả
- `ValueError`: Sai kiểu dữ liệu → `print(df.dtypes)`
- Import error: Cài thư viện thiếu

### 📈 CHIẾN THUẬT THI:

1. **Làm câu dễ trước**: Đọc file, thống kê cơ bản
2. **Copy template**: Sử dụng code mẫu, chỉ thay tên
3. **Nhận xét đơn giản**: "Phân phối lệch phải", "Tương quan dương"
4. **Quản lý thời gian**: 15-20p/câu lớn

### 💡 MẸO HAY:

- **Ctrl+F** tìm nhanh code cần thiết
- **Thay tên hàng loạt**: Ctrl+H trong VS Code
- **Backup code**: Copy vào file .txt để phòng khi mất
- **Test nhỏ**: Chạy với sample nhỏ trước khi chạy full

**🍀 CHÚC BẠN THI TỐT! NHỚ GIỮ BÌNH TĨNH VÀ LÀM TỪNG BƯỚC! 🍀**
