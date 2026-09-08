import java.rmi.RemoteException;

/**
 * Lớp cài đặt nghiệp vụ tính toán (Business Logic) trên Server.
 * - Chỉ implements Calculator (không bị ép extends UnicastRemoteObject).
 */
public class CalculatorImpl implements Calculator {

    public CalculatorImpl() {
        super();
    }

    @Override
    public int add(int a, int b) throws RemoteException {
        System.out.println("[Server] Thực hiện phép cộng: " + a + " + " + b);
        return a + b;
    }

    @Override
    public int subtract(int a, int b) throws RemoteException {
        System.out.println("[Server] Thực hiện phép trừ: " + a + " - " + b);
        return a - b;
    }

    @Override
    public int multiply(int a, int b) throws RemoteException {
        System.out.println("[Server] Thực hiện phép nhân: " + a + " * " + b);
        return a * b;
    }
}
