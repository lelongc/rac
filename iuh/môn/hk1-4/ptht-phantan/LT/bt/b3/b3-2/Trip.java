import java.io.Serializable;

public class Trip implements Serializable {
    private static final long serialVersionUID = 1L;

    private String tripId;
    private String route;
    private String departureTime;
    private int totalSeats;
    private int availableSeats;
    private double price;

    public Trip(String tripId, String route, String departureTime, int totalSeats, double price) {
        this.tripId = tripId;
        this.route = route;
        this.departureTime = departureTime;
        this.totalSeats = totalSeats;
        this.availableSeats = totalSeats;
        this.price = price;
    }

    public String getTripId() {
        return tripId;
    }

    public String getRoute() {
        return route;
    }

    public String getDepartureTime() {
        return departureTime;
    }

    public int getTotalSeats() {
        return totalSeats;
    }

    public synchronized int getAvailableSeats() {
        return availableSeats;
    }

    public double getPrice() {
        return price;
    }

    /**
     * Dat ghe dong bo tranh xung dot khi nhieu nguoi dat cung luc
     */
    public synchronized boolean bookSeats(int count) {
        if (count > 0 && count <= availableSeats) {
            availableSeats -= count;
            return true;
        }
        return false;
    }

    @Override
    public String toString() {
        return String.format("[%-5s] %-25s | Gio: %-15s | Con: %2d/%2d ghe | Gia: %,.0f VND/ve",
                tripId, route, departureTime, availableSeats, totalSeats, price);
    }
}
