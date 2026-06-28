package quanly;

import java.io.*;
import java.util.Scanner;

public class CayNhiPhan {
    private Node root;

    public CayNhiPhan() {
        this.root = null;
    }

    public void chen(int id) {
        root = chenDeQui(root, id);
    }

    private Node chenDeQui(Node current, int id) {
        if (current == null) return new Node(id);
        if (id < current.id) current.left = chenDeQui(current.left, id);
        else if (id > current.id) current.right = chenDeQui(current.right, id);
        return current;
    }
    
    public void xoa(int id) {
        root = xoaDeQui(root, id);
    }

    private Node xoaDeQui(Node current, int id) {
        if (current == null) return null;
        if (id < current.id) current.left = xoaDeQui(current.left, id);
        else if (id > current.id) current.right = xoaDeQui(current.right, id);
        else {
            if (current.left == null) return current.right;
            if (current.right == null) return current.left;
            Node nodeNhoNhat = timNodeNhoNhat(current.right);
            current.id = nodeNhoNhat.id;
            current.right = xoaDeQui(current.right, nodeNhoNhat.id);
        }
        return current;
    }
    
    public boolean tim(int id) {
        return timDeQui(root, id);
    }

    private boolean timDeQui(Node current, int id) {
        if (current == null) return false;
        if (id == current.id) return true;
        return id < current.id ? timDeQui(current.left, id) : timDeQui(current.right, id);
    }

    public int demNode() {
        return demNodeDeQui(root);
    }
    private int demNodeDeQui(Node node) {
        if (node == null) return 0;
        return 1 + demNodeDeQui(node.left) + demNodeDeQui(node.right);
    }

    public int demNodeLa() {
        return demNodeLaDeQui(root);
    }
    private int demNodeLaDeQui(Node node) {
        if (node == null) return 0;
        if (node.left == null && node.right == null) return 1;
        return demNodeLaDeQui(node.left) + demNodeLaDeQui(node.right);
    }

    public int timMin() {
        if (root == null) throw new IllegalStateException("Cay rong");
        return timNodeNhoNhat(root).id;
    }
    private Node timNodeNhoNhat(Node node) {
        return node.left == null ? node : timNodeNhoNhat(node.left);
    }
    
    public int timMax() {
        if (root == null) throw new IllegalStateException("Cay rong");
        Node current = root;
        while (current.right != null) current = current.right;
        return current.id;
    }

    public double tinhTB() {
        if (root == null) return 0.0;
        int sum = tinhTongDeQui(root);
        int count = demNodeDeQui(root);
        return (double) sum / count;
    }
    private int tinhTongDeQui(Node node) {
        if (node == null) return 0;
        return node.id + tinhTongDeQui(node.left) + tinhTongDeQui(node.right);
    }

    public void hienThi() {
        System.out.print("Cay (LNR): ");
        hienThiDeQui(root);
        System.out.println();
    }
    private void hienThiDeQui(Node node) {
        if (node != null) {
            hienThiDeQui(node.left);
            System.out.print(node.id + " ");
            hienThiDeQui(node.right);
        }
    }
    
    public void luuFile(String tenFile) {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(tenFile))) {
            oos.writeObject(this.root);
            System.out.println("=> Da luu cay vao file '" + tenFile + "' thanh cong.");
        } catch (IOException e) {
            System.err.println("Loi khi luu file: " + e.getMessage());
        }
    }

    public void docFile(String tenFile) {
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(tenFile))) {
            this.root = (Node) ois.readObject();
            System.out.println("=> Da doc cay tu file '" + tenFile + "' thanh cong.");
        } catch (IOException | ClassNotFoundException e) {
            System.err.println("Loi khi doc file. Co the file khong ton tai hoac bi loi.");
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        CayNhiPhan bst = new CayNhiPhan();
        String tenFile = "cay_bst.dat";
        int luaChon;

        int[] duLieu = {50, 30, 70, 20, 40, 60, 80};
        for (int giaTri : duLieu) bst.chen(giaTri);

        do {
            System.out.println("\n========= MENU CAY NHI PHAN =========");
            System.out.println("1. Chen mot Node");
            System.out.println("2. Xoa mot Node");
            System.out.println("3. Tim mot Node");
            System.out.println("4. Hien thi cay (LNR)");
            System.out.println("5. Thong ke (Dem Node, Node la)");
            System.out.println("6. Tim Min / Max");
            System.out.println("7. Tinh gia tri trung binh");
            System.out.println("8. Luu cay ra file");
            System.out.println("9. Doc cay tu file");
            System.out.println("0. Thoat");
            System.out.print(">> Vui long chon: ");
            
            luaChon = scanner.nextInt();
            scanner.nextLine(); 

            switch (luaChon) {
                case 1:
                    System.out.print("Nhap gia tri can chen: ");
                    bst.chen(scanner.nextInt());
                    bst.hienThi();
                    break;
                case 2:
                    System.out.print("Nhap gia tri can xoa: ");
                    bst.xoa(scanner.nextInt());
                    bst.hienThi();
                    break;
                case 3:
                    System.out.print("Nhap gia tri can tim: ");
                    if (bst.tim(scanner.nextInt())) System.out.println("=> Tim thay!");
                    else System.out.println("=> Khong tim thay!");
                    break;
                case 4:
                    bst.hienThi();
                    break;
                case 5:
                    System.out.println("Tong so Node: " + bst.demNode());
                    System.out.println("So Node la: " + bst.demNodeLa());
                    break;
                case 6:
                    try {
                        System.out.println("Node nho nhat: " + bst.timMin());
                        System.out.println("Node lon nhat: " + bst.timMax());
                    } catch (IllegalStateException e) { System.out.println(e.getMessage()); }
                    break;
                case 7:
                    System.out.printf("Gia tri trung binh: %.2f\n", bst.tinhTB());
                    break;
                case 8:
                    bst.luuFile(tenFile);
                    break;
                case 9:
                    bst.docFile(tenFile);
                    bst.hienThi();
                    break;
                case 0:
                    System.out.println("Dang thoat chuong trinh...");
                    break;
                default:
                    System.out.println("Lua chon khong hop le. Vui long chon lai.");
            }
        } while (luaChon != 0);
        scanner.close();
    }
}
