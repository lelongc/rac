package File_Folder;

import java.io.*;

public class ThaoTacFile {

    // 1. Xoa File rỗng hoac File don le
    public void deleteFile(String source) {
        File file = new File(source);
        if (file.exists()) {
            file.delete();
            System.out.println("Xoa file thanh cong: " + source);
        } else {
            System.out.println("File khong ton tai");
        }
    }

    // 2. Xoa thumuc rỗng
    public boolean deleteEmptyFolder(String source) {
        File folder = new File(source);
        if (folder.exists()) {
            folder.delete();
            System.out.println("Xoa folder rong thanh cong");
            return true;
        }
        return false;
    }

    // 3. Xoa Đệ Quy Toàn Bộ Folder gồ cả file con bên trong
    public boolean deleteListFileInfolder(String source) {
        File folder = new File(source);
        if (folder.exists()) {
            File[] listFile = folder.listFiles();
            if (listFile != null) {
                for (File f : listFile) {
                    if (f.isFile()) {
                        f.delete();
                    } else if (f.isDirectory()) {
                        deleteListFileInfolder(f.getAbsolutePath());
                    }
                }
            }
            folder.delete();
            System.out.println("Delete folder đệ quy thành công! " + source);
            return true;
        } else {
            System.out.println("folder không tồn tại");
            return false;
        }
    }

    // 4. Tìm kiếm File (Tìm tất cả các file có đuôi / chữ chỉ định)
    public void finFile(String source, String key) {
        File file = new File(source);
        if (file.exists()) {
            if (file.isFile()) {
                if (file.getName().endsWith(key)) {
                    System.out.println("Tim thay: " + file.getAbsolutePath());
                }
            } else {
                File[] listFile = file.listFiles();
                if (listFile != null) {
                    for (File f : listFile) {
                        finFile(f.getAbsolutePath(), key);
                    }
                }
            }
        }
    }

    // 5. Copy File bằng FileInputStream / FileOutputStream
    public boolean copyFile(String source, String dest) {
        File sourceFile = new File(source);
        File destFile = new File(dest);
        if (sourceFile.exists()) {
            try (FileInputStream fis = new FileInputStream(sourceFile);
                 FileOutputStream fos = new FileOutputStream(destFile)) {
                
                byte[] arr = new byte[1024];
                int readNum;
                while ((readNum = fis.read(arr)) != -1) {
                    fos.write(arr, 0, readNum); // Cực kì lưu ý phải có readNum để ko bị lỗi byte rác
                }
                fos.flush();
                System.out.println("Copy thành công từ " + source + " sang " + dest);
                return true;
            } catch (IOException e) {
                System.out.println("Loi IO khi copy: " + e.getMessage());
            }
        } else {
            System.out.println("File nguồn không tồn tại");
        }
        return false;
    }

    public static void main(String[] args) {
        ThaoTacFile ttf = new ThaoTacFile();
        System.out.println("=== TEST CAC HAM THAO TAC FILE ===");
        // Uncomment cac dong duoi de chay thu
        // ttf.finFile("C:\\", ".txt"); 
        // ttf.copyFile("a.txt", "b.txt");
    }
}
