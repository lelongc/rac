package tuan6.bai3;

import java.rmi.Naming;
import java.util.Scanner;

public class RMIClient {
    public static void main(String[] args) {
        try {
            String rmiUrl = "rmi://localhost:1099/CalculatorService";
            System.out.println("Đang tìm kiếm dịch vụ tại: " + rmiUrl);

            Calculator stub = (Calculator) Naming.lookup(rmiUrl);
            System.out.println("Kết nối tới CalculatorService thành công!");

            Scanner scanner = new Scanner(System.in);
            System.out.print("Nhập số nguyên thứ nhất (a): ");
            int a = scanner.nextInt();
            System.out.print("Nhập số nguyên thứ hai (b): ");
            int b = scanner.nextInt();

            System.out.println("=== KẾT QUẢ GỌI DỊCH VỤ RMI TỪ SERVER ===");
            System.out.println(a + " + " + b + " = " + stub.add(a, b));
            System.out.println(a + " - " + b + " = " + stub.sub(a, b));
            System.out.println(a + " * " + b + " = " + stub.mul(a, b));

            try {
                double divResult = stub.div(a, b);
                System.out.println(a + " / " + b + " = " + divResult);
            } catch (Exception ex) {
                System.out.println(a + " / " + b + " = Lỗi chia cho 0: " + ex.getMessage());
            }

            scanner.close();
        } catch (Exception e) {
            System.err.println("Lỗi Client: " + e.getMessage());
        }
    }
}
