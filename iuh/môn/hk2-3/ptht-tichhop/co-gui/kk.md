PtHtTh©IT-FIT (v.2026)
OOP trong Java
VD (Tính Kế thừa và Đa hình): Xây dựng chương trình quản lý DongVat gồm các lớp sau:
Lớp cha DongVat
Thuộc tính
Phương thức
loai (String)
ten (String)
inThongTin()
an()
tuoi(String)
ngu()
taoAmThanh()
Lớp con Meo kế thừa
Thuộc tính
Phương thức
leoTuong()
Lớp con Cho
Thuộc tính
chay()
GỢI Ý:
Phương thức
ttmk©1
PtHtTh©IT-FIT (v.2026)
Bài 1: Xây dựng chương trình quản lý Nhân viên gồm các lớp sau:
Lớp cha NhanVien
Thuộc tính
Thuộc tính
maNV (String)
Phương thức
nhapThongTin()
hoTen (String
hienThiThongTin()
Lớp con NhanVienVanPhong kế thừa NhanVien
luongCoBan (double)
Phương thức
tinhLuong()
Lớp con NhanVienSanXuat kế thừa NhanVien
Thuộc tính
soSanPham (int)
Phương thức
tinhLuong()
donGia (double)
YÊU CẦU
ttmk©2
• Mỗi lớp con kế thừa lại thuộc tính chung từ NhanVien
PtHtTh©IT-FIT (v.2026)
• Không sử dụng đa hình (chỉ tập trung kế thừa)
• Viết chương trình main để tạo và hiển thị thông tin từng loại nhân viên
Bài 2: Xây dựng chương trình quản lý Phương tiện giao thông gồm các lớp sau:
Lớp cha PhuongTien
Thuộc tính
hangSanXuat
Phương thức
hienThiThongTin()
namSanXuat
giaBan
Lớp con XeMay kế thừa PhuongTien
Thuộc tính
dungTichXiLanh
Phương thức
tinhThue()
Lớp con Oto kế thừa PhuongTien
Thuộc tính
soChoNgoi
YÊU CẦU
• Lớp con kế thừa đầy đủ thuộc tính của lớp cha
• Mỗi loại phương tiện có cách tính thuế khác nhau
Phương thức
tinhThue()
• Viết main tạo mỗi loại phương tiện và hiển thị thông tin
ttmk©3


Lab2:	JAVA	Stream
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
PT HTTH – BmIT – 8/2019
1
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
}
}
Bài tập Stream: sử dụng InputStream để nhập dữ liệu cho các bài tập Tuần 1, 2
PT HTTH – BmIT – 8/2019
3


TUẦN 4 (socket)
Sinh viên thực hiện các ví dụ sau:
TCP

UDP

BÀI TẬP THỰC HÀNH
Bài 1:Viết chương trình theo mô hình Client-Server sử dụng dụng Socket ở chế độ có nối kết. Trong đó :

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
  Viết chương trình date/time client/server TCP theo mô tả sau -
  Chương trình server cung cấp các chức năng sau: Date (xem ngày hệ thống), Time (xem giờ hệ
  thống), Date&Time (xem ngày giờ hệ thống). Các chức năng này có thể chọn qua một menu. -
  Client:

1. Kết nối đến server: client nhập địa chỉ server cung cấp dịch vụ và port trước khi kết nối
2. Nếu kết nối được thì nhập yêu cầu cần phục vụ:
3. Time
4. Date
5. Date & Time -
6. Client nhận trả lời của server và in ra màn hình
   Server:
7. Chờ kết nối từ client tại IP/port đã đăng ký
8. Cung cấp menu dịch vụ
9. Xử lý yêu cầu và trả kết quả cho client
10. (*) Cho phép nhiều client kết nối.
    Bài 5:Viết chương trình date/time client/server UDP  -
    Chương trình client cung cấp các chức năng sau:
11. Nhập địa chỉ server cung cấp dịch vụ và port
12. Nhập yêu cầu cần phục vụ từ bàn phím và gửi đến server đã nhập:
13. Time
14. Date -
15. Date & TimeNhận trả lời của server và in ra màn hình
    Bài 6:
    Viết chương trình mô phỏng mô hình tính toán ở server(TCP): -
    Server cung cấp các hàm tính toán, client gửi yêu cầu tính toán, sau đó gửi tham số (giá trị của n)
    đến server để nhận kết quả trả về. -
    Các yêu cầu tính toán gửi từ client như sau:
16. Tổng 1+3+5+7+...+(2n+1)
17. Tổng 1*2 + 2*3+...+n*(n+1)
18. Biểu thức 1-2+3-4+..+(2n+1)Tương tự câu trên nhưng sử dụng giao thức UDP
    Bài 7:
    Viết chương trình gửi file (TCP)Client :
19. Kết nối đến server có địa chỉ do người sử dụng nhập vào,
20. Người sử dụng nhập tên file cần truyền đến server
21. Người sử dụng nhập đường dẫn trên server để chứa file
22. Truyền file đến server
    Tương tự câu trên, viết chương trình gửi file (UDP)
    Bài 8:
    Viết chương trình theo mô hình Client-Server sử dụng Socket ở chế độ có kết nối. Trong đó: -
    Server sẽ nhận các yêu cầu là chuỗi có khuôn dạng sau:
    “OP Operant1 Operant2\n”
    Trong đó:
    o OP là một ký tự chỉ phép toán muốn thực hiện: ‘+’, ‘-‘, ‘*’, ‘/’
    o Operant1, Operant2 là đối số của phép toán
    o Các thành phần trên cách nhau bởi 1 ký tự trắng ‘ ‘.
    o Kết thúc yêu cầu bằng ký tự xuống dòng ‘\n’
    Mỗi khi server nhận được một thông điệp nó sẽ thực hiện phép toán Operant1 OP Operant2
    để cho ra kết quả, sau đó đổi kết quả thành chuỗi và gởi về client -
    Bài 9:
    Client cho phép người dùng nhập các phép toán muốn tính theo cách thức thông thường. Ví
    dụ: 100+200. Client tạo ra thông điệp yêu cầu theo đúng dạng do Server qui định, mô tả về
    phép toán muốn Server thực thi, rồi gởi sang Server, chờ nhận kết quả trả về và in ra màn
    hình.
    Viết chương trình Client-Server theo mô tả sau:
    Server:  -
    Lưu trữ tập tin data.txt (đề cho) -
    Client  - - -
    Bài 10:
    Cho phép nhiều client có thể truy cập và đọc nội dung tập tin.
    Kết nối đến server,
    Nhập tên file cần đọc nội dung.
    Hiển thị ra màn hình nội dung file do server trả về
    Viết chương trình Client-Server theo mô tả sau:
    Server: -
    Server có chức năng lưu tin nhắn của các client vào các tập tin riêng biệt (vd client1.txt,
    client2.txt,…) - -
    Client: - - -
    Thông báo bằng tin nhắn đến client khi việc lưu trữ thành công.
    Server cho phép nhiều client có thể truy cập và gởi tin nhắn cho mình.
    Client kết nối đến server
    Nhập các tin nhắn gởi đến server.
    Kết thúc tin nhắn bằng chuỗi "HET"
    deb http://http.kali.org/kali kali-rolling main non-free contrib
    deb http://http.kali.org/kali kali-last-snapshot main non-free contrib
    deb http://http.kali.org/kali kali-experimental main non-free contrib
    deb-src http://http.kali.org/kali kali-rolling main non-free contrib
    THỰC HÀNH LAB 06 – RMI
    Bài 1. Máy chủ RMI trả về chuỗi "Hello, World!"
    Mô tả. Viết một ứng dụng RMI trong đó client gọi phương thức từ server để nhận về chuỗi "Hello, World!".
    Yêu cầu
    Tạo interface chứa phương thức sayHello().
    Triển khai phương thức này ở server.
    Client gọi phương thức từ xa.
    Bài 2.  Bài tập Tính Tổng Hai Số
    Mô tả. Viết ứng dụng RMI cho phép client gửi hai số nguyên a và b đến server, sau đó server trả về tổng a + b.
    Yêu cầu
    Interface chứa phương thức int add(int a, int b).
    Server triển khai phương thức này.
    Client nhập hai số từ bàn phím và gửi đến server để nhận kết quả.
    Bài 3.  Bài tập Kiểm Tra Số Nguyên Tố
    Mô tả. Viết chương trình RMI giúp client kiểm tra xem một số có phải là số nguyên tố hay không.
    Yêu cầu
    Interface chứa phương thức boolean isPrime(int n).
    Server kiểm tra số nguyên tố và trả kết quả.
    Client nhập số và nhận kết quả từ server.
    Bài 4.  Bài tập Quản Lý Danh Bạ
    Mô tả. Xây dựng một hệ thống quản lý danh bạ từ xa bằng RMI. Client có thể thêm, sửa, xóa và tìm kiếm liên
    hệ trong danh bạ lưu trên server.
    Yêu cầu
    Interface có các phương thức:
    void addContact(String name, String phone)
    String findContact(String name)
    boolean deleteContact(String name)
    Server lưu trữ danh bạ bằng HashMap.
    Client nhập dữ liệu và gửiYêu cầu.
    Bài 5. Bài tập Chat Đơn Giản với RMI
    Mô tả. Tạo ứng dụng chat 1-1 giữa client và server thông qua RMI.
    Yêu cầu
    Interface có phương thức void sendMessage(String message).
    Server nhận tin nhắn từ client và phản hồi.
    Client nhập tin nhắn và hiển thị phản hồi.
    Bài 6.  Bài tập Quản Lý Tài Khoản Ngân Hàng
    Mô tả. Xây dựng ứng dụng ngân hàng từ xa, cho phép client kiểm tra số dư, gửi tiền và rút tiền.
    Yêu cầu
    Interface có các phương thức:
    double getBalance()
    void deposit(double amount)
    boolean withdraw(double amount)
    Server quản lý tài khoản với số dư ban đầu.
    Client có thể gửi/rút tiền và kiểm tra số dư.
    Bài 7.  Bài tập Tính Diện Tích Hình Học
    Mô tả. Viết chương trình RMI giúp client tính diện tích hình chữ nhật, hình tròn, hình tam giác.
    Yêu cầu
    Interface có phương thức:
    double rectangleArea(double width, double height)
    double circleArea(double radius)
    double triangleArea(double base, double height)
    Server thực hiện các phép tính.
    Client gửi thông số và nhận diện tích từ server.
    Bài 8.  Bài tập Hệ Thống Đặt Vé Máy Bay
    Mô tả. Viết ứng dụng RMI quản lý đặt chỗ vé máy bay từ xa.
    Yêu cầu
    Interface có các phương thức:
    boolean bookTicket(String flightNumber, int seats)
    int availableSeats(String flightNumber)
    boolean cancelBooking(String flightNumber, int seats)
    Server quản lý danh sách các chuyến bay.
    Client có thể đặt, hủy vé và kiểm tra số ghế trống.
    Bài 9. Hệ thống Đấu giá trực tuyến (Online Auction System)
    Mô tả:
    • Xây dựng hệ thống đấu giá trực tuyến bằng Java RMI.
    • Người dùng có thể đăng ký sản phẩm đấu giá và đưa ra giá thầu (bid).
    • Server quản lý danh sách sản phẩm và giá thầu, cập nhật giá cao nhất theo thời gian thực.
    Yêu cầu chức năng:
    1
    ️. Chủ sở hữu (Seller):
    • Thêm sản phẩm vào hệ thống đấu giá (tên sản phẩm, giá khởi điểm).
    2
    ️. Người đấu giá (Bidder):
    • Xem danh sách sản phẩm đang đấu giá.
    • Đưa ra giá thầu cao hơn giá hiện tại.
    3
    ️. Server (Auction Server):
    • Quản lý danh sách sản phẩm & giá thầu.
    • Cập nhật giá cao nhất cho từng sản phẩm.
    • Thông báo khi có người đặt giá thầu cao hơn.



JDBC	(JAVA	DATABASE	CONNECTION)
HƯỚNG DẪN THỰC HÀNH
B1. Chuẩn bị môi trường và thiết lập kết nối - Tạo dự án Java mới và thêm thư viện (driver) JDBC cho SQLite (sqlite-jdbc)
Class.forName(“org.sqlite.JDBC”);
String url = “jdbc:sqlite:nhanvien.db”;
Connection conn = DriverManager.getConnection(url, username,
passwd);
B2. Tạo đối tượng Statement từ Connection
Statement stmt = conn.createStatement();
B3. Thực thi các câu truy vấn từ các Statement đã tạo (hoặc tạo mới)
3.1. Tạo bảng - Viết câu lệnh SQL để tạo một bảng mới tên NhanVien với
các cột sau
id(INTEGER, PRIMARY KEY)
ten(TEXT, NOT NULL)
chuc_vu(TEXT)
String sql_create_table = “...” - Thực thi câu lệnh tạo bảng:
stmt.executeUpdate(sql_create_table);
3.2. Thêm dữ liệu - Viết ít nhất 3 câu lệnh sql INSERT INTO để thêm thông
tin của 3 nhân viên vào bảng NhanVien. - Thực
thi
các
câu
lệnh
INSERT
bằng
stmt.executeUpdate(slq_insert);
B4. Truy vấn và hiển thị dữ liệu - Viết câu lệnh sql SELECT để lấy tất cả nhân viên (id, ten,
chucvu) từ bảng NhanVien - Thực
thi
truy
vấn
bằng
ResultSet
rs
stmt.executeQuery(sql_select); - Duyệt qua ResultSet: - Sử dụng vòng lặp while(rs.next()); - Lấy dữ liệu từng cột bằng các phương thức: rs.getInt(“id”) và
rs.getString(“ten”) - In thông tin của từng nhân viên ra màn hình console
B5. Đóng kết nối và giải phóng tài nguyên - Đóng các tài nguyên (theo thứ tự ngược lại)
rs.close();
stmt.close();
conn.close();
*XỬ LÝ NGOẠI LỆ - Bọc toàn bộ khối code JDBC trong một khối try
catch(SQLException) để bắt và in ra các lỗi kết nối sql
tiềm ẩn - Sử dụng khối finally để đảm bảo rằng các kết nối
(Connection, Statement, ResultSet) luôn được đóng ngay cả
khi xảy ra lỗi. - Sử dụng giao dịch (Transactions): - Thực hiện nhiều câu lệnh INSERT hoặc UPDATE trong một
giao dịch duy nhất. - Tắt chế độ auto-commit: conn.setAutoCommit(false);
==============================================================================

- Chỉ gọi conn.commit() khi tất cả các thao tác đều
  thành công, nếu không thì gọi conn.rollback() trong
  khối catch() để hủy bỏ tất cả các thay đổi.
  BÀI TẬP GỢI Ý THỰC HÀNH

1. Quản lý Danh mục sản phẩm - Mở rộng bài tập NhanVien thành một hệ thống quản lý hoàn chỉnh
   cho bảng SanPham (maSP, tenSP, gia, soluong) - Thực hành các thao tác: - Create (Thêm mới): Thêm ít nhất 3 sản phẩm. - Read (Truy vấn): Liệt kê tất cả sản phẩm hoặc Tìm kiếm
   sản phẩm theo tenSP. - Update (Cập nhật): Thay đổi giá hoặc số lượng của một
   sản phẩm theo maSP. - Delete (Xóa): Xóa một sản phẩm (theo maSP).
2. Sử dụng giao dịch (Transaction) trong cập nhật dữ liệu
3. Xử lý ngoại lệ (Exception Handling) triệt để - Thực hiện lại Bài tập 1 và áp dụng khối try-catch-finally một
   cách nghiêm ngặt. - Đảm bảo rằng mọi tài nguyên JDBC (Connection, Statement,
   ResultSet) luôn được đóng trong khối finally để tránh rò rỉ
   tài nguyên (resource leakage), kể cả khi có lỗi SQLException
   xảy ra.
4. Sử dụng PreparedStatement để tăng cường bảo mật và hiệu năng
5. Truy vấn dữ liệu nâng cao (Aggregation Functions) (tùy chọn bổ
   sung) - Thêm nhiều bản ghi vào bảng NhanVien với cột lương (luong) - Thực hành truy vấn sqp với JDBC để: - Tính tổng lương SUM(luong)

- Tìm mức lương trung bình AVG(luong) - Tìm nhân viên có mức lương cao nhất/ thấp nhất MIN/MAX(luong) - Đếm số lượng nhân viên theo chức vụ (COUNT và GROUP BY)
