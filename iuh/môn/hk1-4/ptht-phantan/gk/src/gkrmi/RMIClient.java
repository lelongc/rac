package gkrmi;

import java.rmi.Naming;
import java.util.Scanner;

public class RMIClient {
    public static final String HOST = "localhost";
    public static final int PORT = 1099;
    public static final String SERVICE_NAME = "RemoteService";

    public static void main(String[] args) {
        String rmiUrl = "rmi://" + HOST + ":" + PORT + "/" + SERVICE_NAME;

        try {
            System.out.println("Dang ket noi toi Server tai: " + rmiUrl);
            IRemoteService service = (IRemoteService) Naming.lookup(rmiUrl);
            System.out.println("Ket noi thanh cong!\n");

            Scanner scanner = new Scanner(System.in);

            // =================================================================
            // ⚠️ QUY TẮC PHÒNG THI ĐỂ BÀI NỘP KHÔNG BỊ THỪA:
            // 1. Chỉ uncomment ĐÚNG 1 BÀI tương ứng với IRemoteService và RemoteServiceImpl.
            // 2. VỀ FILE SinhVien.java:
            //    CHỈ DUY NHẤT [BÀI 37: ĐỐI TƯỢNG SINH VIÊN] MỚI CẦN FILE SinhVien.java.
            //    NẾU ĐỀ RA BẤT KỲ BÀI NÀO KHÁC (BÀI 1 ĐẾN BÀI 36):
            //    -> HÃY XÓA THẲNG TAY FILE SinhVien.java ĐI, DỰ ÁN VẪN BIÊN DỊCH VÀ CHẠY 100%!
            // =================================================================

            // ========== BAI 1: May tinh 4 phep tinh (+, -, *, /) - [TUAN 6 BAI 3 - MAC DINH BAT] [KHONG CAN SinhVien.java] ==========
            System.out.println("=== BÀI 1: MÁY TÍNH 4 PHÉP TÍNH ===");
            System.out.print("Nhap so thu nhat (a): ");
            int a = scanner.nextInt();
            System.out.print("Nhap so thu hai (b): ");
            int b = scanner.nextInt();
            System.out.println(a + " + " + b + " = " + service.add(a, b));
            System.out.println(a + " - " + b + " = " + service.sub(a, b));
            System.out.println(a + " * " + b + " = " + service.mul(a, b));
            try {
                System.out.println(a + " / " + b + " = " + service.div(a, b));
            } catch (Exception e) {
                System.out.println("Loi: " + e.getMessage());
            }

            // ========== BAI 2: Tam giac (Chu vi, dien tich Heron) - Input: a, b, c - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 2: TÍNH TAM GIÁC ===");
            // System.out.print("Nhap canh a: "); double a = scanner.nextDouble();
            // System.out.print("Nhap canh b: "); double b = scanner.nextDouble();
            // System.out.print("Nhap canh c: "); double c = scanner.nextDouble();
            // System.out.println("Ket qua: " + service.tinhTamGiac(a, b, c));

            // ========== BAI 3: So phuc (ADD/SUB/MUL/DIV) - Input: op, ar, ai, br, bi - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 3: SỐ PHỨC ===");
            // System.out.print("Nhap phep tinh (ADD/SUB/MUL/DIV): "); String op = scanner.nextLine().trim();
            // System.out.print("Nhap phan thuc a: "); double ar = scanner.nextDouble();
            // System.out.print("Nhap phan ao a: "); double ai = scanner.nextDouble();
            // System.out.print("Nhap phan thuc b: "); double br = scanner.nextDouble();
            // System.out.print("Nhap phan ao b: "); double bi = scanner.nextDouble();
            // System.out.println("Ket qua: " + service.soPhuc(op, ar, ai, br, bi));

            // ========== BAI 4: So Fibonacci / In day Fibonacci - Input: n - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 4: FIBONACCI ===");
            // System.out.print("Nhap n: "); int n = scanner.nextInt();
            // System.out.println("Ket qua: " + service.fibonacci(n));

            // ========== BAI 5: Quy doi tien te - Input: amount, from, to (USD, EUR, JPY, VND) - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 5: QUY ĐỔI TIỀN TỆ ===");
            // System.out.print("Nhap so tien: "); double amt = scanner.nextDouble();
            // scanner.nextLine();
            // System.out.print("Tu loai tien (VND, USD, EUR, JPY): "); String from = scanner.nextLine().trim();
            // System.out.print("Sang loai tien (VND, USD, EUR, JPY): "); String to = scanner.nextLine().trim();
            // System.out.println("Ket qua: " + service.quyDoiTienTe(amt, from, to));

            // ========== BAI 6: Kiem tra so nguyen to - Input: n - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 6: KIỂM TRA SỐ NGUYÊN TỐ ===");
            // System.out.print("Nhap n: "); long n = scanner.nextLong();
            // System.out.println(n + (service.isPrime(n) ? " la so nguyen to" : " khong phai so nguyen to"));

            // ========== BAI 7: Sap xep tang dan danh sach so - Input: "5,2,9,1" - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 7: SẮP XẾP TĂNG DẦN ===");
            // System.out.print("Nhap danh sach so (vd: 5,2,9,1 hoac 5 2 9 1): ");
            // String nums = scanner.nextLine().trim();
            // System.out.println("Ket qua: " + service.sapXepTangDan(nums));

            // ========== BAI 8: Sap xep giam dan danh sach so - Input: "5,2,9,1" - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 8: SẮP XẾP GIẢM DẦN ===");
            // System.out.print("Nhap danh sach so (vd: 5,2,9,1 hoac 5 2 9 1): ");
            // String nums = scanner.nextLine().trim();
            // System.out.println("Ket qua: " + service.sapXepGiamDan(nums));

            // ========== BAI 9: Thong ke so lan xuat hien cua tu - Input: str - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 9: THỐNG KÊ TỪ ===");
            // System.out.print("Nhap chuoi van ban: ");
            // String text = scanner.nextLine().trim();
            // System.out.println("Ket qua: " + service.thongKeTu(text));

            // ========== BAI 10: Sap xep chuoi theo chu cai - Input: "zebra,apple,cat" - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 10: SẮP XẾP CHUỖI THEO BẢNG CHỮ CÁI ===");
            // System.out.print("Nhap chuoi cac tu (vd: zebra,apple,cat): ");
            // String text = scanner.nextLine().trim();
            // System.out.println("Ket qua: " + service.sapXepChuoiTheoChuCai(text));

            // ========== BAI 11: Dao nguoc chuoi - Input: str - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 11: ĐẢO NGƯỢC CHUỖI ===");
            // System.out.print("Nhap chuoi: ");
            // String text = scanner.nextLine();
            // System.out.println("Ket qua dao: " + service.daoChuoi(text));

            // ========== BAI 12: Ngat chuoi theo ky tu phan cach - Input: text, delimiter - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 12: NGẮT CHUỖI ===");
            // System.out.print("Nhap chuoi: "); String text = scanner.nextLine();
            // System.out.print("Nhap ky tu phan cach (delimiter): "); String delim = scanner.nextLine();
            // System.out.println("Ket qua: " + service.ngatChuoi(text, delim));

            // ========== BAI 13: UCLN va BCNN - Input: a, b - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 13: UCLN VÀ BCNN ===");
            // System.out.print("Nhap so a: "); long a = scanner.nextLong();
            // System.out.print("Nhap so b: "); long b = scanner.nextLong();
            // System.out.println("Ket qua: " + service.uclnVaBcnn(a, b));

            // ========== BAI 14: Giai phuong trinh bac 1 (ax + b = 0) - Input: a, b - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 14: GIẢI PHƯƠNG TRÌNH BẬC 1 ===");
            // System.out.print("Nhap he so a: "); double a = scanner.nextDouble();
            // System.out.print("Nhap he so b: "); double b = scanner.nextDouble();
            // System.out.println("Ket qua: " + service.giaiPTBac1(a, b));

            // ========== BAI 15: Giai phuong trinh bac 2 (ax^2 + bx + c = 0) - Input: a, b, c - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 15: GIẢI PHƯƠNG TRÌNH BẬC 2 ===");
            // System.out.print("Nhap he so a: "); double a = scanner.nextDouble();
            // System.out.print("Nhap he so b: "); double b = scanner.nextDouble();
            // System.out.print("Nhap he so c: "); double c = scanner.nextDouble();
            // System.out.println("Ket qua: " + service.giaiPTBac2(a, b, c));

            // ========== BAI 16: Tinh tong 1..n - Input: n - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 16: TÍNH TỔNG 1 ĐẾN N ===");
            // System.out.print("Nhap n: "); long n = scanner.nextLong();
            // System.out.println("Tong 1 den " + n + " = " + service.tong1DenN(n));

            // ========== BAI 17: Dem nguyen am va phu am - Input: str - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 17: ĐẾM NGUYÊN ÂM VÀ PHỤ ÂM ===");
            // System.out.print("Nhap chuoi: "); String text = scanner.nextLine();
            // System.out.println("Ket qua: " + service.demNguyenAmPhuAm(text));

            // ========== BAI 18: Chuan hoa chuoi (Viet hoa dau moi tu) - Input: str - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 18: CHUẨN HÓA CHUỖI ===");
            // System.out.print("Nhap chuoi can chuan hoa: "); String text = scanner.nextLine();
            // System.out.println("Ket qua: " + service.chuanHoaChuoi(text));

            // ========== BAI 19: Kiem tra chuoi Palindrome (Doi xung) - Input: str - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 19: KIỂM TRA PALINDROME ===");
            // System.out.print("Nhap chuoi: "); String text = scanner.nextLine();
            // System.out.println("Ket qua: " + (service.isPalindrome(text) ? "La chuoi Palindrome" : "Khong phai Palindrome"));

            // ========== BAI 20: Tinh giai thua (n!) - Input: n - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 20: TÍNH GIAI THỪA ===");
            // System.out.print("Nhap n: "); int n = scanner.nextInt();
            // System.out.println(n + "! = " + service.giaiThua(n));

            // ========== BAI 21: Tinh tong cac chu so - Input: 12345 - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 21: TỔNG CÁC CHỮ SỐ ===");
            // System.out.print("Nhap so nguyen: "); String numStr = scanner.nextLine().trim();
            // System.out.println("Tong cac chu so = " + service.tongCacChuSo(numStr));

            // ========== BAI 22: Tinh tong danh sach so - Input: "1,2,3,4,5" - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 22: TỔNG DANH SÁCH SỐ ===");
            // System.out.print("Nhap day so (vd: 1,2,3,4,5 hoac 1 2 3): "); String nums = scanner.nextLine().trim();
            // System.out.println("Tong = " + service.tongDanhSachSo(nums));

            // ========== BAI 23: Tim Min va Max cua danh sach so - Input: "5,2,9,1" - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 23: TÌM MIN VÀ MAX ===");
            // System.out.print("Nhap day so (vd: 5,2,9,1 hoac 5 2 9 1): "); String nums = scanner.nextLine().trim();
            // System.out.println("Ket qua: " + service.timMinMax(nums));

            // ========== BAI 24: Kiem tra chan le - Input: n - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 24: KIỂM TRA CHẴN LẺ ===");
            // System.out.print("Nhap n: "); long n = scanner.nextLong();
            // System.out.println("Ket qua: " + service.kiemTraChanLe(n));

            // ========== BAI 25: Chuyen chuoi sang IN HOA - Input: str - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 25: IN HOA ===");
            // System.out.print("Nhap chuoi: "); String text = scanner.nextLine();
            // System.out.println("Ket qua: " + service.inHoa(text));

            // ========== BAI 26: Chuyen chuoi sang in thuong - Input: str - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 26: IN THƯỜNG ===");
            // System.out.print("Nhap chuoi: "); String text = scanner.nextLine();
            // System.out.println("Ket qua: " + service.inThuong(text));

            // ========== BAI 27: Dem tong so ky tu (co space va khong space) - Input: str - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 27: ĐẾM KÝ TỰ ===");
            // System.out.print("Nhap chuoi: "); String text = scanner.nextLine();
            // System.out.println("Ket qua: " + service.demKyTu(text));

            // ========== BAI 28: Dien tich Hinh Chu Nhat - Input: dai, rong - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 28: DIỆN TÍCH HÌNH CHỮ NHẬT ===");
            // System.out.print("Nhap chieu dai: "); double dai = scanner.nextDouble();
            // System.out.print("Nhap chieu rong: "); double rong = scanner.nextDouble();
            // System.out.println("Dien tich HCN = " + service.dienTichHCN(dai, rong));

            // ========== BAI 29: Dien tich Hinh Tron - Input: r - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 29: DIỆN TÍCH HÌNH TRÒN ===");
            // System.out.print("Nhap ban kinh r: "); double r = scanner.nextDouble();
            // System.out.println("Dien tich Hinh Tron = " + service.dienTichHinhTron(r));

            // ========== BAI 30: Dien tich Hinh Thang - Input: a, b, h - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 30: DIỆN TÍCH HÌNH THANG ===");
            // System.out.print("Nhap day lon a: "); double a = scanner.nextDouble();
            // System.out.print("Nhap day be b: "); double b = scanner.nextDouble();
            // System.out.print("Nhap chieu cao h: "); double h = scanner.nextDouble();
            // System.out.println("Dien tich Hinh Thang = " + service.dienTichHinhThang(a, b, h));

            // ========== BAI 31: Chu vi Hinh Vuong - Input: side - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 31: CHU VI HÌNH VUÔNG ===");
            // System.out.print("Nhap canh hinh vuong: "); double side = scanner.nextDouble();
            // System.out.println("Chu vi Hinh Vuong = " + service.chuViHinhVuong(side));

            // ========== BAI 32: Chu vi Hinh Chu Nhat - Input: dai, rong - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 32: CHU VI HÌNH CHỮ NHẬT ===");
            // System.out.print("Nhap chieu dai: "); double dai = scanner.nextDouble();
            // System.out.print("Nhap chieu rong: "); double rong = scanner.nextDouble();
            // System.out.println("Chu vi HCN = " + service.chuViHCN(dai, rong));

            // ========== BAI 33: [ĐỀ THI GIỮA KỲ CÂU 1] Chuyen so thanh chu - Input: "3432" - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 33: CHUYỂN SỐ THÀNH CHỮ ===");
            // System.out.print("Nhap chuoi chu so (vd: 3432): ");
            // String num = scanner.nextLine().trim();
            // System.out.println("Ket qua: " + service.doiSoThanhChu(num));

            // ========== BAI 34: [ĐỀ THI GIỮA KỲ CÂU 2] Tim thong tin theo Email - Input: "abcd1234@gmail.com" - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 34: TÌM THÔNG TIN THEO EMAIL ===");
            // System.out.print("Nhap email can tim (vd: abcd1234@gmail.com): ");
            // String email = scanner.nextLine().trim();
            // System.out.println("Ket qua: " + service.timNguoiDungTheoEmail(email));

            // ========== BAI 35: [THỰC HÀNH LAB 5] Sap xep day so - Input: "11 22 4 25 28 3" - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 35: SẮP XẾP DÃY SỐ ===");
            // System.out.print("Nhap day so cach nhau khoang trang (vd: 11 22 4 25 28 3): ");
            // String daySo = scanner.nextLine().trim();
            // System.out.println("Ket qua:\n" + service.sapXepDaySo(daySo));

            // ========== BAI 36: [THỰC HÀNH TUẦN 3] Doc file van ban tren Server - Input: "users.txt" - [KHONG CAN SinhVien.java] ==========
            // System.out.println("=== BÀI 36: ĐỌC FILE VĂN BẢN TRÊN SERVER ===");
            // System.out.print("Nhap ten file can doc (vd: users.txt): ");
            // String fName = scanner.nextLine().trim();
            // System.out.println("--- NOI DUNG FILE ---\n" + service.docFile(fName));

            // ========== BAI 37: [THỰC HÀNH TUẦN 1 & 3 - ⚠️ CẦN SinhVien.java] Tim sinh vien theo ma - Input: "SV01" ==========
            // System.out.println("=== BÀI 37: TÌM SINH VIÊN THEO MÃ ===");
            // System.out.print("Nhap ma SV (vd: SV01): ");
            // String maSV = scanner.nextLine().trim();
            // SinhVien sv = service.timSinhVienTheoMa(maSV);
            // if (sv != null) System.out.println("Tim thay: " + sv);
            // else System.out.println("Khong tim thay sinh vien!");

            scanner.close();
        } catch (Exception e) {
            System.err.println("Loi Client: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
