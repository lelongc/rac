function loadProductsFromAPI() {
    let apiUrl = "/api/products";

    if (typeof $ !== 'undefined') {
        $.getJSON(apiUrl, function(products) {
            renderTableWithDOM(products);
        }).fail(function() {
            let fallbackProducts = [
                { id: "SP01", name: "Laptop Dell XPS 15", price: 35000000, quantity: 5, category: "Laptop" },
                { id: "SP02", name: "Điện thoại iPhone 15 Pro", price: 28000000, quantity: 10, category: "Điện thoại" },
                { id: "SP03", name: "Tai nghe Sony WH-1000XM5", price: 8500000, quantity: 12, category: "Phụ kiện" },
                { id: "SP04", name: "Bàn phím cơ Keychron K2", price: 2100000, quantity: 8, category: "Phụ kiện" },
                { id: "SP05", name: "Màn hình LG UltraGear 27 inch", price: 7900000, quantity: 4, category: "Màn hình" }
            ];
            renderTableWithDOM(fallbackProducts);
        });
    } else {
        fetch(apiUrl)
            .then(res => res.json())
            .then(products => renderTableWithDOM(products));
    }
}

function renderTableWithDOM(products) {
    let tbody = document.getElementById("product-table-body");
    tbody.innerHTML = "";

    products.forEach(product => {
        let row = `
            <tr>
                <td>${product.id}</td>
                <td>${product.name}</td>
                <td>${Number(product.price).toLocaleString("vi-VN")}</td>
                <td>${product.quantity}</td>
                <td>${product.category}</td>
            </tr>
        `;
        tbody.innerHTML += row;
    });
}

window.onload = loadProductsFromAPI;
