import java.net.ServerSocket;
import java.net.Socket;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class AuctionServer {
    public static final int DEFAULT_RMI_PORT = 1099;
    public static final int DEFAULT_SOCKET_PORT = 5000;
    public static final String SERVICE_NAME = "AuctionService";

    public static void main(String[] args) {
        int rmiPort = DEFAULT_RMI_PORT;
        int socketPort = DEFAULT_SOCKET_PORT;

        String envRmiPort = System.getenv("RMI_PORT");
        if (envRmiPort != null && !envRmiPort.trim().isEmpty()) {
            try {
                rmiPort = Integer.parseInt(envRmiPort.trim());
            } catch (NumberFormatException ignored) {}
        }

        String envSocketPort = System.getenv("SOCKET_PORT");
        if (envSocketPort != null && !envSocketPort.trim().isEmpty()) {
            try {
                socketPort = Integer.parseInt(envSocketPort.trim());
            } catch (NumberFormatException ignored) {}
        }

        String rmiHost = System.getenv("RMI_HOST");
        if (rmiHost != null && !rmiHost.trim().isEmpty()) {
            System.setProperty("java.rmi.server.hostname", rmiHost.trim());
        }

        try {
            AuctionServiceImpl auctionService = new AuctionServiceImpl(0, socketPort);
            Registry registry = LocateRegistry.createRegistry(rmiPort);
            registry.rebind(SERVICE_NAME, auctionService);

            System.out.println("==================================================");
            System.out.println("       HE THONG DAU GIA PHAN TAN - SERVER         ");
            System.out.println("==================================================");
            System.out.println("[RMI] Dang lang nghe tai cong: " + rmiPort);
            System.out.println("[RMI] Ten dich vu: " + SERVICE_NAME);
            System.out.println("[SOCKET TCP] Dang khoi dong tren cong: " + socketPort);

            int finalSocketPort = socketPort;
            Thread socketServerThread = new Thread(() -> {
                try (ServerSocket serverSocket = new ServerSocket(finalSocketPort)) {
                    System.out.println("[SOCKET TCP] ServerSocket da san sang ket noi tai cong: " + finalSocketPort);
                    while (true) {
                        Socket clientSocket = serverSocket.accept();
                        new Thread(new SocketClientHandler(clientSocket, auctionService)).start();
                    }
                } catch (Exception e) {
                    System.err.println("[SOCKET ERROR] " + e.getMessage());
                }
            });
            socketServerThread.setDaemon(true);
            socketServerThread.start();

            System.out.println("[SERVER] Toan bo he thong da san sang!");
            System.out.println("==================================================");

            Thread.currentThread().join();
        } catch (Exception e) {
            System.err.println("[SERVER ERROR] " + e.getMessage());
            e.printStackTrace();
        }
    }
}
