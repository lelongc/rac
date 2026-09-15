import os
import sys
import json

sys.stdout.reconfigure(encoding='utf-8')

print("=== CHECKING TEST 3 DIRECTORIES & FILES ===")
# Check web/data/test3.json
t3_json = 'web/data/test3.json'
print(f"test3.json exists: {os.path.exists(t3_json)} (size: {os.path.getsize(t3_json) if os.path.exists(t3_json) else 0})")

# Check web/assets/images/test3
img_dir = 'web/assets/images/test3'
if os.path.exists(img_dir):
    imgs = os.listdir(img_dir)
    print(f"Images in {img_dir}: {len(imgs)} files")
    print("Sample images:", imgs[:15])
else:
    print(f"Directory {img_dir} does NOT exist!")

# Check web/assets/audio/test3
audio_dir = 'web/assets/audio/test3'
if os.path.exists(audio_dir):
    audios = os.listdir(audio_dir)
    print(f"Audio in {audio_dir}: {audios}")
    cuts_dir = os.path.join(audio_dir, 'cuts')
    if os.path.exists(cuts_dir):
        cuts = os.listdir(cuts_dir)
        print(f"Audio cuts in {cuts_dir}: {len(cuts)} files")
else:
    print(f"Directory {audio_dir} does NOT exist!")

# Check PDFs in root
root_files = os.listdir('.')
pdf_files = [f for f in root_files if f.endswith('.pdf')]
print("PDF files in root:", pdf_files)
