package quanly;

import java.io.Serializable;

public class Node implements Serializable {
    private static final long serialVersionUID = 1L;

    int id;
    Node left;
    Node right;

    public Node(int id) {
        this.id = id;
        this.left = null;
        this.right = null;
    }
}

