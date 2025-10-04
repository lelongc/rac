# 🎯 TÀI LIỆU THI COPY & PASTE - THỐNG KÊ MÔ TẢ

## ⚡ ĐỌC ĐỀ THI → TÌM CODE → COPY → THAY TÊN → XONG!

---

## � BẢNG TÌM KIẾM SIÊU NHANH

### 👁️ NHÌN THẤY TỪ KHÓA NÀO → CTRL+F TÌM MÃ ĐÓ

| **NHÌN THẤY TỪ KHÓA TRONG ĐỀ**      | **CTRL+F TÌM** | **THAY GÌ**                |
| ----------------------------------- | -------------- | -------------------------- |
| `đọc file`, `hiển thị dòng`         | `A1`           | Tên file                   |
| `bao nhiêu dòng`, `bao nhiêu cột`   | `A2`           | Không thay                 |
| `giá trị thiếu`, `missing`          | `A3`           | Không thay                 |
| `định tính`, `định lượng`           | `A4`           | Không thay                 |
| `có bao nhiêu loại`, `nunique`      | `B1`           | Tên cột                    |
| `nhiều nhất`, `ít nhất`, `top`      | `B2`           | Tên cột                    |
| `tỷ lệ`, `phần trăm`, `%`           | `B3`           | Tên cột                    |
| `theo nhóm`, `groupby`, `so sánh`   | `B4`           | Tên 2 cột                  |
| `trung bình`, `trung vị`, `mean`    | `C1`           | Tên cột                    |
| `phân vị`, `25%`, `75%`, `Q1`       | `C2`           | Tên cột                    |
| `biểu đồ cột`, `bar chart`          | `D1`           | Tên cột                    |
| `biểu đồ tròn`, `pie chart`         | `D2`           | Tên cột                    |
| `histogram`, `phân bố`              | `D3`           | Tên cột                    |
| `boxplot`, `hộp`                    | `D4`           | Tên cột                    |
| `so sánh boxplot`, `theo nhóm`      | `D5`           | Tên 2 cột                  |
| `xác suất`, `tính P(`, `nhị thức`   | `E1`           | Số n, p, k                 |
| `Poisson`, `λ`, `lambda`            | `E2`           | Số λ, k                    |
| `chuẩn`, `normal`, `N(μ,σ)`         | `E3`           | Số μ, σ, x                 |
| `lấy mẫu`, `sample`                 | `F1`           | Số mẫu                     |
| `mô phỏng`, `100 lần`, `simulation` | `F2`           | Số lần, số mẫu             |
| `inches`, `pounds`, `đổi đơn vị`    | `G1`           | Tên cột                    |
| `BMI`, `béo phì`                    | `G2`           | Tên cột chiều cao/cân nặng |
| `lọc`, `filter`, `điều kiện`        | `G3`           | Tên cột + điều kiện        |
| `theo tháng`, `thời gian`, `date`   | `H1`           | Tên cột thời gian          |

---

## 🎯 KHU VỰC COPY CODE

### A1. ĐỌC FILE + HIỂN THỊ

**Thấy: "Đọc dữ liệu", "hiển thị 5 dòng đầu"**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ⭐ THAY TÊN FILE Ở ĐÂY
df = pd.read_csv('TÊN_FILE.csv')

# Hiển thị dữ liệu
print(df.head())      # 5 dòng đầu
print(df.head(10))    # 10 dòng đầu
```

### A2. SỐ DÒNG - SỐ CỘT

**Thấy: "có bao nhiêu dòng", "bao nhiêu cột"**

```python
print(f"Dữ liệu có {df.shape[0]} dòng và {df.shape[1]} cột")
```

### A3. GIÁ TRỊ THIẾU

**Thấy: "giá trị thiếu", "missing value"**

```python
print("Số giá trị thiếu trong từng cột:")
print(df.isnull().sum())
```

### A4. PHÂN LOẠI THUỘC TÍNH

**Thấy: "định tính", "định lượng"**

```python
# Thuộc tính định lượng (số)
quantitative = df.select_dtypes(include=[np.number]).columns.tolist()
print("Thuộc tính định lượng:", quantitative)

# Thuộc tính định tính (chữ)
categorical = df.select_dtypes(include=['object']).columns.tolist()
print("Thuộc tính định tính:", categorical)
```

### B1. ĐẾM SỐ LƯỢNG

**Thấy: "có bao nhiêu loại", "nunique"**

```python
# ⭐ THAY TÊN CỘT Ở ĐÂY
counts = df['TÊN_CỘT'].value_counts()
print(counts)
print(f"Số loại khác nhau: {df['TÊN_CỘT'].nunique()}")
```

### B2. TÌM NHIỀU NHẤT/ÍT NHẤT

**Thấy: "nhiều nhất", "ít nhất", "top"**

```python
# ⭐ THAY TÊN CỘT Ở ĐÂY
top_value = df['TÊN_CỘT'].value_counts().head(1)
print(f"Giá trị phổ biến nhất: {top_value.index[0]} ({top_value.iloc[0]} lần)")

# Nếu hỏi sản phẩm được mua nhiều nhất
top_product = df['Product_ID'].value_counts().head(1)
print(f"Sản phẩm bán chạy: {top_product.index[0]} ({top_product.iloc[0]} lần)")
```

### B3. TỶ LỆ PHẦN TRĂM

**Thấy: "tỷ lệ", "phần trăm", "%"**

```python
# ⭐ THAY TÊN CỘT Ở ĐÂY
counts = df['TÊN_CỘT'].value_counts()
percentages = (counts / len(df) * 100).round(1)
print("Tỷ lệ phần trăm:")
for value in counts.index:
    print(f"{value}: {counts[value]} ({percentages[value]}%)")

# Nếu hỏi tỷ lệ nam nữ cụ thể
male_count = (df['Gender'] == 'M').sum()
female_count = (df['Gender'] == 'F').sum()
total = len(df)
print(f"Nam: {male_count} ({male_count/total*100:.1f}%)")
print(f"Nữ: {female_count} ({female_count/total*100:.1f}%)")
```

### B4. SO SÁNH THEO NHÓM

**Thấy: "theo nhóm", "groupby", "so sánh"**

```python
# ⭐ THAY TÊN 2 CỘT Ở ĐÂY
result = df.groupby('CỘT_NHÓM')['CỘT_GIÁ_TRỊ'].mean().sort_values(ascending=False)
print("Kết quả so sánh:")
print(result)
print(f"Nhóm cao nhất: {result.index[0]} ({result.iloc[0]:.2f})")

# Ví dụ: Chi tiêu theo độ tuổi
avg_by_age = df.groupby('Age')['Purchase'].mean().sort_values(ascending=False)
print(f"Nhóm tuổi chi tiêu cao nhất: {avg_by_age.index[0]} ({avg_by_age.iloc[0]:,.0f})")
```

### C1. THỐNG KÊ MÔ TẢ

**Thấy: "trung bình", "trung vị", "độ lệch chuẩn"**

```python
# ⭐ THAY TÊN CỘT Ở ĐÂY
print(f"Trung bình: {df['TÊN_CỘT'].mean():.2f}")
print(f"Trung vị: {df['TÊN_CỘT'].median():.2f}")
print(f"Độ lệch chuẩn: {df['TÊN_CỘT'].std():.2f}")
print(f"Min: {df['TÊN_CỘT'].min()}")
print(f"Max: {df['TÊN_CỘT'].max()}")

# Hoặc tổng hợp
print(df['TÊN_CỘT'].describe())
```

### C2. PHÂN VỊ

**Thấy: "phân vị", "25%", "75%", "Q1", "Q3"**

```python
# ⭐ THAY TÊN CỘT Ở ĐÂY
q1 = df['TÊN_CỘT'].quantile(0.25)
q2 = df['TÊN_CỘT'].quantile(0.50)  # Trung vị
q3 = df['TÊN_CỘT'].quantile(0.75)

print(f"Phân vị 25%: {q1:.2f}")
print(f"Phân vị 50% (trung vị): {q2:.2f}")
print(f"Phân vị 75%: {q3:.2f}")
print(f"Khoảng tứ phân vị (IQR): {q3 - q1:.2f}")
```

### D1. BIỂU ĐỒ CỘT

**Thấy: "biểu đồ cột", "bar chart"**

```python
# ⭐ THAY TÊN CỘT Ở ĐÂY
counts = df['TÊN_CỘT'].value_counts()
plt.figure(figsize=(10, 6))
counts.plot(kind='bar', color='skyblue')
plt.title('Biểu đồ cột')
plt.xlabel('Danh mục')
plt.ylabel('Số lượng')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

### D2. BIỂU ĐỒ TRÒN

**Thấy: "biểu đồ tròn", "pie chart"**

```python
# ⭐ THAY TÊN CỘT Ở ĐÂY
counts = df['TÊN_CỘT'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(counts.values, labels=counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Biểu đồ tròn')
plt.axis('equal')
plt.show()
```

### D3. HISTOGRAM

**Thấy: "histogram", "phân bố"**

```python
# ⭐ THAY TÊN CỘT Ở ĐÂY
plt.figure(figsize=(10, 6))
plt.hist(df['TÊN_CỘT'], bins=20, color='lightblue', edgecolor='black', alpha=0.7)
plt.title('Histogram')
plt.xlabel('Giá trị')
plt.ylabel('Tần suất')
plt.show()

# Nếu hỏi nhiều histogram cùng lúc
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
columns = ['COL1', 'COL2', 'COL3', 'COL4']  # ⭐ THAY TÊN CỘT
for i, col in enumerate(columns):
    ax = axes[i//2, i%2]
    ax.hist(df[col], bins=20, alpha=0.7)
    ax.set_title(f'Histogram của {col}')
plt.tight_layout()
plt.show()
```

### D4. BOXPLOT ĐƠN GIẢN

**Thấy: "boxplot", "hộp"**

```python
# ⭐ THAY TÊN CỘT Ở ĐÂY
plt.figure(figsize=(8, 6))
plt.boxplot(df['TÊN_CỘT'])
plt.title('Boxplot')
plt.ylabel('Giá trị')
plt.show()
```

### D5. BOXPLOT SO SÁNH NHÓM

**Thấy: "so sánh boxplot", "theo nhóm"**

```python
# ⭐ THAY TÊN 2 CỘT Ở ĐÂY
plt.figure(figsize=(10, 6))
df.boxplot(column='CỘT_GIÁ_TRỊ', by='CỘT_NHÓM')
plt.title('Boxplot so sánh theo nhóm')
plt.suptitle('')  # Xóa title mặc định
plt.show()

# Hoặc dùng seaborn
import seaborn as sns
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='CỘT_NHÓM', y='CỘT_GIÁ_TRỊ')
plt.title('Boxplot so sánh')
plt.xticks(rotation=45)
plt.show()
```

````

### B3. TỶ LỆ PHẦN TRĂM
**Thấy: "tỷ lệ", "phần trăm", "%"**

```python
# ⭐ THAY TÊN CỘT Ở ĐÂY
counts = df['TÊN_CỘT'].value_counts()
percentages = (counts / len(df) * 100).round(1)
print("Tỷ lệ phần trăm:")
for value in counts.index:
    print(f"{value}: {counts[value]} ({percentages[value]}%)")

# Nếu hỏi tỷ lệ nam nữ cụ thể
male_count = (df['Gender'] == 'M').sum()
female_count = (df['Gender'] == 'F').sum()
total = len(df)
print(f"Nam: {male_count} ({male_count/total*100:.1f}%)")
print(f"Nữ: {female_count} ({female_count/total*100:.1f}%)")
````

### B4. SO SÁNH THEO NHÓM

**Thấy: "theo nhóm", "groupby", "so sánh"**

```python
# ⭐ THAY TÊN 2 CỘT Ở ĐÂY
result = df.groupby('CỘT_NHÓM')['CỘT_GIÁ_TRỊ'].mean().sort_values(ascending=False)
print("Kết quả so sánh:")
print(result)
print(f"Nhóm cao nhất: {result.index[0]} ({result.iloc[0]:.2f})")

# Ví dụ: Chi tiêu theo độ tuổi
avg_by_age = df.groupby('Age')['Purchase'].mean().sort_values(ascending=False)
print(f"Nhóm tuổi chi tiêu cao nhất: {avg_by_age.index[0]} ({avg_by_age.iloc[0]:,.0f})")
```

# Đọc dữ liệu

df = pd.read_csv('filename.csv') # Thay 'filename.csv'

# Hiển thị 5 dòng đầu tiên

print(df.head())

# Hiển thị 10 dòng đầu tiên

print(df.head(10))

````

#### A2. Kích thước dữ liệu

```python
# Số dòng và số cột
print(f"Dữ liệu có {df.shape[0]} dòng và {df.shape[1]} cột")
print(f"Số dòng: {df.shape[0]}")
print(f"Số cột: {df.shape[1]}")
````

#### A3. Kiểm tra giá trị thiếu

```python
# Kiểm tra giá trị thiếu trong từng cột
print("Số giá trị thiếu trong từng cột:")
print(df.isnull().sum())

# Tổng số giá trị thiếu
print(f"Tổng giá trị thiếu: {df.isnull().sum().sum()}")
```

#### A4. Phân loại thuộc tính

```python
# Thuộc tính định lượng (số)
quantitative = df.select_dtypes(include=[np.number]).columns.tolist()
print("Thuộc tính định lượng:", quantitative)

# Thuộc tính định tính (phân loại)
categorical = df.select_dtypes(include=['object']).columns.tolist()
print("Thuộc tính định tính:", categorical)
```

---

### B. THỐNG KÊ ĐẾM VÀ TỶ LỆ

#### B1. Đếm số lượng

```python
# Đếm số lượng từng loại
counts = df['column_name'].value_counts()  # Thay 'column_name'
print(counts)

# Số lượng giá trị duy nhất
print(f"Số loại khác nhau: {df['column_name'].nunique()}")
```

#### B2. Tìm giá trị phổ biến nhất

```python
# Giá trị xuất hiện nhiều nhất
top_value = df['column_name'].value_counts().head(1)
print(f"Giá trị phổ biến nhất: {top_value.index[0]} ({top_value.iloc[0]} lần)")

# Sản phẩm được mua nhiều nhất
top_product = df['Product_ID'].value_counts().head(1)
print(f"Sản phẩm bán chạy: {top_product.index[0]} ({top_product.iloc[0]} lần)")
```

#### B3. Tính tỷ lệ phần trăm

```python
# Tỷ lệ phần trăm
percentages = df['column_name'].value_counts(normalize=True) * 100
print("Tỷ lệ phần trăm:")
for value in percentages.index:
    count = df['column_name'].value_counts()[value]
    percent = percentages[value]
    print(f"{value}: {count} ({percent:.1f}%)")

# Tỷ lệ nam nữ
gender_counts = df['Gender'].value_counts()
gender_percent = (gender_counts/len(df)*100).round(1)
print(f"Nam: {gender_counts['M']} ({gender_percent['M']}%)")
print(f"Nữ: {gender_counts['F']} ({gender_percent['F']}%)")
```

#### B4. So sánh theo nhóm

```python
# Chi tiêu trung bình theo nhóm tuổi
avg_by_age = df.groupby('Age')['Purchase'].mean().sort_values(ascending=False)
print("Chi tiêu TB theo tuổi:")
print(avg_by_age)

# Nhóm có chi tiêu cao nhất
print(f"Nhóm tuổi chi tiêu cao nhất: {avg_by_age.index[0]} ({avg_by_age.iloc[0]:,.0f})")

# Thống kê tổng hợp theo nhóm
group_stats = df.groupby('group_col')['value_col'].agg(['mean', 'median', 'count'])
print(group_stats)
```

---

### C. THỐNG KÊ MÔ TẢ

#### C1. Thống kê mô tả cơ bản

```python
# Thống kê tổng quan
print(df['column_name'].describe())

# Từng giá trị riêng lẻ
print(f"Trung bình: {df['column_name'].mean():.2f}")
print(f"Trung vị: {df['column_name'].median():.2f}")
print(f"Độ lệch chuẩn: {df['column_name'].std():.2f}")
print(f"Giá trị nhỏ nhất: {df['column_name'].min()}")
print(f"Giá trị lớn nhất: {df['column_name'].max()}")
print(f"Phương sai: {df['column_name'].var():.2f}")
```

#### C2. Phân vị

```python
# Các phân vị
q1 = df['column_name'].quantile(0.25)
q2 = df['column_name'].quantile(0.50)  # Trung vị
q3 = df['column_name'].quantile(0.75)

print(f"Phân vị 25%: {q1:.2f}")
print(f"Phân vị 50% (trung vị): {q2:.2f}")
print(f"Phân vị 75%: {q3:.2f}")
print(f"Khoảng tứ phân vị (IQR): {q3 - q1:.2f}")

# Miền phân vị
print(f"Miền phân vị: [{q1:.1f}, {q3:.1f}]")
```

---

### D. TRỰC QUAN HÓA

#### D1. Biểu đồ cột

```python
# Biểu đồ cột từ value_counts
counts = df['column_name'].value_counts()
plt.figure(figsize=(10, 6))
counts.plot(kind='bar', color='skyblue')
plt.title('Biểu đồ cột')
plt.xlabel('Danh mục')
plt.ylabel('Số lượng')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

#### D2. Biểu đồ tròn

```python
# Biểu đồ tròn
counts = df['column_name'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(counts.values, labels=counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Biểu đồ tròn')
plt.axis('equal')
plt.show()

# Biểu đồ tròn theo nhóm
total_by_group = df.groupby('group_col')['value_col'].sum()
plt.figure(figsize=(8, 8))
plt.pie(total_by_group.values, labels=total_by_group.index, autopct='%1.1f%%')
plt.title('Tỷ lệ tổng theo nhóm')
plt.show()
```

#### D3. Histogram

```python
# Histogram đơn giản
plt.figure(figsize=(10, 6))
plt.hist(df['column_name'], bins=20, color='lightblue', edgecolor='black', alpha=0.7)
plt.title('Histogram')
plt.xlabel('Giá trị')
plt.ylabel('Tần suất')
plt.grid(axis='y', alpha=0.3)
plt.show()

# Nhiều histogram
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
columns = ['col1', 'col2', 'col3', 'col4']  # Thay tên cột
for i, col in enumerate(columns):
    ax = axes[i//2, i%2]
    ax.hist(df[col], bins=20, alpha=0.7)
    ax.set_title(f'Histogram của {col}')
    ax.set_xlabel(col)
    ax.set_ylabel('Tần suất')
plt.tight_layout()
plt.show()
```

#### D4. Boxplot

```python
# Boxplot đơn giản
plt.figure(figsize=(8, 6))
plt.boxplot(df['column_name'])
plt.title('Boxplot')
plt.ylabel('Giá trị')
plt.show()
```

#### D5. Boxplot so sánh nhóm

```python
# Boxplot so sánh theo nhóm
plt.figure(figsize=(12, 6))

# Theo 1 biến
plt.subplot(1, 2, 1)
df.boxplot(column='value_col', by='group_col', ax=plt.gca())
plt.title('So sánh theo nhóm 1')
plt.suptitle('')

# Theo biến khác
plt.subplot(1, 2, 2)
df.boxplot(column='value_col', by='group_col2', ax=plt.gca())
plt.title('So sánh theo nhóm 2')
plt.suptitle('')

plt.tight_layout()
plt.show()

# Hoặc dùng seaborn
import seaborn as sns
plt.figure(figsize=(10, 6))
sns.boxplot(data=df, x='group_col', y='value_col')
plt.title('Boxplot so sánh')
plt.xticks(rotation=45)
plt.show()
```

---

### E. PHÂN PHỐI XÁC SUẤT

#### E1. Phân phối Nhị thức

```python
from scipy.stats import binom

# Tham số
n = 50    # Số thử nghiệm
p = 0.6   # Xác suất thành công (thay theo đề)

# Xác suất chính xác P(X = k)
k = 25
prob_exact = binom.pmf(k, n, p)
print(f"P(X = {k}) = {prob_exact:.6f}")

# Xác suất tích luỹ P(X ≤ k)
prob_less_equal = binom.cdf(k, n, p)
print(f"P(X ≤ {k}) = {prob_less_equal:.6f}")

# Xác suất P(X ≥ k)
prob_greater_equal = 1 - binom.cdf(k-1, n, p)
print(f"P(X ≥ {k}) = {prob_greater_equal:.6f}")

# Kỳ vọng và phương sai
E_X = n * p
Var_X = n * p * (1 - p)
print(f"E(X) = {E_X}")
print(f"Var(X) = {Var_X}")

# Ví dụ: 50 BDS có 25 BDS > 3 tỷ
p_over_3bil = (df['final_price'] > 3000000000).mean()  # Tỷ lệ > 3 tỷ
prob_25_out_of_50 = binom.pmf(25, 50, p_over_3bil)
print(f"P(25 trong 50 BDS > 3 tỷ) = {prob_25_out_of_50:.6f}")
```

#### E2. Phân phối Poisson

```python
from scipy.stats import poisson

# Tham số
lam = 3   # Lambda (trung bình)

# Xác suất
prob_0 = poisson.pmf(0, lam)
prob_1 = poisson.pmf(1, lam)
prob_2_or_more = 1 - poisson.cdf(1, lam)

print(f"P(X = 0) = {prob_0:.6f}")
print(f"P(X = 1) = {prob_1:.6f}")
print(f"P(X ≥ 2) = {prob_2_or_more:.6f}")
```

#### E3. Phân phối Chuẩn

```python
from scipy.stats import norm

# Tham số
mu = 170      # Trung bình
sigma = 10    # Độ lệch chuẩn

# Xác suất
prob_less_160 = norm.cdf(160, mu, sigma)
prob_between = norm.cdf(180, mu, sigma) - norm.cdf(160, mu, sigma)
prob_greater_180 = 1 - norm.cdf(180, mu, sigma)

print(f"P(X < 160) = {prob_less_160:.6f}")
print(f"P(160 < X < 180) = {prob_between:.6f}")
print(f"P(X > 180) = {prob_greater_180:.6f}")

# Tìm phân vị
percentile_95 = norm.ppf(0.95, mu, sigma)
print(f"Phân vị 95%: {percentile_95:.2f}")
```

---

### F. MÔ PHỎNG VÀ LẤY MẪU

#### F1. Lấy mẫu ngẫu nhiên

```python
# Lấy mẫu
sample_size = 50
sample_df = df.sample(n=sample_size, random_state=42)

# Tính tỷ lệ trong mẫu
original_ratio = (df['Gender'] == 'F').mean()
sample_ratio = (sample_df['Gender'] == 'F').mean()
error = abs(sample_ratio - original_ratio)

print(f"Tỷ lệ gốc: {original_ratio:.3f}")
print(f"Tỷ lệ mẫu: {sample_ratio:.3f}")
print(f"Sai số: {error:.3f}")
```

#### F2. Mô phỏng nhiều lần

```python
# Mô phỏng 100 lần
n_simulations = 100
sample_size = 50
ratios = []

for i in range(n_simulations):
    sample = df.sample(n=sample_size)
    ratio = (sample['Gender'] == 'F').mean()
    ratios.append(ratio)

# Vẽ histogram kết quả mô phỏng
plt.figure(figsize=(10, 6))
plt.hist(ratios, bins=20, alpha=0.7, edgecolor='black')
plt.title(f'Histogram {n_simulations} tỷ lệ mẫu (n={sample_size})')
plt.xlabel('Tỷ lệ nữ trong mẫu')
plt.ylabel('Tần suất')
plt.axvline(original_ratio, color='red', linestyle='--', label=f'Tỷ lệ gốc: {original_ratio:.3f}')
plt.legend()
plt.show()

# Thống kê các tỷ lệ mẫu
print(f"Trung bình các tỷ lệ mẫu: {np.mean(ratios):.3f}")
print(f"Độ lệch chuẩn: {np.std(ratios):.3f}")
```

---

### G. XỬ LÝ DỮ LIỆU

#### G1. Chuyển đổi đơn vị

```python
# Inches sang cm
df['height_cm'] = df['height_inches'] * 2.54

# Pounds sang kg
df['weight_kg'] = df['weight_pounds'] * 0.453592

# Hiển thị
print("Đã chuyển đổi đơn vị:")
print(df[['height_inches', 'height_cm', 'weight_pounds', 'weight_kg']].head())
```

#### G2. Tính BMI

```python
# Tính BMI
df['BMI'] = df['weight_kg'] / (df['height_cm']/100)**2

# BMI trung bình theo giới tính
bmi_by_gender = df.groupby('gender')['BMI'].mean()
print("BMI trung bình theo giới tính:")
print(bmi_by_gender)

# Phân loại BMI
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

# Tỷ lệ béo phì
obesity_rate = (df['BMI'] >= 30).mean()
print(f"Tỷ lệ béo phì: {obesity_rate:.3f}")

# Tỷ lệ muốn giảm cân
want_lose_weight = (df['weight'] > df['wtdesire']).mean()
print(f"Tỷ lệ muốn giảm cân: {want_lose_weight:.3f}")
```

#### G3. Lọc dữ liệu

```python
# Lọc theo điều kiện
df_filtered = df[df['column_name'] > 100]

# Lọc 3 thành phố lớn
major_cities = ['tp hồ chí minh', 'hà nội', 'đà nẵng']
df_major = df[df['area_temp'].isin(major_cities)]
print(f"Dữ liệu 3 thành phố: {df_major.shape[0]} dòng")

# Lọc có diện tích (khác -1)
df_with_area = df[df['acreage'] != -1]
print(f"Dữ liệu có diện tích: {df_with_area.shape[0]} dòng")

# Xóa dòng thiếu dữ liệu
df_clean = df.dropna(subset=['Year'])  # Bỏ dòng thiếu năm
```

---

### H. PHÂN TÍCH CHUYÊN BIỆT

#### H1. Phân tích theo thời gian

```python
# Chuyển đổi cột thời gian
df['date'] = pd.to_datetime(df['time'])
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

# Thống kê theo tháng
monthly_counts = df.groupby('month').size()
print("Số lượng theo tháng:")
print(monthly_counts)

# Vẽ biểu đồ theo tháng
plt.figure(figsize=(10, 6))
monthly_counts.plot(kind='bar', color='lightcoral')
plt.title('Số lượng BDS bán theo tháng năm 2020')
plt.xlabel('Tháng')
plt.ylabel('Số lượng')
plt.xticks(rotation=0)
plt.show()

# Xác suất bán trong mùa hè (tháng 6-8)
summer_months = [6, 7, 8]
summer_count = df[df['month'].isin(summer_months)].shape[0]
total_count = df.shape[0]
summer_prob = summer_count / total_count
print(f"Xác suất bán trong mùa hè: {summer_prob:.4f}")
```

#### H2. Bảng phân phối tần số

```python
# Bảng phân phối tần số theo năm (bỏ giá trị thiếu)
year_freq = df['Year'].value_counts().sort_index()
print("Bảng phân phối tần số theo năm:")
print(year_freq)

# Tạo DataFrame đẹp hơn
freq_table = pd.DataFrame({
    'Năm': year_freq.index,
    'Số lượng': year_freq.values
})
print(freq_table)
```

#### H3. Phân tích đặc biệt

```python
# Tỷ lệ đeo khuyên
piercing_rate = (df['Piercings'] > 0).mean()
print(f"Tỷ lệ sinh viên đeo khuyên: {piercing_rate:.3f}")

# So sánh đeo khuyên nam/nữ
piercing_by_gender = df.groupby('Gender')['Piercings'].apply(lambda x: (x > 0).mean())
print("Tỷ lệ đeo khuyên theo giới tính:")
print(piercing_by_gender)

# Người tập thể thao và sức khỏe kém
exercise_poor_health = df[(df['exerany'] == 1) & (df['genhlth'] == 'poor')].shape[0]
total_exercise = df[df['exerany'] == 1].shape[0]
rate = exercise_poor_health / total_exercise if total_exercise > 0 else 0
print(f"Tỷ lệ sức khỏe kém trong số người tập thể thao: {rate:.3f}")

# Bảng chéo BDS
crosstab_bds = pd.crosstab(df['type'], df['poster_temp'])
print("Bảng chéo loại BDS và cách rao bán:")
print(crosstab_bds)
```

---

## 🎯 TEMPLATE MẪU HOÀN CHỈNH

### Template đề Black Friday

```python
import pandas as pd
import matplotlib.pyplot as plt

# 1. Đọc dữ liệu
df = pd.read_csv('black_friday.csv')
print(df.head())

# 2. Thông tin dữ liệu
print(f"Số dòng: {df.shape[0]}, Số cột: {df.shape[1]}")
print(df.isnull().sum())

# 3. Phân loại thuộc tính
print("Thuộc tính số:", df.select_dtypes(include=['number']).columns.tolist())
print("Thuộc tính phân loại:", df.select_dtypes(include=['object']).columns.tolist())

# 4. Sản phẩm phổ biến
print(f"Số sản phẩm: {df['Product_ID'].nunique()}")
top_product = df['Product_ID'].value_counts().head(1)
print(f"Sản phẩm bán chạy: {top_product.index[0]} ({top_product.iloc[0]} lần)")

# 5. Tỷ lệ nam nữ
gender_counts = df['Gender'].value_counts()
gender_percent = (gender_counts/len(df)*100).round(1)
print(f"Nam: {gender_counts['M']} ({gender_percent['M']}%)")
print(f"Nữ: {gender_counts['F']} ({gender_percent['F']}%)")

plt.figure(figsize=(6, 4))
gender_counts.plot(kind='bar')
plt.title('Số lượng theo giới tính')
plt.show()

# 6. Nhóm tuổi chi tiêu cao nhất
avg_spending = df.groupby('Age')['Purchase'].mean().sort_values(ascending=False)
print(f"Nhóm tuổi chi tiêu cao nhất: {avg_spending.index[0]} ({avg_spending.iloc[0]:,.0f})")

# 7. Thống kê chi tiêu
print(df['Purchase'].describe())

# 8. Histogram chi tiêu
plt.figure(figsize=(8, 5))
plt.hist(df['Purchase'], bins=30)
plt.title('Phân bố mức chi tiêu')
plt.show()

# 9. Boxplot so sánh
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
df.boxplot(column='Purchase', by='Age', ax=plt.gca())
plt.title('Chi tiêu theo tuổi')
plt.suptitle('')

plt.subplot(1, 2, 2)
df.boxplot(column='Purchase', by='Gender', ax=plt.gca())
plt.title('Chi tiêu theo giới tính')
plt.suptitle('')
plt.show()

# 10. Biểu đồ tròn
total_by_age = df.groupby('Age')['Purchase'].sum()
plt.figure(figsize=(6, 6))
plt.pie(total_by_age.values, labels=total_by_age.index, autopct='%1.1f%%')
plt.title('Tỷ lệ tổng chi tiêu theo tuổi')
plt.show()
```

---

## 🔧 MẸO SỬ DỤNG KHI THI

1. **Ctrl + F** để tìm keyword nhanh trong file này
2. **Thay tên cột** trong code theo đề bài
3. **Copy nguyên khối code** rồi chỉnh sửa tên file/cột
4. **Kiểm tra tên cột** bằng `df.columns` trước khi chạy
5. **Nhớ import** thư viện ở đầu notebook

### Các lỗi thường gặp và cách sửa:

- `KeyError`: Sai tên cột → Kiểm tra `df.columns`
- `FileNotFoundError`: Sai tên file → Kiểm tra tên file chính xác
- `AttributeError`: Sai kiểu dữ liệu → Kiểm tra `df.dtypes`

**Chúc bạn thi tốt! 🍀**
