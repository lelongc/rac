public class StudentBST {
    private Student root;
    
    public StudentBST() {
        this.root = null;
    }
    
    // Them sinh vien vao cay BST
    public void themSV(int id, String ten, double diem) {
        Student svMoi = new Student(id, ten, diem);
        root = themNode(root, svMoi);
        System.out.println("✓ Da them thanh cong!");
    }
    
    private Student themNode(Student node, Student svMoi) {
        if (node == null) {
            return svMoi;
        }
        
        if (svMoi.Student_ID < node.Student_ID) {
            node.Left = themNode(node.Left, svMoi);
        } else if (svMoi.Student_ID > node.Student_ID) {
            node.Right = themNode(node.Right, svMoi);
        } else {
            System.out.println("✗ Loi: ID da ton tai!");
        }
        
        return node;
    }
    
    // Xoa sinh vien
    public void xoaSV(int id) {
        if (timKiem(root, id) == null) {
            System.out.println("✗ Khong tim thay sinh vien co ID: " + id);
            return;
        }
        root = xoaNode(root, id);
        System.out.println("✓ Da xoa sinh vien co ID: " + id);
    }
    
    private Student xoaNode(Student node, int id) {
        if (node == null) {
            return null;
        }
        
        if (id < node.Student_ID) {
            node.Left = xoaNode(node.Left, id);
        } else if (id > node.Student_ID) {
            node.Right = xoaNode(node.Right, id);
        } else {
            if (node.Left == null) return node.Right;
            if (node.Right == null) return node.Left;
            
            Student nodeMin = timMin(node.Right);
            node.Student_ID = nodeMin.Student_ID;
            node.Student_name = nodeMin.Student_name;
            node.Student_Result = nodeMin.Student_Result;
            node.Right = xoaNode(node.Right, nodeMin.Student_ID);
        }
        
        return node;
    }
    
    private Student timMin(Student node) {
        while (node.Left != null) {
            node = node.Left;
        }
        return node;
    }
    
    private Student timKiem(Student node, int id) {
        if (node == null || node.Student_ID == id) {
            return node;
        }
        
        if (id < node.Student_ID) {
            return timKiem(node.Left, id);
        }
        
        return timKiem(node.Right, id);
    }
    
    // Xuat thong tin tong hop
    public void xuatThongTin() {
        if (root == null) {
            System.out.println("Danh sach rong!");
            return;
        }
        
        ThongKe tk = new ThongKe();
        tinhThongKe(root, tk);
        
        System.out.println("\n╔════════════════════════════════════════════════════╗");
        System.out.println("║          THONG TIN TONG HOP                       ║");
        System.out.println("╠════════════════════════════════════════════════════╣");
        System.out.println(String.format("║ Tong so sinh vien: %-28d║", tk.soSV));
        System.out.println(String.format("║ Diem trung binh: %-30.2f║", tk.tongDiem / tk.soSV));
        System.out.println("╠════════════════════════════════════════════════════╣");
        System.out.println("║ Sinh vien diem cao nhat:                          ║");
        System.out.println(String.format("║   %-48s║", tk.svMax.toString()));
        System.out.println("╠════════════════════════════════════════════════════╣");
        System.out.println("║ Sinh vien diem thap nhat:                         ║");
        System.out.println(String.format("║   %-48s║", tk.svMin.toString()));
        System.out.println("╚════════════════════════════════════════════════════╝");
    }
    
    private void tinhThongKe(Student node, ThongKe tk) {
        if (node == null) return;
        
        tk.soSV++;
        tk.tongDiem += node.Student_Result;
        
        if (tk.svMax == null || node.Student_Result > tk.svMax.Student_Result) {
            tk.svMax = node;
        }
        if (tk.svMin == null || node.Student_Result < tk.svMin.Student_Result) {
            tk.svMin = node;
        }
        
        tinhThongKe(node.Left, tk);
        tinhThongKe(node.Right, tk);
    }
    
    // Thong ke phan loai
    public void thongKeDiem() {
        if (root == null) {
            System.out.println("Danh sach rong!");
            return;
        }
        
        PhanLoai pl = new PhanLoai();
        demPhanLoai(root, pl);
        
        System.out.println("\n╔════════════════════════════════════════════════════╗");
        System.out.println("║          THONG KE PHAN LOAI DIEM                  ║");
        System.out.println("╠════════════════════════════════════════════════════╣");
        System.out.println(String.format("║ Gioi (8.0 - 10.0):  %-30d║", pl.gioi));
        System.out.println(String.format("║ Kha (6.5 - 7.9):    %-30d║", pl.kha));
        System.out.println(String.format("║ Trung binh (5.0 - 6.4): %-25d║", pl.trungBinh));
        System.out.println(String.format("║ Yeu (< 5.0):        %-30d║", pl.yeu));
        System.out.println("╚════════════════════════════════════════════════════╝");
    }
    
    private void demPhanLoai(Student node, PhanLoai pl) {
        if (node == null) return;
        
        double diem = node.Student_Result;
        if (diem >= 8.0) pl.gioi++;
        else if (diem >= 6.5) pl.kha++;
        else if (diem >= 5.0) pl.trungBinh++;
        else pl.yeu++;
        
        demPhanLoai(node.Left, pl);
        demPhanLoai(node.Right, pl);
    }
    
    // Hien thi danh sach
    public void hienThi() {
        System.out.println("\n--- DANH SACH SINH VIEN (theo ID) ---");
        if (root == null) {
            System.out.println("Danh sach trong.");
        } else {
            inOrder(root);
        }
        System.out.println("-------------------------------------");
    }
    
    private void inOrder(Student node) {
        if (node != null) {
            inOrder(node.Left);
            System.out.println(node);
            inOrder(node.Right);
        }
    }
    
    public boolean isEmpty() {
        return root == null;
    }
    
    private class ThongKe {
        int soSV = 0;
        double tongDiem = 0;
        Student svMax = null;
        Student svMin = null;
    }
    
    private class PhanLoai {
        int gioi = 0;
        int kha = 0;
        int trungBinh = 0;
        int yeu = 0;
    }
}
