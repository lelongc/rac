package tuan6.bai3;

import java.rmi.Remote;
import java.rmi.RemoteException;

/**
 * Bài 3: Giao diện dịch vụ tính toán mở rộng:
 * Cộng, Trừ, Nhân, Chia hai số nguyên.
 */
public interface Calculator extends Remote {
    public int add(int a, int b) throws RemoteException;
    public int sub(int a, int b) throws RemoteException;
    public int mul(int a, int b) throws RemoteException;
    public double div(int a, int b) throws RemoteException;
}
