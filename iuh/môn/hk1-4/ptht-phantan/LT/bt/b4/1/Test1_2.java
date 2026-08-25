public class Test1_2 {
    public static void main(String[] args) {
        System.out.println("=== KIEM TRA 1.2: CONSUMER CHUA CHAY ===");

        MessageBroker broker = new MessageBroker();
        Customer customer = new Customer(broker);

        System.out.println("--> Customer gui 3 don hang vao Broker trong khi OrderService CHUA BAT:");
        customer.sendOrder("ORDER-001");
        customer.sendOrder("ORDER-002");
        customer.sendOrder("ORDER-003");

        System.out.println("\n--> Sau do moi khoi dong OrderService (Lay toan bo message ton trong Queue):");
        OrderService orderService = new OrderService();
        broker.registerConsumer(orderService);
    }
}
