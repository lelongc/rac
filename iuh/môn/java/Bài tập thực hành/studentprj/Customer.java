// package studentprj;
// public class Student_Manage {
//     static Scanner scan = new Scanner(System.in);
//     static LinkedList<Student> studentList = new LinkedList<>();

//     // Đọc danh sách sinh viên từ file
//     @SuppressWarnings("unchecked")
//     public static LinkedList<Student> readFromFile(String path) {
//         LinkedList<Student> list = null;
//         try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(path))) {
//             list = (LinkedList<Student>) ois.readObject();
//         } catch (Exception e) {
//             e.printStackTrace();
//         }
//         return list != null ? list : new LinkedList<>();
//     }

//     // Lưu danh sách sinh viên ra file
//     public static boolean saveToFile(LinkedList<Student> list, String path) {
//         try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(path))) {
//             oos.writeObject(list);
//             return true;
//         } catch (Exception e) {
//             e.printStackTrace();
//             return false;
//         }
//     }

//     // Xuất thông tin danh sách sinh viên
//     public static void displayStudentList(LinkedList<Student> list) {
//         System.out.printf("%-10s %-20s %-10s %-10s\n", "ID", "Name", "Result", "Rank");
//         for (Student student : list) {
//             System.out.println(student);
//         }
//     }

//     // Thêm sinh viên mới vào danh sách
//     public static void addStudent(LinkedList<Student> list) {
//         System.out.println("Enter Student ID: ");
//         String id = scan.nextLine();
//         System.out.println("Enter Student Name: ");
//         String name = scan.nextLine();
//         Student student = new Student(id, name);
//         list.add(student);
//     }

//     // Tìm kiếm sinh viên theo mã sinh viên
//     public static int findStudentById(LinkedList<Student> list, String id) {
//         for (int i = 0; i < list.size(); i++) {
//             if (list.get(i).getStudent_id().equalsIgnoreCase(id)) {
//                 return i;
//             }
//         }
//         return -1;
//     }

//     // Xóa sinh viên khỏi danh sách
//     public static void deleteStudent(LinkedList<Student> list) {
//         System.out.println("Enter Student ID to delete: ");
//         String id = scan.nextLine();
//         int index = findStudentById(list, id);
//         if (index != -1) {
//             list.remove(index);
//             System.out.println("Student deleted successfully.");
//         } else {
//             System.out.println("Student not found.");
//         }
//     }

//     // Sắp xếp danh sách sinh viên theo họ tên
//     public static void sortStudentsByName(LinkedList<Student> list) {
//         list.sort((s1, s2) -> s1.getStudent_name().compareToIgnoreCase(s2.getStudent_name()));
//         System.out.println("List sorted by name.");
//     }

//     // Cập nhật điểm trung bình của sinh viên
//     public static void updateStudentResult(LinkedList<Student> list) {
//         System.out.println("Enter Student ID to update result: ");
//         String id = scan.nextLine();
//         int index = findStudentById(list, id);
//         if (index != -1) {
//             System.out.println("Enter new result: ");
//             double result = scan.nextDouble();
//             scan.nextLine(); // Clear buffer
//             list.get(index).setStudent_result(result);
//             System.out.println("Student result updated.");
//         } else {
//             System.out.println("Student not found.");
//         }
//     }

//     // Menu chính
//     public static void main(String[] args) {
//         String filePath = "students.dat";
//         int choice;
//         do {
//             System.out.println("\n--- STUDENT MANAGEMENT SYSTEM ---");
//             System.out.println("1. Read Student List from File");
//             System.out.println("2. Save Student List to File");
//             System.out.println("3. Display Student List");
//             System.out.println("4. Add Student");
//             System.out.println("5. Find Student by ID");
//             System.out.println("6. Delete Student by ID");
//             System.out.println("7. Sort Students by Name");
//             System.out.println("8. Update Student Result");
//             System.out.println("0. Exit");
//             System.out.print("Enter your choice: ");
//             choice = scan.nextInt();
//             scan.nextLine(); // Clear buffer
//             switch (choice) {
//                 case 1 -> studentList = readFromFile(filePath);
//                 case 2 -> {
//                     if (saveToFile(studentList, filePath)) System.out.println("Data saved successfully.");
//                     else System.out.println("Error saving data.");
//                 }
//                 case 3 -> displayStudentList(studentList);
//                 case 4 -> addStudent(studentList);
//                 case 5 -> {
//                     System.out.println("Enter Student ID to search: ");
//                     String id = scan.nextLine();
//                     int index = findStudentById(studentList, id);
//                     if (index != -1) System.out.println(studentList.get(index));
//                     else System.out.println("Student not found.");
//                 }
//                 case 6 -> deleteStudent(studentList);
//                 case 7 -> sortStudentsByName(studentList);
//                 case 8 -> updateStudentResult(studentList);
//                 case 0 -> System.out.println("Exiting program.");
//                 default -> System.out.println("Invalid choice. Please try again.");
//             }
//         } while (choice != 0);
//     }
// }
