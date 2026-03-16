package bai4;


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
            Socket socket = this.clientSocket;
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true)
        ) {
            String line = in.readLine();
            if (line == null) return;

            try {
                int n = Integer.parseInt(line.trim());
                if (n < 0) {
                    out.println("khong tinh giai thua so am.");
                } else if (n > 20) {
                    out.println("n qua lon (toi da 20) de tranh tran so long.");
                } else {
                    long result = factorial(n);
                    out.println("giai thua cua " + n + " = " + result);
                }
            } catch (NumberFormatException e) {
                out.println("loi, gia tri khong hop le.");
            }

        } catch (IOException e) {
            System.out.println("loi handler: " + e.getMessage());
        }
    }

    private static long factorial(int n) {
        long result = 1L;
        for (int i = 2; i <= n; i++) result *= i;
        return result;
    }
}