dựa trên các file kiến thức tôi gửi bạn làm tài liệu mang đi thi giữa kì cho tôi
tài liệu này chỉ cần mang đi thi , đọc đề thi là biết chỗ nào nên dùng mẫu nào trong tài liệu , chỉ cần copy paste là hoàn thành đề thi dễ dàng
Nội dụng thi giữa kì
• Thống kê mô tả (tính toán các độ đo, trực quan hóa dữ liệu)\
• Mô phỏng
• Phân phối xác suất
phía dưới là các câu hỏi ví dụ trong đề thi , ví dụ thôi nha vì chưa biết đề thi ra gì

"

1. Đọc file dữ liệu và hiển thị 5 dòng đầu tiên.
2. Tập dữ liệu có bao nhiêu dòng và bao nhiêu cột? Có bao nhiêu giá trị bị thiếu trong từng cột?
3. Liệt kê danh sách các thuộc tính định tính và định lượng trong tập dữ liệu.
4. Có bao nhiêu loại sản phẩm khác nhau? Sản phẩm nào được mua nhiều nhất?
5. Tỷ lệ nam và nữ trong tập dữ liệu là bao nhiêu? Chọn biểu đồ phù hợp để trực quan hóa.
6. Nhóm khách hàng thuộc độ tuổi nào có mức chi tiêu trung bình cao nhất?
7. Tính các đại lượng thống kê như giá trị trung bình, trung vị, độ lệch chuẩn của mức chi tiêu.
8. Chọn loại đồ thị phù hợp để hiển thị sự phân bố chi tiêu và nhận xét về xu hướng.
9. Biểu đồ hộp so sánh mức chi tiêu theo nhóm tuổi và giới tính
10. Biểu đồ tròn thể hiện tỷ lệ tổng chi tiêu của từng nhóm tuổi

brfss_2000.csv
Hệ thống giám sát rủi ro dựa trên hành vi (The Behavior Risk Factor Surveilance
System - BRFSS) là một cuộc khảo sát qua điện thoại hàng năm với 350.000 người ở Hoa
Kỳ. Như tên gọi của nó, BRFSS được thiết kế để xác định các yếu tố nguy cơ ở người
trưởng thành và báo cáo các xu hướng sức khỏe mớ. Ví dụ, người trả lời được hỏi về chế
độ ăn uống và hoạt động thể chất hàng tuần, tình trạng HIV/AIDS, khả năng sử dụng thuốc
lá và thậm chí cả mức độ chi trả dịch vụ chăm sóc sức khỏe của họ.
Bộ dữ liệu brfss_2000 chứa thông tin khảo sát năm 2000, với hơn 200 thông tin. Trong
bộ dữ liệu này, ta chỉ khảo sát một số thông tin sau:
• genhlth: người khảo sát tự đánh giá sức khỏe (excellent, very good, good, fair
or poor)
• exerany: cho biết có hoạt động thể chất nào trong tháng gần nhất hay không, có
(1), không (0)
• hlthplan: có bảo hiểm (1) hay không (0)
• smoke100: tổng số điếu thuốc đã hút ít nhất
• height: chiều cao (inches)
• weight: cân nặng (pounds)
• wtdesire: cân nặng mong muốn(pounds)
• age: tuổi
• gender: giới tính: nam(m), nữ(f)

Câu 1: Đọc hai bộ dữ liệu trên và cho biết mỗi bộ dữ liệu có kích thước bao nhiêu
dòng, bao nhiêu cột?
2a, Tính tỷ lệ nam nữ
2b, Trong số những người tập thể thao, tỷ lệ những người tự đánh giá có sức khỏe kém
là bao nhiêu?
Câu 3
a, Đổi đơn vị chiều cao từ inches sang centimet, đơn vị cân nặng từ pound sang kg.
b, Tính tỷ lệ những người muốn giảm cân.

Câu 4:
a, Theo bạn trong các thuộc tính trên, thuộc tính nào có phân phối chuẩn. Vẽ hình
minh họa
b, Vẽ đồ thị boxplot so sánh cân nặng của
những người có tập thể dục

Phân bố tuổi tác trong mẫu: Hãy mô tả phân bố tuổi của người tham gia khảo sát.
Tuổi trung bình, độ lệch chuẩn, và các phân vị 25%, 50%, 75% là bao nhiêu?
Câu 6
Tỉ lệ người hút thuốc: Tính tỉ lệ phần trăm người tham gia khảo sát hiện đang hút
thuốc lá. Liệu có sự khác biệt đáng kể về tỉ lệ này giữa các nhóm tuổi khác nhau
không
Câu 7
BMI trung bình theo giới tính: Tính chỉ số BMI trung bình cho nam và nữ trong mẫu.
Câu 8
Phân tích tỉ lệ bệnh béo phì: Sử dụng các tiêu chuẩn của CDC về chỉ số BMI để phân
loại người tham gia vào nhóm béo phì. Tính tỉ lệ béo phì theo giới tính và độ tuổi.

ĐỀ 02 – SỬ DỤNG BẢNG DỮ LIỆU STUDENTSURVERY.CSV
Đề bài: DỮ LIỆU SINH VIÊN
Dữ liệu được cung cấp trong file StudentSurvey.csv được khảo sát. Yêu cầu
Câu 1.
• (1 điểm) Hiển thị 5 dòng dữ liệu
• (1 điểm) Xây dựng bảng phân phối tần số thể hiện số lượng sinh viên mỗi năm, bỏ
qua các dòng bị thiểu dữ liệu năm.
Câu 2. Dựa vào dữ liệu bạn hãy cho biết:
a. (2 điểm) Tỷ lệ sinh viên đeo khuyên?
b. (1 điểm) Giữa sinh viên nam và nữ tỷ lệ đeo khuyên của ai cao hơn?
Câu 3 .
• (1.5 điểm) Vẽ đồ thị histogram của ba thuộc tỉnh nhịp tim (Pulse), số giờ tập thể
thao 3 (Exercise), số khuyên đeo (Piercings).
• (0.5 điểm) Hãy cho biết phân phối của ba thuộc tỉnh trên phân phối nào lệch trái,
lệch phải hoặc đối xứng.
Câu 4. (3 điểm) Sử dụng hảm sample() trên DataFrame. Bạn hãy:
• (1 điểm) Lấy ngẫu nhiên một mẫu tử bộ dữ liệu trên với cỡ mẫu là 50. Tính tỷ lệ nữ
mẫu trên. Tính sai số so với giá trị tỷ lệ tử bộ dữ liệu ban đầu.
• (1 điểm) Hãy thực hiện lại câu trên 100 lần với cùng cỡ mẫu là 50, với mỗi mẫu hãy
tỉnh giả trị tỷ lệ nữ của mẫu và vẽ histogram của 100 giá trị trung bình này
• (1 điểm) Lập lại câu b và thử nghiệm với các cỡ mẫu khác nhau. Bạn có nhận thấy
có gì khác biệt không? Nếu có hãy giải thích

Year Year in school: First Year, Sophomore, Junior, or Senior
Gender Student's gender: F or M
Smoke Smoker? No or Yes
Award Preferred award: Academy, Nobel, or Olympic
HigherSAT Which SAT is higher? Math or Verbal
Exercise Hours of exercise per week
TV Hours of TV viewing per week
Height Height (in inches)
Weight Weight (in pounds)
Siblings Number of siblings
BirthOrder Birth order, 1 oldest, 2 second oldest, etc.
VerbalSAT Verbal SAT score
MathSAT Math SAT score
SAT Combined Verbal + Math SAT
GPA Grade point average
Pulse Pulse rate (beats per asimate)
Piercings Number of body piercings

Đề 03 - file bds.csv
Đề bài: KHẢO SÁT DỮ LIỆU VỀ MUA BÁN BẤT ĐỘNG SẢN NĂM 2020 TẠI VIỆT
NAM
Dữ liệu được cung cấp trong file bds.csv được thu thập năm 2020 tại Việt Nam.
title poster_temp area_temp final_price type acreage
Bán nhà tại p.Phạm Ngũ Lão, Quận
1, 25m2, 4.2 TỶ môi giới
tp hồ chí
minh
420000000
0 nhà 25

1. (1 điểm) Đọc dữ liệu và hiển thị 10 dòng đầu tiên của dữ liệu
2. (5 điểm) Tìm hiểu thông tin về dữ liệu:
   a. (0.75 điểm) Số lượng loại mỗi loại (type) bất động sản có trong dữ liệu
   Loại BDS Số lượng
   nhà
   chung cư
   đất
   khác
   b. (2 điểm)
   i. (0.5 điểm) Số lượng bất động sản của mỗi loại (type) theo từng cách thức rao
   bán (poster_temp).
   Cách rao bán khác môi giơi
   nhà
   chung cư
   đất
   khác
   ii. (1.5 điểm) Vẽ biểu đồ tròn thể hiện phần trăm của từng loại bất động sản theo
   từng cách thức rao bán dựa vào bảng trên và đưa ra nhận xét (tối thiểu 2 nhận xét)
   c. (1.0 điểm)
   i. Tạo bảng dữ liệu mới chỉ có 3 vùng (tp hồ chí minh, hà nội và đà nẵng) và cho
   biết số dòng của bảng dữ liệu mới
   ii. (0.75)Từ bảng dữ liệu trên hãy so sánh các đại lượng thống kê giá trị
   trung bình, trung vị, độ lệch chuẩn của giá BDS của mỗi vùng, vẽ biểu đồ cột và
   đưa ra nhận xét
   d. (1.25 điểm)
   i. (0.5 điểm) Tạo bảng dữ liệu có diện tích (acreage khác -1) và cho biết
   số dòng của bảng dữ liệu mới.
   ii. (1.0 điểm) Vẽ biểu đồ thể hiện số BDS có diện tích trong mô tả (acreage
   khác -1) của mỗi loại poster và đưa ra nhận xét
3. (2 điểm)
   a. (1 điểm) Chuyển dữ liệu time thành kiểu datatime, vẽ biểu đồ thể hiện số lượng
   bất động sản được bán theo từng tháng trong năm 2020 và đưa ra nhận xét
   b. (1 điểm)Hãy tính sác xuất để một bất động sản được bán trong mùa hè (từ tháng
   6 đến tháng 8) năm 2020
4. (2 điểm) Hãy dựa vào bảng dữ liệu được cung cấp, tính xác suất để trong 50 bất động
   sản được bán có 25 bất động sản có giá trị lớn hơn 3 tỷ

5. THỐNG KÊ MÔ TẢ (DESCRIPTIVE STATISTICS)
   Giá trị trung bình (Mean): Đại diện cho giá trị trung bình cộng của một tập hợp
   dữ liệu.
   import numpy as np
   data = [2, 4, 6, 8, 10]
   mean = np.mean(data)
   print("Mean:", mean)
   Trung vị (Median): Là giá trị giữa của dữ liệu khi đã được sắp xếp.
   median = np.median(data)
   print("Median:", median)
   Độ lệch chuẩn (Standard Deviation): Đo lường sự phân tán của dữ liệu so với giá
   trị trung bình.
   std_dev = np.std(data)
   print("Standard Deviation:", std_dev)
   Trực quan hóa dữ liệu: Các biểu đồ thường dùng bao gồm:
   • Histogram: Để hiểu phân bố của dữ liệu.
   • Boxplot: Để hiển thị các đặc trưng như trung vị, phần trăm các giá trị.
   import matplotlib.pyplot as plt
   plt.hist(data)
   plt.show()
6. MÔ PHỎNG (SIMULATION)
   Mô phỏng là quá trình tạo ra dữ liệu ngẫu nhiên để mô phỏng một quá trình hoặc sự
   kiện thực tế, thường dùng trong các bài toán dự đoán và nghiên cứu xác suất. Mô
   phỏng biến ngẫu nhiên: Dùng numpy để mô phỏng các phân phối ngẫu nhiên.
   Mô phỏng tung đồng xu (2 giá trị xác suất: mặt ngửa hoặc mặt sấp):
   outcomes = np.random.choice(['Heads', 'Tails'], size=10)
   print(outcomes)
   @TaiLieuITIUH
   18
   Mô phỏng lăn xúc xắc (6 giá trị xác suất):
   dice_rolls = np.random.choice([1, 2, 3, 4, 5, 6], size=10)
   print(dice_rolls)
   Mô phỏng chuỗi thời gian (Time Series):
   time_series = np.cumsum(np.random.randn(1000))
   plt.plot(time_series)
   plt.show()
7. Phân phối xác suất (Probability Distributions)
   Phân phối xác suất mô tả khả năng xuất hiện của các kết quả khác nhau trong một
   không gian mẫu.
   Phân phối chuẩn (Normal Distribution): Đường cong hình chuông, đặc trưng bởi giá
   trị trung bình và độ lệch chuẩn.
   from scipy.stats import norm
   x = np.linspace(-5, 5, 100)
   plt.plot(x, norm.pdf(x, 0, 1)) # Mean=0, StdDev=1
   plt.title("Normal Distribution")
   plt.show()
   Phân phối nhị thức (Binomial Distribution): Số lần thành công trong một số lần
   thử cố định, với xác suất thành công cố định.
   from scipy.stats import binom
   n, p = 10, 0.5 # 10 trials, probability of success = 0.5
   x = np.arange(0, n+1)
   plt.plot(x, binom.pmf(x, n, p))
   plt.title("Binomial Distribution")
   plt.show()
   Phân phối Poisson: Dùng để mô tả số lần một sự kiện xảy ra trong một khoảng thời
   gian xác định.
   from scipy.stats import poisson
   plt.plot(x, poisson.pmf(x, mu=3))
   plt.title("Poisson Distribution")
   plt.show()
   @TaiLieuITIUH
   19
   Xem lại các bài lab đã thực hành
   NUMPY

# Phát sinh ngẫu nhiên mảng arr gồm 100 phần tử số nguyên có giá trị từ 0 đến

1000
arr = np.random.randint(0, 1001, 100)
print("Mảng ngẫu nhiên arr =\n",arr)
#Câu 1

# 1. Hiển thị 10 phần tử đầu tiên

print("10 phần tử đầu tiên:", arr[:10])

# 2. Hiển thị 5 phần tử cuối cùng

print("5 phần tử cuối cùng:", arr[-5:])

# 3. Hiển thị các phần tử thỏa mãn điều kiện chia hết cho 5 và lớn hơn 100

result = arr[(arr % 5 == 0) & (arr > 100)]
print("Các phần tử chia hết cho 5 và lớn hơn 100:", result)
#Tính tổng mảng
print(f'- Tổng: {arr.sum()}')
#Tìm giá trị trung bình
print('- Trung bình:', arr.mean())
#Tìm giá trị trung vị
print('- Trung vị:', np.median(arr))
#Tìm Q1, Q2, Q3
print('- Tứ phân vị [Q1, Q2, Q3]:', np.quantile(arr, [0.25, 0.5, 0.75]))
#Tìm phân vị 20 (percentile 20)
print('- Phân vị 20:', np.percentile(arr, 20))
import numpy as np

# Chọn ngẫu nhiên 10 phần tử không hoàn lại từ mảng arr 5 lần

for i in range(5):
selected = np.random.choice(arr, size=10, replace=False)
print(f'Lần chọn ngẫu nhiên {i+1}: {selected}')
@TaiLieuITIUH
20
MATPLOTLIB

# Câu 6: Vẽ đồ thị cột

import numpy as np
import matplotlib.pyplot as plt

# Vẽ đồ thị cột đơn giản

x = np.array(["Java", "Python", "PHP", "JavaScript", "C#", "C++"])
y = np.array([22, 18, 9, 8, 7.7, 7])

# Thiết lập tiêu đề và nhãn cho các trục

plt.title('Mức độ phổ biến của các ngôn ngữ lập trình')
plt.xlabel('Programming Langague')
plt.ylabel('Poplarity')
plt.bar(x,y)
plt.show()

# Câu 7: Vẽ đồ thị bánh pie

import matplotlib.pyplot as plt
import numpy as np
y = np.array([31.27, 24.79, 12.39, 11.27, 10.85, 9.44])
mylabels = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
myexplode = [0.1, 0, 0, 0, 0, 0]
plt.pie(y, labels = mylabels, explode = myexplode,
shadow=True, startangle=-90, autopct='%.2f%%')
plt.axis('equal') # Đảm bảo biểu đồ là hình tròn
plt.show()
#startangle là điều chỉnh góc độ thê độ 180 360
#shadow: là bóng
#explode: bôi đậm phần tham số đố
#autopct: hiển thị tỉ lệ phần trăm
@TaiLieuITIUH
21

# Câu 8: vẽ histogram

import numpy as np
import matplotlib.pyplot as plt

# Phát sinh 10000 số ngẫu nhiên thuộc phân phối chuẩn

data = np.random.normal(size=10000)

# Vẽ histogram của các số ngẫu nhiên #Vẽ histogram sử dụng hàm hist()

plt.hist(data, bins=100) #bins: chia thành 100 cột

# Thêm tiêu đề và nhãn

plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Hiển thị biểu đồ

plt.show()
SEABORN
import matplotlib.pyplot as plt
import seaborn as sns

# Tải dữ liệu tips

df = sns.load_dataset("tips")

# Vẽ đồ thị thể hiện tổng tiền tip theo ngày

sns.barplot(x="day", y="tip", data=df, estimator=sum, errorbar=None)

# Định dạng và hiển thị đồ thị

plt.title('Tổng tiền tip theo ngày')
plt.xlabel('Ngày')
plt.ylabel('Tổng tiền tip')
plt.show()

# x="day": Trục x biểu diễn các ngày trong tuần.

# y="tip": Trục y biểu diễn giá trị tiền tip.

# data=df: Dữ liệu được sử dụng là DataFrame df.

# estimator=sum: Sử dụng hàm sum để tính tổng tiền tip cho mỗi ngày.

# ci=None: Loại bỏ khoảng tin cậy (confidence interval) cho biểu đồ thanh.

# errorbar=None: nếu không hỗ trợ ci=None thì dùng errorbar để thay thế

@TaiLieuITIUH
22
import matplotlib.pyplot as plt
import seaborn as sns

# Tải dữ liệu tips

df = sns.load_dataset("tips")

# Vẽ đồ thị thể hiện tổng tiền tip theo ngày

sns.barplot(x="time", y="tip", data=df, estimator=sum, errorbar=None)

# Định dạng và hiển thị đồ thị

plt.title('Tổng tiền tip theo bữa')
plt.xlabel('Bữa')
plt.ylabel('Tổng tiền tip')
plt.show()
import seaborn as sns
import matplotlib.pyplot as plt

# Tải dữ liệu tips

df = sns.load_dataset("tips")

# Vẽ boxplot cho cột total_bill

sns.boxplot(x="day", y="total_bill", data=df)

# Định dạng và hiển thị biểu đồ

plt.title('Đồ thị boxplot so sánh tổng hóa đơn giữa các ngày trong tuần')
plt.xlabel('Ngày trong tuần')
plt.ylabel('Tổng tiền hóa đơn')
plt.show()
@TaiLieuITIUH
23
import seaborn as sns
import matplotlib.pyplot as plt

# Tải dữ liệu tips

df = sns.load_dataset("tips")

# Tạo subplot để hiển thị hai đồ thị histogram cạnh nhau

fig, axes = plt.subplots(1, 2, figsize=(14, 6), sharey=True)

# Vẽ histogram cho thời gian dùng bữa "Lunch"

sns.histplot(df[df["time"] == "Lunch"]["total_bill"], kde=True, ax=axes[0],
color='skyblue')
axes[0].set_title('Tổng tiền hóa đơn cho bữa trưa (Lunch)')
axes[0].set_xlabel('Tổng tiền hóa đơn')
axes[0].set_ylabel('Tần suất')

# Vẽ histogram cho thời gian dùng bữa "Dinner"

sns.histplot(df[df["time"] == "Dinner"]["total_bill"], kde=True, ax=axes[1],
color='salmon')
axes[1].set_title('Tổng tiền hóa đơn cho bữa tối (Dinner)')
axes[1].set_xlabel('Tổng tiền hóa đơn')

# Hiển thị biểu đồ

plt.tight_layout()
plt.show()
@TaiLieuITIUH
24

# Simulation - Mô phỏng & Dữ liệu

#Cau B thucj hien tung dong xu =100 lan cho biet so lan xuat hien cua moi mat
import matplotlib.pyplot as plt
#dem so lan xuat hien cua moi mat
results = {'H':0, 'T':0}
for i in range(0,100):
item = toss_a_fair_coin()
results[item]+=1
print('Ket qua sau khi tung 100 lan',results)
faces = list(results.keys())
counts = list(results.values())
plt.bar(faces, counts, color=['blue', 'orange'])
plt.xlabel('Mặt đồng xu')
plt.ylabel('Số lần xuất hiện')
plt.title(f'Kết quả tung đồng xu 100 lần)')
plt.show()
#a. Định nghĩa hàm toss_a_biased_coin
def toss_a_biased_coin(head_prob):
return random.choices(['H', 'T'], weights=[head_prob, 1 - head_prob])[0]
#b. Thực hiện việc tung đồng xu n = 100 lần
import matplotlib.pyplot as plt

# Đếm số lần xuất hiện của mỗi mặt

def simulate*biased_coin_tosses(num_tosses, head_prob):
results = {'H': 0, 'T': 0}
for * in range(num_tosses):
result = toss_a_biased_coin(head_prob)
results[result] += 1
return results
@TaiLieuITIUH
25
import random
import matplotlib.pyplot as plt

# a. Phát sinh ngẫu nhiên chiều cao của 1000 người

num*people = 1000
heights = [random.randint(140, 210) for * in range(num_people)]

# b. Xác định tỷ lệ các mức chiều cao

def categorize_height(height):
if height < 160:
return 'Thấp'
elif 160 <= height < 175:
return 'Bình thường'
elif 175 <= height < 190:
return 'Cao'
else:
return 'Rất cao'

# Phân loại các chiều cao

categories = [categorize_height(height) for height in heights]

# Tính tỷ lệ phần trăm cho mỗi mức

category_counts = {category: categories.count(category) for category in ['Thấp',
'Bình thường', 'Cao', 'Rất cao']}
category_percentages = {category: (count / num_people) \* 100 for category, count
in category_counts.items()}

# c. Vẽ đồ thị biểu diễn tỷ lệ của mỗi mức chiều cao

# Biểu đồ tròn

plt.figure(figsize=(10, 7))
plt.pie(category_percentages.values(), labels=category_percentages.keys(),
autopct='%1.1f%%', colors=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.title('Tỷ lệ từng mức chiều cao')
plt.show()

# Biểu đồ cột

plt.figure(figsize=(10, 7))
plt.bar(category_percentages.keys(), category_percentages.values(),
color=['#ff9999','#66b3ff','#99ff99','#ffcc99'])
plt.xlabel('Mức chiều cao')
plt.ylabel('Tỷ lệ (%)')
plt.title('Tỷ lệ từng mức chiều cao')
plt.show()
@TaiLieuITIUH
26
DATA – DỮ LIỆU
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Đọc dữ liệu từ tập tin temperature.csv

data = pd.read_csv('temperature.csv')

# Xem qua dữ liệu để hiểu cấu trúc

print(data.head())

# a. Tính toán thống kê cho mỗi tỉnh thành

provinces = data.columns[1:] # Giả sử cột đầu tiên là ngày/tháng và các cột còn
lại là nhiệt độ của các tỉnh
stats = {}
for province in provinces:
temperatures = data[province].to_numpy()
min_temp = np.min(temperatures)
max_temp = np.max(temperatures)
mean_temp = np.mean(temperatures)
std_dev = np.std(temperatures)
temp_range = max_temp - min_temp
stats[province] = {
'Min': min_temp,
'Max': max_temp,
'Mean': mean_temp,
'Std Dev': std_dev,
'Range': temp_range
}
print(f"\n{province}:")
print(f"Nhiệt độ thấp nhất: {min_temp:.2f}")
print(f"Nhiệt độ cao nhất: {max_temp:.2f}")
print(f"Nhiệt độ trung bình: {mean_temp:.2f}")
print(f"Độ lệch chuẩn: {std_dev:.2f}")
print(f"Độ biến thiên về nhiệt độ: {temp_range:.2f}")
@TaiLieuITIUH
27
import pandas as pd
import matplotlib.pyplot as plt

# b. Vẽ histogram nhiệt độ của TP.HCM

# b. Vẽ histogram nhiệt độ của TP.HCM

plt.figure(figsize=(10, 6))

# Trích xuất dữ liệu nhiệt độ của TP.HCM, loại bỏ giá trị NaN

temperature_HCM = data['Ho Chi Minh']

# Vẽ histogram

plt.hist(temperature_HCM, bins=20, edgecolor='black', alpha=0.75)

# Thêm các nhãn và tiêu đề

plt.xlabel('Nhiệt độ (°C)')
plt.ylabel('Số lần xuất hiện')
plt.title('Histogram nhiệt độ của TP.HCM')
plt.grid(True)

# Hiển thị đồ thị

plt.show()
#c. Lựa chọn đồ thị để so sánh nhiệt độ của 6 tỉnh thành
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Chọn 6 tỉnh thành

selected_provinces = ['Ha Noi','Vinh','Da Nang','Nha Trang','Ho Chi Minh','Ca
Mau']

# Tính toán nhiệt độ trung bình của mỗi tỉnh thành

mean_temps = [data[province].dropna().mean() for province in selected_provinces]

# Vẽ biểu đồ cột

plt.figure(figsize=(12, 6))
plt.bar(selected_provinces, mean_temps,
color=['#ff9999','#66b3ff','#99ff99','#ffcc99','#ffb3e6','#c2c2f0'])
plt.xlabel('Tỉnh thành')
plt.ylabel('Nhiệt độ trung bình (°C)')
plt.title('So sánh nhiệt độ trung bình của 6 tỉnh thành')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
@TaiLieuITIUH
28

# a. Tỷ lệ nam nữ

genders = data['Gender']
unique, counts = np.unique(genders, return_counts=True)
gender_counts = dict(zip(unique, counts))
total_count = len(genders)
gender_ratios = {gender: count / total_count for gender, count in
gender_counts.items()}
print("Tỷ lệ nam nữ:")
for gender, ratio in gender_ratios.items():
print(f"{gender}: {ratio:.2%}")

# Tính toán các đại lượng thống kê cho chiều cao và cân nặng

heights = data['Height_cm']
weights = data['Weight_kg']
def calculate_statistics(array):
min_val = np.min(array)
max_val = np.max(array)
range_val = max_val - min_val
mean_val = np.mean(array)
std_dev = np.std(array)
return min_val, max_val, range_val, mean_val, std_dev
height_stats = calculate_statistics(heights)
weight_stats = calculate_statistics(weights)
print("\nCác đại lượng thống kê:")
print("Chiều cao (Height):")
print(f" Min: {height_stats[0]:.2f} cm")
print(f" Max: {height_stats[1]:.2f} cm")
print(f" Range: {height_stats[2]:.2f} cm")
print(f" Mean: {height_stats[3]:.2f} cm")
print(f" Std Dev: {height_stats[4]:.2f} cm")
print("\nCân nặng (Weight):")
print(f" Min: {weight_stats[0]:.2f} kg")
print(f" Max: {weight_stats[1]:.2f} kg")
print(f" Range: {weight_stats[2]:.2f} kg")
print(f" Mean: {weight_stats[3]:.2f} kg")
print(f" Std Dev: {weight_stats[4]:.2f} kg")
@TaiLieuITIUH
29
#b. Vẽ đồ thị histogram về chiều cao và cân nặng của hai thuộc tính chiều cao và
cân nặng
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(heights, bins=20, edgecolor='black', alpha=0.75)
plt.xlabel('Chiều cao (cm)')
plt.ylabel('Số lần xuất hiện')
plt.title('Histogram chiều cao')
plt.subplot(1, 2, 2)
plt.hist(weights, bins=20, edgecolor='black', alpha=0.75)
plt.xlabel('Cân nặng (kg)')
plt.ylabel('Số lần xuất hiện')
plt.title('Histogram cân nặng')
plt.tight_layout()
plt.show()

# 5. Có bao nhiêu nam, bao nhiêu nữ. Tỷ lệ bao nhiêu?

# Số lượng nam, nữ và tỷ lệ

gender_counts = df['sex'].value_counts()
num_males = gender_counts['Male']
num_females = gender_counts['Female']
male_ratio = num_males / num_rows _ 100
female_ratio = num_females / num_rows _ 100
print(f"Số lượng nam: {num_males}, Số lượng nữ: {num_females}")
print(f"Tỷ lệ nam: {male_ratio:.2f}%, Tỷ lệ nữ: {female_ratio:.2f}%")

# 6. Số lượng người hút thuốc và tỷ lệ

smoker_count = df['smoker'].value_counts()['Yes']
smoker_ratio = smoker_count / num_rows \* 100
print(f"Số lượng người hút thuốc: {smoker_count}")
print(f"Tỷ lệ người hút thuốc: {smoker_ratio:.2f}%")
@TaiLieuITIUH
30

# 7. Ngày nào trong tuần khách hàng hay đến dùng bữa nhất. Tỷ lệ bao nhiêu?

day_counts = df['day'].value_counts()
most_frequent_day = day_counts.idxmax()
most_frequent_day_count = day_counts.max()
most_frequent_day_ratio = most_frequent_day_count / num_rows \* 100
print(f"Ngày khách hàng đến dùng bữa nhiều nhất: {most_frequent_day}\nTỷ lệ:
{most_frequent_day_ratio:.2f}%")

# 3. Giữa nam và nữ ai tip nhiều tiền hơn, ai tip thường xuyên hơn?

# Tính tiền tip trung bình theo giới tính

average_tip_by_gender = df.groupby('sex')['tip'].mean()
tip_frequency_by_gender = df['sex'].value_counts()
print("Tiền tip trung bình theo giới tính:")
print(average_tip_by_gender)
print("Số lần tip theo giới tính:")
print(tip_frequency_by_gender)
TRỰC QUAN DỮ LIỆU

# 1. Vẽ đồ thị thể hiện tổng tiền tip theo ngày

total_tip_by_day = tips.groupby('day')['tip'].sum()
plt.figure(figsize=(8, 5))
total_tip_by_day.plot(kind='bar', color='skyblue')
plt.title('Tổng tiền tip theo ngày')
plt.xlabel('Ngày')
plt.ylabel('Tổng tiền tip (USD)')
plt.xticks(rotation=45)
plt.show()

# 3. Vẽ đồ thị histogram của tổng hoá đơn

plt.figure(figsize=(8,5))
plt.hist(tips['total_bill'], bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram của tổng hoá đơn')
plt.xlabel('Tổng hoá đơn (USD)')
@TaiLieuITIUH
31

# Tính tổng hóa đơn theo từng ngày

total_bill_by_day = tips.groupby('day')['total_bill'].sum()

# Vẽ biểu đồ cột

plt.figure(figsize=(8, 5))
total_bill_by_day.plot(kind='bar', color='lightcoral')
plt.title('Tổng chi tiêu theo ngày trong tuần')
plt.xlabel('Ngày')
plt.ylabel('Tổng hoá đơn (USD)')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()
Trực quan vơi seaborn

# 1. Vẽ đồ thị thể hiện tổng tiền tip theo ngày

plt.figure(figsize=(8, 5))
sns.barplot(x='day', y='tip', data=tips, estimator=sum)
plt.title('Tổng tiền tip theo ngày')
plt.xlabel('Ngày')
plt.ylabel('Tổng tiền tip (USD)')
plt.show()

# 3. Vẽ đồ thị histogram của tổng hoá đơn

plt.figure(figsize=(8,5))
sns.histplot(tips['total_bill'], bins=20, kde=True, color='skyblue')
plt.title('Histogram của tổng hoá đơn')
plt.xlabel('Tổng hoá đơn (USD)')

# 4. Vẽ đồ thị boxplot của tổng hoá đơn

plt.figure(figsize=(8,5))
sns.boxplot(x='total_bill', data=tips, color='skyblue')
plt.title('Boxplot của tổng hóa đơn')
plt.xlabel('Tổng hóa đơn (USD)')
@TaiLieuITIUH
32
LAB06 – Tạo quần thể mô phỏng

# Bạn hãy tạo một mẫu gồm 10000 phần tử mô phỏng chiều cao của nam thanh niên có

giá trị từ 120cm - 200cm. Bạn hãy lưu kết quả vào biến POP.
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
POP = np.random.uniform(120, 200, 10000)

# Tính: a. Chiều cao trung bình (kỳ vọng) của quần thể và độ lệch chuẩn về chiều

cao của quần thể.
print("Chiều cao trung bình của quần thể: ", np.mean(POP))
print("Độ lệch chuẩn về chiều cao của quần thể: ", np.std(POP))

# b. Tính tỷ lệ người cao trong quần thể, biết rằng thanh niên có chiều cao từ

180 trở lên được gọi là cao.
CountOfTallMan = np.sum(POP >= 180)
ratioOfTallMan = CountOfTallMan / len(POP) \* 100
print("Tỷ lệ người cao trong quần thể: ", ratioOfTallMan,"%")

# c. Vẽ histogram về chiều cao của quần thể. Theo bạn quần thể có phân phối chuẩn

hay không?
plt.figure(figsize=(8,5))
plt.hist(POP, bins=30, color='pink', edgecolor='black', alpha=0.7)
plt.title('Histogram về chiều cao của quần thể')
plt.xlabel('Chiều cao (cm)')
plt.ylabel('Số lượng')
plt.grid(axis='y', alpha=0.75)

# d. Thử vẽ histogram và đồ thị hàm mật độ của phân phối chuẩn sử dụng tham số

loc và scale bằng với kỳ vọng và độ lệch chuẩn của quần thể.
plt.figure(figsize=(10, 6))
sns.histplot(POP, bins=30, kde=False, color='skyblue', edgecolor='black',
stat='density', label='Histogram')
std_dev_height = np.std(POP)
mean_height = np.mean(POP)

# Tính toán hàm mật độ của phân phối chuẩn

x = np.linspace(120, 200, 1000)
pdf = (1 / (std_dev_height _ np.sqrt(2 _ np.pi))) _ np.exp(-0.5 _ ((x -
mean_height) / std_dev_height) \*\* 2)
@TaiLieuITIUH
33

# Vẽ đồ thị hàm mật độ

plt.plot(x, pdf, color='red', label='Hàm mật độ phân phối chuẩn')
plt.title('Histogram và hàm mật độ của phân phối chuẩn')
plt.xlabel('Chiều cao (cm)')
plt.ylabel('Mật độ')
plt.legend()
plt.grid()
plt.show()

# a. Thực hiện bài 2 100 lần, mỗi lần bạn tính được trung bình mẫu. Vẽ đồ thị

histogram cho 100 trung bình mẫu bạn tính được.
def PPMEAN(data, sample*size, num_samples):
sample_means = []
for * in range(num_samples):
sample = np.random.choice(data, size=sample_size, replace=False)
sample_mean = np.mean(sample)
sample_means.append(sample_mean)
return sample_means

# Sử dụng hàm để lấy 100 trung bình mẫu với kích thước mẫu là 20

sample_means_20 = PPMEAN(data=POP, sample_size = 20, num_samples=100)

# Vẽ histogram cho 100 trung bình mẫu

plt.figure(figsize=(8, 5))
sns.histplot(sample_means_20, bins=10, color='skyblue', stat='density',
edgecolor='black')
plt.title('Histogram của 100 trung bình mẫu (cỡ 20)')
plt.xlabel('Trung bình mẫu (cm)')
plt.ylabel('Mật độ')
plt.grid()
plt.show()
