CREATE DATABASE SmartSellerDB;
USE SmartSellerDB;

-- Bảng Employee
CREATE TABLE Employee (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Phone VARCHAR(12) NOT NULL UNIQUE,
    Username VARCHAR(30) NOT NULL UNIQUE,
    Password VARCHAR(255) NOT NULL,
    Role BOOLEAN DEFAULT FALSE COMMENT 'FALSE = Employee, TRUE = Admin',
    Image LONGBLOB,
    Gender BOOLEAN COMMENT 'TRUE = Male, FALSE = Female',
    DateOfBirth DATE NOT NULL,
    Email VARCHAR(50) NOT NULL UNIQUE,
    Status ENUM('Active', 'Inactive', 'OnLeave') DEFAULT 'Active',
    HireDate DATE NOT NULL,
    Salary DECIMAL(10, 2),
    Position VARCHAR(30)
);

-- Bảng Customer
CREATE TABLE Customer (
    CustomerID VARCHAR(10) PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Phone VARCHAR(12) NOT NULL UNIQUE,
    Address VARCHAR(60),
    Email VARCHAR(50) NOT NULL UNIQUE,
    Account VARCHAR(30) NOT NULL UNIQUE,
    Password VARCHAR(255) NOT NULL,
    Image LONGBLOB,
    TotalSpend DOUBLE DEFAULT 0
);

-- Bảng Category
CREATE TABLE Category (
    CategoryID INT AUTO_INCREMENT PRIMARY KEY,
    CategoryName VARCHAR(30) NOT NULL
);

-- Bảng Supplier
CREATE TABLE Supplier (
    SupplierID INT AUTO_INCREMENT PRIMARY KEY,
    SupplierName VARCHAR(50) NOT NULL,
    Phone VARCHAR(12) NOT NULL UNIQUE,
    Address VARCHAR(60),
    Email VARCHAR(50) NOT NULL UNIQUE
);

-- Bảng Product
CREATE TABLE Product (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,
    ProductName VARCHAR(50) NOT NULL,
    CategoryID INT NOT NULL,
    SupplierID INT NOT NULL,
    Price DOUBLE NOT NULL,
    Quantity INT NOT NULL,
    CreateDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    UpdateDate DATETIME ON UPDATE CURRENT_TIMESTAMP,
    Discount DOUBLE DEFAULT 0,
    FOREIGN KEY (CategoryID) REFERENCES Category(CategoryID) ON DELETE CASCADE,
    FOREIGN KEY (SupplierID) REFERENCES Supplier(SupplierID) ON DELETE CASCADE
);

-- Bảng Image
CREATE TABLE Image (
    ImageID INT AUTO_INCREMENT PRIMARY KEY,
    ImageData LONGBLOB NOT NULL,
    ProductID INT NOT NULL,
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID) ON DELETE CASCADE
);

-- Bảng Order
CREATE TABLE Orders (
    OrderID INT AUTO_INCREMENT PRIMARY KEY,
    CustomerID VARCHAR(10) NOT NULL,
    EmployeeID INT,
    OrderDate DATE NOT NULL,
    TotalAmount DOUBLE NOT NULL,
    OrderStatus ENUM('Processing', 'Delivering', 'Completed', 'Cancelled') DEFAULT 'Processing',
    PaymentType ENUM('COD', 'Card', 'BankTransfer') DEFAULT 'COD',
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID) ON DELETE SET NULL
);

-- Bảng OrderDetail
CREATE TABLE OrderDetail (
    OrderID INT NOT NULL,
    ProductID INT NOT NULL,
    Quantity SMALLINT NOT NULL,
    UnitPrice DOUBLE NOT NULL,
    TotalPrice DOUBLE GENERATED ALWAYS AS (Quantity * UnitPrice) STORED,
    PRIMARY KEY (OrderID, ProductID),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID) ON DELETE CASCADE
);
