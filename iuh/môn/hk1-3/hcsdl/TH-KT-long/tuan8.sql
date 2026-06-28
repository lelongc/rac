/********************************************************************************
** BÀI THỰC HÀNH TUẦN 8 - MODULE 6 & 7
** Script T-SQL với chú thích đầy đủ cho từng bước.
** LƯU Ý: Vui lòng chạy script này trên CSDL AdventureWorks2008.
** Một số bước (như 4, 5, 7) yêu cầu bạn mở một tab truy vấn MỚI
** (New Query) và đăng nhập với tư cách User2/User3 để kiểm tra.
********************************************************************************/

-- Đảm bảo chúng ta đang làm việc ở cấp độ Server (master) để tạo Login
USE master;
GO

/********************************************************************************
** MODULE 6. ROLE - PERMISSION
********************************************************************************/

-- 1) Đăng nhập vào SQL bằng SQL Server authentication, tài khoản sa.
-- BƯỚC NÀY BẠN PHẢI THỰC HIỆN THỦ CÔNG KHI KẾT NỐI VÀO SSMS.
-- Toàn bộ script dưới đây giả định đang được thực thi bởi user 'sa'
-- hoặc một user có quyền 'sysadmin'.

PRINT '--- Bắt đầu Module 6: Roles & Permissions ---';
PRINT '--- (Đang thực thi với quyền SA) ---';

-- 2) Tạo hai login SQL server Authentication User2 và User3
PRINT '--- 2. Tạo Logins User2 và User3 ---';
-- Xóa login nếu đã tồn tại để script có thể chạy lại
IF EXISTS (SELECT 1 FROM sys.server_principals WHERE name = 'User2')
    DROP LOGIN User2;
IF EXISTS (SELECT 1 FROM sys.server_principals WHERE name = 'User3')
    DROP LOGIN User3;

-- Tạo login mới. CHECK_POLICY=OFF để bỏ qua chính sách mật khẩu phức tạp của Windows.
CREATE LOGIN User2 WITH PASSWORD = 'P@ssw0rd123', CHECK_POLICY = OFF;
CREATE LOGIN User3 WITH PASSWORD = 'P@ssw0rd123', CHECK_POLICY = OFF;
PRINT 'Đã tạo xong 2 logins: User2, User3.';
GO

-- 3) Tạo database user User2 và User3 trên CSDL AdventureWorks2008
PRINT '--- 3. Tạo Database Users trong AdventureWorks2008 ---';
-- Chuyển sang context của CSDL AdventureWorks2008
USE AdventureWorks2008;
GO

-- Xóa user nếu đã tồn tại
IF EXISTS (SELECT 1 FROM sys.database_principals WHERE name = 'User2')
    DROP USER User2;
IF EXISTS (SELECT 1 FROM sys.database_principals WHERE name = 'User3')
    DROP USER User3;

-- Tạo database user và "ánh xạ" (map) chúng với các server login tương ứng
CREATE USER User2 FOR LOGIN User2;
CREATE USER User3 FOR LOGIN User3;
PRINT 'Đã tạo 2 database users (User2, User3) và map tới logins.';
GO

-- 4) Tạo 2 kết nối đến server thông qua login User2 và User3, sau đó thực hiện
--    thao tác truy cập CSDL (VD: câu Select). Có thực hiện được không?
PRINT '--- 4. Kiểm tra kết nối User2, User3 ---';
PRINT '*** BƯỚC THỰC HIỆN THỦ CÔNG ***';
PRINT 'Mở 2 cửa sổ New Query, kết nối với login User2 và User3.';
PRINT 'Sau đó, trong mỗi cửa sổ, thử chạy lệnh:';
PRINT 'USE AdventureWorks2008;';
PRINT 'SELECT TOP 10 * FROM HumanResources.Employee;';
PRINT '---';
PRINT '*** GIẢI THÍCH (4) ***';
PRINT '=> KHÔNG thực hiện được.';
PRINT 'Lý do: User2 và User3 vừa được tạo, chúng chỉ thuộc role "public" mặc định.';
PRINT 'Role "public" không có quyền SELECT trên bảng HumanResources.Employee.';
PRINT 'Bạn sẽ nhận được thông báo lỗi: "The SELECT permission was denied on the object ''Employee'', database ''AdventureWorks2008'', schema ''HumanResources''."';
GO

-- 5) Gán quyền select trên Employee cho User2, kiểm tra kết quả.
--    Xóa quyền select trên Employee cho User2.
PRINT '--- 5. Gán quyền (GRANT) và thu hồi quyền (REVOKE) ---';

-- (Thực thi với quyền SA)
USE AdventureWorks2008;
GRANT SELECT ON HumanResources.Employee TO User2;
PRINT 'Đã gán quyền SELECT trên HumanResources.Employee cho User2.';
GO

PRINT '*** BƯỚC THỰC HIỆN THỦ CÔNG (KIỂM TRA) ***';
PRINT 'Quay lại cửa sổ kết nối của User2, chạy lại lệnh:';
PRINT 'SELECT TOP 10 * FROM HumanResources.Employee;';
PRINT '=> Lần này lệnh sẽ chạy THÀNH CÔNG.';
PRINT 'Trong khi đó, cửa sổ của User3 vẫn sẽ báo lỗi nếu chạy lệnh SELECT.';
GO

-- (Thực thi với quyền SA)
USE AdventureWorks2008;
REVOKE SELECT ON HumanResources.Employee FROM User2;
PRINT 'Đã thu hồi (REVOKE) quyền SELECT của User2.';
PRINT 'Nếu User2 chạy lại lệnh SELECT, bây giờ sẽ lại THẤT BẠI.';
GO
-- Ngắt 2 kết nối của User2 và User3 (Bạn tự đóng 2 tab New Query đó lại)
PRINT 'Đã ngắt kết nối User2, User3 (giả định).';

-- 6) Trở lại kết nối của sa, tạo một user-defined database Role tên Employee_Role
--    trên CSDL AdventureWorks2008, sau đó gán các quyền Select, Update, Delete.
PRINT '--- 6. Tạo Database Role và gán quyền cho Role ---';
USE AdventureWorks2008;
GO

-- Xóa role nếu đã tồn tại
IF EXISTS (SELECT 1 FROM sys.database_principals WHERE name = 'Employee_Role' AND type = 'R')
BEGIN
    -- Phải xóa member trước khi xóa role
    DECLARE @member_name sysname;
    DECLARE member_cursor CURSOR FOR
    SELECT m.name
    FROM sys.database_role_members rm
    JOIN sys.database_principals r ON rm.role_principal_id = r.principal_id
    JOIN sys.database_principals m ON rm.member_principal_id = m.principal_id
    WHERE r.name = 'Employee_Role';

    OPEN member_cursor;
    FETCH NEXT FROM member_cursor INTO @member_name;
    WHILE @@FETCH_STATUS = 0
    BEGIN
        EXEC sp_droprolemember 'Employee_Role', @member_name;
        FETCH NEXT FROM member_cursor INTO @member_name;
    END;
    CLOSE member_cursor;
    DEALLOCATE member_cursor;

    DROP ROLE Employee_Role;
END
GO

CREATE ROLE Employee_Role;
PRINT 'Đã tạo database role "Employee_Role".';

-- Gán quyền cho Role
GRANT SELECT, UPDATE, DELETE ON HumanResources.Employee TO Employee_Role;
PRINT 'Đã gán quyền SELECT, UPDATE, DELETE trên HumanResources.Employee cho Employee_Role.';
GO

-- 7) Thêm các User2 và User3 vào Employee_Role.
PRINT '--- 7. Thêm User vào Role ---';
USE AdventureWorks2008;
ALTER ROLE Employee_Role ADD MEMBER User2;
ALTER ROLE Employee_Role ADD MEMBER User3;
PRINT 'Đã thêm User2 và User3 vào Employee_Role.';
GO

PRINT '*** BƯỚC THỰC HIỆN THỦ CÔNG (KIỂM TRA) ***';
PRINT 'Mở lại 2 kết nối mới cho User2 và User3.';

-- 7a) Tại kết nối với User2, thực hiện câu lệnh Select
PRINT '--- 7a. (User2) Kiểm tra quyền SELECT ---';
PRINT 'Tại cửa sổ User2, chạy lệnh:';
PRINT 'USE AdventureWorks2008;';
PRINT 'SELECT BusinessEntityID, JobTitle FROM HumanResources.Employee WHERE BusinessEntityID = 1;';
PRINT '=> Sẽ chạy THÀNH CÔNG (do User2 thừa hưởng quyền SELECT từ Role).';

-- 7b) Tại kết nối của User3, thực hiện cập nhật JobTitle
PRINT '--- 7b. (User3) Kiểm tra quyền UPDATE ---';
PRINT 'Tại cửa sổ User3, chạy lệnh:';
PRINT 'USE AdventureWorks2008;';
PRINT 'UPDATE HumanResources.Employee SET JobTitle = ''Sale Manager'' WHERE BusinessEntityID = 1;';
PRINT '=> Sẽ chạy THÀNH CÔNG (do User3 thừa hưởng quyền UPDATE từ Role).';

-- 7c) Tại kết nối User2, dùng câu lệnh Select xem lại kết quả.
PRINT '--- 7c. (User2) Kiểm tra lại kết quả UPDATE ---';
PRINT 'Tại cửa sổ User2, chạy lại lệnh:';
PRINT 'SELECT BusinessEntityID, JobTitle FROM HumanResources.Employee WHERE BusinessEntityID = 1;';
PRINT '=> Sẽ thấy JobTitle bây giờ là "Sale Manager".';

-- 7d) Xóa role Employee_Role, (quá trình xóa role ra sao ?)
PRINT '--- 7d. (SA) Xóa Role ---';
USE AdventureWorks2008;
GO
PRINT '*** GIẢI THÍCH (7d) ***';
PRINT 'Không thể xóa (DROP) một role khi nó vẫn còn thành viên (members).';
PRINT 'Nếu chạy "DROP ROLE Employee_Role;" ngay, sẽ nhận lỗi:';
PRINT '"The role ''Employee_Role'' is not empty, and cannot be dropped."';
PRINT '=> Quá trình xóa role chuẩn:';
PRINT '   1. Xóa tất cả thành viên ra khỏi role.';
PRINT '   2. Xóa role.';

-- 1. Xóa thành viên
ALTER ROLE Employee_Role DROP MEMBER User2;
ALTER ROLE Employee_Role DROP MEMBER User3;
PRINT 'Đã xóa User2, User3 khỏi Employee_Role.';

-- 2. Xóa role
DROP ROLE Employee_Role;
PRINT 'Đã xóa thành công Employee_Role.';
GO

/********************************************************************************
** MODULE 7. TRANSACTION
** Giả sử bảng HumanResources.Department tồn tại.
********************************************************************************/

PRINT '--- Bắt đầu Module 7: Transactions ---';
USE AdventureWorks2008;
GO

-- 1) Thêm vào bảng Department một dòng dữ liệu tùy ý
PRINT '--- 1. Thao tác với Autocommit (mặc định) ---';
-- Ở chế độ Autocommit, mỗi lệnh T-SQL là một giao dịch riêng lẻ và tự động commit.
INSERT INTO HumanResources.Department (Name, GroupName, ModifiedDate)
VALUES ('New Dept (Autocommit)', 'Temp Group', GETDATE());
PRINT 'Đã
INSERT 1 dòng (Autocommit). Dòng này đã được lưu vĩnh viễn.';
-- Xóa dòng vừa thêm để dọn dẹp
DELETE FROM HumanResources.Department WHERE Name = 'New Dept (Autocommit)';
GO

-- 1a) Thực hiện lệnh chèn... với Begin tran và Rollback
PRINT '--- 1a. Giao dịch với ROLLBACK ---';
BEGIN TRAN;
    INSERT INTO HumanResources.Department (Name, GroupName, ModifiedDate)
    VALUES ('Dept (Rollback)', 'Temp Group', GETDATE());
    PRINT 'Đã INSERT 1 dòng (trong transaction).';
ROLLBACK TRAN;
PRINT 'Đã ROLLBACK giao dịch.';

-- Kiểm tra kết quả
SELECT * FROM HumanResources.Department WHERE Name = 'Dept (Rollback)';
PRINT '=> Kết quả SELECT: 0 dòng. Dữ liệu đã bị hủy bỏ.';
GO

-- 1b) Thực hiện câu lệnh trên với lệnh Commit
PRINT '--- 1b. Giao dịch với COMMIT ---';
BEGIN TRAN;
    INSERT INTO HumanResources.Department (Name, GroupName, ModifiedDate)
    VALUES ('Dept (Commit)', 'Temp Group', GETDATE());
    PRINT 'Đã INSERT 1 dòng (trong transaction).';
COMMIT TRAN;
PRINT 'Đã COMMIT giao dịch.';

-- Kiểm tra kết quả
SELECT * FROM HumanResources.Department WHERE Name = 'Dept (Commit)';
PRINT '=> Kết quả SELECT: 1 dòng. Dữ liệu đã được lưu vĩnh viễn.';

-- Dọn dẹp
DELETE FROM HumanResources.Department WHERE Name = 'Dept (Commit)';
GO

-- 2) Tắt chế độ autocommit (SET IMPLICIT_TRANSACTIONS ON)
PRINT '--- 2. Chế độ IMPLICIT_TRANSACTIONS ---';
SET IMPLICIT_TRANSACTIONS ON;
PRINT 'Đã SET IMPLICIT_TRANSACTIONS ON (tắt autocommit).';

-- Một giao dịch ngầm định (implicit transaction) sẽ TỰ ĐỘNG BẮT ĐẦU
-- ngay khi lệnh T-SQL đầu tiên (INSERT) được thực thi.
INSERT INTO HumanResources.Department (Name, GroupName, ModifiedDate)
VALUES ('Implicit Dept', 'Test Group', GETDATE());

-- Tạo bảng Test (vẫn trong cùng 1 giao dịch)
IF OBJECT_ID('Test', 'U') IS NOT NULL
    DROP TABLE Test;
CREATE TABLE Test (ID int, Name nvarchar(10));

-- Thêm dòng vào Test (vẫn trong cùng 1 giao dịch)
INSERT INTO Test VALUES (1, 'TestName');
PRINT 'Đã INSERT vào Department, CREATE TABLE Test, và INSERT vào Test.';

-- Rollback lại toàn bộ giao dịch ngầm định đã bắt đầu
ROLLBACK;
PRINT 'Đã ROLLBACK giao dịch ngầm định.';

-- Bật lại chế độ autocommit (mặc định)
SET IMPLICIT_TRANSACTIONS OFF;

-- Kiểm tra kết quả
PRINT 'Kiểm tra dữ liệu sau Rollback:';
SELECT * FROM HumanResources.Department WHERE Name = 'Implicit Dept';
PRINT '=> Kết quả SELECT từ Department: 0 dòng.';

-- Lệnh SELECT * FROM Test sẽ gây lỗi, vì bảng Test không tồn tại
-- SELECT * FROM Test;
IF OBJECT_ID('Test', 'U') IS NOT NULL
    PRINT 'Bảng Test VẪN TỒN TẠI.';
ELSE
    PRINT 'Bảng Test KHÔNG TỒN TẠI.';

PRINT '*** GIẢI THÍCH (2) ***';
PRINT 'Khi SET IMPLICIT_TRANSACTIONS ON, lệnh INSERT đầu tiên đã tự động mở một giao dịch.';
PRINT 'Lệnh CREATE TABLE và INSERT tiếp theo đều là một phần của giao dịch đó.';
PRINT 'Lệnh ROLLBACK đã hủy bỏ TẤT CẢ các thao tác này.';
PRINT '=> Dòng "Implicit Dept" bị hủy.';
PRINT '=> Bảng "Test" bị hủy (không được tạo).';
GO

-- 3) Viết đoạn batch thực hiện... (SET XACT_ABORT ON)
PRINT '--- 3. Giao dịch với SET XACT_ABORT ON ---';
SET XACT_ABORT ON;
PRINT 'Đã SET XACT_ABORT ON.';

BEGIN TRAN;
    PRINT 'Bắt đầu giao dịch (XACT_ABORT ON)...';
    -- Thêm 1 dòng hợp lệ
    INSERT INTO HumanResources.Department (Name, GroupName, ModifiedDate)
    VALUES ('Abort Dept', 'Test Group', GETDATE());
    PRINT 'Đã INSERT 1 dòng (Abort Dept).';
    
    -- Câu lệnh SELECT với phép chia 0 (lỗi run-time)
    BEGIN TRY
        PRINT 'Chuẩn bị thực hiện SELECT 1/0...';
        SELECT 1/0 as Dummy;
        
        -- Các lệnh này sẽ KHÔNG BAO GIỜ được thực thi
        UPDATE HumanResources.Department SET Name = 'Test Update' WHERE DepartmentID = 9;
        DELETE FROM HumanResources.Department WHERE DepartmentID = 66;
        INSERT INTO HumanResources.Department (Name, GroupName, ModifiedDate)
        VALUES ('Abort Dept 2', 'Test Group', GETDATE());
        COMMIT;
        PRINT 'Đã Commit (sẽ không bao giờ tới đây).';
    END TRY
    BEGIN CATCH
        PRINT '!!! Đã xảy ra lỗi (CATCH block): ' + ERROR_MESSAGE();
        -- Kiểm tra xem giao dịch có còn mở không
        IF @@TRANCOUNT > 0
        BEGIN
            PRINT 'Giao dịch vẫn còn mở. XACT_ABORT ON sẽ tự động ROLLBACK.';
            -- Mặc dù XACT_ABORT tự động rollback, ta vẫn cần gọi ROLLBACK
            -- để xóa trạng thái giao dịch và thoát CATCH block.
            ROLLBACK;
        END
    END CATCH

-- Kiểm tra kết quả
PRINT 'Kiểm tra dữ liệu sau khi batch kết thúc:';
SELECT * FROM HumanResources.Department WHERE Name = 'Abort Dept';

PRINT '*** GIẢI THÍCH (3) ***';
PRINT 'Khi SET XACT_ABORT ON:';
PRINT '1. Lệnh INSERT đầu tiên (Abort Dept) chạy thành công.';
PRINT '2. Lệnh SELECT 1/0 gây ra lỗi run-time nghiêm trọng.';
PRINT '3. XACT_ABORT ON lập tức dừng (abort) toàn bộ batch VÀ tự động ROLLBACK toàn bộ giao dịch.';
PRINT '4. Các lệnh UPDATE, DELETE, INSERT (Abort Dept 2) và COMMIT sau đó bị bỏ qua.';
PRINT '=> Kết quả: Dòng "Abort Dept" đã bị rollback. Bảng Department trở về trạng thái ban đầu.';
GO

-- 4) Thực hiện lệnh SET XACT_ABORT OFF ... thực thi lại các thao tác của đoạn batch ở câu 3
PRINT '--- 4. Giao dịch với SET XACT_ABORT OFF ---';
SET XACT_ABORT OFF;
PRINT 'Đã SET XACT_ABORT OFF.';

BEGIN TRAN;
    PRINT 'Bắt đầu giao dịch (XACT_ABORT OFF)...';
    -- Thêm 1 dòng hợp lệ
    INSERT INTO HumanResources.Department (Name, GroupName, ModifiedDate)
    VALUES ('No Abort Dept', 'Test Group', GETDATE());
    PRINT 'Đã INSERT 1 dòng (No Abort Dept).';
    
    -- Câu lệnh SELECT với phép chia 0 (lỗi run-time)
    BEGIN TRY
        PRINT 'Chuẩn bị thực hiện SELECT 1/0...';
        SELECT 1/0 as Dummy; -- Lỗi này vẫn đủ nghiêm trọng để dừng batch

        -- Các lệnh này sẽ KHÔNG được thực thi
        UPDATE HumanResources.Department SET Name = 'Test Update' WHERE DepartmentID = 9;
        DELETE FROM HumanResources.Department WHERE DepartmentID = 66;
        INSERT INTO HumanResources.Department (Name, GroupName, ModifiedDate)
        VALUES ('No Abort Dept 2', 'Test Group', GETDATE());
        COMMIT;
        PRINT 'Đã Commit (sẽ không bao giờ tới đây).';
    END TRY
    BEGIN CATCH
        PRINT '!!! Đã xảy ra lỗi (CATCH block): ' + ERROR_MESSAGE();
        -- Kiểm tra xem giao dịch có còn mở không
        PRINT 'Trạng thái giao dịch (@@TRANCOUNT): ' + CAST(@@TRANCOUNT AS VARCHAR(2));
        IF @@TRANCOUNT > 0
        BEGIN
            PRINT 'Giao dịch vẫn còn mở. XACT_ABORT OFF KHÔNG tự động rollback.';
            PRINT 'Giao dịch hiện ở trạng thái "treo" (doomed) và không thể Commit.';
            PRINT 'Phải ROLLBACK thủ công.';
            ROLLBACK;
            PRINT 'Đã ROLLBACK thủ công.';
        END
    END CATCH

-- Kiểm tra kết quả
PRINT 'Kiểm tra dữ liệu sau khi batch kết thúc:';
SELECT * FROM HumanResources.Department WHERE Name = 'No Abort Dept';

PRINT '*** GIẢI THÍCH (4) ***';
PRINT 'Khi SET XACT_ABORT OFF:';
PRINT '1. Lệnh INSERT đầu tiên (No Abort Dept) chạy thành công.';
PRINT '2. Lệnh SELECT 1/0 gây ra lỗi run-time nghiêm trọng. Lỗi này vẫn làm dừng batch.';
PRINT '3. Tuy nhiên, XACT_ABORT OFF có nghĩa là SQL Server KHÔNG tự động rollback giao dịch.';
PRINT '4. Batch nhảy vào CATCH block. Giao dịch vẫn MỞ (@@TRANCOUNT = 1) nhưng ở trạng thái "doomed" (không thể commit).';
PRINT '5. Chúng ta phải ROLLBACK thủ công trong CATCH block để đóng giao dịch.';
PRINT '=> Kết quả: Dòng "No Abort Dept" cũng đã bị rollback (lần này là do thủ công).';
PRINT 'Sự khác biệt chính: XACT_ABORT ON = tự động rollback. XACT_ABORT OFF = không tự động rollback, giao dịch bị "treo" và cần xử lý thủ công.';
GO


 DỌN DẸP 
 xóa các Login và User đã tạo.

PRINT '--- Bắt đầu dọn dẹp ---';
USE AdventureWorks2008;
IF EXISTS (SELECT 1 FROM sys.database_principals WHERE name = 'User2')
    DROP USER User2;
IF EXISTS (SELECT 1 FROM sys.database_principals WHERE name = 'User3')
    DROP USER User3;
PRINT 'Đã xóa database users: User2, User3.';
GO

USE master;
IF EXISTS (SELECT 1 FROM sys.server_principals WHERE name = 'User2')
    DROP LOGIN User2;
IF EXISTS (SELECT 1 FROM sys.server_principals WHERE name = 'User3')
    DROP LOGIN User3;
PRINT 'Đã xóa server logins: User2, User3.';
GO

-- Dọn dẹp các dòng dữ liệu test còn sót lại (nếu có)
USE AdventureWorks2008;
DELETE FROM HumanResources.Department WHERE GroupName = 'Test Group';
DELETE FROM HumanResources.Department WHERE GroupName = 'Temp Group';
PRINT 'Đã dọn dẹp dữ liệu test trong Department.';
PRINT '--- HOÀN TẤT SCRIPT ---';