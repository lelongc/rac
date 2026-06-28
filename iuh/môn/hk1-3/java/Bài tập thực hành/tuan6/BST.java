

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;

import org.w3c.dom.Node;

public class BST {
	private Node root;

	public BST() {
		this.root = null;
	}

	public void insert(int id) {
		root = insertr(root, id);
	}

	private Node insertr(Node cur, int id) {
		if (cur == null) return new Node(id);
		if (id < cur.id) {
			cur.left = insertr(cur.left, id);
		} else if (id > cur.id) {
			cur.right = insertr(cur.right, id);
		}
		return cur;
	}

	public boolean find(int id) {
		return findr(root, id);
	}

	private boolean findr(Node cur, int id) {
		if (cur == null) return false;
		if (cur.id == id) return true;
		
		if (id < cur.id) {
			return findr(cur.left, id);
		} else {
			return findr(cur.right, id);
		}
	}

	private Node nhonhat(Node cur) {
		return cur.left == null ? cur : nhonhat(cur.left);
	}

	public void del(int id) {
		root = delr(root, id);
	}

	private Node delr(Node cur, int id) {
		if (cur == null) return null;
		if (id < cur.id) {
			cur.left = delr(cur.left, id);
		} else if (id > cur.id) {
			cur.right = delr(cur.right, id);
		} else {
			if (cur.left == null) return cur.right;
			else if (cur.right == null) return cur.left;
			
			Node smallestNode = nhonhat(cur.right);
			cur.id = smallestNode.id;
			cur.right = delr(cur.right, smallestNode.id);
		}
		return cur;
	}


	public void preOrder() { System.out.print("NLR: "); NLR(root); System.out.println(); }
	public void inOrder() { System.out.print("LNR: "); LNR(root); System.out.println(); }
	public void postOrder() { System.out.print("LRN: "); LRN(root); System.out.println(); }

	private void NLR(Node cur) {
		if (cur != null) {
			System.out.print(cur.id + " "); 
			NLR(cur.left);
			NLR(cur.right);
		}
	}
	private void LNR(Node cur) {
		if (cur != null) {
			LNR(cur.left);
			System.out.print(cur.id + " ");
			LNR(cur.right);
		}
	}
	private void LRN(Node cur) {
		if (cur != null) {
			LRN(cur.left);
			LRN(cur.right);
			System.out.print(cur.id + " ");
		}
	}

	public int count() { return countr(root); }
	private int countr(Node cur) {
		if (cur == null) return 0;
		return 1 + countr(cur.left) + countr(cur.right);
	}

	public int countLeaf() { return countlr(root); }
	private int countlr(Node cur) {
		if (cur == null) return 0;
		if (cur.left == null && cur.right == null) return 1;
		return countlr(cur.left) + countlr(cur.right);
	}

	public void saveToFile(String filename) {
		try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(filename))) {
			oos.writeObject(this.root);
			System.out.println("=> Đã lưu cây vào file '" + filename + "' thành công.");
		} catch (IOException e) {
			System.err.println("Lỗi khi lưu file: " + e.getMessage());
		}
	}

	public void loadFromFile(String filename) {
		try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(filename))) {
			this.root = (Node) ois.readObject();
			System.out.println("=> Đã đọc cây từ file '" + filename + "' thành công.");
		} catch (IOException | ClassNotFoundException e) {
			System.err.println("Lỗi khi đọc file: " + e.getMessage());
		}
	}
    
   
	private int tong(Node cur) {
		if (cur == null) return 0;
		return cur.id + tong(cur.left) + tong(cur.right);
	}
	private int nhohon(Node cur, double tb) {
		if (cur == null) return 0;
		int curcount = (cur.id < tb) ? 1 : 0;
		return curcount + nhohon(cur.left, tb) + nhohon(cur.right, tb);
	}
	private int lonhon(Node cur, double tb) {
		if (cur == null) return 0;
		int curcount = (cur.id > tb) ? 1 : 0;
		return curcount + lonhon(cur.left, tb) + lonhon(cur.right, tb);
	}
	public void calculate() {
		int count = count();
		if (count == 0) {
			System.out.println("Cây rỗng, không thể thống kê.");
            return;
		}
		int sum = tong(root);
		double avg = (double) sum / count;
        
        System.out.println("Giá trị trung bình: " + String.format("%.2f", avg));
        System.out.println("Số node nhỏ hơn trung bình: " + nhohon(root, avg));
        System.out.println("Số node lớn hơn trung bình: " + lonhon(root, avg));
	}

 
	public static void main(String[] args) {
		BST tree = new BST();
        int[] nodes = {55, 65, 45, 40, 50, 60, 75, 35, 70, 80, 20, 90, 25, 85, 15, 30};
        
        System.out.println("--- 1. Chèn các node vào cây ---");
        for (int value : nodes) {
            tree.insert(value);
        }
        

        System.out.println("\n--- 2. Duyệt cây ---");
        tree.preOrder();
        tree.inOrder();
        tree.postOrder();
        
        System.out.println("\n--- 3. Đếm node ---");
        System.out.println("Tổng số node: " + tree.count());
        System.out.println("Số node lá: " + tree.countLeaf());
        
        System.out.println("\n--- 4. Tìm kiếm ---");
        System.out.println("Tìm node 70: " + (tree.find(70) ? "Tìm thấy" : "Không tìm thấy"));
        System.out.println("Tìm node 99: " + (tree.find(99) ? "Tìm thấy" : "Không tìm thấy"));

        System.out.println("\n--- 5. Xóa node ---");
        System.out.println("Xóa node 20 (node lá)...");
        tree.del(20);
        tree.inOrder();
        System.out.println("Xóa node 75 (có 2 con)...");
        tree.del(75);
        tree.inOrder();

        System.out.println("\n--- 6. Lưu và đọc file ---");
        String filename = "tree.dat";
        tree.saveToFile(filename);
        
        BST loadedTree = new BST();
        loadedTree.loadFromFile(filename);
        System.out.print("Cây được load từ file: ");
        loadedTree.inOrder();

        System.out.println("\n--- 7. Thống kê trên cây đã load ---");
        loadedTree.calculate();
	}
}