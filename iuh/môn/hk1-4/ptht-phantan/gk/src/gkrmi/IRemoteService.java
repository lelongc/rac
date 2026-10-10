package gkrmi;

import java.rmi.Remote;
import java.rmi.RemoteException;
import java.util.List;

public interface IRemoteService extends Remote {

    // =========================================================================
    // ⚠️ QUY TẮC PHÒNG THI ĐỂ BÀI NỘP KHÔNG BỊ THỪA:
    // 1. Chỉ uncomment ĐÚNG 1 BÀI theo đề, các bài còn lại để dấu //
    //    (Uncomment đồng bộ ở cả 3 file: IRemoteService, RemoteServiceImpl, RMIClient).
    // 2. VỀ FILE SinhVien.java:
    //    CHỈ DUY NHẤT [BÀI 37: ĐỐI TƯỢNG SINH VIÊN] MỚI CẦN FILE SinhVien.java.
    //    NẾU ĐỀ RA BẤT KỲ BÀI NÀO KHÁC (BÀI 1 ĐẾN 36):
    //    -> HÃY XÓA THẲNG TAY FILE SinhVien.java ĐI ĐỂ BÀI NỘP GỌN GÀNG, KHÔNG THỪA FILE!
    // =========================================================================

    // ========== BAI 1: May tinh 4 phep tinh (+, -, *, /) - [TUAN 6 BAI 3 - MAC DINH BAT] [KHONG CAN SinhVien.java] ==========
    int add(int a, int b) throws RemoteException;
    int sub(int a, int b) throws RemoteException;
    int mul(int a, int b) throws RemoteException;
    double div(int a, int b) throws RemoteException;

    // ========== BAI 2: Tam giac (Chu vi, dien tich Heron) - Input: a, b, c - [KHONG CAN SinhVien.java] ==========
    // String tinhTamGiac(double a, double b, double c) throws RemoteException;

    // ========== BAI 3: So phuc (ADD/SUB/MUL/DIV) - Input: op, ar, ai, br, bi - [KHONG CAN SinhVien.java] ==========
    // String soPhuc(String op, double ar, double ai, double br, double bi) throws RemoteException;

    // ========== BAI 4: So Fibonacci / In day Fibonacci - Input: n - [KHONG CAN SinhVien.java] ==========
    // String fibonacci(int n) throws RemoteException;

    // ========== BAI 5: Quy doi tien te - Input: amount, from, to (USD, EUR, JPY, VND) - [KHONG CAN SinhVien.java] ==========
    // String quyDoiTienTe(double amount, String from, String to) throws RemoteException;

    // ========== BAI 6: Kiem tra so nguyen to - Input: n - [KHONG CAN SinhVien.java] ==========
    // boolean isPrime(long n) throws RemoteException;

    // ========== BAI 7: Sap xep tang dan danh sach so - Input: "5,2,9,1" - [KHONG CAN SinhVien.java] ==========
    // String sapXepTangDan(String inputNumbers) throws RemoteException;

    // ========== BAI 8: Sap xep giam dan danh sach so - Input: "5,2,9,1" - [KHONG CAN SinhVien.java] ==========
    // String sapXepGiamDan(String inputNumbers) throws RemoteException;

    // ========== BAI 9: Thong ke so lan xuat hien cua tu - Input: str - [KHONG CAN SinhVien.java] ==========
    // String thongKeTu(String str) throws RemoteException;

    // ========== BAI 10: Sap xep chuoi theo chu cai - Input: "zebra,apple,cat" - [KHONG CAN SinhVien.java] ==========
    // String sapXepChuoiTheoChuCai(String str) throws RemoteException;

    // ========== BAI 11: Dao nguoc chuoi - Input: str - [KHONG CAN SinhVien.java] ==========
    // String daoChuoi(String str) throws RemoteException;

    // ========== BAI 12: Ngat chuoi theo ky tu phan cach - Input: text, delimiter - [KHONG CAN SinhVien.java] ==========
    // String ngatChuoi(String text, String delimiter) throws RemoteException;

    // ========== BAI 13: UCLN va BCNN - Input: a, b - [KHONG CAN SinhVien.java] ==========
    // String uclnVaBcnn(long a, long b) throws RemoteException;

    // ========== BAI 14: Giai phuong trinh bac 1 (ax + b = 0) - Input: a, b - [KHONG CAN SinhVien.java] ==========
    // String giaiPTBac1(double a, double b) throws RemoteException;

    // ========== BAI 15: Giai phuong trinh bac 2 (ax^2 + bx + c = 0) - Input: a, b, c - [KHONG CAN SinhVien.java] ==========
    // String giaiPTBac2(double a, double b, double c) throws RemoteException;

    // ========== BAI 16: Tinh tong 1..n - Input: n - [KHONG CAN SinhVien.java] ==========
    // long tong1DenN(long n) throws RemoteException;

    // ========== BAI 17: Dem nguyen am va phu am - Input: str - [KHONG CAN SinhVien.java] ==========
    // String demNguyenAmPhuAm(String str) throws RemoteException;

    // ========== BAI 18: Chuan hoa chuoi (Viet hoa dau moi tu) - Input: str - [KHONG CAN SinhVien.java] ==========
    // String chuanHoaChuoi(String str) throws RemoteException;

    // ========== BAI 19: Kiem tra chuoi Palindrome (Doi xung) - Input: str - [KHONG CAN SinhVien.java] ==========
    // boolean isPalindrome(String str) throws RemoteException;

    // ========== BAI 20: Tinh giai thua (n!) - Input: n - [KHONG CAN SinhVien.java] ==========
    // long giaiThua(int n) throws RemoteException;

    // ========== BAI 21: Tinh tong cac chu so - Input: 12345 - [KHONG CAN SinhVien.java] ==========
    // int tongCacChuSo(String numberStr) throws RemoteException;

    // ========== BAI 22: Tinh tong danh sach so - Input: "1,2,3,4,5" - [KHONG CAN SinhVien.java] ==========
    // double tongDanhSachSo(String inputNumbers) throws RemoteException;

    // ========== BAI 23: Tim Min va Max cua danh sach so - Input: "5,2,9,1" - [KHONG CAN SinhVien.java] ==========
    // String timMinMax(String inputNumbers) throws RemoteException;

    // ========== BAI 24: Kiem tra chan le - Input: n - [KHONG CAN SinhVien.java] ==========
    // String kiemTraChanLe(long n) throws RemoteException;

    // ========== BAI 25: Chuyen chuoi sang IN HOA - Input: str - [KHONG CAN SinhVien.java] ==========
    // String inHoa(String str) throws RemoteException;

    // ========== BAI 26: Chuyen chuoi sang in thuong - Input: str - [KHONG CAN SinhVien.java] ==========
    // String inThuong(String str) throws RemoteException;

    // ========== BAI 27: Dem tong so ky tu (co space va khong space) - Input: str - [KHONG CAN SinhVien.java] ==========
    // String demKyTu(String str) throws RemoteException;

    // ========== BAI 28: Dien tich Hinh Chu Nhat - Input: dai, rong - [KHONG CAN SinhVien.java] ==========
    // double dienTichHCN(double dai, double rong) throws RemoteException;

    // ========== BAI 29: Dien tich Hinh Tron - Input: r - [KHONG CAN SinhVien.java] ==========
    // double dienTichHinhTron(double r) throws RemoteException;

    // ========== BAI 30: Dien tich Hinh Thang - Input: a, b, h - [KHONG CAN SinhVien.java] ==========
    // double dienTichHinhThang(double a, double b, double h) throws RemoteException;

    // ========== BAI 31: Chu vi Hinh Vuong - Input: side - [KHONG CAN SinhVien.java] ==========
    // double chuViHinhVuong(double side) throws RemoteException;

    // ========== BAI 32: Chu vi Hinh Chu Nhat - Input: dai, rong - [KHONG CAN SinhVien.java] ==========
    // double chuViHCN(double dai, double rong) throws RemoteException;

    // ========== BAI 33: [ĐỀ THI GIỮA KỲ CÂU 1] Chuyen so thanh chu - Input: "3432" - [KHONG CAN SinhVien.java] ==========
    // String doiSoThanhChu(String numberStr) throws RemoteException;

    // ========== BAI 34: [ĐỀ THI GIỮA KỲ CÂU 2] Tim thong tin theo Email - Input: "abcd1234@gmail.com" - [KHONG CAN SinhVien.java] ==========
    // String timNguoiDungTheoEmail(String email) throws RemoteException;

    // ========== BAI 35: [THỰC HÀNH LAB 5] Sap xep day so - Input: "11 22 4 25 28 3" - [KHONG CAN SinhVien.java] ==========
    // String sapXepDaySo(String inputNumbers) throws RemoteException;

    // ========== BAI 36: [THỰC HÀNH TUẦN 3] Doc file van ban tren Server - Input: "users.txt" - [KHONG CAN SinhVien.java] ==========
    // String docFile(String fileName) throws RemoteException;

    // ========== BAI 37: [THỰC HÀNH TUẦN 1 & 3 - ⚠️ CẦN SinhVien.java] Tim sinh vien theo ma - Input: "SV01" ==========
    // SinhVien timSinhVienTheoMa(String maSV) throws RemoteException;
}
