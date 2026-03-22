package File_Folder;

import java.awt.image.BufferedImage;
import java.io.*;
import javax.imageio.ImageIO;

public class XuLyAnh {

    // Doc File anh chuyen thanh mang Byte[]
    public static byte[] readFileToByteArray(File path) {
        try (FileInputStream fis = new FileInputStream(path);
             ByteArrayOutputStream bos = new ByteArrayOutputStream()) {
            byte[] buffer = new byte[1024];
            int readNum;
            while ((readNum = fis.read(buffer)) != -1) {
                bos.write(buffer, 0, readNum);
            }
            System.out.println("Doc file thanh cong, kich thuoc: " + bos.size() + " bytes");
            return bos.toByteArray();
        } catch (IOException ex) {
            System.out.println("Loi doc file anh: " + ex.getMessage());
            return null;
        }
    }

    // Ghi mang Byte[] thanh File Anh
    public static void saveByteArrayToFile(String tformat, String destFile, byte[] bfile) {
        try {
            BufferedImage img = ImageIO.read(new ByteArrayInputStream(bfile));
            if (img != null) {
                ImageIO.write(img, tformat, new File(destFile));
                System.out.println("Ghi anh thanh cong: " + destFile);
            } else {
                 System.out.println("Khong the parse byte[] sang BufferedImage.");
            }
        } catch (IOException ex) {
             System.out.println("Loi ghi file anh: " + ex.getMessage());
        }
    }

    public static void main(String[] args) {
        /*
        File inputImg = new File("D:\\HocJava\\hinh.png");
        byte[] bytes = readFileToByteArray(inputImg);
        if (bytes != null) {
            saveByteArrayToFile("png", "D:\\HocJava\\hinh_copy.png", bytes);
        }
        */
        System.out.println("XuLyAnh template san sang hoat dong.");
    }
}
