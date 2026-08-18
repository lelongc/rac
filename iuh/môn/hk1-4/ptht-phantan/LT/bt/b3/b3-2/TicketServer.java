import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class TicketServer {
    public static final int RMI_PORT = 1099;
    public static final String SERVICE_NAME = "TicketService";

    public static void main(String[] args) {
        try {
            System.out.println("====================================================================");
            System.out.println("       HE THONG QUAN LY VE XE TRUC TUYEN (RMI + TCP SOCKET + THREAD)");
            System.out.println("====================================================================");

            // Khoi tao hoac lay RMI Registry tai cong 1099
            Registry registry;
            try {
                registry = LocateRegistry.createRegistry(RMI_PORT);
                System.out.println("[+] Khoi tao RMI Registry tai cong: " + RMI_PORT);
            } catch (Exception e) {
                registry = LocateRegistry.getRegistry(RMI_PORT);
                System.out.println("[!] Su dung RMI Registry hien co tai cong: " + RMI_PORT);
            }

            // Khoi tao Remote Object
            TicketService ticketService = new TicketServiceImpl();

            // Dang ky dich vu vao Registry
            registry.rebind(SERVICE_NAME, ticketService);

            System.out.println("[+] Dich vu '" + SERVICE_NAME + "' da duoc dang ky thanh cong tren RMI!");
            System.out.println("[+] Server san sang phuc vu cac yeu cau dat ve tu Client...");
            System.out.println("====================================================================");

        } catch (Exception e) {
            System.err.println("[-] Loi khoi dong TicketServer: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
