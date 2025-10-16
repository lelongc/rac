package BSTkh;

import java.util.Comparator;
import java.util.List;
import java.util.Optional;
import java.util.Random;
import java.util.stream.Collectors;

public class UngDungKhachHang {
    private BSTKhachHang bst;

    public UngDungKhachHang() {
        this.bst = new BSTKhachHang();
        DuLieuMau(20);
    }

    public void DuLieuMau(int soLuong) {
        String[] tenMau = {"An Nguyen", "Binh Tran", "Cuong Le", "Dung Pham", "Hai Vo", 
                          "Lan Hoang", "Minh Dao", "Nga Bui", "Phuc Do", "Quang Ngo"};
        String[] gioiTinhMau = {"Male", "Female"};
        Random rand = new Random();
        
        for (int i = 1; i <= soLuong; i++) {
            try {
                String ten = tenMau[rand.nextInt(tenMau.length)] + " V" + i;
                int tuoi = rand.nextInt(48) + 18; // Tuổi từ 18-65
                String gioiTinh = gioiTinhMau[rand.nextBoolean() ? 0 : 1];
                String email = ten.toLowerCase().replace(" ", ".") + "@company.com";
                String phone = "09" + String.format("%08d", rand.nextInt(100000000));
                
                KhachHang kh = new KhachHang(i, ten, tuoi, gioiTinh, email, phone);
                this.bst.addkh(kh);
            } catch (IllegalArgumentException e) {
                System.err.println("Lỗi tạo khách hàng " + i + ": " + e.getMessage());
                i--; // Thử lại với ID này
            }
        }
        System.out.println("✅ Đã nhập " + soLuong + " khách hàng vào BST theo ID.");
    }

    public void XuatTheoTen() {
        System.out.println("\n=== 1. DANH SÁCH KHÁCH HÀNG SẮP XẾP THEO TÊN ===");
        
        this.bst.laykh().stream()
            .sorted(Comparator.comparing(KhachHang::getTen))
            .forEach(System.out::println);
    }

    public void ThongKeGioiTinh() {
        System.out.println("\n=== 2. THỐNG KÊ GIỚI TÍNH ===");
        List<KhachHang> danhSach = this.bst.laykh();
        
        long soMale = danhSach.stream()
            .filter(kh -> kh.getGend().equalsIgnoreCase("Male"))
            .count();
            
        long soFemale = danhSach.size() - soMale;
        
        System.out.println("📊 Tổng số khách hàng Male: " + soMale);
        System.out.println("📊 Tổng số khách hàng Female: " + soFemale);
        System.out.println("📊 Tổng số khách hàng: " + danhSach.size());
    }

    public void TuoiNhoNhatLonNhatToanBo() {
        System.out.println("\n=== 3. KHÁCH HÀNG CÓ TUỔI NHỎ NHẤT VÀ LỚN NHẤT (TOÀN BỘ) ===");
        List<KhachHang> danhSach = this.bst.laykh();
        
        if (danhSach.isEmpty()) {
            System.out.println("❌ Danh sách trống.");
            return;
        }

        danhSach.stream()
            .min(Comparator.comparingInt(KhachHang::getTuoi))
            .ifPresent(kh -> System.out.println("👶 Khách hàng tuổi nhỏ nhất: " + kh));

        danhSach.stream()
            .max(Comparator.comparingInt(KhachHang::getTuoi))
            .ifPresent(kh -> System.out.println("👴 Khách hàng tuổi lớn nhất: " + kh));
    }

    private void TimTuoiMinMaxTheoGioiTinh(String gioiTinh) {
        String title = gioiTinh.equalsIgnoreCase("Male") ? "NAM (MALE)" : "NỮ (FEMALE)";
        System.out.println("\n=== KHÁCH HÀNG " + title + " CÓ TUỔI LỚN NHẤT VÀ NHỎ NHẤT ===");
        
        List<KhachHang> filteredList = this.bst.laykh().stream()
            .filter(kh -> kh.getGend().equalsIgnoreCase(gioiTinh))
            .collect(Collectors.toList());

        if (filteredList.isEmpty()) {
            System.out.println("❌ Không có khách hàng " + gioiTinh + " nào.");
            return;
        }

        Optional<KhachHang> khNhoNhat = filteredList.stream()
            .min(Comparator.comparingInt(KhachHang::getTuoi));
            
        Optional<KhachHang> khLonNhat = filteredList.stream()
            .max(Comparator.comparingInt(KhachHang::getTuoi));
        
        khNhoNhat.ifPresent(kh -> System.out.println("👶 Khách hàng " + gioiTinh + " tuổi nhỏ nhất: " + kh));
        khLonNhat.ifPresent(kh -> System.out.println("👴 Khách hàng " + gioiTinh + " tuổi lớn nhất: " + kh));
    }

    public void TuoiMaleNhoNhatLonNhat() {
        TimTuoiMinMaxTheoGioiTinh("Male");
    }

    public void TuoiFemaleNhoNhatLonNhat() {
        TimTuoiMinMaxTheoGioiTinh("Female");
    }

    public void XuatThongTinChiTiet() {
        System.out.println("\n=== 6. THÔNG TIN CHI TIẾT KHÁCH HÀNG ===");
        List<KhachHang> danhSach = this.bst.laykh();
        
        System.out.println("📧 Email và 📞 Phone của tất cả khách hàng:");
        danhSach.stream()
            .sorted(Comparator.comparing(KhachHang::getTen))
            .forEach(kh -> System.out.printf("ID: %d | Tên: %s | Email: %s | Phone: %s%n", 
                                           kh.getId(), kh.getTen(), kh.getEmail(), kh.getPhone()));
    }

    public void ChayUngDung() {
        System.out.println("🚀 CHƯƠNG TRÌNH QUẢN LÝ KHÁCH HÀNG BST - MỞ RỘNG LAB7");
        System.out.println("=" + "=".repeat(59));
        
        XuatTheoTen();
        ThongKeGioiTinh();
        TuoiNhoNhatLonNhatToanBo();
        TuoiMaleNhoNhatLonNhat();
        TuoiFemaleNhoNhatLonNhat();
        XuatThongTinChiTiet();
        
        System.out.println("\n✅ Chương trình hoàn thành!");
    }

    public static void main(String[] args) {
        try {
            UngDungKhachHang ungDung = new UngDungKhachHang();
            ungDung.ChayUngDung();
        } catch (Exception e) {
            System.err.println("❌ Lỗi chương trình: " + e.getMessage());
            e.printStackTrace();
        }
    }
}