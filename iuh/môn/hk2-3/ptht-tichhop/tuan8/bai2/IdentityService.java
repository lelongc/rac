package bai2;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface IdentityService extends Remote {
    String lookup(String idNumber) throws RemoteException;
    
}