package gkrmi;

import java.rmi.Remote;
import java.rmi.RemoteException;
import java.util.List;

public interface IRemoteService extends Remote {

    // =========================================================================
    // KHI THI: CHỈ CẦN GIỮ LẠI HÀM ĐỀ YÊU CẦU, XÓA CÁC HÀM KHÁC
    // (HOẶC ĐỂ NGUYÊN CẢ BỘ CŨNG HOẠT ĐỘNG BÌNH THƯỜNG KHÔNG BỊ LỖI)
    // =========================================================================

    // ========== NHÓM 1: TOÁN HỌC & MÁY TÍNH (TUẦN 6 - BÀI 3) ==========
    int add(int a, int b) throws RemoteException;
    int sub(int a, int b) throws RemoteException;
    int mul(int a, int b) throws RemoteException;
    double div(int a, int b) throws RemoteException;
    boolean isPrime(long n) throws RemoteException;
    long giaiThua(int n) throws RemoteException;
    long fibonacci(int n) throws RemoteException;
    String dayFibonacci(int n) throws RemoteException;
    long gcd(long a, long b) throws RemoteException;
    long lcm(long a, long b) throws RemoteException;
    String giaiPTBac1(double a, double b) throws RemoteException;
    String giaiPTBac2(double a, double b, double c) throws RemoteException;
    String tinhTamGiac(double a, double b, double c) throws RemoteException;

    // ========== NHÓM 2: XỬ LÝ CHUỖI (TRỌNG TÂM ĐỀ THI GIỮA KỲ CÂU 1) ==========
    // ĐỀ THI GIỮA KỲ: "3432" -> "3432: ba bốn ba hai"
    String doiSoThanhChu(String numberStr) throws RemoteException;
    String daoChuoi(String str) throws RemoteException;
    String inHoa(String str) throws RemoteException;
    String inThuong(String str) throws RemoteException;
    String chuanHoaChuoi(String str) throws RemoteException;
    String demKyTu(String str) throws RemoteException;
    String thongKeTu(String str) throws RemoteException;
    boolean isPalindrome(String str) throws RemoteException;

    // ========== NHÓM 3: DÃY SỐ / MẢNG (TRỌNG TÂM LAB 5) ==========
    // Input chuỗi: "11 22 4 25 28 3" -> trả về chuỗi gốc, sắp giảm, sắp tăng
    String sapXepDaySo(String inputNumbers) throws RemoteException;
    String timMaxMinTong(String inputNumbers) throws RemoteException;

    // ========== NHÓM 4: ĐỐI TƯỢNG & TÌM KIẾM (TRỌNG TÂM ĐỀ THI GIỮA KỲ CÂU 2 & LAB 1, 3) ==========
    // ĐỀ THI GIỮA KỲ: Tìm thông tin người dùng theo email -> Họ tên + SĐT
    String timNguoiDungTheoEmail(String email) throws RemoteException;
    SinhVien timSinhVienTheoMa(String maSV) throws RemoteException;
    boolean themSinhVien(SinhVien sv) throws RemoteException;
    List<SinhVien> getDanhSachSinhVien() throws RemoteException;
}
