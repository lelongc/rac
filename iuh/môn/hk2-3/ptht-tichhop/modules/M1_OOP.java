// ============================================================
// MODULE 1 – OOP KẾ THỪA (extends)
// Dùng khi đề: "Viết class cha/con, tính lương/thuế/..."
// Ghép với: M5/M6 (client gửi object), M2 (thread xử lý)
// ============================================================
import java.util.Scanner;

// ── LỚP CHA ──────────────────────────────────────────────────
class Entity {                          // TODO: đổi tên lớp cha
    // TODO: khai báo fields cha
    String id;
    String name;

    // Constructor rỗng
    public Entity() {}

    // Constructor tham số (dùng khi con gọi super())
    public Entity(String id, String name) {
        this.id   = id;
        this.name = name;
    }

    // Nhập (dùng Scanner hoặc BufferedReader tuỳ đề)
    public void nhapThongTin(Scanner sc) {
        System.out.print("Nhap ID: ");   id   = sc.nextLine();
        System.out.print("Nhap ten: "); name = sc.nextLine();
    }

    // Hiển thị
    public void hienThi() {
        System.out.println("ID: " + id + " | Ten: " + name);
    }

    // TODO: thêm method tính toán cha nếu có
    public double tinhToan() { return 0; }
}

// ── LỚP CON A ────────────────────────────────────────────────
class ConA extends Entity {             // TODO: đổi tên lớp con
    // TODO: field riêng của con
    int    soLuong;
    double donGia;

    public ConA() { super(); }

    // Dùng khi cha có constructor tham số
    // public ConA(String id, String name, int soLuong, double donGia) {
    //     super(id, name);
    //     this.soLuong = soLuong;
    //     this.donGia  = donGia;
    // }

    @Override
    public void nhapThongTin(Scanner sc) {
        super.nhapThongTin(sc);          // nhập cha trước
        System.out.print("So luong: "); soLuong = Integer.parseInt(sc.nextLine());
        System.out.print("Don gia: ");  donGia  = Double.parseDouble(sc.nextLine());
    }

    @Override
    public void hienThi() {
        super.hienThi();
        System.out.println("  Luong = " + tinhToan());
    }

    @Override
    public double tinhToan() {
        return soLuong * donGia;         // TODO: công thức riêng
    }
}

// ── LỚP CON B (nếu có nhiều loại) ───────────────────────────
class ConB extends Entity {
    double luongCB;
    double phuCap;

    public ConB() { super(); }

    @Override
    public void nhapThongTin(Scanner sc) {
        super.nhapThongTin(sc);
        System.out.print("Luong CB: "); luongCB = Double.parseDouble(sc.nextLine());
        System.out.print("Phu cap: ");  phuCap  = Double.parseDouble(sc.nextLine());
    }

    @Override
    public double tinhToan() {
        return luongCB + phuCap;         // TODO: công thức riêng
    }
}

// ── MAIN ─────────────────────────────────────────────────────
public class M1_OOP {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        ConA a = new ConA();
        a.nhapThongTin(sc);
        a.hienThi();
        System.out.println("Ket qua: " + a.tinhToan());

        ConB b = new ConB();
        b.nhapThongTin(sc);
        b.hienThi();
        System.out.println("Ket qua: " + b.tinhToan());

        sc.close();
    }
}
