-- Tạo cơ sở dữ liệu
CREATE DATABASE SalesManagementSystem;

-- Sử dụng cơ sở dữ liệu
USE SalesManagementSystem;

-- Tạo bảng Employee
CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(50) NOT NULL,
    Phone VARCHAR(12),
    Username VARCHAR(30) NOT NULL UNIQUE,
    Password VARCHAR(255) NOT NULL,
    Role BOOLEAN DEFAULT 0, -- 1: Quản trị viên, 0: Nhân viên
    Image BLOB
);

-- Tạo bảng Customer
CREATE TABLE Customer (
    CustomerID CHAR(10) PRIMARY KEY NOT NULL,
    CompanyName VARCHAR(50) NOT NULL,
    Phone VARCHAR(12), -- Xóa CHECK constraint ở đây để tránh lỗi
    Address VARCHAR(60),
    Email VARCHAR(30) UNIQUE
);

-- Tạo bảng Category
CREATE TABLE Category (
    CategoryID INT PRIMARY KEY AUTO_INCREMENT,
    CategoryName VARCHAR(25) NOT NULL,
    Image BLOB
);

-- Tạo bảng Supplier
CREATE TABLE Supplier (
    SupplierID INT PRIMARY KEY AUTO_INCREMENT,
    SupplierName VARCHAR(50) NOT NULL,
    Phone VARCHAR(12),
    Address VARCHAR(60),
    Email VARCHAR(30)
);
-- Tạo bảng Product
CREATE TABLE Product (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,
    ProductName VARCHAR(50) NOT NULL,
    CategoryID INT NOT NULL,
    SupplierID INT NOT NULL,
    Price DECIMAL(19, 4) NOT NULL CHECK (Price > 0), -- Giá luôn lớn hơn 0
    Quantity INT NOT NULL CHECK (Quantity >= 0), -- Số lượng không âm
    Image BLOB,
    FOREIGN KEY (CategoryID) REFERENCES Category(CategoryID)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (SupplierID) REFERENCES Supplier(SupplierID)
        ON DELETE CASCADE ON UPDATE CASCADE
);
-- Tạo bảng Orders
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,
    CustomerID CHAR(10) NOT NULL,
    EmployeeID INT NOT NULL,
    OrderDate DATE NOT NULL,
    TotalAmount DECIMAL(19, 4) NOT NULL CHECK (TotalAmount > 0), -- Tổng tiền lớn hơn 0
    OrderStatus ENUM('Processing', 'Completed', 'Cancelled') NOT NULL COMMENT 'Trạng thái đơn hàng',
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
        ON DELETE RESTRICT ON UPDATE CASCADE -- Thay đổi thành RESTRICT để ngăn việc xóa nhân viên khi có đơn hàng liên quan
);

-- Tạo bảng OrderDetail
CREATE TABLE OrderDetail (
    OrderID INT NOT NULL,
    ProductID INT NOT NULL,
    Quantity SMALLINT NOT NULL CHECK (Quantity > 0), -- Số lượng phải lớn hơn 0
    UnitPrice DECIMAL(19, 4) NOT NULL CHECK (UnitPrice > 0), -- Giá đơn vị phải lớn hơn 0
    PRIMARY KEY (OrderID, ProductID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- Xem tất cả các bảng trong cơ sở dữ liệu
SHOW TABLES;


-- Chèn mẫu tin
-- Dữ liệu cho bảng Employee
INSERT INTO Employee (Name, Phone, Username, Password, Role, Image) VALUES
('Nguyễn Văn A', '0123456789', 'nva', 'password123', 0, NULL),
('Trần Thị B', '0987654321', 'ttb', 'password456', 1, NULL),
('Lê Văn C', '0912345678', 'lvc', 'password789', 0, NULL),
('Phạm Thị D', '0923456789', 'ptd', 'password321', 0, NULL),
('Nguyễn Thị E', '0934567890', 'nte', 'password654', 1, NULL);

-- Dữ liệu cho bảng Customer
INSERT INTO Customer (CustomerID, CompanyName, Phone, Address, Email) VALUES
('C001', 'Công ty A', '0123456789', 'Địa chỉ A', 'contact@companya.com'),
('C002', 'Công ty B', '0987654321', 'Địa chỉ B', 'contact@companyb.com'),
('C003', 'Công ty C', '0912345678', 'Địa chỉ C', 'contact@companyc.com'),
('C004', 'Công ty D', '0923456789', 'Địa chỉ D', 'contact@companyd.com'),
('C005', 'Công ty E', '0934567890', 'Địa chỉ E', 'contact@companye.com');

-- Dữ liệu cho bảng Category
INSERT INTO Category (CategoryName, Image) VALUES
('Điện tử', NULL),
('Thời trang', NULL),
('Thực phẩm', NULL),
('Sách', NULL),
('Đồ gia dụng', NULL);

-- Dữ liệu cho bảng Supplier
INSERT INTO Supplier (SupplierName, Phone, Address, Email) VALUES
('Nhà cung cấp A', '0123456789', 'Địa chỉ NCC A', 'suppliera@domain.com'),
('Nhà cung cấp B', '0987654321', 'Địa chỉ NCC B', 'supplierb@domain.com'),
('Nhà cung cấp C', '0912345678', 'Địa chỉ NCC C', 'supplierc@domain.com'),
('Nhà cung cấp D', '0923456789', 'Địa chỉ NCC D', 'supplierd@domain.com'),
('Nhà cung cấp E', '0934567890', 'Địa chỉ NCC E', 'supplidere@domain.com');

-- Dữ liệu cho bảng Product
INSERT INTO Product (ProductName, CategoryID, SupplierID, Price, Quantity, Image) VALUES
('Sản phẩm A', 1, 1, 100000, 50, NULL),
('Sản phẩm B', 2, 2, 200000, 30, NULL),
('Sản phẩm C', 3, 3, 150000, 20, NULL),
('Sản phẩm D', 4, 4, 300000, 10, NULL),
('Sản phẩm E', 5, 5, 50000, 100, NULL);

-- Dữ liệu cho bảng Orders
INSERT INTO Orders (CustomerID, EmployeeID, OrderDate, TotalAmount, OrderStatus) VALUES
('C001', 1, '2024-10-01', 250000, 'Processing'),
('C002', 2, '2024-10-02', 150000, 'Completed'),
('C003', 1, '2024-10-03', 300000, 'Cancelled'),
('C004', 2, '2024-10-04', 400000, 'Processing'),
('C005', 3, '2024-10-05', 50000, 'Completed');

-- Dữ liệu cho bảng OrderDetail
INSERT INTO OrderDetail (OrderID, ProductID, Quantity, UnitPrice) VALUES
(1, 1, 2, 100000), -- Đơn hàng 1, sản phẩm A
(1, 2, 1, 200000), -- Đơn hàng 1, sản phẩm B
(2, 3, 1, 150000), -- Đơn hàng 2, sản phẩm C
(3, 4, 2, 300000), -- Đơn categorycategorycategorycategorycategoryhàng 3, sản phẩm D
(4, 5, 3, 50000);  -- Đơn hàng 4, sản phẩm E

-- Xem dữ liệu của bảng Employee
SELECT * FROM Employee;

-- Xem dữ liệu của bảng Customer
SELECT * FROM Customer;

-- Xem dữ liệu của bảng Product
SELECT * FROM Product;

-- Xem dữ liệu của bảng Orders
SELECT * FROM Orders;

-- Xem dữ liệu của bảng OrderDetail
SELECT * FROM OrderDetail;
