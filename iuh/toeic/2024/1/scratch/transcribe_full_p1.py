from faster_whisper import WhisperModel
import sys

sys.stdout.reconfigure(encoding='utf-8')
model = WhisperModel("tiny", device="cpu", compute_type="int8")

segs, info = model.transcribe("web/assets/audio/test3/part1.mp3", beam_size=5)
print(f"Duration: {info.duration:.2f}s")
for s in segs:
    print(f"[{s.start:.2f} -> {s.end:.2f}] {s.text}")
