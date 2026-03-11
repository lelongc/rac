Dựa trên cấu trúc bài hướng dẫn từ Viblo mà bạn cung cấp, mình sẽ viết lại một chương trình RMI hoàn chỉnh để kiểm tra số nguyên tố.
Chương trình này sẽ giúp bạn hiểu cách truyền một số từ Client lên Server, Server tính toán và trả kết quả về.
1. Định nghĩa Interface dùng chung (ICheckNumber.java)
Đây là "bản hợp đồng" giữa Client và Server. Cả hai bên đều phải biết interface này.
package com.rmi.prime;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface ICheckNumber extends Remote {
    // Phương thức kiểm tra số nguyên tố
    public boolean isPrime(int n) throws RemoteException;
}

2. Cài đặt trên Server
Bước 2.1: Tạo lớp thực thi (CheckNumberImpl.java)
Lớp này chứa logic kiểm tra số nguyên tố thực tế.
package com.rmi.prime.server;

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import com.rmi.prime.ICheckNumber;

public class CheckNumberImpl extends UnicastRemoteObject implements ICheckNumber {

    // Constructor bắt buộc phải ném RemoteException
    public CheckNumberImpl() throws RemoteException {
        super();
    }

    @Override
    public boolean isPrime(int n) throws RemoteException {
        System.out.println("Đang kiểm tra số: " + n);
        if (n <= 1) return false;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}

Bước 2.2: Cài đặt chương trình chạy Server (RMIServer.java)
package com.rmi.prime.server;

import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;
import com.rmi.prime.ICheckNumber;

public class RMIServer {
    public static void main(String[] args) {
        try {
            // 1. Tạo đối tượng thực thi
            ICheckNumber checker = new CheckNumberImpl();

            // 2. Tạo Registry tại cổng 6789
            LocateRegistry.createRegistry(6789);

            // 3. Đăng ký đối tượng với tên "PrimeChecker"
            // Thay "localhost" bằng IP của bạn nếu chạy khác máy
            Naming.rebind("rmi://localhost:6789/PrimeChecker", checker);

            System.out.println(">>>>> Server kiểm tra số nguyên tố đã sẵn sàng!");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

3. Cài đặt trên Client (RMIClient.java)
package com.rmi.prime.client;

import java.rmi.Naming;
import java.util.Scanner;
import com.rmi.prime.ICheckNumber;

public class RMIClient {
    public static void main(String[] args) {
        try {
            // 1. Tìm kiếm đối tượng từ xa trên Server
            ICheckNumber checker = (ICheckNumber) Naming.lookup("rmi://localhost:6789/PrimeChecker");

            // 2. Nhập dữ liệu từ bàn phím
            Scanner sc = new Scanner(System.in);
            System.out.print("Nhập vào một số để kiểm tra: ");
            int n = sc.nextInt();

            // 3. Triệu gọi phương thức từ xa
            if (checker.isPrime(n)) {
                System.out.println(n + " LÀ số nguyên tố.");
            } else {
                System.out.println(n + " KHÔNG PHẢI số nguyên tố.");
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

4. Giải thích kiến trúc và luồng chạy
Khi bạn chạy chương trình trên, quy trình diễn ra như sau:
 * Server khởi tạo một đối tượng thực thi và "treo" nó lên một cái tên (PrimeChecker) thông qua RMI Registry.
 * Client liên hệ với Registry để hỏi: "Tôi muốn tìm dịch vụ có tên PrimeChecker".
 * Registry trả về một Stub (lớp trung gian phía Client).
 * Khi Client gọi hàm isPrime(n), thực tế nó đang gọi thông qua Stub. Stub sẽ gói dữ liệu và gửi qua mạng đến Skeleton phía Server.
 * Server thực hiện tính toán và trả kết quả về cho Client một cách trong suốt (Client cảm thấy như đang gọi hàm trên máy mình).
Lưu ý khi làm bài kiểm tra:
 * RemoteException: Luôn phải throws hoặc try-catch ngoại lệ này vì giao tiếp mạng có thể đứt quãng.
 * Thứ tự chạy: Luôn chạy RMIServer trước, sau đó mới chạy RMIClient.
 * Cổng (Port): Trong ví dụ mình dùng cổng 6789, cổng mặc định của RMI là 1099. Bạn có thể đổi tùy ý nhưng Server và Client phải khớp nhau.
Bạn có muốn mình giải thích thêm về cách đóng gói các file này để chạy trên môi trường Eclipse không? Hay bạn muốn làm bài tập tiếp theo về Socket?
Would you like me to show you how to structure these files in Eclipse for testing?


Chào bạn, để hiểu RMI, bạn hãy tưởng tượng đây là quy trình "Đặt món ăn qua điện thoại".
 * Interface: Là cái Menu (Cả khách và nhà hàng đều phải có để biết món nào gọi là gì).
 * Implementation: Là Đầu bếp (Người thực sự nấu món ăn).
 * Server: Là Nhà hàng (Mở cửa, cắm đường dây điện thoại).
 * Client: Là Khách hàng (Gọi điện đặt món).
Dưới đây là giải thích chi tiết từng dòng và mối liên hệ giữa chúng.
FILE 1: ICheckNumber.java (Cái Menu - Hợp đồng)
File này quan trọng nhất. Cả Server và Client đều phải giữ file này giống hệt nhau.
public interface ICheckNumber extends Remote {
    public boolean isPrime(int n) throws RemoteException;
}

 * extends Remote: Đây là "con dấu" của Java. Nó báo cho Java biết rằng: "Interface này không dùng nội bộ, mà để dùng qua mạng".
 * throws RemoteException: Bắt buộc phải có. Vì khi gọi qua mạng (Network), có thể mạng bị rớt, dây cáp đứt... nên hàm này phải cảnh báo trước là "có thể sẽ lỗi đường truyền đấy".
FILE 2: CheckNumberImpl.java (Đầu bếp - Người làm việc)
Đây là file chỉ nằm ở Server. Client không cần biết file này, Client không quan tâm ai nấu, chỉ quan tâm món ăn (Interface).
// Kế thừa UnicastRemoteObject để đối tượng này có thể "sống" và chờ nhận lệnh từ xa
public class CheckNumberImpl extends UnicastRemoteObject implements ICheckNumber {

    // Constructor (Hàm khởi tạo)
    public CheckNumberImpl() throws RemoteException {
        super(); // Gọi lên cha (UnicastRemoteObject) để mở cổng kết nối ngầm
    }

    // Đây là nơi logic thực sự chạy
    @Override
    public boolean isPrime(int n) throws RemoteException {
        // ... (Code kiểm tra số nguyên tố) ...
        // Khi Client gọi hàm này, Server sẽ chạy đoạn code này và trả về true/false
        return true; 
    }
}

 * extends UnicastRemoteObject: Biến class Java bình thường thành một đối tượng RMI có thể gửi/nhận dữ liệu qua mạng TCP/IP.
 * implements ICheckNumber: Cam kết với "Hợp đồng" (Interface) là tôi sẽ thực hiện đúng hàm isPrime.
FILE 3: RMIServer.java (Cửa hàng - Nơi đăng ký)
File này để bật Server lên.
public class RMIServer {
    public static void main(String[] args) {
        try {
            // 1. Thuê đầu bếp (Tạo đối tượng thực thi logic)
            ICheckNumber checker = new CheckNumberImpl();

            // 2. Mở tổng đài điện thoại ở cổng 6789 (Tạo Registry)
            // Nếu không có dòng này, Client không biết gọi vào đâu.
            LocateRegistry.createRegistry(6789);

            // 3. Gán số điện thoại cho đầu bếp (Đăng ký tên dịch vụ)
            // Cú pháp: "rmi://[Địa chỉ máy]:[Cổng]/[Tên đặt cho dịch vụ]"
            // Ở đây ta đặt tên dịch vụ là "PrimeChecker"
            Naming.rebind("rmi://localhost:6789/PrimeChecker", checker);

            System.out.println("Server đã sẵn sàng...");
        } catch (Exception e) { ... }
    }
}

 * LocateRegistry.createRegistry(6789): Tạo ra một quyển danh bạ trên máy Server tại cổng 6789.
 * Naming.rebind(..., checker): Ghi vào danh bạ dòng chữ: "Ai muốn tìm dịch vụ có tên PrimeChecker thì hãy gặp ông checker (đầu bếp) để xử lý".
FILE 4: RMIClient.java (Khách hàng - Người gọi)
Client chỉ cần biết địa chỉ IP, Cổng và Tên dịch vụ (Tên món ăn).
public class RMIClient {
    public static void main(String[] args) {
        try {
            // 1. Tra cứu danh bạ để tìm người phục vụ
            // lookup: Tìm kiếm.
            // "rmi://localhost:6789/PrimeChecker": Địa chỉ cần tìm.
            // Kết quả trả về là một đối tượng chung chung (Remote), ta phải ép kiểu về (ICheckNumber).
            ICheckNumber checker = (ICheckNumber) Naming.lookup("rmi://localhost:6789/PrimeChecker");

            // 2. Gọi hàm (Thực chất là gửi tín hiệu qua mạng)
            // Dòng này nhìn như gọi hàm bình thường, nhưng thực tế nó đang gửi số 'n' qua mạng tới Server
            boolean ketQua = checker.isPrime(17);

            // 3. Nhận kết quả Server trả về
            if (ketQua) System.out.println("Là số nguyên tố");

        } catch (Exception e) { ... }
    }
}

 * Naming.lookup(...): Client gõ cửa Server (localhost:6789) và hỏi: "Cho tôi gặp dịch vụ tên là PrimeChecker".
 * Server trả về một cái "Remote Reference" (giống như đưa cái điều khiển từ xa cho Client).
 * checker.isPrime(17): Client bấm nút trên điều khiển. Lệnh bay về Server -> Server tính toán -> Server trả kết quả về Client.
MỐI LIÊN HỆ GIỮA CÁC FILE (Tóm tắt để dễ nhớ)
 * ICheckNumber (Interface): Là cầu nối. Cả RMIClient và CheckNumberImpl đều phải nhìn thấy file này. Nếu bạn sửa tên hàm ở đây mà không sửa ở 2 file kia -> Code báo lỗi đỏ lòm ngay.
 * RMIServer & CheckNumberImpl: RMIServer có nhiệm vụ "khởi động" CheckNumberImpl và gán cho nó cái tên "PrimeChecker".
 * RMIClient & RMIServer: Kết nối với nhau qua chuỗi URL: "rmi://localhost:6789/PrimeChecker".
   * Sai IP (localhost) -> Không tìm thấy máy.
   * Sai Cổng (6789) -> Không vào được nhà.
   * Sai Tên (PrimeChecker) -> Vào được nhà nhưng gọi nhầm người.
Bạn đã hiểu rõ luồng đi của dữ liệu chưa? Nó chạy vòng tròn: Client -> Interface -> Server (Impl) -> Interface -> Client.

