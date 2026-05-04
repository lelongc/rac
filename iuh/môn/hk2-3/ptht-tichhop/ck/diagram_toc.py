import sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

path = os.path.join('d:', os.sep, 'folder', 'rac', 'iuh', 'môn', 'hk2-3', 'ptht-tichhop', 'ck', 'du.md')
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 1. Add Diagrams
new_lines = []
skip = False
for i, line in enumerate(lines):
    if "### a. Trình bày ngắn gọn các giai đoạn chính trong quá trình truyền thông TCP Socket" in line:
        new_lines.append(line)
        new_lines.append("\n**Sơ đồ truyền thông TCP:**\n")
        new_lines.append("```mermaid\n")
        new_lines.append("sequenceDiagram\n")
        new_lines.append("    participant Client\n")
        new_lines.append("    participant Server\n")
        new_lines.append("    Note over Server: 1. Tạo ServerSocket()\n")
        new_lines.append("    Note over Server: 2. Lắng nghe accept()\n")
        new_lines.append("    Note over Client: 1. Tạo Socket()\n")
        new_lines.append("    Client->>Server: 2. Yêu cầu kết nối (3-way handshake)\n")
        new_lines.append("    Server-->>Client: Chấp nhận kết nối\n")
        new_lines.append("    Note over Client,Server: --- Thiết lập kết nối thành công ---\n")
        new_lines.append("    Client->>Server: 3. Gửi dữ liệu (OutputStream)\n")
        new_lines.append("    Server-->>Client: 4. Nhận & Phản hồi (InputStream/OutputStream)\n")
        new_lines.append("    Client->>Server: 5. Đóng kết nối close()\n")
        new_lines.append("    Server->>Client: Đóng socket\n")
        new_lines.append("```\n\n")
        continue

    if "### Luồng hoạt động của RMI" in line:
        new_lines.append(line)
        new_lines.append("\n**Sơ đồ Kiến trúc RMI:**\n")
        new_lines.append("```mermaid\n")
        new_lines.append("flowchart LR\n")
        new_lines.append("    subgraph Client_Machine [Máy Client]\n")
        new_lines.append("        C[Client App] --> STUB[Stub / Proxy]\n")
        new_lines.append("    end\n")
        new_lines.append("    subgraph Network [Mạng TCP/IP]\n")
        new_lines.append("        STUB -- \"Marshal (Đóng gói)\\nRequest\" --> SKEL\n")
        new_lines.append("        SKEL -- \"Unmarshal (Giải gói)\\nResponse\" --> STUB\n")
        new_lines.append("    end\n")
        new_lines.append("    subgraph Server_Machine [Máy Server]\n")
        new_lines.append("        SKEL[Skeleton / Dispatcher] --> S[Remote Object]\n")
        new_lines.append("    end\n")
        new_lines.append("    classDef client fill:#d4edda,stroke:#28a745,stroke-width:2px;\n")
        new_lines.append("    classDef server fill:#cce5ff,stroke:#007bff,stroke-width:2px;\n")
        new_lines.append("    classDef network fill:#f8f9fa,stroke:#6c757d,stroke-width:2px,stroke-dasharray: 5 5;\n")
        new_lines.append("    class Client_Machine client;\n")
        new_lines.append("    class Server_Machine server;\n")
        new_lines.append("    class Network network;\n")
        new_lines.append("```\n\n")
        continue

    if "### 2. Các thành phần chính trong kiến trúc JDBC" in line:
        new_lines.append(line)
        new_lines.append("\n**Sơ đồ Kiến trúc JDBC:**\n")
        new_lines.append("```mermaid\n")
        new_lines.append("flowchart TD\n")
        new_lines.append("    A[Java Application] -->|Gọi JDBC API| B(JDBC API)\n")
        new_lines.append("    B -->|Quản lý| C{DriverManager}\n")
        new_lines.append("    C -->|Driver 1| D[MySQL JDBC Driver]\n")
        new_lines.append("    C -->|Driver 2| E[SQL Server Driver]\n")
        new_lines.append("    C -->|Driver 3| F[SQLite Driver]\n")
        new_lines.append("    D --> DB1[(MySQL DB)]\n")
        new_lines.append("    E --> DB2[(SQL Server DB)]\n")
        new_lines.append("    F --> DB3[(SQLite DB)]\n")
        new_lines.append("```\n\n")
        continue

    new_lines.append(line)

# 2. Generate TOC
toc = ["## MỤC LỤC CHI TIẾT\n\n"]
for line in new_lines:
    if line.startswith("# ") and not line.startswith("# ĐỀ CƯƠNG"):
        title = line.strip().replace("# ", "")
        link = title.lower().replace(" ", "-").replace("/", "").replace("(", "").replace(")", "").replace(":", "")
        toc.append(f"- **[{title}](#{link})**\n")
    elif line.startswith("## "):
        title = line.strip().replace("## ", "")
        if title != "MỤC LỤC CHI TIẾT":
            link = title.lower().replace(" ", "-").replace("/", "").replace("(", "").replace(")", "").replace(":", "")
            toc.append(f"  - [{title}](#{link})\n")
    elif line.startswith("### "):
        title = line.strip().replace("### ", "")
        link = title.lower().replace(" ", "-").replace("/", "").replace("(", "").replace(")", "").replace(":", "")
        # Only include important level 3 headings
        if "Dạng" in title or "Bài" in title or "Code" in title or "Kiến trúc" in title or "Luồng" in title:
            toc.append(f"    - [{title}](#{link})\n")

toc.append("\n---\n\n")

# 3. Replace old TOC with new TOC
start_idx = -1
end_idx = -1
for i, line in enumerate(new_lines):
    if line.startswith("## MỤC LỤC"):
        start_idx = i
    if start_idx != -1 and line.startswith("---"):
        end_idx = i
        break

if start_idx != -1 and end_idx != -1:
    final_lines = new_lines[:start_idx] + toc + new_lines[end_idx+1:]
else:
    final_lines = new_lines

with open(path, 'w', encoding='utf-8') as f:
    f.writelines(final_lines)

print("Diagrams added and TOC generated!")
