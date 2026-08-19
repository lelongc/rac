# BÀI 1: DANH SÁCH CÁC VIRTUAL / FAKE RESTFUL API HỖ TRỢ HÌNH ẢNH

Virtual RESTful API (hay Fake REST API / Mock API) là các dịch vụ API giả lập cung cấp sẵn dữ liệu mẫu JSON, hỗ trợ các lập trình viên Frontend kiểm thử các phương thức **GET, POST, PUT, DELETE, SEARCH** mà không cần phải tự dựng Database hay Server backend.

Dưới đây là các Virtual RESTful API hàng đầu hỗ trợ **hình ảnh sản phẩm / avatar / banner thực tế**:

---

## 1. 🌟 FakeStore API (Khuyên dùng nhất cho ứng dụng thương mại / quảng cáo sản phẩm)
- **Website**: [https://fakestoreapi.com](https://fakestoreapi.com)
- **Endpoint Sản phẩm**: `https://fakestoreapi.com/products`
- **Mô tả**: Cung cấp đầy đủ thông tin sản phẩm bán lẻ (thời trang, đồ điện tử, trang sức) kèm link ảnh thật chất lượng cao. Hỗ trợ đầy đủ các phương thức HTTP RESTful.
- **Cấu trúc JSON mẫu**:
```json
[
  {
    "id": 1,
    "title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
    "price": 109.95,
    "description": "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve...",
    "category": "men's clothing",
    "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_.jpg",
    "rating": {
      "rate": 3.9,
      "count": 120
    }
  }
]
```
- **Các Endpoint hỗ trợ**:
  - `GET /products`: Lấy tất cả danh sách sản phẩm.
  - `GET /products/1`: Lấy chi tiết sản phẩm theo ID.
  - `GET /products?limit=5`: Phân trang / Giới hạn số lượng.
  - `GET /products/categories`: Lấy danh sách phân loại danh mục.
  - `GET /products/category/jewelery`: Lọc theo danh mục.
  - `POST /products`: Giả lập thêm sản phẩm mới.
  - `PUT /products/1`: Giả lập cập nhật sản phẩm.
  - `DELETE /products/1`: Giả lập xóa sản phẩm.

---

## 2. ⚡ DummyJSON (Cực kỳ mạnh mẽ, hỗ trợ Search, Paging & Nhiều ảnh)
- **Website**: [https://dummyjson.com](https://dummyjson.com)
- **Endpoint Sản phẩm**: `https://dummyjson.com/products`
- **Mô tả**: Hỗ trợ tìm kiếm theo từ khóa (`/products/search?q=phone`), sắp xếp, phân trang và có mảng nhiều ảnh (`images`) kèm ảnh đại diện (`thumbnail`).
- **Cấu trúc JSON mẫu**:
```json
{
  "products": [
    {
      "id": 1,
      "title": "iPhone 9",
      "description": "An apple mobile which is nothing like apple",
      "price": 549,
      "discountPercentage": 12.96,
      "rating": 4.69,
      "stock": 94,
      "brand": "Apple",
      "category": "smartphones",
      "thumbnail": "https://cdn.dummyjson.com/product-images/1/thumbnail.jpg",
      "images": [
        "https://cdn.dummyjson.com/product-images/1/1.jpg",
        "https://cdn.dummyjson.com/product-images/1/2.jpg"
      ]
    }
  ],
  "total": 100,
  "skip": 0,
  "limit": 30
}
```

---

## 3. 🛍️ Platzi Fake Store API
- **Website**: [https://fakeapi.platzi.com](https://fakeapi.platzi.com)
- **Endpoint**: `https://api.escuelajs.co/api/v1/products`
- **Mô tả**: Chuẩn REST API thế hệ mới, hỗ trợ CRUD thực tế, upload file ảnh và lọc theo danh mục / khoảng giá.
- **Cấu trúc JSON mẫu**:
```json
[
  {
    "id": 4,
    "title": "Handmade Fresh Table",
    "price": 687,
    "description": "Andy shoes are designed to keeping in mind durability as well as style...",
    "category": {
      "id": 1,
      "name": "Clothes",
      "image": "https://i.imgur.com/QkIa5tT.jpeg"
    },
    "images": [
      "https://i.imgur.com/solgGQp.jpeg"
    ]
  }
]
```

---

## 4. 🖼️ JSONPlaceholder Photos
- **Website**: [https://jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com)
- **Endpoint**: `https://jsonplaceholder.typicode.com/photos`
- **Mô tả**: Thư viện API giả lập phổ biến nhất thế giới với 5000 đối tượng hình ảnh placeholder mẫu.
- **Cấu trúc JSON mẫu**:
```json
[
  {
    "albumId": 1,
    "id": 1,
    "title": "accusamus beatae ad facilis cum similique qui sunt",
    "url": "https://via.placeholder.com/600/92c952",
    "thumbnailUrl": "https://via.placeholder.com/150/92c952"
  }
]
```

---

## 5. 🛠️ MockAPI.io (Tự định nghĩa Virtual API theo ý muốn)
- **Website**: [https://mockapi.io](https://mockapi.io)
- **Mô tả**: Cho phép tự tạo schema linh hoạt (tên trường tùy chọn: `id`, `name`, `price`, `image`, `avatar`, `description`). Dữ liệu sẽ lưu trữ trực tiếp trên database đám mây và hỗ trợ CRUD thực tế lưu trạng thái thật.

---

## 6. 📸 Các API hình ảnh bổ trợ khác:
- **Lorem Picsum**: `https://picsum.photos/v2/list` (Kho ảnh nghệ thuật độ phân giải cao).
- **The Cat API**: `https://api.thecatapi.com/v1/images/search` (Ảnh mèo ngẫu nhiên).
- **The Dog API**: `https://api.thedogapi.com/v1/images/search` (Ảnh chó ngẫu nhiên).
- **Unsplash Source**: `https://source.unsplash.com/random/400x300` (Hình ảnh theo chủ đề).
