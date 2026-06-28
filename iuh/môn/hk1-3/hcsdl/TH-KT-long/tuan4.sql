--Module 4. Batch, Stored Procedure, Function
--I) Batch
--1) Viết một batch khai báo biến @tongsoHD chứa tổng số hóa đơn của sản phẩm 
--có ProductID=’778’; nếu @tongsoHD>500 thì in ra chuỗi “Sản phẩm 778 có 
--trên 500 đơn hàng”, ngược lại thì in ra chuỗi “Sản phẩm 778 có ít đơn đặt
--hàng”
--Mỗi productID sẽ có tổng số hóa đơn
select ProductID, count(SalesOrderID) as TongHD
from  Sales.SalesOrderDetail
group by ProductID
go
--khai báo biến
declare @tongsoHD int , @maSP int
--gán giá trị cho biến
set @maSP = 778
--Cach 1
set @tongsoHD= (select count(SalesOrderID)
from  Sales.SalesOrderDetail
where ProductID = @maSP)
--Cach 2
--select @tongsoHD= count(SalesOrderID )
--              from Sales.SalesOrderDetail
--              where ProductID = @maSP
--In kết quả ra cửa sổ results - dùng select
select @maSP as MaSP , @tongsoHD as TongHD
--In kết quả ra cửa sổ Messages - dùng print
if @tongsoHD > 500
print N'Sản phẩm ' + cast(@maSP as char(4)) + N'Có trên 500 đơn hàng'
else
print N'Sản phẩm ' + cast(@maSP as char(4)) + N'Có ít đơn đặt hàng'
go
--2) Viết một đoạn Batch với tham số @makh và @n chứa số hóa đơn của khách 

--hàng @makh, tham số @nam chứa năm lập hóa đơn (ví dụ @nam=2008), nếu
--@n>0 thì in ra chuỗi: “Khách hàng @makh có @n hóa đơn trong năm 2008” 
--ngược lại nếu @n=0 thì in ra chuỗi “Khách hàng @makh không có hóa đơn nào 
--trong năm 2008”
--  tìm hiểu dữ liệu
select CustomerID, year(OrderDate) as Year
from Sales.SalesOrderHeader
where year(OrderDate) = 2008
--khai báo biến
declare @makh int, @n int, @nam int 
--gán giá trị cho biến
set @makh = 29825
set @nam = 2008
set @n = (select count(*)
from  Sales.SalesOrderHeader
where year( [OrderDate])= @nam and customerID=@makh)
--in kết quả
if @n >0
print N'Khách hàng ' + convert(  char(5),@makh) + N' có ' + convert(char(4) , @n) + ' hóa đơn trong 
năm ' + cast(@nam as char(4)) 
else
print N'Khách hàng ' + convert(  char(5),@makh) + ' không có hóa đơn nào trong năm '+
convert( char(4), @nam)
--3) Viết một batch tính số tiền giảm cho những hóa đơn (SalesOrderID) có tổng 
--tiền>100000, thông tin gồm [SalesOrderID], SubTotal=SUM([LineTotal]), 
--Discount (tiền giảm), với Discount được tính như sau:
--  Những hóa đơn có SubTotal<100000 thì không giảm,
--  SubTotal từ 100000 đến <120000 thì giảm 5% của SubTotal
--  SubTotal từ 120000 đến <150000 thì giảm 10% của SubTotal
--  SubTotal từ 150000 trở lên thì giảm 15% của SubTotal
--(Gợi ý: Dùng cấu trúc Case… When …Then …)
select SalesOrderID, SUM([LineTotal]) as Subotal, (
CASE
WHEN SUM([LineTotal]) < 100000 
THEN 0
WHEN SUM([LineTotal]) >= 100000 
AND SUM([LineTotal]) < 120000 THEN SUM([LineTotal]) * 0.05
WHEN SUM([LineTotal]) >= 120000 
AND SUM([LineTotal]) < 150000 THEN SUM([LineTotal]) * 0.1
ELSE SUM([LineTotal]) * 0.15
END) as Discount
FROM [Sales].[SalesOrderDetail]
GROUP BY SalesOrderID
HAVING SUM([LineTotal]) > 100000;

--4) Viết một Batch với 3 tham số: @masp, @mancc, @soluongcc, chứa giá trị của 
--các field [ProductID],[BusinessEntityID],[OnOrderQty], với giá trị truyền cho 
--các biến @mancc, @masp (vd: @mancc=1650, @masp=4), thì chương trình sẽ 
--gán giá trị tương ứng của field [OnOrderQty] cho biến @soluongcc, nếu
--@soluongcc trả về giá trị là null thì in ra chuỗi “Nhà cung cấp 1650 không cung 
--cấp sản phẩm 4”, ngược lại (vd: @soluongcc=5) thì in chuỗi “Nhà cung cấp 1650 
--cung cấp sản phẩm 4 với số lượng là 5”
--(Gợi ý: Dữ liệu lấy từ [Purchasing].[ProductVendor
--tim hieu du lieu


select [ProductID], [BusinessEntityID], [OnOrderQty]
from [Purchasing].[ProductVendor]
go
--khai bao bien
declare @masp int  , @mancc int ,@soluongcc int
--gan gia tri cho bien
--set @masp = 4 
--set @mancc = 1650
set @masp = 2
set @mancc = 1688
set @soluongcc = (
select  [OnOrderQty]
from [Purchasing].[ProductVendor]
where  [ProductID] = @masp  and  [BusinessEntityID] = @mancc 
)
--in ket qua 
if @soluongcc is null
print N'Nha cung cap ' + convert(char(4) , @mancc  ) + ' khong cung cap san pham ' + convert(
char(4),@masp)
else
print N'Nha cung cap ' + convert(char(4), @mancc) + ' cung cap san pham ' + convert( 
char(3),@masp)  + 'voi so luong la ' + convert(  char(5), @soluongcc)
--5) Viết một batch thực hiện tăng lương giờ (Rate) của nhân viên trong 
--[HumanResources].[EmployeePayHistory] theo điều kiện sau: Khi tổng lương 
--giờ của tất cả nhân viên Sum(Rate)<6000 thì cập nhật tăng lương giờ lên 10%, 
--nếu sau khi cập nhật mà lương giờ cao nhất của nhân viên >150 thì dừng.
--kiem tra du lieu
select [BusinessEntityID], [Rate] from [HumanResources].[EmployeePayHistory]
--viet batch
WHILE (SELECT SUM(rate) FROM
[HumanResources].[EmployeePayHistory])<6000 
BEGIN
UPDATE [HumanResources].[EmployeePayHistory] 
SET rate = rate*1.1
IF (SELECT MAX(rate)FROM
[HumanResources].[EmployeePayHistory]) > 150 
BREAK
ELSE
CONTINUE
END
--thuc thi
select [BusinessEntityID], [Rate] from [HumanResources].[EmployeePayHistory]