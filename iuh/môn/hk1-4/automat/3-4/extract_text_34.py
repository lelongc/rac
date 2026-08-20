import PyPDF2
import sys

def extract_pdf(file_path, output_path):
    text = ""
    try:
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for i, page in enumerate(reader.pages):
                text += f"\n--- PAGE {i+1} ---\n"
                t = page.extract_text()
                if t:
                    text += t
        with open(output_path, 'w', encoding='utf-8') as out:
            out.write(text)
        print(f"Extracted {len(reader.pages)} pages to {output_path}")
    except Exception as e:
        print(f"Error extracting {file_path}: {e}")

if __name__ == "__main__":
    extract_pdf(r"d:\folder\rac\iuh\môn\hk1-4\automat\3-4\MÁY HỮU HẠN KHÔNG ĐƠN ĐỊNH SV nfa.pdf", r"d:\folder\rac\iuh\môn\hk1-4\automat\3-4\nfa_theory_text.txt")
    extract_pdf(r"d:\folder\rac\iuh\môn\hk1-4\automat\3-4\Thiết kế NFA SV.pdf", r"d:\folder\rac\iuh\môn\hk1-4\automat\3-4\nfa_design_text.txt")
