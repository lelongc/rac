import java.rmi.Remote;
import java.rmi.RemoteException;

/**
 * Giao diện từ xa (Remote Interface) cho dịch vụ tính giai thừa.
 * - Bắt buộc extends java.rmi.Remote.
 * - Phương thức ném RemoteException theo chuẩn Java RMI.
 */
public interface FactorialService extends Remote {
    long factorial(int n) throws RemoteException;
}
