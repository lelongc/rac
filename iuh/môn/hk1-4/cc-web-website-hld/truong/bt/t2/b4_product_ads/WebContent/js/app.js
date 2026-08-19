// Cac nguon Virtual RESTful API
const API_CONFIG = {
    fakestore: {
        url: "https://fakestoreapi.com/products",
        name: "FakeStore API"
    },
    dummyjson: {
        url: "https://dummyjson.com/products",
        name: "DummyJSON"
    },
    jsonplaceholder: {
        url: "https://jsonplaceholder.typicode.com/photos?_limit=24",
        name: "JSONPlaceholder Photos"
    },
    local: {
        url: "/api/products",
        name: "Local Java Server"
    }
};

let currentSourceKey = "fakestore";
let allProducts = [];      // Danh sach san pham hien tai trong bo nho
let filteredProducts = []; // Danh sach sau khi search/filter

// Khi tai xong trang web
window.onload = function() {
    changeApiSource();
};

// 1. Chuyen doi nguon API
function changeApiSource() {
    currentSourceKey = document.getElementById("api-source").value;
    const config = API_CONFIG[currentSourceKey];
    document.getElementById("api-url-display").innerText = config.url;
    loadProducts();
}

// 2. GET: Lay danh sach san pham tu Virtual API
function loadProducts() {
    const config = API_CONFIG[currentSourceKey];
    setLoading(true);

    $.ajax({
        url: config.url,
        type: "GET",
        dataType: "json",
        success: function(data) {
            setLoading(false);
            logResponse(data);

            // Chuan hoa du lieu ve cau truc chung
            allProducts = normalizeData(data, currentSourceKey);
            filteredProducts = [...allProducts];

            updateCategoryOptions(allProducts);
            renderProducts(filteredProducts);
            showToast(`Tai thanh cong ${allProducts.length} san pham tu ${config.name}!`);
        },
        error: function(xhr, status, err) {
            setLoading(false);
            const errObj = { status: status, error: err, readyState: xhr.readyState };
            logResponse(errObj);
            showToast("Loi khi goi API: " + err, "error");
        }
    });
}

// Chuan hoa du lieu JSON tra ve tu cac nguon API khac nhau
function normalizeData(raw, sourceKey) {
    if (sourceKey === "dummyjson" && raw && raw.products) {
        return raw.products.map(p => ({
            id: p.id,
            title: p.title,
            price: p.price,
            description: p.description || "",
            category: p.category || "General",
            image: p.thumbnail || (p.images && p.images[0]) || "https://via.placeholder.com/300"
        }));
    } else if (sourceKey === "jsonplaceholder" && Array.isArray(raw)) {
        return raw.map(item => ({
            id: item.id,
            title: item.title,
            price: Math.floor(100000 + item.id * 15000),
            description: `Anh mau photo quang cao thu vien placeholder ma so #${item.id}`,
            category: "Photos",
            image: item.thumbnailUrl || item.url || "https://via.placeholder.com/300"
        }));
    } else if (Array.isArray(raw)) {
        return raw.map(p => ({
            id: p.id,
            title: p.title || p.name || "San pham",
            price: p.price || 0,
            description: p.description || "",
            category: p.category || "General",
            image: p.image || "https://via.placeholder.com/300"
        }));
    }
    return [];
}

// 3. Render danh sach san pham bang DOM
function renderProducts(list) {
    const grid = document.getElementById("products-grid");
    grid.innerHTML = "";

    document.getElementById("product-count").innerText = `Hien thi ${list.length} san pham`;

    if (list.length === 0) {
        grid.innerHTML = `<div style="grid-column: 1/-1; text-align:center; padding:40px; color:#64748b;">
            <h3>Khong tim thay san pham nao phu hop!</h3>
            <p>Hay thu tim kiem bang tu khoa khac hoac nhan "Tai lai".</p>
        </div>`;
        return;
    }

    list.forEach(p => {
        const card = document.createElement("div");
        card.className = "product-card";

        // Format gia tien
        const priceFormatted = typeof p.price === 'number' 
            ? (p.price > 1000 ? p.price.toLocaleString('vi-VN') + ' đ' : '$' + p.price.toFixed(2))
            : p.price;

        card.innerHTML = `
            <div class="card-img-wrap">
                <span class="badge-category">${escapeHtml(p.category)}</span>
                <img src="${escapeHtml(p.image)}" alt="${escapeHtml(p.title)}" onerror="this.src='https://via.placeholder.com/200?text=No+Image'">
            </div>
            <div class="card-body">
                <h4 class="card-title" title="${escapeHtml(p.title)}">${escapeHtml(p.title)}</h4>
                <div class="card-price">${priceFormatted}</div>
                <p class="card-desc">${escapeHtml(p.description)}</p>
                <div class="card-actions">
                    <button class="btn-card btn-edit" onclick="openEditModal(${p.id})">✏️ Sửa</button>
                    <button class="btn-card btn-delete" onclick="deleteProduct(${p.id})">🗑️ Xóa</button>
                </div>
            </div>
        `;
        grid.appendChild(card);
    });
}

// 4. Tim kiem san pham (Real-time search)
function handleSearch() {
    const keyword = document.getElementById("search-input").value.trim().toLowerCase();
    const selectedCategory = document.getElementById("category-filter").value;

    filteredProducts = allProducts.filter(p => {
        const matchKeyword = p.title.toLowerCase().includes(keyword) || 
                             p.description.toLowerCase().includes(keyword);
        const matchCat = (selectedCategory === "ALL" || p.category.toLowerCase() === selectedCategory.toLowerCase());
        return matchKeyword && matchCat;
    });

    renderProducts(filteredProducts);
}

// 5. Loc theo danh muc
function handleCategoryFilter() {
    handleSearch();
}

// Cap nhat dropdown danh muc
function updateCategoryOptions(list) {
    const select = document.getElementById("category-filter");
    const categories = new Set();
    list.forEach(p => { if (p.category) categories.add(p.category); });

    select.innerHTML = '<option value="ALL">-- Tất cả danh mục --</option>';
    categories.forEach(cat => {
        const opt = document.createElement("option");
        opt.value = cat;
        opt.innerText = cat;
        select.appendChild(opt);
    });
}

// 6. POST & PUT: Submit Form Them / Sua San Pham
function handleFormSubmit(e) {
    e.preventDefault();

    const idVal = document.getElementById("form-id").value;
    const isEdit = idVal !== "";

    const payload = {
        title: document.getElementById("form-title").value.trim(),
        price: parseFloat(document.getElementById("form-price").value) || 0,
        category: document.getElementById("form-category").value.trim(),
        image: document.getElementById("form-image").value.trim() || "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500&q=80",
        description: document.getElementById("form-desc").value.trim()
    };

    const config = API_CONFIG[currentSourceKey];
    setLoading(true);

    if (isEdit) {
        // PUT METHOD
        const putUrl = currentSourceKey === "local" 
            ? `${config.url}?id=${encodeURIComponent(idVal)}`
            : `${config.url}/${idVal}`;

        $.ajax({
            url: putUrl,
            type: "PUT",
            data: payload,
            dataType: "json",
            success: function(res) {
                setLoading(false);
                logResponse(res);
                closeModal();

                // Cap nhat vao danh sach hien tai
                const targetId = parseInt(idVal) || idVal;
                const index = allProducts.findIndex(p => p.id == targetId);
                if (index !== -1) {
                    allProducts[index] = { ...allProducts[index], ...payload };
                    handleSearch();
                }
                showToast(`Đã cập nhật sản phẩm #${idVal} thành công (PUT)!`);
            },
            error: function(err) {
                setLoading(false);
                logResponse(err);
                showToast("Lỗi khi cập nhật sản phẩm!", "error");
            }
        });
    } else {
        // POST METHOD
        $.ajax({
            url: config.url,
            type: "POST",
            data: payload,
            dataType: "json",
            success: function(res) {
                setLoading(false);
                logResponse(res);
                closeModal();

                // Fake them vao dau danh sach tren UI
                const newProduct = {
                    id: (res && res.id) ? res.id : (allProducts.length > 0 ? Math.max(...allProducts.map(p => Number(p.id) || 0)) + 1 : 1),
                    ...payload
                };
                allProducts.unshift(newProduct);
                handleSearch();
                showToast(`Đã thêm mới sản phẩm thành công (POST)!`);
            },
            error: function(err) {
                setLoading(false);
                logResponse(err);
                showToast("Lỗi khi thêm sản phẩm!", "error");
            }
        });
    }
}

// 7. DELETE: Xoa San Pham
function deleteProduct(id) {
    if (!confirm(`Bạn có chắc chắn muốn xóa sản phẩm #${id}?`)) return;

    const config = API_CONFIG[currentSourceKey];
    const deleteUrl = currentSourceKey === "local"
        ? `${config.url}?id=${encodeURIComponent(id)}`
        : `${config.url}/${id}`;

    setLoading(true);

    $.ajax({
        url: deleteUrl,
        type: "DELETE",
        dataType: "json",
        success: function(res) {
            setLoading(false);
            logResponse(res);

            // Xoa khoi danh sach UI
            allProducts = allProducts.filter(p => p.id != id);
            handleSearch();
            showToast(`Đã xóa sản phẩm #${id} thành công (DELETE)!`);
        },
        error: function(err) {
            setLoading(false);
            logResponse(err);
            showToast("Lỗi khi xóa sản phẩm!", "error");
        }
    });
}

// Modal Form Helpers
function openAddModal() {
    document.getElementById("modal-title").innerText = "➕ Thêm Sản Phẩm Quảng Cáo Mới";
    document.getElementById("btn-save").innerText = "Lưu Sản Phẩm (POST)";
    document.getElementById("form-id").value = "";
    document.getElementById("product-form").reset();
    document.getElementById("image-preview").src = "https://via.placeholder.com/150?text=Xem+Truoc+Anh";
    document.getElementById("product-modal").style.display = "flex";
}

function openEditModal(id) {
    const p = allProducts.find(item => item.id == id);
    if (!p) return;

    document.getElementById("modal-title").innerText = `✏️ Chỉnh Sửa Sản Phẩm #${id}`;
    document.getElementById("btn-save").innerText = "Cập Nhật (PUT)";
    document.getElementById("form-id").value = p.id;
    document.getElementById("form-title").value = p.title || "";
    document.getElementById("form-price").value = p.price || "";
    document.getElementById("form-category").value = p.category || "";
    document.getElementById("form-image").value = p.image || "";
    document.getElementById("form-desc").value = p.description || "";
    document.getElementById("image-preview").src = p.image || "https://via.placeholder.com/150";

    document.getElementById("product-modal").style.display = "flex";
}

function closeModal() {
    document.getElementById("product-modal").style.display = "none";
}

function previewFormImage() {
    const url = document.getElementById("form-image").value.trim();
    if (url) {
        document.getElementById("image-preview").src = url;
    }
}

// Helper: Hien thi log JSON
function logResponse(data) {
    const logBox = document.getElementById("json-response");
    try {
        logBox.innerText = JSON.stringify(data, null, 2);
    } catch (e) {
        logBox.innerText = String(data);
    }
}

function clearLog() {
    document.getElementById("json-response").innerText = "// Log da duoc lam sach...";
}

// Helper: Toast Thong bao
function showToast(msg, type = "info") {
    const toast = document.getElementById("toast");
    toast.innerText = msg;
    toast.style.borderColor = type === "error" ? "#ef4444" : "#3b82f6";
    toast.style.display = "block";
    setTimeout(() => { toast.style.display = "none"; }, 3500);
}

function setLoading(isLoading) {
    document.getElementById("loading-spinner").style.display = isLoading ? "inline-block" : "none";
}

function escapeHtml(str) {
    if (str === null || str === undefined) return "";
    return String(str)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}
