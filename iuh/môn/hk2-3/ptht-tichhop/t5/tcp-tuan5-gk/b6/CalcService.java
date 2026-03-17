package b6;
/*
 * Bai 6 - CalcService
 * Chua cac cong thuc tinh toan dung chung cho TCP va UDP.
 * choice=1: 1+3+...+(2n+1)
 * choice=2: 1*2 + 2*3 + ... + n*(n+1)
 * choice=3: 1-2+3-4+...+(2n+1)
 */
public class CalcService {
    public static long calc(int choice, int n) {
        if (n < 0) throw new IllegalArgumentException("n phai >= 0");
        switch (choice) {
            case 1:
                long k = (long) n + 1;
                return k * k;
            case 2:
                long nn = n;
                long a = nn * (nn + 1) * (2 * nn + 1) / 6;
                long b = nn * (nn + 1) / 2;
                return a + b;
            case 3:
                return (long) n + 1;
            default:
                throw new IllegalArgumentException("choice phai la 1/2/3");
        }
    }
}