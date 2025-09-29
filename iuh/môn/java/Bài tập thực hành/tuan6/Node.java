package tuan6;

import java.io.Serializable;

public class Node implements Serializable {
	int id;
	Node left;
	Node right;
	
	public Node(int id) {
		this.id = id;
		this.left = null;
		this.right = null;
	}
	
}
