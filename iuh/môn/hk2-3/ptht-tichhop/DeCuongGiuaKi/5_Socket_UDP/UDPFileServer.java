package Socket_UDP;

import java.io.*;
import java.net.*;

public class UDPFileServer {
    public static final int PORT = 9998;

    public static void main(String[] args) {
        try (DatagramSocket socket = new DatagramSocket(PORT)) {
            System.out.println("UDP File Server dang lang nghe tren port " + PORT + "...");
            byte[] receiveData = new byte[65000]; // Max size cho UDP an toan la ~65KB

            // Buoc 1: Nhan metadata (Ten file)
            DatagramPacket metaPacket = new DatagramPacket(receiveData, receiveData.length);
            socket.receive(metaPacket);
            String metadata = new String(metaPacket.getData(), 0, metaPacket.getLength());
            String[] parts = metadata.split("::");
            String fileName = parts[0];
            String savePath = parts[1];
            
            System.out.println("Dang chuan bi nhan file: " + fileName + " luu vao " + savePath);
            File dir = new File(savePath);
            if (!dir.exists()) dir.mkdirs();
            File destFile = new File(dir, fileName);

            // Buoc 2: Nhan du lieu file nhi phan
            DatagramPacket filePacket = new DatagramPacket(receiveData, receiveData.length);
            socket.receive(filePacket);
            
            try (FileOutputStream fos = new FileOutputStream(destFile)) {
                fos.write(filePacket.getData(), 0, filePacket.getLength());
                System.out.println("Da nhan va luu file thanh cong vao " + destFile.getAbsolutePath());
            }

            // Buoc 3: Confirm cho Client
            String confirm = "OK da luu!";
            DatagramPacket confirmPacket = new DatagramPacket(confirm.getBytes(), confirm.length(), metaPacket.getAddress(), metaPacket.getPort());
            socket.send(confirmPacket);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
