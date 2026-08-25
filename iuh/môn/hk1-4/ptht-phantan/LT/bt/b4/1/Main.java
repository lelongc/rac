public class Main {
    public static void main(String[] args) {
        System.out.println("==================================================================");
        System.out.println("     CHUONG TRINH KIEM TRA HE THONG MESSAGE BROKER (BAI TAP 4)    ");
        System.out.println("==================================================================\n");

        // ---------------------------------------------------------
        // KIEM TRA 1.1: CONSUMER DANG CHAY
        // ---------------------------------------------------------
        System.out.println(">>> 1. KIEM TRA 1.1: CONSUMER DANG CHAY <<<");
        MessageBroker broker1 = new MessageBroker();
        OrderService orderService1 = new OrderService();
        broker1.registerConsumer(orderService1);

        Customer customer1 = new Customer(broker1);
        customer1.sendOrder("ORDER-001");
        customer1.sendOrder("ORDER-002");
        customer1.sendOrder("ORDER-003");

        System.out.println("\n------------------------------------------------------------------\n");

        // ---------------------------------------------------------
        // KIEM TRA 1.2: CONSUMER CHUA CHAY (TIME-UNCOUPLED)
        // ---------------------------------------------------------
        System.out.println(">>> 2. KIEM TRA 1.2: CONSUMER CHUA CHAY (MESSAGE QUEUE) <<<");
        MessageBroker broker2 = new MessageBroker();
        Customer customer2 = new Customer(broker2);

        System.out.println("--> Cho Customer gui message truoc (Chua chay OrderService):");
        customer2.sendOrder("ORDER-001");
        customer2.sendOrder("ORDER-002");
        customer2.sendOrder("ORDER-003");

        System.out.println("\n--> Sau do moi khoi dong OrderService:");
        System.out.println("Ket qua:");
        OrderService orderService2 = new OrderService();
        broker2.registerConsumer(orderService2);

        System.out.println("\n==================================================================");
    }
}
