package bai1;


import java.rmi.Remote;
import java.rmi.RemoteException;

public interface CalcService extends Remote {
    String evaluate(String expression) throws RemoteException; 
    
}