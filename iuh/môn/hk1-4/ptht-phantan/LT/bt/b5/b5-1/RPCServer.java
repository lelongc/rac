/**
 * Lớp RPCServer giả lập trong slide Bài 1.
 * Đây là lớp cục bộ thông thường, chưa có cơ chế giao tiếp mạng hay RMI.
 */
public class RPCServer {
    public int add(int a, int b) {
        System.out.println("[Server] Nhận yêu cầu cộng: " + a + " + " + b);
        return a + b;
    }
}
