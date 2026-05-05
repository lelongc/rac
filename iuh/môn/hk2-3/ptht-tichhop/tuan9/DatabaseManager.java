package b1;

import java.sql.*;

public class DatabaseManager {
    private static final String URL = "jdbc:sqlite:quanly_hethong.db";


    public static Connection getConnection() throws SQLException {
        return DriverManager.getConnection(URL);
    }


    public static void initDatabase(Connection conn) throws SQLException {
        String sqlSP = "CREATE TABLE IF NOT EXISTS SanPham (" +
                       "maSP INTEGER PRIMARY KEY, tenSP TEXT, gia REAL, soluong INTEGER)";
        String sqlNV = "CREATE TABLE IF NOT EXISTS NhanVien (" +
                       "id INTEGER PRIMARY KEY AUTOINCREMENT, ten TEXT, chuc_vu TEXT, luong REAL)";
        try (Statement stmt = conn.createStatement()) {
            stmt.execute(sqlSP);
            stmt.execute(sqlNV);
        }
    }

  
    public static void insertSanPham(Connection conn, SanPham sp) throws SQLException {
        String sql = "INSERT INTO SanPham(maSP, tenSP, gia, soluong) VALUES(?,?,?,?)";
        try (PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setInt(1, sp.getMaSP());
            pstmt.setString(2, sp.getTenSP());
            pstmt.setDouble(3, sp.getGia());
            pstmt.setInt(4, sp.getSoLuong());
            pstmt.executeUpdate();
        }
    }


    public static void updateSanPham(Connection conn, int maSP, double giaMoi, int slMoi) throws SQLException {
        String sql = "UPDATE SanPham SET gia = ?, soluong = ? WHERE maSP = ?";
        try (PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setDouble(1, giaMoi);
            pstmt.setInt(2, slMoi);
            pstmt.setInt(3, maSP);
            pstmt.executeUpdate();
        }
    }

  
    public static void deleteSanPham(Connection conn, int maSP) throws SQLException {
        String sql = "DELETE FROM SanPham WHERE maSP = ?";
        try (PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setInt(1, maSP);
            pstmt.executeUpdate();
        }
    }

    public static void thongKeNhanVien(Connection conn) throws SQLException {
        String sql = "SELECT SUM(luong) as tong, AVG(luong) as trungbinh, " +
                     "MAX(luong) as cao, MIN(luong) as thap FROM NhanVien";
        try (Statement stmt = conn.createStatement(); ResultSet rs = stmt.executeQuery(sql)) {
            if (rs.next()) {
                System.out.println("--- THỐNG KÊ LƯƠNG NHÂN VIÊN ---");
                System.out.println("Tổng lương: " + rs.getDouble("tong"));
                System.out.println("Lương TB:   " + rs.getDouble("trungbinh"));
                System.out.println("Cao nhất:   " + rs.getDouble("cao"));
            }
        }
    }
}
