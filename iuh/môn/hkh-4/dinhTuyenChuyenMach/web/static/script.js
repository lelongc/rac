const SYSTEM_PROMPT = `
Bạn là một Chuyên gia Mạng (Network Engineer) và Trợ lý AI xuất sắc.
Nhiệm vụ của bạn là đọc đề bài và tạo ra file cấu hình JSON đáp ứng cấu trúc của AutoEVE.
KHÔNG in ra markdown hay giải thích. CHỈ output JSON.

Cấu trúc JSON:
{
  "lab_name": "Ten_Lab_Khong_Dau",
  "nodes": [
    {
      "name": "TenRouter",
      "type": "router" | "switch" | "vpcs",
      "left": 200, "top": 200,
      "interfaces": [
        {"name": "e0/0", "network": "Net_1"},
        {"name": "s1/0", "remote_node": "TenRouter2", "remote_if": "s1/1"}
      ],
      "config": [
        "enable", "configure terminal", ...
      ]
    }
  ]
}

Luật:
1. "type" là "router", "switch", hoặc "vpcs".
2. Tên cổng: "e0/0", "s1/0"...
3. PC cổng luôn là "eth0".
4. Ethernet phải có "network".
5. Serial phải có "remote_node" và "remote_if".
6. Config Router phải bọc bằng "enable", "configure terminal", và "end".
7. Tự động chia IP và định tuyến thông minh.
`;

document.addEventListener('DOMContentLoaded', () => {
    const apiKeyInput = document.getElementById('apiKey');
    const promptInput = document.getElementById('prompt');
    const generateBtn = document.getElementById('generateBtn');
    const copyBtn = document.getElementById('copyBtn');
    const outputCode = document.getElementById('outputCode');
    const spinner = document.getElementById('loadingSpinner');
    const btnText = document.querySelector('.btn-text');

    const savedKey = localStorage.getItem('gemini_api_key');
    if (savedKey) apiKeyInput.value = savedKey;

    let currentReport = "";

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
        outputCode.textContent = '[1/2] AI đang đọc đề và thiết kế mô hình mạng...';
        copyBtn.disabled = true;

        try {
            // 1. Goi AI
            // Gọi API Gemini 3.1 Flash Lite (Siêu nhanh, rẻ và phù hợp tác vụ Agentic)
            const modelName = 'gemini-3.1-flash-lite'; 
            
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
                } catch(e) {
                    errMsg = response.statusText;
                }
                throw new Error('Gemini API báo lỗi: ' + errMsg);
            }
            const data = await response.json();
            let rawText = data.candidates[0].content.parts[0].text;
            rawText = rawText.replace(/```json/gi, '').replace(/```/g, '').trim();
            const jsonObj = JSON.parse(rawText);

            // 2. Goi Backend
            outputCode.textContent = "[2/2] Chuyển giao cho EVE-NG Server...\n\nĐang thực thi các bước:\n1. Upload file cấu hình\n2. Dựng sơ đồ mạng XML\n3. Tự động gọi API bật thiết bị (Power On)\n4. Chờ thiết bị khởi động (45s)...\n5. Đẩy cấu hình siêu tốc\n6. Rút trích báo cáo nghiệm thu\n\nQuá trình này mất khoảng 1.5 phút. Đừng tắt trình duyệt!";
            
            const deployRes = await fetch('/api/deploy', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(jsonObj)
            });
            
            const deployData = await deployRes.json();
            if (deployData.success) {
                currentReport = deployData.report;
                outputCode.textContent = "✅ THÀNH CÔNG RỰC RỠ!\n\n" + currentReport;
                copyBtn.disabled = false;
            } else {
                throw new Error("Lỗi Server EVE-NG: " + deployData.error);
            }
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
});
