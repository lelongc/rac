import zipfile
import re
import sys

def extract_text_from_pptx(pptx_path):
    text_runs = []
    try:
        with zipfile.ZipFile(pptx_path) as z:
            slide_files = [f for f in z.namelist() if f.startswith('ppt/slides/slide') and f.endswith('.xml')]
            slide_files.sort(key=lambda x: int(re.search(r'slide(\d+)\.xml', x).group(1)))
            for i, slide in enumerate(slide_files, 1):
                xml_content = z.read(slide).decode('utf-8')
                texts = re.findall(r'<a:t>(.*?)</a:t>', xml_content)
                text_runs.append(f"\n--- Slide {i} ---")
                text_runs.extend(texts)
    except Exception as e:
        print(f'Error: {e}')
    
    with open('pptx_content.txt', 'w', encoding='utf-8') as f:
        f.write('\n'.join(text_runs))

if __name__ == '__main__':
    extract_text_from_pptx(sys.argv[1])
