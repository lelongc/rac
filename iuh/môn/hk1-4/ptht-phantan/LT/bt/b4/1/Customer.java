public class Customer {
    private MessageBroker broker;

    public Customer(MessageBroker broker) {
        this.broker = broker;
    }

    /**
     */
    public void sendOrder(String orderId) {
        System.out.println("[Customer] Sending " + orderId);
        broker.sendMessage(orderId);
    }
}
