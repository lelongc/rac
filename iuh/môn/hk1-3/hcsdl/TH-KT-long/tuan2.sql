
--Module 3. View
--1) Tạo view dbo.vw_Products hiển thị danh sách các sản phẩm từ bảng 
--Production.Product và bảng Production.ProductCostHistory. Thông tin bao gồm 
--ProductID, Name, Color, Size, Style, StandardCost, EndDate, StartDate
CREATE VIEW vw_Products AS
SELECT p.ProductID, Name, Color, Size, Style, h.StandardCost, EndDate
FROM Production.Product p JOIN Production.ProductCostHistory h on p.ProductID = h.ProductID
GO
--sử dụng
SELECT * FROM vw_Products
Go
--2) Tạo view List_Product_View chứa danh sách các sản phẩm có trên 500 đơn đặt 
--hàng trong quí 1 năm 2008 và có tổng trị giá >10000, thông tin gồm ProductID, 
--Product_Name, CountOfOrderID và SubTotal.
CREATE VIEW List_Product_View AS 
SELECT p.ProductID, Name as Product_Name, count(od.SalesOrderID) as CountOfOrderID,
sum(OrderQty*UnitPrice) as Subtotal
FROM Production.Product  p JOIN Sales.SalesOrderDetail od on p.ProductID = od.ProductID
JOIN Sales.SalesOrderHeader h on h.SalesOrderID = od.SalesOrderID
WHERE DATEPART(q, OrderDate) =1 and YEAR(OrderDate) = 2008
GROUP BY p.ProductID, Name
HAVING count(od.SalesOrderID) > 500 and sum(OrderQty*UnitPrice) >10000
GO
--sử dụng
SELECT * FROM List_Product_View
GO
--3) Tạo view dbo.vw_CustomerTotals hiển thị tổng tiền bán được (total sales) từ cột 
--TotalDue của mỗi khách hàng (customer) theo tháng và theo năm. Thông tin gồm 
--CustomerID, YEAR(OrderDate) AS OrderYear, MONTH(OrderDate) AS 
--OrderMonth, SUM(TotalDue).
CREATE VIEW vw_CustomerTotals  AS 
SELECT c.CustomerID, YEAR(OrderDate) as OrderYear , MONTH(OrderDate) as OrderMonth, SUM(TotalDue) as
TotalSales 
FROM [Sales].[Customer] c JOIN [Sales].[SalesOrderHeader] h on c.CustomerID = h.CustomerID
group by c.CustomerID, YEAR(OrderDate), MONTH(OrderDate) 
GO
--hiện thực view
SELECT * FROM vw_CustomerTotals
Go
--4) Tạo view trả về tổng số lượng sản phẩm (Total Quantity) bán được của mỗi nhân 
--viên theo từng năm. Thông tin gồm SalesPersonID, OrderYear, sumOfOrderQty
CREATE VIEW QuantityTotal AS
SELECT SalesPersonID, YEAR(OrderDate) as OrderYear,sum(OrderQty) as sumOfOrderQty
FROM [Sales].[SalesOrderHeader] h JOIN Sales.SalesOrderDetail od on h.SalesOrderID = od.SalesOrderID 
group by SalesPersonID, year(OrderDate)
Go
--hiện thực view
SELECT * FROM QuantityTotal
Go 

--5) Tạo view ListCustomer_view chứa danh sách các khách hàng có trên 25 hóa đơn 
--đặt hàng từ năm 2007 đến 2008, thông tin gồm mã khách (PersonID) , họ tên 
--(FirstName +' '+ LastName as FullName), Số hóa đơn (CountOfOrders).
CREATE VIEW ListCustomer_view AS 
SELECT  c.PersonID, FirstName + ' ' + LastName as FullName, Count(o.SalesOrderID) as CountOfOrders
FROM Person.Person p JOIN [Sales].[Customer] c on p.BusinessEntityID = c.PersonID
JOIN [Sales].[SalesOrderHeader] o on o.CustomerID = c.CustomerID
WHERE YEAR(OrderDate) >=2007 and YEAR(OrderDate) <=2008
GROUP BY  c.PersonID, FirstName ,LastName 
HAVING Count(o.SalesOrderID) > 25
Go
--hiện thực view 
SELECT * FROM ListCustomer_view
Go
--6) Tạo view ListProduct_view chứa danh sách những sản phẩm có tên bắt đầu với 
--‘Bike’ và ‘Sport’ có tổng số lượng bán trong mỗi năm trên 50 sản phẩm, thông 
--tin gồm ProductID, Name, SumOfOrderQty, Year. (dữ liệu lấy từ các bảng
--Sales.SalesOrderHeader, Sales.SalesOrderDetail, và
--Production.Product)
CREATE VIEW ListProduct_view AS
SELECT p.ProductID, Name, Sum(OrderQty) as SumOfOrderQty, year(OrderDate) as Year
FROM [Production].[Product] p JOIN [Sales].[SalesOrderDetail] od on p.ProductID = od.ProductID
JOIN [Sales].[SalesOrderHeader] h on h.SalesOrderID = od.SalesOrderID
WHERE Name like 'Bike%' OR Name like 'Sport%'
GROUP BY p.ProductID, Name, year(OrderDate)
HAVING Sum(OrderQty) > 50
GO
--hiện thực view 
SELECT * FROM ListProduct_view
Go
--7) Tạo view List_department_View chứa danh sách các phòng ban có lương (Rate: 
--lương theo giờ) trung bình >30, thông tin gồm Mã phòng ban (DepartmentID), 
--tên phòng ban (Name), Lương trung bình (AvgOfRate). Dữ liệu từ các bảng 
--[HumanResources].[Department], 
--[HumanResources].[EmployeeDepartmentHistory], 
--[HumanResources].[EmployeePayHistory].
CREATE VIEW List_department_view AS
SELECT d.DepartmentID, Name, Avg(Rate) as AvgOfRate
FROM [HumanResources].[Department] d JOIN [HumanResources].[EmployeeDepartmentHistory] dh on
d.DepartmentID = dh.DepartmentID
JOIN [HumanResources].[EmployeePayHistory] ph on ph.BusinessEntityID = dh.BusinessEntityID
GROUP BY d.DepartmentID, Name
HAVING Avg(Rate) >30
GO
--hiện thực view
SELECT * FROM List_department_view
Go
exec sp_helptext List_department_view
Go

--8) Tạo view Sales.vw_OrderSummary với từ khóa WITH ENCRYPTION gồm 
--OrderYear (năm của ngày lập), OrderMonth (tháng của ngày lập), OrderTotal 
--(tổng tiền). Sau đó xem thông tin và trợ giúp về mã lệnh của view này
CREATE VIEW vwOrderSummary 
WITH ENCRYPTION 
AS
SELECT YEAR(OrderDate) as OrderYear, MONTH(OrderDate) as OrderMonth, sum(OrderQty*UnitPrice) as
OrderTotal
FROM [Sales].[SalesOrderHeader] o JOIN [Sales].[SalesOrderDetail] od on o.SalesOrderID =
od.SalesOrderID
GROUP BY YEAR(OrderDate), MONTH(OrderDate)
GO
--hiện thực view
select * from vwOrderSummary 
Go
Exec sp_helptext vwOrderSummary  --Không xem được nội dung
Go

--9) Tạo view Production.vwProducts với từ khóa WITH SCHEMABINDING 
--gồm ProductID, Name, StartDate,EndDate,ListPrice của bảng Product và bảng 
--ProductCostHistory. Xem thông tin của View. Xóa cột ListPrice của bảng 
--Product. Có xóa được không? Vì sao?

CREATE VIEW Production.vwProducts 
WITH SCHEMABINDING 
AS
SELECT p.ProductID, Name, StartDate, EndDate, ListPrice
FROM [Production].[Product] p JOIN [Production].[ProductCostHistory] ch on p.ProductID = ch.ProductID
--hiện thực view
go
select * from Production.vwProducts 
--Xóa cột ListPrice của bảng Product:
alter table [Production].[Product]
drop  column ListPrice 

--Lỗi: The object 'vwProducts' is dependent on column 'ListPrice'.

--10) Tạo view view_Department với từ khóa WITH CHECK OPTION chỉ chứa các 
--phòng thuộc nhóm có tên (GroupName) là “Manufacturing” và “Quality 
--Assurance”, thông tin gồm: DepartmentID, Name, GroupName.

CREATE VIEW view_Department
AS
SELECT DepartmentID, Name, GroupName
FROM [HumanResources].[Department]
WHERE GroupName IN ('Manufacturing', 'Quality Assurance')
WITH CHECK OPTION
GO
--hiện thực view
select * from view_Department
select * from [HumanResources].[Department]
----------------------a. Chèn thêm một phòng ban mới thuộc nhóm không thuộc hai nhóm 
--“Manufacturing” và “Quality Assurance” thông qua view vừa tạo. Có 
--chèn được không? Giải thích.
--Xem dữ liệu hiện tại
select * from [HumanResources].[Department]  --16 rows
insert view_Department(Name, GroupName)  --bỏ qua DepartmentID có thuộc tính Identity
values('New Dept', 'Sales and Marketing') 
--lỗi: The attempted insert or update failed because the target view either specifies WITH CHECK OPTION 
--or spans a view.....
--Không chèn được. Vì view đã có thuộc tính WITH CHECK OPTION nên chỉ chèn được những phòng ban phù hợp 
--với điều kiện trong view (GroupName in ('Manufacturing', 'Quality Assurance')
------------------b. Chèn thêm một phòng mới thuộc nhóm “Manufacturing” và một 
--phòng thuộc nhóm “Quality Assurance”.
insert view_Department(Name, GroupName)
values('New Dept1', 'Manufacturing')
insert view_Department(Name, GroupName)
values('New Dept2', 'Quality Assurance')
--Chèn được vì dữ liệu chèn vào phù hợp với điều kiện của view (GroupName in ('Manufacturing', 'Quality Assurance')

-- c. Dùng câu lệnh Select xem kết quả trong bảng Departmen

select DepartmentID, Name, GroupName
from [HumanResources].[Department] --18 rows