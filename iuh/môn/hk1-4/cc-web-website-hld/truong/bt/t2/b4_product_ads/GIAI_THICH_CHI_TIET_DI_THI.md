# 📚 TÀI LIỆU ÔN TẬP VÀ GIẢI THÍCH CHI TIẾT TỪNG DÒNG CODE ĐI THI (BÀI 4 - RESTFUL API & JQUERY AJAX)

Tài liệu này được biên soạn dành riêng để **đi thi, chép code và trả lời vấn đáp** môn Công cụ Web & Website hướng dữ liệu. Mọi đoạn code cốt lõi đều được giải thích rõ ràng ý nghĩa, mục đích và cú pháp.

---

## 📑 MỤC LỤC
1. [Khái niệm cốt lõi bắt buộc phải thuộc lòng](#1-khái-niệm-cốt-lõi-bắt-buộc-phải-thuộc-lòng)
2. [Giải thích chi tiết mã nguồn JavaScript / jQuery (`app.js`)](#2-giải-thích-chi-tiết-mã-nguồn-javascript--jquery-appjs)
   - [2.1. Cấu trúc hàm `$.ajax()` mẫu](#21-cấu-trúc-hàm-ajax-mẫu)
   - [2.2. Phương thức GET (Lấy danh sách dữ liệu)](#22-phương-thức-get-lấy-danh-sách-dữ-liệu)
   - [2.3. Phương thức POST (Thêm mới dữ liệu)](#23-phương-thức-post-thêm-mới-dữ-liệu)
   - [2.4. Phương thức PUT (Cập nhật dữ liệu)](#24-phương-thức-put-cập-nhật-dữ-liệu)
   - [2.5. Phương thức DELETE (Xóa dữ liệu)](#25-phương-thức-delete-xóa-dữ-liệu)
   - [2.6. Xử lý Tìm kiếm Real-time (Filter Search)](#26-xử-lý-tìm-kiếm-real-time-filter-search)
   - [2.7. Xử lý vẽ giao diện DOM (Render HTML)](#27-xử-lý-vẽ-giao-diện-dom-render-html)
3. [Giải thích chi tiết mã nguồn Java Backend (`ServerB4.java`)](#3-giải-thích-chi-tiết-mã-nguồn-java-backend-serverb4java)
4. [Bộ câu hỏi vấn đáp thường gặp nhất khi thi](#4-bộ-câu-hỏi-vấn-đáp-thường-gặp-nhất-khi-thi)

---

## 1. KHÁI NIỆM CỐT LÕI BẮT BUỘC PHẢI THUỘC LÒNG

| Khái niệm | Ý nghĩa trả lời giáo viên |
| :--- | :--- |
| **RESTful API** | Là chuẩn kiến trúc giao tiếp giữa Client và Server qua giao thức HTTP, trao đổi dữ liệu định dạng **JSON** (thay vì trả về trang HTML). |
| **4 HTTP Verbs (CRUD)** | • **GET**: Đọc / Lấy dữ liệu.<br>• **POST**: Thêm mới dữ liệu.<br>• **PUT**: Cập nhật / Sửa dữ liệu.<br>• **DELETE**: Xóa dữ liệu. |
| **AJAX (Asynchronous JavaScript and XML)** | Kỹ thuật gửi yêu cầu ngầm bất đồng bộ từ trình duyệt lên server để lấy dữ liệu mà **không làm load/tải lại toàn bộ trang web**. |
| **DOM (Document Object Model)** | Mô hình cây phân cấp các thẻ HTML của trang web, cho phép JavaScript truy xuất, thay đổi nội dung, thêm xóa phần tử giao diện linh hoạt. |
| **CORS (Cross-Origin Resource Sharing)** | Cơ chế bảo mật của trình duyệt ngăn chặn gọi API từ domain khác; server cần cấp header `Access-Control-Allow-Origin: *` để client gọi được. |

---

## 2. GIẢI THÍCH CHI TIẾT MÃ NGUỒN JAVASCRIPT / JQUERY (`app.js`)

### 2.1. Cấu trúc hàm `$.ajax()` mẫu:
Khi giáo viên yêu cầu viết hàm gọi API bằng jQuery, hãy chép mẫu này:
```javascript
$.ajax({
    url: "https://fakestoreapi.com/products", // 1. Đường dẫn Endpoint API
    type: "GET",                              // 2. Phương thức HTTP (GET, POST, PUT, DELETE)
    data: { name: "iPhone", price: 1000 },    // 3. Dữ liệu gửi lên server (dành cho POST, PUT)
    dataType: "json",                         // 4. Định dạng dữ liệu server trả về mong đợi là JSON
    success: function(response) {             // 5. Hàm callback khi server phản hồi thành công (mã 200/201)
        console.log("Thành công:", response);
    },
    error: function(xhr, status, error) {     // 6. Hàm callback khi có lỗi xảy ra (mã 400, 404, 500...)
        console.error("Lỗi:", error);
    }
});
```

---

### 2.2. Phương thức GET (Lấy danh sách dữ liệu):
```javascript
function loadProducts() {
    // Gọi AJAX phương thức GET
    $.ajax({
        url: "https://fakestoreapi.com/products",
        type: "GET",
        dataType: "json",
        success: function(data) {
            // data nhận về là một mảng [] các đối tượng sản phẩm JSON
            allProducts = data;          // Lưu mảng vào biến toàn cục để dùng khi tìm kiếm
            renderProducts(allProducts); // Gọi hàm vẽ dữ liệu ra màn hình
        },
        error: function(err) {
            alert("Lỗi khi tải dữ liệu từ API!");
        }
    });
}
```
- **Ý nghĩa**: Gửi request `GET` đến endpoint. Khi server trả về danh sách sản phẩm dạng JSON, lưu vào mảng `allProducts` và gọi hàm `renderProducts()` để đưa ra giao diện.

---

### 2.3. Phương thức POST (Thêm mới dữ liệu):
```javascript
function addProduct(newTitle, newPrice, newCategory, newImage, newDesc) {
    // 1. Gom dữ liệu từ Form thành một đối tượng JavaScript Payload
    const payload = {
        title: newTitle,
        price: parseFloat(newPrice),
        category: newCategory,
        image: newImage,
        description: newDesc
    };

    // 2. Gửi AJAX POST lên Server
    $.ajax({
        url: "https://fakestoreapi.com/products",
        type: "POST",
        data: payload,          // Dữ liệu gửi kèm trong Request Body
        dataType: "json",
        success: function(res) {
            // Server trả về sản phẩm vừa tạo (kèm ID mới sinh ra)
            allProducts.unshift(res);     // Thêm sản phẩm mới vào đầu danh sách
            renderProducts(allProducts);  // Vẽ lại giao diện
            alert("Thêm sản phẩm mới thành công!");
        },
        error: function(err) {
            alert("Thêm thất bại!");
        }
    });
}
```
- **Ý nghĩa**: Thu thập thông tin từ các ô nhập liệu, đóng gói vào `payload`, gửi lên bằng method `POST`. Khi nhận kết quả thành công thì chèn vào mảng và cập nhật lại giao diện.

---

### 2.4. Phương thức PUT (Cập nhật dữ liệu):
```javascript
function updateProduct(id, updatedTitle, updatedPrice, updatedCategory, updatedDesc) {
    const payload = {
        title: updatedTitle,
        price: parseFloat(updatedPrice),
        category: updatedCategory,
        description: updatedDesc
    };

    // Gửi AJAX PUT kèm ID sản phẩm trên đường dẫn URL
    $.ajax({
        url: "https://fakestoreapi.com/products/" + id,
        type: "PUT",
        data: payload,
        dataType: "json",
        success: function(res) {
            // Tìm sản phẩm trong mảng theo ID và cập nhật lại
            const index = allProducts.findIndex(p => p.id == id);
            if (index !== -1) {
                allProducts[index] = { ...allProducts[index], ...payload };
                renderProducts(allProducts);
            }
            alert("Cập nhật sản phẩm #" + id + " thành công!");
        },
        error: function(err) {
            alert("Lỗi cập nhật sản phẩm!");
        }
    });
}
```
- **Ý nghĩa**: Dùng method `PUT` để ghi đè thông tin của tài nguyên có mã `id`. Sau đó tìm đúng vị trí index trong mảng để cập nhật lại dữ liệu hiển thị.

---

### 2.5. Phương thức DELETE (Xóa dữ liệu):
```javascript
function deleteProduct(id) {
    // 1. Hỏi người dùng xác nhận trước khi xóa
    if (!confirm("Bạn có chắc chắn muốn xóa sản phẩm #" + id + "?")) return;

    // 2. Gửi AJAX DELETE với mã ID trên URL
    $.ajax({
        url: "https://fakestoreapi.com/products/" + id,
        type: "DELETE",
        dataType: "json",
        success: function(res) {
            // Lọc bỏ sản phẩm đã xóa ra khỏi mảng
            allProducts = allProducts.filter(p => p.id != id);
            renderProducts(allProducts); // Vẽ lại giao diện
            alert("Đã xóa sản phẩm #" + id);
        },
        error: function(err) {
            alert("Xóa thất bại!");
        }
    });
}
```
- **Ý nghĩa**: Gửi request `DELETE` đến `/products/id`. Trong hàm `success`, dùng hàm `Array.filter()` để loại bỏ sản phẩm có `p.id == id` ra khỏi mảng rồi vẽ lại danh sách.

---

### 2.6. Xử lý Tìm kiếm Real-time (Filter Search):
```javascript
function handleSearch() {
    // 1. Lấy từ khóa người dùng gõ, chuyển về chữ thường và xóa khoảng trắng thừa
    const keyword = document.getElementById("search-input").value.trim().toLowerCase();

    // 2. Dùng hàm filter() lọc danh sách theo tiêu đề hoặc mô tả
    const filtered = allProducts.filter(p => {
        const titleMatch = p.title.toLowerCase().includes(keyword);
        const descMatch = (p.description || "").toLowerCase().includes(keyword);
        return titleMatch || descMatch;
    });

    // 3. Render danh sách đã lọc ra màn hình
    renderProducts(filtered);
}
```
- **Ý nghĩa**: Gắn vào sự kiện `onkeyup` của thẻ `<input>`. Mỗi khi người dùng gõ phím, hàm `includes()` sẽ kiểm tra xem từ khóa có nằm trong tên hoặc mô tả sản phẩm hay không.

---

### 2.7. Xử lý vẽ giao diện DOM (Render HTML):
```javascript
function renderProducts(list) {
    // 1. Lấy thẻ chứa container
    const container = document.getElementById("products-grid");
    container.innerHTML = ""; // Xóa sạch nội dung cũ để vẽ lại

    // 2. Duyệt qua từng sản phẩm trong mảng
    list.forEach(p => {
        // Tạo thẻ div đại diện cho 1 card
        const card = document.createElement("div");
        card.className = "product-card";

        // Gắn nội dung HTML vào card
        card.innerHTML = `
            <div class="card-img-wrap">
                <img src="${p.image}" alt="${p.title}" onerror="this.src='https://via.placeholder.com/150'">
            </div>
            <div class="card-body">
                <h4>${p.title}</h4>
                <div class="card-price">$${p.price}</div>
                <p>${p.description}</p>
                <div class="card-actions">
                    <button onclick="openEditModal(${p.id})">Sửa</button>
                    <button onclick="deleteProduct(${p.id})">Xóa</button>
                </div>
            </div>
        `;

        // Đưa card vào container
        container.appendChild(card);
    });
}
```
- **Ý nghĩa**:
  - `document.createElement("div")`: Tạo phần tử HTML mới bằng mã JS.
  - `onerror="this.src='...'"`: Nếu link ảnh bị chết/lỗi mạng thì tự động chuyển sang ảnh mặc định placeholder.
  - `container.appendChild(card)`: Gắn phần tử card con vào thẻ cha container trên trang web.

---

## 3. GIẢI THÍCH CHI TIẾT MÃ NGUỒN JAVA BACKEND (`ServerB4.java`)

Nếu giáo viên hỏi về code Java Backend:

```java
// 1. Khởi tạo HTTP Server lắng nghe tại cổng 8084
HttpServer server = HttpServer.create(new InetSocketAddress(8084), 0);

// 2. Đăng ký Endpoint phục vụ file Web tĩnh (HTML/CSS/JS)
server.createContext("/", new StaticHandler());

// 3. Đăng ký Endpoint RESTful API
server.createContext("/api/products", new LocalApiHandler());

// 4. Bắt đầu lắng nghe kết nối
server.start();
```

Trong hàm xử lý `handle(HttpExchange exchange)`:
```java
// Lấy phương thức HTTP gửi lên (GET, POST, PUT, DELETE)
String method = exchange.getRequestMethod().toUpperCase();

// Cấu hình CORS để trình duyệt không bị chặn gọi API
exchange.getResponseHeaders().set("Access-Control-Allow-Origin", "*");
exchange.getResponseHeaders().set("Content-Type", "application/json; charset=UTF-8");

if ("GET".equals(method)) {
    // Trả về chuỗi danh sách JSON
    String json = "[{\"id\":1,\"title\":\"Laptop\",\"price\":20000000}]";
    byte[] bytes = json.getBytes(StandardCharsets.UTF_8);
    exchange.sendResponseHeaders(200, bytes.length); // Mã 200 OK
    exchange.getResponseBody().write(bytes);
}
```

---

## 4. BỘ CÂU HỎI VẤN ĐÁP THƯỜNG GẶP NHẤT KHI THI

### ❓ Câu 1: Tại sao phải dùng `$.ajax()` mà không dùng `<form action="..." method="POST">` thông thường?
👉 **Trả lời**: Dùng thẻ `<form>` thông thường sẽ khiến trình duyệt phải tải lại toàn bộ trang web (reload trang), làm gián đoạn trải nghiệm người dùng. Dùng `$.ajax()` giúp gửi request và nhận dữ liệu ngầm bất đồng bộ (Asynchronous), chỉ cập nhật đúng phần giao diện cần thay đổi (Single Page App).

### ❓ Câu 2: Phân biệt sự khác nhau giữa phương thức POST và PUT?
👉 **Trả lời**:
- **POST**: Dùng để **tạo mới** một tài nguyên (Server sẽ tự sinh ID mới cho đối tượng).
- **PUT**: Dùng để **cập nhật/ghi đè** toàn bộ thông tin của một tài nguyên **đã tồn tại** (cần truyền kèm ID xác định đối tượng cần sửa).

### ❓ Câu 3: Ý nghĩa của các mã phản hồi HTTP Status Code thông dụng?
👉 **Trả lời**:
- **`200 OK`**: Yêu cầu thành công (thường dùng cho GET, PUT, DELETE).
- **`201 Created`**: Tạo mới tài nguyên thành công (thường dùng cho POST).
- **`400 Bad Request`**: Dữ liệu gửi lên sai định dạng hoặc thiếu trường bắt buộc.
- **`404 Not Found`**: Không tìm thấy Endpoint hoặc ID tài nguyên.
- **`500 Internal Server Error`**: Lỗi logic từ phía máy chủ backend.

### ❓ Câu 4: Làm thế nào để lọc tìm kiếm không phân biệt chữ hoa, chữ thường trong JavaScript?
👉 **Trả lời**: Chuyển cả từ khóa tìm kiếm và chuỗi cần tìm về chữ thường bằng hàm `.toLowerCase()`, sau đó dùng hàm `.includes(keyword)` để kiểm tra:
```javascript
const isMatch = product.title.toLowerCase().includes(keyword.toLowerCase());
```

---
*Chúc bạn ôn tập tốt và đạt điểm tối đa trong kỳ thi!*
