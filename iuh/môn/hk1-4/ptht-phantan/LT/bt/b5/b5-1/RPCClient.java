/**
 * Lớp RPCClient giả lập trong slide Bài 1.
 * Trình diễn lời gọi hàm cục bộ thông qua con trỏ bộ nhớ (chưa phải RPC thực thụ).
 */
public class RPCClient {
    public static void main(String[] args) {
        System.out.println("=== CHƯƠNG TRÌNH GIẢ LẬP GỌI HÀM TỪ XA (BÀI 1) ===");

        // Khởi tạo đối tượng server trực tiếp trong cùng một không gian bộ nhớ JVM
        RPCServer server = new RPCServer();

        // Lời gọi hàm cục bộ (giả lập remote call)
        int result = server.add(5, 7);

        System.out.println("Kết quả nhận từ Server: " + result);
        System.out.println("==================================================");
    }
}
