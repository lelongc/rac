import java.net.MalformedURLException;
import java.rmi.AlreadyBoundException;
import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;

public class rmiServer {
    public static void main(String[] args) {
        try {
            LocateRegistry.createRegistry(1100);
            System.out.println("Server start.....");
            
            phepCong_impl obj = new phepCong_impl();
            Naming.bind("rmi://localhost:1100/congService", obj);
            
            xulychuoi_impl obj2 = new xulychuoi_impl();
            Naming.bind("rmi://localhost:1100/chuoiService", obj2);
            
        } catch (RemoteException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (MalformedURLException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (AlreadyBoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }
}