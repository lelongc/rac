// package studentprj;
// import java.io.FileInputStream;
// import java.io.FileOutputStream;
// import java.io.ObjectInputStream;
// import java.io.ObjectOutputStream;
// import java.util.ArrayList;
// import java.util.LinkedList;
// import java.util.Scanner;

// public class Student_Manage {
// 	static Scanner scan = new Scanner(System.in);
// 	static int stt=0;
	
// 	public static boolean Save_to_file(Student ds, String path) {
//         try {
//             FileOutputStream fos = new FileOutputStream(path);
//             ObjectOutputStream oos = new ObjectOutputStream(fos);
//             oos.writeObject(ds);
//             oos.close();
//             fos.close();
//             return true;
//         } catch (Exception e) {
//             e.printStackTrace();
//         }
//         return false;
//     }
//     @SuppressWarnings("unchecked")
// 	public static Student Read_from_file(String path) {
        
//         Student s=null;
// 		try {
//             FileInputStream fis = new FileInputStream(path);
//             ObjectInputStream ois = new ObjectInputStream(fis);
//             Object o = ois.readObject();
//             s = (Student) o;
//             ois.close();
//             fis.close();
//         } catch (Exception e) {
//             e.printStackTrace();
//         }
//         return s;
//     }
//    public static void Readstudentlist(Student list) {
// 	   if (list!=null) {
// 		   Readstudentlist(list.left);
// 		   System.out.printf("%-3d %-8d %-20s %-10.2f %-10s",++stt,list.getStudent_id(),list.getStudent_name(),list.getStudent_result(),list.getStudent_rank());
// 	    	System.out.println();
// 	    	Readstudentlist(list.right);
// 	   }
   
//     }
//    public static Student Addnode(Student ds,Student e) {
// 	   if (ds==null) return e;
// 	   else if (ds.getStudent_id()<e.getStudent_id()) ds.right=Addnode(ds.right,e);
// 	   else ds.left = Addnode(ds.left,e);
// 	   return ds;
//    }
//    public static int comp(Student o1,Student o2) {
// 	   if (o1.getStudent_id()==o2.getStudent_id()) return 0;
// 	   else return 1;
//    }
//    public static void AddStudent(Student list) {
// 	   int id;
// 	   String name;
// 	   double result;
// 	   System.out.println("Input Student Information:");
	   
// 	   System.out.println("Input id: ");id = scan.nextInt();
// 	   scan.nextLine();
// 	   System.out.println("Input name: ");name = scan.nextLine();
// 	   System.out.println("Input result: ");result = scan.nextDouble();
// 	   Student e = new Student(id,name);
// 	   e.setStudent_result(result);
// 	   if (result<5) e.setStudent_rank("Fail");
// 	   else e.setStudent_rank("PASS");
// 	   list = Addnode(list,e);
	   
//    }
//    public static void main(String[] args) {
// 		// TODO Auto-generated method stub
// 		Student list;
// 		list=Read_from_file("D:\\StudentList.dat");
		
		
		
// 		Student s1 = new Student(100,"Nguyen Van Dung");
// 		Student s2 = new Student(104,"Nguyen Thi Hanh");
// 		Student s3 = new Student(106,"Tran Thi Hai");
// 		Student s4 = new Student(109,"Le Van Phuoc");
// 		Student s5 = new Student(101,"Quach Thanh Danh");
// 		Student s6 = new Student(105,"Vu Van Hung");
// 		Student s7 = new Student(102,"Le Tien Loc");
// 		Student s8 = new Student(107,"Pham Quang Minh");
// 		Student s9 = new Student(108,"Ho Van Mui");
// 		Student s10 = new Student(103,"Nguyen Van Dat ");
// 		Student s11 = new Student(110,"Le Van Hai");
// 		list = s6;
// 		list = Addnode(list,s1);
// 		list = Addnode(list,s2);
// 		list = Addnode(list,s3);
// 		list = Addnode(list,s4);
// 		list = Addnode(list,s5);
// 		list = Addnode(list,s7);
// 		list = Addnode(list,s8);
// 		list = Addnode(list,s9);
// 		list = Addnode(list,s10);
// 		list = Addnode(list,s11);
		
// 		Readstudentlist(list);
		
// 		Save_to_file(list,"D:\\StudentList.dat");
		
// 		int menu=1;
		
// 		while (menu!=0) {
// 		System.out.println("STUDENT MANAGE PROGRAM");
// 		System.out.println("1-Open Student List from File");
// 		System.out.println("2-View Student List ");
// 		System.out.println("3-Add a Student to the List ");
// 		System.out.println("0-Save/Exit");
// 		System.out.println("Please choose: ");
// 		menu = scan.nextInt();
					
// 		switch (menu) {
// 		case 1: {list=Read_from_file("D:\\StudentList.dat");break;}
// 		case 2: {stt=0;System.out.println("READ LIST:"); Readstudentlist(list); break;}
// 		case 3: {AddStudent(list);break;}
// 		case 0: {Save_to_file(list,"D:\\StudentList.dat");break;}
// 		}
// 		}
		
// 		scan.close();
// 		}

// 	}




