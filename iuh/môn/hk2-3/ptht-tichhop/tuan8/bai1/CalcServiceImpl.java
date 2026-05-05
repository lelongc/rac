package bai1;


import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.ArrayList;
import java.util.List;

public class CalcServiceImpl extends UnicastRemoteObject implements CalcService {

    protected CalcServiceImpl() throws RemoteException {
        super();
    }

    @Override
    public String evaluate(String expression) throws RemoteException {
        try {
            double value = eval(expression);
         
            if (Math.abs(value - Math.rint(value)) < 1e-12) {
                return String.valueOf((long) Math.rint(value));
            }
            return String.valueOf(value);
        } catch (IllegalArgumentException ex) {
            return "ERROR: " + ex.getMessage();
        } catch (ArithmeticException ex) {
            return "ERROR: " + ex.getMessage();
        } catch (Exception ex) {
            return "ERROR: bieu thuc khong hop le";
        }
    }


    private double eval(String s) {
        if (s == null) throw new IllegalArgumentException("bieu thuc rong");
        s = s.replaceAll("\\s+", "");
        if (s.isEmpty()) throw new IllegalArgumentException("bieu thuc rong");

        
        if (!Character.isDigit(s.charAt(0))) {
            throw new IllegalArgumentException("bieu thuc phai bat dau bang so");
        }

        List<Double> nums = new ArrayList<>();
        List<Character> ops = new ArrayList<>();

        int i = 0;
        while (i < s.length()) {
            if (!Character.isDigit(s.charAt(i))) {
                throw new IllegalArgumentException("gap ky tu khong hop le tai vi tri " + i);
            }

            long n = 0;
            while (i < s.length() && Character.isDigit(s.charAt(i))) {
                n = n * 10 + (s.charAt(i) - '0');
                i++;
            }
            nums.add((double) n);

            if (i < s.length()) {
                char op = s.charAt(i);
                if (op != '+' && op != '-' && op != '*' && op != '/') {
                    throw new IllegalArgumentException("toan tu khong hop le: " + op);
                }
                ops.add(op);
                i++;

                if (i >= s.length()) {
                    throw new IllegalArgumentException("bieu thuc khong du so hang (ket thuc bang toan tu)");
                }
            }
        }

        
        List<Double> nums2 = new ArrayList<>();
        List<Character> ops2 = new ArrayList<>();

        nums2.add(nums.get(0));
        for (int k = 0; k < ops.size(); k++) {
            char op = ops.get(k);
            double b = nums.get(k + 1);

            if (op == '*' || op == '/') {
                double a = nums2.remove(nums2.size() - 1);
                if (op == '/') {
                    if (Math.abs(b) < 1e-12) throw new ArithmeticException("chia cho 0");
                    nums2.add(a / b);
                } else {
                    nums2.add(a * b);
                }
            } else {
                ops2.add(op);
                nums2.add(b);
            }
        }

        
        double result = nums2.get(0);
        for (int k = 0; k < ops2.size(); k++) {
            char op = ops2.get(k);
            double b = nums2.get(k + 1);
            if (op == '+') result += b;
            else result -= b;
        }

        return result;
    }
}
