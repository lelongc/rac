from faster_whisper import WhisperModel
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

model = WhisperModel("tiny", device="cpu", compute_type="int8")

test_qs = [7, 10, 13, 22, 23, 30, 31]
for qid in test_qs:
    audio_path = f"web/assets/audio/test3/cuts/q{qid}.mp3"
    if os.path.exists(audio_path):
        segments, info = model.transcribe(audio_path, beam_size=5)
        print(f"=== Q{qid} Transcribe ===")
        for s in segments:
            print(f"  [{s.start:.2f}-{s.end:.2f}] {s.text}")
