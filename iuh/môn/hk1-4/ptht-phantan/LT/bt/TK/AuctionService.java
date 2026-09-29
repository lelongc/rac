import java.rmi.Remote;
import java.rmi.RemoteException;
import java.util.List;

public interface AuctionService extends Remote {
    List<AuctionItem> getItems() throws RemoteException;
    AuctionItem getItem(String itemId) throws RemoteException;
    boolean registerUser(String username) throws RemoteException;
    List<String> getParticipants() throws RemoteException;
    boolean placeBid(String itemId, String username, double amount) throws RemoteException;
    int getSocketPort() throws RemoteException;
}
