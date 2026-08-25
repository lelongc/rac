public class NotificationService implements OrderSubscriber {
    @Override
    public void onOrderReceived(Order order) {
        System.out.println("[NotificationService]");
        System.out.println("Received " + order.getOrderId());
        System.out.println("Sending notification...");
        try {
            Thread.sleep(600); // Mo phong thoi gian gui thong bao
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        System.out.println("Notification sent.");
        System.out.println();
    }
}
