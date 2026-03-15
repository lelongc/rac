package tuan2;

public class Main {
    public static void main(String[] args) {
       
        NhanVienVanPhong nv1 = new NhanVienVanPhong();
        System.out.println("nhap nhan vien van phong");
        nv1.nhapThongTinVP();
        
      
        NhanVienSanXuat nv2 = new NhanVienSanXuat();
        System.out.println("\nnhap nhan vien san xuat");
        nv2.nhapThongTinSX();

       
        System.out.println("\ndanh sach nhan vien");
        
        nv1.hienThiThongTin(); 
        System.out.println(" | luong: " + nv1.tinhLuong());

        nv2.hienThiThongTin(); 
        System.out.println(" | luong: " + nv2.tinhLuong());
    }
}