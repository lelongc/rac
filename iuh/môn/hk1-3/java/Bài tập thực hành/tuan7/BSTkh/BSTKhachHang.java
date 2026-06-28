package BSTkh;
import java.util.ArrayList;
import java.util.List;

public class BSTKhachHang {
	private NutCay root;

	public BSTKhachHang() {
		super();
		this.root = null;
	}
	public void addkh(KhachHang m ) {
		root = addkhr(root,m);
	}
	private NutCay addkhr(NutCay cur , KhachHang m) {
		if ( cur == null)return new NutCay(m);
		if(m.getId() < cur.kh.getId()) {
			cur.trai =  addkhr(cur.trai,m);
		}
		else if (m.getId() > cur.kh.getId()) {
			cur.phai =  addkhr(cur.phai,m);
		}
		return cur;
	}
	public List<KhachHang> laykh(){
		List<KhachHang> danhsach = new ArrayList<KhachHang>();
		LNR(root,danhsach);
		return danhsach;
		
	}
	private void LNR(NutCay cur , List<KhachHang> danhs) {
		if( cur != null) {
			LNR(cur.trai,danhs);
			danhs.add(cur.kh);
			LNR(cur.phai,danhs);
		}
	}
	
}
