import java.io.IOException;
import java.net.*;
import java.util.Scanner;

public class UDPClient {
    private static final String SERVER_HOST = "localhost";
    private static final int SERVER_PORT = 8888;
    private static final int BUFFER_SIZE = 1024;

    public static void main(String[] args) {
        System.out.println("=== UDP CLIENT DOAN SO ===");

        try (
            DatagramSocket socket = new DatagramSocket();
            Scanner scanner = new Scanner(System.in)
        ) {
            InetAddress serverAddress = InetAddress.getByName(SERVER_HOST);

            sendPacket(socket, "NEW", serverAddress, SERVER_PORT);
            String welcomeMsg = receivePacket(socket);
            System.out.println("Server: " + welcomeMsg);

            while (true) {
                System.out.print("Nhap so doan cua ban: ");
                String userGuess = scanner.nextLine().trim();

                if (userGuess.equalsIgnoreCase("exit") || userGuess.equalsIgnoreCase("quit")) {
                    System.out.println("Ban da thoat tro choi.");
                    break;
                }

                sendPacket(socket, userGuess, serverAddress, SERVER_PORT);
                String response = receivePacket(socket);

                if (response.startsWith("WIN:")) {
                    System.out.println("\n[THANG CUOC] " + response.substring(4));
                    System.out.println("Tro choi ket thuc. Cam on ban da choi!");
                    break;
                } else {
                    System.out.println("Server: " + response);
                }
            }
        } catch (IOException e) {
            System.err.println("Loi Client UDP: " + e.getMessage());
        }
    }

    private static void sendPacket(DatagramSocket socket, String message, InetAddress address, int port) throws IOException {
        byte[] sendData = message.getBytes();
        DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, address, port);
        socket.send(sendPacket);
    }

    private static String receivePacket(DatagramSocket socket) throws IOException {
        byte[] receiveData = new byte[BUFFER_SIZE];
        DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
        socket.receive(receivePacket);
        return new String(receivePacket.getData(), 0, receivePacket.getLength()).trim();
    }
}
