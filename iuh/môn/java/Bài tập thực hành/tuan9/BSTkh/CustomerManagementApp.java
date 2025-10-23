package BSTkh;

import java.util.*;
import java.util.stream.Collectors;

public class CustomerManagementApp {
    private static Scanner scanner = new Scanner(System.in);
    private static List<Customer> customers = new ArrayList<>();
    private static BSTCustomer bst = new BSTCustomer();
    
    public static void main(String[] args) {
        System.out.println("=== CHƯƠNG TRÌNH QUẢN LÝ KHÁCH HÀNG ===\n");
        
        
        inputCustomers();
        
        
        performOperations();
        
       
        addToBSTAndDisplay();
        
        scanner.close();
    }
    
    private static void inputCustomers() {
        System.out.println("Nhập thông tin 10 khách hàng:");
        System.out.println("(Tuổi >= 18, Email hợp lệ, SĐT định dạng: +84xxxxxxxxx hoặc 0xxxxxxxxx)\n");
        
        for (int i = 0; i < 10; i++) {
            while (true) {
                try {
                    System.out.println("--- Khách hàng thứ " + (i + 1) + " ---");
                    System.out.print("ID: ");
                    int id = scanner.nextInt();
                    scanner.nextLine(); 
                    
                    System.out.print("Tên: ");
                    String name = scanner.nextLine();
                    
                    System.out.print("Tuổi: ");
                    int age = scanner.nextInt();
                    scanner.nextLine(); 
                    
                    System.out.print("Giới tính (Nam/Nữ): ");
                    String gender = scanner.nextLine();
                    
                    System.out.print("Email: ");
                    String email = scanner.nextLine();
                    
                    System.out.print("SĐT: ");
                    String phone = scanner.nextLine();
                    
                    Customer customer = new Customer(id, name, age, gender, email, phone);
                    customers.add(customer);
                    System.out.println("Thêm khách hàng thành công!\n");
                    break;
                    
                } catch (InvalidAgeException | InvalidEmailException | InvalidPhoneException e) {
                    System.out.println("Lỗi: " + e.getMessage());
                    System.out.println("Vui lòng nhập lại thông tin khách hàng này.\n");
                } catch (InputMismatchException e) {
                    System.out.println("Lỗi: Dữ liệu nhập vào không hợp lệ!");
                    System.out.println("Vui lòng nhập lại thông tin khách hàng này.\n");
                    scanner.nextLine(); 
                }
            }
        }
    }
    
    private static void performOperations() {
       
        System.out.println("=== 1. Sắp xếp danh sách theo tuổi ===");
        List<Customer> sortedByAge = new ArrayList<>(customers);
        sortedByAge.sort(Comparator.comparing(Customer::getCustomer_Age));
        sortedByAge.forEach(System.out::println);
        
       
        System.out.println("\n=== 2. Sắp xếp danh sách theo tên ===");
        List<Customer> sortedByName = new ArrayList<>(customers);
        sortedByName.sort(Comparator.comparing(Customer::getCustomer_Name));
        sortedByName.forEach(System.out::println);
        
       
        System.out.println("\n=== 3. Khách hàng nữ tuổi nhỏ nhất và lớn nhất ===");
        List<Customer> femaleCustomers = customers.stream()
            .filter(c -> c.getCustomer_Gender().equalsIgnoreCase("Nu"))
            .collect(Collectors.toList());
        
        if (!femaleCustomers.isEmpty()) {
            Customer youngestFemale = femaleCustomers.stream()
                .min(Comparator.comparing(Customer::getCustomer_Age)).orElse(null);
            Customer oldestFemale = femaleCustomers.stream()
                .max(Comparator.comparing(Customer::getCustomer_Age)).orElse(null);
            
            System.out.println("Khách hàng nữ trẻ nhất: " + youngestFemale);
            System.out.println("Khách hàng nữ lớn tuổi nhất: " + oldestFemale);
        } else {
            System.out.println("Không có khách hàng nữ trong danh sách.");
        }
        
       
        System.out.println("\n=== 4. Khách hàng nam tuổi nhỏ nhất và lớn nhất ===");
        List<Customer> maleCustomers = customers.stream()
            .filter(c -> c.getCustomer_Gender().equalsIgnoreCase("Nam"))
            .collect(Collectors.toList());
        
        if (!maleCustomers.isEmpty()) {
            Customer youngestMale = maleCustomers.stream()
                .min(Comparator.comparing(Customer::getCustomer_Age)).orElse(null);
            Customer oldestMale = maleCustomers.stream()
                .max(Comparator.comparing(Customer::getCustomer_Age)).orElse(null);
            
            System.out.println("Khách hàng nam trẻ nhất: " + youngestMale);
            System.out.println("Khách hàng nam lớn tuổi nhất: " + oldestMale);
        } else {
            System.out.println("Không có khách hàng nam trong danh sách.");
        }
        
     
        System.out.println("\n=== 5. Trung bình tuổi khách hàng nữ ===");
        if (!femaleCustomers.isEmpty()) {
            double avgAgeFemale = femaleCustomers.stream()
                .mapToInt(Customer::getCustomer_Age)
                .average().orElse(0.0);
            System.out.printf("Trung bình tuổi khách hàng nữ: %.2f\n", avgAgeFemale);
        } else {
            System.out.println("Không có khách hàng nữ để tính trung bình.");
        }
        
       
        System.out.println("\n=== 6. Trung bình tuổi khách hàng nam ===");
        if (!maleCustomers.isEmpty()) {
            double avgAgeMale = maleCustomers.stream()
                .mapToInt(Customer::getCustomer_Age)
                .average().orElse(0.0);
            System.out.printf("Trung bình tuổi khách hàng nam: %.2f\n", avgAgeMale);
        } else {
            System.out.println("Không có khách hàng nam để tính trung bình.");
        }
    }
    
    private static void addToBSTAndDisplay() {
        System.out.println("\n=== 7. Thêm vào BST và hiển thị theo ID ===");
        System.out.println("Đang thêm khách hàng vào cây nhị phân tìm kiếm...");
        
        for (Customer customer : customers) {
            bst.insert(customer);
        }
        
        bst.printInOrder();
        
        System.out.println("\n=== Chương trình kết thúc ===");
    }
}
