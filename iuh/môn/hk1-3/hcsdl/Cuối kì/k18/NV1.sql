    UPDATE [Purchasing].[PurchaseOrderDetail]
    SET ModifiedDate = GETDATE()
    WHERE PurchaseOrderDetailID = 851;
	SELECT * FROM Purchasing.Vendor;