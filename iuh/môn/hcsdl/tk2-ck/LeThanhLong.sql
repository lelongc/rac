
--c1
USE [master]
GO
CREATE LOGIN [TN] WITH PASSWORD=N'kkkkkk', DEFAULT_DATABASE=[AdventureWorks2008R2]
GO
CREATE LOGIN [NV] WITH PASSWORD=N'kkkkkk', DEFAULT_DATABASE=[AdventureWorks2008R2]
GO
CREATE LOGIN [QL] WITH PASSWORD=N'kkkkkk', DEFAULT_DATABASE=[AdventureWorks2008R2]
GO

--a

USE [AdventureWorks2008R2]
GO
CREATE USER [TN] FOR LOGIN [TN]
GO
CREATE USER [NV] FOR LOGIN [NV]
GO
CREATE USER [QL] FOR LOGIN [QL]
GO

--b
USE [AdventureWorks2008R2]
GO
CREATE ROLE [NhanVien]
GO

GRANT DELETE, INSERT, SELECT, UPDATE ON [Sales].[ShoppingCartItem] TO [NhanVien]
GO

ALTER ROLE [NhanVien] ADD MEMBER [TN]
GO
ALTER ROLE [NhanVien] ADD MEMBER [NV]
GO
ALTER ROLE [db_datareader] ADD MEMBER [QL]
GO

--d
USE [AdventureWorks2008R2]
GO


ALTER ROLE [NhanVien] DROP MEMBER [NV]
GO

--e
REVOKE DELETE, INSERT, SELECT, UPDATE ON [Sales].[ShoppingCartItem] FROM [NhanVien]
GO


ALTER ROLE [NhanVien] DROP MEMBER [TN]
GO


ALTER ROLE [db_datareader] DROP MEMBER [QL]
GO


DROP ROLE [NhanVien]
GO


--cau 3
use [AdventureWorks2008R2]
ALTER DATABASE [AdventureWorks2008R2] SET RECOVERY FULL
--a
BACKUP DATABASE [AdventureWorks2008R2] 
TO DISK = N'T:\Backup\backup-full.bak' 
WITH INIT
GO
--b

SELECT 
    eph.BusinessEntityID, 
    edh.ShiftID,
    eph.Rate,
	DepartmentID
FROM 
    HumanResources.EmployeePayHistory AS eph
JOIN 
    HumanResources.EmployeeDepartmentHistory AS edh 
    ON eph.BusinessEntityID = edh.BusinessEntityID
WHERE 
    edh.ShiftID IN (1,3) 
ORDER BY
    edh.ShiftID, eph.BusinessEntityID;
GO

    BEGIN TRANSACTION;
     
    UPDATE HumanResources.EmployeePayHistory
    SET Rate = Rate * 1.10
    WHERE BusinessEntityID IN (SELECT BusinessEntityID FROM HumanResources.EmployeeDepartmentHistory WHERE ShiftID = 1 and [DepartmentID] in (1,3,5) );
     
    UPDATE HumanResources.EmployeePayHistory
    SET Rate = Rate * 1.20
    WHERE BusinessEntityID IN (SELECT BusinessEntityID FROM HumanResources.EmployeeDepartmentHistory WHERE ShiftID = 3);
    COMMIT TRANSACTION;



BACKUP LOG [AdventureWorks2008R2] TO  DISK = N'T:\Backup\backup-log.bak' WITH INIT
GO

--c

SELECT COUNT(*) AS SoLuongDong FROM Production.ProductCostHistory;
DELETE FROM Production.ProductCostHistory;
SELECT COUNT(*) AS SoLuongDong FROM Production.ProductCostHistory;


BACKUP LOG [AdventureWorks2008R2] TO  DISK = N'T:\Backup\backup-log2.bak' WITH INIT
GO
--d
--10001

   
SELECT * FROM Person.PersonPhone WHERE BusinessEntityID = 10001;

  
INSERT INTO Person.PersonPhone (BusinessEntityID, PhoneNumber, PhoneNumberTypeID, ModifiedDate)
VALUES (10001, '0909-123-456', 1, GETDATE()); 

BACKUP DATABASE [AdventureWorks2008R2] TO  DISK = N'T:\Backup\backup-diff.bak' WITH  DIFFERENTIAL
GO
--e
USE [master]
drop database AdventureWorks2008R2 



USE [master]
RESTORE DATABASE [AdventureWorks2008R2] FROM  DISK = N'T:\Backup\backup-full.bak' WITH  FILE = 1,  NORECOVERY,  NOUNLOAD,  STATS = 5
RESTORE LOG [AdventureWorks2008R2] FROM  DISK = N'T:\Backup\backup-log.bak' WITH  FILE = 1,  NORECOVERY,  NOUNLOAD,  STATS = 5
RESTORE LOG [AdventureWorks2008R2] FROM  DISK = N'T:\Backup\backup-log2.bak' WITH  FILE = 1,  NOUNLOAD,  STATS = 5

GO


--f
use [AdventureWorks2008R2]
SELECT * FROM Person.PersonPhone WHERE BusinessEntityID = 10001;




