package File_Folder;

import java.io.*;
import java.util.ArrayList;

class MonHoc {
    private String tenMonHoc;
    private int tinChi;
    private double diem;

    public MonHoc(String tenMonHoc, int tinChi, double diem) {
        this.tenMonHoc = tenMonHoc;
        this.tinChi = tinChi;
        this.diem = diem;
    }
    public String getTenMonHoc() { return tenMonHoc; }
    public int getTinChi() { return tinChi; }
    public double getDiem() { return diem; }
    
    @Override
    public String toString() { return tenMonHoc + " (" + tinChi + "TC) - Diem: " + diem; }
}

class SinhVien {
    private String mssv;
    private String ten;
    private int tuoi;
    private ArrayList<MonHoc> listMH;

    public SinhVien(String mssv, String ten, int tuoi, ArrayList<MonHoc> listMH) {
        this.mssv = mssv;
        this.ten = ten;
        this.tuoi = tuoi;
        this.listMH = listMH;
    }
    public String getMssv() { return mssv; }
    public String getTen() { return ten; }
    public int getTuoi() { return tuoi; }
    public ArrayList<MonHoc> getListMH() { return listMH; }

    @Override
    public String toString() {
        return "SV: " + mssv + " - " + ten + " - Tuoi: " + tuoi + "\nMon hoc: " + listMH;
    }
}

public class NhiPhanSinhVien {
    // Luu danh sach sinh vien xuong file nhi phan
    public static void saveSV(String src, ArrayList<SinhVien> listSV) {
        try (DataOutputStream dos = new DataOutputStream(new FileOutputStream(new File(src)))) {
            dos.writeInt(listSV.size()); // Ghi so luong SV
            
            for (SinhVien sv : listSV) {
                dos.writeUTF(sv.getMssv());
                dos.writeUTF(sv.getTen());
                dos.writeInt(sv.getTuoi());
                dos.writeInt(sv.getListMH().size()); // Ghi so luong MonHoc cua SV nay
                
                for (MonHoc mh : sv.getListMH()) {
                    dos.writeUTF(mh.getTenMonHoc());
                    dos.writeInt(mh.getTinChi());
                    dos.writeDouble(mh.getDiem());
                }
            }
            dos.flush();
            System.out.println("Da ghi danh sach SV xuong file nhi phan: " + src);
        } catch (IOException e) {
            System.err.println("Loi ghi file nhi phan: " + e.getMessage());
        }
    }

    // Doc danh sach sinh vien tu file nhi phan
    public static void loadSV(String src) {
        try (DataInputStream dis = new DataInputStream(new FileInputStream(new File(src)))) {
            int size = dis.readInt();
            ArrayList<SinhVien> listSV = new ArrayList<>();
            
            for (int i = 0; i < size; i++) {
                String mssv = dis.readUTF();
                String name = dis.readUTF();
                int age = dis.readInt();
                int sizemh = dis.readInt();
                
                ArrayList<MonHoc> listMH = new ArrayList<>();
                for (int j = 0; j < sizemh; j++) {
                    String tenMonHoc = dis.readUTF();
                    int tinChi = dis.readInt();
                    double diem = dis.readDouble();
                    listMH.add(new MonHoc(tenMonHoc, tinChi, diem));
                }
                listSV.add(new SinhVien(mssv, name, age, listMH));
            }
            
            System.out.println("=== DANH SACH SINH VIEN ĐỌC TỪ FILE ===");
            for (SinhVien sv : listSV) {
                System.out.println(sv.toString());
            }
        } catch (IOException e) {
            System.err.println("Loi doc file nhi phan: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        // Thu nghiem
        ArrayList<MonHoc> listMH = new ArrayList<>();
        listMH.add(new MonHoc("ltcb", 3, 6.7));
        listMH.add(new MonHoc("ltw", 3, 8.0));

        ArrayList<SinhVien> listSV = new ArrayList<>();
        listSV.add(new SinhVien("11329078", "Nguyen Van A", 23, listMH));
        listSV.add(new SinhVien("11329079", "Nguyen Van B", 21, new ArrayList<>()));

        String filePath = "danhsachSV.bin";
        saveSV(filePath, listSV);
        loadSV(filePath);
    }
}
