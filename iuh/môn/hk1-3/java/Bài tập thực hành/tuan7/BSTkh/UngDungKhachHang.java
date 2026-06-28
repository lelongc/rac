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
        String[] tenMau = {"An", "Bình", "Cường", "Dung", "Hải", "Lan", "Minh", "Nga", "Phúc", "Quang"};
        Random rand = new Random();
        
        for (int i = 1; i <= soLuong; i++) {
            String ten = tenMau[rand.nextInt(tenMau.length)] + " V" + i;
            int tuoi = rand.nextInt(48) + 18;
            String gioiTinh = rand.nextBoolean() ? "nam" : "nu";
            KhachHang kh = new KhachHang(i, ten, tuoi, gioiTinh);
            this.bst.addkh(kh);
        }
        System.out.println("✅ Đã nhập " + soLuong + " khách hàng vào BST theo ID.");
    }

    public void XuatTheoTen() {
        System.out.println("\n--- 1. Danh Sách Khách Hàng Sắp Xếp Theo Tên ---");
        
        this.bst.laykh().stream()
            .sorted(Comparator.comparing(KhachHang::getTen))
            .forEach(System.out::println);
    }


    public void ThongKeGioiTinh() {
        System.out.println("\n--- 2. Thống Kê Giới Tính ---");
        List<KhachHang> danhSach = this.bst.laykh();
        
        long soNam = danhSach.stream()
            .filter(kh -> kh.getGend().equals("nam"))
            .count();
            
        long soNu = danhSach.size() - soNam;
        
        System.out.println("Tổng số khách hàng nam: " + soNam);
        System.out.println("Tổng số khách hàng nữ: " + soNu);
    }


    public void TuoiNhoNhatLonNhatToanBo() {
        System.out.println("\n--- 3. Khách Hàng Có Tuổi Nhỏ Nhất và Lớn Nhất (Toàn Bộ) ---");
        List<KhachHang> danhSach = this.bst.laykh();
        
        if (danhSach.isEmpty()) {
            System.out.println("Danh sách trống.");
            return;
        }


        danhSach.stream()
            .min(Comparator.comparingInt(KhachHang::getTuoi))
            .ifPresent(kh -> System.out.println("Khách hàng tuổi nhỏ nhất: " + kh));


        danhSach.stream()
            .max(Comparator.comparingInt(KhachHang::getTuoi))
            .ifPresent(kh -> System.out.println("Khách hàng tuổi lớn nhất: " + kh));
    }

    private void TimTuoiMinMaxTheoGioiTinh(String gioiTinh) {
        System.out.println("\n--- Khách Hàng " + (gioiTinh.equals("nam") ? "Nam" : "Nữ") + " Có Tuổi Lớn Nhất và Nhỏ Nhất ---");
        
        List<KhachHang> filteredList = this.bst.laykh().stream()
            .filter(kh -> kh.getGend().equals(gioiTinh))
            .collect(Collectors.toList());

        if (filteredList.isEmpty()) {
            System.out.println("Không có khách hàng " + gioiTinh + " nào.");
            return;
        }

        Optional<KhachHang> khNhoNhat = filteredList.stream()
            .min(Comparator.comparingInt(KhachHang::getTuoi));
            
        Optional<KhachHang> khLonNhat = filteredList.stream()
            .max(Comparator.comparingInt(KhachHang::getTuoi));
        
        khNhoNhat.ifPresent(kh -> System.out.println("Khách hàng " + gioiTinh + " tuổi nhỏ nhất: " + kh));
        khLonNhat.ifPresent(kh -> System.out.println("Khách hàng " + gioiTinh + " tuổi lớn nhất: " + kh));
    }
    

    public void TuoiNamNhoNhatLonNhat() {
        TimTuoiMinMaxTheoGioiTinh("nam");
    }


    public void TuoiNuNhoNhatLonNhat() {
        TimTuoiMinMaxTheoGioiTinh("nu");
    }


    public void ChayUngDung() {
        XuatTheoTen();
        ThongKeGioiTinh();
        TuoiNhoNhatLonNhatToanBo();
        TuoiNamNhoNhatLonNhat();
        TuoiNuNhoNhatLonNhat();
    }

    public static void main(String[] args) {
        UngDungKhachHang ungDung = new UngDungKhachHang();
        ungDung.ChayUngDung();
    }
}