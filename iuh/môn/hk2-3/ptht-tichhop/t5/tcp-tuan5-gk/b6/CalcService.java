package b6;

public class CalcService {

    public static long calc(int choice, int n) {
        if (n < 0) throw new IllegalArgumentException("n phai >= 0");

        switch (choice) {
            case 1:
                // 1 + 3 + 5 + ... + (2n + 1)
                // có (n+1) số: sum = (n+1)^2
                long k = (long) n + 1;
                return k * k;

            case 2:
                // sum i*(i+1), i=1..n = sum (i^2 + i) = n(n+1)(2n+1)/6 + n(n+1)/2
                long nn = n;
                long a = nn * (nn + 1) * (2 * nn + 1) / 6;
                long b = nn * (nn + 1) / 2;
                return a + b;

            case 3:
                // 1 - 2 + 3 - 4 + ... + (2n+1)
                // nhóm (1-2) + (3-4) + ... + ((2n-1) - 2n) + (2n+1)
                // = (-1)*n + (2n+1) = n+1
                return (long) n + 1;

            default:
                throw new IllegalArgumentException("choice phai la 1/2/3");
        }
    }
}