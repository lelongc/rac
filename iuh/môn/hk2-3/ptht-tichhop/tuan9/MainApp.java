package b1;

import java.sql.*;

public class MainApp {
    public static void main(String[] args) {
        Connection conn = null;
        try {
      
            conn = DatabaseManager.getConnection();
            
          
            conn.setAutoCommit(false); 


            DatabaseManager.initDatabase(conn);

       
            DatabaseManager.insertSanPham(conn, new SanPham(1, "Laptop Dell", 15000, 5));
            DatabaseManager.insertSanPham(conn, new SanPham(2, "Macbook M3", 35000, 3));
            DatabaseManager.insertSanPham(conn, new SanPham(3, "Chuột Logi", 500, 10));

 
            DatabaseManager.updateSanPham(conn, 1, 14500, 4);
            DatabaseManager.deleteSanPham(conn, 3);
      

            System.out.println(">>> Đang thêm dữ liệu nhân viên để thống kê...");
            String sqlInsertNV = "INSERT INTO NhanVien(ten, chuc_vu, luong) VALUES(?,?,?)";
            try (PreparedStatement pstmt = conn.prepareStatement(sqlInsertNV)) {

                pstmt.setString(1, "Nguyen Van A"); pstmt.setString(2, "Dev"); pstmt.setDouble(3, 2000);
                pstmt.executeUpdate();
                
                pstmt.setString(1, "Tran Thi B"); pstmt.setString(2, "Manager"); pstmt.setDouble(3, 5000);
                pstmt.executeUpdate();
            }


            DatabaseManager.thongKeNhanVien(conn);


            conn.commit();
            System.out.println("\n[SUCCESS] Giao dịch hoàn tất thành công!");

        } catch (SQLException e) {
     
            System.err.println("[ERROR] Lỗi SQL: " + e.getMessage());
            try {
                if (conn != null) {
                    conn.rollback(); 
                    System.err.println("[ROLLBACK] Đã khôi phục trạng thái dữ liệu cũ.");
                }
            } catch (SQLException ex) {
                ex.printStackTrace();
            }
        } finally {
  
            try {
                if (conn != null) {
                    conn.close();
                    System.out.println("[INFO] Đã đóng kết nối an toàn.");
                }
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}