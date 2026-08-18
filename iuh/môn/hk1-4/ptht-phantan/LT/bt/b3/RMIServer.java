import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class RMIServer {
    public static final int RMI_PORT = 1099;
    public static final String SERVICE_NAME = "GameService";

    public static void main(String[] args) {
        try {
            System.out.println("=================================================");
            System.out.println("      KHOI DONG RMI SERVER - TRO CHOI DOAN SO     ");
            System.out.println("=================================================");

            // Khoi tao RMI Registry tai cong 1099
            Registry registry;
            try {
                registry = LocateRegistry.createRegistry(RMI_PORT);
                System.out.println("[+] Khoi tao RMI Registry thanh cong tai cong: " + RMI_PORT);
            } catch (Exception e) {
                registry = LocateRegistry.getRegistry(RMI_PORT);
                System.out.println("[!] Su dung RMI Registry hien co tai cong: " + RMI_PORT);
            }

            // Tao doi tuong Remote Service
            GameService gameService = new GameServiceImpl();

            // Dang ky (Bind) dich vu vao Registry
            registry.rebind(SERVICE_NAME, gameService);

            System.out.println("[+] Dich vu '" + SERVICE_NAME + "' da duoc dang ky thanh cong!");
            System.out.println("[+] Server dang lang nghe va san sang phuc vu cac Client...");
            System.out.println("=================================================");

        } catch (Exception e) {
            System.err.println("[-] Loi khoi dong RMI Server: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
