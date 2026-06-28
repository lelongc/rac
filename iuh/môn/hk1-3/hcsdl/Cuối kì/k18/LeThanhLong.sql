---cau1
--a
USE [master]
GO
CREATE LOGIN [NV1] WITH PASSWORD=N'kkkkkkkk', DEFAULT_DATABASE=[AdventureWorks2008R2]
GO
CREATE LOGIN [NV2] WITH PASSWORD=N'kkkkkkkk', DEFAULT_DATABASE=[AdventureWorks2008R2]
GO
CREATE LOGIN [QL] WITH PASSWORD=N'kkkkkkkk', DEFAULT_DATABASE=[AdventureWorks2008R2]
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

GRANT DELETE, INSERT, SELECT, UPDATE ON [Purchasing].[PurchaseOrderDetail] TO [NhanVien]
GO

ALTER ROLE [NhanVien] ADD MEMBER [NV1]
GO
ALTER ROLE [NhanVien] ADD MEMBER [NV2]
GO
ALTER ROLE [db_datareader] ADD MEMBER [QL]
GO
--c 
--23630851
--d
USE [AdventureWorks2008R2]
GO

REVOKE DELETE, INSERT, SELECT, UPDATE ON [Purchasing].[PurchaseOrderDetail] FROM [NhanVien]
GO


ALTER ROLE [NhanVien] DROP MEMBER [NV1]
GO
ALTER ROLE [NhanVien] DROP MEMBER [NV2]
GO


ALTER ROLE [db_datareader] DROP MEMBER [QL]
GO


DROP ROLE [NhanVien]
GO
---cau2
--a
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
SET Rate = Rate * 1.15
WHERE BusinessEntityID IN (SELECT BusinessEntityID FROM HumanResources.EmployeeDepartmentHistory WHERE ShiftID = 2);
     
UPDATE HumanResources.EmployeePayHistory
SET Rate = Rate * 1.25
WHERE BusinessEntityID IN (SELECT BusinessEntityID FROM HumanResources.EmployeeDepartmentHistory WHERE ShiftID = 3);
COMMIT TRANSACTION;

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

--b
USE AdventureWorks2008R2;
--truoc
SELECT COUNT(*) AS SoLuongDong FROM [Sales].[SalesTerritoryHistory]

DELETE FROM [Sales].[SalesTerritoryHistory]

    --sau 
SELECT COUNT(*) AS SoLuongDong FROM [Sales].[SalesTerritoryHistory]


BACKUP DATABASE [AdventureWorks2008R2] TO  DISK = N'D:\Backup\backup-diff.bak' WITH  DIFFERENTIAL
GO
--c
USE AdventureWorks2008R2;
    --truoc
   
SELECT * FROM Person.PersonPhone WHERE BusinessEntityID = 0851;

  
INSERT INTO Person.PersonPhone (BusinessEntityID, PhoneNumber, PhoneNumberTypeID, ModifiedDate)
VALUES (0851, '029-123-4356', 1, GETDATE()); 

--sau 

SELECT * FROM Person.PersonPhone WHERE BusinessEntityID = 0851;
BACKUP LOG [AdventureWorks2008R2] TO  DISK = N'D:\Backup\backup-log.bak' WITH INIT
GO
--d
USE [master]
drop database AdventureWorks2008R2 
USE [master]
RESTORE DATABASE [AdventureWorks2008R2] FROM  DISK = N'D:\Backup\backup-full.bak' WITH  FILE = 1,  NORECOVERY,  NOUNLOAD,  STATS = 5
RESTORE DATABASE [AdventureWorks2008R2] FROM  DISK = N'D:\Backup\backup-diff.bak' WITH  FILE = 5,  NORECOVERY,  NOUNLOAD,  STATS = 5
RESTORE LOG [AdventureWorks2008R2] FROM  DISK = N'D:\Backup\backup-log.bak' WITH  FILE = 1,  NOUNLOAD,  STATS = 5

GO





-- kiem tra sau restoe 
USE AdventureWorks2008R2;
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

SELECT COUNT(*) AS SoLuongDong FROM [Sales].[SalesTerritoryHistory]

SELECT * FROM Person.PersonPhone WHERE BusinessEntityID = 0851;
BACKUP LOG [AdventureWorks2008R2] TO  DISK = N'D:\Backup\backup-log.bak' WITH INIT
GO


---cau3

CREATE TRIGGER TR_ProductReview_UpdateComments
ON Production.ProductReview
INSTEAD OF UPDATE
AS
BEGIN
    SET NOCOUNT ON;

    
    IF UPDATE(Comments)
    BEGIN
       
        UPDATE pr
        SET pr.Comments = i.Comments
        FROM Production.ProductReview pr
        JOIN inserted i ON pr.ProductReviewID = i.ProductReviewID;

       
        SELECT 
            p.ProductID,
            p.Color,
            p.StandardCost,
            i.Rating,
            i.Comments
        FROM inserted i
        JOIN Production.Product p ON i.ProductID = p.ProductID;
    END
    ELSE
    BEGIN
       
        UPDATE pr
        SET 
            pr.ProductID = i.ProductID,
            pr.ReviewerName = i.ReviewerName,
            pr.ReviewDate = i.ReviewDate,
            pr.EmailAddress = i.EmailAddress,
            pr.Rating = i.Rating,
            pr.Comments = i.Comments
        FROM Production.ProductReview pr
        JOIN inserted i ON pr.ProductReviewID = i.ProductReviewID;
    END
END;
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