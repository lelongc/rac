
USE AdventureWorks2008R2
GO
SELECT *
FROM Sales.SalesOrderHeader
GO
-- 1. Tạo một Instead of trigger thực hiện trên view. Thực hiện theo các bước sau:
-- Tạo mới 2 bảng M_Employees và M_Department theo cấu trúc sau: 
-- create table M_Department
-- (
--  DepartmentID int not null primary key, 
--  Name nvarchar(50),
--  GroupName nvarchar(50) 
-- )
-- create table M_Employees 
-- (
--  EmployeeID int not null primary key, 
--  Firstname nvarchar(50),
--  MiddleName nvarchar(50), 
--  LastName nvarchar(50),
--  DepartmentID int foreign key references M_Department(DepartmentID) 
-- ) 
-- Tạo một view tên EmpDepart_View bao gồm các field: EmployeeID,
-- FirstName, MiddleName, LastName, DepartmentID, Name, GroupName, dựa 
-- trên 2 bảng M_Employees và M_Department.
-- Tạo một trigger tên InsteadOf_Trigger thực hiện trên view
-- EmpDepart_View, dùng để chèn dữ liệu vào các bảng M_Employees và 
-- M_Department khi chèn một record mới thông qua view EmpDepart_View.
-- Dữ liệu test:
-- insert EmpDepart_view values(1, 'Nguyen','Hoang','Huy', 11,'Marketing','Sales')
-- tạo table 
CREATE TABLE M_Department
(
DepartmentID INT NOT NULL PRIMARY KEY,
Name NVARCHAR(50),
GroupName NVARCHAR(50)
)
CREATE TABLE M_Employees
(
EmployeeID INT NOT NULL PRIMARY KEY,
Firstname NVARCHAR(50),
MiddleName NVARCHAR(50),
LastName NVARCHAR(50),
DepartmentID INT FOREIGN KEY REFERENCES M_Department(DepartmentID)
)
GO
-- tạo view
CREATE VIEW EmpDepart_View
AS
SELECT e.EmployeeID, e.FirstName, e.MiddleName, e.LastName,
d.DepartmentID, d.Name, d.GroupName
FROM M_Department AS d JOIN M_Employees AS e
ON d.DepartmentID = e.DepartmentID
GO

-- tạo trigger
CREATE TRIGGER insteadof_trigger ON EmpDepart_View
instead OF INSERT
AS 
BEGIN
INSERT M_Department
SELECT DepartmentID, Name, groupName
FROM inserted
INSERT M_Employees
SELECT EmployeeID, FirstName, MiddleName, LastName, DepartmentID
FROM inserted
END
GO
-- test trigger
SELECT *
FROM EmpDepart_View
INSERT EmpDepart_view
VALUES(1, 'Nguyen', 'Hoang', 'Huy', 11, 'Marketing', 'Sales')
SELECT *
FROM M_Department
SELECT *
FROM M_Employees
DROP VIEW dbo.EmpDepart_View
DROP TRIGGER dbo.insteadof_trigger
DROP TABLE dbo.M_Department
DROP TABLE dbo.M_Employees

-- 2. Tạo một trigger thực hiện trên bảng MySalesOrders có chức năng thiết lập độ ưu 
-- tiên của khách hàng (CustPriority) khi người dùng thực hiện các thao tác Insert, 
-- Update và Delete trên bảng MySalesOrders theo điều kiện như sau:
-- Nếu tổng tiền Sum(SubTotal) của khách hàng dưới 10,000 $ thì độ ưu tiên của 
-- khách hàng (CustPriority) là 3 Nếu tổng tiền Sum(SubTotal) của khách hàng từ 10,000 $ đến dưới 50000 $ 
-- thì độ ưu tiên của khách hàng (CustPriority) là 2 Nếu tổng tiền Sum(SubTotal) của khách hàng từ 50000 $ trở lên thì độ ưu tiên 
-- của khách hàng (CustPriority) là 1
-- Các bước thực hiện:
-- Tạo bảng MCustomers và MSalesOrders theo cấu trúc 
-- sau: create table MCustomer
-- ( 
--    CustomerID int not null primary key, 
--    CustPriority int
-- )
-- create table MSalesOrders 
-- (
--    SalesOrderID int not null primary key, 
--    OrderDate date,
--    SubTotal money, CustomerID int foreign key references MCustomer(CustomerID) 
--  )
-- Chèn dữ liệu cho bảng MCustomers, lấy dữ liệu từ bảng Sales.Customer, 
-- nhưng chỉ lấy CustomerID>30100 và CustomerID<30118, cột CustPriority cho 
-- giá trị null.
-- Chèn dữ liệu cho bảng MSalesOrders, lấy dữ liệu từ bảng
-- Sales.SalesOrderHeader, chỉ lấy những hóa đơn của khách hàng có trong bảng 
-- khách hàng.
-- Viết trigger để lấy dữ liệu từ 2 bảng inserted và deleted.
-- Viết câu lệnh kiểm tra việc thực thi của trigger vừa tạo bằng cách chèn thêm hoặc 
-- xóa hoặc update một record trên bảng MSalesOrders
-- tạo table
CREATE TABLE MCustomer
(
CustomerID INT NOT NULL PRIMARY KEY,
CustPriority INT
)
CREATE TABLE MSalesOrders
(
SalesOrderID INT NOT NULL PRIMARY KEY,
OrderDate DATE,
SubTotal MONEY,
CustomerID INT FOREIGN KEY REFERENCES MCustomer(CustomerID)
)
GO
-- chèn dữ liệu
INSERT INTO MCustomer
(CustomerID, CustPriority)
SELECT sc.CustomerID, NULL
FROM Sales.Customer AS sc
WHERE sc.CustomerID BETWEEN 30101 AND 30117







