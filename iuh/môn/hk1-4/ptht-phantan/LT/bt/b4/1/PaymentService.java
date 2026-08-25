public class PaymentService implements OrderSubscriber {
    @Override
    public void onOrderReceived(Order order) {
        System.out.println("[PaymentService]");
        System.out.println("Received " + order.getOrderId());
        System.out.println("Processing payment...");
        try {
            Thread.sleep(800); // Mo phong thoi gian xu ly thanh toan
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        System.out.println("Payment completed.");
        System.out.println();
    }
}
