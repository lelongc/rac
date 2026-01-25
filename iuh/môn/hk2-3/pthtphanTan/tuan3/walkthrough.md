# Hướng dẫn chạy chương trình Socket TCP

Tôi đã hoàn thành 5 bài tập theo yêu cầu, mỗi bài nằm trong một thư mục riêng biệt tại `d:\folder\rac\iuh\môn\hk2-3\pthtphanTan\tuan3`.

## Danh sách bài tập
1.  **Bai1_ReverseString**: Đảo ngược chuỗi.
2.  **Bai2_SortNumbers**: Sắp xếp dãy số.
3.  **Bai3_FindPrimes**: Tìm số nguyên tố.
4.  **Bai4_WordCount**: Đếm tần suất từ.
5.  **Bai5_ProductDB**: Tìm kiếm sản phẩm (Mock DB).

## Cách chạy (Sử dụng dòng lệnh)

Các bài tập nằm trong `package`, vì vậy bạn cần đứng ở thư mục gốc `d:\folder\rac\iuh\môn\hk2-3\pthtphanTan\tuan3` để biên dịch và chạy.

### Bước 1: Mở CMD hoặc Terminal
Di chuyển đến thư mục gốc:
```cmd
cd "d:\folder\rac\iuh\môn\hk2-3\pthtphanTan\tuan3"
```

### Bước 2: Biên dịch và chạy từng bài
**Lưu ý**: Bạn cần chạy **Server** trước, sau đó mở một cửa sổ CMD khác để chạy **Client**.

#### Bài 1: Đảo chuỗi
1.  Biên dịch: `javac Bai1_ReverseString/*.java`
2.  Chạy Server: `java Bai1_ReverseString.Server`
3.  Chạy Client: `java Bai1_ReverseString.Client`

#### Bài 2: Sắp xếp số
1.  Biên dịch: `javac Bai2_SortNumbers/*.java`
2.  Chạy Server: `java Bai2_SortNumbers.Server`
3.  Chạy Client: `java Bai2_SortNumbers.Client` (Nhập dãy số ví dụ: `5,1,9,2`)

#### Bài 3: Tìm số nguyên tố
1.  Biên dịch: `javac Bai3_FindPrimes/*.java`
2.  Chạy Server: `java Bai3_FindPrimes.Server`
3.  Chạy Client: `java Bai3_FindPrimes.Client` (Nhập dãy số ví dụ: `12, 5, 7`)

#### Bài 4: Đếm từ
1.  Biên dịch: `javac Bai4_WordCount/*.java`
2.  Chạy Server: `java Bai4_WordCount.Server`
3.  Chạy Client: `java Bai4_WordCount.Client`

#### Bài 5: Tìm sản phẩm (MySQL + TCP & UDP)
Bài này sử dụng cơ sở dữ liệu MySQL chạy trong Docker.

1.  **Chuẩn bị Database**:
    *   Đảm bảo Docker đang chạy container `product-mysql-db`.
    *   Nạp dữ liệu mẫu:
        ```cmd
        docker exec -i product-mysql-db mysql -u root -proot productdb < Bai5_ProductDB/init.sql
        ```

2.  **Biên dịch**:
    ```cmd
    javac -cp ".;Bai5_ProductDB/lib/mysql-connector-j-8.3.0.jar" -d Bai5_ProductDB/bin Bai5_ProductDB/src/*.java
    ```

3.  **Chạy TCP**:
    *   Server: `java -cp "Bai5_ProductDB/bin;Bai5_ProductDB/lib/mysql-connector-j-8.3.0.jar" ProductServer`
    *   Client: `java -cp "Bai5_ProductDB/bin;Bai5_ProductDB/lib/mysql-connector-j-8.3.0.jar" ProductClient`

4.  **Chạy UDP**:
    *   Server: `java -cp "Bai5_ProductDB/bin;Bai5_ProductDB/lib/mysql-connector-j-8.3.0.jar" ProductUDPServer`
    *   Client: `java -cp "Bai5_ProductDB/bin;Bai5_ProductDB/lib/mysql-connector-j-8.3.0.jar" ProductUDPClient`

## Ghi chú
- Code Server và Client đã được comment chi tiết từng bước (Tạo socket, luồng IO, xử lý logic, đóng kết nối) để dễ dàng theo dõi và học tập.
- Server chạy vòng lặp `while(true)` để có thể nhận liên tiếp các kết nối từ Client (từng cái một).
