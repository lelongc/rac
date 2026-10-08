package gkrmi;

import java.rmi.Naming;
import java.util.List;
import java.util.Scanner;

public class RMIClient {
    public static final String DEFAULT_HOST = "localhost";
    public static final int DEFAULT_PORT = 1099;
    public static final String SERVICE_NAME = "RemoteService";

    public static void main(String[] args) {
        String host = DEFAULT_HOST;
        int port = DEFAULT_PORT;

        // Ho tro truyen tham so IP va Port tu dong lenh (args) - Yeu cau bai 2 Tuan 6
        if (args.length >= 2) {
            host = args[0];
            port = Integer.parseInt(args[1]);
        }

        String rmiUrl = "rmi://" + host + ":" + port + "/" + SERVICE_NAME;

        try {
            System.out.println("Dang ket noi toi Server tai: " + rmiUrl);
            IRemoteService service = (IRemoteService) Naming.lookup(rmiUrl);
            System.out.println("Ket noi thanh cong toi RMI Server!\n");

            Scanner scanner = new Scanner(System.in);

            // =================================================================
            // KHI THI: CHỌN MẪU BÀI TƯƠNG ỨNG DƯỚI ĐÂY, UNCOMMENT VÀ CHẠY
            // =================================================================

            // ---------- MẪU 1: ĐỀ THI GIỮA KỲ CÂU 1 (CHUYỂN SỐ THÀNH CHỮ) ----------
            System.out.println("--- DEMO CÂU 1 ĐỀ THI (Chuyển số thành chữ) ---");
            String demoNum = "3432";
            System.out.println("Gửi: " + demoNum);
            System.out.println("Server trả về: " + service.doiSoThanhChu(demoNum));
            System.out.println();

            // ---------- MẪU 2: ĐỀ THI GIỮA KỲ CÂU 2 (TÌM EMAIL NGƯỜI DÙNG) ----------
            System.out.println("--- DEMO CÂU 2 ĐỀ THI (Tìm thông tin theo Email) ---");
            String demoEmail = "abcd1234@gmail.com";
            System.out.println("Gửi: " + demoEmail);
            System.out.println("Server trả về: " + service.timNguoiDungTheoEmail(demoEmail));
            System.out.println();

            // ---------- MẪU 3: LAB 5 (SẮP XẾP DÃY SỐ) ----------
            System.out.println("--- DEMO LAB 5 (Sắp xếp dãy số) ---");
            String demoDaySo = "11 22 4 25 28 3";
            System.out.println("Gửi: " + demoDaySo);
            System.out.println(service.sapXepDaySo(demoDaySo));
            System.out.println();

            // ---------- MẪU 4: MÁY TÍNH 4 PHÉP TÍNH (TUẦN 6 BÀI 3) ----------
            System.out.println("--- DEMO TUẦN 6 BÀI 3 (Máy tính) ---");
            System.out.println("10 + 5 = " + service.add(10, 5));
            System.out.println("10 - 5 = " + service.sub(10, 5));
            System.out.println("10 * 5 = " + service.mul(10, 5));
            System.out.println("10 / 5 = " + service.div(10, 5));
            System.out.println();

            // ---------- MẪU 5: TRUY VẤN ĐỐI TƯỢNG SINH VIÊN (LAB 1, 3) ----------
            System.out.println("--- DEMO ĐỐI TƯỢNG SINH VIÊN ---");
            SinhVien sv = service.timSinhVienTheoMa("SV01");
            if (sv != null) {
                System.out.println("Tìm thấy: " + sv);
            }
            System.out.println();

            // ---------- MENU NHẬP TỰ DO TỪ BÀN PHÍM (NẾU CẦN CHẠY TƯƠNG TÁC) ----------
            System.out.println("==================================================");
            System.out.println("NHẬP DỮ LIỆU TỪ BÀN PHÍM ĐỂ TEST TRỰC TIẾP");
            System.out.println("1. Nhập chuỗi số (vd: 3432)");
            System.out.println("2. Nhập email (vd: abcd1234@gmail.com)");
            System.out.println("3. Nhập dãy số cách nhau khoảng trắng (vd: 11 22 4 25 28 3)");
            System.out.println("Gõ 'exit' để thoát.");
            System.out.println("==================================================");

            while (true) {
                System.out.print("\nNhập chuỗi: ");
                String input = scanner.nextLine().trim();
                if (input.equalsIgnoreCase("exit")) break;

                // Nếu là chuỗi số nguyên -> gọi đổi số thành chữ
                if (input.matches("\\d+")) {
                    System.out.println("-> Kết quả: " + service.doiSoThanhChu(input));
                }
                // Nếu là email -> gọi tìm email
                else if (input.contains("@")) {
                    System.out.println("-> Kết quả: " + service.timNguoiDungTheoEmail(input));
                }
                // Nếu là dãy nhiều số -> gọi sắp xếp dãy số
                else {
                    System.out.println("-> Kết quả:\n" + service.sapXepDaySo(input));
                }
            }

            scanner.close();
            System.out.println("Ket thuc chuong trinh.");
        } catch (Exception e) {
            System.err.println("Loi Client: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
