package lab7.bai2;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface MathService extends Remote {
    int findGCD(int a, int b) throws RemoteException;
    String checkPrime(int a, int b) throws RemoteException;
}
