import java.rmi.Naming;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) throws Exception {
        String host = args.length > 0 ? args[0] : "localhost";
        int port = args.length > 1 ? Integer.parseInt(args[1]) : 1099;
        IService s = (IService) Naming.lookup("rmi://" + host + ":" + port + "/Service");

        System.out.println("=== KET NOI RMI SERVER (" + host + ":" + port + ") THANH CONG ===");
        Scanner sc = new Scanner(System.in);
        while (true) {
            System.out.print("> Nhap du lieu: ");
            String line = sc.nextLine();
            if ("EXIT".equalsIgnoreCase(line.trim())) break;
            System.out.println("< Server tra ve: " + s.solve(line));
        }
    }
}

