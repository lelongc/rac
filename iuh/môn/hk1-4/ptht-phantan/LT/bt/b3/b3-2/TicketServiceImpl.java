import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.Socket;
import java.nio.charset.StandardCharsets;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.text.SimpleDateFormat;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;

public class TicketServiceImpl extends UnicastRemoteObject implements TicketService {
    private final Map<String, Trip> trips = new ConcurrentHashMap<>();

    public TicketServiceImpl() throws RemoteException {
        super();
        initDefaultTrips();
    }

    private void initDefaultTrips() {
        trips.put("CX01", new Trip("CX01", "TP.HCM -> Da Lat", "20:00 20/08", 30, 250000));
        trips.put("CX02", new Trip("CX02", "TP.HCM -> Nha Trang", "21:30 20/08", 28, 280000));
        trips.put("CX03", new Trip("CX03", "TP.HCM -> Vung Tau", "07:00 21/08", 16, 150000));
        trips.put("CX04", new Trip("CX04", "TP.HCM -> Can Tho", "09:00 21/08", 34, 180000));
        System.out.println("[SERVER] Da khoi tao danh sach chuyen xe mac dinh (" + trips.size() + " chuyen).");
    }

    @Override
    public String getTripList() throws RemoteException {
        StringBuilder sb = new StringBuilder();
        sb.append("========================================================================================\n");
        sb.append("                          DANH SACH CHUYEN XE VA GHE TRONG                              \n");
        sb.append("========================================================================================\n");
        for (Trip trip : trips.values()) {
            sb.append(trip.toString()).append("\n");
        }
        sb.append("========================================================================================");
        return sb.toString();
    }

    @Override
    public String checkTrip(String tripId) throws RemoteException {
        Trip trip = trips.get(tripId != null ? tripId.toUpperCase().trim() : "");
        if (trip == null) {
            return "[-] Khong tim thay chuyen xe co ma: " + tripId;
        }
        return trip.toString();
    }

    @Override
    public String bookTicket(String tripId, String customerName, String customerPhone,
                             int seatCount, String clientHost, int clientTcpPort) throws RemoteException {
        
        if (tripId == null || !trips.containsKey(tripId.toUpperCase().trim())) {
            return "[-] Dat ve that bai: Ma chuyen xe khong ton tai!";
        }

        if (customerName == null || customerName.trim().isEmpty() || customerPhone == null || customerPhone.trim().isEmpty()) {
            return "[-] Dat ve that bai: Vui long dien day du ho ten va so dien thoai!";
        }

        if (seatCount <= 0) {
            return "[-] Dat ve that bai: So luong ve phai lon hon 0!";
        }

        Trip trip = trips.get(tripId.toUpperCase().trim());

        // Dong bo hoa viec dat ghe tren chuyen xe de tranh overbooking
        boolean success = trip.bookSeats(seatCount);
        if (!success) {
            return "[-] Dat ve that bai: Chuyen xe " + trip.getTripId() + " chi con " 
                    + trip.getAvailableSeats() + " ghe trong (Ban yeu cau " + seatCount + " ve)!";
        }

        // Tinh tong tien va tao ma hoa don
        double totalAmount = seatCount * trip.getPrice();
        String invoiceId = "HD" + System.currentTimeMillis();
        String now = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss").format(new Date());

        String invoiceContent = generateInvoiceText(invoiceId, now, customerName, customerPhone, trip, seatCount, totalAmount);

        System.out.println("[SERVER] Khach hang [" + customerName + "] dat thanh cong " + seatCount 
                + " ve chuyen " + trip.getTripId() + ". Con lai: " + trip.getAvailableSeats() + " ghe.");

        // SU DUNG THREAD MO SOCKET TCP GUI HOA DON VE CLIENT
        new Thread(new Runnable() {
            @Override
            public void run() {
                sendInvoiceViaTcp(clientHost, clientTcpPort, invoiceContent, invoiceId);
            }
        }).start();

        return "[+] DAT VE THANH CONG!\n" +
               "    + Ma chuyen: " + trip.getTripId() + " (" + trip.getRoute() + ")\n" +
               "    + So luong : " + seatCount + " ve\n" +
               "    + Tong tien: " + String.format("%,.0f VND", totalAmount) + "\n" +
               "    + Server dang mo Socket TCP de gui Hoa don dien tu ve may ban...";
    }

    private String generateInvoiceText(String invoiceId, String time, String name, String phone, Trip trip, int seats, double total) {
        StringBuilder sb = new StringBuilder();
        sb.append("\n");
        sb.append("******************************************************************\n");
        sb.append("                  HOA DON DIEN TU DAT VE XE                       \n");
        sb.append("                  (Gui qua TCP Socket Stream)                     \n");
        sb.append("******************************************************************\n");
        sb.append(String.format(" Ma hoa don   : %s\n", invoiceId));
        sb.append(String.format(" Ngay lap     : %s\n", time));
        sb.append(String.format(" Khach hang   : %s\n", name));
        sb.append(String.format(" So dien thoai: %s\n", phone));
        sb.append("------------------------------------------------------------------\n");
        sb.append(String.format(" Chuyen xe    : %s - %s\n", trip.getTripId(), trip.getRoute()));
        sb.append(String.format(" Khoi hanh    : %s\n", trip.getDepartureTime()));
        sb.append(String.format(" So luong ve  : %d ve\n", seats));
        sb.append(String.format(" Don gia      : %,.0f VND/ve\n", trip.getPrice()));
        sb.append(String.format(" TONG TIEN    : %,.0f VND\n", total));
        sb.append("------------------------------------------------------------------\n");
        sb.append(" TRANG THAI   : DA XAC NHAN VA THANH TOAN HOP LE                  \n");
        sb.append(" Chuc quy khach mot chuyen di an toan va vui ve!                  \n");
        sb.append("******************************************************************\n");
        return sb.toString();
    }

    private void sendInvoiceViaTcp(String host, int port, String invoiceText, String invoiceId) {
        try {
            System.out.println("[TCP-THREAD] Dang mo ket noi Socket TCP den " + host + ":" + port + " de truyen hoa don " + invoiceId + "...");
            try (Socket socket = new Socket(host, port);
                 PrintWriter out = new PrintWriter(new OutputStreamWriter(socket.getOutputStream(), StandardCharsets.UTF_8), true)) {
                
                out.println(invoiceText);
                out.flush();
                System.out.println("[TCP-THREAD] Da truyen thanh cong hoa don " + invoiceId + " qua TCP Socket!");
            }
        } catch (Exception e) {
            System.err.println("[-] [TCP-THREAD] Loi khi gui hoa don qua TCP den " + host + ":" + port + ": " + e.getMessage());
        }
    }
}
