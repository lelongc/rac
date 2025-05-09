họ tên

chữ cái đầu
^[A-Z][a-z]_(\s+[A-Z][a-z]_)+$

số điện thoại
hoặc và 10 số
^(09|03|08)\d{8}$

gmail

@.\*\.com$
^[a-zA-Z0-9._%+-]+@gmail\.com$

1đ) HỌ VÀ TÊN: Có ít nhất 2 từ và ký tự đầu tiên của mỗi từ phải được viết hoa. Thiết lập
giá trị mặc định là Họ tên SV (ví dụ: Nguyen Van An )
^[A-Z][a-z]_(\s+[A-Z][a-z]_)+$

b. (1đ) SỐ ĐIỆN THOẠI: theo mẫu: 0XXX.XXX.XXX trong đó X: là ký tự số (số điện thoại
10 ký tự số, bắt đầu là 09, 08, 07, 06, 05, 04,03).
^(09|08|07|06|05|04|03)\d{2}\.\d{3}\.\d{3}$
^0[3-9]\d{2}\.\d{3}\.\d{3}$

EMAIL theo mẫu: name_email@gmail.com, trong đó name*email ít nhất là 3 ký tự chỉ là các ký tự chữ,sốhoặc dấu gạch *
^[a-zA-Z0-9_]{3,}@gmail\.com$

d. (1đ) ĐỊA CHỈ bao gồm các kí tự số và chữ và kí tự /
^[a-zA-Z0-9/]+$
nếu có thêm dấu cách
^[a-zA-Z0-9\s/]+$

Họ Và Tên: Có ít nhất 2 từ và ký tự đầu tiên của mỗi từ phải được viết hoa. Thiết lập giá trị mặc định là Họ tên SV ví dụ: Tran Anh Dung
value="Nguyen Van An" vô chõ input
^[A-Z][a-z]_(\s+[A-Z][a-z]_)+$

c. Số Điện Thoại: theo mẫu: 0XXX.XXX.XXX trong đó X: là ký tự số.
^0\d{3}\.\d{3}\.\d{3}$

e. Email Của Bạn theo mẫu: name_email@gmail.com , trong đó name*email ít nhất là 3 ký tự trong đó có kí tự chữ, ký tự số, ít nhất 1 ký tự đặc biệt.
^(?=.*[a-zA-Z])(?=.\*[0-9])(?=.\*\*)[a-zA-Z0-9_]{3,}@gmail\.com$

Mã Tour theo mẫu: XXX-XXX-mm-yyyy với X là các ký tự hoa chỉ thông tin điểm
khởi hành và điểm đến, mm: tháng khởi hành, yyyy: năm khởi hành(1 điểm). (mức 1)
^[A-Z]{3}-[A-Z]{3}-(0[1-9]|1[0-2])-\d{4}$

d. Giá Tour là số >0 (1 điểm). (mức 3)
^[1-9]\d\*$

e. Hình đại diện phải đúng loại hình thuộc 1 trong các đuôi kiểu jpg, gif, png không phân
biệt hoa thường , cái này là text regex thôi
^.+\.(jpg|gif|png)$

Họ Và Tên: Có ít nhất 2 từ và ký tự đầu tiên của mỗi từ phải được viết hoa. Thiết lập giá trị mặc
định là Họ tên SV ví dụ: Tran Anh Dung
^[A-Z][a-z]_(\s+[A-Z][a-z]_)+$

c. Số Điện Thoại: theo mẫu: 0XXX.XXX.XXX trong đó X: là ký tự số.
^0\d{3}\.\d{3}\.\d{3}$

e. Email Của Bạn theo mẫu: name_email@iuh.edu.vn, trong đó name*email ít nhất là 3 ký tự
trong đó có kí tự chữ, ký tự số, ít nhất 1 ký tự đặc biệt.
^(?=.*[a-zA-Z])(?=.\*[0-9])(?=.\*\*)[a-zA-Z0-9_]{3,}@iuh\.edu\.vn$

b. (1 điểm) Số điện thoại không rỗng, nhập theo định dạng sau: XXX-YYYYYY, trong
đó X, Y là các ký tự số.
^\d{3}-\d{6}$

c. (1 điểm) Ngày sinh hợp lệ khi tuổi trên 15 và dưới 18

$("#date").on("change", function () {
  const selectedDate = new Date($(this).val());
const today = new Date();
today.setHours(0, 0, 0, 0);

let isValid = true;
let errorMessage = "";

// Tính tuổi
const ageDiff = today - selectedDate;
const ageDate = new Date(ageDiff);
const age = Math.abs(ageDate.getUTCFullYear() - 1970);

// Kiểm tra điều kiện tuổi
if (age <= 15 || age >= 18) {
isValid = false;
errorMessage = "Tuổi phải lớn hơn 15 và nhỏ hơn 18.";
}

// Hiển thị hoặc ẩn lỗi
if (!isValid) {
$(this).addClass("is-invalid").removeClass("is-valid");
$(this).siblings(".invalid-feedback").text(errorMessage).show();
} else {
$(this).removeClass("is-invalid").addClass("is-valid");
$(this).siblings(".invalid-feedback").hide();
}
});

Họ tên khách hàng: Họ tên chỉ là các ký tự in hoa, có thể có khoảng trắng, họ tên có ít
nhất là 2 từ Họ, Tên (1 đ).
^[A-Z]+(\s+[A-Z]+)+$

c. Ngày đi phải sau ngày hiện tại từ 1 ngày trở lên (1 đ).

if ((selectedDate - today) / (1000 _ 60 _ 60 \* 24) < 1) {
isValid = false;
errorMessage = "Ngày phải sau hôm nay ít nhất 1 ngày.";
}

d. Số điện thoại gồm 10 chữ số trong đó 2 chữ số đầu là 09, 08 hoặc 07 và theo sau là 8
chữ số. (1 đ)
^(09|08|07)\d{8}$

Mã sách có định dạng XXX-XX-XXX, trong có XXX là 3 chữ số, XX là 2 ký tự số thể
hiện năm từ năm hiện tại về sau, XXX 3 ký tự in hoa (1 đ).
^\d{3}-\d{2}-[A-Z]{3}$

d. Số lượng phải >0 và <1000 (1 đ).
^(?:[1-9]|[1-9]\d|[1-9]\d{2})$

function validateSoLuong(value) {
const num = parseInt(value, 10);
return !isNaN(num) && num > 0 && num < 1000;
}

a. Mã bệnh nhân có định dạng BN-YYYYY, trong có BN có định, YYYYY là 5 chữ số
^BN-\d{5}$
