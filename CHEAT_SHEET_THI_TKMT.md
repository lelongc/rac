# 🔥 CHEAT SHEET THI THỐNG KÊ MÔ TẢ - COPY & PASTE

## 🎯 QUY TẮC VÀNG: NHÌN ĐỀ → TÌM MÃ → COPY → THAY TÊN → CHẠY!

---

## 📋 MENU TÌM KIẾM SIÊU TỐC

### 🔍 THẤY TỪ KHÓA GÌ TRONG ĐỀ → CTRL+F TÌM MÃ ĐÓ

| **THẤY TRONG ĐỀ**                | **TÌM MÃ** | **THAY GÌ** |
| -------------------------------- | ---------- | ----------- |
| đọc dữ liệu, hiển thị            | `A01`      | tên file    |
| bao nhiêu dòng, bao nhiêu cột    | `A02`      | không thay  |
| thiếu dữ liệu, missing, null     | `A03`      | không thay  |
| định tính, định lượng, phân loại | `A04`      | không thay  |
| có bao nhiêu, value_counts       | `B01`      | tên cột     |
| nhiều nhất, ít nhất, top         | `B02`      | tên cột     |
| tỷ lệ, %, phần trăm              | `B03`      | tên cột     |
| theo nhóm, groupby, so sánh      | `B04`      | 2 tên cột   |
| trung bình, mean, median         | `C01`      | tên cột     |
| độ lệch chuẩn, std, var          | `C02`      | tên cột     |
| phân vị, quantile, Q1, Q3        | `C03`      | tên cột     |
| biểu đồ cột, bar chart           | `D01`      | tên cột     |
| biểu đồ tròn, pie chart          | `D02`      | tên cột     |
| histogram, phân bố               | `D03`      | tên cột     |
| boxplot, hộp râu                 | `D04`      | tên cột     |
| so sánh boxplot, theo hãng       | `D05`      | 2 tên cột   |
| ma trận tương quan, heatmap      | `D06`      | không thay  |
| xác suất, P(, nhị thức           | `E01`      | n, p, k     |
| Poisson, λ, lambda               | `E02`      | λ, k        |
| chuẩn, normal, mm, đường kính    | `E03`      | μ, σ, x     |
| lấy mẫu, sample                  | `F01`      | số mẫu      |
| mô phỏng, simulation, 100 lần    | `F02`      | số lần      |

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
print("10 dòng đầu:")
print(df.head(10))
```

### A02 - SỐ DÒNG CỘT

```python
print(f"Dữ liệu có {df.shape[0]} dòng và {df.shape[1]} cột")
```

### A03 - THIẾU DỮ LIỆU

```python
print("Số giá trị thiếu:")
print(df.isnull().sum())
print(f"Tổng thiếu: {df.isnull().sum().sum()}")
```

### A04 - PHÂN LOẠI THUỘC TÍNH

```python
print("Thuộc tính định lượng (số):", df.select_dtypes(include=[np.number]).columns.tolist())
print("Thuộc tính định tính (chữ):", df.select_dtypes(include=['object']).columns.tolist())
```

---

### B01 - ĐẾM SỐ LƯỢNG

```python
# ⭐ THAY TÊN CỘT
counts = df['TÊN_CỘT'].value_counts()
print("Số lượng từng loại:")
print(counts)
print(f"Tổng có {df['TÊN_CỘT'].nunique()} loại khác nhau")

# VÍ DỤ: Số phản hồi mỗi hãng
airline_counts = df['airline'].value_counts()
print("Số phản hồi mỗi hãng:")
print(airline_counts)
```

### B02 - TÌM NHIỀU NHẤT/ÍT NHẤT

```python
# ⭐ THAY TÊN CỘT
top = df['TÊN_CỘT'].value_counts().head(1)
print(f"Nhiều nhất: {top.index[0]} ({top.iloc[0]} lần)")

least = df['TÊN_CỘT'].value_counts().tail(1)
print(f"Ít nhất: {least.index[0]} ({least.iloc[0]} lần)")
```

### B03 - TỶ LỆ PHẦN TRĂM

```python
# ⭐ THAY TÊN CỘT
counts = df['TÊN_CỘT'].value_counts()
percentages = (counts / len(df) * 100).round(1)
print("Tỷ lệ %:")
for i, value in enumerate(counts.index):
    print(f"{value}: {counts.iloc[i]} ({percentages.iloc[i]}%)")

# VÍ DỤ: Tỷ lệ mức độ phản hồi
sentiment_counts = df['airline_sentiment'].value_counts()
sentiment_percent = (sentiment_counts / len(df) * 100).round(1)
for sentiment in sentiment_counts.index:
    print(f"{sentiment}: {sentiment_counts[sentiment]} ({sentiment_percent[sentiment]}%)")
```

### B04 - SO SÁNH THEO NHÓM

```python
# ⭐ THAY 2 TÊN CỘT
# Đếm số lượng theo 2 nhóm
crosstab = pd.crosstab(df['CỘT_NHÓM_1'], df['CỘT_NHÓM_2'])
print("Bảng chéo:")
print(crosstab)

# Thống kê số theo nhóm
group_stats = df.groupby('CỘT_NHÓM')['CỘT_GIÁ_TRỊ'].agg(['count', 'mean', 'std']).round(2)
print("Thống kê theo nhóm:")
print(group_stats)

# VÍ DỤ: Phản hồi mỗi mức độ của từng hãng
airline_sentiment = pd.crosstab(df['airline'], df['airline_sentiment'])
print("Số phản hồi mỗi mức độ của từng hãng:")
print(airline_sentiment)
```

---

### C01 - TRUNG BÌNH, TRUNG VỊ

```python
# ⭐ THAY TÊN CỘT
print(f"Trung bình: {df['TÊN_CỘT'].mean():.3f}")
print(f"Trung vị: {df['TÊN_CỘT'].median():.3f}")
print(f"Mode: {df['TÊN_CỘT'].mode().iloc[0] if len(df['TÊN_CỘT'].mode()) > 0 else 'N/A'}")

# Thống kê tổng hợp
print(df['TÊN_CỘT'].describe())

# VÍ DỤ: Độ tin cậy trung bình theo hãng và mức độ
confidence_stats = df.groupby(['airline', 'airline_sentiment'])['airline_sentiment_confidence'].agg(['mean', 'std']).round(3)
print("Độ tin cậy TB và độ lệch chuẩn:")
print(confidence_stats)
```

### C02 - ĐỘ LỆCH CHUẨN, PHƯƠNG SAI

```python
# ⭐ THAY TÊN CỘT
print(f"Độ lệch chuẩn: {df['TÊN_CỘT'].std():.3f}")
print(f"Phương sai: {df['TÊN_CỘT'].var():.3f}")
print(f"Min: {df['TÊN_CỘT'].min():.3f}")
print(f"Max: {df['TÊN_CỘT'].max():.3f}")
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
```

---

### D01 - BIỂU ĐỒ CỘT

```python
# ⭐ THAY TÊN CỘT
plt.figure(figsize=(10, 6))
counts = df['TÊN_CỘT'].value_counts()
counts.plot(kind='bar', color='skyblue')
plt.title('Biểu đồ cột')
plt.xlabel('Danh mục')
plt.ylabel('Số lượng')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# VÍ DỤ: Số phản hồi mỗi hãng
plt.figure(figsize=(10, 6))
airline_counts = df['airline'].value_counts()
airline_counts.plot(kind='bar', color='lightcoral')
plt.title('Số lượng phản hồi của mỗi hãng máy bay')
plt.xlabel('Hãng máy bay')
plt.ylabel('Số phản hồi')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

### D02 - BIỂU ĐỒ TRÒN

```python
# ⭐ THAY TÊN CỘT
plt.figure(figsize=(8, 8))
counts = df['TÊN_CỘT'].value_counts()
plt.pie(counts.values, labels=counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Biểu đồ tròn')
plt.axis('equal')
plt.show()

# VÍ DỤ: Tỷ lệ phản hồi mỗi hãng
plt.figure(figsize=(10, 10))
airline_counts = df['airline'].value_counts()
plt.pie(airline_counts.values, labels=airline_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Số lượng phản hồi của mỗi hãng máy bay')
plt.axis('equal')
plt.show()
```

### D03 - HISTOGRAM

```python
# ⭐ THAY TÊN CỘT
plt.figure(figsize=(10, 6))
plt.hist(df['TÊN_CỘT'], bins=30, color='lightgreen', alpha=0.7, edgecolor='black')
plt.title('Histogram')
plt.xlabel('Giá trị')
plt.ylabel('Tần suất')
plt.grid(axis='y', alpha=0.3)
plt.show()

# VÍ DỤ: Phân bố độ tin cậy
plt.figure(figsize=(10, 6))
plt.hist(df['airline_sentiment_confidence'], bins=30, color='lightblue', alpha=0.7, edgecolor='black')
plt.title('Phân bố độ tin cậy phản hồi')
plt.xlabel('Độ tin cậy')
plt.ylabel('Tần suất')
plt.show()
```

### D04 - BOXPLOT ĐƠN GIẢN

```python
# ⭐ THAY TÊN CỘT
plt.figure(figsize=(8, 6))
plt.boxplot(df['TÊN_CỘT'].dropna())
plt.title('Boxplot')
plt.ylabel('Giá trị')
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

# Cách 2: Seaborn (đẹp hơn)
plt.figure(figsize=(12, 8))
sns.boxplot(data=df, x='CỘT_NHÓM', y='CỘT_GIÁ_TRỊ')
plt.title('Boxplot so sánh theo nhóm')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# VÍ DỤ: Độ tin cậy theo hãng và mức độ phản hồi
plt.figure(figsize=(15, 8))
sns.boxplot(data=df, x='airline', y='airline_sentiment_confidence', hue='airline_sentiment')
plt.title('Độ tin cậy phản hồi theo hãng và mức độ')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
```

### D06 - MA TRẬN TƯƠNG QUAN

```python
# Ma trận tương quan cho các cột số
numeric_cols = df.select_dtypes(include=[np.number]).columns
correlation_matrix = df[numeric_cols].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0,
            square=True, linewidths=0.5)
plt.title('Ma trận tương quan')
plt.tight_layout()
plt.show()

# VÍ DỤ: Tương quan giữa các độ tin cậy
confidence_cols = ['airline_sentiment_confidence', 'negativereason_confidence']
correlation_matrix = df[confidence_cols].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Tương quan giữa các độ tin cậy')
plt.show()
```

---

### E01 - XÁC SUẤT NHỊ THỨC

```python
from scipy.stats import binom

# ⭐ THAY SỐ
n = 50     # Số lần thử
p = 0.3    # Xác suất thành công
k = 15     # Số lần thành công

# Xác suất chính xác P(X = k)
prob_exact = binom.pmf(k, n, p)
print(f"P(X = {k}) = {prob_exact:.6f}")

# Xác suất P(X ≤ k)
prob_less_equal = binom.cdf(k, n, p)
print(f"P(X ≤ {k}) = {prob_less_equal:.6f}")

# Xác suất P(X ≥ k)
prob_greater_equal = 1 - binom.cdf(k-1, n, p)
print(f"P(X ≥ {k}) = {prob_greater_equal:.6f}")

# Kỳ vọng và phương sai
print(f"E(X) = {n * p}")
print(f"Var(X) = {n * p * (1-p)}")
```

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
```

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

# Công thức chung cho bất kỳ giá trị nào
x1 = 19.9  # ⭐ THAY
x2 = 20.3  # ⭐ THAY
prob_between = norm.cdf(x2, mu, sigma) - norm.cdf(x1, mu, sigma)
print(f"P({x1} < X < {x2}) = {prob_between:.6f}")
```

---

### F01 - LẤY MẪU

```python
# ⭐ THAY SỐ MẪU
sample_size = 100
sample_df = df.sample(n=sample_size, random_state=42)

print(f"Mẫu gốc: {len(df)} dòng")
print(f"Mẫu lấy: {len(sample_df)} dòng")

# So sánh tỷ lệ
original_ratio = (df['CỘT_NHÓM'] == 'GIÁ_TRỊ').mean()
sample_ratio = (sample_df['CỘT_NHÓM'] == 'GIÁ_TRỊ').mean()
print(f"Tỷ lệ gốc: {original_ratio:.3f}")
print(f"Tỷ lệ mẫu: {sample_ratio:.3f}")
print(f"Sai số: {abs(sample_ratio - original_ratio):.3f}")
```

### F02 - MÔ PHỎNG

```python
# ⭐ THAY SỐ LẦN VÀ SỐ MẪU
n_simulations = 100
sample_size = 50
results = []

for i in range(n_simulations):
    sample = df.sample(n=sample_size)
    # Tính tỷ lệ hoặc trung bình tùy đề
    result = (sample['CỘT_NHÓM'] == 'GIÁ_TRỊ').mean()  # ⭐ THAY
    results.append(result)

# Thống kê kết quả mô phỏng
print(f"Trung bình {n_simulations} lần mô phỏng: {np.mean(results):.3f}")
print(f"Độ lệch chuẩn: {np.std(results):.3f}")

# Vẽ histogram
plt.figure(figsize=(10, 6))
plt.hist(results, bins=20, alpha=0.7, edgecolor='black')
plt.title(f'Histogram {n_simulations} lần mô phỏng (n={sample_size})')
plt.xlabel('Kết quả mẫu')
plt.ylabel('Tần suất')
plt.axvline(np.mean(results), color='red', linestyle='--', label=f'TB: {np.mean(results):.3f}')
plt.legend()
plt.show()
```

---

## 🎯 TEMPLATE HOÀN CHỈNH CHO ĐỀ MẪU

### Đề: Phản hồi hành khách hãng bay

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# 1. Đọc dữ liệu và hiển thị 10 dòng đầu
df = pd.read_csv('TwitterUSAirlineSentiment.csv')
print("10 dòng đầu:")
print(df.head(10))

# 2a. Số lượng phản hồi mỗi hãng và mỗi mức độ
print("\nSố phản hồi mỗi hãng:")
airline_counts = df['airline'].value_counts()
print(airline_counts)

print("\nSố phản hồi mỗi mức độ của từng hãng:")
airline_sentiment = pd.crosstab(df['airline'], df['airline_sentiment'])
print(airline_sentiment)

# 2b. Thống kê độ tin cậy theo hãng và mức độ
print("\nThống kê độ tin cậy:")
confidence_stats = df.groupby(['airline', 'airline_sentiment']).agg({
    'airline_sentiment_confidence': ['mean', 'std'],
    'negativereason_confidence': ['mean', 'std']
}).round(3)
print(confidence_stats)

# Múi giờ mode (xu hướng tập trung)
print("\nMúi giờ phổ biến nhất:")
timezone_mode = df['user_timezone'].mode()
print(timezone_mode.iloc[0] if len(timezone_mode) > 0 else "N/A")

# 3a. Biểu đồ tròn số phản hồi mỗi hãng
plt.figure(figsize=(10, 10))
airline_counts = df['airline'].value_counts()
plt.pie(airline_counts.values, labels=airline_counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Số lượng phản hồi của mỗi hãng máy bay')
plt.axis('equal')
plt.show()

# 3b. Boxplot độ tin cậy theo hãng và mức độ
plt.figure(figsize=(15, 8))
sns.boxplot(data=df, x='airline', y='airline_sentiment_confidence', hue='airline_sentiment')
plt.title('Độ tin cậy phản hồi theo hãng máy bay và mức độ phản hồi')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 3c. Ma trận tương quan
numeric_cols = df.select_dtypes(include=[np.number]).columns
correlation_matrix = df[numeric_cols].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, square=True)
plt.title('Ma trận tương quan các thuộc tính số')
plt.tight_layout()
plt.show()

# 4. Xác suất phân phối chuẩn (đường kính chi tiết máy)
from scipy.stats import norm
mu = 20      # mm
sigma = 0.2  # mm

# a. P(X < 20.3)
prob_a = norm.cdf(20.3, mu, sigma)
print(f"\n4a. P(X < 20.3) = {prob_a:.6f}")

# b. P(19.9 < X < 20.3)
prob_b = norm.cdf(20.3, mu, sigma) - norm.cdf(19.9, mu, sigma)
print(f"4b. P(19.9 < X < 20.3) = {prob_b:.6f}")

# c. P(|X - 20| ≤ 0.3) = P(19.7 < X < 20.3)
prob_c = norm.cdf(20.3, mu, sigma) - norm.cdf(19.7, mu, sigma)
print(f"4c. P(|X - 20| ≤ 0.3) = {prob_c:.6f}")
```

---

## 🚨 LƯU Ý KHI THI

### ✅ CHECKLIST TRƯỚC KHI NỘP:

1. **Kiểm tra tên file**: `df = pd.read_csv('TÊN_ĐÚNG.csv')`
2. **Kiểm tra tên cột**: `print(df.columns)` trước khi thay
3. **Import đủ thư viện**: pandas, numpy, matplotlib, seaborn, scipy
4. **Thay đúng số liệu**: μ, σ, n, p, k theo đề
5. **Chạy từng cell**: Đừng chạy tất cả cùng lúc

### 🔧 SỬA LỖI NHANH:

- `KeyError`: Sai tên cột → `print(df.columns)`
- `FileNotFoundError`: Sai tên file → Kiểm tra tên file
- `AttributeError`: Sai kiểu dữ liệu → `print(df.dtypes)`

### 📝 CÁCH SỬ DỤNG:

1. **Đọc đề** → Tìm từ khóa
2. **Ctrl+F** tìm mã trong file này
3. **Copy code** → Thay tên file/cột/số
4. **Chạy** → Hoàn thành

**🍀 CHÚC BẠN THI TỐT! 🍀**
