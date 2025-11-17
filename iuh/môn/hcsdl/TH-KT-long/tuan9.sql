/* -----------------------------------------------------------
MODULE 7 – CONCURRENT TRANSACTIONS
----------------------------------------------------------- */

-- 1) Tạo bảng Accounts và chèn dữ liệu
DROP TABLE IF EXISTS Accounts;
CREATE TABLE Accounts (
    AccountID INT NOT NULL PRIMARY KEY,
    balance INT NOT NULL
        CONSTRAINT unloanable_account CHECK (balance >= 0)
);

INSERT INTO Accounts VALUES (101,1000);
INSERT INTO Accounts VALUES (202,2000);



/* ================= CLIENT A ================= */
-- 2+3) READ COMMITTED DEMO
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
BEGIN TRAN;

-- B1: SELECT
SELECT * FROM Accounts WHERE AccountID = 101;

-- B2: Update
UPDATE Accounts SET balance = balance - 200 WHERE AccountID = 101;

-- B4: SELECT and COMMIT
SELECT * FROM Accounts WHERE AccountID = 101;
COMMIT;


/* ================= CLIENT B ================= */
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
BEGIN TRAN;

-- B1: SELECT
SELECT * FROM Accounts WHERE AccountID = 101;

-- B3: Update
UPDATE Accounts SET balance = balance - 500 WHERE AccountID = 101;

-- B5: SELECT and COMMIT
SELECT * FROM Accounts WHERE AccountID = 101;
COMMIT;



/* ================= REPEATABLE READ DEMO ================= */

/* CLIENT A */
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
BEGIN TRAN;

-- B1
SELECT * FROM Accounts WHERE AccountID = 101;

-- B2
UPDATE Accounts SET balance = balance - 200 WHERE AccountID = 101;

/* CLIENT B */
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
BEGIN TRAN;

-- B3: BLOCKED HERE
UPDATE Accounts SET balance = balance - 500 WHERE AccountID = 101;

-- B4 CLIENT A:
SELECT * FROM Accounts WHERE AccountID = 101;
COMMIT;



/* 5) CONTROL DEADLOCK - TRANSFER MONEY */
-- CLIENT A: Transfer 100 (101 -> 202)
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN TRAN;
UPDATE Accounts SET balance = balance - 100 WHERE AccountID = 101;
UPDATE Accounts SET balance = balance + 100 WHERE AccountID = 202;
COMMIT;

-- CLIENT B: Transfer 200 (202 -> 101)
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
BEGIN TRAN;
UPDATE Accounts SET balance = balance - 200 WHERE AccountID = 202;
UPDATE Accounts SET balance = balance + 200 WHERE AccountID = 101;
COMMIT;



/* 6) Dirty Read Demonstration */
DELETE FROM Accounts;
INSERT INTO Accounts VALUES (101,1000),(202,2000);

-- CLIENT A
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
BEGIN TRAN;
UPDATE Accounts SET balance = balance - 100 WHERE AccountID = 101;
UPDATE Accounts SET balance = balance + 100 WHERE AccountID = 202;

-- CLIENT B
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
SELECT * FROM Accounts; -- Dirty read
COMMIT;

-- CLIENT A
ROLLBACK;
SELECT * FROM Accounts;
COMMIT;



/* 7) Phantom Read Demonstration */
DELETE FROM Accounts;
INSERT INTO Accounts VALUES (101,1000),(202,2000);

-- CLIENT A
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
BEGIN TRAN;
SELECT * FROM Accounts WHERE balance > 1000;

-- CLIENT B
INSERT INTO Accounts VALUES (303,3000);
COMMIT;

-- CLIENT A - STILL SEE SAME RESULT
SELECT * FROM Accounts WHERE balance > 1000;
COMMIT;



/* -----------------------------------------------------------
MODULE 8 – BACKUP & RECOVERY
----------------------------------------------------------- */

-- 1) CREATE DEVICE
EXEC sp_addumpdevice 'disk', 'adv2008back', 'T:\backup\adv2008back.bak';

-- 2) ATTACH DB + FULL RECOVERY MODE
ALTER DATABASE AdventureWorks2008 SET RECOVERY FULL;
BACKUP DATABASE AdventureWorks2008 TO adv2008back WITH INIT;

-- 3) Update bicycles price with condition
BEGIN TRAN;
UPDATE Production.Product
SET ListPrice -= 15
WHERE ProductSubcategoryID IN (
    SELECT ProductSubcategoryID FROM Production.ProductSubcategory
    WHERE Name LIKE '%Bike%'
);
COMMIT;

-- 4a) Differential backup
BACKUP DATABASE AdventureWorks2008 TO adv2008back WITH DIFFERENTIAL;

-- 4b) Log Backup
BACKUP LOG AdventureWorks2008 TO adv2008back;

-- 5) Delete all EmailAddress + Log backup
DELETE FROM Person.EmailAddress;
BACKUP LOG AdventureWorks2008 TO adv2008back;

-- 6a) Insert new phone
INSERT INTO Person.PersonPhone VALUES (10000,'123-456-7890',1,GETDATE());

-- 6b) Differential backup
BACKUP DATABASE AdventureWorks2008 TO adv2008back WITH DIFFERENTIAL;

-- 6c) WAIT 1 minute then drop:
DROP TABLE Sales.ShoppingCartItem;



-- 7) XÓA DATABASE
DROP DATABASE AdventureWorks2008;



/* Restore plan
   a) Restore to initial state => FULL backup + RECOVERY
   b) Restore after bike update => FULL + DIFF #1 + LOG #1
   c) Restore to time after note => FULL + DIFF #2 + STOPAT TIME
*/



/* 9) Plan2Recover */
CREATE DATABASE Plan2Recover;
USE Plan2Recover;

CREATE TABLE T1 (
    PK INT IDENTITY PRIMARY KEY,
    Name VARCHAR(15)
);
INSERT T1 VALUES ('Full');

BACKUP DATABASE Plan2Recover
TO DISK='T:\P2R.bak'
WITH NAME='P2R_Full', INIT;

INSERT T1 VALUES ('Log 1');
BACKUP LOG Plan2Recover TO DISK='T:\P2R.bak' WITH NAME='P2R_Log1';

INSERT T1 VALUES ('Log 2');
BACKUP LOG Plan2Recover TO DISK='T:\P2R.bak' WITH NAME='P2R_Log2';

DROP DATABASE Plan2Recover;

-- Restore
USE master;
RESTORE DATABASE Plan2Recover
FROM DISK='T:\P2R.bak'
WITH FILE=1, NORECOVERY;
RESTORE LOG Plan2Recover
FROM DISK='T:\P2R.bak'
WITH FILE=2, NORECOVERY;
RESTORE LOG Plan2Recover
FROM DISK='T:\P2R.bak'
WITH FILE=3, RECOVERY;
