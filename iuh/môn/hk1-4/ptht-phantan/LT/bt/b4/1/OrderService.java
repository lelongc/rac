public class OrderService {
    /**
     * Xu ly don hang khi Consumer dang chay (Kiem tra 1.1)
     */
    public void processOrder(String orderId) {
        System.out.println("[OrderService] Received " + orderId);
        System.out.println("[OrderService] Completed " + orderId);
        System.out.println();
    }

    /**
     * Nhan cac don hang ton dong trong Queue khi vua khoi dong (Kiem tra 1.2)
     */
    public void receivePendingOrder(String orderId) {
        System.out.println("[OrderService] Received " + orderId);
    }
}
