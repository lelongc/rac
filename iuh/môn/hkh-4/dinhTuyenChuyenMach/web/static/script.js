const SYSTEM_PROMPT = `
Bạn là một Chuyên gia Mạng (Network Engineer) và Trợ lý AI xuất sắc.
Nhiệm vụ của bạn là đọc đề bài và tạo ra file cấu hình JSON đáp ứng cấu trúc của AutoEVE, kèm theo Bảng IP.
KHÔNG in ra markdown hay giải thích ra ngoài. CHỈ output JSON thuần túy.

Cấu trúc JSON bắt buộc:
{
  "lab_name": "Ten_Lab_Khong_Dau",
  "nodes": [
    {
      "name": "TenRouter",
      "type": "router" | "switch" | "vpcs",
      "left": 200, "top": 200,
      "interfaces": [
        {"name": "e0/0", "network": "Net_LAN_HQ"},
        {"name": "s1/0", "remote_node": "TenRouter2", "remote_if": "s1/1"}
      ],
      "config": [
        "enable", "configure terminal", ...
      ]
    }
  ],
  "ip_table": [
    {"device": "TenRouter", "interface": "e0/0", "ip": "192.168.10.1", "subnet": "255.255.255.0"}
  ]
}

Luật:
1. "type" là "router", "switch", hoặc "vpcs".
2. Tên cổng: "e0/0", "s1/0"... PC cổng luôn là "eth0".
3. Ethernet phải có "network". Hai cổng nối với nhau thì phải có CÙNG tên "network". Tuyệt đối KHÔNG dùng chung 1 tên (như "LAN") cho tất cả các PC.
4. Serial phải có "remote_node" và "remote_if".
5. Config Router phải bọc bằng "enable", "configure terminal", và "end".
6. Tự động chia IP và định tuyến thông minh. Đảm bảo 'ip_table' phải đầy đủ.
7. Tính toán thuộc tính "left" và "top" hợp lý để vẽ sơ đồ EVE-NG đẹp mắt. Ví dụ:
- Lớp Core/Router WAN xếp ở trên cùng (top: 200). Các Router xếp ngang nhau (left: 200, 500, 800).
- Lớp Switch xếp ở giữa (top: 400), nằm ngay dưới Router quản lý nó (left tương ứng).
- Lớp PC xếp ở dưới cùng (top: 600), nằm ngay dưới Switch.
`;

const SYSTEM_PROMPT_REPORT = `
Bạn là một Chuyên gia Mạng Máy tính xuất sắc.
Bạn sẽ nhận được 2 nguồn dữ liệu:
1. Đề bài & Cấu trúc mạng đã thiết kế (JSON chứa các lệnh cấu hình).
2. OUTPUT thực tế thu được từ EVE-NG sau khi chạy cấu hình.

Nhiệm vụ của bạn: VIẾT MỘT BẢN BÁO CÁO ĐỒ ÁN HOÀN CHỈNH bằng tiếng Việt, chia làm 3 PHẦN rõ rệt đúng như sau:

PHẦN 1: CHẠY LỆNH CẤU HÌNH VÀ GIẢI THÍCH LỆNH
- Lần lượt đi qua TỪNG thiết bị.
- In ra các lệnh cấu hình (CLI) đã gán cho thiết bị đó (lấy từ dữ liệu JSON).
- NGAY BÊN DƯỚI các lệnh đó, HÃY GIẢI THÍCH CHI TIẾT: Lệnh đặt IP này để làm gì? Lệnh định tuyến (ip route) này trỏ đi đâu và tại sao phải làm thế?

PHẦN 2: CÁC LỆNH KIỂM TRA (VERIFY) VÀ GIẢI THÍCH OUTPUT
- Trích dẫn các Output thực tế (như show ip route, show ip int brief, ping...) từ nguồn dữ liệu OUTPUT.
- NGAY BÊN DƯỚI Output, HÃY GIẢI THÍCH ý nghĩa của nó: (Ví dụ: Thấy chữ C nghĩa là gì, S* nghĩa là gì, ping thông 5 dấu ! chứng minh điều gì).

PHẦN 3: BÁO CÁO HOÀN THÀNH
- Viết một đoạn tổng kết khẳng định hệ thống đã liên thông toàn bộ, đáp ứng đúng yêu cầu của đề bài.

Tuyệt đối KHÔNG trả về JSON. Trả về văn bản định dạng Markdown rõ ràng, rành mạch.
`;

const SYSTEM_PROMPT_ROUTING_ANALYSIS = `
Bạn là một Chuyên gia Mạng Máy tính xuất sắc.
Bạn sẽ nhận được 2 nguồn dữ liệu:
1. Đề bài & Cấu trúc mạng đã thiết kế (JSON).
2. OUTPUT thực tế thu được từ EVE-NG.

Nhiệm vụ của bạn: VIẾT MỘT BẢN PHÂN TÍCH ĐỊNH TUYẾN CHUYÊN SÂU bằng tiếng Việt, tập trung trả lời 2 câu hỏi sau:

1) BẢNG ĐỊNH TUYẾN (ROUTING TABLE) VÀ GIẢI THÍCH CÁC THÀNH PHẦN
- Trích xuất bảng định tuyến (show ip route) của các Router quan trọng (đặc biệt là Dynamic Routing).
- Giải thích chi tiết các thành phần trong bảng định tuyến đó (Ví dụ: Mã O, S, C, L nghĩa là gì? Thông số [110/20] là gì? via IP nghĩa là gì?).
- Chứng minh rằng giao thức định tuyến động (Dynamic Routing) đã hội tụ thành công.

2) ĐƯỜNG ĐI CỦA GÓI TIN (PACKET PATH)
- Mô tả chi tiết đường đi của gói tin khi 2 PC ở 2 mạng khác nhau ping nhau (Theo yêu cầu đề bài hoặc chọn ngẫu nhiên 2 PC khác mạng).
- Phân tích gói tin đi qua các cổng nào, địa chỉ IP Source/Destination thay đổi hay giữ nguyên, MAC address thay đổi ra sao qua mỗi Hop.

Tuyệt đối KHÔNG trả về JSON. Trả về văn bản định dạng Markdown rõ ràng, chuyên nghiệp.
`;

const SYSTEM_PROMPT_CONFIG_EXPLANATION = `
Bạn là một Chuyên gia Mạng Máy tính xuất sắc.
Bạn sẽ nhận được Đề bài & Cấu trúc mạng đã thiết kế (JSON).

Nhiệm vụ của bạn: VIẾT MỘT BẢN BÁO CÁO GIẢI THÍCH LỆNH CẤU HÌNH CHI TIẾT.
- Lần lượt đi qua TỪNG thiết bị có trong file JSON.
- Liệt kê toàn bộ các lệnh cấu hình (config) của thiết bị đó.
- Ngay bên dưới mỗi khối lệnh, HÃY GIẢI THÍCH CHI TIẾT: Lệnh này để làm gì? Tại sao lại cấu hình IP/subnet này? Lệnh định tuyến này có ý nghĩa gì?

Tuyệt đối KHÔNG trả về JSON. Báo cáo phải được định dạng Markdown rõ ràng, chuyên nghiệp. Không được bỏ sót bất kỳ thiết bị nào.
`;

document.addEventListener('DOMContentLoaded', () => {
    const apiKeyInput = document.getElementById('apiKey');
    const promptInput = document.getElementById('prompt');
    const generateBtn = document.getElementById('generateBtn');
    const copyBtn = document.getElementById('copyBtn');
    const explainConfigBtn = document.getElementById('explainConfigBtn');
    const analyzeRouteBtn = document.getElementById('analyzeRouteBtn');
    const downloadTxtBtn = document.getElementById('downloadTxtBtn');
    const downloadCsvBtn = document.getElementById('downloadCsvBtn');
    const outputCode = document.getElementById('outputCode');
    const spinner = document.getElementById('loadingSpinner');
    const btnText = document.querySelector('.btn-text');

    const savedKey = localStorage.getItem('gemini_api_key');
    if (savedKey) apiKeyInput.value = savedKey;

    let currentReport = "";
    let finalAiReport = "";
    let currentIpTable = [];
    let currentJsonObj = null;

    generateBtn.addEventListener('click', async () => {
        const apiKey = apiKeyInput.value.trim();
        const promptText = promptInput.value.trim();

        if (!apiKey || !promptText) {
            alert('Vui lòng nhập API Key và Đề bài.');
            return;
        }

        localStorage.setItem('gemini_api_key', apiKey);
        generateBtn.disabled = true;
        btnText.textContent = 'Đang tiến hành...';
        spinner.classList.remove('hidden');
        outputCode.textContent = '[1/3] AI đang đọc đề và thiết kế mô hình mạng...';
        
        copyBtn.disabled = true;
        explainConfigBtn.classList.add('hidden');
        analyzeRouteBtn.classList.add('hidden');
        downloadTxtBtn.classList.add('hidden');
        downloadCsvBtn.classList.add('hidden');

        try {
            const modelName = 'gemini-3.1-flash-lite'; 
            
            // PHASE 1: GENERATE CONFIG
            const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${modelName}:generateContent?key=${apiKey}`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    system_instruction: { parts: [{ text: SYSTEM_PROMPT }] },
                    contents: [{ parts: [{ text: promptText }] }],
                    generationConfig: { temperature: 0.1 }
                })
            });

            if (!response.ok) {
                let errMsg = 'Lỗi không xác định';
                try {
                    const errData = await response.json();
                    errMsg = errData.error?.message || response.statusText;
                } catch(e) { errMsg = response.statusText; }
                throw new Error('Gemini API (P1): ' + errMsg);
            }
            const data = await response.json();
            let rawText = data.candidates[0].content.parts[0].text;
            rawText = rawText.replace(/```json/gi, '').replace(/```/g, '').trim();
            const jsonObj = JSON.parse(rawText);
            currentJsonObj = jsonObj;

            currentIpTable = jsonObj.ip_table || [];

            // PHASE 2: DEPLOY TO EVE-NG
            outputCode.textContent = "[2/3] Chuyển giao cho EVE-NG Server...\n\nĐang thực thi các bước:\n1. Upload cấu hình\n2. Dựng sơ đồ XML\n3. Start thiết bị\n4. Chờ thiết bị khởi động (45s)...\n5. Đẩy cấu hình\n6. Rút trích báo cáo";
            
            const deployRes = await fetch('/api/deploy', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(jsonObj)
            });
            
            const deployData = await deployRes.json();
            if (!deployData.success) {
                throw new Error("Lỗi Server EVE-NG: " + deployData.error);
            }
            currentReport = deployData.report;

            // PHASE 3: AI POST-EXECUTION ANALYSIS
            outputCode.textContent = "[3/3] AI đang đọc Output thực tế và viết Báo cáo Chuyên sâu...\n\nVui lòng chờ thêm khoảng 5-10 giây...";
            
            const postPrompt = `== YÊU CẦU ĐỀ BÀI VÀ THIẾT KẾ ==\n${JSON.stringify(jsonObj)}\n\n== OUTPUT THỰC TẾ TỪ EVE-NG ==\n${currentReport}`;
            
            const reportResponse = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/${modelName}:generateContent?key=${apiKey}`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    system_instruction: { parts: [{ text: SYSTEM_PROMPT_REPORT }] },
                    contents: [{ parts: [{ text: postPrompt }] }],
                    generationConfig: { temperature: 0.3 }
                })
            });

            if (!reportResponse.ok) {
                let errMsg = 'Lỗi không xác định';
                try {
                    const errData = await reportResponse.json();
                    errMsg = errData.error?.message || reportResponse.statusText;
                } catch(e) { errMsg = reportResponse.statusText; }
                throw new Error('Gemini API (P3): ' + errMsg);
            }
            const reportData = await reportResponse.json();
            finalAiReport = reportData.candidates[0].content.parts[0].text;

            // FINAL: SHOW SUCCESS
            outputCode.textContent = "✅ THÀNH CÔNG RỰC RỠ!\n\n" + currentReport;
            copyBtn.disabled = false;
            explainConfigBtn.classList.remove('hidden');
            analyzeRouteBtn.classList.remove('hidden');
            downloadTxtBtn.classList.remove('hidden');
            if (currentIpTable.length > 0) downloadCsvBtn.classList.remove('hidden');

        } catch (error) {
            outputCode.textContent = `Lỗi hệ thống: ${error.message}`;
        } finally {
            generateBtn.disabled = false;
            btnText.textContent = '🚀 CHẠY TỰ ĐỘNG TOÀN DIỆN';
            spinner.classList.add('hidden');
        }
    });

    copyBtn.addEventListener('click', () => {
        navigator.clipboard.writeText(currentReport).then(() => {
            const origin = copyBtn.innerHTML;
            copyBtn.innerHTML = '✅ Đã Copy';
            setTimeout(() => { copyBtn.innerHTML = origin; }, 2000);
        });
    });

    // Xuất file TXT (Báo cáo Phân tích AI)
    downloadTxtBtn.addEventListener('click', () => {
        const blob = new Blob([finalAiReport], { type: 'text/plain;charset=utf-8;' });
        const link = document.createElement("a");
        const url = URL.createObjectURL(blob);
        link.setAttribute("href", url);
        link.setAttribute("download", "Bao_Cao_Chuyen_Sau.txt");
        link.style.visibility = 'hidden';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    });

    // Xuất file CSV (Bảng IP mở bằng Excel)
    downloadCsvBtn.addEventListener('click', () => {
        let csvContent = "\uFEFFThiết bị,Cổng giao tiếp,Địa chỉ IP,Subnet Mask\n";
        currentIpTable.forEach(row => {
            csvContent += `"${row.device || ''}","${row.interface || ''}","${row.ip || ''}","${row.subnet || ''}"\n`;
        });
        const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
        const link = document.createElement("a");
        const url = URL.createObjectURL(blob);
        link.setAttribute("href", url);
        link.setAttribute("download", "Bang_Quy_Hoach_IP.csv");
        link.style.visibility = 'hidden';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    });

    // Phân tích Định tuyến & Gói tin
    analyzeRouteBtn.addEventListener('click', async () => {
        const apiKey = apiKeyInput.value.trim();
        if (!apiKey || !currentReport || !currentJsonObj) return;

        const originalText = analyzeRouteBtn.innerHTML;
        analyzeRouteBtn.innerHTML = '⏳ Đang phân tích...';
        analyzeRouteBtn.disabled = true;

        try {
            const postPrompt = `== YÊU CẦU ĐỀ BÀI VÀ THIẾT KẾ ==\n${JSON.stringify(currentJsonObj)}\n\n== OUTPUT THỰC TẾ TỪ EVE-NG ==\n${currentReport}`;
            const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite:generateContent?key=${apiKey}`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    system_instruction: { parts: [{ text: SYSTEM_PROMPT_ROUTING_ANALYSIS }] },
                    contents: [{ parts: [{ text: postPrompt }] }],
                    generationConfig: { temperature: 0.3 }
                })
            });

            if (!response.ok) throw new Error('Lỗi API Gemini');
            const data = await response.json();
            const analysisReport = data.candidates[0].content.parts[0].text;

            const blob = new Blob([analysisReport], { type: 'text/plain;charset=utf-8;' });
            const link = document.createElement("a");
            const url = URL.createObjectURL(blob);
            link.setAttribute("href", url);
            link.setAttribute("download", "Phan_Tich_Dinh_Tuyen.txt");
            link.style.visibility = 'hidden';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        } catch (error) {
            alert('Lỗi khi phân tích định tuyến: ' + error.message);
        } finally {
            analyzeRouteBtn.innerHTML = originalText;
            analyzeRouteBtn.disabled = false;
        }
    });

    // Giải thích Lệnh Config
    explainConfigBtn.addEventListener('click', async () => {
        const apiKey = apiKeyInput.value.trim();
        if (!apiKey || !currentJsonObj) return;

        const originalText = explainConfigBtn.innerHTML;
        explainConfigBtn.innerHTML = '⏳ Đang phân tích...';
        explainConfigBtn.disabled = true;

        try {
            const promptContent = `== CẤU TRÚC MẠNG VÀ LỆNH CẤU HÌNH (JSON) ==\n${JSON.stringify(currentJsonObj)}`;
            const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite:generateContent?key=${apiKey}`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    system_instruction: { parts: [{ text: SYSTEM_PROMPT_CONFIG_EXPLANATION }] },
                    contents: [{ parts: [{ text: promptContent }] }],
                    generationConfig: { temperature: 0.2 }
                })
            });

            if (!response.ok) throw new Error('Lỗi API Gemini');
            const data = await response.json();
            const explainReport = data.candidates[0].content.parts[0].text;

            const blob = new Blob([explainReport], { type: 'text/plain;charset=utf-8;' });
            const link = document.createElement("a");
            const url = URL.createObjectURL(blob);
            link.setAttribute("href", url);
            link.setAttribute("download", "Giai_Thich_Lenh_Config.txt");
            link.style.visibility = 'hidden';
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
        } catch (error) {
            alert('Lỗi khi giải thích cấu hình: ' + error.message);
        } finally {
            explainConfigBtn.innerHTML = originalText;
            explainConfigBtn.disabled = false;
        }
    });
});
