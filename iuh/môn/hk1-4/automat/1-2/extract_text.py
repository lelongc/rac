import os
import sys

def extract_ppt(file_path):
    import win32com.client
    text = ""
    try:
        app = win32com.client.Dispatch("PowerPoint.Application")
        presentation = app.Presentations.Open(file_path, WithWindow=False)
        for slide in presentation.Slides:
            for shape in slide.Shapes:
                if shape.HasTextFrame:
                    if shape.TextFrame.HasText:
                        text += shape.TextFrame.TextRange.Text + "\n"
        presentation.Close()
        app.Quit()
    except Exception as e:
        text = f"Error reading {file_path}: {e}"
    return text

def extract_docx(file_path):
    import docx
    try:
        doc = docx.Document(file_path)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text
    except Exception as e:
        return f"Error reading {file_path}: {e}"

def extract_pdf(file_path):
    import PyPDF2
    text = ""
    try:
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() + "\n"
    except Exception as e:
        text = f"Error reading {file_path}: {e}"
    return text

def main():
    files = {
        "ppt1": r"d:\folder\rac\iuh\môn\hk1-4\automat\1-2\Tuan1_chuong1_KhaiNiemCoBanVeNgonNgu.ppt",
        "ppt2": r"d:\folder\rac\iuh\môn\hk1-4\automat\1-2\Tuan2_chuong1(tt)_VanPham.ppt",
        "pdf": r"d:\folder\rac\iuh\môn\hk1-4\automat\1-2\chương 1SV.pdf",
        "docx": r"d:\folder\rac\iuh\môn\hk1-4\automat\1-2\BÀI TAP chương 1.docx"
    }

    results = {}
    for key, path in files.items():
        if path.endswith(".ppt"):
            text = extract_ppt(path)
        elif path.endswith(".pdf"):
            text = extract_pdf(path)
        elif path.endswith(".docx"):
            text = extract_docx(path)
        
        with open(f"{key}_text.txt", "w", encoding="utf-8") as f:
            f.write(text)

if __name__ == "__main__":
    main()
