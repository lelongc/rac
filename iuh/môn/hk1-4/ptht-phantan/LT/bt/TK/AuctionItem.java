import java.io.Serializable;

public class AuctionItem implements Serializable {
    private static final long serialVersionUID = 1L;

    private String id;
    private String name;
    private double startingPrice;
    private double currentPrice;
    private String highestBidder;
    private boolean isOpen;

    public AuctionItem(String id, String name, double startingPrice) {
        this.id = id;
        this.name = name;
        this.startingPrice = startingPrice;
        this.currentPrice = startingPrice;
        this.highestBidder = "Chua co";
        this.isOpen = true;
    }

    public String getId() {
        return id;
    }

    public String getName() {
        return name;
    }

    public double getStartingPrice() {
        return startingPrice;
    }

    public synchronized double getCurrentPrice() {
        return currentPrice;
    }

    public synchronized String getHighestBidder() {
        return highestBidder;
    }

    public synchronized boolean isOpen() {
        return isOpen;
    }

    public synchronized void setOpen(boolean open) {
        this.isOpen = open;
    }

    public synchronized boolean updateBid(String bidder, double amount) {
        if (!isOpen) {
            return false;
        }
        if (amount > currentPrice) {
            this.currentPrice = amount;
            this.highestBidder = bidder;
            return true;
        }
        return false;
    }

    @Override
    public synchronized String toString() {
        return String.format("[%s] %s | Khoi diem: %,.0f VND | Gia hien tai: %,.0f VND | Giu gia: %s | Trang thai: %s",
                id, name, startingPrice, currentPrice, highestBidder, (isOpen ? "Dang mo" : "Da ket thuc"));
    }
}
