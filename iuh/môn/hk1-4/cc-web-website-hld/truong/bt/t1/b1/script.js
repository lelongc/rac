const rates = {
    "USD": 1,
    "VND": 25450,
    "EUR": 0.92,
    "JPY": 155.2,
    "GBP": 0.79
};

function convert() {
    let amount = parseFloat(document.getElementById("amount").value);
    let fromCurrency = document.getElementById("from").value;
    let toCurrency = document.getElementById("to").value;

    if (isNaN(amount) || amount <= 0) {
        document.getElementById("result").innerText = "Kết quả: Vui lòng nhập số tiền hợp lệ!";
        return;
    }

    let result = (amount / rates[fromCurrency]) * rates[toCurrency];

    document.getElementById("result").innerText =
        `Kết quả: ${amount} ${fromCurrency} = ${result.toLocaleString()} ${toCurrency}`;
}
