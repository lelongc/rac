import java.rmi.Remote;
import java.rmi.RemoteException;

public interface GameService extends Remote {
    /**
     * Nguoi choi tham gia phong choi
     * @param playerName Ten nguoi choi
     * @return Thong bao chao mung va trang thai phong
     */
    String joinRoom(String playerName) throws RemoteException;

    /**
     * Nguoi choi thuc hien doan so
     * @param playerName Ten nguoi choi
     * @param number So du doan (1 - 100)
     * @return Ket qua doan so (Dung/Lon hon/Nho hon) kem diem
     */
    String makeGuess(String playerName, int number) throws RemoteException;

    /**
     * Lay bang xep hang diem so cua tat ca nguoi choi
     * @return Chuoi thong tin bang xep hang
     */
    String getLeaderboard() throws RemoteException;

    /**
     * Lay diem so hien tai cua nguoi choi
     * @param playerName Ten nguoi choi
     * @return So diem
     */
    int getScore(String playerName) throws RemoteException;

    /**
     * Nguoi choi roi khoi phong
     * @param playerName Ten nguoi choi
     */
    void leaveRoom(String playerName) throws RemoteException;
}
