package tuan2b;


public class XeMay extends PhuongTien {
    double dungTichXiLanh;

    public XeMay(String hangSanXuat, int namSanXuat, double giaBan, double dungTichXiLanh) {
        super(hangSanXuat, namSanXuat, giaBan); 
        this.dungTichXiLanh = dungTichXiLanh;
    }

    public double tinhThue() {
        
        return giaBan * 0.05;
    }
}
