# 🔥 CHEAT SHEET ÔN THI GIỮA KỲ - THỐNG KÊ MÔ TẢ & ỨNG DỤNG

## 🎯 QUY TẮC VÀNG: NHÌN ĐỀ → TÌM MÃ → COPY → THAY TÊN → CHẠY!

---

## � IMPORT TOÀN BỘ THỨ VIỆN CẦN THIẾT (COPY NGUYÊN KHỐI NÀY)

```python
# Import cơ bản - COPY TOÀN BỘ KHỐI NÀY VÀO ĐẦU FILE!
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Import phân phối xác suất (nếu đề có xác suất)
from scipy.stats import binom, poisson, norm, t

# Thiết lập hiển thị đẹp
plt.style.use("ggplot")
plt.rcParams['figure.figsize'] = (10, 6)
```

---

## 📋 MENU TÌM KIẾM SIÊU TỐC - CTRL+F TÌM KEYWORD

### 🔍 THẤY TỪ KHÓA GÌ TRONG ĐỀ → CTRL+F TÌM MÃ ĐÓ

| **THẤY TRONG ĐỀ**                | **TÌM MÃ** | **THAY GÌ**   |
| ----------------------------------------- | ------------------ | -------------------- |
| đọc dữ liệu, hiển thị               | `A01`            | tên file            |
| bao nhiêu dòng, bao nhiêu cột         | `A02`            | không thay          |
| thiếu dữ liệu, missing, null           | `A03`            | không thay          |
| định tính, định lượng, phân loại | `A04`            | không thay          |
| có bao nhiêu, value_counts              | `B01`            | tên cột            |
| nhiều nhất, ít nhất, top              | `B02`            | tên cột            |
| tỷ lệ, %, phần trăm                    | `B03`            | tên cột            |
| theo nhóm, groupby, so sánh             | `B04`            | 2 tên cột          |
| trung bình, mean, median                 | `C01`            | tên cột            |
| độ lệch chuẩn, std, var               | `C02`            | tên cột            |
| phân vị, quantile, Q1, Q3               | `C03`            | tên cột            |
| biểu đồ cột, bar chart                | `D01`            | tên cột            |
| biểu đồ tròn, pie chart               | `D02`            | tên cột            |
| histogram, phân bố                      | `D03`            | tên cột            |
| boxplot, hộp râu                        | `D04`            | tên cột            |
| so sánh boxplot                         | `D05`            | 2 tên cột          |
| ma trận tương quan, heatmap            | `D06`            | không thay          |
| scatter plot, tương quan                | `D07`            | 2 tên cột          |
| xác suất, nhị thức, P(X=k)            | `E01`            | n, p, k              |
| Poisson, λ, lambda                       | `E02`            | λ, k                |
| chuẩn, normal, phân phối chuẩn        | `E03`            | μ, σ, x            |
| lấy mẫu, sample                         | `F01`            | số mẫu             |
| mô phỏng, simulation                    | `F02`            | số lần             |

---

## 📋 MỤC LỤC CHI TIẾT
1. [A - Đọc và Khám phá Dữ liệu](#a---đọc-và-khám-phá-dữ-liệu)
2. [B - Thống kê Cơ bản](#b---thống-kê-cơ-bản)  
3. [C - Thống kê Mô tả](#c---thống-kê-mô-tả)
4. [D - Trực quan hóa](#d---trực-quan-hóa)
5. [E - Xác suất](#e---xác-suất)
6. [F - Lấy mẫu & Mô phỏng](#f---lấy-mẫu--mô-phỏng)
7. [Templates Hoàn chỉnh](#templates-hoàn-chỉnh)

---

## A - ĐỌC VÀ KHÁM PHÁ DỮ LIỆU

### A01 - ĐỌC FILE + HIỂN THỊ ✨ COPY NGUYÊN

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ⭐ THAY TÊN FILE
df = pd.read_csv('TÊN_FILE.csv')
print("5/7/10 dòng đầu:")
print(df.head(5))  # Thay 5→7→10 tùy đề
print("5/7/10 dòng cuối:")
print(df.tail(5))
print("Dữ liệu ngẫu nhiên:")
print(df.sample(5))

# 📝 VÍ DỤ THAY THẾ:
# df = pd.read_csv('tips.csv')
# df = pd.read_csv('mpg.csv') 
# df = pd.read_csv('US_Baby_Names.csv')
```

### A02 - SỐ DÒNG CỘT + THÔNG TIN CƠ BẢN ✨ COPY NGUYÊN

```python
print(f"Dữ liệu có {df.shape[0]} dòng và {df.shape[1]} cột")
print(f"Kích thước: {df.shape}")
print("\nThông tin cột:")
print(df.info())
print("\nThống kê mô tả:")
print(df.describe())
print("\nTên các cột:")
print(df.columns.tolist())
```

### A03 - THIẾU DỮ LIỆU ✨ COPY NGUYÊN

```python
print("Số giá trị thiếu:")
print(df.isnull().sum())
print(f"Tổng thiếu: {df.isnull().sum().sum()}")

# Hiển thị các dòng thiếu dữ liệu
print("Các dòng có giá trị thiếu:")
print(df[df.isnull().any(axis=1)])

# Bỏ dòng thiếu dữ liệu
df_clean = df.dropna()
print(f"Sau khi bỏ thiếu: {df_clean.shape[0]} dòng")

# Điền giá trị thiếu
df['CỘT'] = df['CỘT'].fillna('Unknown')  # ⭐ THAY TÊN CỘT cho cột text
df = df.fillna(0)  # Điền 0 cho tất cả

# Xóa cột không cần thiết
if 'Unnamed: 0' in df.columns:
    df = df.drop('Unnamed: 0', axis=1)
if 'Id' in df.columns:
    df = df.drop('Id', axis=1)
```

### A04 - PHÂN LOẠI THUỘC TÍNH ✨ COPY NGUYÊN

```python
print("Thuộc tính định lượng (số):", df.select_dtypes(include=[np.number]).columns.tolist())
print("Thuộc tính định tính (chữ):", df.select_dtypes(include=['object']).columns.tolist())

# Hiển thị giá trị phân biệt cho thuộc tính định tính
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    print(f"\n{col}: {df[col].unique()}")
    print(f"Số giá trị phân biệt: {df[col].nunique()}")
```

---

## B - THỐNG KÊ CƠ BẢN

### B01 - ĐẾM SỐ LƯỢNG ✨ CHỈ THAY TÊN CỘT

```python
# ⭐ THAY TÊN CỘT
counts = df['TÊN_CỘT'].value_counts()
print("Số lượng từng loại:")
print(counts)
print(f"Tổng có {df['TÊN_CỘT'].nunique()} loại khác nhau")

# 📝 VÍ DỤ:
# df['sex'].value_counts()      # Tips dataset
# df['origin'].value_counts()   # MPG dataset
# df['Gender'].value_counts()   # Baby Names dataset
```

### B02 - TÌM NHIỀU NHẤT/ÍT NHẤT ✨ CHỈ THAY TÊN CỘT

```python
# ⭐ THAY TÊN CỘT
top = df['TÊN_CỘT'].value_counts().head(1)
print(f"Nhiều nhất: {top.index[0]} ({top.iloc[0]} lần)")

least = df['TÊN_CỘT'].value_counts().tail(1)
print(f"Ít nhất: {least.index[0]} ({least.iloc[0]} lần)")

# Top 10
print("Top 10 giá trị:")
top_10 = df['TÊN_CỘT'].value_counts().head(10)
print(top_10)

# 📝 VÍ DỤ:
# df['Name'].value_counts().head(10)  # Top 10 tên baby names
# df['day'].value_counts().head(1)    # Ngày tip nhiều nhất
```

### B03 - TỶ LỆ PHẦN TRĂM ✨ CHỈ THAY TÊN CỘT

```python
# ⭐ THAY TÊN CỘT
counts = df['TÊN_CỘT'].value_counts()
percentages = (counts / len(df) * 100).round(1)
print("Tỷ lệ %:")
for i, value in enumerate(counts.index):
    print(f"{value}: {counts.iloc[i]} ({percentages.iloc[i]}%)")

# Tỷ lệ trực tiếp
percent_direct = df['TÊN_CỘT'].value_counts(normalize=True) * 100
print("\nTỷ lệ % trực tiếp:")
print(percent_direct.round(1))

# 📝 VÍ DỤ ĐẶC BIỆT - Tỷ lệ theo điều kiện:
# Tỷ lệ người muốn giảm cân
# want_lose = (df['wtdesire'] < df['weight']).sum()
# percent_lose = want_lose / len(df) * 100
# print(f"Tỷ lệ người muốn giảm cân: {percent_lose:.1f}%")
```

### B04 - SO SÁNH THEO NHÓM ✨ THAY 2 TÊN CỘT

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

# Group by cơ bản
grouped = df.groupby('CỘT_NHÓM')['CỘT_GIÁ_TRỊ'].agg(['count', 'mean', 'std']).round(2)
print("Thống kê theo nhóm:")
print(grouped)

# 📝 VÍ DỤ:
# df.groupby('sex')['tip'].agg(['count', 'mean'])        # Tips
# df.groupby('origin')['mpg'].agg(['count', 'mean'])     # MPG  
# pd.crosstab(df['Gender'], df['Grade'])                 # Grades
```

---

## C - THỐNG KÊ MÔ TẢ

### C01 - TRUNG BÌNH, TRUNG VỊ ✨ CHỈ THAY TÊN CỘT

```python
# ⭐ THAY TÊN CỘT
print(f"Trung bình: {df['TÊN_CỘT'].mean():.3f}")
print(f"Trung vị: {df['TÊN_CỘT'].median():.3f}")
print(f"Mode: {df['TÊN_CỘT'].mode().iloc[0] if len(df['TÊN_CỘT'].mode()) > 0 else 'N/A'}")

# Thống kê tổng hợp
print("\nThống kê tổng hợp:")
print(df['TÊN_CỘT'].describe())

# Theo nhóm
group_stats = df.groupby('CỘT_NHÓM')['CỘT_GIÁ_TRỊ'].agg(['mean', 'median', 'std', 'count']).round(2)
print("Thống kê theo nhóm:")
print(group_stats)

# 📝 VÍ DỤ:
# df['tip'].mean()                           # Tips dataset
# df['mpg'].median()                         # MPG dataset
# df.groupby('sex')['tip'].mean()           # Tip trung bình theo giới tính
```

### C02 - ĐỘ LỆCH CHUẨN, PHƯƠNG SAI ✨ CHỈ THAY TÊN CỘT

```python
# ⭐ THAY TÊN CỘT
print(f"Độ lệch chuẩn: {df['TÊN_CỘT'].std():.3f}")
print(f"Phương sai: {df['TÊN_CỘT'].var():.3f}")
print(f"Min: {df['TÊN_CỘT'].min():.3f}")
print(f"Max: {df['TÊN_CỘT'].max():.3f}")
print(f"Khoảng (Range): {df['TÊN_CỘT'].max() - df['TÊN_CỘT'].min():.3f}")

# Hệ số biến thiên
cv = (df['TÊN_CỘT'].std() / df['TÊN_CỘT'].mean()) * 100
print(f"Hệ số biến thiên: {cv:.2f}%")

# 📝 VÍ DỤ:
# df['total_bill'].std()                    # Tips dataset
# df['weight'].var()                        # MPG dataset
```

### C03 - PHÂN VỊ ✨ CHỈ THAY TÊN CỘT

```python
# ⭐ THAY TÊN CỘT
q1 = df['TÊN_CỘT'].quantile(0.25)
q2 = df['TÊN_CỘT'].quantile(0.50)  # Trung vị
q3 = df['TÊN_CỘT'].quantile(0.75)

print(f"Q1 (25%): {q1:.3f}")
print(f"Q2 (50%): {q2:.3f}")
print(f"Q3 (75%): {q3:.3f}")
print(f"IQR: {q3-q1:.3f}")

# Miền giá trị và miền phân vị
print(f"Miền giá trị: [{df['TÊN_CỘT'].min():.1f}, {df['TÊN_CỘT'].max():.1f}]")
print(f"Miền phân vị (Q1, Q3): [{q1:.1f}, {q3:.1f}]")

# 📝 VÍ DỤ MPG dataset:
# q1 = df['mpg'].quantile(0.25)
# q3 = df['mpg'].quantile(0.75)
# print(f"Miền phân vị mpg: [{q1:.1f}, {q3:.1f}]")
```

---

## D - TRỰC QUAN HÓA

### D01 - BIỂU ĐỒ CỘT ✨ CHỈ THAY TÊN CỘT

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

# 📝 VÍ DỤ:
# df['sex'].value_counts().plot(kind='bar')              # Tips
# df.groupby('day')['tip'].sum().plot(kind='bar')        # Tip theo ngày
# df.groupby('origin')['mpg'].mean().plot(kind='bar')    # MPG theo origin
```

### D02 - BIỂU ĐỒ TRÒN ✨ CHỈ THAY TÊN CỘT

```python
# ⭐ THAY TÊN CỘT
plt.figure(figsize=(10, 8))
counts = df['TÊN_CỘT'].value_counts()
plt.pie(counts.values, labels=counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Biểu đồ tròn - TÊN_CỘT')
plt.axis('equal')
plt.tight_layout()
plt.show()

# 📝 VÍ DỤ:
# counts = df['time'].value_counts()
# plt.pie(counts.values, labels=counts.index, autopct='%1.1f%%')
```

### D03 - HISTOGRAM ✨ CHỈ THAY TÊN CỘT

```python
# ⭐ THAY TÊN CỘT
plt.figure(figsize=(10, 6))
plt.hist(df['TÊN_CỘT'].dropna(), bins=30, color='lightgreen', alpha=0.7, edgecolor='black')
plt.title('Histogram - TÊN_CỘT')
plt.xlabel('Giá trị')
plt.ylabel('Tần suất')
plt.grid(axis='y', alpha=0.3)

# Thêm đường trung bình
mean_val = df['TÊN_CỘT'].mean()
plt.axvline(mean_val, color='red', linestyle='--', linewidth=2, label=f'TB: {mean_val:.2f}')
plt.legend()
plt.show()

# 📝 VÍ DỤ:
# plt.hist(df['total_bill'].dropna(), bins=20)    # Tips
# plt.hist(df['mpg'].dropna(), bins=30)           # MPG
# plt.hist(df['weight'].dropna(), bins=25)        # Weight
```

### D04 - BOXPLOT ĐỞN GIẢN ✨ CHỈ THAY TÊN CỘT

```python
# ⭐ THAY TÊN CỘT
plt.figure(figsize=(8, 6))
plt.boxplot(df['TÊN_CỘT'].dropna())
plt.title('Boxplot - TÊN_CỘT')
plt.ylabel('Giá trị')
plt.show()

# Nhiều cột cùng lúc với pandas
df[['CỘT_1', 'CỘT_2', 'CỘT_3']].boxplot(figsize=(10, 6))
plt.title('Boxplot nhiều cột')
plt.show()

# 📝 VÍ DỤ:
# plt.boxplot(df['tip'].dropna())                    # Tips
# df[['mpg', 'horsepower', 'weight']].boxplot()     # MPG multiple columns
```

### D05 - BOXPLOT SO SÁNH NHÓM ✨ THAY 2 TÊN CỘT

```python
# ⭐ THAY 2 TÊN CỘT

# Cách 1: Pandas
plt.figure(figsize=(12, 8))
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

# 📝 VÍ DỤ:
# sns.boxplot(data=df, x='sex', y='tip')              # Tips theo giới tính
# sns.boxplot(data=df, x='origin', y='mpg')           # MPG theo origin
# df.boxplot(column='horsepower', by='cylinders')     # Horsepower theo cylinders
```

### D06 - MA TRẬN TƯƠNG QUAN ✨ COPY NGUYÊN

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

# In ma trận tương quan
print("Ma trận tương quan:")
print(correlation_matrix.round(3))
```

### D07 - SCATTER PLOT ✨ THAY 2 TÊN CỘT

```python
# ⭐ THAY 2 TÊN CỘT
plt.figure(figsize=(10, 6))
plt.scatter(df['CỘT_X'], df['CỘT_Y'], alpha=0.6)
plt.title('Tương quan giữa X và Y')
plt.xlabel('CỘT_X')
plt.ylabel('CỘT_Y')
plt.grid(True, alpha=0.3)

# Thêm đường xu hướng
z = np.polyfit(df['CỘT_X'].dropna(), df['CỘT_Y'].dropna(), 1)
p = np.poly1d(z)
plt.plot(df['CỘT_X'], p(df['CỘT_X']), "r--", alpha=0.8, linewidth=2)

# Tính hệ số tương quan
correlation = df['CỘT_X'].corr(df['CỘT_Y'])
plt.title(f'Tương quan: {correlation:.3f}')
plt.show()

# 📝 VÍ DỤ:
# plt.scatter(df['total_bill'], df['tip'])        # Tips
# plt.scatter(df['horsepower'], df['mpg'])        # MPG
# correlation = df['total_bill'].corr(df['tip'])  # Tính tương quan
```

---

## E - XÁC SUẤT & PHÂN PHỐI 🎲

### E01 - PHÂN PHỐI NHỊ THỨC ✨ THAY n, p, k

```python
from scipy.stats import binom

# ⭐ THAY SỐ THEO ĐỀ BÀI
n = 10     # Số lần thử (số câu hỏi, số sản phẩm...)
p = 0.4    # Xác suất thành công (tỷ lệ đúng, tỷ lệ đạt chuẩn...)
k = 4      # Số lần thành công cần tìm

# Tạo phân phối nhị thức
binomial_dist = binom(n, p)

# a. P(X = k) - Xác suất có đúng k lần thành công
prob_k = binomial_dist.pmf(k)
print(f"P(X = {k}) = {prob_k:.6f}")

# b. Lập bảng phân phối xác suất
print("Bảng phân phối xác suất:")
for i in range(n+1):
    prob = binomial_dist.pmf(i)
    print(f"P(X = {i}) = {prob:.4f}")

# c. Các xác suất quan trọng
print(f"P(X <= {k}) = {binomial_dist.cdf(k):.6f}")  # Nhỏ hơn bằng
print(f"P(X >= {k}) = {1 - binomial_dist.cdf(k-1):.6f}")  # Lớn hơn bằng
print(f"P(X > {k}) = {1 - binomial_dist.cdf(k):.6f}")  # Lớn hơn

# d. Kỳ vọng và phương sai
print(f"E(X) = {binomial_dist.mean():.2f}")
print(f"Var(X) = {binomial_dist.var():.2f}")
print(f"Std(X) = {binomial_dist.std():.2f}")

# e. Tính E(aX + b) và Var(cX + d)
a, b, c, d = 3, -5, 2, 1  # ⭐ THAY SỐ THEO ĐỀ
E_aX_b = a * binomial_dist.mean() + b
Var_cX_d = c**2 * binomial_dist.var()
print(f"E({a}X + {b}) = {E_aX_b:.2f}")
print(f"Var({c}X + {d}) = {Var_cX_d:.2f}")

# f. Vẽ biểu đồ
x_values = range(0, n+1)
probs = [binomial_dist.pmf(x) for x in x_values]
plt.figure(figsize=(10, 6))
plt.bar(x_values, probs, alpha=0.7, color='lightblue', edgecolor='black')
plt.title(f'Phân phối nhị thức B({n}, {p})')
plt.xlabel('Số lần thành công (k)')
plt.ylabel('P(X = k)')
plt.xticks(x_values)
plt.grid(axis='y', alpha=0.3)
plt.show()

# 📝 VÍ DỤ ĐỀ BÀI:
# "10 câu trắc nghiệm, mỗi câu 4 đáp án" → n=10, p=1/4=0.25
# "5 sản phẩm, 70% đạt chuẩn" → n=5, p=0.7
# "15 bệnh nhân, 40% khỏi bệnh" → n=15, p=0.4
```

### E02 - PHÂN PHỐI POISSON ✨ THAY λ, k

```python
from scipy.stats import poisson

# ⭐ THAY SỐ THEO ĐỀ BÀI
lam = 3     # Lambda (trung bình số sự kiện)
k = 2       # Số sự kiện cần tìm

# Tạo phân phối Poisson
poisson_dist = poisson(lam)

# a. P(X = k) - Xác suất có đúng k sự kiện
prob_k = poisson_dist.pmf(k)
print(f"P(X = {k}) = {prob_k:.6f}")

# b. Lập bảng phân phối (thường từ 0 đến 3λ)
print("Bảng phân phối xác suất:")
for i in range(0, int(3*lam)+1):
    prob = poisson_dist.pmf(i)
    if prob > 0.001:  # Chỉ in nếu xác suất > 0.1%
        print(f"P(X = {i}) = {prob:.4f}")

# c. Các xác suất quan trọng
print(f"P(X = 0) = {poisson_dist.pmf(0):.6f}")  # Không có sự kiện
print(f"P(X <= {k}) = {poisson_dist.cdf(k):.6f}")  # Nhỏ hơn bằng
print(f"P(X >= {k}) = {1 - poisson_dist.cdf(k-1):.6f}")  # Lớn hơn bằng
print(f"P(X > {k}) = {1 - poisson_dist.cdf(k):.6f}")  # Lớn hơn

# d. Kỳ vọng và phương sai (đều = λ)
print(f"E(X) = {poisson_dist.mean():.2f}")
print(f"Var(X) = {poisson_dist.var():.2f}")

# e. Thay đổi thời gian/không gian
# Nếu λ = 3 sự kiện/giờ, tính cho 2 giờ hoặc 30 phút
lam_2h = lam * 2      # 2 giờ
lam_30m = lam * 0.5   # 30 phút
print(f"λ trong 2 giờ: {lam_2h}")
print(f"λ trong 30 phút: {lam_30m}")

# f. Vẽ biểu đồ
x_values = range(0, int(3*lam)+1)
probs = [poisson_dist.pmf(x) for x in x_values]
plt.figure(figsize=(10, 6))
plt.bar(x_values, probs, alpha=0.7, color='lightcoral', edgecolor='black')
plt.title(f'Phân phối Poisson(λ = {lam})')
plt.xlabel('Số sự kiện (k)')
plt.ylabel('P(X = k)')
plt.xticks(x_values)
plt.grid(axis='y', alpha=0.3)
plt.show()

# 📝 VÍ DỤ ỨNG DỤNG:
# "3 cuộc gọi/phút" → λ=3
# "6 xe/phút qua trạm" → λ=6  
# "10 cuộc gọi/giờ" → λ=10 (1 giờ), λ=5 (30 phút), λ=20 (2 giờ)
# "2% sản phẩm lỗi, 1000 sản phẩm" → λ = 1000×0.02 = 20
```

### E03 - PHÂN PHỐI CHUẨN ✨ THAY μ, σ, x

```python
from scipy.stats import norm
import numpy as np

# ⭐ THAY SỐ THEO ĐỀ BÀI
mu = 500      # Trung bình (μ)
sigma = 4     # Độ lệch chuẩn (σ)
x1, x2 = 495, 505  # Các giá trị cần tìm

# Tạo phân phối chuẩn
normal_dist = norm(mu, sigma)

# a. P(X < x) - Xác suất nhỏ hơn
prob_less = normal_dist.cdf(x1)
print(f"P(X < {x1}) = {prob_less:.6f}")

# b. P(X > x) - Xác suất lớn hơn  
prob_greater = 1 - normal_dist.cdf(x2)
print(f"P(X > {x2}) = {prob_greater:.6f}")

# c. P(a < X < b) - Xác suất trong khoảng
prob_between = normal_dist.cdf(x2) - normal_dist.cdf(x1)
print(f"P({x1} < X < {x2}) = {prob_between:.6f}")

# d. Tìm giá trị tại phân vị
percentiles = [0.25, 0.5, 0.75, 0.95]
print("Các phân vị:")
for p in percentiles:
    value = normal_dist.ppf(p)
    print(f"Phân vị {p*100}%: {value:.2f}")

# e. Phân loại theo khoảng (ví dụ trái cây)
print("\nPhân loại:")
loai1 = 1 - normal_dist.cdf(x2)  # > 505
loai2 = normal_dist.cdf(x2) - normal_dist.cdf(x1)  # 495-505  
loai3 = normal_dist.cdf(x1)  # < 495
print(f"Loại 1 (>{x2}): {loai1:.4f} ({loai1*100:.1f}%)")
print(f"Loại 2 ({x1}-{x2}): {loai2:.4f} ({loai2*100:.1f}%)")
print(f"Loại 3 (<{x1}): {loai3:.4f} ({loai3*100:.1f}%)")

# f. Mô phỏng mẫu
sample_sizes = [20, 100, 1000]
print("\nMô phỏng mẫu:")
for n in sample_sizes:
    sample = normal_dist.rvs(n)
    print(f"n={n}: mean={np.mean(sample):.2f}, std={np.std(sample, ddof=1):.2f}")

# g. Vẽ đồ thị
x_range = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = normal_dist.pdf(x_range)

plt.figure(figsize=(12, 8))

# Đồ thị chính
plt.subplot(2, 2, 1)
plt.plot(x_range, y, 'b-', linewidth=2, label=f'μ={mu}, σ={sigma}')
plt.title('Hàm mật độ xác suất')
plt.xlabel('Giá trị')
plt.ylabel('Mật độ')
plt.grid(True, alpha=0.3)
plt.legend()

# Tô vùng P(a < X < b)
plt.subplot(2, 2, 2)
plt.plot(x_range, y, 'b-', linewidth=2)
x_fill = np.linspace(x1, x2, 100)
y_fill = normal_dist.pdf(x_fill)
plt.fill_between(x_fill, y_fill, alpha=0.3, color='red')
plt.title(f'P({x1} < X < {x2}) = {prob_between:.4f}')
plt.xlabel('Giá trị')
plt.ylabel('Mật độ')

# Histogram mẫu n=100
plt.subplot(2, 2, 3)
sample_100 = normal_dist.rvs(100)
plt.hist(sample_100, bins=15, alpha=0.7, density=True, edgecolor='black')
plt.plot(x_range, y, 'r-', linewidth=2, label='Lý thuyết')
plt.title('Histogram mẫu n=100')
plt.legend()

# Histogram mẫu n=1000
plt.subplot(2, 2, 4)
sample_1000 = normal_dist.rvs(1000)
plt.hist(sample_1000, bins=30, alpha=0.7, density=True, edgecolor='black')
plt.plot(x_range, y, 'r-', linewidth=2, label='Lý thuyết')
plt.title('Histogram mẫu n=1000')
plt.legend()

plt.tight_layout()
plt.show()

# 📝 VÍ DỤ ĐỀ BÀI:
# "Chiều cao nam μ=170cm, σ=5cm" → P(165 < X < 175)
# "Trọng lượng trái cây μ=500g, σ=4g" → Phân loại theo khoảng
# "Điểm thi μ=100, σ=15" → P(X > 120), phân vị 95%
```

---

## 🎯 BÀI TẬP MẪU PHÂN PHỐI XÁC SUẤT

### 📚 BÀI 1: TRẮC NGHIỆM (NHỊ THỨC)
**Đề bài:** Một bài thi trắc nghiệm gồm 10 câu, mỗi câu có 4 phương án. Sinh viên làm bài bằng cách chọn ngẫu nhiên. Mỗi câu đúng được 4 điểm, sai bị trừ 2 điểm.

**⚡ Giải nhanh:**
```python
# Thiết lập
n, p = 10, 0.25  # 10 câu, 1/4 xác suất đúng
binomial_dist = binom(n, p)

# a) E(X) và Var(X)
print(f"E(X) = {binomial_dist.mean()}")
print(f"Var(X) = {binomial_dist.var()}")

# b) Xác suất được 4 điểm (4 câu đúng)
# Điểm = 4×đúng - 2×sai = 4×đúng - 2×(10-đúng) = 6×đúng - 20
# Để được 4 điểm: 6×đúng - 20 = 4 → đúng = 4 câu
prob_4_diem = binomial_dist.pmf(4)
print(f"P(được 4 điểm) = {prob_4_diem:.6f}")

# c) Mô phỏng 10 lần thi
results = [binomial_dist.rvs() for _ in range(10)]
print(f"Kết quả 10 lần: {results}")
```

### 📚 BÀI 2: CUỘC GỌI ĐIỆN THOẠI (POISSON)
**Đề bài:** Trung tâm bưu điện nhận được 3 cuộc gọi mỗi phút. Tính xác suất nhận được 1, 2, 3 cuộc gọi trong một phút.

**⚡ Giải nhanh:**
```python
# Thiết lập  
lam = 3  # λ = 3 cuộc gọi/phút
poisson_dist = poisson(lam)

# Tính xác suất cho 1, 2, 3 cuộc gọi
for k in [1, 2, 3]:
    prob = poisson_dist.pmf(k)
    print(f"P(X = {k}) = {prob:.6f}")

# Mở rộng: Trong 2 phút, 30 giây
lam_2m = lam * 2      # 6 cuộc gọi/2 phút  
lam_30s = lam * 0.5   # 1.5 cuộc gọi/30 giây
print(f"Trong 2 phút, P(X = 5) = {poisson(lam_2m).pmf(5):.6f}")
print(f"Trong 30s, P(X = 1) = {poisson(lam_30s).pmf(1):.6f}")
```

### 📚 BÀI 3: TRỌNG LƯỢNG TRÁI CÂY (CHUẨN)
**Đề bài:** Trọng lượng trái cây có phân phối chuẩn μ=500g, σ²=16g². Phân loại: Loại 1 (>505g), Loại 2 (495-505g), Loại 3 (<495g).

**⚡ Giải nhanh:**
```python
# Thiết lập
mu, sigma = 500, 4  # σ = √16 = 4
normal_dist = norm(mu, sigma)

# a) Tỷ lệ từng loại
loai1 = 1 - normal_dist.cdf(505)
loai2 = normal_dist.cdf(505) - normal_dist.cdf(495)  
loai3 = normal_dist.cdf(495)

print(f"Loại 1 (>505g): {loai1:.4f} ({loai1*100:.1f}%)")
print(f"Loại 2 (495-505g): {loai2:.4f} ({loai2*100:.1f}%)")
print(f"Loại 3 (<495g): {loai3:.4f} ({loai3*100:.1f}%)")

# b) Mô phỏng mẫu 20 và 100 trái
sample20 = normal_dist.rvs(20)
sample100 = normal_dist.rvs(100)

print(f"\nMẫu 20: mean={np.mean(sample20):.2f}, std={np.std(sample20, ddof=1):.2f}")
print(f"Mẫu 100: mean={np.mean(sample100):.2f}, std={np.std(sample100, ddof=1):.2f}")

# c) Vẽ so sánh
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
ax1.hist(sample20, bins=5, alpha=0.7, density=True)
ax1.set_title('Mẫu 20')
ax2.hist(sample100, bins=10, alpha=0.7, density=True)
ax2.set_title('Mẫu 100')
plt.show()
```

### 📚 BÀI 4: SẢN PHẨM LỖI (POISSON XẤP XỈ NHỊ THỨC)
**Đề bài:** Máy dệt có 5000 ống sợi, xác suất mỗi ống ngưng hoạt động trong 1 phút là 0.0004. Tính xác suất có >2 ống ngưng hoạt động.

**⚡ Giải nhanh:**
```python
# Phương pháp 1: Nhị thức (chính xác)
n, p = 5000, 0.0004
binomial_dist = binom(n, p)
prob_binom = 1 - binomial_dist.cdf(2)

# Phương pháp 2: Poisson (xấp xỉ)  
lam = n * p  # λ = 5000 × 0.0004 = 2
poisson_dist = poisson(lam)
prob_poisson = 1 - poisson_dist.cdf(2)

print(f"n={n}, p={p} → λ={lam}")
print(f"P(X > 2) - Nhị thức: {prob_binom:.6f}")
print(f"P(X > 2) - Poisson: {prob_poisson:.6f}")
print(f"Sai số: {abs(prob_binom - prob_poisson):.6f}")

# Khi nào dùng Poisson xấp xỉ Nhị thức?
print("\n📝 Điều kiện xấp xỉ: n lớn, p nhỏ, np vừa phải")
print(f"n={n} (lớn ✓), p={p} (nhỏ ✓), np={n*p} (vừa ✓)")
```

### 📚 BÀI 5: ĐIỀU TRỊ BỆNH (NHỊ THỨC)
**Đề bài:** Xác suất chữa khỏi bệnh là 0.4. Có 15 người điều trị. Tính xác suất: a) Ít nhất 10 người khỏi, b) Từ 3-8 người khỏi, c) Đúng 5 người khỏi.

**⚡ Giải nhanh:**
```python
# Thiết lập
n, p = 15, 0.4
binomial_dist = binom(n, p)

# a) P(X >= 10) = 1 - P(X <= 9)
prob_a = 1 - binomial_dist.cdf(9)
print(f"a) P(X >= 10) = {prob_a:.6f}")

# b) P(3 <= X <= 8) = P(X <= 8) - P(X <= 2)  
prob_b = binomial_dist.cdf(8) - binomial_dist.cdf(2)
print(f"b) P(3 <= X <= 8) = {prob_b:.6f}")

# c) P(X = 5)
prob_c = binomial_dist.pmf(5)
print(f"c) P(X = 5) = {prob_c:.6f}")

# Thống kê
print(f"\nE(X) = {binomial_dist.mean():.1f} người")
print(f"Std(X) = {binomial_dist.std():.2f} người")

# Giá trị có xác suất cao nhất (mode)
mode = int(n * p)
print(f"Số người khỏi có khả năng cao nhất: {mode}")
```

### 📚 BÀI 6: KIỂM TRA CHẤT LƯỢNG (NHỊ THỨC LỒNG)
**Đề bài:** Thiết bị điện tử có 3% bị hỏng. Kiểm tra ngẫu nhiên 20 thiết bị từ mỗi lô. Có 10 lô/tháng. Tính xác suất có đúng 3 lô chứa ít nhất 1 thiết bị hỏng.

**⚡ Giải nhanh:**
```python
# Bước 1: Xác suất 1 lô có ít nhất 1 thiết bị hỏng
n_thiet_bi, p_hong = 20, 0.03
prob_it_nhat_1 = 1 - binom(n_thiet_bi, p_hong).pmf(0)
print(f"P(ít nhất 1 hỏng trong 20) = {prob_it_nhat_1:.6f}")

# Bước 2: Trong 10 lô, có đúng 3 lô chứa ít nhất 1 hỏng
n_lo = 10
prob_3_lo = binom(n_lo, prob_it_nhat_1).pmf(3)
print(f"P(đúng 3 lô có hỏng) = {prob_3_lo:.6f}")

# Giải thích
print(f"\n📝 Giải thích:")
print(f"- Mỗi lô: n={n_thiet_bi}, p={p_hong}")
print(f"- P(lô có hỏng) = {prob_it_nhat_1:.4f}")
print(f"- 10 lô: n={n_lo}, p={prob_it_nhat_1:.4f}")
print(f"- Cần đúng 3 lô có hỏng")
```

---

## 🏆 TIPS QUAN TRỌNG KHI LÀM BÀI PHÂN PHỐI

### ✅ NHẬN DẠNG PHÂN PHỐI:

| **Từ khóa trong đề** | **Phân phối** | **Tham số** |
|---------------------|---------------|-------------|
| "trắc nghiệm", "có/không", "thành công/thất bại" | **Nhị thức** | n (số lần), p (xác suất) |
| "số lần xảy ra", "trung bình X lần", "hiếm" | **Poisson** | λ (trung bình) |
| "chiều cao", "cân nặng", "điểm số", "sai số" | **Chuẩn** | μ (TB), σ (độ lệch) |

### ✅ CÁC CÔNG THỨC NHANH:

```python
# P(X >= k) = 1 - P(X <= k-1) = 1 - cdf(k-1)
# P(X > k) = 1 - P(X <= k) = 1 - cdf(k)  
# P(a <= X <= b) = cdf(b) - cdf(a-1)  # Rời rạc
# P(a < X < b) = cdf(b) - cdf(a)      # Liên tục

# Nhị thức: E(X) = np, Var(X) = np(1-p)
# Poisson: E(X) = Var(X) = λ
# Chuẩn: E(X) = μ, Var(X) = σ²

# Tuyến tính: E(aX + b) = aE(X) + b
#            Var(aX + b) = a²Var(X)
```

### ✅ KHI NÀO DÙNG POISSON XẤP XỈ NHỊ THỨC:
- **n lớn** (>= 100), **p nhỏ** (<= 0.01), **np vừa** (<= 10)
- **λ = np**
- **Ví dụ:** n=1000, p=0.002 → λ=2 ✓

---

*🎯 Học thuộc các template này, khi thi chỉ cần thay số và chạy!*
import matplotlib.pyplot as plt
import seaborn as sns
```

### 🎯 Đọc dữ liệu và làm sạch:
```python
# Template cơ bản
df = pd.read_csv('FILE_NAME.csv')  # ⚠️ SỬA TÊN FILE
df = df.drop('Unnamed: 0', axis=1)  # Xóa cột index (nếu có)
df = df.dropna()  # Xóa dòng null
print(f"Dữ liệu: {df.shape[0]} dòng, {df.shape[1]} cột")
```

### 🎯 Thống kê nhanh:
```python
# Mô tả tổng quan
print(df.describe())

# Thống kê 1 biến
bien = 'TEN_BIEN'  # ⚠️ SỬA
print(f"TB: {df[bien].mean():.2f}")
print(f"TV: {df[bien].median():.2f}")
print(f"Min-Max: {df[bien].min():.2f} - {df[bien].max():.2f}")
```

### 🎯 Group by nhanh:
```python
# Template group by cơ bản
result = df.groupby('BIEN_NHOM')['BIEN_SO'].agg(['mean', 'sum', 'count']).round(2)  # ⚠️ SỬA
print(result)
```

### 🎯 Plot nhanh:
```python
# Bar chart nhanh
df.groupby('BIEN_NHOM')['BIEN_SO'].mean().plot(kind='bar')  # ⚠️ SỬA
plt.title('TIÊU ĐỀ')  # ⚠️ SỬA
plt.show()

# Scatter plot nhanh
df.plot.scatter('BIEN_X', 'BIEN_Y')  # ⚠️ SỬA
plt.title('TIÊU ĐỀ')  # ⚠️ SỬA
plt.show()
```

---

## 🚨 CHECKLIST KHI LÀM BÀI THI

### ✅ Bước 1: Đọc đề và xác định
- [ ] File dữ liệu tên gì? (tips.csv, mpg.csv, US_Baby_Names.csv...)
- [ ] Biến cần phân tích là gì? (tip, mpg, Count, Final Exam...)
- [ ] Cần tính thống kê gì? (mean, median, sum, count, correlation...)
- [ ] Cần so sánh theo nhóm nào? (sex, origin, Gender, Grade...)
- [ ] Cần vẽ biểu đồ gì? (bar, scatter, line, histogram, boxplot...)

### ✅ Bước 2: Setup cơ bản
- [ ] Import thư viện: `pandas, numpy, matplotlib.pyplot, seaborn`
- [ ] Đọc file CSV: `pd.read_csv('filename.csv')`
- [ ] Xóa cột thừa: `df.drop(['Unnamed: 0'], axis=1)`
- [ ] Kiểm tra null: `df.isnull().sum()`

### ✅ Bước 3: Thực hiện yêu cầu
- [ ] Tìm template phù hợp trong tài liệu
- [ ] Copy code và sửa tên biến
- [ ] Sửa tiêu đề biểu đồ cho phù hợp
- [ ] Chạy và kiểm tra kết quả hợp lý

### ✅ Bước 4: Hoàn thiện
- [ ] Format số thập phân (.2f, .1f)
- [ ] Thêm tiêu đề và nhãn trục
- [ ] Kiểm tra logic kết quả
- [ ] So sánh với dữ liệu gốc

---

## 🎯 KEYWORDS QUAN TRỌNG TRONG ĐỀ THI

| Từ khóa trong đề | Code cần dùng | Dataset ví dụ |
|------------------|---------------|---------------|
| **"trung bình"** | `.mean()` | `df['tip'].mean()` |
| **"trung vị"** | `.median()` | `df['mpg'].median()` |
| **"tỷ lệ"** | `.value_counts(normalize=True)*100` | `df['Gender'].value_counts(normalize=True)*100` |
| **"so sánh"** | `.groupby().agg(['mean','sum','count'])` | `df.groupby('sex')['tip'].mean()` |
| **"top 10"** | `.nlargest(10)` hoặc `.head(10)` | `df.groupby('Name')['Count'].sum().nlargest(10)` |
| **"mối quan hệ"** | `.corr()` + scatter plot | `df['mpg'].corr(df['weight'])` |
| **"phân phối"** | histogram | `plt.hist(df['total_bill'])` |
| **"so sánh nhóm"** | boxplot | `sns.boxplot(data=df, x='origin', y='mpg')` |
| **"xu hướng"** | line plot | `plt.plot(years, values)` |
| **"năm 2014"** | filter data | `df[df['Year'] == 2014]` |

---

## 🔧 TEMPLATE SIÊU NHANH - COPY PASTE

### 📊 Thống kê cơ bản 1 biến:
```python
col = 'TEN_COT'  # ⚠️ SỬA
print(f"TB: {df[col].mean():.2f}, TV: {df[col].median():.2f}")
print(f"Min-Max: {df[col].min():.2f} - {df[col].max():.2f}")
```

### 📊 So sánh nhóm:
```python
result = df.groupby('NHOM')['GIA_TRI'].agg(['mean','count']).round(2)  # ⚠️ SỬA
print(result)
```

### 📊 Top N:
```python
top_n = df.groupby('NHOM')['GIA_TRI'].sum().nlargest(10)  # ⚠️ SỬA N và tên cột
print(top_n)
```

### 📊 Vẽ nhanh:
```python
# Bar chart
df.groupby('NHOM')['GIA_TRI'].mean().plot(kind='bar')  # ⚠️ SỬA
plt.title('TIÊU ĐỀ'); plt.show()  # ⚠️ SỬA

# Scatter  
plt.scatter(df['X'], df['Y']); plt.title('TIÊU ĐỀ'); plt.show()  # ⚠️ SỬA
```

### 📊 Lọc dữ liệu:
```python
# Lọc theo điều kiện
filtered = df[df['COT'] == 'GIA_TRI']  # ⚠️ SỬA
print(f"Số dòng sau lọc: {len(filtered)}")
```

---

## 📝 LƯU Ý QUAN TRỌNG

1. **⚠️ LUÔN SỬA TÊN BIẾN** trong code template cho phù hợp với đề bài
2. **📊 CHỌN ĐÚNG LOẠI BIỂU ĐỒ** theo yêu cầu đề
3. **🔢 FORMAT SỐ** với `.2f` cho số thập phân
4. **📋 ĐỌC KỸ ĐỀ** để xác định biến nào cần phân tích
5. **✅ KIỂM TRA KẾT QUẢ** có hợp lý không

---

*Tài liệu được tổng hợp từ bài tập Tips, MPG, US Baby Names, Pandas và Matplotlib. Chúc bạn thi tốt! 🎯*

---

## 📚 PHỤ LỤC: VÍ DỤ CỤ THỂ VÀ HÌNH DUNG

### 🎯 VÍ DỤ THAY THẾ BIẾN - DATASET TIPS:
```python
# ❌ Template gốc:
df.groupby('BIEN_NHOM')['BIEN_SO'].mean()

# ✅ Áp dụng cho Tips:
df.groupby('sex')['tip'].mean()           # tip trung bình theo giới tính
df.groupby('day')['total_bill'].sum()     # tổng hóa đơn theo ngày
df.groupby('time')['tip'].count()         # số lượng tip theo bữa ăn
```

### 🎯 VÍ DỤ THAY THẾ BIẾN - DATASET MPG:
```python
# ❌ Template gốc:
df['BIEN_CAN_SO_SANH'].corr(df['BIEN_KHAC'])

# ✅ Áp dụng cho MPG:
df['mpg'].corr(df['horsepower'])         # tương quan mpg với công suất
df['mpg'].corr(df['weight'])             # tương quan mpg với trọng lượng
df['mpg'].corr(df['cylinders'])          # tương quan mpg với số xi lanh
```

### 🎯 VÍ DỤ THAY THẾ BIẾN - DATASET US BABY NAMES:
```python
# ❌ Template gốc:
df.groupby(['Year', 'Gender'])['Count'].sum().unstack()

# ✅ Áp dụng cho Baby Names:
df.groupby(['Year', 'Gender'])['Count'].sum().unstack()  # đúng rồi!
df[df['Year'] == 2014]                   # lọc dữ liệu năm 2014
df.groupby('Name')['Count'].sum()        # tổng theo tên
```

### 🎯 BẢNG CHEAT SHEET - THAY THẾ NHANH:

| Dataset | Cột Số | Cột Phân Loại | Cột Thời Gian | Cột ID |
|---------|---------|---------------|---------------|---------|
| **Tips** | tip, total_bill, size | sex, smoker, day, time | - | - |
| **MPG** | mpg, horsepower, weight, acceleration | origin | model_year | - |
| **Baby Names** | Count | Name, Gender | Year | Id (xóa) |
| **Grades** | Project 1, Project 2, Final Exam | Gender, Grade | - | Student ID (xóa) |

### 🎯 VÍ DỤ GROUPBY NÂNG CAO:

#### Giải thích groupby().unstack():
```python
# BƯỚC 1: Groupby tạo MultiIndex Series
result = df.groupby(['Year', 'Gender'])['Count'].sum()
# Kết quả: 
# Year Gender
# 2004 F      1500000
#      M      1600000  
# 2005 F      1520000
#      M      1580000

# BƯỚC 2: unstack() chuyển thành DataFrame
table = result.unstack()
# Kết quả:
# Gender     F        M
# Year               
# 2004    1500000  1600000
# 2005    1520000  1580000

# BƯỚC 3: Tính tỷ lệ %
percentage = table.div(table.sum(axis=1), axis=0) * 100
# Kết quả:
# Gender      F     M
# Year              
# 2004     48.4  51.6
# 2005     49.0  51.0
```

### 🎯 VÍ DỤ SCATTER PLOT VÀ TƯƠNG QUAN:
```python
# Template:
plt.scatter(df['BIEN_X'], df['BIEN_Y'])

# Áp dụng:
plt.scatter(df['horsepower'], df['mpg'])      # MPG: công suất vs tiêu hao
plt.scatter(df['total_bill'], df['tip'])      # Tips: hóa đơn vs tip
plt.scatter(df['weight'], df['mpg'])          # MPG: trọng lượng vs tiêu hao

# Thêm đường xu hướng:
z = np.polyfit(df['horsepower'], df['mpg'], 1)  # ⚠️ SỬA 2 BIẾN NÀY
p = np.poly1d(z)
plt.plot(df['horsepower'], p(df['horsepower']), "r--")
```

### 🎯 PATTERN THƯỜNG GẶP TRONG ĐỀ:

#### Pattern 1: "Top N cái gì đó"
```python
# Template:
top_n = df.groupby('COT_NHOM')['COT_SO'].sum().sort_values(ascending=False).head(N)

# Ví dụ:
top_10_names = df.groupby('Name')['Count'].sum().sort_values(ascending=False).head(10)
top_5_tips = df.groupby('day')['tip'].sum().sort_values(ascending=False).head(5)
```

#### Pattern 2: "So sánh A với B" 
```python
# Template:
comparison = df.groupby('COT_PHAN_LOAI')['COT_SO'].agg(['mean', 'sum', 'count'])

# Ví dụ:
gender_comparison = df.groupby('sex')['tip'].agg(['mean', 'sum', 'count'])
origin_comparison = df.groupby('origin')['mpg'].agg(['mean', 'count'])
```

#### Pattern 3: "Xu hướng theo thời gian"
```python
# Template:
trend = df.groupby('COT_THOI_GIAN')['COT_SO'].mean()
plt.plot(trend.index, trend.values)

# Ví dụ:
mpg_trend = df.groupby('model_year')['mpg'].mean()
plt.plot(mpg_trend.index, mpg_trend.values)
```

### 🎯 CÂU LỆNH 1 DÒNG HAY DÙNG:
```python
# Đếm tần số
df['column'].value_counts()

# Tỷ lệ phần trăm  
df['column'].value_counts(normalize=True) * 100

# Thống kê mô tả nhanh
df['column'].describe()

# Tương quan nhanh
df[['col1', 'col2', 'col3']].corr()

# Lọc và đếm
df[df['condition']]['column'].count()

# Top 5 nhanh
df.groupby('group')['value'].sum().nlargest(5)
```

---

*Tài liệu được tổng hợp từ bài tập Tips, MPG, US Baby Names, Pandas và Matplotlib. Chúc bạn thi tốt! 🎯*

---

## 🔥 TEMPLATES HOÀN CHỈNH - COPY TOÀN BỘ 🔥

### 🚨 TEMPLATE PHÂN TÍCH TỔNG QUÁT ✨ COPY HẾT

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ⭐ THAY TÊN FILE
df = pd.read_csv('TÊN_FILE.csv')

print("=== THÔNG TIN CƠ BẢN ===")
print(f"Kích thước: {df.shape}")
print(f"Các cột: {df.columns.tolist()}")
print(f"Dữ liệu thiếu:\n{df.isnull().sum()}")

# Xử lý dữ liệu
if 'Unnamed: 0' in df.columns:
    df = df.drop('Unnamed: 0', axis=1)
df = df.dropna()

print("\n=== THỐNG KÊ MÔ TẢ ===")
numeric_cols = df.select_dtypes(include=[np.number]).columns
categorical_cols = df.select_dtypes(include=['object']).columns

for col in numeric_cols:
    print(f"{col}: TB={df[col].mean():.2f}, TV={df[col].median():.2f}")

for col in categorical_cols:
    print(f"{col}: {df[col].value_counts().head(3).to_dict()}")

# Trực quan hóa
df[numeric_cols].hist(figsize=(15, 10), bins=20)
plt.suptitle('Histogram các cột số')
plt.tight_layout()
plt.show()

if len(numeric_cols) > 1:
    plt.figure(figsize=(10, 8))
    sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm')
    plt.title('Ma trận tương quan')
    plt.show()

print("=== HOÀN THÀNH ===")
```

### 🚨 TEMPLATE PHÂN PHỐI XÁC SUẤT ✨ THAY SỐ

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson, norm

print("=== PHÂN PHỐI NHỊ THỨC ===")
n, p = 10, 0.3  # ⭐ THAY SỐ

for k in [0, 1, 2, 5]:  # ⭐ THAY CÁC GIÁ TRỊ K
    prob = binom.pmf(k, n, p)
    print(f"P(X = {k}) = {prob:.6f}")

x = range(n+1)
probs = [binom.pmf(i, n, p) for i in x]
plt.figure(figsize=(10, 6))
plt.bar(x, probs, alpha=0.7)
plt.title(f'Phân phối nhị thức B({n}, {p})')
plt.show()

print("\n=== PHÂN PHỐI POISSON ===")
lam = 3  # ⭐ THAY LAMBDA

for k in [0, 1, 2, 5]:  # ⭐ THAY CÁC GIÁ TRỊ K
    prob = poisson.pmf(k, lam)
    print(f"P(X = {k}) = {prob:.6f}")

x = range(15)
probs = [poisson.pmf(i, lam) for i in x]
plt.figure(figsize=(10, 6))
plt.bar(x, probs, alpha=0.7, color='orange')
plt.title(f'Phân phối Poisson(λ={lam})')
plt.show()

print("\n=== PHÂN PHỐI CHUẨN ===")
mu, sigma = 100, 15  # ⭐ THAY MU, SIGMA

values = [90, 110, 120]  # ⭐ THAY CÁC GIÁ TRỊ CẦN TÍNH
for val in values:
    prob = norm.cdf(val, mu, sigma)
    print(f"P(X < {val}) = {prob:.6f}")

x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = norm.pdf(x, mu, sigma)
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2)
plt.title(f'Phân phối chuẩn N({mu}, {sigma}²)')
plt.show()

print("=== HOÀN THÀNH ===")
```

### 🚨 TEMPLATE TIPS ANALYSIS ✨ THAY TÊN CỘT

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ⭐ ĐỌC FILE
df = pd.read_csv('tips.csv')  # ⭐ THAY TÊN FILE
if 'Unnamed: 0' in df.columns:
    df = df.drop('Unnamed: 0', axis=1)

print("=== THÔNG TIN DỮ LIỆU ===")
print(f"Kích thước: {df.shape}")
print(df.head())

# ⭐ TẠO BIẾN PHỤ TRỢ (nếu cần)
df['tip_percentage'] = (df['tip'] / df['total_bill']) * 100

print("\n=== THỐNG KÊ CƠ BẢN ===")
print(f"Trung bình tip: ${df['tip'].mean():.2f}")  # ⭐ THAY CỘT
print(f"Tỷ lệ tip: {df['tip_percentage'].mean():.1f}%")

# ⭐ THỐNG KÊ THEO NHÓM
print("\n=== THEO GIỚI TÍNH ===")
gender_stats = df.groupby('sex').agg({  # ⭐ THAY CỘT NHÓM
    'tip': ['mean', 'count'],           # ⭐ THAY CỘT GIÁ TRỊ
    'total_bill': 'mean'
}).round(2)
print(gender_stats)

print("\n=== THEO NGÀY ===")
day_stats = df.groupby('day').agg({     # ⭐ THAY CỘT NHÓM
    'tip': ['sum', 'mean', 'count']     # ⭐ THAY CỘT GIÁ TRỊ
}).round(2)
print(day_stats)

# ⭐ BIỂU ĐỒ
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Histogram
axes[0, 0].hist(df['total_bill'], bins=20)  # ⭐ THAY CỘT
axes[0, 0].set_title('Histogram - Total Bill')

# Scatter
axes[0, 1].scatter(df['total_bill'], df['tip'])  # ⭐ THAY 2 CỘT
axes[0, 1].set_title('Tip vs Total Bill')

# Bar charts
df.groupby('day')['tip'].sum().plot(kind='bar', ax=axes[1, 0])  # ⭐ THAY
axes[1, 0].set_title('Tips by Day')

df.groupby('time')['tip'].sum().plot(kind='bar', ax=axes[1, 1])  # ⭐ THAY
axes[1, 1].set_title('Tips by Time')

plt.tight_layout()
plt.show()

print("=== HOÀN THÀNH ===")
```

---

## 🚨 CHECKLIST THI CỰC QUAN TRỌNG

### ✅ TRƯỚC KHI BẮT ĐẦU (2 PHÚT ĐẦU):
1. **Copy toàn bộ import** vào cell đầu tiên
2. **Ctrl+F tìm keyword** trong đề bài  
3. **Kiểm tra tên file** có đúng không?
4. **Print df.columns** để biết tên cột chính xác

### ✅ KHI LÀM BÀI (TỪNG CELL):
1. **Copy template** phù hợp từ cheat sheet
2. **Thay tên file/cột** theo đề bài
3. **Chạy ngay** để kiểm tra
4. **Sửa lỗi** nếu có trước khi làm tiếp

### ✅ KEYWORDS SIÊU QUAN TRỌNG:

| **THẤY TRONG ĐỀ** | **SEARCH** | **ACTION** |
|-------------------|------------|------------|
| "đọc dữ liệu" | `A01` | Copy A01, thay tên file |
| "bao nhiêu dòng" | `A02` | Copy A02, chạy luôn |
| "trung bình" | `C01` | Copy C01, thay tên cột |
| "tỷ lệ %" | `B03` | Copy B03, thay tên cột |
| "biểu đồ cột" | `D01` | Copy D01, thay tên cột |
| "histogram" | `D03` | Copy D03, thay tên cột |
| "boxplot" | `D04` hoặc `D05` | Copy template, thay cột |
| "so sánh nhóm" | `B04` | Copy B04, thay 2 tên cột |
| "tương quan" | `D07` | Copy D07, thay 2 tên cột |
| "xác suất" | `E01/E02/E03` | Copy template, thay số |

### 💡 CHIẾN THUẬT 20 PHÚT CUỐI:
1. **Ưu tiên câu dễ**: Đọc file, thống kê cơ bản
2. **Copy paste nhanh**: Đừng viết code từ đầu
3. **Thay tên nhanh**: Ctrl+H để replace all
4. **Comment đơn giản**: "Phân phối lệch phải", "Tương quan mạnh"

---

## 🎨 BẢNG CHEAT DATASETS THƯỜNG GẶP

| **Dataset** | **File** | **Cột Số** | **Cột Phân Loại** | **Ví dụ Groupby** |
|-------------|----------|-------------|-------------------|-------------------|
| **Tips** | `tips.csv` | tip, total_bill, size | sex, smoker, day, time | `df.groupby('sex')['tip'].mean()` |
| **MPG** | `mpg.csv` | mpg, horsepower, weight | origin | `df.groupby('origin')['mpg'].mean()` |
| **Baby Names** | `US_Baby_Names.csv` | Count | Name, Gender | `df.groupby('Gender')['Count'].sum()` |
| **Grades** | `sample_grades.csv` | Final Exam, Mid-Term | Gender, Grade | `df.groupby('Grade')['Final Exam'].mean()` |

### 🔥 COPY-PASTE SIÊU NHANH:

```python
# ĐỌC FILE NHANH
df = pd.read_csv('FILENAME.csv')
if 'Unnamed: 0' in df.columns: df = df.drop('Unnamed: 0', axis=1)
print(f"Shape: {df.shape}")
print(df.head())

# THỐNG KÊ NHANH  
print(f"Mean: {df['COLUMN'].mean():.2f}")
print(f"Std: {df['COLUMN'].std():.2f}")
print(df['COLUMN'].value_counts())

# VẼ NHANH
plt.figure(figsize=(10,6))
df['COLUMN'].value_counts().plot(kind='bar')
plt.title('TITLE')
plt.show()

# GROUPBY NHANH
result = df.groupby('GROUP_COL')['VALUE_COL'].agg(['mean','count']).round(2)
print(result)

# CORRELATION NHANH
corr = df['COL1'].corr(df['COL2'])
print(f"Correlation: {corr:.3f}")
```

---

**🍀 CHÚC BẠN THI TỐT! CTRL+F LÀ VŨ KHÍ BÍ MẬT! 🍀**
**🔥 COPY CHEAT SHEET VÀO USB - DÙNG KHI CẦN! 🔥**

---

*LƯU Ý: Tài liệu này được tối ưu cho kỳ thi Giữa kỳ Thống kê máy tính - IUH*