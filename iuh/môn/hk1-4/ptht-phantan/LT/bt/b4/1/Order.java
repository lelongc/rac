public class Order {
    private String orderId;
    private String productName;
    private double price;

    public Order(String orderId, String productName, double price) {
        this.orderId = orderId;
        this.productName = productName;
        this.price = price;
    }

    public String getOrderId() {
        return orderId;
    }

    public String getProductName() {
        return productName;
    }

    public double getPrice() {
        return price;
    }

    @Override
    public String toString() {
        return orderId + " | " + productName + " | " + String.format("%.0f", price);
    }
}
