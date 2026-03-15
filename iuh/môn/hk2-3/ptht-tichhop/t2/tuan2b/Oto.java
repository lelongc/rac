/**
 * 
 */
package tuan2b;

public class Oto extends PhuongTien {
    int soChoNgoi;

    public Oto(String hangSanXuat, int namSanXuat, double giaBan, int soChoNgoi) {
        super(hangSanXuat, namSanXuat, giaBan);
        this.soChoNgoi = soChoNgoi;
    }

    public double tinhThue() {
        return giaBan * 0.1;
    }
}