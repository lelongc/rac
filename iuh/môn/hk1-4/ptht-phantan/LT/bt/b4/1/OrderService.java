public class OrderService {
    private String name = "OrderService";

    public OrderService() {
    }

    public OrderService(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    /**
     * Xu ly don hang khi Consumer dang chay (Kiem tra 1.1 va Kiem tra 3)
     */
    public void processOrder(String orderId) {
        System.out.println("[" + name + "] Received " + orderId);
        System.out.println("[" + name + "] Completed " + orderId);
        System.out.println(orderId + " -> " + name);
        System.out.println();
    }

    /**
     * Nhan cac don hang ton dong trong Queue khi vua khoi dong (Kiem tra 1.2)
     */
    public void receivePendingOrder(String orderId) {
        System.out.println("[" + name + "] Received " + orderId);
    }
}
