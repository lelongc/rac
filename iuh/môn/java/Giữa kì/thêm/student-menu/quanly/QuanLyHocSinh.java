package quanly;

import java.io.*;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.List;
import java.util.Optional;

public class QuanLyHocSinh {
    private List<HocSinh> danhSachHS;
    private static final String TEN_FILE = "hocsinh.dat";

    public QuanLyHocSinh() {
        // NOTE: Để dùng ArrayList, chỉ cần đổi dòng dưới thành:
        // this.danhSachHS = new ArrayList<>();
        this.danhSachHS = new LinkedList<>();
    }

    // --- CÁC CHỨC NĂNG CHÍNH ---

    public void themHS(String maHS, String tenHS, double diem) {
        HocSinh hs = new HocSinh(maHS, tenHS, diem);
        danhSachHS.add(hs);
    }

    public boolean xoaHS(String maHS) {
        return danhSachHS.removeIf(hs -> hs.getMaHS().equalsIgnoreCase(maHS));
    }
    
    public Optional<HocSinh> timHSTheoMa(String maHS) {
        return danhSachHS.stream()
                .filter(hs -> hs.getMaHS().equalsIgnoreCase(maHS))
                .findFirst();
    }

    public void sapXepTheoTen() {
        danhSachHS.sort(Comparator.comparing(HocSinh::getTenHS, String.CASE_INSENSITIVE_ORDER));
    }

    public void sapXepTheoDiem() {
        danhSachHS.sort(Comparator.comparingDouble(HocSinh::getDiem).reversed());
    }
    
    public void hienThiDanhSach() {
        if (danhSachHS.isEmpty()) {
            System.out.println("Danh sach hoc sinh trong.");
            return;
        }
        System.out.println("Ma HS      | Ho va Ten                 | Diem     | Xep Loai");
        System.out.println("------------------------------------------------------------------");
        for (HocSinh hs : danhSachHS) {
            System.out.println(hs);
        }
    }

    // --- CÁC HÀM ĐỌC/GHI FILE ---
    
    public boolean luuFile() {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(TEN_FILE))) {
            oos.writeObject(danhSachHS);
            return true;
        } catch (IOException e) {
            return false;
        }
    }

    @SuppressWarnings("unchecked")
    public boolean docFile() {
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(TEN_FILE))) {
            this.danhSachHS = (List<HocSinh>) ois.readObject();
            return true;
        } catch (IOException | ClassNotFoundException e) {
            return false;
        }
    }
}