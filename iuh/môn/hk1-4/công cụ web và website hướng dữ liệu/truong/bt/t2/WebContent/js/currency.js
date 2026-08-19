function convertCurrency() {
    let amount = parseFloat(document.getElementById("amount").value);
    let from = document.getElementById("from").value;
    let to = document.getElementById("to").value;

    if (isNaN(amount) || amount <= 0) {
        document.getElementById("result").innerText = "Kết quả: Vui lòng nhập số tiền hợp lệ!";
        return;
    }

    let apiUrl = `/api/convert?amount=${amount}&from=${from}&to=${to}`;

    // Gọi RESTful API bằng jQuery $.ajax
    if (typeof $ !== 'undefined') {
        $.ajax({
            url: apiUrl,
            type: "GET",
            dataType: "json",
            success: function(data) {
                if (data.status === "success") {
                    let formattedResult = Number(data.result).toLocaleString("vi-VN");
                    document.getElementById("result").innerText = 
                        `Kết quả: ${data.amount} ${data.from} = ${formattedResult} ${data.to}`;
                } else {
                    document.getElementById("result").innerText = "Lỗi: " + data.message;
                }
            },
            error: function() {
                let rates = { "USD": 1, "VND": 25450, "EUR": 0.92, "JPY": 155.2, "GBP": 0.79 };
                let localResult = (amount / rates[from]) * rates[to];
                document.getElementById("result").innerText = 
                    `Kết quả (Local): ${amount} ${from} = ${localResult.toLocaleString("vi-VN")} ${to}`;
            }
        });
    } else {
        fetch(apiUrl)
            .then(res => res.json())
            .then(data => {
                let formattedResult = Number(data.result).toLocaleString("vi-VN");
                document.getElementById("result").innerText = 
                    `Kết quả: ${data.amount} ${data.from} = ${formattedResult} ${data.to}`;
            });
    }
}
