tuan 1


1
PT HTTH – BmIT – 6/2018
Lab1:	JAVA	Basic
Contents
Bài tập cơ bản về sử dụng biến, lệnh IF/ELSE, lệnh SWITCH/CASE, vòng lặp FOR và WHILE trong Java:
 ................................................................................................................................................................ 2
Viết chương trình in ra màn hình “Hello, World!”. ........................................................................ 2
Viết chương trình nhập vào tên của bạn, sau đó in ra màn hình với nội dung “Hi, I am” cộng với
tên bạn vừa nhập. .......................................................................................................................... 2
Viết chương trình nhập vào 2 số A và B, sau đó in ra màn hình kết quả tính tổng. ....................... 2
Viết chương trình nhập vào một số, sau đó in ra màn hình số vừa nhập là số chẵn hay lẻ ........... 2
Viết chương trình nhập vào một tháng trong năm, sau đó bạn in ra màn hình tháng vừa nhập
bằng tiếng Anh ............................................................................................................................... 3
Yêu cầu viết một chương trình để có thể giúp quản lý các vật nuôi trong vườn thú. Hiện tại,
vườn thú có một số động vật như sư tử (lion), rắn (snake) và khỉ (monkey). Mỗi loài động vật
đều có các thuộc tính chung bao gồm tên động vật (name) và cân nặng (weight). Người chủ
vườn thú cần biết mỗi ngày sư tử ăn bao nhiêu thức ăn (eat), chiều dài của mỗi con rắn (length)
và thức ăn yêu thích của khỉ. Ví dụ như sau: .................................................................................. 4
Làm việc với File/Folder trong Java ........................................................................................................ 4
Delete file trong Java ...................................................................................................................... 4
Delete Folder .................................................................................................................................. 5
Tìm kiếm File .................................................................................................................................. 6
Copy File ......................................................................................................................................... 7
Ghi File nhị phân ............................................................................................................................. 7
Đọc File nhị phân ............................................................................................................................ 8
Đọc và ghi File ảnh .......................................................................................................................... 9

2
PT HTTH – BmIT – 6/2018
Bài	tập	cơ	bản	về	sử	dụng	biến,	lệnh	IF/ELSE,	lệnh	SWITCH/CASE,	vòng	lặp
FOR	và	WHILE	trong	Java:
Viết	chương	trình	in	ra	màn	hình	“Hello,	World!”.
public class ExampleJava {

    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }

}

Viết	chương	trình	nhập	vào	tên	của	bạn,	sau	đó	in	ra	màn	hình	với	nội	dung	“Hi,	I	am”
cộng	với	tên	bạn	vừa	nhập.
import java.util.Scanner;

public class ExampleJava {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("What's your name?");
        String str = scanner.nextLine();
        System.out.println("Hi, I am "+str);
    }
}

Viết	chương	trình	nhập	vào	2	số	A	và	B,	sau	đó	in	ra	màn	hình	kết	quả	tính	tổng.
import java.util.Scanner;

public class ExampleJava {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Vui lòng nhập số hạng thứ nhất: ");
        int soA = scanner.nextInt();
        System.out.print("Vui lòng nhập số hạng thứ hai: ");
        int soB = scanner.nextInt();
        int kq = soA + soB;
        System.out.println("Tính tổng [" + soA + " + " + soB + " = " + kq);
    }
}

Viết	chương	trình	nhập	vào	một	số,	sau	đó	in	ra	màn	hình	số	vừa	nhập	là	số	chẵn	hay	lẻ
import java.util.Scanner;

public class ExampleJava {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println(">> Kiểm tra số chẳn lẽ <<");
        System.out.print("Vui lòng nhập số cần kiểm tra: ");
        int so = scanner.nextInt();
        if (so % 2 == 0) {
3
PT HTTH – BmIT – 6/2018
            System.out.println("Số " + so + " là số chẵn.");
        } else {
            System.out.println("Số " + so + " là số lẽ.");
        }
    }

}

Viết	chương	trình	nhập	vào	một	tháng	trong	năm,	sau	đó	bạn	in	ra	màn	hình	tháng	vừa
nhập	bằng	tiếng	Anh
import java.util.Scanner;

public class ExampleJava {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        boolean isrun = true;
        while (isrun) {
            System.out.print("Vui lòng nhập tháng: ");
            int so = scanner.nextInt();
            switch (so) {
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
4
PT HTTH – BmIT – 6/2018
                    break;
                default:
                    isrun = false;
                    scanner.close();
                    System.out.println("STOP");
                    break;
            }
        }
    }
}

Yêu	cầu	viết	một	chương	trình	để	có	thể	giúp	quản	lý	các	vật	nuôi	trong	vườn	thú.	Hiện
tại,	vườn	thú	có	một	số	động	vật	như	sư	tử	(lion),	rắn	(snake)	và	khỉ	(monkey).	Mỗi	loài
động	vật	đều	có	các	thuộc	tính	chung	bao	gồm	tên	động	vật	(name)	và	cân	nặng
(weight).	Người	chủ	vườn	thú	cần	biết	mỗi	ngày	sư	tử	ăn	bao	nhiêu	thức	ăn	(eat),	chiều
dài	của	mỗi	con	rắn	(length)	và	thức	ăn	yêu	thích	của	khỉ.	Ví	dụ	như	sau:	– Sư tử Leo nặng 300 cân và ăn 5 cân thịt mỗi ngày. – Con rắn Boa nặng 50 cân và dài 5 mét. – Con khỉ George nặng 150 cân và thích ăn chuối

Làm	việc	với	File/Folder	trong	Java
Delete	file	trong	Java
package delete;

import java.io.File;

public class DeleteFileIO {

 private void deleteFile(String source) {
  //new file
  File file = new File(source);
  //check file exist
  // neu ton tai
  if(file.exists()) {
   System.out.println("file ton tai");
   file.delete();
   System.out.print("xoa file thanh cong");
  }
  else {
   System.out.println("file khong ton tai");
  }
 }

 public static void main(String[] args) {
  DeleteFileIO deleteFileIO = new DeleteFileIO();
  deleteFileIO.deleteFile("D:/HocJava/demo.txt");
 }

5
PT HTTH – BmIT – 6/2018
}

Delete	Folder
TH1: Delete thư mục rỗng
public boolean deleteEmptyFolder(String source)
 {
  File folder = new File(source);
  //kiem tra neu folder ton tai thi xoa
  if(folder.exists())
  {
   folder.delete();
   System.out.println("folder ton tai\n xoa folder thanh cong");
   return true;
  }
  else
  {
   System.out.println("folder khong ton tai");
  }
  return false;
 }

TH2: Delete thư mục chứa Files
        public boolean deleteListFileInfolder(String source) {
        File folder = new File(source);
//        folder tồn tại
        if (folder.exists()) {
//            danh sách file
    File[] listFile = folder.listFiles();
            if (listFile.length != 0) {
                for (File f : listFile) {
//                file thì xóa
                    if (f.isFile()) {
                        f.delete();
                    }
                }
            }
            folder.delete();
          System.out.println("Delete folder thành công!");
            return true;
        } else {
            System.out.println("folder không tồn tại");
            return false;
        }
    }

TH3: Delete thư mục chứa danh sách thư mục con và trong thư mục con chứa danh sách file, các bạn
tham khảo ở hai trường hợp mình đã làm ở trên để giải quyết cho trường hợp thứ 3, có vấn đề gì thì
các bạn cứ command ờ bên dưới.
import java.io.File;
import java.io.IOException;

6
PT HTTH – BmIT – 6/2018
/**

* 
* @author IT
  */
  public class DeleteDirTH3 {

  public boolean deleteListFileInfolder(String source) throws IOException {
  File folder = new File(source);
  //        folder tá»“n táº¡i
  if (folder.exists()) {
  //            danh sÃ¡ch file
  File[] listFile = folder.listFiles();
  if (listFile.length != 0) {
  for (File f : listFile) {
  //                    náº¿u lÃ  file thÃ¬ delete
  if(f.isFile()){
  f.delete();
  }
  //                    new la thu muc thi goi de quy lai
  if(f.isDirectory()){
  deleteListFileInfolder(f.getAbsolutePath());
  }
  }
  }
  folder.delete();
  System.out.println("Delete folder thÃ nh cÃ´ng!");
  return true;
  } else {
  System.out.println("folder khÃ´ng tá»“n táº¡i");
  return false;
  }
  }

  public static void main(String[] args) throws IOException {
  DeleteDirTH3 deleteDirTH3 = new DeleteDirTH3();

  deleteDirTH3.deleteListFileInfolder("D:\\HocJava\\TestDeleteDir");
  }

}

Tìm	kiếm	File
ví dụ tìm file trong Java với phương thức finFile() nhận vào đường dẫn chỉ tới thư mục cần tìm kiếm
và từ khóa để tìm kiếm.
  public void finFile(String source, String key) {
        File file = new File(source);
        if (file.exists()) {
            if (file.isFile()) {
                if (file.getName().endsWith(key)) {
                    System.out.println(file.getAbsolutePath());
                }
            }
            File[] listFile = file.listFiles();
            if (listFile != null) {
7
PT HTTH – BmIT – 6/2018
                for (File f : listFile) {
                    finFile(f.getAbsolutePath(), key);
                }
            }
        } else {
            System.out.println("source không tồn tại");
        }
    }

Copy	File
Ví dụ sau đây minh họa copy file  a.txt sang một file khác b.txt
    public boolean copyFile(String source, String dest) throws FileNotFoundException, IOException {
//        file nguồn
        File sourceFile = new File(source);
//        file đích
        File destFile = new File(dest);
//        kiem tra file nguồn có tồn tại không
        if (sourceFile.exists()) {
//           luồng đọc file
          FileInputStream fis = new FileInputStream(sourceFile);
//           luồng ghi file
            FileOutputStream fos = new FileOutputStream(destFile);
            byte[] arr = new byte[1024];
            while ((fis.read(arr)) != -1) {
                fos.write(arr);
                fos.flush();
            }
            fis.close();
            fos.close();
            System.out.println("copy thành công");
            return true;
        } else {
            System.out.println("file nguồn không tồn tại");
            return false;
        }
    }

Ghi	File	nhị	phân
Bây giờ mình có một danh sách sinh viên với sinh viên có những thuộc tính là mssv, tên, tuổi, và
danh sách môn học, môn học có những thuộc tính như là tên môn học, tín chỉ, điểm. Làm sao để lưu
danh sách sinh viên xuống file nhị phân?
Giải quyết vấn đề ghi file nhị phân trong Java:
Với vấn đề đặt ra thì mình xác định sẽ có một class SinhVien, class MonHoc và một class xử lý để lưu
danh sách sinh viên xuống file nhị phân, mình gọi class này là WriteBinaryFile.
Class SinhVien với các thuộc tính như mã số sinh viên, tên, tuổi và danh sách môn học.
8
PT HTTH – BmIT – 6/2018
Class MonHoc với các thuộc tính như tên môn học, số tín chỉ và điểm.
Class WriteBinaryFile:
public class WriteBinaryFile {

    public static void saveSV(String src, ArrayList listSV)
            throws IOException {
        DataOutputStream dos = new DataOutputStream(new FileOutputStream(
                new File(src)));
        dos.writeInt(listSV.size());
        for (SinhVien sv : listSV) {
            dos.writeUTF(sv.getMssv());
            dos.writeUTF(sv.getTen());
            dos.writeInt(sv.getTuoi());
            dos.writeInt(sv.getListMH().size());
            for (MonHoc mh : sv.getListMH()) {
                dos.writeUTF(mh.getTenMonHoc());
                dos.writeInt(mh.getTinChi());
                dos.writeDouble(mh.getDiem());
            }
        }
        dos.flush();
        dos.close();
    }

    public static void main(String[] args) throws IOException {
        MonHoc mh = new MonHoc("ltcb", 3, 6.7);
        MonHoc mh1 = new MonHoc("ltw", 3, 6.7);
        MonHoc mh2 = new MonHoc("tkhdt", 3, 6.7);
        ArrayList listMH = new ArrayList<>();
        listMH.add(mh2);
        listMH.add(mh1);
        listMH.add(mh);
        ArrayList listSV = new ArrayList<>();
        SinhVien sv = new SinhVien("11329078", "nguyen van A", 23, listMH);
        SinhVien sv1 = new SinhVien("11329078", "nguyen Van B", 23, listMH);
        listSV.add(sv);
        listSV.add(sv1);
        saveSV("E:\\a.txt", listSV);
    }
}

Đọc	File	nhị	phân
Để đọc file nhị phân mình cần biết những gì?
Giải quyết vấn đề đọc file nhị phân trong Java:
9
PT HTTH – BmIT – 6/2018
Giải quyết vấn đề này rất đơn giản bạn chỉ cần biết ở bài trước mình dùng stream nào ghi thì chỉ cần
dùng stream tương ứng mà đọc ra. Sau đây là phương thức load sinh viên từ file nhị phân và stream
được dùng ở đây là DataInputStream. Sau đây là đoạn code mô tả chi tiết cách đọc file nhị phân
public static void loadSV(String src) throws IOException {
        DataInputStream dis = new DataInputStream(new FileInputStream(new File(
                src)));
        int size = dis.readInt();
        ArrayList listSV = new ArrayList();
        for (int i = 0; i < size; i++) {
            String mssv = dis.readUTF();
            String name = dis.readUTF();
            int age = dis.readInt();
            int sizemh = dis.readInt();
            ArrayList listMH = new ArrayList();
            for (int j = 0; j < sizemh; j++) {
                String tenMonHoc = dis.readUTF();
                int tinChi = dis.readInt();
                double diem = dis.readDouble();
                MonHoc mh1 = new MonHoc(tenMonHoc, tinChi, diem);
                listMH.add(mh1);
            }
            listSV.add(new SinhVien(mssv, name, age, listMH));
        }
        for(SinhVien sv : listSV){
            System.out.println(sv.toString());
        }
        dis.close();
    }

    public static void main(String[] args) throws IOException {
        loadSV("E:\\a.txt");
    }

Đọc	và	ghi	File	ảnh
Ghi file ảnh
package gui;

import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.File;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.imageio.ImageIO;

public class Class_Images {

    public static void saveFile(File path, String tfile, byte[] bfile) {
10
PT HTTH – BmIT – 6/2018
        try {
            BufferedImage img = ImageIO.read(new ByteArrayInputStream(bfile));
            ImageIO.write(img, tfile, path);
        } catch (IOException ex) {
            Logger.getLogger(Class_Images.class.getName()).log(Level.SEVERE, null, ex);
        }
    }

}

Đọc file ảnh
package gui;

import java.awt.image.BufferedImage;
import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.imageio.ImageIO;

public class Class_Images {

    public static byte[] readFile(File path) {
        try {
            FileInputStream fis = new FileInputStream(path);
            byte[] buf = new byte[1024];
            ByteArrayOutputStream bos = new ByteArrayOutputStream();
            for (int readNum; (readNum = fis.read(buf)) != -1;) {
                bos.write(buf, 0, readNum);
    }
            return bos.toByteArray();
        } catch (IOException ex) {
            Logger.getLogger(Class_Images.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }

}

tuan 2 



OOP trong Java

VD (Tính Kế thừa và Đa hình): Xây dựng chương trình quản lý DongVat gồm các lớp sau:
Lớp cha DongVat
Thuộc tính Phương thức
loai (String) inThongTin()
ten (String) an()
tuoi(String) ngu()
taoAmThanh()

Lớp con Meo kế thừa
Thuộc tính Phương thức
leoTuong()

Lớp con Cho
Thuộc tính Phương thức
chay()

GỢI Ý:

PtHtTh©IT-FIT (v.2026)

ttmk©2

Bài 1: Xây dựng chương trình quản lý Nhân viên gồm các lớp sau:
Lớp cha NhanVien
Thuộc tính Phương thức
maNV (String) nhapThongTin()
hoTen (String hienThiThongTin()
Lớp con NhanVienVanPhong kế thừa NhanVien
Thuộc tính Phương thức
luongCoBan (double) tinhLuong()
Lớp con NhanVienSanXuat kế thừa NhanVien
Thuộc tính Phương thức
soSanPham (int) tinhLuong()
donGia (double)
YÊU CẦU
• Mỗi lớp con kế thừa lại thuộc tính chung từ NhanVien

PtHtTh©IT-FIT (v.2026)

ttmk©3

• Không sử dụng đa hình (chỉ tập trung kế thừa)
• Viết chương trình main để tạo và hiển thị thông tin từng loại nhân viên

Bài 2: Xây dựng chương trình quản lý Phương tiện giao thông gồm các lớp sau:
Lớp cha PhuongTien
Thuộc tính Phương thức
hangSanXuat hienThiThongTin()
namSanXuat
giaBan
Lớp con XeMay kế thừa PhuongTien
Thuộc tính Phương thức
dungTichXiLanh tinhThue()
Lớp con Oto kế thừa PhuongTien
Thuộc tính Phương thức
soChoNgoi tinhThue()
YÊU CẦU
• Lớp con kế thừa đầy đủ thuộc tính của lớp cha
• Mỗi loại phương tiện có cách tính thuế khác nhau
• Viết main tạo mỗi loại phương tiện và hiển thị thông tin


tuan 3 


Lab2: JAVA Stream

v Stream là dòng chảy liên tục, có thứ tự của các bytes dữ liệu chảy giữa chương trình và
thiết bị ngoại vi
v Dùng stream có thể kết nối nhiều thiết bị ngoại vi với chương trình
v java.io.InputStream: stream nhập
o int read() throws IOException
o int read(byte b[]) throws IOException
o int read(byte b[], int offset, int len)

v java.io.OutputStream: stream xuất

o void write(int b) throws IOException
o void write(byte[] b) throws IOException
o void write(byte[] b, int offset, int len)

v java.io.InputStreamReader: chuyển InputStream dạng byte sang InputStream dạng ký tự
v java.io.BufferedReader: hỗ trợ việc đọc văn bản từ một InputStream dạng ký tự
o String readLine() throws IOException: dọc dòng văn bản kế tiếp trong
InputStream

v java.io.PrintWriter: gởi chuỗi ra một OutputStream

Hoàn chỉnh các ví dụ sau:
Ex1:
public class InStream1 {
public static void main(String args[]) {
InputStream is = System.in;//keyboard = system.in
while(true) {
try {
int ch = is.read();
if(ch == -1 || ch == 'q') break;
System.out.println((char)ch);
}catch (IOException ie) {
System.out.println("Error: "+ie);
}

}
}
}

Ex2:
public class InStream2 {
public static void main(String[] args) {
InputStream is = System.in;

2

PT HTTH – BmIT – 8/2019
while(true) {
try {
int num = is.available();
if(num > 0) {
byte[] b = new byte[num];
int result = is.read(b);
if(result == -1) break;
String s = new String(b);
System.out.print(s);
}else {
System.out.println('.');
}
}catch(IOException ie) {
System.out.println("Error: "+ie);
}
}
}
}

Ex3:
public class ReadLine {
public static void main(String[] args) {
InputStreamReader isr = new InputStreamReader(System.in);
BufferedReader br = new BufferedReader(isr);
while(true) {
try {
String line = br.readLine();
if(line != null)
System.out.println(line);

}catch(IOException ie) {
System.out.println("Error: "+ie);
}
}
}
}

Ex4:
public class PrintString {
public static void main(String[] args) {
OutputStream os = System.out;
PrintWriter pw = new PrintWriter(os);
pw.write("this is a string \r\n");
pw.println("this is a line");
pw.write("Bye!Bye!");
pw.flush();

3

PT HTTH – BmIT – 8/2019
}
}

Bài tập Stream: sử dụng InputStream để nhập dữ liệu cho các bài tập Tuần 1, 2


tuan 4 


Bài 1. Cài đặt các chương trình đã được giới thiệu trong buổi học lý thuyết (2 ví dụ)
Bài 2. Viết chương trình tạo ra một đối tượng FileTWrite kế thừa đối đối tượng Thread(hoặc cài đặt giao
diện Runable), cho phép viết một dãy số ngẫu nhiên vào tập tin. Đối tượng FileTWriter có thuộc tính
tên tập tin cần viết. Viết hàm main tạo ra 3 đối tượngviết 3 tập tin chạy ở 3 tiến trình đồng thời riêng
biệt.
Bài 3. Viết chương trình tạo ra một đối tượng FileTReader kế thừa đối đối tượng Thread (hoặc cài đặt
Runable), cho phép đọc nội dung một tập tin và hiển thị lên màn hình. Đốitượng FileReader có thuộc
tính tên tập tin cần mở. Viết hàm main tạo ra 3 đối tượng đọc 3 tập tin chạy ở 3 tiến trình đồng thời
riêng biệt
Bài 4. Viết chương trình tạo ra đối tượng đọc tập tin, viết tập tin chạy ở từng tiến trìnhriêng (có xử lý đồng
bộ hóa dư liệu). Viết hàm main tạo ra đối tượng viết và đọc dữ liệuvới tập tin giống nhau. Kiểm tra
việc đồng bộ hóa dữ liệu
Bài 5. Viết chương trình mô phỏng bài toán "Người sản xuất - Người tiêu dùng", trong đó Người sản xuất sẽ
sản xuất ra một số lượng ngẫu nhiên n sản phẩm nào đó rồi yêu cầu nhập kho. Người tiêu dùng sẽ
yêu cầu xuất kho một số lượng ngẫu nhiên m sản phẩm nào đó từ kho. Yêu cầu nhập kho chỉ được
chấp nhận nếu số lượng hàng hóa đưa vào không vượt quá sức chứa của kho, nếu không, phải chờ
cho đến khi có đủ chổ trống trong kho. Yêu cầu xuất kho chỉ được chấp nhận khi còn đủ hàng trong
kho nếu không cũng phải chờ
Gợi ý : Thiết kế các lớp sau:

- Lớp Kho: Có thuộc tính là sức chứa, phương thức khởi tạo gán giá trị cho sức chứa, các phương
  thức xem số lượng hàng tồn, phương thức nhập kho, phương thức xuất kho. In thông báo mỗi khi
  nhập kho hay xuất kho thành công
- Lớp Người Sản Xuất là một Thread: Có thuộc tính là kho để nhập hàng. Phương thức khởi tạo gán
  giá trị cho kho nhập hàng. Phương thức sản xuất lặp lại công việc là tạo ra n sản phẩm ngẫu nhiên
  và chờ để nhập vào kho.
- Lớp Người Tiêu Dùng là một Thread: Có thuộc tính là kho để xuất hàng. Phương thức khởi tạo gán
  giá trị cho kho để xuất hàng. Phương thức tiêu dùng lặp lại công việc là chờ để yêu cầu xuất m sản
  phẩm từ kho.
- Lớp Demo tạo ra một kho và 2 người sản xuất, 2 người tiêu dùng thực hiện việc nhập xuất trên cùng
  một kho

tuần 5 



UDP

BÀI TẬP THỰC HÀNH
Bài 1:
Viết chương trình theo mô hình Client-Server sử dụng dụng Socket ở chế độ có nối kết. Trong đó :

+ Server làm nhiệm vụ đọc một ký tự số từ '0' đến '9'.
  ( Ví dụ : nhận số 0 : trả về "không" , 1 : trả về "một" ; ... ... 9 : trả về "chín", nếu nhận ký tự khác số thì
  trả về "Không phải số nguyên" ).
+ Client sẽ nhập vào 1 ký tự, gửi qua Server, nhận kết quả trả về từ Server và thể hiện lên màn hình
  InputStream/OutStream
  DataInputStream/ DataOutputStream
  Bài 2: (gởi nhiều tn cùng lúc + nhiều client)
  Viết ứng dụng Chat đơn giản sử dụng Socket TCP.
  Yêu cầu:
  Xây dựng Server có thể lắng nghe kết nối từ Client.
  Client sau khi kết nối thành công với Server có thể gởi tin nhắn (text) qua lại với Server
  Bài 3:
  Cải tiến bài trên với yêu cầu: Server và Client được cài đặt trên 2 máy khác nhau. Client sẽ xác định địa
  chỉ IP và Port dựa theo tham số truyền vào (args)
  Bài 4:
  Viết chương trình date/time client/server TCP theo mô tả sau

- Chương trình server cung cấp các chức năng sau: Date (xem ngày hệ thống), Time (xem giờ hệ
  thống), Date&Time (xem ngày giờ hệ thống). Các chức năng này có thể chọn qua một menu.
- Client:

1. Kết nối đến server: client nhập địa chỉ server cung cấp dịch vụ và port trước khi kết nối
2. Nếu kết nối được thì nhập yêu cầu cần phục vụ:
3. Time
4. Date
5. Date & Time
6. Client nhận trả lời của server và in ra màn hình

- Server:

1. Chờ kết nối từ client tại IP/port đã đăng ký
2. Cung cấp menu dịch vụ
3. Xử lý yêu cầu và trả kết quả cho client
4. (*) Cho phép nhiều client kết nối.
   Bài 5:
   Viết chương trình date/time client/server UDP

- Chương trình client cung cấp các chức năng sau:

1. Nhập địa chỉ server cung cấp dịch vụ và port
2. Nhập yêu cầu cần phục vụ từ bàn phím và gửi đến server đã nhập:
3. Time
4. Date
5. Date & Time

- Nhận trả lời của server và in ra màn hình
  Bài 6:
  Viết chương trình mô phỏng mô hình tính toán ở server(TCP):
- Server cung cấp các hàm tính toán, client gửi yêu cầu tính toán, sau đó gửi tham số (giá trị của n)
  đến server để nhận kết quả trả về.
- Các yêu cầu tính toán gửi từ client như sau:

1. Tổng 1+3+5+7+...+(2n+1)
2. Tổng 1*2 + 2*3+...+n*(n+1)
3. Biểu thức 1-2+3-4+..+(2n+1)
   Tương tự câu trên nhưng sử dụng giao thức UDP
   Bài 7:
   Viết chương trình gửi file (TCP)
   Client :
4. Kết nối đến server có địa chỉ do người sử dụng nhập vào,
5. Người sử dụng nhập tên file cần truyền đến server
6. Người sử dụng nhập đường dẫn trên server để chứa file
7. Truyền file đến server
   Tương tự câu trên, viết chương trình gửi file (UDP)
   Bài 8:
   Viết chương trình theo mô hình Client-Server sử dụng Socket ở chế độ có kết nối. Trong đó:

- Server sẽ nhận các yêu cầu là chuỗi có khuôn dạng sau:
  “OP Operant1 Operant2\n”

Trong đó:
o OP là một ký tự chỉ phép toán muốn thực hiện: ‘+’, ‘-‘, ‘*’, ‘/’
o Operant1, Operant2 là đối số của phép toán
o Các thành phần trên cách nhau bởi 1 ký tự trắng ‘ ‘.
o Kết thúc yêu cầu bằng ký tự xuống dòng ‘\n’
Mỗi khi server nhận được một thông điệp nó sẽ thực hiện phép toán Operant1 OP Operant2
để cho ra kết quả, sau đó đổi kết quả thành chuỗi và gởi về client

- Client cho phép người dùng nhập các phép toán muốn tính theo cách thức thông thường. Ví
  dụ: 100+200. Client tạo ra thông điệp yêu cầu theo đúng dạng do Server qui định, mô tả về
  phép toán muốn Server thực thi, rồi gởi sang Server, chờ nhận kết quả trả về và in ra màn
  hình.

Bài 9:
Viết chương trình Client-Server theo mô tả sau:
Server:

- Lưu trữ tập tin data.txt (đề cho)
- Cho phép nhiều client có thể truy cập và đọc nội dung tập tin.
  Client
- Kết nối đến server,
- Nhập tên file cần đọc nội dung.
- Hiển thị ra màn hình nội dung file do server trả về
  Bài 10:
  Viết chương trình Client-Server theo mô tả sau:
  Server:
- Server có chức năng lưu tin nhắn của các client vào các tập tin riêng biệt (vd client1.txt,
  client2.txt,...)
- Thông báo bằng tin nhắn đến client khi việc lưu trữ thành công.
- Server cho phép nhiều client có thể truy cập và gởi tin nhắn cho mình.
  Client:
- Client kết nối đến server
- Nhập các tin nhắn gởi đến server.
- Kết thúc tin nhắn bằng chuỗi "HET"
  deb http://http.kali.org/kali kali-rolling main non-free contrib
  deb http://http.kali.org/kali kali-last-snapshot main non-free contrib
  deb http://http.kali.org/kali kali-experimental main non-free contrib
  deb-src http://http.kali.org/kali kali-rolling main non-free contrib

 (socket) Sinh viên thực hiện các ví dụ sau:

TCP


tuần 6 


--url--

1. Viết chương trình Java nhận vào một tên miền (domain) từ tham số dòng lệnh và hiển thị: hostname, địa chỉ IP

(Vd: java DomainInfo.java google.com)

2. Viết chương trình Java kiểm tra một hostname có tồn tại hay không? Nếu tồn tại thì hãy liệt kê tất cả địa chỉ IP của hostname đó.

--Threads--

3. Viết chương trình tạo vùng nhớ đệm lưu trữ số nguyên

-Thread 1: nhập số từ bàn phím đưa vào buffer.

-Thread 2: lấy số từ buffer và tính tổng các số.

-Chương trình dừng khi nhập số **-1**

--Socket TCP--

4. Xây dựng ứng dụng TCP Client-Server:

Server lắng nghe tại cổng 6789. Nhận một số nguyên n từ client. Trả về giai thừa của n

Client nhận n từ bàn phím. Gửi tới server. Nhận kết quả

5. Sử dụng TCP Socket xây dựng ứng dụng

Server lắng nghe tại cổng 6789. Nhận một chuỗi từ client. Trả về chuỗi viết hoa, số ký tự trong chuỗi

Client nhập chuỗi từ bàn phím. Gửi tới server. Hiển thị kết quả nhận được
