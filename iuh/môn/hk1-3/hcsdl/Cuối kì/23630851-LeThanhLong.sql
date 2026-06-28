--c1 
--a
USE [master]
GO
CREATE LOGIN [NV1] WITH PASSWORD=N'P@ssw0rd123', DEFAULT_DATABASE=[AdventureWorks2008R2]
GO
CREATE LOGIN [NV2] WITH PASSWORD=N'P@ssw0rd123', DEFAULT_DATABASE=[AdventureWorks2008R2]
GO
CREATE LOGIN [QL] WITH PASSWORD=N'P@ssw0rd123', DEFAULT_DATABASE=[AdventureWorks2008R2]
GO

SELECT * 
FROM SYS.SQL_LOGINS 

USE [AdventureWorks2008R2]
GO
CREATE USER [NV1] FOR LOGIN [NV1]
GO
CREATE USER [NV2] FOR LOGIN [NV2]
GO
CREATE USER [QL] FOR LOGIN [QL]
GO
--b

USE [AdventureWorks2008R2]
GO
CREATE ROLE [NhanVien]
GO

GRANT DELETE, INSERT, SELECT, UPDATE ON [HumanResources].[EmployeeDepartmentHistory] TO [NhanVien]
GO

ALTER ROLE [NhanVien] ADD MEMBER [NV1]
GO
ALTER ROLE [NhanVien] ADD MEMBER [NV2]
GO
ALTER ROLE [db_datareader] ADD MEMBER [QL]
GO
--c
--23630851
--nv1
    UPDATE HumanResources.EmployeeDepartmentHistory
    SET ModifiedDate = GETDATE()
    WHERE BusinessEntityID = 51;

   

--nv2

    USE AdventureWorks2008R2;
    DELETE FROM HumanResources.EmployeeDepartmentHistory
    WHERE BusinessEntityID = 21; 

   
--ql
    USE AdventureWorks2008R2;
   
    SELECT * FROM HumanResources.EmployeeDepartmentHistory WHERE BusinessEntityID = 51;
  
    SELECT * FROM HumanResources.EmployeeDepartmentHistory WHERE BusinessEntityID = 23;
  
    SELECT * FROM HumanResources.Department;
-- cau d 
-- ql xem được HumanResources.Employee vì thuộc role db_datareader . Nó cấp cho user toàn bộ quyền đọc  trên tất cả các bảng và view trong cơ sở dữ liệu , nv1 nv2 không xem được do k có quyền đó mà chỉ có quyền đọc trên bảng mà role nhanvien tác động được  
SELECT TOP 10 * FROM HumanResources.Employee;

--cau e 
USE [AdventureWorks2008R2]
GO

REVOKE DELETE, INSERT, SELECT, UPDATE ON [HumanResources].[EmployeeDepartmentHistory] FROM [NhanVien]
GO


ALTER ROLE [NhanVien] DROP MEMBER [NV1]
GO
ALTER ROLE [NhanVien] DROP MEMBER [NV2]
GO


ALTER ROLE [db_datareader] DROP MEMBER [QL]
GO


DROP ROLE [NhanVien]
GO
--cau 2 
--cau a 
ALTER DATABASE [AdventureWorks2008R2] SET RECOVERY FULL


USE AdventureWorks2008R2;
GO

SELECT *
FROM HumanResources.EmployeeDepartmentHistory

-- truoc khi tang luong 
SELECT 
    eph.BusinessEntityID, 
    edh.ShiftID,
    eph.Rate
FROM 
    HumanResources.EmployeePayHistory AS eph
JOIN 
    HumanResources.EmployeeDepartmentHistory AS edh 
    ON eph.BusinessEntityID = edh.BusinessEntityID
WHERE 
    edh.ShiftID IN (2, 3) 
ORDER BY
    edh.ShiftID, eph.BusinessEntityID;
GO

    BEGIN TRANSACTION;
     
    UPDATE HumanResources.EmployeePayHistory
    SET Rate = Rate * 1.10
    WHERE BusinessEntityID IN (SELECT BusinessEntityID FROM HumanResources.EmployeeDepartmentHistory WHERE ShiftID = 2);
     
    UPDATE HumanResources.EmployeePayHistory
    SET Rate = Rate * 1.20
    WHERE BusinessEntityID IN (SELECT BusinessEntityID FROM HumanResources.EmployeeDepartmentHistory WHERE ShiftID = 3);
    COMMIT TRANSACTION;

	   -- BEGIN TRANSACTION;
     
    --UPDATE HumanResources.EmployeePayHistory
    --SET Rate = Rate * 1.10
    --WHERE BusinessEntityID IN (SELECT BusinessEntityID FROM HumanResources.EmployeeDepartmentHistory WHERE ShiftID = 1 and [DepartmentID] in (1,3,5) );
     
    --UPDATE HumanResources.EmployeePayHistory
    --SET Rate = Rate * 1.20
    --WHERE BusinessEntityID IN (SELECT BusinessEntityID FROM HumanResources.EmployeeDepartmentHistory WHERE ShiftID = 3);
    --COMMIT TRANSACTION;

-- sau cap nhat 
SELECT 
    eph.BusinessEntityID, 
    edh.ShiftID,
    eph.Rate
FROM 
    HumanResources.EmployeePayHistory AS eph
JOIN 
    HumanResources.EmployeeDepartmentHistory AS edh 
    ON eph.BusinessEntityID = edh.BusinessEntityID
WHERE 
    edh.ShiftID IN (2, 3) 
ORDER BY
    edh.ShiftID, eph.BusinessEntityID;
GO



BACKUP DATABASE [AdventureWorks2008R2] 
TO DISK = N'D:\Backup\backup-full.bak' 
WITH INIT
GO
--cau b 
    USE AdventureWorks2008R2;
	--truoc
    SELECT COUNT(*) AS SoLuongDong FROM Production.ProductCostHistory;

    DELETE FROM Production.ProductCostHistory;

     --sau 
    SELECT COUNT(*) AS SoLuongDong FROM Production.ProductCostHistory;


BACKUP DATABASE [AdventureWorks2008R2] TO  DISK = N'D:\Backup\backup-diff.bak' WITH  DIFFERENTIAL
GO
--cau c 
    USE AdventureWorks2008R2;
     --truoc
   
    SELECT * FROM Person.PersonPhone WHERE BusinessEntityID = 0851;

  
    INSERT INTO Person.PersonPhone (BusinessEntityID, PhoneNumber, PhoneNumberTypeID, ModifiedDate)
    VALUES (0851, '0909-123-456', 1, GETDATE()); 

	--sau 

    SELECT * FROM Person.PersonPhone WHERE BusinessEntityID = 0851;



BACKUP LOG [AdventureWorks2008R2] TO  DISK = N'D:\Backup\backup-log.bak' WITH INIT
GO

--cau d 

USE [master]
drop database AdventureWorks2008R2 



RESTORE DATABASE [AdventureWorks2008R2] 
FROM  DISK = N'D:\Backup\backup-full.bak' 
WITH  FILE = 1,  NORECOVERY
GO

RESTORE DATABASE [AdventureWorks2008R2] 
FROM  DISK = N'D:\Backup\backup-diff.bak' 
WITH  FILE = 1,  NORECOVERY
GO

RESTORE LOG [AdventureWorks2008R2] 
FROM  DISK = N'D:\Backup\backup-log.bak' 
WITH  FILE = 1,  RECOVERY
GO


-- kiem tra sau restoe 
USE AdventureWorks2008R2;

	-- luong sau 
SELECT 
    eph.BusinessEntityID, 
    edh.ShiftID,
    eph.Rate
FROM 
    HumanResources.EmployeePayHistory AS eph
JOIN 
    HumanResources.EmployeeDepartmentHistory AS edh 
    ON eph.BusinessEntityID = edh.BusinessEntityID
WHERE 
    edh.ShiftID IN (2, 3)
ORDER BY
    edh.ShiftID, eph.BusinessEntityID;
GO

-- bang da xoa 
	SELECT COUNT(*) AS SoLuongDong FROM Production.ProductCostHistory;
-- sdt da them 
    SELECT * FROM Person.PersonPhone WHERE BusinessEntityID = 0851;
--cau 3 

USE [AdventureWorks2008R2]
GO

CREATE TRIGGER TR_ProductReview_OnUpdateComments
ON Production.ProductReview
AFTER UPDATE 
AS
BEGIN
    SET NOCOUNT ON; 
    IF UPDATE(Comments)
    BEGIN
        
        DECLARE @ProductID INT;
        DECLARE @Rating INT;
        DECLARE @Comments NVARCHAR(384);

        
        SELECT 
            @ProductID = i.ProductID,
            @Rating = i.Rating,
            @Comments = i.Comments
        FROM inserted i;

        IF (SELECT COUNT(*) FROM Production.Product WHERE ProductID = @ProductID) > 0
        BEGIN
            
            PRINT N'cập nhật thành công cho ProductID: ' + CAST(@ProductID AS NVARCHAR(10));
            
            
            SELECT 
                p.ProductID,
                p.Color,
                p.StandardCost,
                @Rating AS Rating,    
                @Comments AS Comments   
            FROM 
                Production.Product AS p
            WHERE 
                p.ProductID = @ProductID;
        END
        ELSE
        BEGIN
            
            RAISERROR (N'lỗi: Mã sản phẩm %d không tồn tại. Giao tác bị hủy', 16, 1, @ProductID);
            ROLLBACK TRANSACTION; 
        END
    END
END
GO
--instead 


CREATE TRIGGER TR_ProductReview_OnUpdateComments1
ON Production.ProductReview
INSTEAD OF UPDATE 
AS
BEGIN
    SET NOCOUNT ON; 


    IF UPDATE(Comments)
    BEGIN
        
 
        IF EXISTS (
            SELECT 1 FROM inserted i
            LEFT JOIN Production.Product p ON i.ProductID = p.ProductID
            WHERE p.ProductID IS NULL 
        )
        BEGIN
          
            DECLARE @BadProductID INT;
            SELECT TOP 1 @BadProductID = i.ProductID
            FROM inserted i
            LEFT JOIN Production.Product p ON i.ProductID = p.ProductID
            WHERE p.ProductID IS NULL;

           
            RAISERROR (N'lỗi: Mã sản phẩm %d không tồn tại. Giao tác bị hủy', 16, 1, @BadProductID);
            RETURN; 
        END

    
        UPDATE p  
        SET 
            
            p.ProductID = i.ProductID,
            p.ReviewerName = i.ReviewerName,
            p.ReviewDate = i.ReviewDate,
            p.EmailAddress = i.EmailAddress,
            p.Rating = i.Rating,
            p.Comments = i.Comments
           
        FROM 
            Production.ProductReview p
        JOIN 
            inserted i ON p.ProductReviewID = i.ProductReviewID;

        PRINT N'Cập nhật comments thành công. Thông tin sản phẩm liên quan:';
        SELECT 
            p.ProductID,
            p.Color,
            p.StandardCost,
            i.Rating,   
            i.Comments  
        FROM 
            Production.Product AS p
        JOIN 
            inserted AS i ON p.ProductID = i.ProductID;
        
    END
    ELSE
    BEGIN
        UPDATE p
        SET 
            p.ProductID = i.ProductID,
            p.ReviewerName = i.ReviewerName,
            p.ReviewDate = i.ReviewDate,
            p.EmailAddress = i.EmailAddress,
            p.Rating = i.Rating,
            p.Comments = i.Comments
        FROM 
            Production.ProductReview p
        JOIN 
            inserted i ON p.ProductReviewID = i.ProductReviewID;
    END
END
GO


-- kiem tra thanh cong 

UPDATE Production.ProductReview
SET Comments = N'Đây là bình luận test trigger thành công.'
WHERE ProductReviewID = 1;
GO


-- kiem tra that bai 


UPDATE Production.ProductReview
SET Comments = N'Cố gắng cập nhật bình luận cho ProductID không tồn tại'
WHERE ProductReviewID = 9999;
GO
