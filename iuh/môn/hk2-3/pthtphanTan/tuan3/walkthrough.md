# Hướng dẫn chạy chương trình (Update cho Eclipse Project)

Hệ thống bài tập đã được chuyển vào dự án Eclipse tại thư mục `tuan3gk`.

**Cấu trúc thư mục mới**: `d:\folder\rac\iuh\môn\hk2-3\pthtphanTan\tuan3\tuan3gk`

## Cách 1: Chạy trên Eclipse (Khuyên dùng)
1.  Mở Eclipse.
2.  **File** > **Open Projects from File System...**
3.  Chọn thư mục: `d:\folder\rac\iuh\môn\hk2-3\pthtphanTan\tuan3\tuan3gk`.
4.  Nhấn **Finish**.
5.  Mở `src` > `Bai1...` hoặc `Bai5...`, chuột phải vào file Server/Client và chọn **Run As** > **Java Application**.

## Cách 2: Chạy bằng dòng lệnh (CMD)
Di chuyển vào thư mục dự án:
```cmd
cd "d:\folder\rac\iuh\môn\hk2-3\pthtphanTan\tuan3\tuan3gk"
```

### Bài 1 - Bài 4
Biên dịch và chạy (Ví dụ Bài 1):
```cmd
javac -d bin src/Bai1_ReverseString/*.java
java -cp bin Bai1_ReverseString.Server
java -cp bin Bai1_ReverseString.Client
```

### Bài 5: Tìm sản phẩm (MySQL)
1.  **Chuẩn bị DB**:
    ```cmd
    docker exec -i product-mysql-db mysql -u root -proot productdb < src/Bai5_ProductDB/init.sql
    ```

2.  **Biên dịch**:
    ```cmd
    javac -cp ".;src/Bai5_ProductDB/lib/mysql-connector-j-8.3.0.jar" -d bin src/Bai5_ProductDB/*.java
    ```

3.  **Chạy TCP**:
    *   Server: `java -cp "bin;src/Bai5_ProductDB/lib/mysql-connector-j-8.3.0.jar" Bai5_ProductDB.ProductServer`
    *   Client: `java -cp "bin;src/Bai5_ProductDB/lib/mysql-connector-j-8.3.0.jar" Bai5_ProductDB.ProductClient`

4.  **Chạy UDP**:
    *   Server: `java -cp "bin;src/Bai5_ProductDB/lib/mysql-connector-j-8.3.0.jar" Bai5_ProductDB.ProductUDPServer`
    *   Client: `java -cp "bin;src/Bai5_ProductDB/lib/mysql-connector-j-8.3.0.jar" Bai5_ProductDB.ProductUDPClient`
