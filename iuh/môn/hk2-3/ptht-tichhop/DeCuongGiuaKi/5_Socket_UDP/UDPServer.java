package Socket_UDP;

import java.io.*;
import java.net.*;

public class UDPServer {
    public static final int PORT = 9999;

    public static void main(String[] args) {
        try (DatagramSocket socket = new DatagramSocket(PORT)) {
            System.out.println("UDP Server dang lang nghe tren port " + PORT + "...");
            byte[] receiveData = new byte[1024];

            while (true) {
                // Nhan request
                DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
                socket.receive(receivePacket);
                
                String input = new String(receivePacket.getData(), 0, receivePacket.getLength()).trim();
                InetAddress clientIp = receivePacket.getAddress();
                int clientPort = receivePacket.getPort();
                System.out.println("Nhan tu Client [" + clientIp + ":" + clientPort + "]: " + input);

                String result = "";

                // =================================== LOGIC ===================================
                // 1. DẠNG TUẦN 5-b5: MENU DATE/TIME (1. Time, 2. Date, 3. DateTime)
                /*
                try {
                    int choice = Integer.parseInt(input);
                    java.time.LocalDateTime now = java.time.LocalDateTime.now();
                    java.time.format.DateTimeFormatter timeFmt = java.time.format.DateTimeFormatter.ofPattern("HH:mm:ss");
                    java.time.format.DateTimeFormatter dateFmt = java.time.format.DateTimeFormatter.ofPattern("dd/MM/yyyy");
                    if (choice == 1) result = now.format(timeFmt);
                    else if (choice == 2) result = now.format(dateFmt);
                    else if (choice == 3) result = now.format(dateFmt) + " " + now.format(timeFmt);
                    else result = "Lua chon khong hop le!";
                } catch (NumberFormatException e) {
                    result = "Vui long nhap so (1-3)!";
                }
                */

                // 2. DẠNG TUẦN 5-b6: TÍNH TỔNG CHUỖI SỐ ĐẶC BIỆT
                /*
                try {
                    String[] parts = input.split("\\s+");
                    int menu = Integer.parseInt(parts[0]);
                    int n = Integer.parseInt(parts[1]);
                    long sum = 0;
                    if (menu == 1) { for (int i = 0; i <= n; i++) sum += (2*i + 1); result = "Tong 1 = " + sum; }
                    else if (menu == 2) { for (int i = 1; i <= n; i++) sum += (i * (i+1)); result = "Tong 2 = " + sum; }
                    else if (menu == 3) { 
                        int sign = 1; for (int i = 1; i <= 2*n+1; i++) { sum += sign * i; sign = -sign; }
                        result = "Tong 3 = " + sum;
                    }
                } catch (Exception e) { result = "Sai cu phap. Vd: '1 5'"; }
                */

                // MAC DINH: DAO NGUOC CHUOI
                result = new StringBuilder(input).reverse().toString();

                byte[] sendData = result.getBytes();
                DatagramPacket sendPacket = new DatagramPacket(sendData, sendData.length, clientIp, clientPort);
                socket.send(sendPacket);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
