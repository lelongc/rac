package BSTkh;

import java.util.ArrayList;
import java.util.List;

public class BSTCustomer {
    private BSTNode root;
    
    public BSTCustomer() {
        this.root = null;
    }
    
    public void insert(Customer customer) {
        root = insertRec(root, customer);
    }
    
    private BSTNode insertRec(BSTNode root, Customer customer) {
        if (root == null) {
            root = new BSTNode(customer);
            return root;
        }
        
        if (customer.getCustomer_ID() < root.customer.getCustomer_ID()) {
            root.left = insertRec(root.left, customer);
        } else if (customer.getCustomer_ID() > root.customer.getCustomer_ID()) {
            root.right = insertRec(root.right, customer);
        }
        
        return root;
    }
    
    public Customer search(int customer_ID) {
        BSTNode result = searchRec(root, customer_ID);
        return result != null ? result.customer : null;
    }
    
    private BSTNode searchRec(BSTNode root, int customer_ID) {
        if (root == null || root.customer.getCustomer_ID() == customer_ID) {
            return root;
        }
        
        if (customer_ID < root.customer.getCustomer_ID()) {
            return searchRec(root.left, customer_ID);
        }
        
        return searchRec(root.right, customer_ID);
    }
    
    public List<Customer> inOrderTraversal() {
        List<Customer> result = new ArrayList<>();
        inOrderRec(root, result);
        return result;
    }
    
    private void inOrderRec(BSTNode root, List<Customer> result) {
        if (root != null) {
            inOrderRec(root.left, result);
            result.add(root.customer);
            inOrderRec(root.right, result);
        }
    }
    
    public void printInOrder() {
        System.out.println("\n=== Danh sách khách hàng sắp xếp theo ID (BST) ===");
        List<Customer> customers = inOrderTraversal();
        for (Customer customer : customers) {
            System.out.println(customer);
        }
    }
}
