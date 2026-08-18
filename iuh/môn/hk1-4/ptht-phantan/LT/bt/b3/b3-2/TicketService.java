import java.rmi.Remote;
import java.rmi.RemoteException;

public interface TicketService extends Remote {
    /**
     * Lay danh sach tat ca chuyen xe va so ghe con trong
     */
    String getTripList() throws RemoteException;

    /**
     * Kiem tra chi tiet mot chuyen xe theo ma
     */
    String checkTrip(String tripId) throws RemoteException;

    /**
     * Dat ve xe truc tuyen qua RMI.
     * Khi dat thanh cong, Server se mo Socket TCP gui hoa don ve dia chi va port cua Client.
     * 
     * @param tripId Ma chuyen xe (vd: CX01)
     * @param customerName Ten khach hang
     * @param customerPhone So dien thoai
     * @param seatCount So luong ve can dat
     * @param clientHost Dia chi IP cua Client nhan hoa don TCP
     * @param clientTcpPort Cong TCP cua Client dang lang nghe hoa don
     * @return Ket qua xu ly ban dau tu RMI Server
     */
    String bookTicket(String tripId, String customerName, String customerPhone, 
                      int seatCount, String clientHost, int clientTcpPort) throws RemoteException;
}
