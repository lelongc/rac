họ tên

chữ cái đầu
^[A-Z][a-z]*(\s+[A-Z][a-z]*)+$

số điện thoại
hoặc và 10 số
^(09|03|08)\d{8}$

gmail

@.*\.com$
^[a-zA-Z0-9._%+-]+@gmail\.com$

1đ) HỌ VÀ TÊN: Có ít nhất 2 từ và ký tự đầu tiên của mỗi từ phải được viết hoa. Thiết lập
giá trị mặc định là Họ tên SV (ví dụ: Nguyen Van An )
^[A-Z][a-z]*(\s+[A-Z][a-z]*)+$


b. (1đ) SỐ ĐIỆN THOẠI: theo mẫu: 0XXX.XXX.XXX trong đó X: là ký tự số (số điện thoại
10 ký tự số, bắt đầu là 09, 08, 07, 06, 05, 04,03).
^(09|08|07|06|05|04|03)\d{2}\.\d{3}\.\d{3}$
^0[3-9]\d{2}\.\d{3}\.\d{3}$

EMAIL theo mẫu: name_email@gmail.com, trong đó name_email ít nhất là 3 ký tự chỉ là các ký tự chữ,sốhoặc dấu gạch _ 
^[a-zA-Z0-9_]{3,}@gmail\.com$

d. (1đ) ĐỊA CHỈ bao gồm các kí tự số và chữ và kí tự /
^[a-zA-Z0-9/]+$
nếu có thêm dấu cách
^[a-zA-Z0-9\s/]+$

Họ Và Tên: Có ít nhất 2 từ và ký tự đầu tiên của mỗi từ phải được viết hoa. Thiết lập giá trị mặc định là Họ tên SV ví dụ: Tran Anh Dung
value="Nguyen Van An" vô chõ input
^[A-Z][a-z]*(\s+[A-Z][a-z]*)+$

c. Số Điện Thoại: theo mẫu: 0XXX.XXX.XXX trong đó X: là ký tự số.
^0\d{3}\.\d{3}\.\d{3}$

e. Email Của Bạn theo mẫu: name_email@gmail.com , trong đó name_email ít nhất là 3 ký tự trong đó có kí tự chữ, ký tự số, ít nhất 1 ký tự đặc biệt.
^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*_)[a-zA-Z0-9_]{3,}@gmail\.com$

Mã Tour theo mẫu: XXX-XXX-mm-yyyy với X là các ký tự hoa chỉ thông tin điểm
khởi hành và điểm đến, mm: tháng khởi hành, yyyy: năm khởi hành(1 điểm). (mức 1)
^[A-Z]{3}-[A-Z]{3}-(0[1-9]|1[0-2])-\d{4}$

c. Ngày khởi hành phải sau ngày hiện tại 30 ngày (1 điểm). (mức 2)
d. Giá Tour là số >0 (1 điểm). (mức 3)
e. Hình đại diện phải đúng loại hình thuộc 1 trong các đuôi kiểu jpg, gif, png không phân
biệt hoa thường , cái này là text regex thôi
^.+\.(jpg|gif|png)$

Họ Và Tên: Có ít nhất 2 từ và ký tự đầu tiên của mỗi từ phải được viết hoa. Thiết lập giá trị mặc
định là Họ tên SV ví dụ: Tran Anh Dung
c. Số Điện Thoại: theo mẫu: 0XXX.XXX.XXX trong đó X: là ký tự số.
^0\d{3}\.\d{3}\.\d{3}$
d. Ngày Đặt sau ngày hiện tại.
e. Email Của Bạn theo mẫu: name_email@iuh.edu.vn, trong đó name_email ít nhất là 3 ký tự
trong đó có kí tự chữ, ký tự số, ít nhất 1 ký tự đặc biệt.
^[a-zA-Z0-9]*[!@#$%^&_()\_+\-=\[\]{};':"\\|,.<>\/?][a-zA-Z0-9]_@iuh\.edu\.vn$

(1 điểm) Họ tên không được bỏ trống, họ tên phải từ 2 từ trở lên, mỗi ký tự đầu phải
viết hoa.
^[A-Z]+(\s+[A-Z]+)+$
b. (1 điểm) Số điện thoại không rỗng, nhập theo định dạng sau: XXX-YYYYYY, trong
đó X, Y là các ký tự số.
^\d{3}-\d{6}$
c. (1 điểm) Ngày sinh hợp lệ khi tuổi trên 15 và dưới 18

Họ tên khách hàng: Họ tên chỉ là các ký tự in hoa, có thể có khoảng trắng, họ tên có ít
nhất là 2 từ Họ, Tên (1 đ).
^[A-Z]+(\s+[A-Z]+)+$
b. Hình CMND là các file hình có tên bất kỳ và có phần định dạng .jpg, .png, .gif (1 đ).
c. Ngày đi phải sau ngày hiện tại từ 1 ngày trở lên (1 đ).
d. Số điện thoại gồm 10 chữ số trong đó 2 chữ số đầu là 09, 08 hoặc 07 và theo sau là 8
chữ số. (1 đ)
^(09|08|07)\d{8}$

Mã sách có định dạng XXX-XX-XXX, trong có XXX là 3 chữ số, XX là 2 ký tự số thể
hiện năm từ năm hiện tại về sau, XXX 2 ký tự in hoa (1 đ).
^\d{3}-\d{2}-[A-Z]{3}$
b. Hình minh họa là các file hình có tên bất kỳ và có phần định dạng .jpg, .png, .gif (1 đ)
c. Ngày nhập phải sau ngày hiện tại (1 đ).
d. Số lượng phải >0 và <1000 (1 đ).
// Không thể dùng regex hoàn toàn, cần kiểm tra bằng code:
// var num = parseInt(value);
// return num > 0 && num < 1000;

a. Mã bệnh nhân có định dạng BN-YYYYY, trong có BN có định, YYYYY là 5 chữ số
^BN-\d{5}$

b. Số khám bệnh là các file hình có tên bắt kỳ và có phần định dạng .jpg, .png, .gif
^.+\.(jpg|png|gif)$
