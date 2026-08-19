# HƯỚNG DẪN BÀI 1 & BÀI 2 (TUẦN 2) - QUẢNG CÁO SẢN PHẨM VỚI VIRTUAL RESTFUL API

---

## 📌 BÀI 1: TÌM VIRTUAL RESTFUL API CÓ HỖ TRỢ HÌNH ẢNH
*(Xem chi tiết đầy đủ tại file [DANH_SACH_VIRTUAL_API.md](DANH_SACH_VIRTUAL_API.md))*

Các Virtual RESTful API phổ biến và tốt nhất hiện nay:
1. **FakeStore API**: `https://fakestoreapi.com/products` (Hỗ trợ hình ảnh sản phẩm thời trang, trang sức, điện tử; hỗ trợ đầy đủ GET, POST, PUT, DELETE).
2. **DummyJSON**: `https://dummyjson.com/products` (Hỗ trợ tìm kiếm, phân trang, thumbnail và mảng ảnh `images`).
3. **Platzi Fake Store API**: `https://api.escuelajs.co/api/v1/products` (RESTful thế hệ mới có category & images).
4. **JSONPlaceholder Photos**: `https://jsonplaceholder.typicode.com/photos` (API ảnh placeholder kinh điển).
5. **MockAPI.io**: `https://mockapi.io` (Tự thiết kế fake API có lưu dữ liệu thật trên đám mây).

---

## 🚀 BÀI 2: ỨNG DỤNG QUẢNG CÁO SẢN PHẨM (SINGLE PAGE APP - CRUD & TÌM KIẾM)

Dự án **`b4_product_ads`** là ứng dụng độc lập hoàn chỉnh đáp ứng đầy đủ yêu cầu:
- **Hiển thị sản phẩm dạng Card/Banner quảng cáo**: Tên, Giá bán, Danh mục (Badge), Ảnh thực tế, Mô tả.
- **Lựa chọn nguồn API linh hoạt**: Có thể chuyển đổi tức thì giữa **FakeStore API**, **DummyJSON**, **JSONPlaceholder** hoặc **Local Server**.
- **Chức năng Tìm kiếm (Search)**: Tìm kiếm sản phẩm theo từ khóa theo thời gian thực (real-time).
- **Chức năng Lọc (Filter)**: Lọc theo từng danh mục sản phẩm (Electronics, Fashion, Jewelery, v.v.).
- **Chức năng Thêm mới (POST)**: Form Modal thêm sản phẩm kèm xem trước ảnh (preview image).
- **Chức năng Sửa (PUT)**: Chỉnh sửa thông tin sản phẩm và cập nhật giao diện.
- **Chức năng Xóa (DELETE)**: Xóa sản phẩm khỏi danh sách có hộp thoại xác nhận.
- **Khung Log JSON Response**: Hiển thị kết quả JSON trả về từ API mỗi khi thực hiện thao tác.

---

## 🏃 HƯỚNG DẪN CHẠY VÀ TEST TRONG ECLIPSE:

1. **Import vào Eclipse**:
   - Mở Eclipse ➔ `File` ➔ `Import...` ➔ `General` ➔ `Existing Projects into Workspace` (hoặc `Projects from Folder or Archive`).
   - Chọn thư mục: `d:\folder\rac\iuh\môn\hk1-4\cc-web-website-hld\truong\bt\t2\b4_product_ads`.
   - Bấm **Finish**.

2. **Chạy ứng dụng**:
   - Mở file `src/api/ServerB4.java`.
   - Nhấp chuột phải ➔ chọn **Run As ➔ Java Application**.
   - Mở trình duyệt web truy cập: **`http://localhost:8084/index.html`**

3. **Chạy trực tiếp trên trình duyệt (không cần Eclipse)**:
   - Bạn cũng có thể mở trực tiếp file `WebContent/index.html` bằng trình duyệt (Chrome, Edge) hoặc Live Server để test các Virtual API online như FakeStoreAPI, DummyJSON, JSONPlaceholder!
