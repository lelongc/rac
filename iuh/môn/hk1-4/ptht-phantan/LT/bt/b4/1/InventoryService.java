public class InventoryService implements OrderSubscriber {
    @Override
    public void onOrderReceived(Order order) {
        System.out.println("[InventoryService]");
        System.out.println("Received " + order.getOrderId());
        System.out.println("Checking and updating inventory for product: " + order.getProductName() + "...");
        try {
            Thread.sleep(700); // Mo phong thoi gian kiem tra va cap nhat kho
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        System.out.println("Inventory updated.");
        System.out.println();
    }
}
