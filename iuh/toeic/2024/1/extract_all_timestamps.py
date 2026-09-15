# extract_all_timestamps.py: Transcribe Part 2, 3, 4 to find exact timestamps
from faster_whisper import WhisperModel
import json

model = WhisperModel('tiny', device='cpu', compute_type='int8')

def transcribe_and_save(audio_path, out_json):
    print(f"Transcribing {audio_path}...")
    segments, info = model.transcribe(audio_path)
    data = []
    for s in segments:
        data.append({
            "start": round(s.start, 2),
            "end": round(s.end, 2),
            "text": s.text.strip()
        })
        print(f"{s.start:6.2f} - {s.end:6.2f}: {s.text.strip()}")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Saved to {out_json}")

if __name__ == "__main__":
    transcribe_and_save("web/assets/audio/part2.mp3", "part2_segments.json")
    transcribe_and_save("web/assets/audio/part3.mp3", "part3_segments.json")
    transcribe_and_save("web/assets/audio/part4.mp3", "part4_segments.json")
