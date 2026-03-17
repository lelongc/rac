package b8;
import java.io.*;
import java.net.Socket;
/*
 * Bai 8 - ClientHandler
 * Parse thong diep, tinh + - * /, xu ly loi va tra ket qua.
 */
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
    private String format(double v) {
        return (v == Math.floor(v) && !Double.isInfinite(v))
                ? String.valueOf((long) v)
                : String.format("%.2f", v);
    }
}