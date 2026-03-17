import java.rmi.Remote;
import java.rmi.RemoteException;

public interface xulychuoi_intf extends Remote {
    public String noi2chuoi(String str1, String str2) throws RemoteException;
}