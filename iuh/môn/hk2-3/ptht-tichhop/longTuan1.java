import java.util.Scanner;

class cau1 {
	public void inCau1() {
		System.out.println("Hello, World!");
	}
}

class cau2 {
	public void inCau2(Scanner scanner) {
		System.out.print("What's your name? ");
		String name = scanner.nextLine();
		System.out.println("Hi, I am " + name);
	}
}

class cau3 {
	public void inCau3(Scanner scanner) {
		System.out.print("nhap so A: ");
		int a = scanner.nextInt();
		System.out.print("nhap so B: ");
		int b = scanner.nextInt();
		System.out.println("sum = " + (a + b));
	}
}

class cau4 {
	public void inCau4(Scanner scanner) {
		System.out.print("nhap 1 so: ");
		int so = scanner.nextInt();
		if (so % 2 == 0) {
			System.out.println("so chan");
		} else {
			System.out.println("so le");
		}
	}
}

class cau5 {
	public void inCau5(Scanner scanner) {
		System.out.print("nhap so thang : ");
		int thang = scanner.nextInt();

		switch (thang) {
		case 1:
			System.out.println("January");
			break;
		case 2:
			System.out.println("February");
			break;
		case 3:
			System.out.println("March");
			break;
		case 4:
			System.out.println("April");
			break;
		case 5:
			System.out.println("May");
			break;
		case 6:
			System.out.println("June");
			break;
		case 7:
			System.out.println("July");
			break;
		case 8:
			System.out.println("August");
			break;
		case 9:
			System.out.println("September");
			break;
		case 10:
			System.out.println("October");
			break;
		case 11:
			System.out.println("November");
			break;
		case 12:
			System.out.println("December");
			break;
		default:
			System.out.println("Tháng không hợp lệ");
		}
	}
}

public class LeLongTuan1 {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		cau1 c1 = new cau1();
		cau2 c2 = new cau2();
		cau3 c3 = new cau3();
		cau4 c4 = new cau4();
		cau5 c5 = new cau5();

		c1.inCau1();
		c2.inCau2(scanner);
		c3.inCau3(scanner);
		c4.inCau4(scanner);
		c5.inCau5(scanner);

		scanner.close();
	}
}
