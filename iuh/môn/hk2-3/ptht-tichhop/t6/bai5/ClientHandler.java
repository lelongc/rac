package bai5;

import java.io.*;
import java.net.Socket;

public class ClientHandler extends Thread {
    private final Socket clientSocket;

    public ClientHandler(Socket clientSocket) {
        this.clientSocket = clientSocket;
    }

    @Override
    public void run() {
        try (
            BufferedReader in = new BufferedReader(
                    new InputStreamReader(clientSocket.getInputStream(), "UTF-8"));
            PrintWriter out = new PrintWriter(
                    new OutputStreamWriter(clientSocket.getOutputStream(), "UTF-8"), true)
        ) {
            String received = in.readLine();
            if (received != null) {
                String upperCase = received.toUpperCase();
                int charCount = received.length();
                out.println("chuoi viet hoa: " + upperCase);
                out.println("so ky tu: " + charCount);
            }
        } catch (IOException e) {
            System.out.println("loi xu ly client: " + e.getMessage());
        } finally {
            try {
                clientSocket.close();
            } catch (IOException ignored) {}
        }
    }
}