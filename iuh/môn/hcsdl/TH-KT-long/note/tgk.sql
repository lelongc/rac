--c1-patch
SELECT  CustomerID, SalesOrderID, OrderDate, TotalDue
FROM Sales.SalesOrderHeader


DECLARE @CustomerID INT = 29825;   
DECLARE @TotalOrders INT;
DECLARE @TotalAmount MONEY;
DECLARE @AvgAmount MONEY;

SELECT 
    @TotalOrders = COUNT(SalesOrderID),
    @TotalAmount = SUM(TotalDue),
    @AvgAmount   = AVG(TotalDue)
FROM Sales.SalesOrderHeader h
JOIN Sales.Customer c ON h.CustomerID = c.CustomerID
WHERE h.CustomerID = @CustomerID;

IF @TotalOrders IS NULL OR @TotalOrders = 0
    PRINT N'Không có đơn hàng nào cho khách hàng ' + CAST(@CustomerID AS NVARCHAR(10));
ELSE
    PRINT N'Khách hàng ' + CAST(@CustomerID AS NVARCHAR(10)) 
        + N' đã thực hiện ' + CAST(@TotalOrders AS NVARCHAR(10)) 
        + N' đơn hàng, tổng thanh toán là ' + CAST(@TotalAmount AS NVARCHAR(20)) 
        + N', trung bình mỗi đơn hàng là ' + CAST(@AvgAmount AS NVARCHAR(20));
go

-- c2 -store-procedure
CREATE PROCEDURE usp_DonHangKhachHang
    @CustomerID INT,
    @OrderYear INT
AS
BEGIN
    SET NOCOUNT ON;

    IF EXISTS (
        SELECT 1 
        FROM Sales.SalesOrderHeader h
        WHERE h.CustomerID = @CustomerID
          AND YEAR(h.OrderDate) = @OrderYear
    )
    BEGIN
        SELECT 
            h.SalesOrderID,
            h.OrderDate,
            h.TotalDue
        FROM Sales.SalesOrderHeader h
        JOIN Sales.Customer c ON h.CustomerID = c.CustomerID
        WHERE h.CustomerID = @CustomerID
          AND YEAR(h.OrderDate) = @OrderYear;
    END
    ELSE
    BEGIN
        PRINT N'Không có đơn hàng nào cho khách hàng ' 
              + CAST(@CustomerID AS NVARCHAR(10)) 
              + N' trong năm ' + CAST(@OrderYear AS NVARCHAR(10));
        SELECT 0 AS SalesOrderID, NULL AS OrderDate, 0 AS TotalDue;
    END
END;

--b exec 
DECLARE @CusID INT = 29825;
EXEC usp_DonHangKhachHang @CusID, 2008;

SET @CusID = 17753;
EXEC usp_DonHangKhachHang @CusID, 2005;
go

--c3 func 

SELECT *
    FROM Sales.SalesOrderHeader h
    JOIN Sales.SalesPerson sp ON h.SalesPersonID = sp.BusinessEntityID
    WHERE h.SalesPersonID = 279;


CREATE FUNCTION ufn_DoanhThuNhanVien(@SalesPersonID INT)
RETURNS MONEY
AS
BEGIN
    DECLARE @Total MONEY;

    SELECT @Total = SUM(h.TotalDue)
    FROM Sales.SalesOrderHeader h
    JOIN Sales.SalesPerson sp ON h.SalesPersonID = sp.BusinessEntityID
    WHERE h.SalesPersonID = @SalesPersonID;

    IF @Total IS NULL
        SET @Total = 0;

    RETURN @Total;
END;
go


DECLARE @EmpID INT = 279;  -- giả sử nhân viên này có nhiều đơn hàng
SELECT dbo.ufn_DoanhThuNhanVien(@EmpID) AS DoanhThuNhanVien;
