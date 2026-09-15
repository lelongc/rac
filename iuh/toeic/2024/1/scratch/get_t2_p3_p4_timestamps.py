import json
import re
from faster_whisper import WhisperModel

model = WhisperModel('tiny', device='cpu', compute_type='int8')

def extract_p3():
    print("Transcribing Test 2 Part 3...")
    segments, info = model.transcribe('web/assets/audio/test2/part3.mp3')
    segs = []
    for s in segments:
        segs.append({"start": round(s.start, 2), "end": round(s.end, 2), "text": s.text.strip()})
        txt = s.text.strip()
        if "refer to the following" in txt.lower() or "questions" in txt.lower() or "number" in txt.lower():
            print(f"{s.start:6.2f} - {s.end:6.2f}: {txt}")
    with open("scratch/t2_p3_segments.json", "w", encoding="utf-8") as f:
        json.dump(segs, f, ensure_ascii=False, indent=2)
    print("Saved scratch/t2_p3_segments.json")

def extract_p4():
    print("Transcribing Test 2 Part 4...")
    segments, info = model.transcribe('web/assets/audio/test2/part4.mp3')
    segs = []
    for s in segments:
        segs.append({"start": round(s.start, 2), "end": round(s.end, 2), "text": s.text.strip()})
        txt = s.text.strip()
        if "refer to the following" in txt.lower() or "questions" in txt.lower() or "number" in txt.lower():
            print(f"{s.start:6.2f} - {s.end:6.2f}: {txt}")
    with open("scratch/t2_p4_segments.json", "w", encoding="utf-8") as f:
        json.dump(segs, f, ensure_ascii=False, indent=2)
    print("Saved scratch/t2_p4_segments.json")

if __name__ == "__main__":
    extract_p3()
    extract_p4()
