# Tong hop code bai tap

Tong hop theo **nhom bai tap (thu muc)**. Moi bai gom nhieu file lien quan.

## Đề bài đầy đủ theo file kk.md (đối chiếu với code thư mục để dò khi đi thi)

### Tuần 1 - Java Basic (đề tổng quát)

- In `Hello, World!`.
- Nhập tên và in `Hi, I am <tên>`.
- Nhập 2 số nguyên và in tổng.
- Kiểm tra chẵn/lẻ.
- Nhập tháng (1-12), in tên tháng tiếng Anh.
- OOP mở rộng: bài quản lý động vật.
- File/Folder: xóa, tìm, copy, đọc/ghi file (kể cả nhị phân, ảnh).

### Tuần 2 - OOP (kế thừa, đa hình)

- Bài 1: Quản lý **NhanVien** (`NhanVien`, `NhanVienVanPhong`, `NhanVienSanXuat`), nhập/xuất và tính lương.
- Bài 2: Quản lý **PhuongTien** (`PhuongTien`, `XeMay`, `Oto`), tính thuế theo loại.

### Tuần 3 - Stream (InputStream, BufferedReader, PrintWriter)

- Hoàn chỉnh 4 ví dụ `InStream1`, `InStream2`, `ReadLine`, `PrintString`.
- Áp dụng Stream cho các bài tuần 1-2 (nhập/xuất theo luồng).

### Tuần 4 - Threads

- Bài 1: Thread cơ bản.
- Bài 2: `FileTWrite` ghi file bằng nhiều thread.
- Bài 3: `FileTReader` đọc file bằng nhiều thread.
- Bài 4: Đọc/ghi cùng file có đồng bộ hóa.
- Bài 5: Producer-Consumer với `wait/notify`.

### Tuần 5 - Socket TCP/UDP

- Bài 1: Đổi số 0-9 sang chữ tiếng Việt (TCP).
- Bài 2-3: Chat TCP (bản cơ bản và mở rộng args IP/port).
- Bài 4-5: Date/Time với TCP rồi UDP.
- Bài 6: Bài toán tính toán trên server (TCP/UDP).
- Bài 7: Gửi file (TCP/UDP).
- Bài 8: Tính toán theo khung `OP Operand1 Operand2`.
- Bài 9: Nhiều client đọc `data.txt`.
- Bài 10: Lưu tin nhắn từng client vào file riêng.

### Tuần 6 - URL + Threads + TCP

- Bài 1: Nhận domain, in hostname/IP.
- Bài 2: Kiểm tra hostname tồn tại và liệt kê toàn bộ IP.
- Bài 3: 2 thread + buffer số nguyên, tính tổng, dừng khi nhập `-1`.
- Bài 4: TCP tính giai thừa.
- Bài 5: TCP xử lý chuỗi (in hoa + đếm ký tự).

### Tuần 7 - LAB 06 RMI

- Bài 1: `sayHello()`.
- Bài 2: `add(a,b)`.
- Bài 3: `isPrime(n)`.
- Bài 4: Danh bạ từ xa (add/find/delete).
- Bài 5: Chat đơn giản.
- Bài 6: Tài khoản ngân hàng (balance/deposit/withdraw).
- Bài 7: Tính diện tích hình học.
- Bài 8: Đặt vé máy bay.
- Bài 9: Đấu giá trực tuyến.

### Tuần 8 - RMI mở rộng (đối chiếu `tuan8/kk.txt`)

- Bài 1: Client gửi chuỗi biểu thức không ngoặc (`+ - * /`), server tính và trả kết quả hoặc báo lỗi định dạng.
- Bài 2: Client gửi CMND/CCCD, server tra cứu họ tên/quê quán và trả kết quả hoặc báo không tìm thấy.

### Tuần 9 - JDBC + SQLite (đối chiếu `tuan9`)

- Thiết lập SQLite JDBC, tạo kết nối DB.
- Tạo bảng `SanPham`, `NhanVien`.
- CRUD sản phẩm (`insert`, `update`, `delete`) bằng `PreparedStatement`.
- Dùng transaction (`setAutoCommit(false)`, `commit`, `rollback`).
- Truy vấn thống kê lương nhân viên (`SUM`, `AVG`, `MAX`, `MIN`).

## 📑 Mục lục mới (chuẩn theo tuần -> bài -> thư mục code)

### TUẦN 2 - OOP

- [Bài tập 1 - TUẦN 2 - `t2/tuan2`](#bai-tap-001)
- [Bài tập 2 - TUẦN 2 - `t2/tuan2b`](#bai-tap-002)

### TUẦN 3 - Stream + OOP

- [Bài tập 3 - TUẦN 3 - `t3/eg`](#bai-tap-003)
- [Bài tập 4 - TUẦN 3 - `t3/tuan1`](#bai-tap-004)
- [Bài tập 5 - TUẦN 3 - `t3/tuan2`](#bai-tap-005)
- [Bài tập 6 - TUẦN 3 - `t3/tuan2b`](#bai-tap-006)

### TUẦN 4 - Threads

- [Bài tập 7 - TUẦN 4 - `t4/tuan4/src`](#bai-tap-007)
- [Bài tập 8 - TUẦN 4 - `t4/tuan4/src/bai1`](#bai-tap-008)
- [Bài tập 9 - TUẦN 4 - `t4/tuan4/src/bai2`](#bai-tap-009)
- [Bài tập 10 - TUẦN 4 - `t4/tuan4/src/bai3`](#bai-tap-010)
- [Bài tập 11 - TUẦN 4 - `t4/tuan4/src/bai4`](#bai-tap-011)
- [Bài tập 12 - TUẦN 4 - `t4/tuan4/src/bai5`](#bai-tap-012)

### TUẦN 5 - TCP/UDP + Socket

- [Bài tập 13 - TUẦN 5 - `t5`](#bai-tap-013)
- [Bài tập 14 - TUẦN 5 - `t5/t5-2/cac-bai-co-ban/countchar`](#bai-tap-014)
- [Bài tập 15 - TUẦN 5 - `t5/t5-2/cac-bai-co-ban/evenodd`](#bai-tap-015)
- [Bài tập 16 - TUẦN 5 - `t5/t5-2/cac-bai-co-ban/lowercase`](#bai-tap-016)
- [Bài tập 17 - TUẦN 5 - `t5/t5-2/cac-bai-co-ban/sumnumbers`](#bai-tap-017)
- [Bài tập 18 - TUẦN 5 - `t5/t5-2/cac-bai-co-ban/uppercase`](#bai-tap-018)
- [Bài tập 19 - TUẦN 5 - `t5/t5-2/gui-nhan`](#bai-tap-019)
- [Bài tập 20 - TUẦN 5 - `t5/t5-2/gui-nhan-luong`](#bai-tap-020)
- [Bài tập 21 - TUẦN 5 - `t5/t5-2/nhieuServer-guitext`](#bai-tap-021)
- [Bài tập 22 - TUẦN 5 - `t5/tcp-tuan5-gk/b1`](#bai-tap-022)
- [Bài tập 23 - TUẦN 5 - `t5/tcp-tuan5-gk/b10`](#bai-tap-023)
- [Bài tập 24 - TUẦN 5 - `t5/tcp-tuan5-gk/b2`](#bai-tap-024)
- [Bài tập 25 - TUẦN 5 - `t5/tcp-tuan5-gk/b3`](#bai-tap-025)
- [Bài tập 26 - TUẦN 5 - `t5/tcp-tuan5-gk/b4`](#bai-tap-026)
- [Bài tập 27 - TUẦN 5 - `t5/tcp-tuan5-gk/b5`](#bai-tap-027)
- [Bài tập 28 - TUẦN 5 - `t5/tcp-tuan5-gk/b6`](#bai-tap-028)
- [Bài tập 29 - TUẦN 5 - `t5/tcp-tuan5-gk/b7`](#bai-tap-029)
- [Bài tập 30 - TUẦN 5 - `t5/tcp-tuan5-gk/b8`](#bai-tap-030)
- [Bài tập 31 - TUẦN 5 - `t5/tcp-tuan5-gk/b9`](#bai-tap-031)

### TUẦN 6 - URL/Domain + Thread + TCP

- [Bài tập 32 - TUẦN 6 - `t6-lt`](#bai-tap-032)
- [Bài tập 33 - TUẦN 6 - `t6/bai1`](#bai-tap-033)
- [Bài tập 34 - TUẦN 6 - `t6/bai2`](#bai-tap-034)
- [Bài tập 35 - TUẦN 6 - `t6/bai3`](#bai-tap-035)
- [Bài tập 36 - TUẦN 6 - `t6/bai4`](#bai-tap-036)
- [Bài tập 37 - TUẦN 6 - `t6/bai5`](#bai-tap-037)

### TUẦN 7 - RMI

- [Bài tập 38 - TUẦN 7 - `tuan7`](#bai-tap-038)
- [Bài tập 39 - TUẦN 7 - `tuan7/bai1`](#bai-tap-039)
- [Bài tập 40 - TUẦN 7 - `tuan7/bai2`](#bai-tap-040)
- [Bài tập 41 - TUẦN 7 - `tuan7/bai3`](#bai-tap-041)
- [Bài tập 42 - TUẦN 7 - `tuan7/bai4`](#bai-tap-042)
- [Bài tập 43 - TUẦN 7 - `tuan7/bai5`](#bai-tap-043)
- [Bài tập 44 - TUẦN 7 - `tuan7/bai6`](#bai-tap-044)

### TUẦN 8 - RMI mở rộng

- [Bài tập 45 - TUẦN 8 - `tuan8`](#bai-tap-045)
- [Bài tập 46 - TUẦN 8 - `tuan8/bai1`](#bai-tap-046)
- [Bài tập 47 - TUẦN 8 - `tuan8/bai2`](#bai-tap-047)

### TUẦN 9 - JDBC/SQLite

- [Bài tập 48 - TUẦN 9 - `tuan9`](#bai-tap-048)

`<a id='bai-tap-001'></a>`

## Bài tập 1 - TUẦN 2 - `t2/tuan2`

**Tiêu đề bài tập:** T2 – OOP (Lập Trình Hướng Đối Tượng)

**Yeu cau tom tat:** Cấu trúc thư mục t2/ ├── tuan2/     ← OOP + Scanner (nhập từng dòng đơn giản)

**DE BAI / MO TA CHI TIET:**

**Vấn đề**: Quản lý nhân viên với các loại khác nhau (văn phòng, sản xuất), mỗi loại có cách tính lương riêng.

**Yêu cầu chi tiết**:

- Tạo lớp cha **NhanVien** với thuộc tính: maNV (String), hoTen (String), các phương thức nhập/hiển thị
- Tạo lớp con **NhanVienVanPhong** với luongCoBan (double) → lương = luongCoBan
- Tạo lớp con **NhanVienSanXuat** với soSanPham (int), donGia (double) → lương = soSanPham × donGia
- Sử dụng **kế thừa (inheritance)** để tái sử dụng code
- Main: tạo 1 NhanVienVanPhong + 1 NhanVienSanXuat, nhập thông tin bằng Scanner.nextLine() / nextDouble(), tính lương, hiển thị kết quả

### Danh sach file

- Main.java
- NhanVien.java
- NhanVienSanXuat.java
- NhanVienVanPhong.java

### File: Main.java

**Duong dan:** `t2/tuan2/Main.java`

```java
package tuan2;

public class Main {
    public static void main(String[] args) {
   
        NhanVienVanPhong nv1 = new NhanVienVanPhong();
        System.out.println("nhap nhan vien van phong");
        nv1.nhapThongTinVP();
    
  
        NhanVienSanXuat nv2 = new NhanVienSanXuat();
        System.out.println("\nnhap nhan vien san xuat");
        nv2.nhapThongTinSX();

   
        System.out.println("\ndanh sach nhan vien");
    
        nv1.hienThiThongTin(); 
        System.out.println(" | luong: " + nv1.tinhLuong());

        nv2.hienThiThongTin(); 
        System.out.println(" | luong: " + nv2.tinhLuong());
    }
}
```

### File: NhanVien.java

**Duong dan:** `t2/tuan2/NhanVien.java`

```java
package tuan2;

import java.util.Scanner;

public class NhanVien {
    String maNV;
    String hoTen;

  
    public void nhapThongTin() {
        Scanner sc = new Scanner(System.in);
        System.out.print("nhap ma nv: ");
        maNV = sc.nextLine();
        System.out.print("nhap ho ten: ");
        hoTen = sc.nextLine();
    }

   
    public void hienThiThongTin() {
        System.out.print("ma nv : " + maNV + " | ho ten : " + hoTen);
    }
}
```

### File: NhanVienSanXuat.java

**Duong dan:** `t2/tuan2/NhanVienSanXuat.java`

```java
package tuan2;

import java.util.Scanner;

public class NhanVienSanXuat extends NhanVien {
    int soSanPham;
    double donGia;

    public void nhapThongTinSX() {
        super.nhapThongTin(); 
        Scanner sc = new Scanner(System.in);
        System.out.print("so san pham : ");
        soSanPham = sc.nextInt();
        System.out.print("don gia : ");
        donGia = sc.nextDouble();
    }

    public double tinhLuong() {
        return soSanPham * donGia;
    }
}
```

### File: NhanVienVanPhong.java

**Duong dan:** `t2/tuan2/NhanVienVanPhong.java`

```java
package tuan2;

import java.util.Scanner;

public class NhanVienVanPhong extends NhanVien {
    double luongCoBan;

    public void nhapThongTinVP() {
        super.nhapThongTin(); 
        Scanner sc = new Scanner(System.in);
        System.out.print("nhap luong can ban : ");
        luongCoBan = sc.nextDouble();
    }

    public double tinhLuong() {
        return luongCoBan;
    }
}
```

`<a id='bai-tap-002'></a>`

## Bài tập 2 - TUẦN 2 - `t2/tuan2b`

**Tiêu đề bài tập:** T2 – OOP (Lập Trình Hướng Đối Tượng)

**Yeu cau tom tat:** Cấu trúc thư mục t2/ ├── tuan2/     ← OOP + Scanner (nhập từng dòng đơn giản)

**DE BAI / MO TA CHI TIET:**

**Vấn đề**: Quản lý các loại phương tiện khác nhau (xe máy, ô tô) với cách tính thuế khác nhau dựa trên giá bán.

**Yêu cầu chi tiết**:

- Tạo lớp cha **PhuongTien** với: hangSanXuat, namSanXuat, giaBan
- Tạo lớp con **XeMay**: thuế = giaBan × 5%
- Tạo lớp con **Oto**: thuế = giaBan × 10%
- Sử dụng **phương thức ảo (virtual method)** để tính thuế khác nhau
- Sử dụng **BufferedReader** hoặc hardcode dữ liệu, sử dụng **PrintWriter** để xuất kết quả
- Main: tạo danh sách phương tiện, in thông tin từng xe + thuế phải trả

### Danh sach file

- Main.java
- Oto.java
- PhuongTien.java
- XeMay.java

### File: Main.java

**Duong dan:** `t2/tuan2b/Main.java`

```java
package tuan2b;

public class Main {
    public static void main(String[] args) {
   
        XeMay xm = new XeMay("Honda", 2026, 40000000, 125);
        System.out.println("thong tin xe may");
        xm.hienThiThongTin();
        System.out.println("tax: " + xm.tinhThue());

        System.out.println("\n------------------------\n");

    
        Oto ot = new Oto("Toyota", 2028, 800000000, 5);
        System.out.println("thong tin oto");
        ot.hienThiThongTin();
        System.out.println("tax: " + ot.tinhThue());
    }
}
```

### File: Oto.java

**Duong dan:** `t2/tuan2b/Oto.java`

```java
/**
 * 
 */
package tuan2b;

public class Oto extends PhuongTien {
    int soChoNgoi;

    public Oto(String hangSanXuat, int namSanXuat, double giaBan, int soChoNgoi) {
        super(hangSanXuat, namSanXuat, giaBan);
        this.soChoNgoi = soChoNgoi;
    }

    public double tinhThue() {
        return giaBan * 0.1;
    }
}
```

### File: PhuongTien.java

**Duong dan:** `t2/tuan2b/PhuongTien.java`

```java
package tuan2b;

public class PhuongTien {
    String hangSanXuat;
    int namSanXuat;
    double giaBan;

    public PhuongTien(String hangSanXuat, int namSanXuat, double giaBan) {
        this.hangSanXuat = hangSanXuat;
        this.namSanXuat = namSanXuat;
        this.giaBan = giaBan;
    }

    public void hienThiThongTin() {
        System.out.println("Hang: " + hangSanXuat + ", Nam: " + namSanXuat + ", Gia: " + giaBan);
    }
}

```

### File: XeMay.java

**Duong dan:** `t2/tuan2b/XeMay.java`

```java
package tuan2b;


public class XeMay extends PhuongTien {
    double dungTichXiLanh;

    public XeMay(String hangSanXuat, int namSanXuat, double giaBan, double dungTichXiLanh) {
        super(hangSanXuat, namSanXuat, giaBan); 
        this.dungTichXiLanh = dungTichXiLanh;
    }

    public double tinhThue() {
    
        return giaBan * 0.05;
    }
}

```

`<a id='bai-tap-003'></a>`

## Bài tập 3 - TUẦN 3 - `t3/eg`

**Tiêu đề bài tập:** T3 – Stream (InputStream, BufferedReader, PrintWriter) + OOP

**Yeu cau tom tat:** | File | Nội dung | Chạy |

**Cau hoi de bai:** Viet cac vi du co ban ve Stream trong Java: doc byte bang InputStream, doc dong bang BufferedReader va ghi du lieu bang PrintWriter.

### Danh sach file

- ex1.java
- ex2.java
- ex3.java
- ex4.java

### File: ex1.java

**Duong dan:** `t3/eg/ex1.java`

```java
package eg;

import java.io.IOException;
import java.io.InputStream;

public class ex1 {
    public static void main(String args[]) {
        InputStream is = System.in;                        
        System.out.println("nhap cac ki tu ( 'q' de thoat):");
    
        while(true) {
            try {
                int ch = is.read();
                if(ch == -1 || ch == 'q') break;

   
                if (ch >= 32) { 
                    System.out.println("Ký tự vừa nhập: " + (char)ch);
                }
            } catch (IOException ie) {
                System.out.println("Error: " + ie);
            }
        }
    }
}
```

### File: ex2.java

**Duong dan:** `t3/eg/ex2.java`

```java
package eg;

import java.io.IOException;
import java.io.InputStream;

public class ex2 {
    public static void main(String[] args) {
        InputStream is = System.in;
        System.out.println("nhap noi dung bat ki:");

        while (true) {
            try {
                int num = is.available();    
                if (num > 0) {
                    byte[] b = new byte[num];
                    int result = is.read(b);                      
                    if (result == -1) break;
                
                    String s = new String(b); 
                    System.out.print("ban da nhap: " + s);
                } else {
                
                    Thread.sleep(500); 
                    System.out.print(".");
                }
            } catch (IOException | InterruptedException ie) {
                System.out.println("Error: " + ie);
            }
        }
    }
}
```

### File: ex3.java

**Duong dan:** `t3/eg/ex3.java`

```java
package eg;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class ex3 {
    public static void main(String[] args) {
    
        InputStreamReader isr = new InputStreamReader(System.in);
        BufferedReader br = new BufferedReader(isr);
    

        System.out.println("--- Chuong trinh doc van ban (BufferedReader) ---");
        System.out.println("Nhap noi dung (Go 'exit' hoac 'quit' de dung):");

        while (true) {
            try {
            
                String line = br.readLine();

           
                if (line == null || line.equalsIgnoreCase("exit") || line.equalsIgnoreCase("quit")) {
                    System.out.println("Dang thoat...");
                    break;
                }

          
                System.out.println("Ket qua: " + line);

            } catch (IOException ie) {
                System.out.println("Co loi xay ra: " + ie.getMessage());
                break;
            }
        }

  
        try {
            br.close();
            isr.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    
        System.out.println("Chuong trinh ket thuc.");
    }
}
```

### File: ex4.java

**Duong dan:** `t3/eg/ex4.java`

```java
package eg;

import java.io.OutputStream;
import java.io.PrintWriter;

public class ex4 {
    public static void main(String[] args) {
        OutputStream os = System.out;
    
    
        PrintWriter pw = new PrintWriter(os, true);

        pw.write("This is a string using write() \r\n");

        pw.println("This is a line using println()");

    
        pw.write("Bye! Bye! (No newline here)");

    
        pw.flush();

                                  
        pw.close();
    }
}
```

`<a id='bai-tap-004'></a>`

## Bài tập 4 - TUẦN 3 - `t3/tuan1`

**Tiêu đề bài tập:** T3 – Stream (InputStream, BufferedReader, PrintWriter) + OOP

**Yeu cau tom tat:** | File | Nội dung | Chạy |

**Cau hoi de bai:** Thuc hien bo bai tap nhap/xu ly co ban gom: in chuoi, nhap ten, tinh tong 2 so, kiem tra chan-le va doi so thang sang ten thang tieng Anh.

### Danh sach file

- ex1.java
- ex2.java
- ex3.java
- ex4.java
- ex5.java

### File: ex1.java

**Duong dan:** `t3/tuan1/ex1.java`

```java
package tuan1;

import java.io.*;

public class ex1 {
    public static void main(String[] args) {
   
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out, true);

        try {
       
            pw.println("--- Bai 1 ---");
            pw.println("Hello, World!");

      
            pw.println("\n--- Bai 2 ---");
            pw.print("Nhap ten cua ban: "); pw.flush();
            String name = br.readLine();
            pw.println("Hi, I am " + name);

     
            pw.println("\n--- Bai 3 ---");
            pw.print("Nhap so A: "); pw.flush();
            double a = Double.parseDouble(br.readLine());
            pw.print("Nhap so B: "); pw.flush();
            double b = Double.parseDouble(br.readLine());
            pw.println("Tong A + B = " + (a + b));

      
            pw.println("\n--- Bai 4 ---");
            pw.print("Nhap mot so nguyen: "); pw.flush();
            int n = Integer.parseInt(br.readLine());
            if (n % 2 == 0) {
                pw.println(n + " la so chan");
            } else {
                pw.println(n + " la so le");
            }

        
            pw.println("\n--- Bai 5 ---");
            pw.print("Nhap mot thang (1-12): "); pw.flush();
            int month = Integer.parseInt(br.readLine());
            String result;
            switch (month) {
                case 1:  result = "January"; break;
                case 2:  result = "February"; break;
                case 3:  result = "March"; break;
                case 4:  result = "April"; break;
                case 5:  result = "May"; break;
                case 6:  result = "June"; break;
                case 7:  result = "July"; break;
                case 8:  result = "August"; break;
                case 9:  result = "September"; break;
                case 10: result = "October"; break;
                case 11: result = "November"; break;
                case 12: result = "December"; break;
                default: result = "Invalid month!"; break;
            }
            pw.println("English name: " + result);

        } catch (IOException e) {
            pw.println("Loi nhap xuat: " + e.getMessage());
        } catch (NumberFormatException e) {
            pw.println("Loi: Vui long nhap dung dinh dang so!");
        }
    }
}
```

### File: ex2.java

**Duong dan:** `t3/tuan1/ex2.java`

```java
package tuan1;

import java.io.*;

public class ex2 {
    public static void main(String[] args) throws IOException {
        // InputStream (byte) → InputStreamReader (byte→char) → BufferedReader (buffer + dòng)
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out, true);

        pw.print("Nhap ten cua ban: "); pw.flush();
        String name = br.readLine();
        pw.println("Hi, I am " + name);
    }
}
```

### File: ex3.java

**Duong dan:** `t3/tuan1/ex3.java`

```java
package tuan1;

import java.io.*;

public class ex3 {
    public static void main(String[] args) throws IOException {
        // InputStream (byte) → InputStreamReader (byte→char) → BufferedReader (buffer + dòng)
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out, true);

        try {
            pw.print("Nhap so A: "); pw.flush();
            int a = Integer.parseInt(br.readLine());

            pw.print("Nhap so B: "); pw.flush();
            int b = Integer.parseInt(br.readLine());

            pw.println("Tong cua A + B la: " + (a + b));
        } catch (NumberFormatException e) {
            pw.println("Vui long nhap so nguyen hop le!");
        }
    }
}

```

### File: ex4.java

**Duong dan:** `t3/tuan1/ex4.java`

```java
package tuan1;

import java.io.*;

public class ex4 {
    public static void main(String[] args) throws IOException {
        // InputStream (byte) → InputStreamReader (byte→char) → BufferedReader (buffer + dòng)
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out, true);

        pw.print("Nhap vao mot so: "); pw.flush();
        int n = Integer.parseInt(br.readLine());

        if (n % 2 == 0) {
            pw.println(n + " la so chan.");
        } else {
            pw.println(n + " la so le.");
        }
    }
}
```

### File: ex5.java

**Duong dan:** `t3/tuan1/ex5.java`

```java
package tuan1;

import java.io.*;

public class ex5 {
    public static void main(String[] args) throws IOException {
        // InputStream (byte) → InputStreamReader (byte→char) → BufferedReader (buffer + dòng)
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter pw = new PrintWriter(System.out, true);

        pw.print("Nhap vao mot thang (1-12): "); pw.flush();
        int month = Integer.parseInt(br.readLine());
        String monthName;

        switch (month) {
            case 1:  monthName = "January";   break;
            case 2:  monthName = "February";  break;
            case 3:  monthName = "March";     break;
            case 4:  monthName = "April";     break;
            case 5:  monthName = "May";       break;
            case 6:  monthName = "June";      break;
            case 7:  monthName = "July";      break;
            case 8:  monthName = "August";    break;
            case 9:  monthName = "September"; break;
            case 10: monthName = "October";   break;
            case 11: monthName = "November";  break;
            case 12: monthName = "December";  break;
            default: monthName = "Thang khong hop le!"; break;
        }

        pw.println("Ten tieng Anh: " + monthName);
    }
}
```

`<a id='bai-tap-005'></a>`

## Bài tập 5 - TUẦN 3 - `t3/tuan2`

**Tiêu đề bài tập:** T3 – Stream (InputStream, BufferedReader, PrintWriter) + OOP

**Yeu cau tom tat:** | File | Nội dung | Chạy |

**Cau hoi de bai:** Viet chuong trinh OOP NhanVien su dung BufferedReader/PrintWriter de nhap xuat, gom nhan vien van phong va san xuat, co ham tinh luong.

### Danh sach file

- Main.java
- NhanVien.java
- NhanVienSanXuat.java
- NhanVienVanPhong.java

### File: Main.java

**Duong dan:** `t3/tuan2/Main.java`

```java
package tuan2;

import java.io.*;

public class Main {
    public static void main(String[] args) {
                 
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    
        PrintWriter pw = new PrintWriter(System.out, true);

        try {
            pw.println("NHAP NHAN VIEN VAN PHONG");
            NhanVienVanPhong nvvp = new NhanVienVanPhong();
            nvvp.nhapVanPhong(br, pw);

            pw.println("\nNHAP NHAN VIEN SAN XUAT");
            NhanVienSanXuat nvsx = new NhanVienSanXuat();
            nvsx.nhapSanXuat(br, pw);

            pw.println("\nKET QUA QUAN LY ");
            nvvp.hienThiVanPhong(pw);
            pw.println(" ");
            nvsx.hienThiSanXuat(pw);

        } catch (IOException e) {
            pw.println("Loi doc du lieu: " + e.getMessage());
        } catch (NumberFormatException e) {
            pw.println("Loi dinh dang so: Vui long nhap dung con so!");
        } finally {
        
            pw.close();
        }
    }
}
```

### File: NhanVien.java

**Duong dan:** `t3/tuan2/NhanVien.java`

```java
package tuan2;

import java.io.*;

public class NhanVien {
    protected String maNV;
    protected String hoTen;

   
    public void nhapThongTin(BufferedReader br, PrintWriter pw) throws IOException {
        pw.print("Nhap ma nhan vien: "); pw.flush();
        maNV = br.readLine();
        pw.print("Nhap ho ten: "); pw.flush();
        hoTen = br.readLine();
    }

    public void hienThiThongTin(PrintWriter pw) {
        pw.println("Ma NV: " + maNV);
        pw.println("Ho ten: " + hoTen);
    }
}
```

### File: NhanVienSanXuat.java

**Duong dan:** `t3/tuan2/NhanVienSanXuat.java`

```java
package tuan2;

import java.io.*;

public class NhanVienSanXuat extends NhanVien {
    private int soSanPham;
    private double donGia;

    public void nhapSanXuat(BufferedReader br, PrintWriter pw) throws IOException {
        super.nhapThongTin(br, pw);
        pw.print("Nhap so san pham: "); pw.flush();
        soSanPham = Integer.parseInt(br.readLine());
        pw.print("Nhap don gia: "); pw.flush();
        donGia = Double.parseDouble(br.readLine());
    }

    public double tinhLuong() {
        return soSanPham * donGia;
    }

    public void hienThiSanXuat(PrintWriter pw) {
        super.hienThiThongTin(pw);
        pw.println("Luong San Xuat: " + tinhLuong());
    }
}
```

### File: NhanVienVanPhong.java

**Duong dan:** `t3/tuan2/NhanVienVanPhong.java`

```java
package tuan2;

       
 
import java.io.*;

public class NhanVienVanPhong extends NhanVien {
    private double luongCoBan;

    public void nhapVanPhong(BufferedReader br, PrintWriter pw) throws IOException {
        super.nhapThongTin(br, pw);
        pw.print("Nhap luong co ban: "); pw.flush();
        luongCoBan = Double.parseDouble(br.readLine());
    }

    public double tinhLuong() {
        return luongCoBan;
    }

    public void hienThiVanPhong(PrintWriter pw) {
        super.hienThiThongTin(pw);
        pw.println("Luong: " + tinhLuong());
    }
}
```

`<a id='bai-tap-006'></a>`

## Bài tập 6 - TUẦN 3 - `t3/tuan2b`

**Tiêu đề bài tập:** T3 – Stream (InputStream, BufferedReader, PrintWriter) + OOP

**Yeu cau tom tat:** | File | Nội dung | Chạy |

**Cau hoi de bai:** Viet chuong trinh OOP PhuongTien su dung BufferedReader/PrintWriter, gom XeMay va Oto, tinh thue theo quy tac rieng cho moi loai.

### Danh sach file

- Main.java
- Oto.java
- PhuongTien.java
- XeMay.java

### File: Main.java

**Duong dan:** `t3/tuan2b/Main.java`

```java
package tuan2b;

import java.io.*;

public class Main {
    public static void main(String[] args) {
    
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
    
        PrintWriter pw = new PrintWriter(System.out, true);

        try {
      
            pw.println("NHAP DU LIEU XE MAY:");
            XeMay xm = new XeMay();
            xm.nhapXeMay(br, pw);

      
            pw.println("\nNHAP DU LIEU O TO:");
            Oto ot = new Oto();
            ot.nhapOto(br, pw);

     
            pw.println("\nKET QUA QUAN LY");
            xm.hienThiThongTin(pw);
            pw.println(" ");
            ot.hienThiThongTin(pw);

        } catch (IOException e) {
            pw.println("Loi vao ra du lieu: " + e.getMessage());
        } catch (NumberFormatException e) {
            pw.println("Loi sai dinh dang so!");
        } finally {
       
            pw.flush();
        }
    }
}
```

### File: Oto.java

**Duong dan:** `t3/tuan2b/Oto.java`

```java
/**
 * 
 */
package tuan2b;

import java.io.*;

public class Oto extends PhuongTien {
    private int soChoNgoi;

    public void nhapOto(BufferedReader br, PrintWriter pw) throws IOException {
        super.nhapThongTin(br, pw);
        pw.print("Nhap so cho ngoi: "); pw.flush();
        soChoNgoi = Integer.parseInt(br.readLine());
    }

    public double tinhThue() {
        return giaBan * 0.1; 
    }

    @Override
    public void hienThiThongTin(PrintWriter pw) {
        pw.println("\nTHONG TIN O TO");
        super.hienThiThongTin(pw);
        pw.println("So cho ngoi: " + soChoNgoi);
        pw.println("Thue phai nop: " + tinhThue());
    }
}
```

### File: PhuongTien.java

**Duong dan:** `t3/tuan2b/PhuongTien.java`

```java
package tuan2b;

import java.io.*;

public class PhuongTien {
    protected String hangSanXuat;
    protected int namSanXuat;
    protected double giaBan;

   
    public void nhapThongTin(BufferedReader br, PrintWriter pw) throws IOException {
        pw.print("Nhap hang san xuat: "); pw.flush();
        hangSanXuat = br.readLine();
    
        pw.print("Nhap nam san xuat: "); pw.flush();
        namSanXuat = Integer.parseInt(br.readLine());
    
        pw.print("Nhap gia ban: "); pw.flush();
        giaBan = Double.parseDouble(br.readLine());
    }

    public void hienThiThongTin(PrintWriter pw) {
        pw.println("Hang SX: " + hangSanXuat);
        pw.println("Nam SX: " + namSanXuat);
        pw.println("Gia ban: " + giaBan);
    }
}
```

### File: XeMay.java

**Duong dan:** `t3/tuan2b/XeMay.java`

```java
package tuan2b;

import java.io.*;

public class XeMay extends PhuongTien {
    private int dungTichXiLanh;

    public void nhapXeMay(BufferedReader br, PrintWriter pw) throws IOException {
        super.nhapThongTin(br, pw); 
        pw.print("Nhap dung tich xi lanh (cc): "); pw.flush();
        dungTichXiLanh = Integer.parseInt(br.readLine());
    }

    public double tinhThue() {
        return giaBan * 0.05; 
    }

    @Override
    public void hienThiThongTin(PrintWriter pw) {
        pw.println("\nTHONG TIN XE MAY");
        super.hienThiThongTin(pw);
        pw.println("Dung tich: " + dungTichXiLanh + "cc");
        pw.println("Thue phai nop: " + tinhThue());
    }
}
```

`<a id='bai-tap-007'></a>`

## Bài tập 7 - TUẦN 4 - `t4/tuan4/src`

**Tiêu đề bài tập:** TUẦN 4 – Thread (5 bài tăng dần độ khó)

**Yeu cau tom tat:** Cấu trúc thư mục tuan4/ ├── bai1/   ← Thread cơ bản: extends Thread

**Cau hoi de bai:** Tong hop bai tap Thread tu co ban den nang cao: tao luong, doc/ghi file song song, dong bo luong va bai toan nha san xuat - nguoi tieu dung.

### Danh sach file

- module-info.java

### File: module-info.java

**Duong dan:** `t4/tuan4/src/module-info.java`

```java
/**
 * 
 */
/**
 * 
 */
module tuan4 {
}
```

`<a id='bai-tap-008'></a>`

## Bài tập 8 - TUẦN 4 - `t4/tuan4/src/bai1`

**Tiêu đề bài tập:** TUẦN 4 – Thread (5 bài tăng dần độ khó)

**Yeu cau tom tat:** Cấu trúc thư mục tuan4/ ├── bai1/   ← Thread cơ bản: extends Thread

**Cau hoi de bai:** Tao chuong trinh thread co ban bang cach ke thua Thread; tao nhieu luong va cho moi luong thuc thi cong viec lap lai.

### Danh sach file

- MyThread.java
- ThreadSimple.java

### File: MyThread.java

**Duong dan:** `t4/tuan4/src/bai1/MyThread.java`

```java
package bai1;


public class MyThread extends Thread {
    String name;
    int n;

    MyThread(String name, int n) {
        this.name = name;
        this.n = n;
        System.out.println("Thread " + name + " has been created ...!");
        start();
    }

    @Override
    public void run() {
        for (int i = 0; i < n; i++) {
            System.out.println("Hello, I'm " + name);
            System.out.println("I go to bed now, bye bye ... wow ...");
        }
    }

    public static void main(String[] args) {
        int n = 1000;
        int nt = 4;
        for (int i = 0; i < nt; i++) {
            MyThread t = new MyThread("Thread" + i, n);
        }
    }
}
```

### File: ThreadSimple.java

**Duong dan:** `t4/tuan4/src/bai1/ThreadSimple.java`

```java
package bai1;


public class ThreadSimple extends Thread {

    @Override
    public void run() {
        System.out.println("Thread is running...");
    }

    public static void main(String[] args) {
        ThreadSimple t1 = new ThreadSimple();
        t1.start();
    }
}
```

`<a id='bai-tap-009'></a>`

## Bài tập 9 - TUẦN 4 - `t4/tuan4/src/bai2`

**Tiêu đề bài tập:** TUẦN 4 – Thread (5 bài tăng dần độ khó)

**Yeu cau tom tat:** Cấu trúc thư mục tuan4/ ├── bai1/   ← Thread cơ bản: extends Thread

**Cau hoi de bai:** Viet chuong trinh dung nhieu thread de ghi so ngau nhien vao nhieu file khac nhau; co the trien khai theo extends Thread hoac implements Runnable.

### Danh sach file

- FileTWrite.java
- Main.java
- TestPath.java

### File: FileTWrite.java

**Duong dan:** `t4/tuan4/src/bai2/FileTWrite.java`

```java
package bai2;

import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;
//c1 kế thừa Thread
//public class FileTWrite extends Thread {
//    private String filename;
//
//    public FileTWrite(String filename) {
//        this.filename = filename;
//    }
//
//    @Override
//    public void run() {
//        Random rand = new Random();
//        try (FileWriter fw = new FileWriter(filename)) {
//            for (int i = 0; i < 10; i++) {
//                int num = rand.nextInt(100); 
//                fw.write(num + "\n");
//            }
//            System.out.println("da ghi file: " + filename);
//        } catch (IOException e) {
//            e.printStackTrace();
//        }
//    }
//}



//c2 interface Runnable
public class FileTWrite implements Runnable {
    private String filename;

    public FileTWrite(String filename) {
        this.filename = filename;
    }

    @Override
    public void run() {
        Random rand = new Random();
        try (FileWriter fw = new FileWriter(filename)) {
            for (int i = 0; i < 10; i++) {
                int num = rand.nextInt(100); 
                fw.write(num + "\n");
            }
            System.out.println("da ghi: " + filename);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

### File: Main.java

**Duong dan:** `t4/tuan4/src/bai2/Main.java`

```java
package bai2;

import java.io.File;

public class Main {
    public static void main(String[] args) throws Exception {
        // Lấy thư mục bin/bai2 (nơi chứa .class)
        String binDir = new File(Main.class.getResource("Main.class").toURI()).getParent();
        // Đổi bin → src để lưu file vào thư mục source
        String dir = binDir.replace(File.separator + "bin" + File.separator,
                                    File.separator + "src" + File.separator);
        System.out.println("Luu file vao: " + dir);

        //c1 extends Thread
        //FileTWrite t1 = new FileTWrite(dir + File.separator + "file1.txt");
        //FileTWrite t2 = new FileTWrite(dir + File.separator + "file2.txt");
        //FileTWrite t3 = new FileTWrite(dir + File.separator + "file3.txt");
        //t1.start(); t2.start(); t3.start();

        //c2 implements Runnable
        Thread t1 = new Thread(new FileTWrite(dir + File.separator + "file11.txt"));
        Thread t2 = new Thread(new FileTWrite(dir + File.separator + "file22.txt"));
        Thread t3 = new Thread(new FileTWrite(dir + File.separator + "file33.txt"));

        t1.start();
        t2.start();
        t3.start();
    }
}
```

### File: TestPath.java

**Duong dan:** `t4/tuan4/src/bai2/TestPath.java`

```java
package bai2;
import java.io.File;

public class TestPath {
    public static void main(String[] args) throws Exception {
        // Cách 1: getResource
        try {
            String d1 = new File(TestPath.class.getResource("TestPath.class").toURI()).getParent();
            System.out.println("getResource: " + d1);
        } catch (Exception e) { System.out.println("getResource ERROR: " + e); }

        // Cách 2: getProtectionDomain
        try {
            String d2 = new File(TestPath.class.getProtectionDomain().getCodeSource().getLocation().toURI()).getPath();
            System.out.println("getProtection: " + d2);
        } catch (Exception e) { System.out.println("getProtection ERROR: " + e); }

        // Cách 3: user.dir (thư mục hiện tại khi chạy lệnh)
        System.out.println("user.dir: " + System.getProperty("user.dir"));
    }
}

```

`<a id='bai-tap-010'></a>`

## Bài tập 10 - TUẦN 4 - `t4/tuan4/src/bai3`

**Tiêu đề bài tập:** TUẦN 4 – Thread (5 bài tăng dần độ khó)

**Yeu cau tom tat:** Cấu trúc thư mục tuan4/ ├── bai1/   ← Thread cơ bản: extends Thread

**Cau hoi de bai:** Viet chuong trinh dung nhieu thread de doc dong thoi nhieu file van ban va in noi dung theo ten file tuong ung.

### Danh sach file

- file11.txt
- file22.txt
- file33.txt
- FileTReader.java
- Main.java

### File: file11.txt

**Duong dan:** `t4/tuan4/src/bai3/file11.txt`

```text
file1 dong 1
file1 dong 2
file1 dong 3
file1 dong 4
file1 dong 5

```

### File: file22.txt

**Duong dan:** `t4/tuan4/src/bai3/file22.txt`

```text
file2 dong 1
file2 dong 2
file2 dong 3
file2 dong 4
file2 dong 5

```

### File: file33.txt

**Duong dan:** `t4/tuan4/src/bai3/file33.txt`

```text
file3 dong 1
file3 dong 2
file3 dong 3
file3 dong 4
file3 dong 5

```

### File: FileTReader.java

**Duong dan:** `t4/tuan4/src/bai3/FileTReader.java`

```java
package bai3;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
//c1
//public class FileTReader extends Thread {
//    private String filename;
//
//    public FileTReader(String filename) {
//        this.filename = filename;
//    }
//
//    @Override
//    public void run() {
//        System.out.println("doc file: " + filename);
//        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
//            String line;
//            while((line = br.readLine()) != null) {
//                System.out.println("[" + filename + "] " + line);
//            }
//        } catch (IOException e) {
//            System.out.println("khong doc duoc file: " + filename);
//            e.printStackTrace();
//        }
//    }
//}

//c2

public class FileTReader implements Runnable {
    private String filename;

    public FileTReader(String filename) {
        this.filename = filename;
    }

    @Override
    public void run() {
        System.out.println("doc file: " + filename);
        try (BufferedReader br = new BufferedReader(new FileReader(filename))) {
            String line;
            while((line = br.readLine()) != null) {
                System.out.println("[" + filename + "] " + line);
            }
        } catch (IOException e) {
            System.out.println("khong doc duoc file: " + filename);
            e.printStackTrace();
        }
    }
}
```

### File: Main.java

**Duong dan:** `t4/tuan4/src/bai3/Main.java`

```java
package bai3;

import java.io.File;
import java.io.FileWriter;

public class Main {
    public static void main(String[] args) throws Exception {
        // Lấy thư mục bin/bai3, đổi bin → src để lưu vào thư mục source
        String binDir = new File(Main.class.getResource("Main.class").toURI()).getParent();
        String dir = binDir.replace(File.separator + "bin" + File.separator,
                                    File.separator + "src" + File.separator);
        System.out.println("Luu file vao: " + dir);

        // Tạo sẵn 3 file mẫu để đọc
        String[] files = {
            dir + File.separator + "file11.txt",
            dir + File.separator + "file22.txt",
            dir + File.separator + "file33.txt"
        };
        for (int i = 0; i < files.length; i++) {
            try (FileWriter fw = new FileWriter(files[i])) {
                for (int j = 1; j <= 5; j++) {
                    fw.write("file" + (i + 1) + " dong " + j + "\n");
                }
            }
        }

        //c1 extends Thread
        //FileTReader t1 = new FileTReader(files[0]);
        //FileTReader t2 = new FileTReader(files[1]);
        //FileTReader t3 = new FileTReader(files[2]);
        //t1.start(); t2.start(); t3.start();

        //c2 implements Runnable
        Thread t1 = new Thread(new FileTReader(files[0]));
        Thread t2 = new Thread(new FileTReader(files[1]));
        Thread t3 = new Thread(new FileTReader(files[2]));

        t1.start();
        t2.start();
        t3.start();
    }
}
```

`<a id='bai-tap-011'></a>`

## Bài tập 11 - TUẦN 4 - `t4/tuan4/src/bai4`

**Tiêu đề bài tập:** TUẦN 4 – Thread (5 bài tăng dần độ khó)

**Yeu cau tom tat:** Cấu trúc thư mục tuan4/ ├── bai1/   ← Thread cơ bản: extends Thread

**Cau hoi de bai:** Xay dung bai toan 1 luong ghi va 1 luong doc cung file dung wait/notify de dong bo, dam bao doc du lieu moi sau moi lan ghi.

### Danh sach file

- FileBuffer.java
- FileReaderThread.java
- FileWriterThread.java
- Main.java
- shared_file.txt

### File: FileBuffer.java

**Duong dan:** `t4/tuan4/src/bai4/FileBuffer.java`

```java
package bai4;

public class FileBuffer {
    private boolean hasNewData = false;
    public final String filename;

    public FileBuffer(String filename) {
        this.filename = filename;
    }

   
    public synchronized void writeLine(String line) throws InterruptedException, java.io.IOException {
        while (hasNewData) {
            wait();
        }
        try (java.io.FileWriter fw = new java.io.FileWriter(filename, true)) {
            fw.write(line + "\n");
        }
        System.out.println("Writer ghi: " + line);
        hasNewData = true;
        notifyAll();
    }

  
    public synchronized String readNewLine(int lastLineIdx) throws InterruptedException, java.io.IOException {
        while (!hasNewData) {
            wait();
        }

        java.util.List<String> lines = new java.util.ArrayList<>();
        try (java.io.BufferedReader br = new java.io.BufferedReader(new java.io.FileReader(filename))) {
            String line;
            while ((line = br.readLine()) != null) {
                lines.add(line);
            }
        }
        String out = "";
        if (lastLineIdx < lines.size()) {
            out = lines.get(lastLineIdx);
        }

        hasNewData = false;
        notifyAll();
        return out;
    }
}
```

### File: FileReaderThread.java

**Duong dan:** `t4/tuan4/src/bai4/FileReaderThread.java`

```java
package bai4;
public class FileReaderThread extends Thread {
    private FileBuffer buffer;
    private int soLan;

    public FileReaderThread(FileBuffer buffer, int soLan) {
        this.buffer = buffer;
        this.soLan = soLan;
    }

    @Override
    public void run() {
        int lineIndex = 0;
        try {
            for (int i = 1; i <= soLan; i++) {
                String line = buffer.readNewLine(lineIndex++);
                System.out.println("Reader doc: " + line);
                Thread.sleep(400); 
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

### File: FileWriterThread.java

**Duong dan:** `t4/tuan4/src/bai4/FileWriterThread.java`

```java
package bai4;

import java.io.FileWriter;
import java.util.Random;

public class FileWriterThread extends Thread {
    private FileBuffer buffer;
    private int soLan;

    public FileWriterThread(FileBuffer buffer, int soLan) {
        this.buffer = buffer;
        this.soLan = soLan;
    }

    @Override
    public void run() {
        try {
            for (int i = 1; i <= soLan; i++) {
                String data = "dong so " + i + ": " + (int)(Math.random()*100);
                buffer.writeLine(data);
                Thread.sleep(300);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

### File: Main.java

**Duong dan:** `t4/tuan4/src/bai4/Main.java`

```java
package bai4;

import java.io.File;

public class Main {
    public static void main(String[] args) throws Exception {
        // Lấy thư mục bin/bai4, đổi bin → src để lưu vào thư mục source
        String binDir = new File(Main.class.getResource("Main.class").toURI()).getParent();
        String dir = binDir.replace(File.separator + "bin" + File.separator,
                                    File.separator + "src" + File.separator);
        System.out.println("Luu file vao: " + dir);

        String filename = dir + File.separator + "shared_file.txt";
        new File(filename).delete();

        FileBuffer buf = new FileBuffer(filename);

        FileWriterThread writer = new FileWriterThread(buf, 10);
        FileReaderThread reader = new FileReaderThread(buf, 10);

        writer.start();
        reader.start();
    }
}
```

### File: shared_file.txt

**Duong dan:** `t4/tuan4/src/bai4/shared_file.txt`

```text
dong so 1: 35
dong so 2: 92
dong so 3: 88
dong so 4: 75
dong so 5: 25
dong so 6: 67
dong so 7: 45
dong so 8: 13
dong so 9: 19
dong so 10: 20

```

`<a id='bai-tap-012'></a>`

## Bài tập 12 - TUẦN 4 - `t4/tuan4/src/bai5`

**Tiêu đề bài tập:** TUẦN 4 – Thread (5 bài tăng dần độ khó)

**Yeu cau tom tat:** Cấu trúc thư mục tuan4/ ├── bai1/   ← Thread cơ bản: extends Thread

**Cau hoi de bai:** Giai bai toan producer-consumer: mo phong kho hang co suc chua gioi han, nguoi san xuat nhap kho va nguoi tieu dung xuat kho co dong bo wait/notify.

### Danh sach file

- Demo.java
- Kho.java
- NguoiSanXuat.java
- NguoiTieuDung.java

### File: Demo.java

**Duong dan:** `t4/tuan4/src/bai5/Demo.java`

```java
package bai5;

public class Demo {
    public static void main(String[] args) {
        Kho kho = new Kho(10);

        NguoiSanXuat nsx1 = new NguoiSanXuat(kho, "NSX01");
        NguoiSanXuat nsx2 = new NguoiSanXuat(kho, "NSX02");
        NguoiTieuDung ntd1 = new NguoiTieuDung(kho, "NTD01");
        NguoiTieuDung ntd2 = new NguoiTieuDung(kho, "NTD02");

        nsx1.start();
        nsx2.start();
        ntd1.start();
        ntd2.start();
    }
}
```

### File: Kho.java

**Duong dan:** `t4/tuan4/src/bai5/Kho.java`

```java
package bai5;
public class Kho {
    private int sucChua;
    private int tonKho = 0;

    public Kho(int sucChua) {
        this.sucChua = sucChua;
    }

    public synchronized void nhapKho(int soLuong, String tenNguoi) throws InterruptedException {
        while (tonKho + soLuong > sucChua) {
            System.out.println(tenNguoi + " muon nhap " + soLuong + ". khong du cho , wait nhap kho...");
            wait();
        }
        tonKho += soLuong;
        System.out.println(tenNguoi + " da nhap " + soLuong + ". Tồn kho: " + tonKho);
        notifyAll();
    }

    public synchronized void xuatKho(int soLuong, String tenNguoi) throws InterruptedException {
        while (tonKho < soLuong) {
            System.out.println(tenNguoi + " muon xuat " + soLuong + ". khong du hang , cho xuat kho...");
            wait();
        }
        tonKho -= soLuong;
        System.out.println(tenNguoi + " da xuat " + soLuong + ". ton kho: " + tonKho);
        notifyAll();
    }

    public synchronized int getTonKho() {
        return tonKho;
    }
}
```

### File: NguoiSanXuat.java

**Duong dan:** `t4/tuan4/src/bai5/NguoiSanXuat.java`

```java
package bai5;

import java.util.Random;

public class NguoiSanXuat extends Thread {
    private Kho kho;
    private String tenSP;

    public NguoiSanXuat(Kho kho, String tenSP) {
        this.kho = kho;
        this.tenSP = tenSP;
    }

    @Override
    public void run() {
        Random rand = new Random();
        try {
            while (true) {
                int n = 1 + rand.nextInt(5); 
                kho.nhapKho(n, tenSP);
                Thread.sleep(500 + rand.nextInt(1000));
            }
        } catch (InterruptedException e) {
            System.out.println(tenSP + " ket thuc.");
        }
    }
}
```

### File: NguoiTieuDung.java

**Duong dan:** `t4/tuan4/src/bai5/NguoiTieuDung.java`

```java
package bai5;
import java.util.Random;

public class NguoiTieuDung extends Thread {
    private Kho kho;
    private String tenKH;

    public NguoiTieuDung(Kho kho, String tenKH) {
        this.kho = kho;
        this.tenKH = tenKH;
    }

    @Override
    public void run() {
        Random rand = new Random();
        try {
            while (true) {
                int m = 1 + rand.nextInt(5);
                kho.xuatKho(m, tenKH);
                Thread.sleep(700 + rand.nextInt(1000)); 
            }
        } catch (InterruptedException e) {
            System.out.println(tenKH + " ket thuc.");
        }
    }
}
```

`<a id='bai-tap-013'></a>`

## Bài tập 13 - TUẦN 5 - `t5`

**Tiêu đề bài tập:** T5 – Thread ghi File + Socket TCP (nhiều bài thực hành)

**Yeu cau tom tat:** Cấu trúc thư mục t5/ ├── FileThreadWriter.java   ← Thread ghi file

**Cau hoi de bai:** Viet chuong trinh su dung da luong de ghi du lieu vao nhieu file; thread chinh tao nhieu worker, start va join de cho hoan tat.

### Danh sach file

- FileThreadWriter.java
- Main.java

### File: FileThreadWriter.java

**Duong dan:** `t5/FileThreadWriter.java`

```java
import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

public class FileThreadWriter extends Thread {
      private String fileName;
      private int count;

      public FileThreadWriter(String fileName, int count) {
            this.fileName = fileName;
            this.count = count;
      }

      @Override
      public void run() {
            Random random = new Random();
            try (FileWriter writer = new FileWriter(fileName)) {
                  for (int i = 0; i < count; i++) {
                        writer.write(random.nextInt(1000) + "\n");
                        Thread.sleep(100);
                  }
                  System.out.println(getName() + " xong");
            } catch (IOException | InterruptedException e) {
                  e.printStackTrace();
            }
      }
}
```

### File: Main.java

**Duong dan:** `t5/Main.java`

```java
import java.net.URISyntaxException;

public class Main {
      public static void main(String[] args) throws InterruptedException, URISyntaxException {
            String outputDir = new java.io.File(Main.class.getProtectionDomain().getCodeSource().getLocation().toURI()).getPath();
        
            FileThreadWriter[] t = new FileThreadWriter[3];
            for (int i = 0; i < 3; i++) {
                  String filePath = outputDir + java.io.File.separator + "file" + (i + 1) + ".txt";
                  t[i] = new FileThreadWriter(filePath, 10);
                  t[i].setName("T" + (i + 1));
                  t[i].start();
            }
            for (FileThreadWriter thread : t)
                  thread.join();
      }
}
```

`<a id='bai-tap-014'></a>`

## Bài tập 14 - TUẦN 5 - `t5/t5-2/cac-bai-co-ban/countchar`

**Tiêu đề bài tập:** T5 – Thread ghi File + Socket TCP (nhiều bài thực hành)

**Yeu cau tom tat:** Cấu trúc thư mục t5/ ├── FileThreadWriter.java   ← Thread ghi file

**Cau hoi de bai:** Viet ung dung TCP client/server, client gui chuoi va server tra ve so ky tu cua chuoi do.

### Danh sach file

- CountCharClient.java
- CountCharHandler.java
- CountCharServer.java

### File: CountCharClient.java

**Duong dan:** `t5/t5-2/cac-bai-co-ban/countchar/CountCharClient.java`

```java
import java.io.*;
import java.net.*;

public class CountCharClient {
      public static void main(String[] args) throws IOException {
            /*
            // Uncomment để tạo output.txt (không cần server đang chạy)
            try (java.io.PrintWriter pw = new java.io.PrintWriter(new java.io.FileWriter("output.txt"))) {
                pw.println("=== Demo countchar: Dem so ky tu ===");
                String[] inputs = {"Hello", "Java Programming", "TCP Socket", "Xin chao the gioi"};
                for (String s : inputs) {
                    pw.println("Nhap chuoi: " + s);
                    pw.println("Ket qua: So ky tu: " + s.length());
                }
            } catch (java.io.IOException ex) { ex.printStackTrace(); }
            System.exit(0);
            */

            Socket socket = new Socket("localhost", 8890);
            System.out.println("Kết nối đến server đếm ký tự");

            PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader reader = new BufferedReader(
                        new InputStreamReader(socket.getInputStream()));
            BufferedReader inputUser = new BufferedReader(new InputStreamReader(System.in));

            String userMessage;
            while (true) {
                  System.out.print("Nhập chuỗi (gõ 'exit' để thoát): ");
                  userMessage = inputUser.readLine();

                  if (userMessage.equalsIgnoreCase("exit")) {
                        writer.println("exit");
                        break;
                  }

                  writer.println(userMessage);
                  String response = reader.readLine();
                  System.out.println("Kết quả: " + response);
            }

            writer.close();
            reader.close();
            inputUser.close();
            socket.close();
            System.out.println("Ngắt kết nối!");
      }
}

```

### File: CountCharHandler.java

**Duong dan:** `t5/t5-2/cac-bai-co-ban/countchar/CountCharHandler.java`

```java
import java.io.*;
import java.net.*;

public class CountCharHandler extends Thread {
      private Socket socket;
      private int clientId;

      public CountCharHandler(Socket socket, int clientId) {
            this.socket = socket;
            this.clientId = clientId;
      }

      @Override
      public void run() {
            try {
                  BufferedReader reader = new BufferedReader(
                        new InputStreamReader(socket.getInputStream()));
                  PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);

                  String message;
                  while ((message = reader.readLine()) != null && !message.equals("exit")) {
                        System.out.println("Client #" + clientId + " gửi: " + message);
                        int count = message.length();
                        writer.println("Số ký tự: " + count);
                  }

                  System.out.println("Client #" + clientId + " ngắt kết nối!");
                  reader.close();
                  writer.close();
                  socket.close();
            } catch (IOException e) {
                  System.out.println("Lỗi với client #" + clientId);
            }
      }
}

```

### File: CountCharServer.java

**Duong dan:** `t5/t5-2/cac-bai-co-ban/countchar/CountCharServer.java`

```java
import java.io.*;
import java.net.*;

public class CountCharServer {
      public static void main(String[] args) throws IOException {
            ServerSocket serverSocket = new ServerSocket(8890);
            System.out.println("Server đếm số ký tự - Lắng nghe trên port 8890...");

            int clientCount = 0;
            while (true) {
                  Socket socket = serverSocket.accept();
                  clientCount++;
                  System.out.println("Client #" + clientCount + " kết nối!");
              
                  CountCharHandler handler = new CountCharHandler(socket, clientCount);
                  handler.start();
            }
      }
}

```

`<a id='bai-tap-015'></a>`

## Bài tập 15 - TUẦN 5 - `t5/t5-2/cac-bai-co-ban/evenodd`

**Tiêu đề bài tập:** T5 – Thread ghi File + Socket TCP (nhiều bài thực hành)

**Yeu cau tom tat:** Cấu trúc thư mục t5/ ├── FileThreadWriter.java   ← Thread ghi file

**Cau hoi de bai:** Viet ung dung TCP client/server, client gui mot so nguyen va server tra ve ket qua chan hay le.

### Danh sach file

- EvenOddClient.java
- EvenOddHandler.java
- EvenOddServer.java

### File: EvenOddClient.java

**Duong dan:** `t5/t5-2/cac-bai-co-ban/evenodd/EvenOddClient.java`

```java
import java.io.*;
import java.net.*;

public class EvenOddClient {
      public static void main(String[] args) throws IOException {
            /*
            // Uncomment để tạo output.txt (không cần server đang chạy)
            try (java.io.PrintWriter pw = new java.io.PrintWriter(new java.io.FileWriter("output.txt"))) {
                pw.println("=== Demo evenodd: Kiem tra chan le ===");
                int[] nums = {4, 7, 0, 13, 100};
                for (int n : nums) {
                    pw.println("Nhap so: " + n);
                    pw.println("Ket qua: " + n + " la so " + (n % 2 == 0 ? "Chẵn" : "Lẻ"));
                }
            } catch (java.io.IOException ex) { ex.printStackTrace(); }
            System.exit(0);
            */

            Socket socket = new Socket("localhost", 8891);
            System.out.println("Kết nối đến server kiểm tra chẵn lẻ");

            PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader reader = new BufferedReader(
                        new InputStreamReader(socket.getInputStream()));
            BufferedReader inputUser = new BufferedReader(new InputStreamReader(System.in));

            String userMessage;
            while (true) {
                  System.out.print("Nhập số (gõ 'exit' để thoát): ");
                  userMessage = inputUser.readLine();

                  if (userMessage.equalsIgnoreCase("exit")) {
                        writer.println("exit");
                        break;
                  }

                  writer.println(userMessage);
                  String response = reader.readLine();
                  System.out.println("Kết quả: " + response);
            }

            writer.close();
            reader.close();
            inputUser.close();
            socket.close();
            System.out.println("Ngắt kết nối!");
      }
}

```

### File: EvenOddHandler.java

**Duong dan:** `t5/t5-2/cac-bai-co-ban/evenodd/EvenOddHandler.java`

```java
import java.io.*;
import java.net.*;

public class EvenOddHandler extends Thread {
      private Socket socket;
      private int clientId;

      public EvenOddHandler(Socket socket, int clientId) {
            this.socket = socket;
            this.clientId = clientId;
      }

      @Override
      public void run() {
            try {
                  BufferedReader reader = new BufferedReader(
                        new InputStreamReader(socket.getInputStream()));
                  PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);

                  String message;
                  while ((message = reader.readLine()) != null && !message.equals("exit")) {
                        System.out.println("Client #" + clientId + " gửi: " + message);
                        try {
                              int num = Integer.parseInt(message);
                              String result = (num % 2 == 0) ? "Chẵn" : "Lẻ";
                              writer.println(num + " là số " + result);
                        } catch (NumberFormatException e) {
                              writer.println("Lỗi: Vui lòng nhập một số nguyên!");
                        }
                  }

                  System.out.println("Client #" + clientId + " ngắt kết nối!");
                  reader.close();
                  writer.close();
                  socket.close();
            } catch (IOException e) {
                  System.out.println("Lỗi với client #" + clientId);
            }
      }
}

```

### File: EvenOddServer.java

**Duong dan:** `t5/t5-2/cac-bai-co-ban/evenodd/EvenOddServer.java`

```java
import java.io.*;
import java.net.*;

public class EvenOddServer {
      public static void main(String[] args) throws IOException {
            ServerSocket serverSocket = new ServerSocket(8891);
            System.out.println("Server kiểm tra chẵn lẻ - Lắng nghe trên port 8891...");

            int clientCount = 0;
            while (true) {
                  Socket socket = serverSocket.accept();
                  clientCount++;
                  System.out.println("Client #" + clientCount + " kết nối!");
              
                  EvenOddHandler handler = new EvenOddHandler(socket, clientCount);
                  handler.start();
            }
      }
}

```

`<a id='bai-tap-016'></a>`

## Bài tập 16 - TUẦN 5 - `t5/t5-2/cac-bai-co-ban/lowercase`

**Tiêu đề bài tập:** T5 – Thread ghi File + Socket TCP (nhiều bài thực hành)

**Yeu cau tom tat:** Cấu trúc thư mục t5/ ├── FileThreadWriter.java   ← Thread ghi file

**Cau hoi de bai:** Viet ung dung TCP client/server, client gui chuoi va server chuyen toan bo thanh chu thuong roi gui lai.

### Danh sach file

- LowerCaseClient.java
- LowerCaseHandler.java
- LowerCaseServer.java

### File: LowerCaseClient.java

**Duong dan:** `t5/t5-2/cac-bai-co-ban/lowercase/LowerCaseClient.java`

```java
import java.io.*;
import java.net.*;

public class LowerCaseClient {
      public static void main(String[] args) throws IOException {
            /*
            // Uncomment để tạo output.txt (không cần server đang chạy)
            try (java.io.PrintWriter pw = new java.io.PrintWriter(new java.io.FileWriter("output.txt"))) {
                pw.println("=== Demo lowercase: Chuyen chu thuong ===");
                String[] inputs = {"HELLO WORLD", "Java TCP Server", "XIN CHAO THE GIOI", "MixEd CaSe"};
                for (String s : inputs) {
                    pw.println("Nhap chuoi: " + s);
                    pw.println("Ket qua: " + s.toLowerCase());
                }
            } catch (java.io.IOException ex) { ex.printStackTrace(); }
            System.exit(0);
            */

            Socket socket = new Socket("localhost", 8889);
            System.out.println("Kết nối đến server chuyển sang chữ thường");

            PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader reader = new BufferedReader(
                        new InputStreamReader(socket.getInputStream()));
            BufferedReader inputUser = new BufferedReader(new InputStreamReader(System.in));

            String userMessage;
            while (true) {
                  System.out.print("Nhập chuỗi (gõ 'exit' để thoát): ");
                  userMessage = inputUser.readLine();

                  if (userMessage.equalsIgnoreCase("exit")) {
                        writer.println("exit");
                        break;
                  }

                  writer.println(userMessage);
                  String response = reader.readLine();
                  System.out.println("Kết quả: " + response);
            }

            writer.close();
            reader.close();
            inputUser.close();
            socket.close();
            System.out.println("Ngắt kết nối!");
      }
}

```

### File: LowerCaseHandler.java

**Duong dan:** `t5/t5-2/cac-bai-co-ban/lowercase/LowerCaseHandler.java`

```java
import java.io.*;
import java.net.*;

public class LowerCaseHandler extends Thread {
      private Socket socket;
      private int clientId;

      public LowerCaseHandler(Socket socket, int clientId) {
            this.socket = socket;
            this.clientId = clientId;
      }

      @Override
      public void run() {
            try {
                  BufferedReader reader = new BufferedReader(
                        new InputStreamReader(socket.getInputStream()));
                  PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);

                  String message;
                  while ((message = reader.readLine()) != null && !message.equals("exit")) {
                        System.out.println("Client #" + clientId + " gửi: " + message);
                        String result = message.toLowerCase();
                        writer.println(result);
                  }

                  System.out.println("Client #" + clientId + " ngắt kết nối!");
                  reader.close();
                  writer.close();
                  socket.close();
            } catch (IOException e) {
                  System.out.println("Lỗi với client #" + clientId);
            }
      }
}

```

### File: LowerCaseServer.java

**Duong dan:** `t5/t5-2/cac-bai-co-ban/lowercase/LowerCaseServer.java`

```java
import java.io.*;
import java.net.*;

public class LowerCaseServer {
      public static void main(String[] args) throws IOException {
            ServerSocket serverSocket = new ServerSocket(8889);
            System.out.println("Server chuyển sang chữ thường - Lắng nghe trên port 8889...");

            int clientCount = 0;
            while (true) {
                  Socket socket = serverSocket.accept();
                  clientCount++;
                  System.out.println("Client #" + clientCount + " kết nối!");
              
                  LowerCaseHandler handler = new LowerCaseHandler(socket, clientCount);
                  handler.start();
            }
      }
}

```

`<a id='bai-tap-017'></a>`

## Bài tập 17 - TUẦN 5 - `t5/t5-2/cac-bai-co-ban/sumnumbers`

**Tiêu đề bài tập:** T5 – Thread ghi File + Socket TCP (nhiều bài thực hành)

**Yeu cau tom tat:** Cấu trúc thư mục t5/ ├── FileThreadWriter.java   ← Thread ghi file

**Cau hoi de bai:** Viet ung dung TCP client/server, client gui day so (phan tach boi khoang trang) va server tinh tong cac so hop le.

### Danh sach file

- SumNumbersClient.java
- SumNumbersHandler.java
- SumNumbersServer.java

### File: SumNumbersClient.java

**Duong dan:** `t5/t5-2/cac-bai-co-ban/sumnumbers/SumNumbersClient.java`

```java
import java.io.*;
import java.net.*;

public class SumNumbersClient {
      public static void main(String[] args) throws IOException {
            /*
            // Uncomment để tạo output.txt (không cần server đang chạy)
            try (java.io.PrintWriter pw = new java.io.PrintWriter(new java.io.FileWriter("output.txt"))) {
                pw.println("=== Demo sumnumbers: Tinh tong cac so ===");
                String[][] tests = {{"1 2 3 4 5"}, {"10 20 30"}, {"100 200 300 400"}};
                for (String[] t : tests) {
                    String input = t[0];
                    int sum = 0;
                    for (String x : input.split(" ")) sum += Integer.parseInt(x);
                    pw.println("Nhap cac so: " + input);
                    pw.println("Ket qua: Tong: " + sum);
                }
            } catch (java.io.IOException ex) { ex.printStackTrace(); }
            System.exit(0);
            */

            Socket socket = new Socket("localhost", 8892);
            System.out.println("Kết nối đến server tính tổng");

            PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader reader = new BufferedReader(
                        new InputStreamReader(socket.getInputStream()));
            BufferedReader inputUser = new BufferedReader(new InputStreamReader(System.in));

            String userMessage;
            while (true) {
                  System.out.print("Nhập các số cách nhau bằng dấu cách (gõ 'exit' để thoát): ");
                  userMessage = inputUser.readLine();

                  if (userMessage.equalsIgnoreCase("exit")) {
                        writer.println("exit");
                        break;
                  }

                  writer.println(userMessage);
                  String response = reader.readLine();
                  System.out.println("Kết quả: " + response);
            }

            writer.close();
            reader.close();
            inputUser.close();
            socket.close();
            System.out.println("Ngắt kết nối!");
      }
}

```

### File: SumNumbersHandler.java

**Duong dan:** `t5/t5-2/cac-bai-co-ban/sumnumbers/SumNumbersHandler.java`

```java
import java.io.*;
import java.net.*;

public class SumNumbersHandler extends Thread {
      private Socket socket;
      private int clientId;

      public SumNumbersHandler(Socket socket, int clientId) {
            this.socket = socket;
            this.clientId = clientId;
      }

      @Override
      public void run() {
            try {
                  BufferedReader reader = new BufferedReader(
                        new InputStreamReader(socket.getInputStream()));
                  PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);

                  String message;
                  while ((message = reader.readLine()) != null && !message.equals("exit")) {
                        System.out.println("Client #" + clientId + " gửi: " + message);
                        try {
                              String[] numbers = message.split(" ");
                              int sum = 0;
                              for (String num : numbers) {
                                    sum += Integer.parseInt(num);
                              }
                              writer.println("Tổng: " + sum);
                        } catch (NumberFormatException e) {
                              writer.println("Lỗi: Vui lòng nhập các số cách nhau bằng dấu cách!");
                        }
                  }

                  System.out.println("Client #" + clientId + " ngắt kết nối!");
                  reader.close();
                  writer.close();
                  socket.close();
            } catch (IOException e) {
                  System.out.println("Lỗi với client #" + clientId);
            }
      }
}

```

### File: SumNumbersServer.java

**Duong dan:** `t5/t5-2/cac-bai-co-ban/sumnumbers/SumNumbersServer.java`

```java
import java.io.*;
import java.net.*;

public class SumNumbersServer {
      public static void main(String[] args) throws IOException {
            ServerSocket serverSocket = new ServerSocket(8892);
            System.out.println("Server tính tổng các số - Lắng nghe trên port 8892...");

            int clientCount = 0;
            while (true) {
                  Socket socket = serverSocket.accept();
                  clientCount++;
                  System.out.println("Client #" + clientCount + " kết nối!");
              
                  SumNumbersHandler handler = new SumNumbersHandler(socket, clientCount);
                  handler.start();
            }
      }
}

```

`<a id='bai-tap-018'></a>`

## Bài tập 18 - TUẦN 5 - `t5/t5-2/cac-bai-co-ban/uppercase`

**Tiêu đề bài tập:** T5 – Thread ghi File + Socket TCP (nhiều bài thực hành)

**Yeu cau tom tat:** Cấu trúc thư mục t5/ ├── FileThreadWriter.java   ← Thread ghi file

**Cau hoi de bai:** Viet ung dung TCP client/server, client gui chuoi va server chuyen toan bo thanh chu hoa roi gui lai.

### Danh sach file

- UpperCaseClient.java
- UpperCaseHandler.java
- UpperCaseServer.java

### File: UpperCaseClient.java

**Duong dan:** `t5/t5-2/cac-bai-co-ban/uppercase/UpperCaseClient.java`

```java
import java.io.*;
import java.net.*;

public class UpperCaseClient {
      public static void main(String[] args) throws IOException {
            /*
            // Uncomment để tạo output.txt (không cần server đang chạy)
            try (java.io.PrintWriter pw = new java.io.PrintWriter(new java.io.FileWriter("output.txt"))) {
                pw.println("=== Demo uppercase: Chuyen chu hoa ===");
                String[] inputs = {"hello world", "java tcp server", "xin chao the gioi", "MixEd CaSe"};
                for (String s : inputs) {
                    pw.println("Nhap chuoi: " + s);
                    pw.println("Ket qua: " + s.toUpperCase());
                }
            } catch (java.io.IOException ex) { ex.printStackTrace(); }
            System.exit(0);
            */

            Socket socket = new Socket("localhost", 8888);
            System.out.println("Kết nối đến server chuyển sang chữ hoa");

            PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader reader = new BufferedReader(
                        new InputStreamReader(socket.getInputStream()));
            BufferedReader inputUser = new BufferedReader(new InputStreamReader(System.in));

            String userMessage;
            while (true) {
                  System.out.print("Nhập chuỗi (gõ 'exit' để thoát): ");
                  userMessage = inputUser.readLine();

                  if (userMessage.equalsIgnoreCase("exit")) {
                        writer.println("exit");
                        break;
                  }

                  writer.println(userMessage);
                  String response = reader.readLine();
                  System.out.println("Kết quả: " + response);
            }

            writer.close();
            reader.close();
            inputUser.close();
            socket.close();
            System.out.println("Ngắt kết nối!");
      }
}

```

### File: UpperCaseHandler.java

**Duong dan:** `t5/t5-2/cac-bai-co-ban/uppercase/UpperCaseHandler.java`

```java
import java.io.*;
import java.net.*;

public class UpperCaseHandler extends Thread {
      private Socket socket;
      private int clientId;

      public UpperCaseHandler(Socket socket, int clientId) {
            this.socket = socket;
            this.clientId = clientId;
      }

      @Override
      public void run() {
            try {
                  BufferedReader reader = new BufferedReader(
                        new InputStreamReader(socket.getInputStream()));
                  PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);

                  String message;
                  while ((message = reader.readLine()) != null && !message.equals("exit")) {
                        System.out.println("Client #" + clientId + " gửi: " + message);
                        String result = message.toUpperCase();
                        writer.println(result);
                  }

                  System.out.println("Client #" + clientId + " ngắt kết nối!");
                  reader.close();
                  writer.close();
                  socket.close();
            } catch (IOException e) {
                  System.out.println("Lỗi với client #" + clientId);
            }
      }
}

```

### File: UpperCaseServer.java

**Duong dan:** `t5/t5-2/cac-bai-co-ban/uppercase/UpperCaseServer.java`

```java
import java.io.*;
import java.net.*;

public class UpperCaseServer {
      public static void main(String[] args) throws IOException {
            ServerSocket serverSocket = new ServerSocket(8888);
            System.out.println("Server chuyển sang chữ hoa - Lắng nghe trên port 8888...");

            int clientCount = 0;
            while (true) {
                  Socket socket = serverSocket.accept();
                  clientCount++;
                  System.out.println("Client #" + clientCount + " kết nối!");
              
                  UpperCaseHandler handler = new UpperCaseHandler(socket, clientCount);
                  handler.start();
            }
      }
}

```

`<a id='bai-tap-019'></a>`

## Bài tập 19 - TUẦN 5 - `t5/t5-2/gui-nhan`

**Tiêu đề bài tập:** T5 – Thread ghi File + Socket TCP (nhiều bài thực hành)

**Yeu cau tom tat:** Cấu trúc thư mục t5/ ├── FileThreadWriter.java   ← Thread ghi file

**Cau hoi de bai:** Viet chuong trinh TCP gui-nhan co ban: client gui thong diep string, server nhan va phan hoi lai cho client.

### Danh sach file

- TCPClient.java
- TCPServer.java

### File: TCPClient.java

**Duong dan:** `t5/t5-2/gui-nhan/TCPClient.java`

```java
import java.io.*;
import java.net.*;

public class TCPClient {
      public static void main(String[] args) throws IOException {
            /*
            // Uncomment để tạo output.txt (không cần server đang chạy)
            try (java.io.PrintWriter pw = new java.io.PrintWriter(new java.io.FileWriter("output.txt"))) {
                pw.println("=== Demo gui-nhan: TCP Client-Server (Echo) ===");
                pw.println("Ket noi den server localhost:8888");
                pw.println("Gui: Hello Server");
                pw.println("Nhan tu server: Echo: Hello Server");
            } catch (java.io.IOException ex) { ex.printStackTrace(); }
            System.exit(0);
            */

            Socket socket = new Socket("localhost", 8888);
            System.out.println("Kết nối đến server");

            PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader reader = new BufferedReader(
                        new InputStreamReader(socket.getInputStream()));

            writer.println("Hello Server");

            String response = reader.readLine();
            System.out.println("Nhận từ server: " + response);

            writer.close();
            reader.close();
            socket.close();
      }
}

```

### File: TCPServer.java

**Duong dan:** `t5/t5-2/gui-nhan/TCPServer.java`

```java
import java.io.*;
import java.net.*;

public class TCPServer {
      public static void main(String[] args) throws IOException {
            ServerSocket serverSocket = new ServerSocket(8888);
            System.out.println("Server đang lắng nghe trên port 8888...");

            Socket socket = serverSocket.accept();
            System.out.println("Client kết nối!");

            BufferedReader reader = new BufferedReader(
                        new InputStreamReader(socket.getInputStream()));
            PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);

            String message = reader.readLine();
            System.out.println("Nhận từ client: " + message);

            writer.println("Echo: " + message);

            reader.close();
            writer.close();
            socket.close();
            serverSocket.close();
      }
}

```

`<a id='bai-tap-020'></a>`

## Bài tập 20 - TUẦN 5 - `t5/t5-2/gui-nhan-luong`

**Tiêu đề bài tập:** T5 – Thread ghi File + Socket TCP (nhiều bài thực hành)

**Yeu cau tom tat:** Cấu trúc thư mục t5/ ├── FileThreadWriter.java   ← Thread ghi file

**Cau hoi de bai:** Viet chuong trinh TCP su dung luong va stream du lieu dang byte/int; server in thong tin ket noi (IP/port) va echo du lieu ve client.

### Danh sach file

- serverThread.java
- tcpClient.java
- tcpServer.java

### File: serverThread.java

**Duong dan:** `t5/t5-2/gui-nhan-luong/serverThread.java`

```java
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;

public class serverThread extends Thread {
    private Socket client;

    public serverThread(Socket client) {
        this.client = client;
    }

    @Override
    public void run() {
        try {
            // In thông tin client
            System.out.println("===== Client kết nối =====");
            System.out.println("IP Address: " + client.getInetAddress().getHostAddress());
            System.out.println("Port: " + client.getPort());
            System.out.println("Local Port: " + client.getLocalPort());
            System.out.println("Connect Time: " + new java.util.Date());
            System.out.println("========================");
        
            InputStream is = client.getInputStream();
            OutputStream os = client.getOutputStream();

            int ch = 0;
        
            while (true) {
                ch = is.read();
                if (ch == -1) break; 
            
                System.out.println("client goi : " + (char)ch);
            
            
                os.write((char)ch);
            }
        
            System.out.println("Client từ " + client.getInetAddress().getHostAddress() + " đã ngắt kết nối!");
            client.close();
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
```

### File: tcpClient.java

**Duong dan:** `t5/t5-2/gui-nhan-luong/tcpClient.java`

```java
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.Socket;

public class tcpClient {
    public static int port = 5678;

    public static void main(String[] args) throws IOException {
        /*
        // Uncomment để tạo output.txt (không cần server đang chạy)
        try (java.io.PrintWriter pw = new java.io.PrintWriter(new java.io.FileWriter("output.txt"))) {
            pw.println("=== Demo gui-nhan-luong: TCP Client (Echo byte) ===");
            pw.println("Client da duoc tao, ket noi localhost:" + port);
            for (int i = '0'; i <= '9'; i++) {
                pw.println("Gui: " + (char)i + "  =>  ket qua chuyen doi tu Server: " + (char)i);
            }
        } catch (java.io.IOException ex) { ex.printStackTrace(); }
        System.exit(0);
        */

        Socket client;

        try {
            client = new Socket("localhost", port);
            System.out.println("Client da duoc tao");

            OutputStream os = client.getOutputStream();
            InputStream is = client.getInputStream();

            for (int i = '0'; i <= '9'; i++) {
                os.write(i);

                int kq = is.read();
                System.out.println("ket qua chuyen doi tu Server: " + (char)kq);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

### File: tcpServer.java

**Duong dan:** `t5/t5-2/gui-nhan-luong/tcpServer.java`

```java
import java.net.ServerSocket;
import java.net.Socket;

public class tcpServer extends Thread {
    public static int port = 5678; 
    public static void main(String[] args) {
        try {
            ServerSocket server = new ServerSocket(port);
            System.out.println("Server đã được tạo (port: " + port + ")");
            System.out.println("Đang chờ kết nối từ client...\n");
        
            int clientCount = 0;
            while (true) {
                Socket client = server.accept();
                clientCount++;
                System.out.println(">>> Client #" + clientCount + " kết nối!");

                serverThread th = new serverThread(client);
                th.start();
            }
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
```

`<a id='bai-tap-021'></a>`

## Bài tập 21 - TUẦN 5 - `t5/t5-2/nhieuServer-guitext`

**Tiêu đề bài tập:** T5 – Thread ghi File + Socket TCP (nhiều bài thực hành)

**Yeu cau tom tat:** Cấu trúc thư mục t5/ ├── FileThreadWriter.java   ← Thread ghi file

**Cau hoi de bai:** Viet TCP server da client: moi ket noi tao mot thread xu ly rieng; client cho phep gui nhieu dong text lien tuc den khi exit.

### Danh sach file

- ClientHandlerMulti.java
- TCPClientMulti.java
- TCPServerMulti.java

### File: ClientHandlerMulti.java

**Duong dan:** `t5/t5-2/nhieuServer-guitext/ClientHandlerMulti.java`

```java
import java.io.*;
import java.net.*;

public class ClientHandlerMulti extends Thread {
      private Socket socket;
      private int clientId;

      public ClientHandlerMulti(Socket socket, int clientId) {
            this.socket = socket;
            this.clientId = clientId;
      }

      @Override
      public void run() {
            try {
                  BufferedReader reader = new BufferedReader(
                        new InputStreamReader(socket.getInputStream()));
                  PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);

                  String message;
                  while ((message = reader.readLine()) != null) {
                        System.out.println("Client #" + clientId + " gửi: " + message);
                        writer.println("Echo từ server: " + message);
                  }

                  System.out.println("Client #" + clientId + " ngắt kết nối!");
                  reader.close();
                  writer.close();
                  socket.close();
            } catch (IOException e) {
                  System.out.println("Lỗi với client #" + clientId + ": " + e.getMessage());
            }
      }
}

```

### File: TCPClientMulti.java

**Duong dan:** `t5/t5-2/nhieuServer-guitext/TCPClientMulti.java`

```java

import java.io.*;
import java.net.*;

public class TCPClientMulti {
      public static void main(String[] args) throws IOException {
            /*
            // Uncomment để tạo output.txt (không cần server đang chạy)
            try (java.io.PrintWriter pw = new java.io.PrintWriter(new java.io.FileWriter("output.txt"))) {
                pw.println("=== Demo nhieuServer-guitext: TCP Multi-Client (Echo) ===");
                String[] msgs = {"Xin chao!", "Day la tin nhan thu 2", "Ket thuc phien"};
                for (String m : msgs) {
                    pw.println("Nhap tin nhan: " + m);
                    pw.println("Nhan tu server: Echo tu server: " + m);
                }
            } catch (java.io.IOException ex) { ex.printStackTrace(); }
            System.exit(0);
            */

            Socket socket = new Socket("localhost", 8888);
            System.out.println("Kết nối đến server");

            PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader reader = new BufferedReader(
                        new InputStreamReader(socket.getInputStream()));
            BufferedReader inputUser = new BufferedReader(new InputStreamReader(System.in));

            String userMessage;
            while (true) {
                  System.out.print("Nhập tin nhắn (gõ 'exit' để thoát): ");
                  userMessage = inputUser.readLine();

                  if (userMessage.equalsIgnoreCase("exit")) {
                        break;
                  }

                  writer.println(userMessage);
                  String response = reader.readLine();
                  System.out.println("Nhận từ server: " + response);
            }

            writer.close();
            reader.close();
            inputUser.close();
            socket.close();
            System.out.println("Ngắt kết nối!");
      }
}

```

### File: TCPServerMulti.java

**Duong dan:** `t5/t5-2/nhieuServer-guitext/TCPServerMulti.java`

```java
import java.io.*;
import java.net.*;

public class TCPServerMulti {
      public static void main(String[] args) throws IOException {
            ServerSocket serverSocket = new ServerSocket(8888);
            System.out.println("Server đang lắng nghe trên port 8888...");

            int clientCount = 0;
            while (true) {
                  Socket socket = serverSocket.accept();
                  clientCount++;
                  System.out.println("Client #" + clientCount + " kết nối!");
              
                  ClientHandlerMulti handler = new ClientHandlerMulti(socket, clientCount);
                  handler.start();
            }
      }
}

```

`<a id='bai-tap-022'></a>`

## Bài tập 22 - TUẦN 5 - `t5/tcp-tuan5-gk/b1`

**Tiêu đề bài tập:** TCP-TUẦN 5-GK – Bài Tập TCP/UDP Nâng Cao (Giữa Kì)

**Yeu cau tom tat:** Cấu trúc thư mục tcp-tuan5-gk/ ├── b1/   ← TCP: đọc số viết chữ (DataInputStream/DataOutputStream)

**Cau hoi de bai:** Viet bai TCP: client gui ky tu so 0-9, server doi sang chu tieng Viet tuong ung va tra ve ket qua.

### Danh sach file

- Client.java
- ClientHandler.java
- Server.java

### File: Client.java

**Duong dan:** `t5/tcp-tuan5-gk/b1/Client.java`

```java
package b1;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.util.Scanner;

public class Client {
    public static void main(String[] args) {
        String host = "127.0.0.1";
        int port = 5000;

        /*
        // Uncomment để tạo output.txt (không cần server đang chạy)
        try (java.io.PrintWriter pw = new java.io.PrintWriter(new java.io.FileWriter("output.txt"))) {
            pw.println("=== Demo b1: Gui ky tu so, nhan ten tieng Viet ===");
            String[] digits = {"0","1","2","3","4","5","6","7","8","9"};
            String[] names  = {"không","một","hai","ba","bốn","năm","sáu","bảy","tám","chín"};
            for (int i = 0; i < digits.length; i++) {
                pw.println("Nhap: " + digits[i] + "  =>  Server tra ve: " + names[i]);
            }
            pw.println("Nhap: exit  =>  Server tra ve: Bye");
        } catch (java.io.IOException ex) { ex.printStackTrace(); }
        System.exit(0);
        */

        try (Socket socket = new Socket(host, port);
             DataInputStream in = new DataInputStream(socket.getInputStream());
             DataOutputStream out = new DataOutputStream(socket.getOutputStream());
             Scanner sc = new Scanner(System.in)) {

            System.out.println("Da ket noi server. Nhap 1 ky tu (0-9) hoac 'exit' de thoat:");

            while (true) {
                System.out.print("Nhap: ");
                String s = sc.nextLine();

  
                String send = s.equalsIgnoreCase("exit") ? "exit"
                        : (s.isEmpty() ? "" : String.valueOf(s.charAt(0)));

                out.writeUTF(send);
                out.flush();

                String resp = in.readUTF();
                System.out.println("Server tra ve: " + resp);

                if ("exit".equalsIgnoreCase(send)) break;
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

### File: ClientHandler.java

**Duong dan:** `t5/tcp-tuan5-gk/b1/ClientHandler.java`

```java
package b1;


import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;

public class ClientHandler extends Thread {
    private final Socket socket;

    public ClientHandler(Socket socket) {
        this.socket = socket;
    }

    private String docSo(char c) {
        switch (c) {
            case '0': return "không";
            case '1': return "một";
            case '2': return "hai";
            case '3': return "ba";
            case '4': return "bốn";
            case '5': return "năm";
            case '6': return "sáu";
            case '7': return "bảy";
            case '8': return "tám";
            case '9': return "chín";
            default:  return "Không phải số nguyên";
        }
    }

    @Override
    public void run() {
        System.out.println("Client ket noi: " + socket.getInetAddress() + ":" + socket.getPort());

        try (Socket s = socket;
             DataInputStream in = new DataInputStream(s.getInputStream());
             DataOutputStream out = new DataOutputStream(s.getOutputStream())) {

            while (true) {
                String msg;
                try {
                    msg = in.readUTF(); 
                } catch (IOException e) {
                
                    break;
                }

                if ("exit".equalsIgnoreCase(msg)) {
                    out.writeUTF("Bye");
                    out.flush();
                    break;
                }

                char c = msg.isEmpty() ? '\0' : msg.charAt(0);
                String kq = docSo(c);

                out.writeUTF(kq);
                out.flush();
            }

        } catch (IOException e) {
            e.printStackTrace();
        }

        System.out.println("Client ngat: " + socket.getInetAddress() + ":" + socket.getPort());
    }
}
```

### File: Server.java

**Duong dan:** `t5/tcp-tuan5-gk/b1/Server.java`

```java
package b1;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {
    public static void main(String[] args) {
        int port = 5000;

        try (ServerSocket serverSocket = new ServerSocket(port)) {
            System.out.println("Server dang chay tai port " + port + " ...");

            while (true) {
                Socket clientSocket = serverSocket.accept();
                ClientHandler handler = new ClientHandler(clientSocket);
                handler.start(); 
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

`<a id='bai-tap-023'></a>`

## Bài tập 23 - TUẦN 5 - `t5/tcp-tuan5-gk/b10`

**Tiêu đề bài tập:** TCP-TUẦN 5-GK – Bài Tập TCP/UDP Nâng Cao (Giữa Kì)

**Yeu cau tom tat:** Cấu trúc thư mục tcp-tuan5-gk/ ├── b1/   ← TCP: đọc số viết chữ (DataInputStream/DataOutputStream)

**Cau hoi de bai:** Viet bai TCP luu nhat ky client: server nhan nhieu dong tin nhan den khi gap "HET" va ghi vao file rieng clientX.txt.

### Danh sach file

- Client.java
- ClientHandler.java
- Server.java

### File: Client.java

**Duong dan:** `t5/tcp-tuan5-gk/b10/Client.java`

```java
package b10;
import java.io.*;
import java.net.Socket;
import java.util.Scanner;
/*
 * Bai 10 - Client
 * Gui nhieu dong tin nhan den server, ket thuc bang "HET".
 */
public class Client {
    public static void main(String[] args) {
        String host = "127.0.0.1";
        int    port = 5000;
        try (Socket socket      = new Socket(host, port);
             BufferedReader in  = new BufferedReader(
                     new InputStreamReader(socket.getInputStream()));
             PrintWriter    out = new PrintWriter(socket.getOutputStream(), true);
             Scanner sc          = new Scanner(System.in)) {
            System.out.println("Server: " + in.readLine());
            while (true) {
                System.out.print("Tin nhan (HET de ket thuc): ");
                String msg = sc.nextLine();
                out.println(msg);
                if ("HET".equalsIgnoreCase(msg)) {
                    String resp = in.readLine();
                    System.out.println("Server: " + resp);
                    break;
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

### File: ClientHandler.java

**Duong dan:** `t5/tcp-tuan5-gk/b10/ClientHandler.java`

```java
package b10;
import java.io.*;
import java.net.Socket;
/*
 * Bai 10 - ClientHandler
 * Doc tin nhan den khi gap "HET", ghi vao clientX.txt
 * (uu tien package source b10 thay vi bin).
 */
public class ClientHandler extends Thread {
    private final Socket socket;
    private final int    clientId;
    public ClientHandler(Socket socket, int clientId) {
        this.socket   = socket;
        this.clientId = clientId;
    }
    @Override
    public void run() {
        try {
            File projectDir = new File(System.getProperty("user.dir"));
            File sourceDir  = new File(projectDir, "src\\b10");
            if (!sourceDir.exists()) sourceDir = new File(projectDir, "b10");
            if (!sourceDir.exists()) sourceDir.mkdirs();
            File outFile = new File(sourceDir, "client" + clientId + ".txt");
            try (BufferedReader netIn  = new BufferedReader(
                     new InputStreamReader(socket.getInputStream()));
                 PrintWriter    netOut = new PrintWriter(socket.getOutputStream(), true);
                 PrintWriter    fileOut = new PrintWriter(new FileWriter(outFile))) {
                netOut.println("Xin chao client #" + clientId
                        + "! Nhap tin nhan, go 'HET' de ket thuc.");
                String msg;
                int count = 0;
                while ((msg = netIn.readLine()) != null) {
                    if ("HET".equalsIgnoreCase(msg)) break;
                    fileOut.println(msg);
                    fileOut.flush();
                    count++;
                    System.out.println("Client #" + clientId + " gui: " + msg);
                }
                System.out.println("Client #" + clientId + " da luu " + count
                        + " tin nhan vao " + outFile.getAbsolutePath());
                netOut.println("Da luu " + count + " tin nhan vao file " + outFile.getName());
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try { socket.close(); } catch (IOException e) {}
        }
    }
}

```

### File: Server.java

**Duong dan:** `t5/tcp-tuan5-gk/b10/Server.java`

```java
package b10;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.concurrent.atomic.AtomicInteger;
/*
 * Bai 10 - Server
 * Nhan tin nhan tu nhieu client, moi client se ghi vao 1 file rieng.
 */
public class Server {
    static final int PORT = 5000;
    static AtomicInteger clientCount = new AtomicInteger(0);
    public static void main(String[] args) {
        try (ServerSocket ss = new ServerSocket(PORT)) {
            System.out.println("Message Server dang chay port " + PORT + " ...");
            while (true) {
                Socket client = ss.accept();
                int id = clientCount.incrementAndGet();
                System.out.println("Client #" + id + " ket noi: "
                        + client.getInetAddress().getHostAddress());
                new ClientHandler(client, id).start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

`<a id='bai-tap-024'></a>`

## Bài tập 24 - TUẦN 5 - `t5/tcp-tuan5-gk/b2`

**Tiêu đề bài tập:** TCP-TUẦN 5-GK – Bài Tập TCP/UDP Nâng Cao (Giữa Kì)

**Yeu cau tom tat:** Cấu trúc thư mục tcp-tuan5-gk/ ├── b1/   ← TCP: đọc số viết chữ (DataInputStream/DataOutputStream)

**Cau hoi de bai:** Viet bai TCP chat: server echo tin nhan, client co thread rieng de nhan du lieu song song voi viec nhap.

### Danh sach file

- ChatClient.java
- ChatServer.java
- ClientHandler.java

### File: ChatClient.java

**Duong dan:** `t5/tcp-tuan5-gk/b2/ChatClient.java`

```java
package b2;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.util.Scanner;

public class ChatClient {
    public static void main(String[] args) {
        String host = "127.0.0.1";
        int port = 5000;

        /*
        // Uncomment để tạo output.txt (không cần server đang chạy)
        try (java.io.PrintWriter pw = new java.io.PrintWriter(new java.io.FileWriter("output.txt"))) {
            pw.println("=== Demo b2: Chat Client-Server ===");
            pw.println("[Server] Chao ban! Go /quit de thoat.");
            pw.println("[Client] Nhap: Xin chao Server!");
            pw.println("[Server] Server: da nhan -> Xin chao Server!");
            pw.println("[Client] Nhap: Hom nay the nao?");
            pw.println("[Server] Server: da nhan -> Hom nay the nao?");
            pw.println("[Client] Nhap: /quit");
            pw.println("[Server] Bye!");
        } catch (java.io.IOException ex) { ex.printStackTrace(); }
        System.exit(0);
        */

        try (Socket socket = new Socket(host, port);
             DataInputStream in = new DataInputStream(socket.getInputStream());
             DataOutputStream out = new DataOutputStream(socket.getOutputStream());
             Scanner sc = new Scanner(System.in)) {

        
            new Thread(() -> {
                try {
                    while (true) {
                        System.out.println("\n" + in.readUTF());
                        System.out.print("Nhap: ");
                    }
                } catch (IOException e) {
                    System.out.println("\n[Mat ket noi server]");
                }
            }).start();

        
            while (true) {
                System.out.print("Nhap: ");
                String msg = sc.nextLine();

                out.writeUTF(msg);
                out.flush();

                if ("/quit".equalsIgnoreCase(msg)) break;
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

### File: ChatServer.java

**Duong dan:** `t5/tcp-tuan5-gk/b2/ChatServer.java`

```java
package b2;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class ChatServer {
    public static void main(String[] args) {
        int port = 5000;

        try (ServerSocket server = new ServerSocket(port)) {
            System.out.println("Server running on port " + port);

            while (true) {
                Socket client = server.accept();
                new ClientHandler(client).start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

### File: ClientHandler.java

**Duong dan:** `t5/tcp-tuan5-gk/b2/ClientHandler.java`

```java
package b2;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;

public class ClientHandler extends Thread {
    private final Socket socket;

    public ClientHandler(Socket socket) {
        this.socket = socket;
    }

    @Override
    public void run() {
        System.out.println("Client connected: " + socket.getInetAddress() + ":" + socket.getPort());

        try (Socket s = socket;
             DataInputStream in = new DataInputStream(s.getInputStream());
             DataOutputStream out = new DataOutputStream(s.getOutputStream())) {

        
            out.writeUTF("Chao ban! Go /quit de thoat.");
            out.flush();

            while (true) {
                String msg = in.readUTF();   
                if ("/quit".equalsIgnoreCase(msg)) {
                    out.writeUTF("Bye!");
                    out.flush();
                    break;
                }

                System.out.println("From client " + s.getPort() + ": " + msg);

            
                out.writeUTF("Server: da nhan -> " + msg);
                out.flush();
            }

        } catch (IOException e) {
     
        }

        System.out.println("Client disconnected: " + socket.getPort());
    }
}
```

`<a id='bai-tap-025'></a>`

## Bài tập 25 - TUẦN 5 - `t5/tcp-tuan5-gk/b3`

**Tiêu đề bài tập:** TCP-TUẦN 5-GK – Bài Tập TCP/UDP Nâng Cao (Giữa Kì)

**Yeu cau tom tat:** Cấu trúc thư mục tcp-tuan5-gk/ ├── b1/   ← TCP: đọc số viết chữ (DataInputStream/DataOutputStream)

**Cau hoi de bai:** Viet bai TCP chat nhu bai 2 nhung server cho phep nhan cong tu dong lenh (args).

### Danh sach file

- ChatClient.java
- ChatServer.java
- ClientHandler.java

### File: ChatClient.java

**Duong dan:** `t5/tcp-tuan5-gk/b3/ChatClient.java`

```java
package b3;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.util.Scanner;

public class ChatClient {
    public static void main(String[] args) {
        /*
        // Uncomment để tạo output.txt (không cần server đang chạy)
        try (java.io.PrintWriter pw = new java.io.PrintWriter(new java.io.FileWriter("output.txt"))) {
            pw.println("=== Demo b3: Chat Client-Server (IP/Port qua args) ===");
            pw.println("Cach dung: java b3.ChatClient <ip_server> <port>");
            pw.println("Vi du   : java b3.ChatClient 192.168.1.10 5000");
            pw.println("[Server] Chao ban! Go /quit de thoat.");
            pw.println("[Client] Nhap: Hello from remote!");
            pw.println("[Server] Server: da nhan -> Hello from remote!");
            pw.println("[Client] Nhap: /quit");
            pw.println("[Server] Bye!");
        } catch (java.io.IOException ex) { ex.printStackTrace(); }
        System.exit(0);
        */

        if (args.length < 2) {
            System.out.println("Cach dung: java b3.ChatClient <ip_server> <port>");
            System.out.println("Vi du   : java b3.ChatClient 192.168.1.10 5000");
            return;
        }

        String host = args[0];
        int port;

        try {
            port = Integer.parseInt(args[1]);
        } catch (NumberFormatException e) {
            System.out.println("Port khong hop le!");
            return;
        }

        try (Socket socket = new Socket(host, port);
             DataInputStream in = new DataInputStream(socket.getInputStream());
             DataOutputStream out = new DataOutputStream(socket.getOutputStream());
             Scanner sc = new Scanner(System.in)) {

        
            new Thread(() -> {
                try {
                    while (true) {
                        System.out.println("\n" + in.readUTF());
                        System.out.print("Nhap: ");
                    }
                } catch (IOException e) {
                    System.out.println("\n[Mat ket noi server]");
                }
            }).start();

       
            while (true) {
                System.out.print("Nhap: ");
                String msg = sc.nextLine();

                out.writeUTF(msg);
                out.flush();

                if ("/quit".equalsIgnoreCase(msg)) break;
            }

        } catch (IOException e) {
            System.out.println("Khong ket noi duoc server " + host + ":" + port);
            e.printStackTrace();
        }
    }
}
```

### File: ChatServer.java

**Duong dan:** `t5/tcp-tuan5-gk/b3/ChatServer.java`

```java
package b3;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class ChatServer {
    public static void main(String[] args) {
        int port = 5000; 

        if (args.length >= 1) {
            try {
                port = Integer.parseInt(args[0]);
            } catch (NumberFormatException e) {
                System.out.println("PORT khong hop le, dung mac dinh 5000");
                port = 5000;
            }
        }

        try (ServerSocket server = new ServerSocket(port)) {
            System.out.println("Server running on port " + port);

            while (true) {
                Socket client = server.accept();
                new ClientHandler(client).start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

### File: ClientHandler.java

**Duong dan:** `t5/tcp-tuan5-gk/b3/ClientHandler.java`

```java
package b3;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;

public class ClientHandler extends Thread {
    private final Socket socket;

    public ClientHandler(Socket socket) {
        this.socket = socket;
    }

    @Override
    public void run() {
        System.out.println("Client connected: " + socket.getInetAddress() + ":" + socket.getPort());

        try (Socket s = socket;
             DataInputStream in = new DataInputStream(s.getInputStream());
             DataOutputStream out = new DataOutputStream(s.getOutputStream())) {

            out.writeUTF("Chao ban! Go /quit de thoat.");
            out.flush();

            while (true) {
                String msg = in.readUTF();
                if ("/quit".equalsIgnoreCase(msg)) {
                    out.writeUTF("Bye!");
                    out.flush();
                    break;
                }

                System.out.println("From client " + s.getPort() + ": " + msg);

                out.writeUTF("Server: da nhan -> " + msg);
                out.flush();
            }

        } catch (IOException e) {
       
        }

        System.out.println("Client disconnected: " + socket.getPort());
    }
}
```

`<a id='bai-tap-026'></a>`

## Bài tập 26 - TUẦN 5 - `t5/tcp-tuan5-gk/b4`

**Tiêu đề bài tập:** TCP-TUẦN 5-GK – Bài Tập TCP/UDP Nâng Cao (Giữa Kì)

**Yeu cau tom tat:** Cấu trúc thư mục tcp-tuan5-gk/ ├── b1/   ← TCP: đọc số viết chữ (DataInputStream/DataOutputStream)

**Cau hoi de bai:** Viet bai TCP tra cuu ngay-gio: client gui lua chon (1 time, 2 date, 3 datetime), server tra du lieu tuong ung.

### Danh sach file

- ClientHandler.java
- DateTimeClient.java
- DateTimeServer.java

### File: ClientHandler.java

**Duong dan:** `t5/tcp-tuan5-gk/b4/ClientHandler.java`

```java
package b4;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;

public class ClientHandler extends Thread {
    private final Socket socket;

    public ClientHandler(Socket socket) {
        this.socket = socket;
    }

    private String handle(int choice) {
        switch (choice) {
            case 1: 
                return "Time: " + LocalTime.now();
            case 2: 
                return "Date: " + LocalDate.now();
            case 3: 
                return "Date&Time: " + LocalDateTime.now();
            default:
                return "Lua chon khong hop le!";
        }
    }

    @Override
    public void run() {
        try (Socket s = socket;
             DataInputStream in = new DataInputStream(s.getInputStream());
             DataOutputStream out = new DataOutputStream(s.getOutputStream())) {

        
            out.writeUTF("MENU:\n1. Time\n2. Date\n3. Date & Time\nNhap 1/2/3 (hoac 0 de thoat)");
            out.flush();

            while (true) {
                int choice = in.readInt(); 
                if (choice == 0) {
                    out.writeUTF("Bye!");
                    out.flush();
                    break;
                }

                String resp = handle(choice);
                out.writeUTF(resp);
                out.flush();
            }

        } catch (IOException e) {
       
        }
    }
}
```

### File: DateTimeClient.java

**Duong dan:** `t5/tcp-tuan5-gk/b4/DateTimeClient.java`

```java
package b4;

import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.util.Scanner;

public class DateTimeClient {
    public static void main(String[] args) {
        /*
        // Uncomment để tạo output.txt (không cần server đang chạy)
        try (java.io.PrintWriter pw = new java.io.PrintWriter(new java.io.FileWriter("output.txt"))) {
            pw.println("=== Demo b4: DateTime Client-Server ===");
            pw.println("[Server] MENU:\n1. Time\n2. Date\n3. Date & Time\nNhap 1/2/3 (hoac 0 de thoat)");
            pw.println("[Client] Chon: 1");
            pw.println("[Server] Time: " + java.time.LocalTime.now());
            pw.println("[Client] Chon: 2");
            pw.println("[Server] Date: " + java.time.LocalDate.now());
            pw.println("[Client] Chon: 3");
            pw.println("[Server] Date&Time: " + java.time.LocalDateTime.now());
            pw.println("[Client] Chon: 0");
            pw.println("[Server] Bye!");
        } catch (java.io.IOException ex) { ex.printStackTrace(); }
        System.exit(0);
        */

        try (Scanner sc = new Scanner(System.in)) {
            System.out.print("Nhap IP server: ");
            String host = sc.nextLine().trim();
            if (host.isEmpty()) host = "127.0.0.1";

            System.out.print("Nhap port: ");
            int port = Integer.parseInt(sc.nextLine().trim());

            try (Socket socket = new Socket(host, port);
                 DataInputStream in = new DataInputStream(socket.getInputStream());
                 DataOutputStream out = new DataOutputStream(socket.getOutputStream())) {

           
                System.out.println(in.readUTF());

                while (true) {
                    System.out.print("Chon: ");
                    int choice = Integer.parseInt(sc.nextLine().trim());

                    out.writeInt(choice);
                    out.flush();

                    String resp = in.readUTF();
                    System.out.println("Server: " + resp);

                    if (choice == 0) break;
                }

            } catch (IOException e) {
                System.out.println("Khong ket noi duoc server!");
                e.printStackTrace();
            }
        }
    }
}
```

### File: DateTimeServer.java

**Duong dan:** `t5/tcp-tuan5-gk/b4/DateTimeServer.java`

```java
package b4;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class DateTimeServer {
    public static void main(String[] args) {
        int port = 5000; 

        try (ServerSocket server = new ServerSocket(port)) {
            System.out.println("DateTimeServer running on port " + port);

            while (true) {
                Socket client = server.accept();
                new ClientHandler(client).start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

`<a id='bai-tap-027'></a>`

## Bài tập 27 - TUẦN 5 - `t5/tcp-tuan5-gk/b5`

**Tiêu đề bài tập:** TCP-TUẦN 5-GK – Bài Tập TCP/UDP Nâng Cao (Giữa Kì)

**Yeu cau tom tat:** Cấu trúc thư mục tcp-tuan5-gk/ ├── b1/   ← TCP: đọc số viết chữ (DataInputStream/DataOutputStream)

**Cau hoi de bai:** Viet bai UDP tra cuu ngay-gio tuong tu bai 4, su dung DatagramSocket/DatagramPacket de gui-nhan du lieu.

### Danh sach file

- DateTimeService.java
- DateTimeUDPClient.java
- DateTimeUDPServer.java

### File: DateTimeService.java

**Duong dan:** `t5/tcp-tuan5-gk/b5/DateTimeService.java`

```java
package b5;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;

public class DateTimeService {

   
    public static String handle(String req) {
        if (req == null) return "Nhap 1(Time) / 2(Date) / 3(Date&Time)";

        String s = req.trim();

        switch (s) {
            case "1":
            case "Time":
            case "time":
                return "Time: " + LocalTime.now();

            case "2":
            case "Date":
            case "date":
                return "Date: " + LocalDate.now();

            case "3":
            case "Date & Time":
            case "DateTime":
            case "datetime":
                return "Date&Time: " + LocalDateTime.now();

            default:
                return "Nhap 1(Time) / 2(Date) / 3(Date&Time)";
        }
    }
}
```

### File: DateTimeUDPClient.java

**Duong dan:** `t5/tcp-tuan5-gk/b5/DateTimeUDPClient.java`

```java
package b5;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.nio.charset.StandardCharsets;
import java.util.Scanner;

public class DateTimeUDPClient {
    public static void main(String[] args) {
        /*
        // Uncomment để tạo output.txt (không cần server đang chạy)
        try (java.io.PrintWriter pw = new java.io.PrintWriter(new java.io.FileWriter("output.txt"))) {
            pw.println("=== Demo b5: DateTime UDP Client-Server ===");
            pw.println("[Client] Chon: 1 (Time)");
            pw.println("[Server] Time: " + java.time.LocalTime.now());
            pw.println("[Client] Chon: 2 (Date)");
            pw.println("[Server] Date: " + java.time.LocalDate.now());
            pw.println("[Client] Chon: 3 (Date & Time)");
            pw.println("[Server] Date&Time: " + java.time.LocalDateTime.now());
        } catch (java.io.IOException ex) { ex.printStackTrace(); }
        System.exit(0);
        */

        try (Scanner sc = new Scanner(System.in);
             DatagramSocket socket = new DatagramSocket()) {

            System.out.print("Nhap IP server: ");
            String host = sc.nextLine().trim();
            if (host.isEmpty()) host = "127.0.0.1";

            System.out.print("Nhap port: ");
            int port = Integer.parseInt(sc.nextLine().trim());

            InetAddress serverAddr = InetAddress.getByName(host);

            while (true) {
                System.out.println("\n1. Time\n2. Date\n3. Date & Time\n0. Thoat");
                System.out.print("Chon: ");
                String choice = sc.nextLine().trim();

                if ("0".equals(choice)) break;

                byte[] data = choice.getBytes(StandardCharsets.UTF_8);
                DatagramPacket req = new DatagramPacket(data, data.length, serverAddr, port);
                socket.send(req);

                byte[] buf = new byte[1024];
                DatagramPacket resp = new DatagramPacket(buf, buf.length);
                socket.receive(resp);

                String text = new String(resp.getData(), resp.getOffset(), resp.getLength(), StandardCharsets.UTF_8);
                System.out.println("Server: " + text);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

### File: DateTimeUDPServer.java

**Duong dan:** `t5/tcp-tuan5-gk/b5/DateTimeUDPServer.java`

```java
package b5;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.nio.charset.StandardCharsets;

public class DateTimeUDPServer {
    public static void main(String[] args) {
        int port = 5000;

        try (DatagramSocket socket = new DatagramSocket(port)) {
            System.out.println("UDP Server running on port " + port);

            byte[] buf = new byte[1024];

            while (true) {
                DatagramPacket req = new DatagramPacket(buf, buf.length);
                socket.receive(req);

                String msg = new String(
                        req.getData(), req.getOffset(), req.getLength(),
                        StandardCharsets.UTF_8
                );

                String respText = DateTimeService.handle(msg);

                byte[] out = respText.getBytes(StandardCharsets.UTF_8);
                DatagramPacket resp = new DatagramPacket(out, out.length, req.getAddress(), req.getPort());
                socket.send(resp);
            }

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

`<a id='bai-tap-028'></a>`

## Bài tập 28 - TUẦN 5 - `t5/tcp-tuan5-gk/b6`

**Tiêu đề bài tập:** TCP-TUẦN 5-GK – Bài Tập TCP/UDP Nâng Cao (Giữa Kì)

**Yeu cau tom tat:** Cấu trúc thư mục tcp-tuan5-gk/ ├── b1/   ← TCP: đọc số viết chữ (DataInputStream/DataOutputStream)

**Cau hoi de bai:** Viet bai tinh toan chuoi so (co TCP va UDP): client gui choice va n, server tinh theo cong thuc quy dinh va tra ket qua.

### Danh sach file

- CalcService.java
- TcpCalcClient.java
- TcpCalcServer.java
- TcpClientHandler.java
- UdpCalcClient.java
- UdpCalcServer.java

### File: CalcService.java

**Duong dan:** `t5/tcp-tuan5-gk/b6/CalcService.java`

```java
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
```

### File: TcpCalcClient.java

**Duong dan:** `t5/tcp-tuan5-gk/b6/TcpCalcClient.java`

```java
package b6;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.util.Scanner;
/*
 * Bai 6 TCP - Client
 * Nhap menu tinh toan, gui choice + n, nhan ket qua tu server.
 */
public class TcpCalcClient {
    public static void main(String[] args) {
        String host = "127.0.0.1";
        int port = 5000;
        try (Socket socket = new Socket(host, port);
             DataInputStream in = new DataInputStream(socket.getInputStream());
             DataOutputStream out = new DataOutputStream(socket.getOutputStream());
             Scanner sc = new Scanner(System.in)) {
            while (true) {
                System.out.println("\nChon phep tinh:");
                System.out.println("1) Tong 1+3+...+(2n+1)");
                System.out.println("2) Tong 1*2 + 2*3 + ... + n*(n+1)");
                System.out.println("3) 1-2+3-4+...+(2n+1)");
                System.out.println("0) Thoat");
                System.out.print("Choice: ");
                int choice = Integer.parseInt(sc.nextLine().trim());
                out.writeInt(choice);
                if (choice == 0) {
                    out.flush();
                    break;
                }
                System.out.print("Nhap n: ");
                int n = Integer.parseInt(sc.nextLine().trim());
                out.writeInt(n);
                out.flush();
                long result = in.readLong();
                if (result == Long.MIN_VALUE) {
                    System.out.println("Server: Tham so/choice khong hop le!");
                } else {
                    System.out.println("Ket qua = " + result);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

### File: TcpCalcServer.java

**Duong dan:** `t5/tcp-tuan5-gk/b6/TcpCalcServer.java`

```java
package b6;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
/*
 * Bai 6 TCP - Server
 * Lang nghe ket noi va tao 1 thread xu ly cho moi client.
 */
public class TcpCalcServer {
    public static void main(String[] args) {
        int port = 5000;
        try (ServerSocket server = new ServerSocket(port)) {
            System.out.println("TCP Calc Server running on port " + port);
            while (true) {
                Socket client = server.accept();
                new TcpClientHandler(client).start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

### File: TcpClientHandler.java

**Duong dan:** `t5/tcp-tuan5-gk/b6/TcpClientHandler.java`

```java
package b6;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
/*
 * Bai 6 TCP - ClientHandler
 * Nhan choice + n tu client, tinh toan va tra ket qua long.
 */
public class TcpClientHandler extends Thread {
    private final Socket socket;
    public TcpClientHandler(Socket socket) {
        this.socket = socket;
    }
    @Override
    public void run() {
        try (Socket s = socket;
             DataInputStream in = new DataInputStream(s.getInputStream());
             DataOutputStream out = new DataOutputStream(s.getOutputStream())) {
            while (true) {
                int choice;
                try {
                    choice = in.readInt();
                } catch (IOException e) {
                    break; 
                }
                if (choice == 0) { 
                    out.writeLong(0);
                    out.flush();
                    break;
                }
                int n = in.readInt();
                try {
                    long result = CalcService.calc(choice, n);
                    out.writeLong(result);
                } catch (IllegalArgumentException ex) {
                    out.writeLong(Long.MIN_VALUE);
                }
                out.flush();
            }
        } catch (IOException e) {
        }
    }
}
```

### File: UdpCalcClient.java

**Duong dan:** `t5/tcp-tuan5-gk/b6/UdpCalcClient.java`

```java
package b6;
import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.nio.ByteBuffer;
import java.util.Scanner;
/*
 * Bai 6 UDP - Client
 * Gui yeu cau tinh toan bang UDP va in ket qua tra ve.
 */
public class UdpCalcClient {
    public static void main(String[] args) {
        String host = "127.0.0.1";
        int port = 6000;
        try (DatagramSocket socket = new DatagramSocket();
             Scanner sc = new Scanner(System.in)) {
            InetAddress server = InetAddress.getByName(host);
            while (true) {
                System.out.println("\nChon phep tinh:");
                System.out.println("1) Tong 1+3+...+(2n+1)");
                System.out.println("2) Tong 1*2 + 2*3 + ... + n*(n+1)");
                System.out.println("3) 1-2+3-4+...+(2n+1)");
                System.out.println("0) Thoat");
                System.out.print("Choice: ");
                int choice = Integer.parseInt(sc.nextLine().trim());
                if (choice == 0) break;
                System.out.print("Nhap n: ");
                int n = Integer.parseInt(sc.nextLine().trim());
                byte[] data = ByteBuffer.allocate(8).putInt(choice).putInt(n).array();
                DatagramPacket req = new DatagramPacket(data, data.length, server, port);
                socket.send(req);
                byte[] buf = new byte[8];
                DatagramPacket resp = new DatagramPacket(buf, buf.length);
                socket.receive(resp);
                long result = ByteBuffer.wrap(resp.getData(), 0, resp.getLength()).getLong();
                if (result == Long.MIN_VALUE) {
                    System.out.println("Server: Tham so/choice khong hop le!");
                } else {
                    System.out.println("Ket qua = " + result);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

### File: UdpCalcServer.java

**Duong dan:** `t5/tcp-tuan5-gk/b6/UdpCalcServer.java`

```java
package b6;
import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.nio.ByteBuffer;
/*
 * Bai 6 UDP - Server
 * Nhan datagram choice+n, tinh toan va gui ket qua ve client.
 */
public class UdpCalcServer {
    public static void main(String[] args) {
        int port = 6000;
        try (DatagramSocket socket = new DatagramSocket(port)) {
            System.out.println("UDP Calc Server running on port " + port);
            byte[] buf = new byte[8]; 
            while (true) {
                DatagramPacket req = new DatagramPacket(buf, buf.length);
                socket.receive(req);
                ByteBuffer bb = ByteBuffer.wrap(req.getData(), 0, req.getLength());
                int choice = bb.getInt();
                int n = bb.getInt();
                long result;
                try {
                    result = CalcService.calc(choice, n);
                } catch (IllegalArgumentException ex) {
                    result = Long.MIN_VALUE;
                }
                byte[] out = ByteBuffer.allocate(8).putLong(result).array();
                DatagramPacket resp = new DatagramPacket(out, out.length, req.getAddress(), req.getPort());
                socket.send(resp);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

`<a id='bai-tap-029'></a>`

## Bài tập 29 - TUẦN 5 - `t5/tcp-tuan5-gk/b7`

**Tiêu đề bài tập:** TCP-TUẦN 5-GK – Bài Tập TCP/UDP Nâng Cao (Giữa Kì)

**Yeu cau tom tat:** Cấu trúc thư mục tcp-tuan5-gk/ ├── b1/   ← TCP: đọc số viết chữ (DataInputStream/DataOutputStream)

**Cau hoi de bai:** Viet bai TCP gui file: client gui ten file + duong dan + kich thuoc + du lieu, server nhan va luu file roi phan hoi trang thai.

### Danh sach file

- Client.java
- ClientHandler.java
- Server.java
- UdpFileClient.java
- UdpFileServer.java

### File: Client.java

**Duong dan:** `t5/tcp-tuan5-gk/b7/Client.java`

```java
package b7;
import java.io.*;
import java.net.Socket;
import java.util.Scanner;
/*
 * Bai 7 TCP - Client
 * Chon file can gui va duong dan luu tren server, sau do truyen file.
 */
public class Client {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.print("Nhap dia chi server (Enter = 127.0.0.1): ");
            String host = sc.nextLine().trim();
            if (host.isEmpty()) host = "127.0.0.1";
            System.out.print("Nhap port: ");
            int port = Integer.parseInt(sc.nextLine().trim());
            System.out.print("Nhap duong dan file can truyen: ");
            String filePath = sc.nextLine().trim();
            System.out.print("Nhap duong dan luu tren server: ");
            String savePath = sc.nextLine().trim();
            File file = new File(filePath);
            if (!file.exists() || !file.isFile()) {
                System.out.println("File khong ton tai: " + filePath);
                return;
            }
            try (Socket socket         = new Socket(host, port);
                 DataOutputStream out  = new DataOutputStream(socket.getOutputStream());
                 DataInputStream  in   = new DataInputStream(socket.getInputStream());
                 FileInputStream  fis  = new FileInputStream(file)) {
                out.writeUTF(file.getName());
                out.writeUTF(savePath);
                out.writeLong(file.length());
                System.out.println("Dang truyen file " + file.getName()
                        + " (" + file.length() + " bytes)...");
                byte[] buf = new byte[4096];
                int n;
                while ((n = fis.read(buf)) != -1) {
                    out.write(buf, 0, n);
                }
                out.flush();
                String resp = in.readUTF();
                System.out.println("Server: " + resp);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
```

### File: ClientHandler.java

**Duong dan:** `t5/tcp-tuan5-gk/b7/ClientHandler.java`

```java
package b7;
import java.io.*;
import java.net.Socket;
/*
 * Bai 7 TCP - ClientHandler
 * Nhan ten file, duong dan luu, kich thuoc va du lieu file.
 * Sau khi luu xong se gui thong bao OK ve client.
 */
public class ClientHandler extends Thread {
    private final Socket socket;
    public ClientHandler(Socket socket) {
        this.socket = socket;
    }
    @Override
    public void run() {
        try (DataInputStream  in  = new DataInputStream(socket.getInputStream());
             DataOutputStream out = new DataOutputStream(socket.getOutputStream())) {
            String fileName = in.readUTF();   
            String savePath = in.readUTF();   
            long   fileSize = in.readLong();  
            File dir = new File(savePath);
            if (!dir.exists()) dir.mkdirs();
            File dest = new File(dir, fileName);
            try (FileOutputStream fos = new FileOutputStream(dest)) {
                byte[] buf = new byte[4096];
                long remaining = fileSize;
                while (remaining > 0) {
                    int toRead = (int) Math.min(buf.length, remaining);
                    int n = in.read(buf, 0, toRead);
                    if (n < 0) break;
                    fos.write(buf, 0, n);
                    remaining -= n;
                }
            }
            System.out.println("Da luu file: " + dest.getAbsolutePath()
                    + " (" + fileSize + " bytes)");
            out.writeUTF("OK: Da luu " + dest.getAbsolutePath());
            out.flush();
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try { socket.close(); } catch (IOException e) {}
        }
    }
}
```

### File: Server.java

**Duong dan:** `t5/tcp-tuan5-gk/b7/Server.java`

```java
package b7;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
/*
 * Bai 7 TCP - Server
 * Nhan file tu nhieu client, moi ket noi mot ClientHandler.
 */
public class Server {
    static final int PORT = 5000;
    public static void main(String[] args) {
        try (ServerSocket ss = new ServerSocket(PORT)) {
            System.out.println("TCP File Server dang chay port " + PORT + " ...");
            while (true) {
                Socket client = ss.accept();
                System.out.println("Client ket noi: " + client.getInetAddress().getHostAddress());
                new ClientHandler(client).start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

### File: UdpFileClient.java

**Duong dan:** `t5/tcp-tuan5-gk/b7/UdpFileClient.java`

```java
package b7;
import java.io.*;
import java.net.*;
import java.util.Scanner;
/*
 * Bai 7 UDP - Client
 * Cat file thanh chunk, gui theo thu tu va doi ACK tu server.
 */
public class UdpFileClient {
    static final int CHUNK_SIZE = 60000;
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.print("Nhap dia chi server (Enter = 127.0.0.1): ");
            String host = sc.nextLine().trim();
            if (host.isEmpty()) host = "127.0.0.1";
            System.out.print("Nhap port UDP server: ");
            int port = Integer.parseInt(sc.nextLine().trim());
            System.out.print("Nhap duong dan file can truyen: ");
            String filePath = sc.nextLine().trim();
            System.out.print("Nhap duong dan luu tren server: ");
            String savePath = sc.nextLine().trim();
            File file = new File(filePath);
            if (!file.exists() || !file.isFile()) {
                System.out.println("File khong ton tai!");
                return;
            }
            byte[] fileBytes;
            try (FileInputStream fis = new FileInputStream(file)) {
                fileBytes = fis.readAllBytes();
            }
            int totalChunks = (int) Math.ceil((double) fileBytes.length / CHUNK_SIZE);
            if (totalChunks == 0) totalChunks = 1; 
            InetAddress addr = InetAddress.getByName(host);
            try (DatagramSocket socket = new DatagramSocket()) {
                socket.setSoTimeout(5000); 
                String header = "HEADER|" + file.getName() + "|" + savePath + "|" + totalChunks;
                sendStr(socket, header, addr, port);
                String ack = recvStr(socket, 1024);
                if (!"READY".equals(ack)) {
                    System.out.println("Server khong san sang: " + ack); return;
                }
                System.out.println("Server READY. Bat dau truyen " + totalChunks + " chunk...");
                for (int seq = 0; seq < totalChunks; seq++) {
                    int offset  = seq * CHUNK_SIZE;
                    int dataLen = Math.min(CHUNK_SIZE, fileBytes.length - offset);
                    if (dataLen <= 0) dataLen = 0;
                    byte[] pktData = new byte[4 + dataLen];
                    pktData[0] = (byte) (seq >> 24);
                    pktData[1] = (byte) (seq >> 16);
                    pktData[2] = (byte) (seq >> 8);
                    pktData[3] = (byte)  seq;
                    if (dataLen > 0)
                        System.arraycopy(fileBytes, offset, pktData, 4, dataLen);
                    socket.send(new DatagramPacket(pktData, pktData.length, addr, port));
                    System.out.println("Truyen chunk " + seq + " (" + dataLen + " bytes)...");
                    String resp = recvStr(socket, 32);
                    System.out.println("Server: " + resp);
                }
                sendStr(socket, "END", addr, port);
                String result = recvStr(socket, 512);
                System.out.println("Server: " + result);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private static void sendStr(DatagramSocket s, String msg,
                                InetAddress addr, int port) throws IOException {
        byte[] data = msg.getBytes("UTF-8");
        s.send(new DatagramPacket(data, data.length, addr, port));
    }
    private static String recvStr(DatagramSocket s, int bufSize) throws IOException {
        byte[] buf = new byte[bufSize];
        DatagramPacket pkt = new DatagramPacket(buf, buf.length);
        s.receive(pkt);
        return new String(pkt.getData(), 0, pkt.getLength(), "UTF-8");
    }
}
```

### File: UdpFileServer.java

**Duong dan:** `t5/tcp-tuan5-gk/b7/UdpFileServer.java`

```java
package b7;
import java.io.*;
import java.net.*;
/*
 * Bai 7 UDP - Server
 * Nhan header, nhan tung chunk co so thu tu, ACK tung chunk,
 * ghep lai va ghi ra file dich.
 */
public class UdpFileServer {
    static final int PORT    = 5001;
    static final int MAXDATA = 60000; 
    public static void main(String[] args) throws IOException {
        try (DatagramSocket socket = new DatagramSocket(PORT)) {
            System.out.println("UDP File Server dang chay port " + PORT + " ...");
            byte[] buf = new byte[MAXDATA + 4];
            while (true) {
                DatagramPacket pkt = new DatagramPacket(buf, buf.length);
                socket.receive(pkt);
                String header = new String(pkt.getData(), 0, pkt.getLength(), "UTF-8");
                System.out.println("Header: " + header);
                if (!header.startsWith("HEADER|")) continue;
                String[] parts   = header.split("\\|", 4);
                String fileName  = parts[1];
                String savePath  = parts[2];
                int    totalChunks = Integer.parseInt(parts[3].trim());
                InetAddress clientAddr = pkt.getAddress();
                int         clientPort = pkt.getPort();
                send(socket, "READY", clientAddr, clientPort);
                File dir = new File(savePath);
                if (!dir.exists()) dir.mkdirs();
                File dest = new File(dir, fileName);
                byte[][] chunks = new byte[totalChunks][];
                int[] sizes = new int[totalChunks];
                for (int i = 0; i < totalChunks; i++) {
                    pkt = new DatagramPacket(buf, buf.length);
                    socket.receive(pkt);
                    int seq = ((buf[0] & 0xFF) << 24) | ((buf[1] & 0xFF) << 16)
                            | ((buf[2] & 0xFF) << 8)  |  (buf[3] & 0xFF);
                    int dataLen = pkt.getLength() - 4;
                    chunks[seq] = new byte[dataLen];
                    System.arraycopy(buf, 4, chunks[seq], 0, dataLen);
                    sizes[seq] = dataLen;
                    send(socket, "ACK:" + seq, clientAddr, clientPort);
                }
                pkt = new DatagramPacket(buf, buf.length);
                socket.receive(pkt);
                try (FileOutputStream fos = new FileOutputStream(dest)) {
                    for (int i = 0; i < totalChunks; i++) {
                        fos.write(chunks[i], 0, sizes[i]);
                    }
                }
                System.out.println("Da luu: " + dest.getAbsolutePath());
                send(socket, "OK: Da luu " + dest.getAbsolutePath(), clientAddr, clientPort);
            }
        }
    }
    private static void send(DatagramSocket s, String msg,
                             InetAddress addr, int port) throws IOException {
        byte[] data = msg.getBytes("UTF-8");
        s.send(new DatagramPacket(data, data.length, addr, port));
    }
}
```

`<a id='bai-tap-030'></a>`

## Bài tập 30 - TUẦN 5 - `t5/tcp-tuan5-gk/b8`

**Tiêu đề bài tập:** TCP-TUẦN 5-GK – Bài Tập TCP/UDP Nâng Cao (Giữa Kì)

**Yeu cau tom tat:** Cấu trúc thư mục tcp-tuan5-gk/ ├── b1/   ← TCP: đọc số viết chữ (DataInputStream/DataOutputStream)

**Cau hoi de bai:** Viet bai TCP may tinh don gian: client gui bieu thuc dang "OP so1 so2", server parse va tinh + - * /, xu ly ca loi.

### Danh sach file

- Client.java
- ClientHandler.java
- Server.java

### File: Client.java

**Duong dan:** `t5/tcp-tuan5-gk/b8/Client.java`

```java
package b8;
import java.io.*;
import java.net.Socket;
import java.util.Scanner;
/*
 * Bai 8 - Client
 * Nguoi dung nhap dang 100+200, client doi sang "+ 100 200" de gui.
 */
public class Client {
    public static void main(String[] args) {
        String host = "127.0.0.1";
        int    port = 5000;
        try (Socket socket      = new Socket(host, port);
             BufferedReader in  = new BufferedReader(
                     new InputStreamReader(socket.getInputStream()));
             PrintWriter    out = new PrintWriter(socket.getOutputStream(), true);
             Scanner sc         = new Scanner(System.in)) {
            System.out.println("Ket noi server " + host + ":" + port + " thanh cong.");
            System.out.println("Nhap phep tinh (vi du: 100+200) hoac 'exit' de thoat.");
            while (true) {
                System.out.print("Nhap: ");
                String input = sc.nextLine().trim();
                if (input.equalsIgnoreCase("exit")) {
                    out.println("exit");
                    System.out.println("Server: " + in.readLine());
                    break;
                }
                String msg = parseExpr(input);
                if (msg == null) {
                    System.out.println("Dinh dang sai! Vd: 100+200 | 50-8 | 6*7 | 10/4");
                    continue;
                }
                out.println(msg);   
                String resp = in.readLine();
                System.out.println("Ket qua: " + resp);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    private static String parseExpr(String s) {
        char[] ops = {'+', '-', '*', '/'};
        for (char op : ops) {
            int idx = (op == '-') ? s.indexOf('-', 1) : s.indexOf(op);
            if (idx > 0) {
                String a = s.substring(0, idx).trim();
                String b = s.substring(idx + 1).trim();
                if (!a.isEmpty() && !b.isEmpty())
                    return op + " " + a + " " + b;
            }
        }
        return null;
    }
}
```

### File: ClientHandler.java

**Duong dan:** `t5/tcp-tuan5-gk/b8/ClientHandler.java`

```java
package b8;
import java.io.*;
import java.net.Socket;
/*
 * Bai 8 - ClientHandler
 * Parse thong diep, tinh + - * /, xu ly loi va tra ket qua.
 */
public class ClientHandler extends Thread {
    private final Socket socket;
    public ClientHandler(Socket socket) {
        this.socket = socket;
    }
    @Override
    public void run() {
        try (BufferedReader reader = new BufferedReader(
                 new InputStreamReader(socket.getInputStream()));
             PrintWriter writer = new PrintWriter(socket.getOutputStream(), true)) {
            String msg;
            while ((msg = reader.readLine()) != null) {
                msg = msg.trim();
                if (msg.equalsIgnoreCase("exit")) {
                    writer.println("Bye!");
                    break;
                }
                String result = calculate(msg);
                System.out.println("Nhan: [" + msg + "]  =>  Tra ve: " + result);
                writer.println(result);
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try { socket.close(); } catch (IOException e) {}
        }
        System.out.println("Client ngat ket noi: " + socket.getInetAddress());
    }
    private String calculate(String expr) {
        String[] parts = expr.split("\\s+");
        if (parts.length != 3) return "Loi: dinh dang phai la 'OP so1 so2'";
        char op;
        double a, b;
        try {
            op = parts[0].charAt(0);
            a  = Double.parseDouble(parts[1]);
            b  = Double.parseDouble(parts[2]);
        } catch (NumberFormatException e) {
            return "Loi: Operand khong phai so";
        }
        switch (op) {
            case '+': return format(a + b);
            case '-': return format(a - b);
            case '*': return format(a * b);
            case '/':
                if (b == 0) return "Loi: Chia cho 0";
                return format(a / b);
            default:
                return "Loi: OP phai la + - * /";
        }
    }
    private String format(double v) {
        return (v == Math.floor(v) && !Double.isInfinite(v))
                ? String.valueOf((long) v)
                : String.format("%.2f", v);
    }
}
```

### File: Server.java

**Duong dan:** `t5/tcp-tuan5-gk/b8/Server.java`

```java
package b8;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
/*
 * Bai 8 - Server
 * Nhan bieu thuc dang "OP so1 so2" va tra ve ket qua.
 */
public class Server {
    static final int PORT = 5000;
    public static void main(String[] args) {
        try (ServerSocket ss = new ServerSocket(PORT)) {
            System.out.println("Calc Server dang chay port " + PORT + " ...");
            while (true) {
                Socket client = ss.accept();
                System.out.println("Client ket noi: " + client.getInetAddress().getHostAddress());
                new ClientHandler(client).start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

`<a id='bai-tap-031'></a>`

## Bài tập 31 - TUẦN 5 - `t5/tcp-tuan5-gk/b9`

**Tiêu đề bài tập:** TCP-TUẦN 5-GK – Bài Tập TCP/UDP Nâng Cao (Giữa Kì)

**Yeu cau tom tat:** Cấu trúc thư mục tcp-tuan5-gk/ ├── b1/   ← TCP: đọc số viết chữ (DataInputStream/DataOutputStream)

**Cau hoi de bai:** Viet bai TCP doc file tren server: client gui ten file, server doc noi dung file va gui tung dong cho client den khi ket thuc.

### Danh sach file

- Client.java
- ClientHandler.java
- data.txt
- Server.java

### File: Client.java

**Duong dan:** `t5/tcp-tuan5-gk/b9/Client.java`

```java
package b9;
import java.io.*;
import java.net.Socket;
import java.util.Scanner;
/*
 * Bai 9 - Client
 * Gui ten file can doc va hien thi noi dung server tra ve.
 */
public class Client {
    public static void main(String[] args) {
        String host = "127.0.0.1";
        int    port = 5000;
        try (Scanner sc = new Scanner(System.in)) {
            System.out.print("Nhap IP server (Enter = 127.0.0.1): ");
            String h = sc.nextLine().trim();
            if (!h.isEmpty()) host = h;
            while (true) {
                System.out.print("Nhap ten file (exit de thoat): ");
                String fileName = sc.nextLine().trim();
                if (fileName.equalsIgnoreCase("exit")) break;
                try (Socket socket      = new Socket(host, port);
                     PrintWriter netOut = new PrintWriter(socket.getOutputStream(), true);
                     BufferedReader netIn = new BufferedReader(
                             new InputStreamReader(socket.getInputStream()))) {
                    netOut.println(fileName);
                    System.out.println("--- Noi dung file ---");
                    String line;
                    while ((line = netIn.readLine()) != null) {
                        if ("##END##".equals(line)) break;
                        System.out.println(line);
                    }
                    System.out.println("---------------------");
                } catch (IOException e) {
                    System.out.println("Loi ket noi: " + e.getMessage());
                }
            }
        }
    }
}
```

### File: ClientHandler.java

**Duong dan:** `t5/tcp-tuan5-gk/b9/ClientHandler.java`

```java
package b9;
import java.io.*;
import java.net.Socket;
/*
 * Bai 9 - ClientHandler
 * Nhan ten file tu client, doc file trong thu muc package b9,
 * gui tung dong noi dung va ket thuc bang ##END##.
 */
public class ClientHandler extends Thread {
    private final Socket socket;
    public ClientHandler(Socket socket) {
        this.socket = socket;
    }
    @Override
    public void run() {
        try (BufferedReader netIn  = new BufferedReader(
                 new InputStreamReader(socket.getInputStream()));
             PrintWriter    netOut = new PrintWriter(socket.getOutputStream(), true)) {
            String fileName = netIn.readLine();
            if (fileName == null || fileName.trim().isEmpty()) return;
            fileName = fileName.trim();
            System.out.println("Client yeu cau file: " + fileName);
            File dir  = new File(getClass().getResource("").toURI());
            File file = new File(dir, fileName);
            if (!file.exists() || !file.isFile()) {
                netOut.println("ERROR: File khong ton tai: " + file.getAbsolutePath());
                return;
            }
            try (BufferedReader fileIn = new BufferedReader(new FileReader(file))) {
                String line;
                while ((line = fileIn.readLine()) != null) {
                    netOut.println(line);
                }
            }
            netOut.println("##END##");
            System.out.println("Da gui xong file: " + file.getAbsolutePath());
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            try { socket.close(); } catch (IOException e) {}
        }
    }
}
```

### File: data.txt

**Duong dan:** `t5/tcp-tuan5-gk/b9/data.txt`

```text
Dong 1: Xin chao! Day la noi dung file data.txt tren server.
Dong 2: File nay duoc doc va gui toan bo den client khi co yeu cau.
Dong 3: Server ho tro nhieu client ket noi cung luc (moi ket noi 1 thread).
Dong 4: Client chi can nhap ten file, server se tim va gui noi dung.
Dong 5: Het file data.txt.

```

### File: Server.java

**Duong dan:** `t5/tcp-tuan5-gk/b9/Server.java`

```java
package b9;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
/*
 * Bai 9 - Server
 * Cho nhieu client doc noi dung file duoc luu trong package b9.
 */
public class Server {
    static final int PORT = 5000;
    public static void main(String[] args) {
        try (ServerSocket ss = new ServerSocket(PORT)) {
            System.out.println("File Server dang chay port " + PORT + " ...");
            System.out.println("Thu muc phuc vu: " + System.getProperty("user.dir"));
            while (true) {
                Socket client = ss.accept();
                System.out.println("Client ket noi: " + client.getInetAddress().getHostAddress());
                new ClientHandler(client).start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

`<a id='bai-tap-032'></a>`

## Bài tập 32 - TUẦN 6 - `t6-lt`

**Tiêu đề bài tập:** TUẦN 6 - Tài liệu tổng hợp RMI (tham khảo)

**Yeu cau tom tat:** On tap luong xu ly RMI: dinh nghia Remote Interface, cai dat service, dang ky Registry, client lookup va goi ham tu xa.

**Cau hoi de bai:** Tai lieu nay dong vai tro de cuong/mau tham khao cho cac bai RMI. Muc tieu la hieu cau truc Client-Server-RMI va cach truyen tham so/nhan ket qua qua mang.

### Danh sach file

- rmiClient.java
- rmiServer.java
- xulychuoi_impl.java
- xulychuoi_intf.java

### File: rmiClient.java

**Duong dan:** `t6-lt/rmiClient.java`

```java
import java.rmi.Naming;

public class rmiClient {
    public static void main(String[] args) {
        try {
            phepCong_intf stub = (phepCong_intf)Naming.lookup("rmi://localhost:1100/congService");
            int result_int = stub.tong2songuyen(5, 5);
            double result_double = stub.tong2sothuc(7.7, 3.3);
            int result_3_int = stub.tong3songuyen(1, 1, 1);
        
            System.out.println(result_int);
            System.out.println(result_double);
            System.out.println(result_3_int);
        
            xulychuoi_intf stub2 = (xulychuoi_intf)Naming.lookup("rmi://localhost:1100/chuoiService");
            String result_str = stub2.noi2chuoi("phat trien", " ht th");
            System.out.println(result_str);
        
        } catch (Exception e) {
        }
    }
}
```

### File: rmiServer.java

**Duong dan:** `t6-lt/rmiServer.java`

```java
import java.net.MalformedURLException;
import java.rmi.AlreadyBoundException;
import java.rmi.Naming;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;

public class rmiServer {
    public static void main(String[] args) {
        try {
            LocateRegistry.createRegistry(1100);
            System.out.println("Server start.....");
        
            phepCong_impl obj = new phepCong_impl();
            Naming.bind("rmi://localhost:1100/congService", obj);
        
            xulychuoi_impl obj2 = new xulychuoi_impl();
            Naming.bind("rmi://localhost:1100/chuoiService", obj2);
        
        } catch (RemoteException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (MalformedURLException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        } catch (AlreadyBoundException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
    }
}
```

### File: xulychuoi_impl.java

**Duong dan:** `t6-lt/xulychuoi_impl.java`

```java
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class xulychuoi_impl extends UnicastRemoteObject implements xulychuoi_intf {

    protected xulychuoi_impl() throws RemoteException {
        super();
        // TODO Auto-generated constructor stub
    }

    @Override
    public String noi2chuoi(String str1, String str2) throws RemoteException {
        return str1 + str2;
    }
}
```

### File: xulychuoi_intf.java

**Duong dan:** `t6-lt/xulychuoi_intf.java`

```java
import java.rmi.Remote;
import java.rmi.RemoteException;

public interface xulychuoi_intf extends Remote {
    public String noi2chuoi(String str1, String str2) throws RemoteException;
}
```

`<a id='bai-tap-033'></a>`

## Bài tập 33 - TUẦN 6 - `t6/bai1`

**Tiêu đề bài tập:** TUẦN 6 - URL/Domain - BÀI 1

**Yeu cau tom tat:** Nhan 1 ten mien (domain) tu tham so dong lenh, hien thi host name va dia chi IP tuong ung.

**Cau hoi de bai:** Viet chuong trinh Java nhan vao ten mien (vi du google.com), sau do in host name va dia chi IP su dung lop InetAddress.

### Danh sach file

- DomainInfo.java

### File: DomainInfo.java

**Duong dan:** `t6/bai1/DomainInfo.java`

```java
package bai1;

import java.net.InetAddress;

public class DomainInfo {
    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("cach dung: java DomainInfo <domain>");
            System.out.println("vd: java bai1.DomainInfo google.com");
            return;
        }
        String domain = args[0];
        try {
            InetAddress address = InetAddress.getByName(domain);
            System.out.println("Hostname : " + address.getHostName());
            System.out.println("dia chi ip: " + address.getHostAddress());
        } catch (Exception e) {
            System.out.println("khong the phan giai ten mien: " + domain);
            System.out.println("loi: " + e.getMessage());
        }
    }
}
```

`<a id='bai-tap-034'></a>`

## Bài tập 34 - TUẦN 6 - `t6/bai2`

**Tiêu đề bài tập:** TUẦN 6 - URL/Domain - BÀI 2

**Yeu cau tom tat:** Kiem tra hostname co ton tai hay khong; neu ton tai thi liet ke tat ca dia chi IP cua hostname do.

**Cau hoi de bai:** Viet chuong trinh Java kiem tra su ton tai cua hostname. Neu hop le, hien thi day du danh sach IP (IPv4/IPv6 neu co).

### Danh sach file

- HostnameCheck.java

### File: HostnameCheck.java

**Duong dan:** `t6/bai2/HostnameCheck.java`

```java
package bai2;

import java.net.InetAddress;
import java.net.UnknownHostException;
import java.util.Scanner;

public class HostnameCheck {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("nhap host name kiem tra: ");
        String hostname = scanner.nextLine().trim();

        try {
            InetAddress[] addresses = InetAddress.getAllByName(hostname);
            System.out.println("Hostname \"" + hostname + "\" ton tai.");
            System.out.println("Danh sach dia chi ip:");
            for (InetAddress addr : addresses) {
                System.out.println("  " + addr.getHostAddress());
            }
        } catch (UnknownHostException e) {
            System.out.println("Hostname \"" + hostname + "\" khong ton tai.");
        } finally {
            scanner.close();
        }
    }
}
```

`<a id='bai-tap-035'></a>`

## Bài tập 35 - TUẦN 6 - `t6/bai3`

**Tiêu đề bài tập:** TUẦN 6 - Threads/Buffer - BÀI 3

**Yeu cau tom tat:** Tao vung dem luu so nguyen voi 2 thread: thread 1 nhap so vao buffer, thread 2 lay so ra tinh tong; dung khi nhap -1.

**Cau hoi de bai:** Viet chuong trinh Producer-Consumer: mot thread nhap du lieu vao bo dem, mot thread xu ly tinh tong. Co dong bo hoa va dieu kien ket thuc bang gia tri -1.

### Danh sach file

- BufferApp.java

### File: BufferApp.java

**Duong dan:** `t6/bai3/BufferApp.java`

```java
package bai3;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class BufferApp {

    private static final Queue<Integer> buffer = new LinkedList<>();
    private static boolean done = false;
    private static final Object lock = new Object();


    static class Producer extends Thread {
        @Override
        public void run() {
            Scanner scanner = new Scanner(System.in);
            System.out.println("Thread 1 (Producer): nhap cac so nguyen (nhap -1 de dung):");
            while (true) {
                System.out.print("nhap so: ");
                int num = scanner.nextInt();
                synchronized (lock) {
                    buffer.offer(num);
                    lock.notify();
                    if (num == -1) {
                        done = true;
                        break;
                    }
                }
            }
            scanner.close();
        }
    }

 
    static class Consumer extends Thread {
        @Override
        public void run() {
            int sum = 0;
            System.out.println("Thread 2 (Consumer): dang tinh tong...");
            while (true) {
                int num;
                synchronized (lock) {
                    while (buffer.isEmpty() && !done) {
                        try {
                            lock.wait();
                        } catch (InterruptedException e) {
                            Thread.currentThread().interrupt();
                            return;
                        }
                    }
                    if (buffer.isEmpty()) break;
                    num = buffer.poll();
                }
                if (num == -1) break;
                sum += num;
                System.out.println("  lay duoc: " + num + " | tong hien tai: " + sum);
            }
            System.out.println("tong c�c so da nhap: " + sum);
        }
    }

    public static void main(String[] args) throws InterruptedException {
        Thread producer = new Producer();
        Thread consumer = new Consumer();

        consumer.start();
        producer.start();

        producer.join();
        consumer.join();
    }
}
```

`<a id='bai-tap-036'></a>`

## Bài tập 36 - TUẦN 6 - `t6/bai4`

**Tiêu đề bài tập:** TUẦN 6 - Socket TCP - BÀI 4

**Yeu cau tom tat:** Xay dung TCP Client-Server (port 6789): client gui so nguyen n, server tra ve n! (giai thua).

**Cau hoi de bai:** Server lang nghe tai cong 6789, nhan n tu client va tra ket qua giai thua. Client nhap n tu ban phim, gui den server, nhan ket qua va hien thi.

### Danh sach file

- Client.java
- ClientHandler.java
- Server.java

### File: Client.java

**Duong dan:** `t6/bai4/Client.java`

```java
package bai4;

import java.io.*;
import java.net.*;
import java.util.Scanner;

public class Client {
    private static final String HOST = "localhost";
    private static final int PORT = 6789;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        try {
            System.out.print("nhap so nguyen n de tinh giai thua: ");
            int n = scanner.nextInt();

            try (Socket socket = new Socket(HOST, PORT)) {
                PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
                BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));

                out.println(n);
                String response = in.readLine();
                System.out.println("ket qua tu server: " + response);

            } catch (ConnectException e) {
                System.out.println("khong the ket noi server.");
            } catch (IOException e) {
                System.out.println("loi: " + e.getMessage());
            }
        } finally {
            scanner.close();
        }
    }
}
```

### File: ClientHandler.java

**Duong dan:** `t6/bai4/ClientHandler.java`

```java
package bai4;


import java.io.*;
import java.net.Socket;

public class ClientHandler extends Thread {
    private final Socket clientSocket;

    public ClientHandler(Socket clientSocket) {
        this.clientSocket = clientSocket;
    }

    @Override
    public void run() {
        try (
            Socket socket = this.clientSocket;
            BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter out = new PrintWriter(socket.getOutputStream(), true)
        ) {
            String line = in.readLine();
            if (line == null) return;

            try {
                int n = Integer.parseInt(line.trim());
                if (n < 0) {
                    out.println("khong tinh giai thua so am.");
                } else if (n > 20) {
                    out.println("n qua lon (toi da 20) de tranh tran so long.");
                } else {
                    long result = factorial(n);
                    out.println("giai thua cua " + n + " = " + result);
                }
            } catch (NumberFormatException e) {
                out.println("loi, gia tri khong hop le.");
            }

        } catch (IOException e) {
            System.out.println("loi handler: " + e.getMessage());
        }
    }

    private static long factorial(int n) {
        long result = 1L;
        for (int i = 2; i <= n; i++) result *= i;
        return result;
    }
}
```

### File: Server.java

**Duong dan:** `t6/bai4/Server.java`

```java
package bai4;



import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {
    private static final int PORT = 6789;

    public static void main(String[] args) {
        System.out.println("Server TCP lang nghe tai cong " + PORT + "...");

        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
            while (true) {
                Socket clientSocket = serverSocket.accept();
                System.out.println("ket noi tu: " + clientSocket.getInetAddress());

          
                new ClientHandler(clientSocket).start();
            }
        } catch (IOException e) {
            System.out.println("loi server: " + e.getMessage());
        }
    }
}
```

`<a id='bai-tap-037'></a>`

## Bài tập 37 - TUẦN 6 - `t6/bai5`

**Tiêu đề bài tập:** TUẦN 6 - Socket TCP - BÀI 5

**Yeu cau tom tat:** Server TCP nhan chuoi tu client, tra ve chuoi viet hoa va tong so ky tu trong chuoi.

**Cau hoi de bai:** Viet ung dung TCP trong do client nhap chuoi, server xu ly va phan hoi 2 thong tin: chuoi IN HOA va do dai chuoi.

### Danh sach file

- Client.java
- ClientHandler.java
- Server.java

### File: Client.java

**Duong dan:** `t6/bai5/Client.java`

```java
package bai5;

import java.io.*;
import java.net.*;
import java.util.Scanner;

public class Client {
    private static final String HOST = "localhost";
    private static final int PORT = 6789;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in, "UTF-8");
        System.out.print("nhap chuoi can xu ly: ");
        String input = scanner.nextLine();

        try (Socket socket = new Socket(HOST, PORT)) {
            PrintWriter out = new PrintWriter(
                    new OutputStreamWriter(socket.getOutputStream(), "UTF-8"), true);
            BufferedReader in = new BufferedReader(
                    new InputStreamReader(socket.getInputStream(), "UTF-8"));

            out.println(input);

            String line;
            while ((line = in.readLine()) != null) {
                System.out.println(line);
            }

        } catch (ConnectException e) {
            System.out.println("khong the ket noi den server.");
        } catch (IOException e) {
            System.out.println("loi: " + e.getMessage());
        } finally {
            scanner.close();
        }
    }
}
```

### File: ClientHandler.java

**Duong dan:** `t6/bai5/ClientHandler.java`

```java
package bai5;

import java.io.*;
import java.net.Socket;

public class ClientHandler extends Thread {
    private final Socket clientSocket;

    public ClientHandler(Socket clientSocket) {
        this.clientSocket = clientSocket;
    }

    @Override
    public void run() {
        try (
            BufferedReader in = new BufferedReader(
                    new InputStreamReader(clientSocket.getInputStream(), "UTF-8"));
            PrintWriter out = new PrintWriter(
                    new OutputStreamWriter(clientSocket.getOutputStream(), "UTF-8"), true)
        ) {
            String received = in.readLine();
            if (received != null) {
                String upperCase = received.toUpperCase();
                int charCount = received.length();
                out.println("chuoi viet hoa: " + upperCase);
                out.println("so ky tu: " + charCount);
            }
        } catch (IOException e) {
            System.out.println("loi xu ly client: " + e.getMessage());
        } finally {
            try {
                clientSocket.close();
            } catch (IOException ignored) {}
        }
    }
}
```

### File: Server.java

**Duong dan:** `t6/bai5/Server.java`

```java
package bai5;


import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class Server {
    private static final int PORT = 6789;

    public static void main(String[] args) {
        System.out.println("Server TCP lang nghe tai cong " + PORT + "...");
        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
            while (true) {
                Socket clientSocket = serverSocket.accept();
                System.out.println("ket noi tu: " + clientSocket.getInetAddress());

            
                new ClientHandler(clientSocket).start();
            }
        } catch (IOException e) {
            System.out.println("loi server: " + e.getMessage());
        }
    }
}
```

`<a id='bai-tap-038'></a>`

## Bài tập 38 - TUẦN 7 - `tuan7`

**Tiêu đề bài tập:** TUẦN 7 - THỰC HÀNH LAB 06 RMI (Tổng hợp 9 BÀI)

**Yeu cau tom tat:** Tong hop de RMI gom 9 bai: Hello World, cong 2 so, kiem tra nguyen to, danh ba, chat, ngan hang, tinh dien tich, dat ve may bay, dau gia truc tuyen.

**Cau hoi de bai:** Hoan thanh cac bai RMI theo de: thiet ke interface, cai dat server, dang ky registry, client goi ham tu xa. Danh sach day du trong file bt7.txt (co them bai 7-8-9 theo de).

### Danh sach file

- bt7.txt

### File: bt7.txt

**Duong dan:** `tuan7/bt7.txt`

```text
Bài 1. Máy chủ RMI trả về chuỗi "Hello, World!"

Mô tả. Viết một ứng dụng RMI trong đó client gọi phương thức từ server để nhận về chuỗi "Hello, World!".

Yêu cầu

Tạo interface chứa phương thức sayHello().

Triển khai phương thức này ở server.

Client gọi phương thức từ xa.



Bài 2. Bài tập Tính Tổng Hai Số

Mô tả. Viết ứng dụng RMI cho phép client gửi hai số nguyên a và b đến server, sau đó server trả về tổng a + b.

Yêu cầu

Interface chứa phương thức int add(int a, int b).

Server triển khai phương thức này.

Client nhập hai số từ bàn phím và gửi đến server để nhận kết quả.



Bài 3. Bài tập Kiểm Tra Số Nguyên Tố

Mô tả. Viết chương trình RMI giúp client kiểm tra xem một số có phải là số nguyên tố hay không.

Yêu cầu

Interface chứa phương thức boolean isPrime(int n).

Server kiểm tra số nguyên tố và trả kết quả.

Client nhập số và nhận kết quả từ server.



Bài 4. Bài tập Quản Lý Danh Bạ

Mô tả. Xây dựng một hệ thống quản lý danh bạ từ xa bằng RMI. Client có thể thêm, sửa, xóa và tìm kiếm liên

hệ trong danh bạ lưu trên server.

Yêu cầu

Interface có các phương thức:

void addContact(String name, String phone)

String findContact(String name)

boolean deleteContact(String name)

Server lưu trữ danh bạ bằng HashMap<String, String>.

Client nhập dữ liệu và gửiYêu cầu.



Bài 5. Bài tập Chat Đơn Giản với RMI

Mô tả. Tạo ứng dụng chat 1-1 giữa client và server thông qua RMI.

Yêu cầu

Interface có phương thức void sendMessage(String message).

Server nhận tin nhắn từ client và phản hồi.

Client nhập tin nhắn và hiển thị phản hồi.



Bài 6. Bài tập Quản Lý Tài Khoản Ngân Hàng

Mô tả. Xây dựng ứng dụng ngân hàng từ xa, cho phép client kiểm tra số dư, gửi tiền và rút tiền.

Yêu cầu

Interface có các phương thức:

double getBalance()

void deposit(double amount)

boolean withdraw(double amount)

Server quản lý tài khoản với số dư ban đầu.

Client có thể gửi/rút tiền và kiểm tra số dư.
```

`<a id='bai-tap-039'></a>`

## Bài tập 39 - TUẦN 7 - `tuan7/bai1`

**Tiêu đề bài tập:** TUẦN 7 - RMI BÀI 1 - Hello World

**Yeu cau tom tat:** Tao interface co phuong thuc sayHello(), server cai dat va client goi tu xa de nhan chuoi \"Hello, World!\".

**Cau hoi de bai:** Viet ung dung RMI trong do client goi sayHello() tren server va nhan ket qua \"Hello, World!\". Hoan chinh day du interface - server - client.

### Danh sach file

- HelloService.java
- HelloServiceImpl.java
- RMIClient.java
- RMIServer.java

### File: HelloService.java

**Duong dan:** `tuan7/bai1/HelloService.java`

```java
package bai1;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface HelloService extends Remote {
    String sayHello() throws RemoteException;
}
```

### File: HelloServiceImpl.java

**Duong dan:** `tuan7/bai1/HelloServiceImpl.java`

```java
package bai1;

import java.rmi.server.UnicastRemoteObject;
import java.rmi.RemoteException;

public class HelloServiceImpl extends UnicastRemoteObject implements HelloService {

    protected HelloServiceImpl() throws RemoteException {
        super();
    }

    @Override
    public String sayHello() throws RemoteException {
        return "Hello, World!";
    }
}
```

### File: RMIClient.java

**Duong dan:** `tuan7/bai1/RMIClient.java`

```java
package bai1;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class RMIClient {
    public static void main(String[] args) {
        try {
      
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);

       
            HelloService service = (HelloService) registry.lookup("HelloService");

       
            String result = service.sayHello();
            System.out.println("Server tra ve: " + result);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

### File: RMIServer.java

**Duong dan:** `tuan7/bai1/RMIServer.java`

```java
package bai1;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class RMIServer {
    public static void main(String[] args) {
        try {
            HelloService service = new HelloServiceImpl();

       
            Registry registry = LocateRegistry.createRegistry(1099);

        
            registry.rebind("HelloService", service);

            System.out.println("RMI Server dang chay...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

`<a id='bai-tap-040'></a>`

## Bài tập 40 - TUẦN 7 - `tuan7/bai2`

**Tiêu đề bài tập:** TUẦN 7 - RMI BÀI 2 - Tính tổng 2 so

**Yeu cau tom tat:** Interface co int add(int a, int b); client nhap a,b va goi server de nhan tong.

**Cau hoi de bai:** Viet bai tap RMI tinh tong 2 so nguyen: server xu ly add(a,b), client gui tham so va hien thi ket qua tra ve.

### Danh sach file

- AddClient.java
- AddServer.java
- AddService.java
- AddServiceImpl.java

### File: AddClient.java

**Duong dan:** `tuan7/bai2/AddClient.java`

```java
package bai2;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class AddClient {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);
            AddService service = (AddService) registry.lookup("AddService");

            System.out.print("Nhap a: ");
            int a = sc.nextInt();
            System.out.print("Nhap b: ");
            int b = sc.nextInt();

            int sum = service.add(a, b);
            System.out.println("Tong a + b = " + sum);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

### File: AddServer.java

**Duong dan:** `tuan7/bai2/AddServer.java`

```java
package bai2;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class AddServer {
    public static void main(String[] args) {
        try {
            AddService service = new AddServiceImpl();
            Registry registry = LocateRegistry.createRegistry(1099);
            registry.rebind("AddService", service);
            System.out.println("AddServer dang chay...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

### File: AddService.java

**Duong dan:** `tuan7/bai2/AddService.java`

```java
package bai2;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface AddService extends Remote {
    int add(int a, int b) throws RemoteException;
}
```

### File: AddServiceImpl.java

**Duong dan:** `tuan7/bai2/AddServiceImpl.java`

```java
package bai2;

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class AddServiceImpl extends UnicastRemoteObject implements AddService {

    protected AddServiceImpl() throws RemoteException {
        super();
    }

    @Override
    public int add(int a, int b) throws RemoteException {
        return a + b;
    }
}

```

`<a id='bai-tap-041'></a>`

## Bài tập 41 - TUẦN 7 - `tuan7/bai3`

**Tiêu đề bài tập:** TUẦN 7 - RMI BÀI 3 - Kiểm tra so nguyen to

**Yeu cau tom tat:** Interface co boolean isPrime(int n); server kiem tra so nguyen to va tra ket qua true/false cho client.

**Cau hoi de bai:** Viet chuong trinh RMI giup client kiem tra mot so co phai nguyen to hay khong, dua tren phuong thuc isPrime(int n).

### Danh sach file

- PrimeService.java
- PrimeServiceImpl.java
- RMIClient.java
- RMIServer.java

### File: PrimeService.java

**Duong dan:** `tuan7/bai3/PrimeService.java`

```java
package bai3;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface PrimeService extends Remote {
    boolean isPrime(int n) throws RemoteException;
}
```

### File: PrimeServiceImpl.java

**Duong dan:** `tuan7/bai3/PrimeServiceImpl.java`

```java
package bai3;

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class PrimeServiceImpl extends UnicastRemoteObject implements PrimeService {

    protected PrimeServiceImpl() throws RemoteException {
        super();
    }

    @Override
    public boolean isPrime(int n) throws RemoteException {
        if (n < 2) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;

        for (int i = 3; i * i <= n; i += 2) {
            if (n % i == 0) return false;
        }
        return true;
    }
}
```

### File: RMIClient.java

**Duong dan:** `tuan7/bai3/RMIClient.java`

```java
package bai3;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class RMIClient {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);
            PrimeService service = (PrimeService) registry.lookup("PrimeService");

            System.out.print("Nhap n: ");
            int n = sc.nextInt();

            boolean result = service.isPrime(n);
            System.out.println(result ? (n + " la so nguyen to")
                                      : (n + " khong phai so nguyen to"));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

### File: RMIServer.java

**Duong dan:** `tuan7/bai3/RMIServer.java`

```java
package bai3;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class RMIServer {
    public static void main(String[] args) {
        try {
            PrimeService service = new PrimeServiceImpl();
            Registry registry = LocateRegistry.createRegistry(1099);
            registry.rebind("PrimeService", service);
            System.out.println("RMI Server dang chay...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

`<a id='bai-tap-042'></a>`

## Bài tập 42 - TUẦN 7 - `tuan7/bai4`

**Tiêu đề bài tập:** TUẦN 7 - RMI BÀI 4 - Quản lý danh ba

**Yeu cau tom tat:** Xay dung ContactService voi addContact, findContact, deleteContact; server luu danh ba bang HashMap<String,String>.

**Cau hoi de bai:** Viet he thong danh ba tu xa bang RMI. Client co the them/tim/xoa lien he; du lieu duoc luu va quan ly tap trung tren server.

### Danh sach file

- ContactService.java
- ContactServiceImpl.java
- RMIClient.java
- RMIServer.java

### File: ContactService.java

**Duong dan:** `tuan7/bai4/ContactService.java`

```java
package bai4;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface ContactService extends Remote {
    void addContact(String name, String phone) throws RemoteException;
    String findContact(String name) throws RemoteException;
    boolean deleteContact(String name) throws RemoteException;
}
```

### File: ContactServiceImpl.java

**Duong dan:** `tuan7/bai4/ContactServiceImpl.java`

```java
package bai4;

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.HashMap;

public class ContactServiceImpl extends UnicastRemoteObject implements ContactService {

    private final HashMap<String, String> contacts;

    protected ContactServiceImpl() throws RemoteException {
        super();
        contacts = new HashMap<>();
    }

    @Override
    public synchronized void addContact(String name, String phone) throws RemoteException {
        contacts.put(name, phone); 
    }

    @Override
    public synchronized String findContact(String name) throws RemoteException {
        return contacts.get(name); 
    }

    @Override
    public synchronized boolean deleteContact(String name) throws RemoteException {
        return contacts.remove(name) != null;
    }
}
```

### File: RMIClient.java

**Duong dan:** `tuan7/bai4/RMIClient.java`

```java
package bai4;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class RMIClient {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);
            ContactService service = (ContactService) registry.lookup("ContactService");

            while (true) {
                System.out.println("\n===== QUAN LY DANH BA =====");
                System.out.println("1. Them / Cap nhat lien he");
                System.out.println("2. Tim lien he");
                System.out.println("3. Xoa lien he");
                System.out.println("0. Thoat");
                System.out.print("Chon: ");

                int choice = Integer.parseInt(sc.nextLine().trim());

                switch (choice) {
                    case 1:
                        System.out.print("Nhap ten: ");
                        String nameAdd = sc.nextLine().trim();
                        System.out.print("Nhap so dien thoai: ");
                        String phone = sc.nextLine().trim();
                        service.addContact(nameAdd, phone);
                        System.out.println("Da luu lien he.");
                        break;

                    case 2:
                        System.out.print("Nhap ten can tim: ");
                        String nameFind = sc.nextLine().trim();
                        String result = service.findContact(nameFind);
                        if (result != null) {
                            System.out.println("So dien thoai: " + result);
                        } else {
                            System.out.println("Khong tim thay lien he.");
                        }
                        break;

                    case 3:
                        System.out.print("Nhap ten can xoa: ");
                        String nameDelete = sc.nextLine().trim();
                        boolean deleted = service.deleteContact(nameDelete);
                        System.out.println(deleted ? "Xoa thanh cong." : "Khong tim thay de xoa.");
                        break;

                    case 0:
                        System.out.println("Tam biet!");
                        return;

                    default:
                        System.out.println("Lua chon khong hop le.");
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

### File: RMIServer.java

**Duong dan:** `tuan7/bai4/RMIServer.java`

```java
package bai4;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class RMIServer {
    public static void main(String[] args) {
        try {
            ContactService service = new ContactServiceImpl();
            Registry registry = LocateRegistry.createRegistry(1099);
            registry.rebind("ContactService", service);
            System.out.println("RMI Server dang chay...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

`<a id='bai-tap-043'></a>`

## Bài tập 43 - TUẦN 7 - `tuan7/bai5`

**Tiêu đề bài tập:** TUẦN 7 - RMI BÀI 5 - Chat don gian

**Yeu cau tom tat:** Interface co sendMessage(String message); client gui tin, server nhan va phan hoi theo luong chat 1-1.

**Cau hoi de bai:** Tao ung dung chat don gian giua client va server qua RMI: gui/nhan thong diep va hien thi phan hoi.

### Danh sach file

- ChatService.java
- ChatServiceImpl.java
- RMIClient.java
- RMIServer.java

### File: ChatService.java

**Duong dan:** `tuan7/bai5/ChatService.java`

```java
package bai5;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface ChatService extends Remote {
    String sendMessage(String message) throws RemoteException;
}
```

### File: ChatServiceImpl.java

**Duong dan:** `tuan7/bai5/ChatServiceImpl.java`

```java
package bai5;

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class ChatServiceImpl extends UnicastRemoteObject implements ChatService {

    protected ChatServiceImpl() throws RemoteException {
        super();
    }

    @Override
    public String sendMessage(String message) throws RemoteException {
        System.out.println("Client: " + message);

        String msg = message == null ? "" : message.trim().toLowerCase();

        if (msg.equals("hello") || msg.equals("hi")) {
            return "Server: Xin chao ban!";
        } else if (msg.equals("bye")) {
            return "Server: Tam biet!";
        } else if (msg.isEmpty()) {
            return "Server: Ban chua nhap gi.";
        } else {
            return "Server: Da nhan -> " + message;
        }
    }
}
```

### File: RMIClient.java

**Duong dan:** `tuan7/bai5/RMIClient.java`

```java
package bai5;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class RMIClient {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);
            ChatService service = (ChatService) registry.lookup("ChatService");

            System.out.println("Chat voi server (go 'exit' de thoat)");

            while (true) {
                System.out.print("Ban: ");
                String message = sc.nextLine();

                if ("exit".equalsIgnoreCase(message)) {
                    System.out.println("Thoat chat.");
                    break;
                }

                String reply = service.sendMessage(message);
                System.out.println(reply);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

### File: RMIServer.java

**Duong dan:** `tuan7/bai5/RMIServer.java`

```java
package bai5;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class RMIServer {
    public static void main(String[] args) {
        try {
            ChatService service = new ChatServiceImpl();
            Registry registry = LocateRegistry.createRegistry(1099);
            registry.rebind("ChatService", service);
            System.out.println("RMI Server dang chay...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

`<a id='bai-tap-044'></a>`

## Bài tập 44 - TUẦN 7 - `tuan7/bai6`

**Tiêu đề bài tập:** TUẦN 7 - RMI BÀI 6 - Quản lý tai khoan ngan hang

**Yeu cau tom tat:** Interface gom getBalance(), deposit(amount), withdraw(amount); server quan ly so du, client gui/rut tien va xem so du.

**Cau hoi de bai:** Xay dung ung dung ngan hang tu xa bang RMI: client thuc hien gui tien, rut tien, kiem tra so du tren cung mot tai khoan do server quan ly.

### Danh sach file

- BankService.java
- BankServiceImpl.java
- RMIClient.java
- RMIServer.java

### File: BankService.java

**Duong dan:** `tuan7/bai6/BankService.java`

```java
package bai6;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface BankService extends Remote {
    double getBalance() throws RemoteException;
    void deposit(double amount) throws RemoteException;
    boolean withdraw(double amount) throws RemoteException;
}
```

### File: BankServiceImpl.java

**Duong dan:** `tuan7/bai6/BankServiceImpl.java`

```java
package bai6;

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class BankServiceImpl extends UnicastRemoteObject implements BankService {

    private double balance;

    protected BankServiceImpl(double initialBalance) throws RemoteException {
        super();
        this.balance = initialBalance;
    }

    @Override
    public synchronized double getBalance() throws RemoteException {
        return balance;
    }

    @Override
    public synchronized void deposit(double amount) throws RemoteException {
        if (amount > 0) {
            balance += amount;
        }
    }

    @Override
    public synchronized boolean withdraw(double amount) throws RemoteException {
        if (amount <= 0) return false;
        if (amount > balance) return false;
        balance -= amount;
        return true;
    }
}
```

### File: RMIClient.java

**Duong dan:** `tuan7/bai6/RMIClient.java`

```java
package bai6;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class RMIClient {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);
            BankService service = (BankService) registry.lookup("BankService");

            while (true) {
                System.out.println("\n===== NGAN HANG RMI =====");
                System.out.println("1. Xem so du");
                System.out.println("2. Gui tien");
                System.out.println("3. Rut tien");
                System.out.println("0. Thoat");
                System.out.print("Chon: ");

                int choice = Integer.parseInt(sc.nextLine().trim());

                switch (choice) {
                    case 1:
                        System.out.println("So du hien tai: " + service.getBalance());
                        break;

                    case 2:
                        System.out.print("Nhap so tien muon gui: ");
                        double depositAmount = Double.parseDouble(sc.nextLine().trim());
                        service.deposit(depositAmount);
                        System.out.println("Gui tien thanh cong. So du moi: " + service.getBalance());
                        break;

                    case 3:
                        System.out.print("Nhap so tien muon rut: ");
                        double withdrawAmount = Double.parseDouble(sc.nextLine().trim());
                        boolean ok = service.withdraw(withdrawAmount);
                        if (ok) {
                            System.out.println("Rut tien thanh cong. So du moi: " + service.getBalance());
                        } else {
                            System.out.println("Rut tien that bai (so tien khong hop le hoac khong du so du).");
                        }
                        break;

                    case 0:
                        System.out.println("Tam biet!");
                        return;

                    default:
                        System.out.println("Lua chon khong hop le.");
                }
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

### File: RMIServer.java

**Duong dan:** `tuan7/bai6/RMIServer.java`

```java
package bai6;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class RMIServer {
    public static void main(String[] args) {
        try {
            double initialBalance = 1000.0; // so du ban dau
            BankService service = new BankServiceImpl(initialBalance);

            Registry registry = LocateRegistry.createRegistry(1099);
            registry.rebind("BankService", service);

            System.out.println("RMI Server dang chay... So du ban dau: " + initialBalance);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

`<a id='bai-tap-045'></a>`

## Bài tập 45 - TUẦN 8 - `tuan8`

**Tiêu đề bài tập:** TUẦN 8 - Đề RMI mở rộng (tổng hợp từ `tuan8/kk.txt`)

**Yeu cau tom tat:** Tong hop 2 de RMI: (1) tinh bieu thuc so hoc khong ngoac, (2) tra cuu thong tin ca nhan theo CMND/CCCD.

**Cau hoi de bai:** Dua tren `tuan8/kk.txt`, hoan thanh 2 bai RMI mo rong: server cung cap dich vu tinh toan/tra cuu, client gui yeu cau va nhan ket qua hoac thong bao loi.

### Danh sach file

- kk.txt

### File: kk.txt

**Duong dan:** `tuan8/kk.txt`

```text
Bài 1: Sử dụng RMI, Viết chương trình tính toán sau

- Client gửi 1 chuỗi phép toán gồm nhiều số phân cách nhau bởi 1 trong 4 phép toán (+, -

, *, /) đến server, giả sử chuỗi phép toán không chứa các dấu ngoặc. Ví dụ chuỗi phép

toán sau: 12+34-56*78/4+14-17

- Server cung cấp phương thức tính giá trị biểu thức, tính kết quả và trả lại client hoặc trả thông báo lỗi nếu chuỗi

phép toán không đúng định dạng.

- Client xuất kết quả ra console

Bài 2: Sử dụng RMI, Viết chương trình tra cứu thông tin cá nhân

- Client gửi 1 số chứng minh nhân dân/căn cước công dân người VN đến server.

- Server cung cấp phương thức tìm kiếm họ tên, quê quán tương ứng với số CMND/CCCD đó và gửi trả ngược lại

client hoặc trả thông báo lỗi nếu không tìm thấy thông tin.

- Client xuất kết quả ra console.

```

`<a id='bai-tap-046'></a>`

## Bài tập 46 - TUẦN 8 - `tuan8/bai1`

**Tiêu đề bài tập:** TUẦN 8 - Bài mở rộng - Tính biểu thức (RMI)

**Yeu cau tom tat:** Client gui bieu thuc khong ngoac (co + - * /), server phan tich theo dung thu tu uu tien toan tu va tra ket qua.

**Cau hoi de bai:** Bai mo rong thuc hanh: xay dung dich vu tinh bieu thuc so hoc tren mo hinh client-server (RMI), xu ly loi dinh dang dau vao ro rang.

### Danh sach file

- CalcService.java
- CalcServiceImpl.java
- RMIClient.java
- RMIServer.java

### File: CalcService.java

**Duong dan:** `tuan8/bai1/CalcService.java`

```java
package bai1;


import java.rmi.Remote;
import java.rmi.RemoteException;

public interface CalcService extends Remote {
    String evaluate(String expression) throws RemoteException; 
  
}
```

### File: CalcServiceImpl.java

**Duong dan:** `tuan8/bai1/CalcServiceImpl.java`

```java
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

```

### File: RMIClient.java

**Duong dan:** `tuan8/bai1/RMIClient.java`

```java
package bai1;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class RMIClient {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);
            CalcService service = (CalcService) registry.lookup("CalcService");

            System.out.println("Nhap bieu thuc (go 'exit' de thoat).");

            while (true) {
                System.out.print("Bieu thuc> ");
                String expr = sc.nextLine().trim();

                if (expr.equalsIgnoreCase("exit")) {
                    System.out.println("Thoat chuong trinh.");
                    break;
                }

                if (expr.isEmpty()) {
                    System.out.println("ERROR: bieu thuc rong");
                    continue;
                }

                String result = service.evaluate(expr);
                System.out.println("Ket qua: " + result);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

### File: RMIServer.java

**Duong dan:** `tuan8/bai1/RMIServer.java`

```java
package bai1;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class RMIServer {
    public static void main(String[] args) {
        try {
            CalcService service = new CalcServiceImpl();
            Registry registry = LocateRegistry.createRegistry(1099);
            registry.rebind("CalcService", service);
            System.out.println("RMI Server dang chay...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

`<a id='bai-tap-047'></a>`

## Bài tập 47 - TUẦN 8 - `tuan8/bai2`

**Tiêu đề bài tập:** TUẦN 8 - Bài mở rộng - Tra cứu thông tin (RMI)

**Yeu cau tom tat:** Client gui so giay to (CMND/CCCD), server tim kiem trong du lieu luu tru va tra ve thong tin ho ten/que quan hoac thong bao khong tim thay.

**Cau hoi de bai:** Bai mo rong thuc hanh: xay dung dich vu tra cuu thong tin ca nhan qua mang theo so dinh danh, co xu ly truong hop khong ton tai.

### Danh sach file

- IdentityService.java
- IdentityServiceImpl.java
- RMIClient.java
- RMIServer.java

### File: IdentityService.java

**Duong dan:** `tuan8/bai2/IdentityService.java`

```java
package bai2;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface IdentityService extends Remote {
    String lookup(String idNumber) throws RemoteException;
  
}
```

### File: IdentityServiceImpl.java

**Duong dan:** `tuan8/bai2/IdentityServiceImpl.java`

```java
package bai2;

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.HashMap;
import java.util.Map;

public class IdentityServiceImpl extends UnicastRemoteObject implements IdentityService {

    /**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	private final Map<String, PersonInfo> db = new HashMap<>();

    protected IdentityServiceImpl() throws RemoteException {
        super();

   
        db.put("012345678901", new PersonInfo("Nguyen Van A", "Ha Noi"));
        db.put("079123456789", new PersonInfo("Tran Thi B", "TP Ho Chi Minh"));
        db.put("123456789",    new PersonInfo("Le Van C", "Da Nang")); 
    }

    @Override
    public String lookup(String idNumber) throws RemoteException {
        if (idNumber == null) return "ERROR: id rong";
        String id = idNumber.trim();

        if (id.isEmpty()) return "ERROR: id rong";
        if (!id.matches("\\d+")) return "ERROR: id chi duoc chua chu so";
    
        if (id.length() < 9 || id.length() > 12) return "ERROR: do dai id khong hop le (9-12 so)";

        PersonInfo info = db.get(id);
        if (info == null) return "ERROR: khong tim thay thong tin cho id " + id;

        return "Ho ten: " + info.fullName + " | Que quan: " + info.hometown;
    }

    private static class PersonInfo {
        final String fullName;
        final String hometown;

        PersonInfo(String fullName, String hometown) {
            this.fullName = fullName;
            this.hometown = hometown;
        }
    }
}
```

### File: RMIClient.java

**Duong dan:** `tuan8/bai2/RMIClient.java`

```java
package bai2;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.Scanner;

public class RMIClient {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            Registry registry = LocateRegistry.getRegistry("localhost", 1099);
            IdentityService service = (IdentityService) registry.lookup("IdentityService");

            System.out.print("Nhap so CMND/CCCD: ");
            String id = sc.nextLine();

            String result = service.lookup(id);
            System.out.println(result);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

### File: RMIServer.java

**Duong dan:** `tuan8/bai2/RMIServer.java`

```java
package bai2;

import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class RMIServer {
    public static void main(String[] args) {
        try {
            IdentityService service = new IdentityServiceImpl();
            Registry registry = LocateRegistry.createRegistry(1099);
            registry.rebind("IdentityService", service);
            System.out.println("RMI Server dang chay...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

`<a id='bai-tap-048'></a>`

## Bài tập 48 - TUẦN 9 - `tuan9`

**Tiêu đề bài tập:** TUẦN 9 - JDBC/SQLite: Quản lý cửa hàng (A-Z)

**Yeu cau tom tat:** Thuc hanh JDBC voi SQLite theo huong dan A-Z: ket noi CSDL, tao bang, them/sua/xoa/truy van du lieu, dung PreparedStatement, transaction va xu ly ngoai le day du.

**Cau hoi de bai:** Viet ung dung quan ly cua hang bang JDBC + SQLite: CRUD du lieu, bao cao tong hop (SUM/AVG/MIN/MAX/COUNT), dam bao dong ket noi dung cach va ho tro commit/rollback khi cap nhat nhieu buoc.

### Danh sach file

- DatabaseManager.java
- huongdan.txt
- MainApp.java
- SanPham.java

### File: DatabaseManager.java

**Duong dan:** `tuan9/DatabaseManager.java`

```java
package b1;

import java.sql.*;

public class DatabaseManager {
    private static final String URL = "jdbc:sqlite:quanly_hethong.db";


    public static Connection getConnection() throws SQLException {
        return DriverManager.getConnection(URL);
    }


    public static void initDatabase(Connection conn) throws SQLException {
        String sqlSP = "CREATE TABLE IF NOT EXISTS SanPham (" +
                       "maSP INTEGER PRIMARY KEY, tenSP TEXT, gia REAL, soluong INTEGER)";
        String sqlNV = "CREATE TABLE IF NOT EXISTS NhanVien (" +
                       "id INTEGER PRIMARY KEY AUTOINCREMENT, ten TEXT, chuc_vu TEXT, luong REAL)";
        try (Statement stmt = conn.createStatement()) {
            stmt.execute(sqlSP);
            stmt.execute(sqlNV);
        }
    }

  
    public static void insertSanPham(Connection conn, SanPham sp) throws SQLException {
        String sql = "INSERT INTO SanPham(maSP, tenSP, gia, soluong) VALUES(?,?,?,?)";
        try (PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setInt(1, sp.getMaSP());
            pstmt.setString(2, sp.getTenSP());
            pstmt.setDouble(3, sp.getGia());
            pstmt.setInt(4, sp.getSoLuong());
            pstmt.executeUpdate();
        }
    }


    public static void updateSanPham(Connection conn, int maSP, double giaMoi, int slMoi) throws SQLException {
        String sql = "UPDATE SanPham SET gia = ?, soluong = ? WHERE maSP = ?";
        try (PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setDouble(1, giaMoi);
            pstmt.setInt(2, slMoi);
            pstmt.setInt(3, maSP);
            pstmt.executeUpdate();
        }
    }

  
    public static void deleteSanPham(Connection conn, int maSP) throws SQLException {
        String sql = "DELETE FROM SanPham WHERE maSP = ?";
        try (PreparedStatement pstmt = conn.prepareStatement(sql)) {
            pstmt.setInt(1, maSP);
            pstmt.executeUpdate();
        }
    }

    public static void thongKeNhanVien(Connection conn) throws SQLException {
        String sql = "SELECT SUM(luong) as tong, AVG(luong) as trungbinh, " +
                     "MAX(luong) as cao, MIN(luong) as thap FROM NhanVien";
        try (Statement stmt = conn.createStatement(); ResultSet rs = stmt.executeQuery(sql)) {
            if (rs.next()) {
                System.out.println("--- THỐNG KÊ LƯƠNG NHÂN VIÊN ---");
                System.out.println("Tổng lương: " + rs.getDouble("tong"));
                System.out.println("Lương TB:   " + rs.getDouble("trungbinh"));
                System.out.println("Cao nhất:   " + rs.getDouble("cao"));
            }
        }
    }
}

```

### File: huongdan.txt

**Duong dan:** `tuan9/huongdan.txt`

```text
HƯỚNG DẪN TỪ A - Z: QUẢN LÝ CỬA HÀNG VỚI JDBC & SQLITE
Bước 1: Tải và Chuẩn bị thư viện (Driver)
Vì Java không đi kèm sẵn trình điều khiển cho SQLite, bạn phải tự tải về:

Truy cập: SQLite JDBC Releases.

Tìm bản mới nhất (ví dụ: sqlite-jdbc-3.45.1.0.jar) và tải về máy.

Lưu file này ở một thư mục dễ nhớ trên máy tính.

Bước 2: Thiết lập dự án trên Eclipse
Tạo Project: File > New > Java Project. Đặt tên: QuanLyHeThong.

Thêm Thư viện vào Classpath:

Chuột phải vào tên Project > Properties.

Chọn Java Build Path (bên trái) > Thẻ Libraries.

Chọn Classpath (nếu có) > Nhấn nút Add External JARs....

Chọn file .jar bạn vừa tải ở Bước 1.

Nhấn Apply and Close.

Bước 3: Tạo các file mã nguồn
Tạo 3 file .java trong thư mục src với nội dung như sau:

File 1: SanPham.java (Lớp đối tượng)
Java

public class SanPham {
    private int maSP;
    private String tenSP;
    private double gia;
    private int soLuong;

    public SanPham(int maSP, String tenSP, double gia, int soLuong) {
        this.maSP = maSP;
        this.tenSP = tenSP;
        this.gia = gia;
        this.soLuong = soLuong;
    }
    public int getMaSP() { return maSP; }
    public String getTenSP() { return tenSP; }
    public double getGia() { return gia; }
    public int getSoLuong() { return soLuong; }
}
File 2: DatabaseManager.java (Xử lý DB)
Java

import java.sql.*;

public class DatabaseManager {
    private static final String URL = "jdbc:sqlite:quanly.db";

    public static Connection getConnection() throws SQLException {
        return DriverManager.getConnection(URL);
    }

    public static void initDatabase(Connection conn) throws SQLException {
        try (Statement stmt = conn.createStatement()) {
            // Tạo bảng Sản phẩm và Nhân viên
            stmt.execute("CREATE TABLE IF NOT EXISTS SanPham (maSP INTEGER PRIMARY KEY, tenSP TEXT, gia REAL, soluong INTEGER)");
            stmt.execute("CREATE TABLE IF NOT EXISTS NhanVien (id INTEGER PRIMARY KEY AUTOINCREMENT, ten TEXT, chuc_vu TEXT, luong REAL)");
        }
    }
}
File 3: MainApp.java (Chương trình chạy chính)
Java

import java.sql.*;

public class MainApp {
    public static void main(String[] args) {
        Connection conn = null;
        try {
            conn = DatabaseManager.getConnection();
            conn.setAutoCommit(false); // Bắt đầu Giao dịch (Transaction)
            DatabaseManager.initDatabase(conn);

            // 1. Thêm sản phẩm (Dùng INSERT OR IGNORE để tránh lỗi trùng ID)
            String sqlInsert = "INSERT OR IGNORE INTO SanPham(maSP, tenSP, gia, soluong) VALUES(?,?,?,?)";
            try (PreparedStatement pstmt = conn.prepareStatement(sqlInsert)) {
                pstmt.setInt(1, 1); pstmt.setString(2, "Laptop Dell"); pstmt.setDouble(3, 15000); pstmt.setInt(4, 5);
                pstmt.executeUpdate();
            }

            // 2. Thêm nhân viên mẫu để có dữ liệu thống kê
            String sqlNV = "INSERT INTO NhanVien(ten, chuc_vu, luong) VALUES(?,?,?)";
            try (PreparedStatement pstmt = conn.prepareStatement(sqlNV)) {
                pstmt.setString(1, "Nguyen Van A"); pstmt.setString(2, "Dev"); pstmt.setDouble(3, 3000);
                pstmt.executeUpdate();
            }

            // 3. Truy vấn nâng cao (SUM, AVG)
            try (Statement stmt = conn.createStatement(); 
                 ResultSet rs = stmt.executeQuery("SELECT SUM(luong), AVG(luong) FROM NhanVien")) {
                if (rs.next()) {
                    System.out.println("Tổng lương NV: " + rs.getDouble(1));
                    System.out.println("Lương TB NV: " + rs.getDouble(2));
                }
            }

            conn.commit(); // Lưu mọi thay đổi
            System.out.println("[SUCCESS] Chạy thành công!");

        } catch (SQLException e) {
            System.err.println("[ERROR] Lỗi: " + e.getMessage());
            try { if (conn != null) conn.rollback(); } catch (SQLException ex) {}
        } finally {
            try { if (conn != null) conn.close(); } catch (SQLException e) {}
        }
    }
}
Bước 4: Chạy và Kiểm tra kết quả
Chuột phải vào MainApp.java > Run As > Java Application.

Xem kết quả ở cửa sổ Console.

Để xem bảng dữ liệu:

Nhấn F5 vào tên Project trong Eclipse để thấy file quanly.db xuất hiện.

Tải phần mềm DB Browser for SQLite.

Mở file quanly.db bằng phần mềm đó để xem các hàng dữ liệu đã được chèn vào.

Tóm tắt các điểm "sống còn" cần nhớ:
Driver: Thiếu file .jar là code không bao giờ chạy được.

Transaction: Phải có commit() ở cuối thì dữ liệu mới thực sự được ghi vào file.

Primary Key: Không được chèn trùng ID (nên dùng INSERT OR IGNORE hoặc xóa file .db cũ để chạy lại sạch sẽ).

Finally: Luôn luôn đóng kết nối để giải phóng tài nguyên máy tính.

Giờ bạn chỉ cần làm theo đúng thứ tự này là hệ thống sẽ vận hành hoàn hảo! Bạn đã sẵn sàng để thử chạy lại toàn bộ chưa?
```

### File: MainApp.java

**Duong dan:** `tuan9/MainApp.java`

```java
package b1;

import java.sql.*;

public class MainApp {
    public static void main(String[] args) {
        Connection conn = null;
        try {
  
            conn = DatabaseManager.getConnection();
        
      
            conn.setAutoCommit(false); 


            DatabaseManager.initDatabase(conn);

   
            DatabaseManager.insertSanPham(conn, new SanPham(1, "Laptop Dell", 15000, 5));
            DatabaseManager.insertSanPham(conn, new SanPham(2, "Macbook M3", 35000, 3));
            DatabaseManager.insertSanPham(conn, new SanPham(3, "Chuột Logi", 500, 10));

 
            DatabaseManager.updateSanPham(conn, 1, 14500, 4);
            DatabaseManager.deleteSanPham(conn, 3);
  

            System.out.println(">>> Đang thêm dữ liệu nhân viên để thống kê...");
            String sqlInsertNV = "INSERT INTO NhanVien(ten, chuc_vu, luong) VALUES(?,?,?)";
            try (PreparedStatement pstmt = conn.prepareStatement(sqlInsertNV)) {

                pstmt.setString(1, "Nguyen Van A"); pstmt.setString(2, "Dev"); pstmt.setDouble(3, 2000);
                pstmt.executeUpdate();
            
                pstmt.setString(1, "Tran Thi B"); pstmt.setString(2, "Manager"); pstmt.setDouble(3, 5000);
                pstmt.executeUpdate();
            }


            DatabaseManager.thongKeNhanVien(conn);


            conn.commit();
            System.out.println("\n[SUCCESS] Giao dịch hoàn tất thành công!");

        } catch (SQLException e) {
   
            System.err.println("[ERROR] Lỗi SQL: " + e.getMessage());
            try {
                if (conn != null) {
                    conn.rollback(); 
                    System.err.println("[ROLLBACK] Đã khôi phục trạng thái dữ liệu cũ.");
                }
            } catch (SQLException ex) {
                ex.printStackTrace();
            }
        } finally {
  
            try {
                if (conn != null) {
                    conn.close();
                    System.out.println("[INFO] Đã đóng kết nối an toàn.");
                }
            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
    }
}
```

### File: SanPham.java

**Duong dan:** `tuan9/SanPham.java`

```java
package b1;

public class SanPham {
    private int maSP;
    private String tenSP;
    private double gia;
    private int soLuong;

    public SanPham(int maSP, String tenSP, double gia, int soLuong) {
        this.maSP = maSP;
        this.tenSP = tenSP;
        this.gia = gia;
        this.soLuong = soLuong;
    }

  
    public int getMaSP() { return maSP; }
    public String getTenSP() { return tenSP; }
    public double getGia() { return gia; }
    public int getSoLuong() { return soLuong; }

    @Override
    public String toString() {
        return String.format("ID: %d | T�n: %-15s | Gi�: %,.0f | SL: %d", maSP, tenSP, gia, soLuong);
    }
}
```
