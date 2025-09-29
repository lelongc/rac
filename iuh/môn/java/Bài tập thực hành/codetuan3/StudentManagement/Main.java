package codetuan3.StudentManagement;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {

		Scanner scanner = new Scanner(System.in);
		StudentManagement manager = new StudentManagement();

		manager.addStudent(new Student(1, "Nguyen Van An", 8.5));
		manager.addStudent(new Student(2, "Le Thi Binh", 9.0));
		manager.addStudent(new Student(3, "Tran Van Chien", 7.5));

		while (true) {

			System.out.println("\n--- MENU QUẢN LÝ SINH VIÊN ---");
			System.out.println("1. Thêm sinh viên mới");
			System.out.println("2. Xóa sinh viên theo ID");
			System.out.println("3. Sắp xếp sinh viên theo tên");
			System.out.println("4. Sắp xếp sinh viên theo điểm (cao đến thấp)");
			System.out.println("5. Hiển thị danh sách sinh viên");
			System.out.println("0. Thoát chương trình");
			System.out.print(">> Vui lòng chọn chức năng: ");

			int choice = -1;
			try {
				choice = scanner.nextInt();
			} catch (InputMismatchException e) {
				System.out.println("Lỗi: Vui lòng chỉ nhập số!");
				scanner.next();
				continue;
			}

			switch (choice) {
				case 1:

					System.out.println("--- Thêm sinh viên mới ---");
					System.out.print("Nhập ID: ");
					int id = scanner.nextInt();
					scanner.nextLine();
					System.out.print("Nhập tên: ");
					String name = scanner.nextLine();

					System.out.print("Nhập điểm: ");
					double result = scanner.nextDouble();

					manager.addStudent(new Student(id, name, result));
					break;
				case 2:

					System.out.print("Nhập ID sinh viên cần xóa: ");
					int removeId = scanner.nextInt();
					manager.removeStudent(removeId);
					break;
				case 3:

					manager.sortByName();
					manager.displayStudents();
					break;
				case 4:

					manager.sortBySe();
					manager.displayStudents();
					break;
				case 5:
					manager.displayStudents();
					break;
				case 0:

					System.out.println("Cảm ơn đã sử dụng chương trình!");
					scanner.close();
					System.exit(0);
					break;
				default:

					System.out.println("Lựa chọn không hợp lệ, vui lòng chọn lại từ 0 đến 5.");
			}
		}

	}

}
