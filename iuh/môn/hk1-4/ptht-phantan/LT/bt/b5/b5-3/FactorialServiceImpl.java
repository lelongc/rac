import java.rmi.RemoteException;

/**
 * Lớp cài đặt nghiệp vụ tính giai thừa phía Server (Máy A).
 * - Sử dụng thuật toán lặp chống tràn ngăn xếp (StackOverflowError).
 * - Kiểm tra số âm và giới hạn kiểu dữ liệu long (tối đa n = 20).
 */
public class FactorialServiceImpl implements FactorialService {

    public FactorialServiceImpl() {
        super();
    }

    @Override
    public long factorial(int n) throws RemoteException {
        System.out.println("[Server] Nhận yêu cầu tính giai thừa của n = " + n);
        if (n < 0) {
            throw new IllegalArgumentException("Không tính được giai thừa cho số âm: " + n);
        }
        if (n > 20) {
            throw new IllegalArgumentException("Giá trị n = " + n + " vượt quá giới hạn biểu diễn của kiểu long (tối đa n = 20)!");
        }
        long result = 1;
        for (int i = 2; i <= n; i++) {
            result *= i;
        }
        return result;
    }
}
