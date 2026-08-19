const API_BASE = "/api/products";

// 1. GET ALL (Lấy tất cả danh sách sản phẩm)
function btnGetAll() {
    $.ajax({
        url: API_BASE,
        type: "GET",
        dataType: "json",
        success: function(data) {
            showJsonResponse(data);
            renderTableWithDOM(data);
        },
        error: function(err) { showJsonResponse(err); }
    });
}

// 2. GET BY ID (Tìm kiếm theo ID)
function btnGetById() {
    let id = document.getElementById("p-id").value.trim();
    if (!id) {
        alert("Vui lòng nhập Mã sản phẩm (ID) để tìm!");
        return;
    }
    $.ajax({
        url: `${API_BASE}?id=${encodeURIComponent(id)}`,
        type: "GET",
        dataType: "json",
        success: function(data) {
            showJsonResponse(data);
            if (data.id) {
                fillForm(data);
                renderTableWithDOM([data]);
            }
        },
        error: function(err) { showJsonResponse(err); }
    });
}

// 3. POST (Thêm mới sản phẩm)
function btnPost() {
    let id = document.getElementById("p-id").value.trim();
    let name = document.getElementById("p-name").value.trim();
    let price = document.getElementById("p-price").value;
    let quantity = document.getElementById("p-qty").value;
    let category = document.getElementById("p-cat").value.trim();

    if (!id || !name) {
        alert("Vui lòng nhập đầy đủ Mã SP (ID) và Tên sản phẩm!");
        return;
    }

    $.ajax({
        url: API_BASE,
        type: "POST",
        data: { id: id, name: name, price: price, quantity: quantity, category: category },
        dataType: "json",
        success: function(res) {
            showJsonResponse(res);
            btnGetAll(); // Reload lại bảng
        },
        error: function(err) { showJsonResponse(err); }
    });
}

// 4. PUT (Cập nhật sản phẩm)
function btnPut() {
    let id = document.getElementById("p-id").value.trim();
    let name = document.getElementById("p-name").value.trim();
    let price = document.getElementById("p-price").value;
    let quantity = document.getElementById("p-qty").value;
    let category = document.getElementById("p-cat").value.trim();

    if (!id) {
        alert("Vui lòng nhập Mã SP (ID) cần cập nhật!");
        return;
    }

    $.ajax({
        url: `${API_BASE}?id=${encodeURIComponent(id)}&name=${encodeURIComponent(name)}&price=${price}&quantity=${quantity}&category=${encodeURIComponent(category)}`,
        type: "PUT",
        dataType: "json",
        success: function(res) {
            showJsonResponse(res);
            btnGetAll(); // Reload lại bảng
        },
        error: function(err) { showJsonResponse(err); }
    });
}

// 5. DELETE (Xóa sản phẩm)
function btnDelete() {
    let id = document.getElementById("p-id").value.trim();
    if (!id) {
        alert("Vui lòng nhập Mã SP (ID) cần xóa!");
        return;
    }

    if (!confirm(`Bạn có chắc muốn xóa sản phẩm ${id}?`)) return;

    $.ajax({
        url: `${API_BASE}?id=${encodeURIComponent(id)}`,
        type: "DELETE",
        dataType: "json",
        success: function(res) {
            showJsonResponse(res);
            btnGetAll(); // Reload lại bảng
        },
        error: function(err) { showJsonResponse(err); }
    });
}

// Helper: Hiển thị chuỗi JSON nhận được lên khung đen
function showJsonResponse(data) {
    document.getElementById("json-response").innerText = JSON.stringify(data, null, 2);
}

// Helper: Tự động điền thông tin lên Form khi chọn dòng trong bảng
function fillForm(item) {
    document.getElementById("p-id").value = item.id || "";
    document.getElementById("p-name").value = item.name || "";
    document.getElementById("p-price").value = item.price || "";
    document.getElementById("p-qty").value = item.quantity || "";
    document.getElementById("p-cat").value = item.category || "";
}

// Render dữ liệu ra thẻ <table> bằng JavaScript DOM thuần
function renderTableWithDOM(list) {
    let tbody = document.getElementById("table-body");
    tbody.innerHTML = "";

    if (!Array.isArray(list)) list = [list];

    list.forEach(p => {
        if (!p || !p.id) return;
        let row = document.createElement("tr");

        row.innerHTML = `
            <td><strong>${p.id}</strong></td>
            <td>${p.name}</td>
            <td>${Number(p.price).toLocaleString("vi-VN")}</td>
            <td>${p.quantity}</td>
            <td>${p.category}</td>
            <td>
                <button class="btn-action" style="background:#ffc107; color:#000;" onclick='fillForm(${JSON.stringify(p)})'>Sửa</button>
                <button class="btn-action" style="background:#dc3545; color:#fff;" onclick='deleteQuick("${p.id}")'>Xóa</button>
            </td>
        `;
        tbody.appendChild(row);
    });
}

function deleteQuick(id) {
    document.getElementById("p-id").value = id;
    btnDelete();
}

// Tự động tải danh sách ban đầu khi mở web
window.onload = btnGetAll;
