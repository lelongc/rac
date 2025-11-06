use AdventureWorks2008R2
SELECT TABLE_SCHEMA, TABLE_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE COLUMN_NAME = 'BusinessEntityID'

USE AdventureWorks2008R2;
GO

-- tìm nhiều cột trên 1 bảng 
SELECT TABLE_SCHEMA, TABLE_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE COLUMN_NAME IN ('SalesPersonID', 'SubTotal','Bonus')
GROUP BY TABLE_SCHEMA, TABLE_NAME
HAVING COUNT(DISTINCT COLUMN_NAME) = 3

--- 
-- tìm bảng chứa các cột để kết bảng 
SELECT TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE COLUMN_NAME IN ('TotalDue', 'ProductCategoryID','Name','OrderDate')
ORDER BY COLUMN_NAME, TABLE_SCHEMA, TABLE_NAME;

----
--- kiểu của cột 
SELECT 
    COLUMN_NAME, 
    DATA_TYPE, 
    CHARACTER_MAXIMUM_LENGTH, 
    IS_NULLABLE
FROM 
    INFORMATION_SCHEMA.COLUMNS
WHERE 
    TABLE_NAME = 'Product'
    AND TABLE_SCHEMA = 'Production'
ORDER BY 
    ORDINAL_POSITION;

---
-- join cột nào 1 

SELECT
    OBJECT_NAME(fk.parent_object_id) AS BangNguon,
    COL_NAME(fkc.parent_object_id, fkc.parent_column_id) AS CotKhoaNgoai,
    OBJECT_NAME(fk.referenced_object_id) AS BangDich,
    COL_NAME(fkc.referenced_object_id, fkc.referenced_column_id) AS CotKhoaChinh
FROM
    sys.foreign_keys AS fk
INNER JOIN
    sys.foreign_key_columns AS fkc ON fk.object_id = fkc.constraint_object_id
WHERE
    OBJECT_NAME(fk.parent_object_id) IN ('ProductCategory', 'ProductSubcategory', 'Product', 'SalesOrderDetail')
    AND OBJECT_NAME(fk.referenced_object_id) IN ('ProductCategory', 'ProductSubcategory', 'Product', 'SalesOrderDetail')
ORDER BY
    BangNguon;


