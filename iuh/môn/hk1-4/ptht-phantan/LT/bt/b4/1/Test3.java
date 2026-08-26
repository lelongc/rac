public class Test3 {
    public static void main(String[] args) {
        System.out.println("=== KIEM TRA 3: NHIEU NGUOI TIEU DUNG (COMPETING CONSUMERS) ===");
        System.out.println("Mo hinh: 1 Message Broker phan phoi cho 2 Service (Service-1 va Service-2)\n");

        // 1. Khoi tao Message Broker
        MessageBroker broker = new MessageBroker();

        // 2. Them OrderService-1 va OrderService-2
        OrderService service1 = new OrderService("Service-1");
        OrderService service2 = new OrderService("Service-2");
        broker.registerConsumer(service1);
        broker.registerConsumer(service2);

        // 3. Customer gui 4 don hang
        Customer customer = new Customer(broker);
        customer.sendOrder("ORDER-001");
        customer.sendOrder("ORDER-002");
        customer.sendOrder("ORDER-003");
        customer.sendOrder("ORDER-004");

        System.out.println("--> Ghi chu: Moi don hang chi duoc 1 Service nhan va xu ly (khong bi trung lap).");
    }
}
