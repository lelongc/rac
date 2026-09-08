import java.rmi.Remote;
import java.rmi.RemoteException;

/**
 * Giao diện từ xa (Remote Interface) cho dịch vụ Calculator.
 * - Bắt buộc kế thừa java.rmi.Remote.
 * - Các phương thức đều ném ngoại lệ java.rmi.RemoteException.
 */
public interface Calculator extends Remote {
    int add(int a, int b) throws RemoteException;
    int subtract(int a, int b) throws RemoteException;
    int multiply(int a, int b) throws RemoteException;
}
