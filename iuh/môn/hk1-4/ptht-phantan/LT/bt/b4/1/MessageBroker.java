import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class MessageBroker {
    private final Queue<String> messageQueue = new LinkedList<>();
    private final List<OrderService> consumers = new ArrayList<>();
    private int currentConsumerIndex = 0;

    public void sendMessage(String orderId) {
        System.out.println("[Broker] Message received " + orderId);
        
        if (!consumers.isEmpty()) {
            // Phan phoi luan phien Round-Robin (Moi order chi do 1 Consumer xu ly)
            OrderService consumer = consumers.get(currentConsumerIndex);
            currentConsumerIndex = (currentConsumerIndex + 1) % consumers.size();
            consumer.processOrder(orderId);
        } else {
            messageQueue.add(orderId);
        }
    }

    public void registerConsumer(OrderService consumer) {
        this.consumers.add(consumer);
        
        // Xu ly cac message dang cho san trong hang doi
        while (!messageQueue.isEmpty()) {
            String pendingOrder = messageQueue.poll();
            consumer.receivePendingOrder(pendingOrder);
        }
    }
}
