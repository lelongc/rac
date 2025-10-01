public class StudentBST {
    private Student root;
    
    public StudentBST() {
        this.root = null;
    }
    
    // a) Them sinh vien vao cay BST (theo Student_ID)
    public void themSV(int id, String ten, double diem) {
        Student svMoi = new Student(id, ten, diem);
        root = themNode(root, svMoi);
        System.out.println("Da them: " + svMoi);
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
            System.out.println("ID da ton tai!");
        }
        
        return node;
    }
    
    // b) Xoa sinh vien khoi cay
    public void xoaSV(int id) {
        root = xoaNode(root, id);
        System.out.println("Da xoa SV co ID: " + id);
    }
    
    private Student xoaNode(Student node, int id) {
        if (node == null) {
            System.out.println("Khong tim thay ID!");
            return null;
        }
        
        if (id < node.Student_ID) {
            node.Left = xoaNode(node.Left, id);
        } else if (id > node.Student_ID) {
            node.Right = xoaNode(node.Right, id);
        } else {
            // Tim thay node can xoa
            if (node.Left == null) return node.Right;
            if (node.Right == null) return node.Left;
            
            // Node co 2 con: lay node nho nhat ben phai
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
    
    // c) Xuat thong tin: diem TB, cao nhat, thap nhat
    public void xuatThongTin() {
        if (root == null) {
            System.out.println("Danh sach rong!");
            return;
        }
        
        ThongKe tk = new ThongKe();
        tinhThongKe(root, tk);
        
        System.out.println("\n=== THONG TIN ===");
        System.out.println("Diem trung binh: " + String.format("%.2f", tk.tongDiem / tk.soSV));
        System.out.println("SV diem cao nhat: " + tk.svMax);
        System.out.println("SV diem thap nhat: " + tk.svMin);
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
    
    // d) Thong ke so SV gioi, kha, TB, yeu
    public void thongKeDiem() {
        if (root == null) {
            System.out.println("Danh sach rong!");
            return;
        }
        
        PhanLoai pl = new PhanLoai();
        demPhanLoai(root, pl);
        
        System.out.println("\n=== THONG KE PHAN LOAI ===");
        System.out.println("Gioi (8.0-10): " + pl.gioi + " SV");
        System.out.println("Kha (6.5-7.9): " + pl.kha + " SV");
        System.out.println("TB (5.0-6.4): " + pl.trungBinh + " SV");
        System.out.println("Yeu (<5.0): " + pl.yeu + " SV");
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
    
    // Hien thi tat ca SV (in-order)
    public void hienThi() {
        System.out.println("\n=== DANH SACH SINH VIEN ===");
        inOrder(root);
    }
    
    private void inOrder(Student node) {
        if (node != null) {
            inOrder(node.Left);
            System.out.println(node);
            inOrder(node.Right);
        }
    }
    
    // Tim kiem sinh vien theo ID
    public void timKiem(int id) {
        Student ketQua = timKiemNode(root, id);
        if (ketQua != null) {
            System.out.println("Tim thay sinh vien:");
            System.out.println(ketQua);
        } else {
            System.out.println("Khong tim thay sinh vien co ID: " + id);
        }
    }
    
    private Student timKiemNode(Student node, int id) {
        if (node == null || node.Student_ID == id) {
            return node;
        }
        
        if (id < node.Student_ID) {
            return timKiemNode(node.Left, id);
        } else {
            return timKiemNode(node.Right, id);
        }
    }

    // Class ho tro thong ke
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
