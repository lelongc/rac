# CẨM NANG CẤP TỐC: HIỂU RÕ TOÀN BỘ MODEL & BỘ CÂU HỎI VẤN ĐÁP CỦA THẦY PHÚC

> **Đọc ngay trong 10-15 phút để chuẩn bị trả lời khi thầy xuống bàn hỏi!**  
> Thầy nói: *"Từ đây tới cuối học kỳ mình chỉ học cái model thôi"* vì **Model (Entity JPA)** chính là linh hồn của kiến trúc ORM (Object-Relational Mapping) kết nối Java với Cơ sở dữ liệu MySQL.

---

## PHẦN 1: BẢN CHẤT CỐT TỬ – TẠI SAO THẦY NÓI "CHỈ HỌC CÁI MODEL"?

1. **Hồi Giữa kỳ**: `Model` chỉ là các Class Java thường (POJO), chứa biến và hàm `getter/setter`. Dữ liệu chỉ lưu tạm trong RAM (`ArrayList`), tắt server là mất sạch.
2. **Hiện tại (Bài 7 & Đồ án cuối kỳ)**: `Model` được nâng cấp thành **`JPA ENTITY`**:
   - Mỗi **Class** trong Model $\longleftrightarrow$ Tương ứng với **1 Bảng** dưới CSDL MySQL (`@Table`).
   - Mỗi **Thuộc tính (Field)** $\longleftrightarrow$ Tương ứng với **1 Cột** trong bảng (`@Column`).
   - Mỗi **Đối tượng (Object)** $\longleftrightarrow$ Tương ứng với **1 Dòng dữ liệu (Record)**.
   - Các **Mối liên kết giữa các Class** $\longleftrightarrow$ Tương ứng với **Khóa ngoại & Quan hệ RDB** (`@OneToMany`, `@ManyToOne`, `@JoinColumn`).
👉 **Vì vậy**: Chỉ cần bạn khai báo đúng Model, **Hibernate sẽ tự động tạo bảng, tự tạo khóa ngoại, tự sinh câu lệnh SQL** mà bạn không cần phải gõ `CREATE TABLE` hay `SELECT * FROM...` thủ công!

---

## PHẦN 2: GIẢI THÍCH TỪNG DÒNG CODE TRONG 2 FILE MODEL

### 1. File `Department.java` (Bảng Cha – Đại diện cho 1 Phòng Ban)

```java
@Entity
@Table(name = "departments")
public class Department {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, length = 100)
    private String name;

    @OneToMany(mappedBy = "department", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
    @JsonIgnoreProperties("department")
    private List<Staff> staffs = new ArrayList<>();
```

* **`@Entity`**: Báo cho Spring Boot và Hibernate biết: *"Class này là một thực thể CSDL, hãy quản lý nó và map nó thành bảng trong MySQL!"*
* **`@Table(name = "departments")`**: Đặt tên bảng dưới MySQL là `departments` (viết thường, số nhiều). Nếu không có dòng này, Hibernate sẽ lấy tên Class `Department` làm tên bảng.
* **`@Id`**: Đánh dấu thuộc tính `id` chính là **Khóa chính (PRIMARY KEY)** của bảng.
* **`@GeneratedValue(strategy = GenerationType.IDENTITY)`**: Chỉ định cơ chế sinh ID tự động tăng. Trong MySQL, nó tương ứng với thuộc tính **`AUTO_INCREMENT`** (1, 2, 3, 4...).
* **`@Column(nullable = false, length = 100)`**: Cột `name` không được để trống (`NOT NULL`) và độ dài tối đa là 100 ký tự (`VARCHAR(100)`).
* **`@OneToMany(...)`**: Khai báo mối quan hệ **1 Phòng ban có Nhiều Nhân viên** ($1 - N$).
  * `mappedBy = "department"`: Báo rằng quyền quản lý khóa ngoại thuộc về biến `department` bên Class `Staff` (Department không giữ khóa ngoại).
  * `cascade = CascadeType.ALL`: Hiệu ứng dây chuyền. Khi xóa hoặc lưu 1 Department, tất cả các Staff thuộc phòng ban đó cũng được tự động xử lý theo.
  * `orphanRemoval = true`: Nếu một nhân viên bị xóa khỏi danh sách `staffs`, dòng đó dưới database cũng sẽ bị xóa luôn.
  * `fetch = FetchType.LAZY`: **Nạp lười (Lazy Loading)**. Khi lấy thông tin phòng ban, Hibernate chưa vội load danh sách nhân viên để tiết kiệm RAM; chỉ khi nào gọi `getStaffs()` thì mới truy vấn tiếp.
* **`@JsonIgnoreProperties("department")`**: **CỰC KỲ QUAN TRỌNG ĐỂ TRÁNH SẬP SERVER!** Chống vòng lặp vô tận (Infinite Loop). Ngăn việc Jackson biến đổi: Department gọi Staff $\rightarrow$ Staff lại gọi Department $\rightarrow$ lặp vô tận gây tràn bộ nhớ.

---

### 2. File `Staff.java` (Bảng Con – Đại diện cho 1 Nhân Viên)

```java
@Entity
@Table(name = "staffs")
public class Staff {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, length = 100)
    private String name;

    @Column(nullable = false, length = 150)
    private String email;

    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "department_id", nullable = false)
    @JsonIgnoreProperties({"staffs", "hibernateLazyInitializer"})
    private Department department;

    @Transient
    private Long departmentId;
```

* **`@ManyToOne(fetch = FetchType.EAGER)`**: Khai báo quan hệ **Nhiều Nhân viên thuộc về Một Phòng ban**.
  * `fetch = FetchType.EAGER`: **Nạp ngay lập tức**. Khi lấy 1 nhân viên thì tự động JOIN lấy luôn thông tin phòng ban của người đó.
* **`@JoinColumn(name = "department_id", nullable = false)`**: **ĐÂY CHÍNH LÀ KHÓA NGOẠI (FOREIGN KEY)!**
  * Hibernate sẽ tạo 1 cột tên là `department_id` trong bảng `staffs`.
  * Cột này liên kết trực tiếp tới khóa chính `id` của bảng `departments`.
* **`@Transient private Long departmentId;`**:
  * `@Transient` nghĩa là: *"Hibernate ơi, ĐỪNG tạo cột này trong CSDL!"*
  * **Tại sao cần nó?** Vì phía giao diện Web (Frontend JSON) thường gửi lên `{ "departmentId": 1 }`. Nhờ có biến này kèm getter/setter mà Spring Boot đọc được ID phòng ban do Web gửi lên một cách dễ dàng.

---

## PHẦN 3: BỘ CÂU HỎI VẤN ĐÁP CỦA THẦY & CÂU TRẢ LỜI MẪU ĂN TRỌN ĐIỂM

Dưới đây là 7 câu hỏi thầy Phúc rất hay hỏi sinh viên khi đứng kiểm tra tại máy:

---

### ❓ Câu 1: Em hãy chỉ cho thầy đâu là Khóa Chính, đâu là Khóa Ngoại trong 2 class Model này?
> **Trả lời mẫu**:  
> - Dạ thưa thầy, **Khóa chính** nằm ở thuộc tính `id` của cả 2 class, được đánh dấu bằng `@Id` và `@GeneratedValue(strategy = GenerationType.IDENTITY)` để tự tăng `AUTO_INCREMENT`.  
> - **Khóa ngoại** nằm ở thuộc tính `department` bên class `Staff`, được đánh dấu bằng `@ManyToOne` và `@JoinColumn(name = "department_id")`. Cột `department_id` này sẽ tham chiếu đến cột `id` của bảng `departments`.

---

### ❓ Câu 2: Tại sao quan hệ 1-N mà bên Department lại để `mappedBy = "department"`? Nếu bỏ `mappedBy` thì sao?
> **Trả lời mẫu**:  
> - Dạ thưa thầy, trong CSDL quan hệ, bảng N (`staffs`) là bên nắm giữ khóa ngoại trỏ về bảng 1 (`departments`).  
> - Từ khóa `mappedBy = "department"` khai báo rằng `Department` là bên bị động (Inverse side), nó nhường quyền quản trị mối quan hệ và khóa ngoại cho biến `department` bên class `Staff`.  
> - Nếu bỏ `mappedBy`, Hibernate sẽ hiểu nhầm đây là quan hệ độc lập và tự động tạo ra một **bảng trung gian thứ 3** (ví dụ `departments_staffs`), làm sai lệch cấu trúc CSDL chuẩn của mình.

---

### ❓ Câu 3: `@JsonIgnoreProperties` để làm gì? Nếu không có thì bị lỗi gì?
> **Trả lời mẫu**:  
> - Dạ thưa thầy, đây là annotation để **chống lỗi vòng lặp vô tận (Infinite Recursion)** khi chuyển đổi đối tượng sang chuỗi JSON (Serialization).  
> - Vì `Department` chứa danh sách `Staff`, mà mỗi `Staff` lại chứa ngược lại `Department`. Khi REST Controller biến đổi thành JSON trả về cho trình duyệt, nó sẽ lặp vô hạn giữa 2 đối tượng này dẫn đến lỗi **`StackOverflowError`** và làm sập ứng dụng.  
> - Khai báo `@JsonIgnoreProperties("department")` giúp ngắt vòng lặp: khi đọc nhân viên thì không lặp lại danh sách nhân viên của phòng ban đó nữa.

---

### ❓ Câu 4: Phân biệt `FetchType.LAZY` và `FetchType.EAGER`?
> **Trả lời mẫu**:  
> - **`FetchType.LAZY` (Nạp lười)**: Khi truy vấn đối tượng cha, dữ liệu của bảng con chưa được nạp ngay mà chỉ nạp khi nào code thực sự gọi đến hàm getter. Giúp tối ưu bộ nhớ, thường dùng cho danh sách nhiều phần tử (`@OneToMany`).  
> - **`FetchType.EAGER` (Nạp hăng hái / Nạp ngay)**: Khi truy vấn nhân viên, Hibernate sẽ dùng lệnh JOIN để lấy luôn thông tin phòng ban đi kèm ngay lập tức. Thường dùng cho quan hệ `@ManyToOne`.

---

### ❓ Câu 5: Thuộc tính `@Transient` dùng để làm gì?
> **Trả lời mẫu**:  
> - Dạ thưa thầy, `@Transient` dùng để đánh dấu một thuộc tính chỉ tồn tại trong bộ nhớ Java để xử lý logic hoặc nhận dữ liệu JSON từ Frontend, **hoàn toàn KHÔNG được tạo thành cột trong CSDL**.  
> - Ở đây em dùng `@Transient private Long departmentId;` để hứng trực tiếp số ID phòng ban mà file `index.html` gửi lên qua API, tránh việc Hibernate tạo thêm 1 cột trùng lặp với `department_id`.

---

### ❓ Câu 6: `cascade = CascadeType.ALL` có ý nghĩa thực tế như thế nào?
> **Trả lời mẫu**:  
> - Dạ thưa thầy, `Cascade` là tính năng lan truyền thao tác từ đối tượng cha sang đối tượng con.  
> - `CascadeType.ALL` bao gồm lưu (PERSIST), cập nhật (MERGE), và xóa (REMOVE). Ví dụ: Khi ta xóa một Phòng ban khỏi CSDL, tất cả nhân viên thuộc phòng ban đó cũng sẽ tự động bị xóa theo (tương đương với `ON DELETE CASCADE` trong SQL), giúp CSDL không bị lỗi mồ côi dữ liệu (Orphan records).

---

### ❓ Câu 7: Giờ thầy muốn thêm trường "Số điện thoại" cho nhân viên thì em sửa Model như thế nào?
> **Trả lời mẫu**:  
> 1. Em vào class `Staff.java`, thêm một dòng thuộc tính:  
>    `@Column(length = 15)`  
>    `private String phone;`  
> 2. Tạo thêm hàm `getPhone()` và `setPhone(String phone)`.  
> 3. Vì trong `application.properties` đã cấu hình `spring.jpa.hibernate.ddl-auto=update`, nên khi khởi động lại ứng dụng, Hibernate sẽ **tự động chạy lệnh `ALTER TABLE staffs ADD COLUMN phone...` xuống MySQL Clever Cloud** mà em không cần phải gõ lệnh SQL bằng tay.

---

## PHẦN 4: HÌNH DUNG NHANH SƠ ĐỒ TRỰC QUAN (VẼ NHÁP NẾU THẦY BẮT VẼ)

```
[Bảng DEPARTMENTS] (Bên 1 - Cha)
+ id (PK, Auto Increment)
+ name (Varchar 100)
       │
       │ 1
       │ có nhiều (OneToMany)
       │
       ▼ N
[Bảng STAFFS] (Bên N - Con)
+ id (PK, Auto Increment)
+ name (Varchar 100)
+ email (Varchar 150)
+ department_id (FK -> trỏ về departments.id)
```

---
*Tài liệu này được lưu tại: `d:\folder\rac\iuh\môn\hk1-4\cc-web-website-hld\truong\bt\t2\b7_department_staff_mysql\GIAI_THICH_CHI_TIET_MODEL_VA_BO_CAU_HOI_VAN_DAP.md`*  
*Bạn hãy mở đọc kỹ 7 câu hỏi vấn đáp ở Phần 3 để tự tin trả lời lưu loát khi thầy xuống kiểm tra!*
