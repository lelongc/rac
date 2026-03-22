package Socket_TCP_Thread;

import java.io.*;
import java.net.Socket;

public class WorkerThread extends Thread {
    private Socket socket;
    private int clientId;

    public WorkerThread(Socket socket, int clientId) {
        this.socket = socket;
        this.clientId = clientId;
    }

    @Override
    public void run() {
        try (BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
             PrintWriter out = new PrintWriter(socket.getOutputStream(), true)) {

            /*
             * -----------------------------------------------------------------
             * DONG IN DIA CHI IP CUA CLIENT (Co the comment/uncomment tuy y)
             * -----------------------------------------------------------------
             */
            System.out.println("   [INFO] Client IP: " + socket.getInetAddress().getHostAddress());
            System.out.println("   [INFO] Client Port: " + socket.getPort());
            
            // ==============================================================================
            // CẦN LƯU Ý PHẦN NÀY ĐỂ FIX ĐƯỜNG DẪN ĐỌC/GHI FILE ĐỂ FILE KHÔNG BỊ RƠT LUNG TUNG 
            // TRONG ECLIPSE PROJECT ROOT:
            // Sửa đường dẫn nếu cần, ví dụ: "src/Socket_TCP_Thread/" hoặc "4_Socket_TCP/"
            // ==============================================================================
            String DIR = "DeCuongGiuaKi/4_Socket_TCP/"; // Tuỳ chỉnh tuỳ cấu trúc Workspace Eclipse
            
            String inputLine;
            while ((inputLine = in.readLine()) != null) {
                System.out.println("Nhan tu Client #" + clientId + ": " + inputLine);
                
                String result = "";

                /*
                ========================================================================================
                [PHAN CHON LOGIC XU LY]
                De thi ra dang nao thi UNCOMMENT dang do ra va COMMENT cac dang con lai.
                ========================================================================================
                */

                // -------------------------------------------------------------------------------------
                // DANG 1: CHU THUONG THANH IN HOA / IN THUONG
                // -------------------------------------------------------------------------------------
                // result = inputLine.toUpperCase(); // In hoa
                // result = inputLine.toLowerCase(); // In thuong

                // -------------------------------------------------------------------------------------
                // DANG 2: DAO NGUOC CHUOI
                // -------------------------------------------------------------------------------------
                // StringBuilder sb = new StringBuilder(inputLine);
                // result = sb.reverse().toString();

                // -------------------------------------------------------------------------------------
                // DANG 3: DEM SO TU, DEM SO KY TU (Khoang trang khong tinh vao ky tu)
                // -------------------------------------------------------------------------------------
                // String trimmed = inputLine.trim();
                // int wordCount = trimmed.isEmpty() ? 0 : trimmed.split("\\s+").length;
                // int charCount = inputLine.replace(" ", "").length();
                // result = "So tu: " + wordCount + " | So ky tu: " + charCount;

                // -------------------------------------------------------------------------------------
                // DANG 4: LOAI BO KHOANG TRANG THUA (Chuan hoa chuoi)
                // -------------------------------------------------------------------------------------
                // result = inputLine.trim().replaceAll("\\s+", " ");

                // -------------------------------------------------------------------------------------
                // DANG 5: IN HOA CHU CAI DAU TIEN MOI TU (Title Case)
                // -------------------------------------------------------------------------------------
                /*
                String[] words = inputLine.trim().split("\\s+");
                StringBuilder titleCase = new StringBuilder();
                for (String w : words) {
                    if (w.length() > 0) {
                        titleCase.append(Character.toUpperCase(w.charAt(0)))
                                 .append(w.substring(1).toLowerCase()).append(" ");
                    }
                }
                result = titleCase.toString().trim();
                */

                // -------------------------------------------------------------------------------------
                // DANG 6: KIEM TRA CHUOI DOI XUNG (Palindrome)
                // -------------------------------------------------------------------------------------
                /*
                String cleanStr = inputLine.replaceAll("\\s+", "").toLowerCase();
                String reversedStr = new StringBuilder(cleanStr).reverse().toString();
                if (cleanStr.equals(reversedStr)) {
                    result = "La chuoi doi xung (Palindrome)";
                } else {
                    result = "Khong phai chuoi doi xung";
                }
                */

                // -------------------------------------------------------------------------------------
                // DANG 7: KIEM TRA MOT SO TU NHIEN (Chan/Le, Nguyen To) - Input vd: "5"
                // -------------------------------------------------------------------------------------
                /*
                try {
                    int n = Integer.parseInt(inputLine.trim());
                    String chanLe = (n % 2 == 0) ? "So Chan" : "So Le";
                    
                    boolean isPrime = n >= 2;
                    for (int i = 2; i <= Math.sqrt(n); i++) {
                        if (n % i == 0) { isPrime = false; break; }
                    }
                    String nguyenTo = isPrime ? "La so Nguyen To" : "Khong phai Nguyen To";
                    
                    result = chanLe + " | " + nguyenTo;
                } catch (NumberFormatException e) {
                    result = "Loi: Vui long nhap mot so nguyen hop le!";
                }
                */

                // -------------------------------------------------------------------------------------
                // DANG 8: TINH TONG CAC CHU SO CUA MOT SO (vd: "123" -> 6)
                // -------------------------------------------------------------------------------------
                /*
                try {
                    int n = Math.abs(Integer.parseInt(inputLine.trim()));
                    int sum = 0;
                    while (n > 0) {
                        sum += n % 10;
                        n /= 10;
                    }
                    result = "Tong cac chu so = " + sum;
                } catch (NumberFormatException e) {
                    result = "Loi: Vui long nhap mot so nguyen hop le!";
                }
                */

                // -------------------------------------------------------------------------------------
                // DANG 9: TONG, MAX/MIN CUA CHUOI NHIEU SO (vd: "1 5 3 4" -> Max=5, Sum=13)
                // -------------------------------------------------------------------------------------
                /*
                try {
                    String[] strNums = inputLine.trim().split("\\s+");
                    int sum = 0; // co the la double neu can
                    int max = Integer.MIN_VALUE;
                    int min = Integer.MAX_VALUE;
                    
                    for (String s : strNums) {
                        int val = Integer.parseInt(s);
                        sum += val;
                        if (val > max) max = val;
                        if (val < min) min = val;
                    }
                    result = "Tong = " + sum + " | Max = " + max + " | Min = " + min;
                } catch (NumberFormatException e) {
                    result = "Loi: Input phai la day so cac nhau boi khoang trang!";
                }
                */

                // -------------------------------------------------------------------------------------
                // DANG 10: NHAN DU LIEU TU CLIENT VA GHI VAO FILE (Ghi tiep / Append)
                // -------------------------------------------------------------------------------------
                /*
                try (FileWriter fw = new FileWriter(DIR + "Xuat.txt", true);
                     BufferedWriter bw = new BufferedWriter(fw)) {
                    bw.write("Client " + clientId + ": " + inputLine);
                    bw.newLine();
                    result = "Server da luu '" + inputLine + "' vao file " + DIR + "Xuat.txt";
                } catch (IOException e) {
                    result = "Loi ghi file: " + e.getMessage();
                }
                */

                // -------------------------------------------------------------------------------------
                // DANG 11: NHAN TEN FILE TU CLIENT, DOC NOI DUNG FILE THEM VAO OUTPUT VA TRA VE
                // Vd: Client gui chuoi "data.txt" (Server se tim o muc thu muc DIR / data.txt)
                // -------------------------------------------------------------------------------------
                /*
                File file = new File(DIR + inputLine.trim());
                if (file.exists() && file.isFile()) {
                    StringBuilder fileContent = new StringBuilder();
                    try (BufferedReader fileReader = new BufferedReader(new FileReader(file))) {
                        String line;
                        while ((line = fileReader.readLine()) != null) {
                            fileContent.append(line).append(" \\n "); 
                        }
                        result = "Noi dung file " + file.getName() + ": " + fileContent.toString();
                    } catch (IOException e) {
                        result = "Loi doc file: " + e.getMessage();
                    }
                } else {
                    result = "File '" + inputLine + "' khong ton tai tren Server!";
                }
                */

                // -------------------------------------------------------------------------------------
                // DANG 12: TINH GIAI THUA CUA MOT SO n (vd: "5" -> 120)
                // -------------------------------------------------------------------------------------
                /*
                try {
                    int n = Integer.parseInt(inputLine.trim());
                    if (n < 0) {
                        result = "Loi: Khong tinh giai thua so am.";
                    } else if (n > 20) {
                        result = "Loi: n qua lon, de tranh tran so (toi da 20).";
                    } else {
                        long fact = 1;
                        for (int i = 2; i <= n; i++) fact *= i;
                        result = "Giai thua cua " + n + " la = " + fact;
                    }
                } catch (NumberFormatException e) {
                    result = "Loi: Input phai la mot so nguyen hop le!";
                }
                */

                // -------------------------------------------------------------------------------------
                // DANG 13: TIM DIA CHI IP TU TEN MIEN (Domain -> IP Lookup su dung InetAddress)
                // Vd: Client gui "google.com" hoac "localhost"
                // -------------------------------------------------------------------------------------
                /*
                try {
                    java.net.InetAddress address = java.net.InetAddress.getByName(inputLine.trim());
                    result = "Ten mien: " + address.getHostName() + " | Dia chi IP: " + address.getHostAddress();
                } catch (java.net.UnknownHostException e) {
                    result = "Loi: Khong the phan giai ten mien '" + inputLine + "'";
                }
                */

                // -------------------------------------------------------------------------------------
                // DANG 17: BÀI 1 TUẦN 5 - ĐỌC MỘT KÝ TỰ SỐ TỪ 0-9 VÀ TRẢ VỀ CHỮ (vd: "1" -> "một")
                // -------------------------------------------------------------------------------------
                /*
                String trimInput = inputLine.trim();
                if (trimInput.length() == 1 && Character.isDigit(trimInput.charAt(0))) {
                    int num = Integer.parseInt(trimInput);
                    String[] words = {"khong", "mot", "hai", "ba", "bon", "nam", "sau", "bay", "tam", "chin"};
                    result = words[num];
                } else {
                    result = "Khong phai so nguyen tu 0 den 9";
                }
                */

                // -------------------------------------------------------------------------------------
                // DANG 18: BÀI 4 TUẦN 5 - MENU NGÀY GIỜ (1. Time, 2. Date, 3. Date & Time)
                // -------------------------------------------------------------------------------------
                /*
                try {
                    int choice = Integer.parseInt(inputLine.trim());
                    java.time.LocalDateTime now = java.time.LocalDateTime.now();
                    java.time.format.DateTimeFormatter timeFmt = java.time.format.DateTimeFormatter.ofPattern("HH:mm:ss");
                    java.time.format.DateTimeFormatter dateFmt = java.time.format.DateTimeFormatter.ofPattern("dd/MM/yyyy");
                    if (choice == 1) result = now.format(timeFmt);
                    else if (choice == 2) result = now.format(dateFmt);
                    else if (choice == 3) result = now.format(dateFmt) + " " + now.format(timeFmt);
                    else result = "Lua chon khong hop le!";
                } catch (NumberFormatException e) {
                    result = "Vui long nhap so (1-3)!";
                }
                */

                // -------------------------------------------------------------------------------------
                // DANG 19: BÀI 6 TUẦN 5 - TÍNH CHUỖI TỔNG THEO MENU (1. 1+3+..., 2. 1*2+..., 3. 1-2+...)
                // Input format tu Client: "<MenuID> <n>" vd: "1 5" hoac "2 4"
                // -------------------------------------------------------------------------------------
                /*
                try {
                    String[] parts = inputLine.trim().split("\\s+");
                    int menu = Integer.parseInt(parts[0]);
                    int n = Integer.parseInt(parts[1]);
                    long sum = 0;
                    if (menu == 1) {        // 1+3+5+...+(2n+1)
                        for (int i = 0; i <= n; i++) sum += (2*i + 1);
                        result = "Tong 1 = " + sum;
                    } else if (menu == 2) { // 1*2 + 2*3 +...+ n*(n+1)
                        for (int i = 1; i <= n; i++) sum += (i * (i+1));
                        result = "Tong 2 = " + sum;
                    } else if (menu == 3) { // 1-2+3-4+...+(2n+1)
                        int sign = 1;
                        for (int i = 1; i <= 2*n+1; i++) {
                            sum += sign * i;
                            sign = -sign;
                        }
                        result = "Tong 3 = " + sum;
                    } else {
                        result = "Menu khong hop le!";
                    }
                } catch (Exception e) {
                    result = "Sai cu phap. Vd: '1 5'";
                }
                */

                // -------------------------------------------------------------------------------------
                // DANG 20: BÀI 8 TUẦN 5 - NHAN PHEP TINH "Operant1 OP Operant2" (vd: "200 + 200")
                // -------------------------------------------------------------------------------------
                /*
                try {
                    String[] parts = inputLine.trim().split("\\s+");
                    double a = Double.parseDouble(parts[0]);
                    String op = parts[1];
                    double b = Double.parseDouble(parts[2]);
                    double ans = 0;
                    if (op.equals("+")) ans = a + b;
                    else if (op.equals("-")) ans = a - b;
                    else if (op.equals("*")) ans = a * b;
                    else if (op.equals("/")) ans = a / b;
                    result = "Ket qua: " + ans;
                } catch (Exception e) {
                    result = "Loi dinh dang. Input dung phai co khoang trang: '200 + 200'";
                }
                */

                // -------------------------------------------------------------------------------------
                // DANG 14: BÀI 9 - NHAN TEN FILE TU CLIENT, DOC FILE GUI TUNG DONG (Den khi ##END##)
                // (Truong hop nay: chay het khoi nay se bo qua cac thao tac print result khac)
                // -------------------------------------------------------------------------------------
                /*
                File file = new File(DIR + inputLine.trim());
                if (file.exists() && file.isFile()) {
                    try (BufferedReader fileReader = new BufferedReader(new FileReader(file))) {
                        String line;
                        while ((line = fileReader.readLine()) != null) {
                            out.println(line); 
                        }
                    } catch (IOException e) {
                        out.println("ERROR: Loi doc file: " + e.getMessage());
                    }
                } else {
                    out.println("ERROR: File khong ton tai!");
                }
                out.println("##END##"); // Ket thuc bang ##END## nhu bai 9
                continue; // Chuyen sang vong lap tiep theo cua in.readLine() ma khong xuong duoi
                */

                // -------------------------------------------------------------------------------------
                // DANG 15: BÀI 10 - NHAN NHIEU TIN NHAN VA GHI VAO FILE DEN KHI GAP "HET"
                // -------------------------------------------------------------------------------------
                /*
                File outFile = new File(DIR + "client" + clientId + ".txt");
                try (PrintWriter fileOut = new PrintWriter(new java.io.FileWriter(outFile))) {
                    
                    if (inputLine.toUpperCase().contains("HET")) {
                        out.println("Phat hien chu 'HET' ngay tn dau tien! Dong file.");
                    } else {
                        fileOut.println(inputLine);
                        out.println("Da ghi tn 1. Nhap tiep (Go 'HET' de dung):");
                        
                        while (true) {
                            String msg = in.readLine();
                            if (msg == null) break;
                            
                            if (msg.toUpperCase().contains("HET")) {
                                out.println("Da nhan thong diep ngung! Luu vao: " + outFile.getName());
                                break;
                            }
                            
                            fileOut.println(msg);
                            // TRẢ VỀ CHO CLIENT ĐỂ NÓ KHÔNG BỊ TREO CHỜ (Đồng bộ)
                            out.println("Da ghi vao file. Xin moi nhap tiep...");
                        }
                    }
                } catch (IOException e) {
                    out.println("Loi ghi file: " + e.getMessage());
                }
                continue; // Bo qua phan in kq duoi cung, vi da rep li trong block nay
                */

                // -------------------------------------------------------------------------------------
                // DANG 16: MAY TINH MINI (vd: "5 + 3" -> 8)
                // -------------------------------------------------------------------------------------
                try {
                    String cleanMathStr = inputLine.trim().replaceAll("\\s+", "");
                    String operator = "";
                    if (cleanMathStr.contains("+")) operator = "\\+";
                    else if (cleanMathStr.contains("-")) operator = "-";
                    else if (cleanMathStr.contains("*")) operator = "\\*";
                    else if (cleanMathStr.contains("/")) operator = "/";
                    
                    if (!operator.isEmpty()) {
                        String[] parts = cleanMathStr.split(operator);
                        if (parts.length == 2) {
                            double a = Double.parseDouble(parts[0]);
                            double b = Double.parseDouble(parts[1]);
                            double calc = 0;
                            switch (operator) {
                                case "\\+": calc = a + b; break;
                                case "-": calc = a - b; break;
                                case "\\*": calc = a * b; break;
                                case "/": calc = a / b; break;
                            }
                            result = "Ket qua phep tinh: " + calc;
                        } else { result = "Cu phap phep tinh chua chuan!"; }
                    } else {
                        // NEU KHONG CO MATCH VOI TOAN TU NAO
                        result = "Echo (Khong co logic): " + inputLine;
                    }
                } catch (Exception e) {
                    result = "Loi doc bieu thuc toan hoc!";
                }

                out.println(result); // Tra ve cho client
            }

            System.out.println("Client #" + clientId + " da ngat ket noi!");

        } catch (IOException e) {
            System.err.println("Loi o Client #" + clientId + ": " + e.getMessage());
        } finally {
            try { socket.close(); } catch (IOException e) {}
        }

        // =========================================================================================
        // KHOI MA THAY THE DÀNH RIÊNG CHO BÀI 7 - TRUYỀN FILE NHỊ PHÂN (Dùng DataInputStream)
        // =========================================================================================
        // NẾU ĐI THI GẶP BÀI TRUYỀN DUNG LƯỢNG FILE + MẢNG BYTE[]:
        // 1. Comment toàn bộ khối: try (BufferedReader in = ...) ở bên trên! (Khoảng từ dòng 17 -> 267)
        // 2. Uncomment khối "try (DataInputStream...)" ngay phía dưới đây để chạy!
        // =========================================================================================
        /*
        try (DataInputStream dataIn = new DataInputStream(socket.getInputStream());
             DataOutputStream dataOut = new DataOutputStream(socket.getOutputStream())) {
            
            String fileName = dataIn.readUTF();   
            String savePath = dataIn.readUTF();   
            long fileSize = dataIn.readLong();  
            
            File dir = new File(savePath);
            if (!dir.exists()) dir.mkdirs();
            File dest = new File(dir, fileName);
            
            try (FileOutputStream fos = new FileOutputStream(dest)) {
                byte[] buf = new byte[4096];
                long remaining = fileSize;
                while (remaining > 0) {
                    int toRead = (int) Math.min(buf.length, remaining);
                    int n = dataIn.read(buf, 0, toRead);
                    if (n < 0) break;
                    fos.write(buf, 0, n);
                    remaining -= n;
                }
            }
            System.out.println("Da luu file: " + dest.getAbsolutePath() + " (" + fileSize + " bytes)");
            dataOut.writeUTF("OK: Da luu " + dest.getAbsolutePath());
            dataOut.flush();

        } catch (IOException e) {
            System.err.println("Loi Binary Client #" + clientId + ": " + e.getMessage());
        } finally {
            try { socket.close(); } catch (IOException e) {}
        }
        */
    }
}
