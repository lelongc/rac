import java.rmi.Remote;
import java.rmi.RemoteException;

public interface IService extends Remote {
    // Ham da nang xu ly moi dang bai:
    String solve(String input) throws RemoteException;

    // Cac ham cu the theo de bai Tuan 6 & Tuan 7:
    int add(int a, int b) throws RemoteException;
    int sub(int a, int b) throws RemoteException;
    int mul(int a, int b) throws RemoteException;
    double div(int a, int b) throws RemoteException;
    int gcd(int a, int b) throws RemoteException;
    boolean isPrime(int n) throws RemoteException;
}

