public interface OrderSubscriber {
    /**
     * Nhan va xu ly don hang duoc phat tu Message Broker
     * @param order Thong tin don hang
     */
    void onOrderReceived(Order order);
}
