import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;
import java.nio.charset.StandardCharsets;

public class SocketClientHandler implements Runnable {
    private final Socket socket;
    private final AuctionServiceImpl auctionService;

    public SocketClientHandler(Socket socket, AuctionServiceImpl auctionService) {
        this.socket = socket;
        this.auctionService = auctionService;
    }

    @Override
    public void run() {
        PrintWriter out = null;
        try {
            out = new PrintWriter(socket.getOutputStream(), true, StandardCharsets.UTF_8);
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream(), StandardCharsets.UTF_8));
            auctionService.addSocketClient(out);

            out.println("[KET NOI THANH CONG] Da ket noi toi kenh truyen thong Socket TCP cua phien dau gia!");
            for (AuctionItem item : auctionService.getItems()) {
                out.println("  " + item.toString());
            }

            String line;
            while ((line = in.readLine()) != null) {
                line = line.trim();
                if (line.equalsIgnoreCase("exit") || line.equalsIgnoreCase("quit")) {
                    break;
                }
                if (line.startsWith("BID ")) {
                    String[] parts = line.split("\\s+");
                    if (parts.length >= 4) {
                        String itemId = parts[1];
                        try {
                            double amount = Double.parseDouble(parts[2]);
                            String user = parts[3];
                            boolean ok = auctionService.placeBid(itemId, user, amount);
                            if (ok) {
                                out.println("[BID SUCCESS] Dat gia thanh cong!");
                            } else {
                                out.println("[BID REJECTED] Dat gia that bai. Kiem tra ma SP hoac gia phai cao hon gia hien tai!");
                            }
                        } catch (NumberFormatException e) {
                            out.println("[ERROR] Gia tien khong hop le.");
                        }
                    } else {
                        out.println("[FORMAT] Cu phap: BID <MaSP> <GiaTien> <NguoiDat>");
                    }
                } else if (line.equalsIgnoreCase("LIST")) {
                    for (AuctionItem item : auctionService.getItems()) {
                        out.println("  " + item.toString());
                    }
                }
            }
        } catch (Exception e) {
        } finally {
            if (out != null) {
                auctionService.removeSocketClient(out);
            }
            try {
                socket.close();
            } catch (Exception ignored) {}
        }
    }
}
