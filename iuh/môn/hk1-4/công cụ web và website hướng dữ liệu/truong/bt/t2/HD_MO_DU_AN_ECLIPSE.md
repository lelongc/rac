# HƯỚNG DẪN MỞ VÀ CHẠY DỰ ÁN JAVA TRONG ECLIPSE IDE

Tài liệu này hướng dẫn bạn **2 cách** mở và chạy dự án mẫu Java tại thư mục `t2` trên phần mềm **Eclipse IDE**.

---

## 🚀 CÁCH 1: Import dự án có sẵn vào Eclipse (Nhanh & Khuyên dùng)

### **Bước 1: Mở Eclipse IDE**
Mở phần mềm Eclipse và chọn Workspace làm việc của bạn.

### **Bước 2: Mở cửa sổ Import**
Trên thanh menu trên cùng, chọn **File** ➔ **Import...**

### **Bước 3: Chọn kiểu Import**
* Trong danh sách hiện ra, mở thư mục **General**.
* Chọn dòng **Existing Projects into Workspace**.
* Nhấn nút **Next**.

### **Bước 4: Trỏ đường dẫn đến thư mục dự án**
* Tích chọn mục **Select root directory**.
* Nhấn nút **Browse...** và tìm chọn đến thư mục:
  `D:\folder\rac\iuh\môn\hk1-4\công cụ web và website hướng dữ liệu\truong\bt\t2`
* Eclipse sẽ tự động nhận diện dự án tên là `t2`.

### **Bước 5: Hoàn tất Import**
* Đảm bảo ô vuông trước dự án `t2` đã được tích chọn.
* Nhấn nút **Finish**.

### **Bước 6: Chạy chương trình**
* Trong cửa sổ **Package Explorer** bên trái, mở cây thư mục:
  `t2` ➔ `src` ➔ `firstoop` ➔ nhấp đúp chuột mở file **`App.java`**.
* Nhấp chuột phải vào màn hình code của `App.java` chọn **Run As** ➔ **Java Application** (hoặc nhấn phím tắt `Ctrl + F11`).
* Kết quả chạy sẽ hiển thị ở bảng **Console** phía dưới.

---

## 🛠️ CÁCH 2: Tạo Java Project mới trong Eclipse rồi chép code vào

Nếu dự án của bạn chưa có file cấu hình Eclipse (`.project`, `.classpath`), bạn làm theo các bước sau:

### **Bước 1: Tạo Java Project mới**
* Vào menu **File** ➔ **New** ➔ **Java Project**.
* Nhập **Project name**: `t2` (hoặc tên tùy ý).
* *(Lưu ý)*: Nếu Eclipse hỏi tạo `module-info.java`, bạn chọn **Don't Create**.
* Nhấn **Finish**.

### **Bước 2: Tạo Package**
* Trong cửa sổ Package Explorer, nhấp chuột phải vào thư mục **`src`**.
* Chọn **New** ➔ **Package**.
* Nhập tên Package: **`firstoop`** ➔ Nhấn **Finish**.

### **Bước 3: Thêm các file Java vào Package**
* Tạo lần lượt từng lớp bằng cách nhấp chuột phải vào package `firstoop` vừa tạo ➔ **New** ➔ **Class**:
  1. `Person.java`
  2. `Student.java`
  3. `Teacher.java`
  4. `PersonManagement.java`
  5. `Functional.java`
  6. `App.java`
* Copy nội dung mã nguồn tương ứng đã viết sẵn vào từng file.

### **Bước 4: Chạy thử**
Mở file `App.java`, nhấp chuột phải chọn **Run As** ➔ **Java Application**.

---

## 📁 CẤU TRÚC THƯ MỤC DỰ ÁN MẪU `t2`:
```text
t2/
├── .project                   # File cấu hình dự án Eclipse
├── .classpath                 # File cấu hình đường dẫn biên dịch Eclipse
├── HD_MO_DU_AN_ECLIPSE.md     # Tài liệu hướng dẫn này
└── src/
    └── firstoop/              # Package chứa mã nguồn OOP
        ├── Person.java        # Lớp cha Person
        ├── Student.java       # Lớp con Student (kế thừa Person)
        ├── Teacher.java       # Lớp con Teacher (kế thừa Person)
        ├── PersonManagement.java # Lớp quản lý danh sách
        ├── Functional.java    # Lớp xử lý chức năng
        └── App.java           # Lớp chứa hàm main() để chạy
```
