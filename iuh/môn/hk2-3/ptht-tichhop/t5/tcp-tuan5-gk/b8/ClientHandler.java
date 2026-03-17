package b8;

import java.io.*;
import java.net.Socket;

// Giao thức:
// Client gửi chuỗi dạng "OP Operand1 Operand2\n"
//   ví dụ: "+ 100 200\n"  →  server tính 100+200=300, trả về "300\n"
// Client gửi "exit\n" để ngắt kết nối
public class ClientHandler extends Thread {
    private final Socket socket;

    public ClientHandler(Socket socket) {
        this.socket = socket;
    }

    @Override
    public void run() {
        try (BufferedReader reader = new BufferedReader(
                 new InputStreamReader(socket.getInputStream()));
             PrintWriter writer = new PrintWriter(socket.getOutputStream(), true)) {

            String msg;
            while ((msg = reader.readLine()) != null) {
                msg = msg.trim();
                if (msg.equalsIgnoreCase("exit")) {
                    writer.println("Bye!");
                    break;
                }

                String result = calculate(msg);
                System.out.println("Nhan: [" + msg + "]  =>  Tra ve: " + result);
                writer.println(result);
            }

        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try { socket.close(); } catch (IOException e) {}
        }
        System.out.println("Client ngat ket noi: " + socket.getInetAddress());
    }

    // Phân tích và tính "OP op1 op2"
    private String calculate(String expr) {
        String[] parts = expr.split("\\s+");
        if (parts.length != 3) return "Loi: dinh dang phai la 'OP so1 so2'";

        char op;
        double a, b;
        try {
            op = parts[0].charAt(0);
            a  = Double.parseDouble(parts[1]);
            b  = Double.parseDouble(parts[2]);
        } catch (NumberFormatException e) {
            return "Loi: Operand khong phai so";
        }

        switch (op) {
            case '+': return format(a + b);
            case '-': return format(a - b);
            case '*': return format(a * b);
            case '/':
                if (b == 0) return "Loi: Chia cho 0";
                return format(a / b);
            default:
                return "Loi: OP phai la + - * /";
        }
    }

    // Trả về số nguyên nếu không có phần thập phân, ngược lại giữ 2 chữ số
    private String format(double v) {
        return (v == Math.floor(v) && !Double.isInfinite(v))
                ? String.valueOf((long) v)
                : String.format("%.2f", v);
    }
}
