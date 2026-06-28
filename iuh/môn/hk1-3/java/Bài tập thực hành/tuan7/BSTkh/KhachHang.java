package BSTkh;
import java.util.Comparator;
public class KhachHang {
	private int id;
	private String ten;
	private int tuoi;
	private String gend;
	
	public KhachHang(int id, String ten, int tuoi, String gend) {
		super();
		this.id = id;
		this.ten = ten;
		this.tuoi = tuoi;
		this.gend = gend;
	}

	

	public int getId() {
		return id;
	}

	public String getTen() {
		return ten;
	}

	public int getTuoi() {
		return tuoi;
	}

	public String getGend() {
		return gend;
	}
	@Override
	public String toString() {
		return "KhachHang [id=" + id + ", ten=" + ten + ", tuoi=" + tuoi + ", gend=" + gend + "]";
	}
	
}
