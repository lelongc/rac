// Bảng tỷ giá quy đổi cơ bản (gốc là USD)
const rates = {
    "USD": 1,
    "VND": 25450,
    "EUR": 0.92,
    "JPY": 155.2,
    "GBP": 0.79
};

function convert() {
    // Lấy giá trị từ ô nhập và 2 thẻ select
    let amount = parseFloat(document.getElementById("amount").value);
    let fromCurrency = document.getElementById("from").value;
    let toCurrency = document.getElementById("to").value;

    // Kiểm tra dữ liệu đầu vào
    if (isNaN(amount) || amount <= 0) {
        document.getElementById("result").innerText = "Kết quả: Vui lòng nhập số tiền hợp lệ!";
        return;
    }

    // Tính toán quy đổi: (Số tiền / tỷ giá gốc) * tỷ giá đích
    let result = (amount / rates[fromCurrency]) * rates[toCurrency];

    // Hiển thị kết quả ra màn hình
    document.getElementById("result").innerText = 
        `Kết quả: ${amount} ${fromCurrency} = ${result.toLocaleString()} ${toCurrency}`;
}
