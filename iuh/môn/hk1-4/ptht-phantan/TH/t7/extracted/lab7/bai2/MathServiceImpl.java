package lab7.bai2;

import java.rmi.server.UnicastRemoteObject;
import java.rmi.RemoteException;

public class MathServiceImpl extends UnicastRemoteObject implements MathService {
    
    public MathServiceImpl() throws RemoteException {
        super();
    }

    @Override
    public int findGCD(int a, int b) throws RemoteException {
        a = Math.abs(a);
        b = Math.abs(b);
        if (a == 0 || b == 0) return a + b;
        while (a != b) {
            if (a > b) a = a - b;
            else b = b - a;
        }
        return a;
    }

    @Override
    public String checkPrime(int a, int b) throws RemoteException {
        boolean aIsPrime = isPrime(a);
        boolean bIsPrime = isPrime(b);
        
        String result = "";
        if (aIsPrime) result += a + " là số nguyên tố. ";
        else result += a + " không phải số nguyên tố. ";
        
        if (bIsPrime) result += b + " là số nguyên tố.";
        else result += b + " không phải số nguyên tố.";
        
        return result;
    }
    
    private boolean isPrime(int n) {
        if (n <= 1) return false;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}
