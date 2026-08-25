import java.util.LinkedList;
import java.util.Queue;

public class MessageBroker {
    private final Queue<String> messageQueue = new LinkedList<>();
    private OrderService consumer = null;

    public void sendMessage(String orderId) {
        System.out.println("[Broker] Message received " + orderId);
        
        if (consumer != null) {
            consumer.processOrder(orderId);
        } else {
            messageQueue.add(orderId);
        }
    }

    /**
     */
    public void registerConsumer(OrderService consumer) {
        this.consumer = consumer;
        
        // Xu ly cac message dang cho san trong hang doi
        while (!messageQueue.isEmpty()) {
            String pendingOrder = messageQueue.poll();
            this.consumer.receivePendingOrder(pendingOrder);
        }
    }
}
