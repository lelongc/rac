# Web Builder

Ứng dụng Web Builder cho phép bạn tạo ra các trang web form và bảng một cách nhanh chóng, với các tính năng kiểm tra đầu vào sử dụng biểu thức chính quy (regex) và hiển thị lỗi khi nhập liệu không hợp lệ.

## Tính năng

- Tạo form với nhiều loại trường nhập liệu: text, email, phone, date, radio, checkbox
- Thêm kiểm tra đầu vào với regex và thông báo lỗi tùy chỉnh
- Tự động tạo bảng để hiển thị dữ liệu đã nhập
- Tùy chỉnh màu sắc, vị trí và kích thước của các thành phần
- Xem trước trang web trước khi xuất mã
- Xuất mã HTML, CSS và JavaScript để triển khai trên web

## Cách sử dụng

### 1. Tùy chỉnh giao diện

- Thiết lập tiêu đề trang web
- Chọn màu nền và màu chữ cho header, form và footer
- Tùy chỉnh nội dung footer

### 2. Tạo các trường nhập liệu

- Chọn loại trường (text, email, phone, date, radio, checkbox)
- Nhập nhãn và ID cho trường
- Thêm placeholder và biểu thức regex cho việc kiểm tra
- Đánh dấu trường bắt buộc nếu cần
- Đối với radio và checkbox, thêm các tùy chọn

### 3. Sắp xếp các trường

- Sử dụng các nút mũi tên để di chuyển trường lên/xuống
- Xóa trường nếu cần

### 4. Xuất mã

- Xem trước trang web để kiểm tra giao diện
- Xuất mã HTML, CSS và JavaScript
- Tải xuống tất cả các file dưới dạng ZIP

## Biểu thức chính quy (Regex) phổ biến

Web Builder bao gồm các mẫu regex thường dùng:

- **Họ tên:** `^[A-Z][a-z]*(\s+[A-Z][a-z]*)+$` - Mỗi từ bắt đầu bằng chữ hoa
- **Số điện thoại:** `^(09|03|08)\d{8}$` - 10 số bắt đầu với 09, 03, 08
- **Định dạng điện thoại:** `^0\d{3}\.\d{3}\.\d{3}$` - Định dạng 0XXX.XXX.XXX
- **Email cơ bản:** `@.*\.com$` - Chứa @ và kết thúc với .com
- **Email chi tiết:** `^[a-zA-Z0-9_]{3,}@gmail\.com$` - name_email@gmail.com
- **Địa chỉ:** `^[A-Za-z0-9\/]+$` - Chỉ cho phép chữ, số và dấu /

## Cách trang web tạo ra hoạt động

1. Form kiểm tra đầu vào khi người dùng nhập liệu
2. Hiển thị thông báo lỗi nếu dữ liệu không hợp lệ
3. Khi người dùng gửi form hợp lệ, dữ liệu được thêm vào bảng
4. Form được reset để nhập dữ liệu mới
