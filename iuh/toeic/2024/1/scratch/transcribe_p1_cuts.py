from faster_whisper import WhisperModel
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

model = WhisperModel("tiny", device="cpu", compute_type="int8")

for qid in range(1, 7):
    audio_path = f"web/assets/audio/test3/cuts/q{qid}.mp3"
    print(f"\n=== Q{qid} Audio Cut ({audio_path}) ===")
    if os.path.exists(audio_path):
        segments, info = model.transcribe(audio_path, beam_size=5)
        for s in segments:
            print(f"  [{s.start:.2f}-{s.end:.2f}] {s.text}")
    else:
        print("  File not found!")
