import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.*;
import java.util.concurrent.ConcurrentHashMap;

public class GameServiceImpl extends UnicastRemoteObject implements GameService {
    // Luu danh sach nguoi choi va diem so: Ten -> Diem
    private final Map<String, Integer> playerScores = new ConcurrentHashMap<>();
    
    // So bi mat hien tai can doan (1 - 100)
    private int secretNumber;
    private int currentRound = 1;
    private final Random random = new Random();

    public GameServiceImpl() throws RemoteException {
        super();
        generateNewSecretNumber();
        System.out.println("[SERVER] Tro choi da san sang! Vong " + currentRound + " - So bi mat: " + secretNumber);
    }

    private void generateNewSecretNumber() {
        this.secretNumber = random.nextInt(100) + 1; // 1 -> 100
    }

    @Override
    public synchronized String joinRoom(String playerName) throws RemoteException {
        if (playerName == null || playerName.trim().isEmpty()) {
            return "Ten nguoi choi khong hop le!";
        }
        playerName = playerName.trim();
        if (!playerScores.containsKey(playerName)) {
            playerScores.put(playerName, 0);
            System.out.println("[SERVER] Nguoi choi moi gia nhap: " + playerName);
        } else {
            System.out.println("[SERVER] Nguoi choi quay lai phong: " + playerName);
        }
        return "=== CHAO MUNG " + playerName.toUpperCase() + " THAM GIA PHONG CHOI DOAN SO (RMI) ===\n" +
               "+ So bi mat nam trong khoang [1 - 100].\n" +
               "+ Vong choi hien tai: Vong " + currentRound + "\n" +
               "+ Diem hien tai cua ban: " + playerScores.get(playerName) + " diem.\n" +
               "+ Hay nhap so du doan hoac lenh: 'bxh' (xem diem), 'thoat' (roi phong).";
    }

    @Override
    public synchronized String makeGuess(String playerName, int number) throws RemoteException {
        if (!playerScores.containsKey(playerName)) {
            return "Loi: Ban chua tham gia phong choi!";
        }

        System.out.println("[SERVER] [" + playerName + "] doan so: " + number + " (So bi mat: " + secretNumber + ")");

        if (number < 1 || number > 100) {
            return "[NHAC NHO] So du doan phai nam trong khoang tu 1 den 100!";
        }

        if (number == secretNumber) {
            int oldScore = playerScores.get(playerName);
            int newScore = oldScore + 10;
            playerScores.put(playerName, newScore);

            int finishedRound = currentRound;
            int correctNumber = secretNumber;

            // Tao vong moi
            currentRound++;
            generateNewSecretNumber();

            System.out.println("[SERVER] CHUC MUNG: " + playerName + " da doan dung so " + correctNumber + " o Vong " + finishedRound + "!");
            System.out.println("[SERVER] Bat dau Vong " + currentRound + " - So bi mat moi: " + secretNumber);

            return ">>> CHINH XAC! BAN DA DOAN DUNG SO " + correctNumber + " o VONG " + finishedRound + "! <<<\n" +
                   "+ Ban duoc cong +10 diem! Tong diem hien tai: " + newScore + " diem.\n" +
                   "+ He thong da tu dong tao SO BI MAT MOI cho Vong " + currentRound + ". Tiep tuc doan nao!";
        } else if (number < secretNumber) {
            return "[GOI Y] So bi mat LON HON (>) so " + number + " cua ban!";
        } else {
            return "[GOI Y] So bi mat NHO HON (<) so " + number + " cua ban!";
        }
    }

    @Override
    public synchronized String getLeaderboard() throws RemoteException {
        if (playerScores.isEmpty()) {
            return "Chua co nguoi choi nao trong phong.";
        }

        StringBuilder sb = new StringBuilder();
        sb.append("=========================================\n");
        sb.append("      BANG XEP HANG DIEM SO (RMI)        \n");
        sb.append("=========================================\n");
        sb.append(String.format("%-5s | %-20s | %-8s\n", "Top", "Ten nguoi choi", "Diem"));
        sb.append("-----------------------------------------\n");

        // Sap xep danh sach theo diem giam dan
        List<Map.Entry<String, Integer>> list = new ArrayList<>(playerScores.entrySet());
        list.sort((a, b) -> b.getValue().compareTo(a.getValue()));

        int rank = 1;
        for (Map.Entry<String, Integer> entry : list) {
            sb.append(String.format("%-5d | %-20s | %-8d\n", rank++, entry.getKey(), entry.getValue()));
        }
        sb.append("=========================================");
        return sb.toString();
    }

    @Override
    public int getScore(String playerName) throws RemoteException {
        return playerScores.getOrDefault(playerName, 0);
    }

    @Override
    public synchronized void leaveRoom(String playerName) throws RemoteException {
        if (playerName != null && playerScores.containsKey(playerName)) {
            System.out.println("[SERVER] Nguoi choi [" + playerName + "] da roi phong.");
        }
    }
}
