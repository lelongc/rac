package BSTkh;

import java.util.regex.Pattern;

class InvalidAgeException extends Exception {
    /**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	public InvalidAgeException(String message) {
        super(message);
    }
}

class InvalidEmailException extends Exception {
    /**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	public InvalidEmailException(String message) {
        super(message);
    }
}

class InvalidPhoneException extends Exception {
    /**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	public InvalidPhoneException(String message) {
        super(message);
    }
}

public class Customer implements Comparable<Customer> {
    private int customer_ID;
    private String customer_Name;
    private int customer_Age;
    private String customer_Gender;
    private String customer_Email;
    private String customer_Phone;
    
    
    private static final Pattern EMAIL_PATTERN = 
        Pattern.compile("^[A-Za-z0-9+_.-]+@([A-Za-z0-9.-]+\\.[A-Za-z]{2,})$");
    
    
    private static final Pattern PHONE_PATTERN = 
        Pattern.compile("^(\\+84|0)[0-9]{9,10}$");
    
    public Customer(int customer_ID, String customer_Name, int customer_Age, 
                   String customer_Gender, String customer_Email, String customer_Phone) 
                   throws InvalidAgeException, InvalidEmailException, InvalidPhoneException {
        validateAge(customer_Age);
        validateEmail(customer_Email);
        validatePhone(customer_Phone);
        
        this.customer_ID = customer_ID;
        this.customer_Name = customer_Name;
        this.customer_Age = customer_Age;
        this.customer_Gender = customer_Gender;
        this.customer_Email = customer_Email;
        this.customer_Phone = customer_Phone;
    }
    
    private void validateAge(int age) throws InvalidAgeException {
        if (age < 18) {
            throw new InvalidAgeException("Tuổi phải >= 18. Tuổi nhập vào: " + age);
        }
    }
    
    private void validateEmail(String email) throws InvalidEmailException {
        if (!EMAIL_PATTERN.matcher(email).matches()) {
            throw new InvalidEmailException("Email không hợp lệ: " + email);
        }
    }
    
    private void validatePhone(String phone) throws InvalidPhoneException {
        if (!PHONE_PATTERN.matcher(phone).matches()) {
            throw new InvalidPhoneException("Số điện thoại không hợp lệ: " + phone);
        }
    }
    
   
    public int getCustomer_ID() { return customer_ID; }
    public void setCustomer_ID(int customer_ID) { this.customer_ID = customer_ID; }
    
    public String getCustomer_Name() { return customer_Name; }
    public void setCustomer_Name(String customer_Name) { this.customer_Name = customer_Name; }
    
    public int getCustomer_Age() { return customer_Age; }
    public void setCustomer_Age(int customer_Age) throws InvalidAgeException {
        validateAge(customer_Age);
        this.customer_Age = customer_Age;
    }
    
    public String getCustomer_Gender() { return customer_Gender; }
    public void setCustomer_Gender(String customer_Gender) { this.customer_Gender = customer_Gender; }
    
    public String getCustomer_Email() { return customer_Email; }
    public void setCustomer_Email(String customer_Email) throws InvalidEmailException {
        validateEmail(customer_Email);
        this.customer_Email = customer_Email;
    }
    
    public String getCustomer_Phone() { return customer_Phone; }
    public void setCustomer_Phone(String customer_Phone) throws InvalidPhoneException {
        validatePhone(customer_Phone);
        this.customer_Phone = customer_Phone;
    }
    
    @Override
    public int compareTo(Customer other) {
        return Integer.compare(this.customer_ID, other.customer_ID);
    }
    
    @Override
    public String toString() {
        return String.format("ID: %d, Name: %s, Age: %d, Gender: %s, Email: %s, Phone: %s",
                customer_ID, customer_Name, customer_Age, customer_Gender, customer_Email, customer_Phone);
    }
}

class BSTNode {
    Customer customer;
    BSTNode left, right;
    
    public BSTNode(Customer customer) {
        this.customer = customer;
        this.left = this.right = null;
    }
}
