import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class xulychuoi_impl extends UnicastRemoteObject implements xulychuoi_intf {

    protected xulychuoi_impl() throws RemoteException {
        super();
        // TODO Auto-generated constructor stub
    }

    @Override
    public String noi2chuoi(String str1, String str2) throws RemoteException {
        return str1 + str2;
    }
}