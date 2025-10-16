package BSTkh;
import java.util.ArrayList;
import java.util.List;

public class BSTKhachHang {
    private KhachHang root;

    public BSTKhachHang() {
        super();
        this.root = null;
    }

    public void addkh(KhachHang m) {
        root = addkhr(root, m);
    }

    private KhachHang addkhr(KhachHang cur, KhachHang m) {
        if (cur == null) return m;
        if (m.getId() < cur.getId()) {
            cur.setTrai(addkhr(cur.getTrai(), m));
        } else if (m.getId() > cur.getId()) {
            cur.setPhai(addkhr(cur.getPhai(), m));
        }
        return cur;
    }

    public List<KhachHang> laykh() {
        List<KhachHang> danhsach = new ArrayList<>();
        LNR(root, danhsach);
        return danhsach;
    }

    private void LNR(KhachHang cur, List<KhachHang> danhs) {
        if (cur != null) {
            LNR(cur.getTrai(), danhs);
            danhs.add(cur);
            LNR(cur.getPhai(), danhs);
        }
    }
}
