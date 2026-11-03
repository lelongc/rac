import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

public class Server {
    public static void main(String[] args) throws Exception {
        int port = args.length > 0 ? Integer.parseInt(args[0]) : 1099;
        try {
            LocateRegistry.createRegistry(port);
        } catch (Exception ignored) {}
        Naming.rebind("rmi://localhost:" + port + "/Service", new ServiceImpl());
        System.out.println("RMI Server running on port " + port + "...");
    }
}

