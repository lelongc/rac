import java.rmi.Naming;

public class rmiClient {
    public static void main(String[] args) {
        try {
            phepCong_intf stub = (phepCong_intf)Naming.lookup("rmi://localhost:1100/congService");
            int result_int = stub.tong2songuyen(5, 5);
            double result_double = stub.tong2sothuc(7.7, 3.3);
            int result_3_int = stub.tong3songuyen(1, 1, 1);
            
            System.out.println(result_int);
            System.out.println(result_double);
            System.out.println(result_3_int);
            
            xulychuoi_intf stub2 = (xulychuoi_intf)Naming.lookup("rmi://localhost:1100/chuoiService");
            String result_str = stub2.noi2chuoi("phat trien", " ht th");
            System.out.println(result_str);
            
        } catch (Exception e) {
        }
    }
}