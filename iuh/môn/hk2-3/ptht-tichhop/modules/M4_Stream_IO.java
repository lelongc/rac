// ============================================================
// MODULE 4 – STREAM I/O (InputStream / BufferedReader / PrintWriter)
// Dùng khi đề: nhập liệu console, đọc/ghi file, xử lý ký tự
// Ghép với: M5/M6 (stream trong socket), M1 (nhập object)
// ============================================================
import java.io.*;

public class M4_Stream_IO {
    public static void main(String[] args) throws IOException {

        // ── CÁCH 1: InputStream thuần (byte thô) ─────────────
        // Dùng khi: đề yêu cầu đọc byte, xử lý ký tự số, 'q' thoát
        /*
        InputStream is = System.in;
        System.out.println("Nhap ky tu ('q' de thoat):");
        while (true) {
            int ch = is.read();            // trả về int (mã ASCII) hoặc -1
            if (ch == -1 || ch == 'q') break;
            if (ch >= 32) {                // bỏ qua ký tự điều khiển
                System.out.println("Doc duoc: " + (char) ch + "  (ASCII=" + ch + ")");
                // TODO: xử lý byte ch theo yêu cầu đề
            }
        }
        */

        // ── CÁCH 2: InputStreamReader + BufferedReader ───────
        // Dùng khi: nhập chuỗi, số nguyên, vòng lặp theo dòng
        // ĐÂY LÀ CÁCH DÙNG PHỔ BIẾN NHẤT TRONG THI
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter    pw = new PrintWriter(System.out, true);  // true = auto-flush

        // Nhập String
        pw.print("Nhap chuoi: "); pw.flush();
        String line = br.readLine();                   // đọc 1 dòng
        pw.println("Ban vua nhap: " + line);

        // Nhập int
        pw.print("Nhap so nguyen: "); pw.flush();
        int n = Integer.parseInt(br.readLine().trim()); // .trim() để bỏ khoảng trắng thừa
        pw.println("So + 1 = " + (n + 1));

        // Nhập double
        pw.print("Nhap so thuc: "); pw.flush();
        double d = Double.parseDouble(br.readLine().trim());
        pw.println("So * 2 = " + (d * 2));

        // Vòng lặp đọc đến "exit"
        pw.println("Nhap cac dong (exit de dung):");
        while (true) {
            String s = br.readLine();
            if (s == null || s.equalsIgnoreCase("exit")) break;
            // TODO: xử lý s theo yêu cầu đề
            pw.println(">> " + s.toUpperCase());  // ví dụ: in hoa
        }

        // ── CÁCH 3: Đọc ghi FILE ─────────────────────────────
        // Ghi file
        /*
        try (FileWriter fw = new FileWriter("output.txt")) {
            fw.write("Dong 1\n");
            fw.write("Dong 2\n");
        }
        */
        // Đọc file
        /*
        try (BufferedReader fbr = new BufferedReader(new FileReader("output.txt"))) {
            String row;
            while ((row = fbr.readLine()) != null) {
                System.out.println(row);
            }
        }
        */

        // ── CÁCH 4: OutputStream + PrintWriter ───────────────
        // Dùng khi đề dùng OutputStream tường minh
        /*
        OutputStream os = System.out;
        PrintWriter pw2 = new PrintWriter(os, true);
        pw2.println("Ket qua: " + n);
        pw2.flush();
        pw2.close();
        */
    }
}

/*
 CHUỖI KẾ THỪA CẦN NHỚ:
 InputStream (byte)
     └── InputStreamReader (byte → char, có encoding)
             └── BufferedReader (đọc cả dòng: readLine())

 OutputStream (byte)
     └── OutputStreamWriter (char → byte)
             └── PrintWriter (println/print/flush)    ← hay dùng trực tiếp
*/
