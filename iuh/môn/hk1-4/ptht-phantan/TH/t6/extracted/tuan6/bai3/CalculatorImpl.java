package tuan6.bai3;

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

/**
 * Bài 3: Cài đặt chi tiết các dịch vụ cộng, trừ, nhân, chia.
 */
public class CalculatorImpl extends UnicastRemoteObject implements Calculator {
    public CalculatorImpl() throws RemoteException {
        super();
    }

    @Override
    public int add(int a, int b) throws RemoteException {
        return a + b;
    }

    @Override
    public int sub(int a, int b) throws RemoteException {
        return a - b;
    }

    @Override
    public int mul(int a, int b) throws RemoteException {
        return a * b;
    }

    @Override
    public double div(int a, int b) throws RemoteException {
        if (b == 0) {
            throw new ArithmeticException("Lỗi: Không thể chia cho 0!");
        }
        return (double) a / b;
    }
}
