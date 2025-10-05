# 🔥 CHEAT SHEET THỐNG KÊ MÔ TẢ - TỔNG HỢP TOÀN TẬP

## 🎯 QUY TẮC VÀNG: NHÌN ĐỀ → TÌM MÃ → COPY → THAY TÊN → CHẠY!

---

## 📚 IMPORT TOÀN BỘ THỨ VIỆN CẦN THIẾT

```python
# Import cơ bản
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Import phân phối xác suất
from scipy.stats import binom, poisson, norm, t

# Thiết lập hiển thị
plt.style.use("ggplot")
plt.rcParams['figure.figsize'] = (10, 6)
```

---

## 📋 MENU TÌM KIẾM SIÊU TỐC

### 🔍 THẤY TỪ KHÓA GÌ TRONG ĐỀ → CTRL+F TÌM MÃ ĐÓ

| **THẤY TRONG ĐỀ**                | **TÌM MÃ** | **THAY GÌ**   |
| ----------------------------------------- | ------------------ | -------------------- |
| đọc dữ liệu, hiển thị               | `A01`            | tên file            |
| bao nhiêu dòng, bao nhiêu cột         | `A02`            | không thay          |
| thiếu dữ liệu, missing, null           | `A03`            | không thay          |
| định tính, định lượng, phân loại | `A04`            | không thay          |
| có bao nhiêu, value_counts              | `B01`            | tên cột            |
| nhiều nhất, ít nhất, top              | `B02`            | tên cột            |
| tỷ lệ, %, phần trăm , sự khác biệt | `B03`            | tên cột            |
| theo nhóm, groupby, so sánh             | `B04`            | 2 tên cột          |
| trung bình, mean, median                 | `C01`            | tên cột            |
| độ lệch chuẩn, std, var               | `C02`            | tên cột            |
| phân vị, quantile, Q1, Q3               | `C03`            | tên cột            |
| biểu đồ cột, bar chart                | `D01`            | tên cột            |
| biểu đồ tròn, pie chart               | `D02`            | tên cột            |
| histogram, phân bố                      | `D03`            | tên cột            |
| boxplot, hộp râu                        | `D04`            | tên cột            |
| so sánh boxplot, theo hãng              | `D05`            | 2 tên cột          |
| ma trận tương quan, heatmap            | `D06`            | không thay          |
| scatter plot, tương quan                | `D07`            | 2 tên cột          |
| xác suất, P(, nhị thức                | `E01`            | n, p, k              |
| Poisson, λ, lambda                       | `E02`            | λ, k                |
| chuẩn, normal, mm, đường kính        | `E03`            | μ, σ, x            |
| lấy mẫu, sample                         | `F01`            | số mẫu             |
| mô phỏng, simulation, 100 lần          | `F02`            | số lần             |
| đổi đơn vị, inches, pounds           | `G01`            | công thức          |
| BMI, kg/m², béo phì                    | `G02`            | height, weight       |
| datetime, thời gian, tháng              | `G03`            | cột time            |
| histogram nhiều cột                     | `H01`            | danh sách cột      |
| subplot, nhiều biểu đồ                | `H02`            | số dòng, cột      |
| phân nhóm theo ngưỡng                 | `H03`            | ngưỡng phân nhóm |

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
print("Dữ liệu ngẫu nhiên:")
print(df.sample(5))
```

### A02 - SỐ DÒNG CỘT + THÔNG TIN CƠ BẢN

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

### A03 - THIẾU DỮ LIỆU

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
df['CỘT'] = df['CỘT'].fillna('Unknown')  # Cho cột text
df = df.fillna(0)  # Điền 0 cho tất cả
```

### A04 - PHÂN LOẠI THUỘC TÍNH

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

### B01 - ĐẾM SỐ LƯỢNG

```python
# ⭐ THAY TÊN CỘT
counts = df['TÊN_CỘT'].value_counts()
print("Số lượng từng loại:")
print(counts)
print(f"Tổng có {df['TÊN_CỘT'].nunique()} loại khác nhau")

# Thống kê nâng cao
print("\nBảng phân phối tần số:")
freq_table = df['TÊN_CỘT'].value_counts().sort_index()
print(freq_table)
```

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

# Top 10
print("Top 10 giá trị:")
top_10 = df['TÊN_CỘT'].value_counts().head(10)
print(top_10)
```

### B03 - TỶ LỆ PHẦN TRĂM

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



# lọc rồi tính tổng rồi tính phần trăm giá trị nào đó trong cột

## Lọc những người có tập thể thao (exerany == 1)
exercisers = df[df['exerany'] == 1]

## Tính tỷ lệ người có sức khỏe 'poor' trong nhóm này
count_poor = (exercisers['genhlth'] == 'poor').sum()
total = len(exercisers)
percent_poor = count_poor / total * 100

print(f"Tỷ lệ người có sức khỏe 'poor' trong nhóm tập thể thao: {percent_poor:.1f}%")


# Người muốn giảm cân là người có cân nặng mong muốn nhỏ hơn cân nặng hiện tại
want_lose = (df['wtdesire'] < df['weight']).sum()
total = len(df)

percent_lose = want_lose / total * 100

print(f"Tỷ lệ người muốn giảm cân: {percent_lose:.1f}%")

# Tính tỉ lệ phần trăm người tham gia khảo sát hiện đang hút thuốc lá.Liệu có "sự khác biệt" đáng kể về tỉ lệ này giữa các nhóm tuổi khác nhau
không?
smoking_rate = data[data['smoke100'] > 0].shape[0] / data.shape[0]
print("Tỷ lệ hút thuốc:", smoking_rate)

# 2️⃣ Tạo biến phân loại người hút thuốc
df['smoker'] = df['smoke100'] > 0
# 3️⃣ Gom nhóm theo độ tuổi để xem sự khác biệt
# Có thể chia nhóm tuổi thành các khoảng dễ hiểu
bins = [18, 30, 45, 60, 75, 90]
labels = ['18–29', '30–44', '45–59', '60–74', '75+']
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)

# 4️⃣ Tính tỷ lệ hút thuốc theo nhóm tuổi
crosstab_percent = pd.crosstab(df['age_group'], df['smoker'], normalize='index') * 100
print("\nTỷ lệ % hút thuốc theo nhóm tuổi:")
print(crosstab_percent.round(1))


from scipy.stats import chi2_contingency
contingency_table = pd.crosstab(age_groups, data_cleaned['smoke100'] > 0)
# Thực hiện kiểm định Chi-Square
chi2, p, dof, expected = chi2_contingency(contingency_table)
print("Kiểm định Chi-Square")
print(f"Chi2 statistic: {chi2}, p-value: {p}")
if p < 0.05:
print("Có sự khác biệt đáng kể về tỷ lệ hút thuốc giữa các nhóm tuổi.")
else:
print("Không có sự khác biệt đáng kể về tỷ lệ hút thuốc giữa các nhóm tuổi.")
```

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

# Group by cơ bản
grouped = df.groupby('CỘT_NHÓM')['CỘT_GIÁ_TRỊ'].agg(['count', 'mean', 'std']).round(2)
print("Thống kê theo nhóm:")
print(grouped)
```

---

### C01 - TRUNG BÌNH, TRUNG VỊ

```python
# ⭐ THAY TÊN CỘT
print(f"Trung bình: {df['TÊN_CỘT'].mean():.3f}")
print(f"Trung vị: {df['TÊN_CỘT'].median():.3f}")
print(f"Mode: {df['TÊN_CỘT'].mode().iloc[0] if len(df['TÊN_CỘT'].mode()) > 0 else 'N/A'}")

# Thống kê tổng hợp
print("\nThống kê tổng hợp:")
print(df['TÊN_CỘT'].describe())

age_stats = data['age'].describe()
print("Tuổi trung bình:", age_stats['mean'])
print("Độ lệch chuẩn:", age_stats['std'])
print("Phân vị 25%:", age_stats['25%'])
print("Phân vị 50%:", age_stats['50%'])
print("Phân vị 75%:", age_stats['75%'])

# Theo nhóm
group_stats = df.groupby('CỘT_NHÓM')['CỘT_GIÁ_TRỊ'].agg(['mean', 'median', 'std', 'count']).round(2)
print("Thống kê theo nhóm:")
print(group_stats)
```

### C02 - ĐỘ LỆCH CHUẨN, PHƯƠNG SAI

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
```

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

# Miền giá trị và miền phân vị
print(f"Miền giá trị: [{df['TÊN_CỘT'].min():.1f}, {df['TÊN_CỘT'].max():.1f}]")
print(f"Miền phân vị (Q1, Q3): [{q1:.1f}, {q3:.1f}]")
```

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

# Bar chart với seaborn
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='TÊN_CỘT', palette='viridis')
plt.title('Biểu đồ cột với Seaborn')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

### D02 - BIỂU ĐỒ TRÒN

```python
# ⭐ THAY TÊN CỘT
plt.figure(figsize=(10, 8))
counts = df['TÊN_CỘT'].value_counts()
plt.pie(counts.values, labels=counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Biểu đồ tròn - TÊN_CỘT')
plt.axis('equal')
plt.tight_layout()
plt.show()

# Pie chart với explode
plt.figure(figsize=(10, 8))
explode = [0.05] * len(counts)  # Tách nhỏ các phần
plt.pie(counts.values, labels=counts.index, autopct='%1.1f%%',
        explode=explode, startangle=90, shadow=True)
plt.title('Biểu đồ tròn có hiệu ứng')
plt.axis('equal')
plt.show()
```

### D03 - HISTOGRAM

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

# Histogram nhiều cột cùng lúc
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
cols = ['CỘT_1', 'CỘT_2', 'CỘT_3']
for i, col in enumerate(cols):
    axes[i].hist(df[col].dropna(), bins=20, alpha=0.7)
    axes[i].set_title(f'Histogram {col}')
    axes[i].set_xlabel(col)
plt.tight_layout()
plt.show()
```

### D04 - BOXPLOT ĐƠN GIẢN

```python
# ⭐ THAY TÊN CỘT
plt.figure(figsize=(8, 6))
plt.boxplot(df['TÊN_CỘT'].dropna())
plt.title('Boxplot - TÊN_CỘT')
plt.ylabel('Giá trị')
plt.show()

# Nhiều cột cùng lúc với pandas
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
cols = ['CỘT_1', 'CỘT_2', 'CỘT_3']
for i, col in enumerate(cols):
    axes[i].boxplot(df[col].dropna())
    axes[i].set_title(f'Boxplot {col}')
    axes[i].set_ylabel(col)
plt.tight_layout()
plt.show()

# Boxplot với pandas
df[['CỘT_1', 'CỘT_2', 'CỘT_3']].boxplot(figsize=(10, 6))
plt.title('Boxplot nhiều cột')
plt.show()
```

### D05 - BOXPLOT SO SÁNH NHÓM

```python
# ⭐ THAY 2 TÊN CỘT
plt.figure(figsize=(12, 8))

# Cách 1: Pandas
df.boxplot(column='CỘT_GIÁ_TRỊ', by='CỘT_NHÓM', figsize=(12, 8))
plt.title('Boxplot so sánh theo nhóm')
plt.suptitle('')  # Xóa title mặc định
plt.show()

# Vẽ boxplot so sánh cân nặng giữa nhóm có và không tập thể dục
df.boxplot(column='weight', by='exerany', figsize=(12, 8))
# Cách 2: Seaborn (đẹp hơn)
plt.figure(figsize=(12, 8))
sns.boxplot(data=df, x='CỘT_NHÓM', y='CỘT_GIÁ_TRỊ')
plt.title('Boxplot so sánh theo nhóm')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Boxplot theo nhiều nhóm
plt.figure(figsize=(12, 8))
sns.boxplot(data=df, x='CỘT_NHÓM_1', y='CỘT_GIÁ_TRỊ', hue='CỘT_NHÓM_2')
plt.title('Boxplot so sánh theo 2 nhóm')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

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

# In ma trận tương quan
print("Ma trận tương quan:")
print(correlation_matrix.round(3))

# Tìm tương quan cao nhất
high_corr = correlation_matrix.abs().unstack().sort_values(ascending=False)
high_corr = high_corr[high_corr < 1]  # Bỏ tương quan với chính nó
print(f"\nTương quan cao nhất: {high_corr.head(5)}")
```

### D07 - SCATTER PLOT

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

# Scatter plot với seaborn
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='CỘT_X', y='CỘT_Y', hue='CỘT_NHÓM')
plt.title('Scatter plot theo nhóm')
plt.show()
```

---

### E01 - XÁC SUẤT NHỊ THỨC

```python
from scipy.stats import binom

# ⭐ THAY SỐ
n = 10     # Số lần thử
p = 0.4    # Xác suất thành công

# Tạo phân phối
binomial_dist = binom(n, p)

# a. P(X = k)
k = 4
prob_k = binomial_dist.pmf(k)
print(f"P(X = {k}) = {prob_k:.6f}")

# b. P(X <= k)
prob_leq = binomial_dist.cdf(k)
print(f"P(X <= {k}) = {prob_leq:.6f}")

# c. P(X > k)
prob_gt = 1 - binomial_dist.cdf(k)
print(f"P(X > {k}) = {prob_gt:.6f}")

# d. E(X) và Var(X)
print(f"E(X) = {binomial_dist.mean()}")
print(f"Var(X) = {binomial_dist.var()}")

# e. Vẽ đồ thị PMF
x_values = range(0, n+1)
probs = [binomial_dist.pmf(x) for x in x_values]
plt.figure(figsize=(10, 6))
plt.bar(x_values, probs, alpha=0.7, color='lightblue')
plt.title('Phân phối xác suất nhị thức')
plt.xlabel('Số lần thành công')
plt.ylabel('P(X = k)')
plt.show()

# f. Vẽ đồ thị CDF
cdf_values = [binomial_dist.cdf(x) for x in x_values]
plt.figure(figsize=(10, 6))
plt.plot(x_values, cdf_values, 'bo-', markersize=8)
plt.title('Hàm phân phối tích lũy')
plt.xlabel('k')
plt.ylabel('P(X ≤ k)')
plt.grid(True)
plt.show()
```

### E02 - XÁC SUẤT POISSON

```python
from scipy.stats import poisson

# ⭐ THAY SỐ
lam = 3    # Lambda (trung bình)

# Tạo phân phối
poisson_dist = poisson(lam)

# a. P(X = k)
k = 2
prob_k = poisson_dist.pmf(k)
print(f"P(X = {k}) = {prob_k:.6f}")

# b. P(X <= k)
prob_leq = poisson_dist.cdf(k)
print(f"P(X <= {k}) = {prob_leq:.6f}")

# c. P(X > k)
prob_gt = 1 - poisson_dist.cdf(k)
print(f"P(X > {k}) = {prob_gt:.6f}")

# d. E(X) và Var(X)
print(f"E(X) = {poisson_dist.mean()}")
print(f"Var(X) = {poisson_dist.var()}")

# e. Vẽ đồ thị PMF
x_values = range(0, lam*3+1)
probs = [poisson_dist.pmf(x) for x in x_values]
plt.figure(figsize=(10, 6))
plt.bar(x_values, probs, alpha=0.7, color='lightcoral')
plt.title('Phân phối Poisson')
plt.xlabel('k')
plt.ylabel('P(X = k)')
plt.show()

# Ví dụ ứng dụng thời gian
print("\nÁp dụng cho thời gian:")
lam_hour = 10  # 10 sự kiện/giờ
print(f"P(5 sự kiện trong 1h) = {poisson.pmf(5, lam_hour):.6f}")
print(f"P(15 sự kiện trong 2h) = {poisson.pmf(15, lam_hour*2):.6f}")
print(f"P(5 sự kiện trong 30p) = {poisson.pmf(5, lam_hour*0.5):.6f}")
```

### E03 - XÁC SUẤT CHUẨN

```python
from scipy.stats import norm

# ⭐ THAY SỐ
mu = 500     # Trung bình
sigma = 4    # Độ lệch chuẩn

# Tạo phân phối
normal_dist = norm(mu, sigma)

# a. P(X < a)
a = 505
prob_less = normal_dist.cdf(a)
print(f"P(X < {a}) = {prob_less:.6f}")

# b. P(a < X < b)
b = 510
prob_between = normal_dist.cdf(b) - normal_dist.cdf(a)
print(f"P({a} < X < {b}) = {prob_between:.6f}")

# c. P(X > a)
prob_greater = 1 - normal_dist.cdf(a)
print(f"P(X > {a}) = {prob_greater:.6f}")

# d. Tìm giá trị tại phân vị
percentile = 0.95
value_at_percentile = normal_dist.ppf(percentile)
print(f"Giá trị tại phân vị {percentile*100}%: {value_at_percentile:.2f}")

# e. Vẽ đồ thị PDF
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = normal_dist.pdf(x)
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2, label=f'μ={mu}, σ={sigma}')
plt.title('Phân phối chuẩn')
plt.xlabel('Giá trị')
plt.ylabel('Mật độ xác suất')
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()

# f. Phân phối chuẩn tắc
print(f"\nPhân phối chuẩn tắc:")
z = (a - mu) / sigma
print(f"Z-score của {a}: {z:.2f}")
print(f"P(Z < {z:.2f}) = {norm.cdf(z):.6f}")

# Phân phối chuẩn
import matplotlib.pyplot as plt
import seaborn as sns

# Danh sách các cột dạng số cần kiểm tra
cols = ['height', 'weight', 'wtdesire', 'age']

for col in cols:
    plt.figure(figsize=(6,4))
    sns.histplot(df[col].dropna(), kde=True, bins=30)
    plt.title(f'Phân phối của {col}')
    plt.xlabel(col)
    plt.ylabel('Tần suất')
    plt.show()

```

---

### F01 - LẤY MẪU

```python
# ⭐ THAY SỐ MẪU
sample_size = 50
sample_df = df.sample(n=sample_size, random_state=42)

print(f"Mẫu gốc: {len(df)} dòng")
print(f"Mẫu lấy: {len(sample_df)} dòng")

# So sánh thống kê
original_mean = df['CỘT_SỐ'].mean()
sample_mean = sample_df['CỘT_SỐ'].mean()
error = abs(sample_mean - original_mean)

print(f"Trung bình gốc: {original_mean:.3f}")
print(f"Trung bình mẫu: {sample_mean:.3f}")
print(f"Sai số: {error:.3f}")

# Lấy mẫu theo tỷ lệ
sample_percent = df.sample(frac=0.1, random_state=42)  # 10%
print(f"Mẫu 10%: {len(sample_percent)} dòng")
```

### F02 - MÔ PHỎNG

```python
# ⭐ THAY SỐ LẦN VÀ SỐ MẪU
n_simulations = 100
sample_size = 50
results = []

np.random.seed(42)  # Để kết quả ổn định
for i in range(n_simulations):
    sample = df.sample(n=sample_size)
    # Tính thống kê cần thiết (thay đổi tùy đề)
    result = sample['CỘT_SỐ'].mean()  # ⭐ THAY
    results.append(result)

# Thống kê kết quả mô phỏng
print(f"Trung bình {n_simulations} lần mô phỏng: {np.mean(results):.3f}")
print(f"Độ lệch chuẩn: {np.std(results):.3f}")

# Vẽ histogram kết quả
plt.figure(figsize=(10, 6))
plt.hist(results, bins=20, alpha=0.7, edgecolor='black', color='lightblue')
plt.title(f'Histogram {n_simulations} lần mô phỏng (n={sample_size})')
plt.xlabel('Kết quả mẫu')
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
        result = sample['CỘT_SỐ'].mean()
        results_size.append(result)

    axes[i].hist(results_size, bins=15, alpha=0.7)
    axes[i].set_title(f'n={size}, SD={np.std(results_size):.3f}')
    axes[i].axvline(np.mean(results_size), color='red', linestyle='--')

plt.tight_layout()
plt.show()
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

print(df[['height_cm', 'weight_kg']].head())

# Fahrenheit sang Celsius
df['temp_celsius'] = (df['temp_fahrenheit'] - 32) * 5/9

# Feet sang mét
df['distance_m'] = df['distance_ft'] * 0.3048

# Gallon sang lít
df['volume_l'] = df['volume_gallon'] * 3.78541

print("Đã hoàn thành chuyển đổi đơn vị!")
```

### G02 - TÍNH BMI VÀ PHÂN LOẠI

```python
# Tính BMI (cần có height_cm và weight_kg)
df['BMI'] = df['weight_kg'] / (df['height_cm'] / 100) ** 2

# Phân loại BMI
def classify_bmi(bmi):
    if pd.isna(bmi):
        return 'Unknown'
    elif bmi < 18.5:
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

# Tỷ lệ phân loại BMI
obesity_stats = df['BMI_category'].value_counts()
obesity_percent = (obesity_stats / len(df) * 100).round(1)
print("\nTỷ lệ phân loại BMI:")
for category in obesity_stats.index:
    print(f"{category}: {obesity_stats[category]} ({obesity_percent[category]}%)")

# Tỷ lệ béo phì theo nhóm tuổi
df['age_group'] = pd.cut(df['age'], bins=[0, 30, 45, 60, 100],
                        labels=['<30', '30-44', '45-59', '60+'])
obesity_by_age = pd.crosstab(df['age_group'], df['BMI_category'], normalize='index') * 100
print("\nTỷ lệ % BMI theo nhóm tuổi:")
print(obesity_by_age.round(1))
```

### G03 - XỬ LÝ DATETIME

```python
# ⭐ THAY TÊN CỘT THỜI GIAN
# Chuyển cột thời gian thành datetime
df['time'] = pd.to_datetime(df['time'])

# Trích xuất thông tin thời gian
df['year'] = df['time'].dt.year
df['month'] = df['time'].dt.month
df['day'] = df['time'].dt.day
df['weekday'] = df['time'].dt.day_name()
df['hour'] = df['time'].dt.hour
df['quarter'] = df['time'].dt.quarter

# Thống kê theo thời gian
monthly_stats = df.groupby('month').size()
print("Số lượng theo tháng:")
print(monthly_stats)

# Vẽ biểu đồ theo thời gian
plt.figure(figsize=(12, 6))
monthly_stats.plot(kind='bar', color='lightblue')
plt.title('Thống kê theo tháng')
plt.xlabel('Tháng')
plt.ylabel('Số lượng')
plt.xticks(rotation=0)
plt.grid(axis='y', alpha=0.3)
plt.show()

# Thống kê theo ngày trong tuần
weekday_stats = df['weekday'].value_counts()
print("\nThống kê theo ngày trong tuần:")
print(weekday_stats)

# Tìm xu hướng theo thời gian
time_trend = df.groupby('time').size().resample('M').sum()
plt.figure(figsize=(12, 6))
time_trend.plot()
plt.title('Xu hướng theo thời gian')
plt.ylabel('Số lượng')
plt.show()
```

---

### H01 - HISTOGRAM NHIỀU CỘT

```python
# ⭐ THAY DANH SÁCH CỘT
columns = ['CỘT_1', 'CỘT_2', 'CỘT_3', 'CỘT_4']

# Cách 1: Subplot
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
axes = axes.flatten()

for i, col in enumerate(columns):
    axes[i].hist(df[col].dropna(), bins=20, alpha=0.7, color=f'C{i}')
    axes[i].set_title(f'Histogram {col}')
    axes[i].set_xlabel(col)
    axes[i].set_ylabel('Tần suất')
    axes[i].grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.show()

# Cách 2: Pandas hist
df[columns].hist(figsize=(15, 10), bins=20)
plt.suptitle('Histogram tất cả các cột', fontsize=16)
plt.tight_layout()
plt.show()

# Cách 3: Chồng histogram
plt.figure(figsize=(12, 6))
for col in columns:
    plt.hist(df[col].dropna(), bins=20, alpha=0.5, label=col)
plt.title('Histogram chồng')
plt.xlabel('Giá trị')
plt.ylabel('Tần suất')
plt.legend()
plt.show()

print("Nhận xét phân phối:")
for col in columns:
    skew = df[col].skew()
    if skew > 0.5:
        dist_type = "lệch phải"
    elif skew < -0.5:
        dist_type = "lệch trái"
    else:
        dist_type = "gần đối xứng"
    print(f"- {col}: {dist_type} (skewness: {skew:.2f})")
```

### H02 - SUBPLOT NHIỀU BIỂU ĐỒ

```python
# ⭐ THAY SỐ DÒNG, CỘT VÀ LOẠI BIỂU ĐỒ
fig, axes = plt.subplots(2, 3, figsize=(18, 12))

# Histogram
axes[0, 0].hist(df['CỘT_SỐ'].dropna(), bins=20, alpha=0.7)
axes[0, 0].set_title('Histogram')

# Boxplot
axes[0, 1].boxplot(df['CỘT_SỐ'].dropna())
axes[0, 1].set_title('Boxplot')

# Scatter plot
axes[0, 2].scatter(df['CỘT_X'], df['CỘT_Y'], alpha=0.6)
axes[0, 2].set_title('Scatter Plot')

# Bar chart
counts = df['CỘT_PHÂN_LOẠI'].value_counts()
axes[1, 0].bar(counts.index, counts.values)
axes[1, 0].set_title('Bar Chart')
axes[1, 0].tick_params(axis='x', rotation=45)

# Line plot
time_data = df.groupby('THỜI_GIAN')['GIÁ_TRỊ'].mean()
axes[1, 1].plot(time_data.index, time_data.values, marker='o')
axes[1, 1].set_title('Line Plot')

# Pie chart
pie_data = df['CỘT_PHÂN_LOẠI'].value_counts()
axes[1, 2].pie(pie_data.values, labels=pie_data.index, autopct='%1.1f%%')
axes[1, 2].set_title('Pie Chart')

plt.tight_layout()
plt.show()
```

### H03 - PHÂN NHÓM THEO NGƯỠNG

```python
# ⭐ THAY NGƯỠNG PHÂN NHÓM
# Phân nhóm theo khoảng giá trị
df['nhom_tuoi'] = pd.cut(df['age'],
                        bins=[0, 25, 35, 50, 100],
                        labels=['Trẻ', 'Trung niên', 'Lớn tuổi', 'Cao tuổi'])

# Phân nhóm theo phân vị
df['nhom_thu_nhap'] = pd.qcut(df['income'],
                             q=4,
                             labels=['Thấp', 'Trung bình', 'Cao', 'Rất cao'])

# Phân nhóm theo điều kiện
def phan_loai_bmi(bmi):
    if bmi < 18.5:
        return 'Gầy'
    elif bmi < 25:
        return 'Bình thường'
    elif bmi < 30:
        return 'Thừa cân'
    else:
        return 'Béo phì'

df['nhom_bmi'] = df['BMI'].apply(phan_loai_bmi)

# Thống kê theo nhóm
print("Thống kê theo nhóm tuổi:")
print(df['nhom_tuoi'].value_counts())

print("\nThống kê theo nhóm thu nhập:")
print(df['nhom_thu_nhap'].value_counts())

# So sánh giữa các nhóm
comparison = df.groupby('nhom_tuoi')['income'].agg(['mean', 'median', 'std']).round(2)
print("\nSo sánh thu nhập theo nhóm tuổi:")
print(comparison)
```

---

## 🎯 TEMPLATE ĐỀ HOÀN CHỈNH

### TEMPLATE 1: PHÂN TÍCH DỮ LIỆU TỔNG QUÁT

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# 1. ĐỌC VÀ KHÁM PHÁ DỮ LIỆU
df = pd.read_csv('TÊN_FILE.csv')

print("=== THÔNG TIN CƠ BẢN ===")
print(f"Kích thước: {df.shape}")
print(f"Các cột: {df.columns.tolist()}")
print(f"Kiểu dữ liệu:\n{df.dtypes}")
print(f"Dữ liệu thiếu:\n{df.isnull().sum()}")

print("\n=== MẪU DỮ LIỆU ===")
print(df.head())
print(df.describe())

# 2. XỬ LÝ DỮ LIỆU
# Xóa cột không cần thiết
if 'Unnamed: 0' in df.columns:
    df = df.drop('Unnamed: 0', axis=1)

# Xử lý dữ liệu thiếu
df = df.dropna()  # hoặc df.fillna()

# 3. PHÂN TÍCH THỐNG KÊ MÔ TẢ
numeric_cols = df.select_dtypes(include=[np.number]).columns
categorical_cols = df.select_dtypes(include=['object']).columns

print("\n=== THỐNG KÊ CÁC CỘT SỐ ===")
for col in numeric_cols:
    print(f"\n{col}:")
    print(f"  Trung bình: {df[col].mean():.2f}")
    print(f"  Trung vị: {df[col].median():.2f}")
    print(f"  Độ lệch chuẩn: {df[col].std():.2f}")
    print(f"  Min-Max: {df[col].min()} - {df[col].max()}")

print("\n=== THỐNG KÊ CÁC CỘT PHÂN LOẠI ===")
for col in categorical_cols:
    print(f"\n{col}:")
    print(df[col].value_counts())

# 4. TRỰC QUAN HÓA
# Histogram cho các cột số
if len(numeric_cols) > 0:
    df[numeric_cols].hist(figsize=(15, 10), bins=20)
    plt.suptitle('Histogram các cột số')
    plt.tight_layout()
    plt.show()

# Bar chart cho các cột phân loại
for col in categorical_cols[:3]:  # Chỉ vẽ 3 cột đầu
    plt.figure(figsize=(10, 6))
    df[col].value_counts().plot(kind='bar')
    plt.title(f'Biểu đồ cột - {col}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Ma trận tương quan
if len(numeric_cols) > 1:
    plt.figure(figsize=(10, 8))
    sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm')
    plt.title('Ma trận tương quan')
    plt.show()

print("\n=== HOÀN THÀNH PHÂN TÍCH ===")
```

### TEMPLATE 2: PHÂN PHỐI XÁC SUẤT

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson, norm

# ===== PHÂN PHỐI NHỊ THỨC =====
print("PHÂN PHỐI NHỊ THỨC")
n, p = 10, 0.3  # Thay số theo đề

# Tính xác suất
for k in [0, 1, 2, 5]:
    prob = binom.pmf(k, n, p)
    print(f"P(X = {k}) = {prob:.6f}")

# Vẽ đồ thị
x = range(n+1)
probs = [binom.pmf(i, n, p) for i in x]
plt.figure(figsize=(10, 6))
plt.bar(x, probs, alpha=0.7)
plt.title(f'Phân phối nhị thức B({n}, {p})')
plt.xlabel('k')
plt.ylabel('P(X = k)')
plt.show()

# ===== PHÂN PHỐI POISSON =====
print("\nPHÂN PHỐI POISSON")
lam = 3  # Thay số theo đề

for k in [0, 1, 2, 5]:
    prob = poisson.pmf(k, lam)
    print(f"P(X = {k}) = {prob:.6f}")

x = range(15)
probs = [poisson.pmf(i, lam) for i in x]
plt.figure(figsize=(10, 6))
plt.bar(x, probs, alpha=0.7, color='orange')
plt.title(f'Phân phối Poisson(λ={lam})')
plt.xlabel('k')
plt.ylabel('P(X = k)')
plt.show()

# ===== PHÂN PHỐI CHUẨN =====
print("\nPHÂN PHỐI CHUẨN")
mu, sigma = 100, 15  # Thay số theo đề

# Tính xác suất
values = [90, 110, 120]
for val in values:
    prob = norm.cdf(val, mu, sigma)
    print(f"P(X < {val}) = {prob:.6f}")

# Vẽ đồ thị
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y = norm.pdf(x, mu, sigma)
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2)
plt.title(f'Phân phối chuẩn N({mu}, {sigma}²)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True, alpha=0.3)
plt.show()

print("\n=== HOÀN THÀNH PHÂN TÍCH XÁC SUẤT ===")
```

### TEMPLATE 3: TIPS DATA ANALYSIS

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu
df = pd.read_csv('tips.csv')
if 'Unnamed: 0' in df.columns:
    df = df.drop('Unnamed: 0', axis=1)

print("=== THÔNG TIN DỮ LIỆU ===")
print(f"Kích thước: {df.shape}")
print(df.head())

# Tính tỷ lệ tip
df['tip_percentage'] = (df['tip'] / df['total_bill']) * 100

print("\n=== THỐNG KÊ CƠ BẢN ===")
print(f"Trung bình tip: ${df['tip'].mean():.2f}")
print(f"Tỷ lệ tip trung bình: {df['tip_percentage'].mean():.1f}%")
print(f"Số khách trung bình: {df['size'].mean():.1f}")

# Thống kê theo giới tính
print("\n=== THEO GIỚI TÍNH ===")
gender_stats = df.groupby('sex').agg({
    'tip': ['mean', 'count'],
    'tip_percentage': 'mean',
    'total_bill': 'mean'
}).round(2)
print(gender_stats)

# Thống kê theo ngày
print("\n=== THEO NGÀY ===")
day_stats = df.groupby('day').agg({
    'tip': ['sum', 'mean', 'count'],
    'total_bill': 'sum'
}).round(2)
print(day_stats)

# Biểu đồ
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Total bill histogram
axes[0, 0].hist(df['total_bill'], bins=20, alpha=0.7)
axes[0, 0].set_title('Histogram - Total Bill')

# Tip vs Total Bill scatter
axes[0, 1].scatter(df['total_bill'], df['tip'], alpha=0.6)
axes[0, 1].set_title('Tip vs Total Bill')
axes[0, 1].set_xlabel('Total Bill')
axes[0, 1].set_ylabel('Tip')

# Tips by day
day_tips = df.groupby('day')['tip'].sum()
axes[1, 0].bar(day_tips.index, day_tips.values)
axes[1, 0].set_title('Total Tips by Day')

# Tips by time
time_tips = df.groupby('time')['tip'].sum()
axes[1, 1].bar(time_tips.index, time_tips.values, color='orange')
axes[1, 1].set_title('Total Tips by Time')

plt.tight_layout()
plt.show()

print("\n=== HOÀN THÀNH PHÂN TÍCH TIPS ===")
```

---

## 🚨 CHECKLIST THI QUAN TRỌNG

### ✅ TRƯỚC KHI BẮT ĐẦU:

1. **Import đầy đủ**: Copy toàn bộ import statements
2. **Đọc kỹ đề**: Gạch chân từ khóa quan trọng
3. **Kiểm tra file**: Tên file có đúng không?
4. **Kiểm tra cột**: `print(df.columns)` để biết tên cột chính xác

### ✅ KHI LÀM BÀI:

1. **Thay tên đúng**: File name, column name, số liệu
2. **Chạy từng cell**: Đừng chạy tất cả cùng lúc
3. **Kiểm tra kết quả**: Có hợp lý không?
4. **Comment kết quả**: Viết nhận xét nếu đề yêu cầu

### ✅ TRƯỚC KHI NỘP:

1. **Kiểm tra tên file notebook**: `stt_hoten_GK.ipynb`
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

- **Ctrl+F** tìm nhanh code cần thiết trong cheat sheet này
- **Thay tên hàng loạt**: Ctrl+H trong VS Code
- **Backup code**: Copy vào file .txt để phòng khi mất
- **Test nhỏ**: Chạy với sample nhỏ trước khi chạy full

---

## 🎨 CÁC LOẠI BIỂU ĐỒ VÀ KHI NÀO DÙNG

| **Loại biểu đồ** | **Khi nào dùng**              | **Code mẫu**                             |
| -------------------------- | ------------------------------------- | ----------------------------------------------- |
| **Histogram**        | Phân bố của 1 biến liên tục     | `plt.hist(df['col'], bins=20)`                |
| **Bar Chart**        | So sánh các nhóm riêng biệt      | `df['col'].value_counts().plot(kind='bar')`   |
| **Pie Chart**        | Tỷ lệ phần trăm các thành phần | `plt.pie(counts.values, labels=counts.index)` |
| **Boxplot**          | Phân bố và outliers                | `plt.boxplot(df['col'])`                      |
| **Scatter Plot**     | Tương quan 2 biến                  | `plt.scatter(df['x'], df['y'])`               |
| **Line Plot**        | Xu hướng theo thời gian            | `plt.plot(df['time'], df['value'])`           |
| **Heatmap**          | Ma trận tương quan                 | `sns.heatmap(df.corr(), annot=True)`          |

---

**🍀 CHÚC BẠN THI TỐT! NHỚ GIỮ BÌNH TĨNH VÀ LÀM TỪNG BƯỚC! 🍀**
**📝 COPY CHEAT SHEET NÀY VÀO USB ĐỂ DÙNG KHI CẦN! 📝**

Giả sử bạn có một túi đựng bóng với tỷ lệ bóng đỏ là p=0.4 và bóng xanh là 1-p=0.6
Lấy ngẫu nhiên 10 bóng từ túi
a) Viết mã python dể tính xác suất để có đúng 4 bóng đỏ
b) Viết mã python để tính xác suất để có đúng 2 bóng xanh
c) Tổng quát gọi X là số bóng xanh lấy được. Vẽ đồ thị thể hiện xác suất các giá trị X có
thể nhận được
d) Tổng quát gọi X là số bóng xanh lấy được. Vẽ đồ thị thể hiện xác suất tích lũy các giá
trị X có thể nhận được




Rất hay 👏 — đây là một **bài toán phân phối nhị thức (Binomial Distribution)** kinh điển trong xác suất.

Ta sẽ giải lần lượt từng phần (a → d) và viết **code Python đầy đủ, rõ ràng** nhé 👇

---

## ⚙️ Giả thiết ban đầu

* Tỷ lệ bóng đỏ: `p_red = 0.4`
* Tỷ lệ bóng xanh: `p_blue = 0.6 = 1 - p_red`
* Số bóng lấy: `n = 10`

---

## ✅ a) Xác suất có đúng 4 bóng đỏ

Sử dụng  **phân phối nhị thức** :

[

P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}

]

Trong Python, ta dùng `scipy.stats.binom.pmf(k, n, p)`

(`pmf` = Probability Mass Function).

```python
from scipy.stats import binom

n = 10
p_red = 0.4
k = 4  # số bóng đỏ cần tìm

P_4_red = binom.pmf(k, n, p_red)
print(f"Xác suất có đúng 4 bóng đỏ: {P_4_red:.4f}")
```

---

## ✅ b) Xác suất có đúng 2 bóng xanh

Tương tự, nhưng xác suất của bóng xanh là `p_blue = 0.6`.

```python
p_blue = 1 - p_red
k = 2  # số bóng xanh cần tìm

P_2_blue = binom.pmf(k, n, p_blue)
print(f"Xác suất có đúng 2 bóng xanh: {P_2_blue:.4f}")
```

---

## ✅ c) Tổng quát — Gọi X là  **số bóng xanh** , vẽ đồ thị xác suất (PMF)

Ta vẽ **phân phối xác suất rời rạc** của X (tức là `P(X = x)` với `x = 0, 1, 2, ..., 10`).

```python
import matplotlib.pyplot as plt

x = range(0, n + 1)
pmf = binom.pmf(x, n, p_blue)

plt.figure(figsize=(8,5))
plt.bar(x, pmf)
plt.title('Phân phối xác suất P(X = x) — Số bóng xanh')
plt.xlabel('Số bóng xanh (X)')
plt.ylabel('Xác suất')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
```

---

## ✅ d) Tổng quát — Vẽ đồ thị **xác suất tích lũy (CDF)** của X

CDF (Cumulative Distribution Function) là:

[

P(X \le x)

]

→ xác suất có  **tối đa x bóng xanh** .

```python
cdf = binom.cdf(x, n, p_blue)

plt.figure(figsize=(8,5))
plt.step(x, cdf, where='mid')
plt.title('Phân phối tích lũy P(X ≤ x) — Số bóng xanh')
plt.xlabel('Số bóng xanh (X)')
plt.ylabel('Xác suất tích lũy')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
```

---

## 📊 Ví dụ kết quả (minh họa):

```
Xác suất có đúng 4 bóng đỏ: 0.2508
Xác suất có đúng 2 bóng xanh: 0.0168
```

* Đồ thị PMF: có dạng **chuông lệch phải** (trung bình ~6 bóng xanh).
* Đồ thị CDF: tăng dần từ 0 → 1.

---

## 💡 Gợi ý mở rộng:

Nếu bạn muốn kiểm tra **giá trị kỳ vọng và phương sai** của X (số bóng xanh):

```python
E_X = n * p_blue
Var_X = n * p_blue * (1 - p_blue)
print(f"Kỳ vọng E[X] = {E_X:.2f}, Phương sai Var[X] = {Var_X:.2f}")
```

---

✅ **Tóm tắt:**

| Mục | Hàm                      | Kết quả                        |
| ---- | ------------------------- | -------------------------------- |
| (a)  | `binom.pmf(4, 10, 0.4)` | P(có đúng 4 bóng đỏ)       |
| (b)  | `binom.pmf(2, 10, 0.6)` | P(có đúng 2 bóng xanh)       |
| (c)  | `binom.pmf(x, 10, 0.6)` | Vẽ phân phối xác suất (PMF) |
| (d)  | `binom.cdf(x, 10, 0.6)` | Vẽ phân phối tích lũy (CDF) |

---

Bạn có muốn mình giúp thêm **biểu đồ PMF & CDF hiển thị cùng trong một hình** (để đưa vào báo cáo) không? Trông sẽ rất đẹp và chuyên nghiệp.
