package Socket_UDP;

import java.io.*;
import java.net.*;
import java.util.Scanner;

public class UDPFileClient {
    public static final String HOST = "localhost";
    public static final int PORT = 9998;

    public static void main(String[] args) {
        try (DatagramSocket socket = new DatagramSocket();
             Scanner scanner = new Scanner(System.in)) {
            InetAddress ip = InetAddress.getByName(HOST);

            System.out.print("Nhap duong dan file can gui tren Client (vd: D:\\test.txt): ");
            String filePath = scanner.nextLine();
            File file = new File(filePath);

            if (!file.exists()) {
                System.out.println("File khong ton tai!");
                return;
            }

            System.out.print("Nhap duong dan folder tren Server de luu (vd: D:\\luu): ");
            String savePath = scanner.nextLine();

            // Buoc 1: Gui Metadata (Ten file :: Thu muc luu)
            String metaInfo = file.getName() + "::" + savePath;
            byte[] metaBytes = metaInfo.getBytes();
            DatagramPacket metaPacket = new DatagramPacket(metaBytes, metaBytes.length, ip, PORT);
            socket.send(metaPacket);

            // Buoc 2: Doc file va Gui mảng byte
            try (FileInputStream fis = new FileInputStream(file);
                 ByteArrayOutputStream bos = new ByteArrayOutputStream()) {
                byte[] buffer = new byte[1024];
                int n;
                while ((n = fis.read(buffer)) != -1) {
                    bos.write(buffer, 0, n);
                }
                byte[] fileBytes = bos.toByteArray();
                if (fileBytes.length > 60000) {
                    System.out.println("File qua lon cho 1 goi UDP don gian. Day la code demo giua ki!");
                }
                DatagramPacket fileDataPacket = new DatagramPacket(fileBytes, fileBytes.length, ip, PORT);
                socket.send(fileDataPacket);
            }

            // Buoc 3: Nhan xac nhan
            byte[] receiveData = new byte[1024];
            DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
            socket.receive(receivePacket);
            String response = new String(receivePacket.getData(), 0, receivePacket.getLength());
            System.out.println("Server > " + response);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
