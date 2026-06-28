    USE AdventureWorks2008R2;

     --Sửa cột ModifiedDate
    UPDATE HumanResources.EmployeeDepartmentHistory
    SET ModifiedDate = GETDATE()
    WHERE BusinessEntityID = 51; 



	--kiem tra quyen
	select * from HumanResources.EmployeeDepartmentHistory
    WHERE BusinessEntityID = 51; 

	SELECT * FROM HumanResources.EmployeeDepartmentHistory
	WHERE BusinessEntityID = 23;

	SELECT * FROM HumanResources.Employee;