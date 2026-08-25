public class Test1_1 {
    public static void main(String[] args) {
        System.out.println("=== KIEM TRA 1.1: CONSUMER DANG CHAY ===");
        
        MessageBroker broker = new MessageBroker();

        OrderService orderService = new OrderService();
        broker.registerConsumer(orderService);

        Customer customer = new Customer(broker);
        customer.sendOrder("ORDER-001");
        customer.sendOrder("ORDER-002");
        customer.sendOrder("ORDER-003");
    }
}
