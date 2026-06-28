    USE AdventureWorks2008R2;
    DELETE FROM HumanResources.EmployeeDepartmentHistory
    WHERE BusinessEntityID = 23; 

    
	--kiem tra quyen
	select * from HumanResources.EmployeeDepartmentHistory
    WHERE BusinessEntityID = 51; 

	SELECT * FROM HumanResources.EmployeeDepartmentHistory
	WHERE BusinessEntityID = 23;

	SELECT * FROM HumanResources.Employee;