import java.io.PrintWriter;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.CopyOnWriteArrayList;

public class AuctionServiceImpl extends UnicastRemoteObject implements AuctionService {
    private static final long serialVersionUID = 1L;

    private final Map<String, AuctionItem> items = new ConcurrentHashMap<>();
    private final Set<String> participants = ConcurrentHashMap.newKeySet();
    private final List<PrintWriter> socketClients = new CopyOnWriteArrayList<>();
    private final int socketPort;

    public AuctionServiceImpl(int rmiPort, int socketPort) throws RemoteException {
        super(rmiPort);
        this.socketPort = socketPort;
        initData();
    }

    private void initData() {
        items.put("SP01", new AuctionItem("SP01", "Laptop Dell XPS 15", 20000000.0));
        items.put("SP02", new AuctionItem("SP02", "iPhone 15 Pro Max", 25000000.0));
        items.put("SP03", new AuctionItem("SP03", "Dong ho Rolex Submariner", 150000000.0));
        items.put("SP04", new AuctionItem("SP04", "May anh Sony A7 Mark IV", 45000000.0));
    }

    public void addSocketClient(PrintWriter out) {
        socketClients.add(out);
    }

    public void removeSocketClient(PrintWriter out) {
        socketClients.remove(out);
    }

    public void broadcastSocket(String message) {
        for (PrintWriter out : socketClients) {
            try {
                out.println(message);
            } catch (Exception e) {
                socketClients.remove(out);
            }
        }
    }

    @Override
    public List<AuctionItem> getItems() throws RemoteException {
        return new ArrayList<>(items.values());
    }

    @Override
    public AuctionItem getItem(String itemId) throws RemoteException {
        return items.get(itemId);
    }

    @Override
    public boolean registerUser(String username) throws RemoteException {
        if (username == null || username.trim().isEmpty()) {
            return false;
        }
        boolean added = participants.add(username.trim());
        if (added) {
            broadcastSocket(String.format("[HE THONG] Nguoi dung '%s' da tham gia he thong dau gia.", username.trim()));
        }
        return true;
    }

    @Override
    public List<String> getParticipants() throws RemoteException {
        return new ArrayList<>(participants);
    }

    @Override
    public boolean placeBid(String itemId, String username, double amount) throws RemoteException {
        AuctionItem item = items.get(itemId);
        if (item == null) {
            return false;
        }

        boolean success;
        synchronized (item) {
            success = item.updateBid(username, amount);
        }

        if (success) {
            String notification = String.format(
                "[PHIEN DAU GIA TCP] Cap nhat: San pham '%s' (%s) | Gia moi nhat: %,.0f VND | Nguoi giu gia cao nhat: %s",
                item.getName(), item.getId(), item.getCurrentPrice(), item.getHighestBidder()
            );
            broadcastSocket(notification);
        }
        return success;
    }

    @Override
    public int getSocketPort() throws RemoteException {
        return socketPort;
    }
}
