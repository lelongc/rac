package Bai5_ProductDB;

import java.sql.*;

public class DatabaseUtils {
    public static Product find(String name) {
        try (Connection c = DriverManager.getConnection("jdbc:mysql://localhost:3306/productdb", "root", "root");
                PreparedStatement s = c.prepareStatement("SELECT * FROM products WHERE name LIKE ?")) {
            s.setString(1, "%" + name + "%");
            ResultSet rs = s.executeQuery();
            if (rs.next())
                return new Product(rs.getInt(1), rs.getString(2), rs.getDouble(3), rs.getString(4));
        } catch (Exception e) {
            e.printStackTrace();
        }
        return null;
    }
}
