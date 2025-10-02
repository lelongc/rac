import java.io.File;
import java.util.Scanner;



public class Main {
    public static void main(String[] args) {
        QuanLySinhVien qlsv = new QuanLySinhVien(); 
        Scanner scanner = new Scanner(System.in);
        int luaChon;
        
        do {
            clearScreen();
            hienThiMenu();
            try {
                luaChon = Integer.parseInt(scanner.nextLine());
                
                switch (luaChon) {
                    case 1:
                        themSinhVienMoi(qlsv, scanner);
                        break;
                    case 2:
                        xoaSinhVienTheoID(qlsv, scanner);
                        break;
                    case 3:
                        qlsv.sapXepTheoTen();
                        break;
                    case 4:
                        qlsv.sapXepTheoDiem();
                        break;
                    case 5:
                        qlsv.hienThiDanhSach();
                        break;
                    case 6:
                        luuDuLieuRaFile(qlsv, scanner);
                        break;
                    case 7:
                        docDuLieuTuFile(qlsv, scanner);
                        break;
                    case 8:
                        timSinhVienTheoID(qlsv, scanner);
                        break;
                    case 0:
                        System.out.println("Cảm ơn bạn đã sử dụng chương trình!");
                        break;
                    default:
                        System.out.println("Lựa chọn không hợp lệ!");
                }
            } catch (NumberFormatException e) {
                System.out.println("Vui lòng nhập số!");
                luaChon = -1;
            }
            
        } while (luaChon != 0);
        
        scanner.close();
    }
    
    private static void clearScreen() {
        try {
            final String os = System.getProperty("os.name");
            if (os.contains("Windows")) {
                new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
            } else {
                System.out.print("\033[H\033[2J");
                System.out.flush();
            }
        } catch (Exception e) {
            for (int i = 0; i < 50; i++) {
                System.out.println();
            }
        }
    }
    
    private static void hienThiMenu() {
        System.out.println("\n=== MENU QUẢN LÝ SINH VIÊN (DÙNG BST) ===");
        System.out.println("1. Thêm sinh viên mới");
        System.out.println("2. Xóa sinh viên theo ID");
        System.out.println("3. Sắp xếp sinh viên theo tên (Hiển thị)");
        System.out.println("4. Sắp xếp sinh viên theo điểm (cao đến thấp)");
        System.out.println("5. Hiển thị danh sách sinh viên (Theo ID)");
        System.out.println("6. Lưu dữ liệu ra file");
        System.out.println("7. Đọc dữ liệu từ file");
        System.out.println("8. Tìm sinh viên theo ID");
        System.out.println("0. Thoát chương trình");
        System.out.print(">> Vui lòng chọn chức năng: ");
    }
    
    private static void themSinhVienMoi(QuanLySinhVien qlsv, Scanner scanner) {
        try {
            System.out.print("Nhập ID sinh viên: ");
            int id = Integer.parseInt(scanner.nextLine());
            
            System.out.print("Nhập tên sinh viên: ");
            String ten = scanner.nextLine();
            
            System.out.print("Nhập điểm sinh viên (0-10): ");
            double diem = Double.parseDouble(scanner.nextLine());
            
            if (diem < 0 || diem > 10) {
                System.out.println("Điểm phải nằm trong khoảng từ 0 đến 10!");
                return;
            }
            
            qlsv.themSinhVien(id, ten, diem);
        } catch (NumberFormatException e) {
            System.out.println("Dữ liệu nhập không hợp lệ! Vui lòng kiểm tra lại ID và Điểm.");
        }
    }
    
    private static void xoaSinhVienTheoID(QuanLySinhVien qlsv, Scanner scanner) {
        try {
            System.out.print("Nhập ID sinh viên cần xóa: ");
            int id = Integer.parseInt(scanner.nextLine());
            qlsv.xoaSinhVien(id);
        } catch (NumberFormatException e) {
            System.out.println("ID phải là số nguyên!");
        }
    }
    
    private static void luuDuLieuRaFile(QuanLySinhVien qlsv, Scanner scanner) {
        System.out.print("Nhập tên file để lưu (vd: sinhvien.dat): ");
        String filename = scanner.nextLine();
        
        if (!filename.trim().isEmpty()) {
            qlsv.saveToFile(filename);
        } else {
            System.out.println("Tên file không được để trống!");
        }
    }
    
    private static void docDuLieuTuFile(QuanLySinhVien qlsv, Scanner scanner) {
        System.out.print("Nhập tên file để đọc (vd: sinhvien.dat): ");
        String filename = scanner.nextLine();
        
        if (!filename.trim().isEmpty()) {
            File file = new File(filename);
            if (file.exists()) {
                qlsv.loadFromFile(filename);
            } else {
                System.out.println("File '" + filename + "' không tồn tại!");
            }
        } else {
            System.out.println("Tên file không được để trống!");
        }
    }
    
    private static void timSinhVienTheoID(QuanLySinhVien qlsv, Scanner scanner) {
        try {
            System.out.print("Nhập ID sinh viên cần tìm: ");
            int id = Integer.parseInt(scanner.nextLine());
            Student found = timSinhVienRecursive(qlsv.getRoot(), id); 
            System.out.println("\n=== KẾT QUẢ TÌM KIẾM ===");
            if (found != null) {
                System.out.println("TÌM THẤY: " + found);
            } else {
                System.out.println("Không tìm thấy sinh viên có ID: " + id);
            }
            System.out.println("========================");
        } catch (NumberFormatException e) {
            System.out.println("ID phải là số nguyên!");
        }
    }
    
    /**
     * Hàm tìm kiếm đệ quy trong BST dựa trên ID.
     */
    private static Student timSinhVienRecursive(Student node, int id) {
        if (node == null) {
            return null;
        }
        
        if (id == node.getStudentId()) {
            return node;
        }
        
        if (id < node.getStudentId()) { 
            return timSinhVienRecursive(node.getPrev(), id); // Đi sang trái
        } else {
            return timSinhVienRecursive(node.getNext(), id); // Đi sang phải
        }
    }
}